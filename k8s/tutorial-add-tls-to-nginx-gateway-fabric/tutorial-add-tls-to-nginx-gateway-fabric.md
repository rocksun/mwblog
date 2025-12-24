<!--
title: Nginx Gateway Fabric TLS配置实战：手把手教你加固网关
cover: https://cdn.thenewstack.io/media/2025/12/0921a86c-thomas-park-20gggxxmaim-unsplash.jpg
summary: 本教程为Nginx Gateway Fabric部署添加TLS加密和HTTP到HTTPS重定向。通过Gateway API，配置证书、HTTPS监听器及RequestRedirect过滤器，实现生产级安全流量管理。
-->

本教程为Nginx Gateway Fabric部署添加TLS加密和HTTP到HTTPS重定向。通过Gateway API，配置证书、HTTPS监听器及RequestRedirect过滤器，实现生产级安全流量管理。

> 译自：[Tutorial: Add TLS to Nginx Gateway Fabric](https://thenewstack.io/tutorial-add-tls-to-nginx-gateway-fabric/)
> 
> 作者：Janakiram MSV

在[上一个教程](https://thenewstack.io/tutorial-implement-a-nginx-gateway-fabric-as-an-alternative-to-ingress/)中，我们部署了 [Nginx Gateway Fabric](https://docs.nginx.com/nginx-gateway-fabric/) 并配置了 HTTP 路由，通过 [Kubernetes Gateway API](https://thenewstack.io/cncf-retires-the-ingress-nginx-controller-for-kubernetes/) 暴露内部服务。虽然这对于开发是可用的，但生产部署需要 [TLS 加密](https://thenewstack.io/why-your-apps-biggest-performance-bottleneck-might-be-ssl-tls/) 来保护客户端和网关之间的流量。

本教程通过在网关添加 TLS 终止并实现自动 HTTP 到 HTTPS 重定向来扩展我们现有的设置。完成本教程后，您将拥有一个生产就绪的配置，可加密所有客户端流量。

## 先决条件

本教程假定您已完成[第一部分](https://thenewstack.io/tutorial-implement-a-nginx-gateway-fabric-as-an-alternative-to-ingress/)，并且运行着以下资源：

*   Nginx Gateway Fabric 部署在 nginx-gateway 命名空间中。
*   一个名为 demo-gateway 的 Gateway 资源，在端口 80 上有一个 HTTP 监听器。
*   示例应用程序 (demo-web 和 demo-api) 运行在 demo 命名空间中。
*   配置为将流量路由到后端服务的 HTTPRoute。
*   本地安装了 OpenSSL (用于证书生成)。

验证您现有的设置：

```
kubectl get gateway -n nginx-gateway
kubectl get httproute -n demo
kubectl get pods -n demo
```

## 第一步：生成 TLS 证书

在本教程中，我们将创建一个自签名证书。在生产环境中，您将使用 cert-manager 结合 Let's Encrypt 或来自您组织 CA 的证书。`12

创建目录并生成证书：

```
mkdir -p ~/gateway-certs && cd ~/gateway-certs

# Generate private key
openssl genrsa -out tls.key 2048

# Generate self-signed certificate with SAN
openssl req -new -x509 -key tls.key -out tls.crt -days 365 \
  -subj "/CN=demo.example.com" \
  -addext "subjectAltName=DNS:demo.example.com,DNS:*.demo.example.com"
```

**重要提示：** 请将 `demo.example.com` 替换为您的实际域名。现代浏览器和客户端接受证书需要主题备用名称 (SAN)。

验证证书：

```
openssl x509 -in tls.crt -text -noout | grep -A1 "Subject Alternative Name"
```

## 第二步：创建 Kubernetes TLS Secret

将证书和密钥存储在 Kubernetes secret 中。该 secret 必须与 Gateway 位于同一命名空间（nginx-gateway）中。

```
kubectl create secret tls demo-tls-secret \
  --cert=tls.crt \
  --key=tls.key \
  -n nginx-gateway
```

验证 secret：

```
kubectl describe secret demo-tls-secret -n nginx-gateway
```

您应该在 Data 部分看到 `tls.crt` 和 `tls.key`。

## 第三步：更新 Gateway 以支持 HTTPS

修改 Gateway 以在现有 HTTP 监听器旁添加一个 HTTPS 监听器。创建一个名为 `gateway-tls.yaml` 的文件：

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

关键配置元素：`tls.mode: Terminate` 设置在网关执行 TLS 终止，在通过纯 HTTP 转发到后端服务之前解密流量。`certificateRefs` 指向我们的 TLS secret。

应用更新后的 Gateway：

```
kubectl apply -f gateway-tls.yaml
```

验证两个监听器都已配置：

```
kubectl get gateway demo-gateway -n nginx-gateway -o yaml | grep -A5 "listeners:"
```

## 第四步：创建 HTTPS 路由

创建一个使用 `sectionName` 字段绑定到 HTTPS 监听器的 HTTPRoute。另存为 `route-https.yaml`：

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

应用 HTTPS 路由：

```
kubectl apply -f route-https.yaml
```

## 第五步：配置 HTTP 到 HTTPS 重定向

为确保所有流量都使用 HTTPS，请创建一个重定向路由，该路由捕获 HTTP 请求并返回 301 重定向。另存为 `http-redirect.yaml`：

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

此路由绑定到 HTTP 监听器 (`sectionName: http`) 并应用 `RequestRedirect` 过滤器，将方案更改为 HTTPS 并返回 301 永久重定向。

应用重定向路由：

```
kubectl apply -f http-redirect.yaml
```

现在您可以删除第一部分中的原始 HTTP 路由，因为所有 HTTP 流量都将被重定向：

```
kubectl delete httproute demo-route -n demo
```

## 第六步：测试 TLS 配置

首先，获取 HTTP 和 HTTPS 的 NodePort 分配：

```
kubectl get svc -n nginx-gateway
```

注意映射到 80 (HTTP) 和 443 (HTTPS) 的端口。在此示例中，我们假设 HTTP 在端口 31080 上，HTTPS 在端口 31443 上。

### 测试 HTTPS 访问

使用 curl 结合 `--resolve` 将主机名映射到您的节点 IP。`-k` 标志跳过自签名证书的验证：

```
# Test web endpoint over HTTPS
curl -k --resolve demo.example.com:31443:<NODE_IP> \
  https://demo.example.com:31443/web

# Test API endpoint over HTTPS
curl -k --resolve demo.example.com:31443:<NODE_IP> \
  https://demo.example.com:31443/api
```

### 测试 HTTP 重定向

验证 HTTP 请求是否收到 301 重定向到 HTTPS：

```
curl -I --resolve demo.example.com:31080:<NODE_IP> \
  http://demo.example.com:31080/
```

预期响应：
`HTTP/1.1 301 Moved Permanently`
`Location: https://demo.example.com/`

### 验证证书详细信息

检查网关提供的证书：

```
echo | openssl s_client -connect <NODE_IP>:31443 \
  -servername demo.example.com 2>/dev/null | \
  openssl x509 -noout -subject -dates
```

## 总结

您已成功为您的 Nginx Gateway Fabric 部署添加了 TLS 支持。最终配置包括：

*   一个带有 HTTP (端口 80) 和 HTTPS (端口 443) 监听器的 Gateway。
*   使用 Kubernetes secret 在网关处进行 TLS 终止。
*   一个用于 HTTPS 流量的 HTTPRoute，绑定到 https 监听器。
*   使用 Gateway API 的原生 RequestRedirect 过滤器实现 HTTP 到 HTTPS 的自动重定向。

本教程中创建的资源：

| **资源**     | **名称**           | **命名空间**    |
| ------------ | ------------------ | --------------- |
| Secret       | demo-tls-secret    | nginx-gateway   |
| Gateway      | demo-gateway (已更新) | nginx-gateway   |
| HTTPRoute    | demo-route-https   | demo            |
| HTTPRoute    | http-to-https-redirect | demo            |

## 生产环境建议

对于生产部署，请使用 cert-manager 自动化证书管理来替换自签名证书：

```
# Install cert-manager
kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.14.0/cert-manager.yaml
```

为 Let’s Encrypt 创建一个 ClusterIssuer，并为您的 Gateway 添加注解以自动配置证书。有关 Gateway API 集成详情，请参阅 cert-manager 文档。

**额外的安全强化：**

*   使用 Prometheus 指标监控证书过期。
*   使用 Nginx Gateway Fabric 的策略资源实现 HSTS 标头。
*   为不同的域名或环境使用独立的证书。
*   证书至少每年轮换一次，最好通过自动化更频繁地轮换。

## 展望未来

本教程演示了如何通过 TLS 终止和自动 HTTP 重定向来保护您的 Gateway API 实现。Gateway API 对这些模式的本地支持——通过 `tls.mode: Terminate` 和 `RequestRedirect` 过滤器——消除了 Ingress 配置中困扰已久的供应商特定注解的需求。

在后续教程中，我们将探索高级流量管理模式，包括带流量拆分的金丝雀部署、基于标头的 A/B 测试路由、速率限制和请求节流，以及多租户集群的跨命名空间路由。

您在此处构建的安全基础——包括适当的 TLS 终止和重定向处理——是这些生产场景必不可少的基础工作。敬请关注！