# Opa Gatekeeper: How To Write Policies For Kubernetes Clusters
Learn how to leverage OPA Gatekeeper to write and enforce policies in Kubernetes clusters, ensuring security and efficient resource management in your environment.

### Table Of Contents
-
[What is Open Policy Agent (OPA)?](#what-is-open-policy-agent-opa) -
[How OPA And Kubernetes Work Together?](#how-opa-and-kubernetes-work-together) -
[What is OPA Gatekeeper?](#what-is-opa-gatekeeper) -
[Writing Policies In Kubernetes Clusters With OPA Gateway](#what-is-opa-gatekeeper) -
[Summary and Conclusion](#summary-and-conclusion)
Due to the presence of tools like kubernetes, it is easier to manage and automate the daily working processes of a microservices environment.

Using policies in your kubernetes will give you maximum control and flexibility especially in areas such as:

- Improving the security of your microservices
- Active management of limited resources in your cloud infrastructure
- Compliance and governance with regulatory laws
By reading this article you will learn:

- The benefits of using policies in securing kubernetes environment.
- How to set up a system for dispensing policies; how kubernetes and OPA work behind the scenes.
- Everything you need to get started writing and running policies within your cluster.
## What is Open Policy Agent (OPA)?
[Open Policy Agent (OPA)](https://www.openpolicyagent.org/) helps us write policy as code using Rego, a declarative language designed specifically for this reason.
With OPA, we can define and enforce policies across various layers of the stack, from kubernetes to microservices.

This approach contributes to consistency, scalability, and agility in managing policies within your kubernetes clusters.

In addition, by using an expressive syntax you can efficiently represent access control rules and complex policy decisions that your organization reaches.

Altogether, this goes a long way to make sure that your kubernetes environment is compliant and secure.

The focus of this article is on writing policies in kubernetes setup.

If you are not familiar with OPA, you can quickly learn more about how it works and implementation details in [this article ](https://permify.co/post/implementing-opa/)

## How OPA And Kubernetes Work Together?
In this section, let us dive a bit more into how you can get Open Policy Agent (OPA) up and running.

Good enough, OPA provides good support for kubernetes as reflected in its documentation so we shall look into how you can integrate it into your kubernetes environment.

But first things first, let's talk about some important components and understand how it works ‘behind the scenes’.

Kubernetes ships with what is called an admission controller. It's a piece of code that acts like a middleman between the kubernetes API itself and any request sent.

Admission controllers can also be used to enforce policies and security measures, making sure that only authorized and properly configured workloads are allowed into the cluster.

They may alter requests to ensure that it is of valid and acceptable form before processing takes place.

So, admission controllers can be of two types: mutating or validating. It's important to understand this aspect as this is where Open Policy Agent (OPA) plugs in.

As to why we need admission controllers in our cluster, [the official kubernetes documentation](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) has this to say:

"...a Kubernetes API server that is not properly configured with the right set of admission controllers is an incomplete server and will not support all the features you expect..."

In essence, you may choose to use Open Policy Agent (OPA) or write your own custom admission controller, depending on the scope of customizations you are planning to achieve in your kubernetes environment.

## What is OPA Gatekeeper?
A kubernetes setup is barely complete without an admission controller. [OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper) is one such controller that checks any request coming into the kubernetes API.

Gatekeeper intercepts the request and checks with predefined policies. Based on this check, a request can be denied or granted.

From the illustration above, we see the workflow of how OPA gatekeeper **reviews** any request that comes into the kubernetes API server.

It also constantly **watches** for any changes in the elements of the API server such as the pods and services.

So in essence, when you install gatekeeper on kubernetes environment, you can write policies and have them take effect in the cluster. We will see more of this in a bit.

## Writing Policies In Kubernetes Clusters With OPA Gateway
To further understand the benefits and integration scope of OPA gatekeeper in kubernetes, we will cover the following use cases throughout this piece:

This 2-part tutorial will take you step by step through the entire process of how to write and test policies using Open Policy Agent (OPA) in your kubernetes cluster.

In the first part, we'll make use of OPA gatekeeper admission controller to enforce the policies we write, and then, in the second part we shall write our own custom validating controller.

Thus, by the end of this guide you'll have:

- Gained knowledge of how OPA policies work within a kubernetes set up
- How to write and apply your own policies
- A better understanding of the admission controller webhook in Kubernetes; the workflow and how to implement your own validating controller.
**Prerequisites**
To benefit fully from this practical guide, you need to have the following set up in your local machine:

- Ensure you have
[OPA](https://www.openpolicyagent.org/docs/latest/#1-download-opa)installed - Minikube : Ensure you have
[Minikube](https://minikube.sigs.k8s.io/docs/start/)and a running Kubernates cluster [kubectl:](https://kubernetes.io/docs/tasks/tools/#kubectl)Ensure you have`kubectl`
configured to interact with your cluster.- OPA gatekeeper : Ensure
[OPA Gatekeeper is installed in your cluster.](https://open-policy-agent.github.io/gatekeeper/website/docs/install#installation) - Docker and
[DockerHub](https://hub.docker.com/signup)account
Let's get right into it.

### 1. Defining namespaces policies
For this usecase, let's write an OPA policy that states that every namespace create request should have an annotation added to it.

**Step I:** Create a constraint template file
A ConstraintTemplate defines the structure and logic of the policy. This template will enforce that every namespace must have the `team`
annotation.
```
apiVersion: templates.gatekeeper.sh/v1beta1
kind: ConstraintTemplate
metadata:
name: k8srequiredannotations
spec:
crd:
spec:
names:
kind: K8sRequiredAnnotations
targets:
- target: admission.k8s.gatekeeper.sh
rego: |
package k8srequiredannotations
violation[{"msg": msg}] {
input.review.kind.kind == "Namespace"
not input.review.object.metadata.annotations["team"]
msg := "Namespace must have an annotation 'team'"
}
```
Save this YAML to a file named `constrainttemplate.yaml`
then apply it to your cluster:

`kubectl apply -f constrainttemplate.yaml`
**Step II:** Create a constraint file
A Constraint uses the ConstraintTemplate to enforce the policy on specific resources—in this case, namespaces.

```
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sRequiredAnnotations
metadata:
name: require-team-annotation
spec:
match:
kinds:
- apiGroups: [""]
kinds: ["Namespace"]
```
Save this YAML to a file named `constraint.yaml`
and also apply it to your cluster:

`kubectl apply -f constraint.yaml`
**Step III:** Verify the policy
To verify that the policy is working, try creating a namespace without the team annotation. It should be denied.

```
apiVersion: v1
kind: Namespace
metadata:
name: demo-namespace
```
Save this YAML to a file named `demo-namespace.yaml`
and apply it:

`kubectl apply -f demo-namespace.yaml`
As expected, we get an error response:

Now let's comply with the policy by creating a namespace with the `team`
annotation.

```
apiVersion: v1
kind: Namespace
metadata:
name: test-namespace
annotations:
team: "devops"
```
Save the above YAML file as `test-namespace-with-annotation.yaml`
and apply it to the cluster.

This time, it creates the namespace successfully.

### 2. Allocating resources quotas
Next, we want to write a bit more advanced policy that states that namespaces labelled with `env:production`
must have a resource quota applied to them.

Such a policy can be helpful when you want to control or monitor usage of resources and make things more efficient. Let's get started.

**Step I:** Create the constraint template file
This template will check if namespaces labeled with `env: production`
have a resource quota.

```
apiVersion: templates.gatekeeper.sh/v1beta1
kind: ConstraintTemplate
metadata:
name: k8srequiredresourcequotas
spec:
crd:
spec:
names:
kind: K8sRequiredResourceQuotas
targets:
- target: admission.k8s.gatekeeper.sh
rego: |
package k8srequiredresourcequotas
violation[{"msg": msg}] {
input.review.kind.kind == "Namespace"
namespace := input.review.object
some label_key
namespace.metadata.labels[label_key] == "production"
not has_resource_quota(namespace.metadata.name)
msg := sprintf("Namespace labeled 'env: production' must have a resource quota", [])
}
has_resource_quota(namespace_name) {
some i
input.review.context.related[i].kind == "ResourceQuota"
input.review.context.related[i].metadata.namespace == namespace_name
}
```
Save this YAML to a file named `constrainttemplate.yaml`
and apply it to your cluster:

`kubectl apply -f constrainttemplate.yaml`
**Step II:** Create a constraint file
```
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sRequiredResourceQuotas
metadata:
name: require-resource-quota-for-production
spec:
match:
kinds:
- apiGroups: [""]
kinds: ["Namespace"]
```
Save this YAML to a file named `constraint.yaml`
and apply it to your cluster:

`kubectl apply -f constraint.yaml`
**Step III:** Verify the policy
To verify that the policy works, let's create a simple test namespace with the production label but without specifying any resource quotas. It should be rejected.
```
apiVersion: v1
kind: Namespace
metadata:
name: test-namespace-production-no-quota
labels:
env: production
```
Save this YAML to a file `test-namespace-production-no-quota.yaml`
and apply it:

```
kubectl apply -f test-namespace-production-no-quota.yaml
```
As expected, we get an error response when we try to create a namespace, saying that we must assign a quota just like it is stated in our policy file:

Awesome. Let's go ahead and assign a quota for our namespace.

```
apiVersion: v1
kind: ResourceQuota
metadata:
name: resource-quota
namespace: default
spec:
hard:
requests.cpu: "1"
requests.memory: 1Gi
limits.cpu: "2"
limits.memory: 2Gi
```
Save this YAML to a file named `resource-quota.yaml`
and apply it:

`kubectl apply -f resource-quota.yaml`
After applying as shown above, the namespace creation and quota application is successful.

You can also go further to actually check the assigned quota for the namespace with the command:

`kubectl get resourcequotas -n default`
Thus far, we have seen how OPA gatekeeper acts as middleman or interceptor whenever we want to perform specific actions in kubernetes.

Let's now move to the final part, which is creating our own custom validation webhook.

### 3. Writing a custom controller
To begin, create and switch to a seperate folder specifically for this entire drill, you can call it `webhook_server.`

**1**. Start the Minikube cluster.
`minikube start`
**2**. Write the validating logic for the webhook. We'll write this in Python but it can also be written in any other language of choice.
Create a file `app.py`
and copy the following contents.
```
from flask import Flask, request, jsonify
import logging
app = Flask(__name__)
logger = logging.getLogger(__name__)
@app.route('/validate', methods=['POST'])
def validate_pod():
try:
admission_review = request.get_json()
pod_spec = admission_review['request']['object']['spec']
# Add your validation logic here
# Example: Check if the pod has a specific label
labels = pod_spec.get('labels', {})
if 'app' not in labels:
logger.error("Pod validation failed: Missing 'app' label")
return jsonify({"response": {"allowed": False, "status": {"reason": "MissingAppLabel"}}}), 200
# If all validation checks pass
logger.info("Pod validation succeeded")
return jsonify({"response": {"allowed": True}}), 200
except Exception as e:
logger.exception("An error occurred during pod validation")
return jsonify({"response": {"allowed": False, "status": {"reason": "InternalServerError"}}}), 500
if __name__ == '__main__':
# Configure logging
logging.basicConfig(level=logging.INFO)
# Start the Flask app
app.run(host='0.0.0.0', port=8080, debug=False)
```
**3.** We need to containerize this webhook server, build and push it to a DockerHub repository.
I. Create a repository on your Dockerhub account.
II. Create a Dockerfile in the folder with the following contents:
` touch Dockerfile`
```
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
CMD [ "python", "app.py" ]
```
III. Build the image
`docker build -t your-username/repository-name:latest .`

IV. Push it to DockerHub

` docker login`
```
docker tag <repository-name>:latest your-username/repository-name:latest
docker push your-username/repository-name:latest
```
Now, the image should be live on Dockerhub. This means we can now use it in our deployment yaml file.

💡**Troubleshooting tip:** if you experience request denied errors while pushing your docker image to DockerHub, ensure to login to docker on terminal, double check for any typos or mismatch in the image name, repository name and tagname.

**4**. Generate TLS Certificates. This helps to secure communication between our webhook server and kubernetes. It is a crucial step to pay attention to. If not properly configured, you might end up getting TLS errors down the line.
```
openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -nodes -subj "/CN=pod-validation-webhook.default.svc"
```
```
kubectl create secret tls pod-validation-webhook-tls --cert=server.crt --key=server.key -n default
```
**5.** Create the deployment YAML file.
`touch webhook-deployment.yaml`
```
apiVersion: apps/v1
kind: Deployment
metadata:
name: pod-validation-webhook
namespace: default
spec:
replicas: 1
selector:
matchLabels:
app: pod-validation-webhook
template:
metadata:
labels:
app: pod-validation-webhook
spec:
containers:
- name: cweb
image: cannarron/cweb:latest
ports:
- containerPort: 8080
volumeMounts:
- name: tls-certs
mountPath: /etc/webhook/certs
readOnly: true
volumes:
- name: tls-certs
secret:
secretName: pod-validation-webhook-tls
```
**6.** Create a service
We need to create a kubectl service resource to point back to our Python webhook server
`touch webhook-service.yaml`
```
apiVersion: v1
kind: Service
metadata:
name: pod-validation-webhook
spec:
selector:
app: pod-validation-webhook
ports:
- protocol: TCP
port: 8080
targetPort: 8080
```
**7.** Create the validation configuration file.
The validation configuration file is what officially registers our webhook as part of the kubernetes API. In other words, kubernetes will be aware that there's a new middleman that should be called whenever a pod creation request is sent.
`touch validating-webhook-config.yaml`
```
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
name: pod-validation-webhook
webhooks:
- name: pod.validation.example.com
clientConfig:
service:
name: pod-validation-webhook
namespace: default
path: "/validate"
caBundle: <base64 encoded ca.crt>
admissionReviewVersions:
- v1
sideEffects: None
timeoutSeconds: 5
failurePolicy: Fail
matchPolicy: Equivalent
rules:
- apiGroups: [""]
apiVersions: ["v1"]
operations: ["CREATE", "UPDATE"]
resources: ["pods"]
```
**8.** Apply manifest files; Let's apply the deployment, service and validation configuration files YAML we have created in the earlier steps.
```
kubectl apply -f webhook-deployment.yaml
kubectl apply -f webhook-service.yaml
kubectl apply -f validating-webhook-config.yaml
```
**9.** Verify.
Finally if the deployment goes well, then you should see the pod running successfully. And the validation webhook should be active as well
To verify that our validation hook is now active, based on the validation rules set in the webhook, we simply create a test pod without a label which request should be denied.
## Summary and Conclusion
In this comprehensive guide, we have talked about using policies in kubernetes to extend its features and add custom enhancements or team preferences. We have also gone through step by step on implementing kubernetes policies with practical usecases.

Using policies in your kubernetes setup is a creative way to fully explore the capabilities within your containerized deployments and make it more secure.