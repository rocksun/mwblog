In the [previous tutorial](https://thenewstack.io/tutorial-implement-a-nginx-gateway-fabric-as-an-alternative-to-ingress/), we deployed [Nginx Gateway Fabric](https://docs.nginx.com/nginx-gateway-fabric/) and configured HTTP routing to expose internal services through the [Kubernetes Gateway API](https://thenewstack.io/cncf-retires-the-ingress-nginx-controller-for-kubernetes/). While functional for development, production deployments require [TLS encryption](https://thenewstack.io/why-your-apps-biggest-performance-bottleneck-might-be-ssl-tls/) to secure traffic between clients and the gateway.

This tutorial extends our existing setup by adding TLS termination at the gateway and implementing automatic HTTP to HTTPS redirection. By the end, you’ll have a production-ready configuration that encrypts all client traffic.

## Prerequisites

This tutorial assumes you have completed [Part 1](https://thenewstack.io/tutorial-implement-a-nginx-gateway-fabric-as-an-alternative-to-ingress/) and have the following resources running:

* Nginx Gateway Fabric deployed in the nginx-gateway namespace.
* A Gateway resource named demo-gateway with an HTTP listener on port 80.
* Sample application (demo-web and demo-api) running in the demo namespace.
* HTTPRoute configured to route traffic to the backend services.
* OpenSSL installed locally (for certificate generation).

Verify your existing setup:

```
kubectl get gateway -n nginx-gateway
kubectl get httproute -n demo
kubectl get pods -n demo
```

## Step 1: Generate TLS Certificates

For this tutorial, we’ll create a self-signed certificate. In production, you would use cert-manager with Let’s Encrypt or certificates from your organization’s CA.`12

Create a directory and generate the certificate:

```
mkdir -p ~/gateway-certs &amp;&amp; cd ~/gateway-certs

# Generate private key
openssl genrsa -out tls.key 2048

# Generate self-signed certificate with SAN
openssl req -new -x509 -key tls.key -out tls.crt -days 365 \
  -subj "/CN=demo.example.com" \
  -addext "subjectAltName=DNS:demo.example.com,DNS:*.demo.example.com"
```

**Important:** Replace `demo.example.com` with your actual domain. The Subject Alternative Name (SAN) is required for modern browsers and clients to accept the certificate.

Verify the certificate:

```
openssl x509 -in tls.crt -text -noout | grep -A1 "Subject Alternative Name"
```

## Step 2: Create the Kubernetes TLS Secret

Store the certificate and key in a Kubernetes secret. The secret must reside in the same namespace as the Gateway (nginx-gateway).

```
kubectl create secret tls demo-tls-secret \
  --cert=tls.crt \
  --key=tls.key \
  -n nginx-gateway
```

Verify the secret:

```
kubectl describe secret demo-tls-secret -n nginx-gateway
```

You should see `tls.crt` and `tls.key` listed in the Data section.

## Step 3: Update the Gateway for HTTPS

Modify the Gateway to add an HTTPS listener alongside the existing HTTP listener. Create a file named `gateway-tls.yaml`:

```
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: demo-gateway
  namespace: nginx-gateway
spec:
  gatewayClassName: nginx
  listeners:
    # Existing HTTP listener - kept for redirect
    - name: http
      port: 80
      protocol: HTTP
      hostname: demo.example.com
      allowedRoutes:
        namespaces:
          from: All
    # New HTTPS listener with TLS termination
    - name: https
      port: 443
      protocol: HTTPS
      hostname: demo.example.com
      tls:
        mode: Terminate
        certificateRefs:
          - kind: Secret
            name: demo-tls-secret
      allowedRoutes:
        namespaces:
          from: All
```

Key configuration elements: The `tls.mode: Terminate` setting performs TLS termination at the gateway, decrypting traffic before forwarding to backend services over plain HTTP. The `certificateRefs` points to our TLS secret.

Apply the updated Gateway:

```
kubectl apply -f gateway-tls.yaml
```

Verify both listeners are configured:

```
kubectl get gateway demo-gateway -n nginx-gateway -o yaml | grep -A5 "listeners:"
```

## Step 4: Create the HTTPS Route

Create an HTTPRoute that binds to the HTTPS listener using the `sectionName` field. Save as `route-https.yaml`:

```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: demo-route-https
  namespace: demo
spec:
  parentRefs:
    - name: demo-gateway
      namespace: nginx-gateway
      sectionName: https
  hostnames:
    - demo.example.com
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api
      backendRefs:
        - name: demo-api
          port: 80
    - matches:
        - path:
            type: PathPrefix
            value: /
      backendRefs:
        - name: demo-web
          port: 80
```

Apply the HTTPS route:

```
kubectl apply -f route-https.yaml
```

## Step 5: Configure HTTP to HTTPS Redirect

To ensure all traffic uses HTTPS, create a redirect route that captures HTTP requests and returns a 301 redirect. Save as `http-redirect.yaml`:

```
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: http-to-https-redirect
  namespace: demo
spec:
  parentRefs:
    - name: demo-gateway
      namespace: nginx-gateway
      sectionName: http
  hostnames:
    - demo.example.com
  rules:
    - filters:
        - type: RequestRedirect
          requestRedirect:
            scheme: https
            statusCode: 301
```

This route binds to the HTTP listener (`sectionName: http`) and applies a `RequestRedirect` filter that changes the scheme to HTTPS and returns a 301 permanent redirect.

Apply the redirect route:

```
kubectl apply -f http-redirect.yaml
```

You can now delete the original HTTP route from Part 1 since all HTTP traffic will be redirected:

```
kubectl delete httproute demo-route -n demo
```

## Step 6: Test the TLS Configuration

First, get the NodePort assignments for HTTP and HTTPS:

```
kubectl get svc -n nginx-gateway
```

Note the ports mapped to 80 (HTTP) and 443 (HTTPS). For this example, we’ll assume HTTP is on port 31080 and HTTPS is on port 31443.

### Test HTTPS Access

Use curl with `--resolve` to map the hostname to your node IP. The `-k` flag skips certificate verification for self-signed certs:

```
# Test web endpoint over HTTPS
curl -k --resolve demo.example.com:31443:&lt;NODE_IP&gt; \
  https://demo.example.com:31443/web

# Test API endpoint over HTTPS
curl -k --resolve demo.example.com:31443:&lt;NODE_IP&gt; \
  https://demo.example.com:31443/api
```

### Test HTTP Redirect

Verify that HTTP requests receive a 301 redirect to HTTPS:

```
curl -I --resolve demo.example.com:31080:&lt;NODE_IP&gt; \
  http://demo.example.com:31080/
```

Expected response:  
 `HTTP/1.1 301 Moved Permanently  
Location: https://demo.example.com/`

### Verify Certificate Details

Inspect the certificate being served by the gateway:

```
echo | openssl s_client -connect &lt;NODE_IP&gt;:31443 \
  -servername demo.example.com 2&gt;/dev/null | \
  openssl x509 -noout -subject -dates
```

## Summary

You have successfully added TLS support to your Nginx Gateway Fabric deployment. The final configuration includes:

* A Gateway with both HTTP (port 80) and HTTPS (port 443) listeners.
* TLS termination at the gateway using a Kubernetes secret.
* An HTTPRoute for HTTPS traffic bound to the https listener.
* Automatic HTTP to HTTPS redirect using the Gateway API’s native RequestRedirect filter.

Resources created in this tutorial:

| **Resource** | **Name** | **Namespace** |
| --- | --- | --- |
| Secret | demo-tls-secret | nginx-gateway |
| Gateway | demo-gateway (updated) | nginx-gateway |
| HTTPRoute | demo-route-https | demo |
| HTTPRoute | http-to-https-redirect | demo |

## Production Recommendations

For production deployments, replace self-signed certificates with automated certificate management using cert-manager:

```
# Install cert-manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.14.0/cert-manager.yaml
```

Create a ClusterIssuer for Let’s Encrypt and annotate your Gateway to automatically provision certificates. Refer to the cert-manager documentation for Gateway API integration details.

**Additional security hardening:**

* Monitor certificate expiration with [Prometheus](https://thenewstack.io/opentelemetry-adoption-update-rust-prometheus-and-other-speed-bumps/) metrics.
* Implement HSTS headers using Nginx Gateway Fabric’s policy resources.
* Use separate certificates for different domains or environments.
* Rotate certificates at least annually, preferably more frequently with automation.

## Looking Ahead

This tutorial demonstrated how to secure your Gateway API implementation with TLS termination and automatic HTTP redirects. The Gateway API’s native support for these patterns — through `tls.mode: Terminate` and `RequestRedirect` filters — eliminates the need for vendor-specific annotations that plagued Ingress configurations.

In subsequent tutorials, we’ll explore advanced traffic management patterns including canary deployments with traffic splitting, header-based routing for A/B testing, rate limiting and request throttling, and cross-namespace routing for multi-tenant clusters.

The secure foundation you’ve built here — with proper TLS termination and redirect handling — is essential groundwork for these production scenarios. Stay tuned!

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/05/de43524e-janakiram-msv.jpg)

Janakiram MSV is the principal analyst at Janakiram & Associates and an adjunct faculty member at the International Institute of Information Technology. He is also a Google Qualified Cloud Developer, an Amazon Certified Solution Architect, an Amazon Certified Developer, an...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)