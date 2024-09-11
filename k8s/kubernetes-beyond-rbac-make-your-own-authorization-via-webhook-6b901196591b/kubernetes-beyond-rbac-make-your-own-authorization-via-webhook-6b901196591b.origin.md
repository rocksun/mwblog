# Kubernetes Beyond RBAC - Make Your Own Authorization via Webhook
[https://kubernetes.io](https://kubernetes.io)
Kubernetes is a great container orchestration tool that gives you a lot of customization options. You can easily extend/replace many of its components like CNI, CSI, scheduler or even authorization components.

In this article, you will see how to write your own authorization webhook that works on Kubernetes to extend RBAC functionalities or remove it at all.

We will take a look at the following topics:

- Kubernetes Authorization Flow

- Configuring Kubernetes API Server for Authorization Webhook
- What an Authorization Request Looks Like
- Writing Authorization Webhook
- Generating Self Signed Certificate
- What About Kubectl Auth
- Show Time - Running All
- Where to Use
- References
## Kubernetes Authorization Flow
Let’s start with explaining the internal authorization flow of Kubernetes.

[https://kubernetes.io/docs/concepts/security/controlling-access/](https://kubernetes.io/docs/concepts/security/controlling-access/)
A request that arrives at the API server goes through the flow shown in the above image.

Every request that goes to Kubernetes cluster is authenticated by the API server, and then a couple of authorization flows start. After that authorization flow, the API server calls admission control webhooks. Finally, if everything goes well, the request will be accomplished by querying or modifying the state of etcd.

Thanks to the extensible architecture of Kubernetes, we can extend every step described above. We can integrate our custom authentication solutions. We can write our own authorization server. Or we can interfere with every resource creation or modification.

If you would like to learn authorization using RBAC in Kubernetes please take a look my previous article about configuring RBAC 👇

## Configuring Kubernetes API Server for Authorization Webhook
You need to configure the API server to specify your authorization webhook address.

Personally, I am using Kind to test Kubernetes locally. The following configuration enables Webhook authorization on the API server for Kubernetes. Let’s put this configuration in a file named “kind-cp.yaml”.

`kind: Cluster`
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
extraMounts:
- hostPath: /Users/emre.savci/Desktop/kube-authz
containerPath: /files
kubeadmConfigPatches:
- |
kind: ClusterConfiguration
apiServer:
extraArgs:
enable-admission-plugins: NodeRestriction,MutatingAdmissionWebhook,ValidatingAdmissionWebhook
authorization-mode: Webhook, RBAC
authorization-webhook-version: v1
authorization-webhook-config-file: /files/authz-webhook.yaml
authorization-webhook-cache-authorized-ttl: 120s
authorization-webhook-cache-unauthorized-ttl: 30s
extraVolumes:
- name: api-server-basic-auth-files
hostPath: "/files"
mountPath: "/files"
readOnly: true
If you take a closer look at the configuration file, you will face authorization-related arguments.

The following line specifies that our authorization mode uses both native RBAC and our custom-written authorization webhook:

`authorization-mode: Webhook, RBAC`
The following line specifies the configuration file of our authorization webhook:

`authorization-webhook-config-file: /files/authz-webhook.yaml`
Here is our authorization webhook configuration file:

`clusters:`
- name: my-cluster
cluster:
certificate-authority: /files/webhook.crt
server: https://authz-webhook/authorize
users:
- name: api-server
user:
token: test-token
current-context: my-cluster
contexts:
- context:
cluster: my-cluster
user: api-server
name: my-cluster
Now we can create a cluster using those configurations.

`kind create cluster --retain --config kind-cp.yaml`
## What an Authorization Request Looks Like
Before writing a custom authorization webhook, let’s take a look at authorization request that send by Kubernetes.

You can always define a custom type for incoming requests but thanks to Kubernetes api we have that request type for Golang.

We can install the Kubernetes api package by the following command:

`go get "k8s.io/api/authorization/v1"`
After that, we have our authorization request object: `SubjectAccessReview`
.

`// SubjectAccessReview checks whether or not a user or group can perform an action.`
type SubjectAccessReview struct {
metav1.TypeMeta `json:",inline"`
// Standard list metadata.
// More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
// +optional
metav1.ObjectMeta `json:"metadata,omitempty" protobuf:"bytes,1,opt,name=metadata"`
// Spec holds information about the request being evaluated
Spec SubjectAccessReviewSpec `json:"spec" protobuf:"bytes,2,opt,name=spec"`
// Status is filled in by the server and indicates whether the request is allowed or not
// +optional
Status SubjectAccessReviewStatus `json:"status,omitempty" protobuf:"bytes,3,opt,name=status"`
}
In this struct we have two important fields:

`SubjectAccessReviewSpec`
: It contains request details like resource attributes and user group information.
In this type there are two important fields: **ResourceAttributes** and **NonResourceAttributes**.

**ResourceAttributes: **This field is non-nil when access is requested to a Kubernetes resource like pod, service, etc.
**NonResourceAttributes: **This field is non-nil when you try to check permissions via **kubectl auth can-i**.
`// SubjectAccessReviewSpec is a description of the access request. Exactly one of ResourceAuthorizationAttributes`
// and NonResourceAuthorizationAttributes must be set
type SubjectAccessReviewSpec struct {
// ResourceAuthorizationAttributes describes information for a resource access request
// +optional
ResourceAttributes *ResourceAttributes `json:"resourceAttributes,omitempty" protobuf:"bytes,1,opt,name=resourceAttributes"`
// NonResourceAttributes describes information for a non-resource access request
// +optional
NonResourceAttributes *NonResourceAttributes `json:"nonResourceAttributes,omitempty" protobuf:"bytes,2,opt,name=nonResourceAttributes"`
// User is the user you're testing for.
// If you specify "User" but not "Groups", then is it interpreted as "What if User were not a member of any groups
// +optional
User string `json:"user,omitempty" protobuf:"bytes,3,opt,name=user"`
// Groups is the groups you're testing for.
// +optional
Groups []string `json:"groups,omitempty" protobuf:"bytes,4,rep,name=groups"`
// Extra corresponds to the user.Info.GetExtra() method from the authenticator. Since that is input to the authorizer
// it needs a reflection here.
// +optional
Extra map[string]ExtraValue `json:"extra,omitempty" protobuf:"bytes,5,rep,name=extra"`
// UID information about the requesting user.
// +optional
UID string `json:"uid,omitempty" protobuf:"bytes,6,opt,name=uid"`
}
`// ResourceAttributes includes the authorization attributes available for resource requests to the Authorizer interface`
type ResourceAttributes struct {
// Namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces
// "" (empty) is defaulted for LocalSubjectAccessReviews
// "" (empty) is empty for cluster-scoped resources
// "" (empty) means "all" for namespace scoped resources from a SubjectAccessReview or SelfSubjectAccessReview
// +optional
Namespace string `json:"namespace,omitempty" protobuf:"bytes,1,opt,name=namespace"`
// Verb is a kubernetes resource API verb, like: get, list, watch, create, update, delete, proxy. "*" means all.
// +optional
Verb string `json:"verb,omitempty" protobuf:"bytes,2,opt,name=verb"`
// Group is the API Group of the Resource. "*" means all.
// +optional
Group string `json:"group,omitempty" protobuf:"bytes,3,opt,name=group"`
// Version is the API Version of the Resource. "*" means all.
// +optional
Version string `json:"version,omitempty" protobuf:"bytes,4,opt,name=version"`
// Resource is one of the existing resource types. "*" means all.
// +optional
Resource string `json:"resource,omitempty" protobuf:"bytes,5,opt,name=resource"`
// Subresource is one of the existing resource types. "" means none.
// +optional
Subresource string `json:"subresource,omitempty" protobuf:"bytes,6,opt,name=subresource"`
// Name is the name of the resource being requested for a "get" or deleted for a "delete". "" (empty) means all.
// +optional
Name string `json:"name,omitempty" protobuf:"bytes,7,opt,name=name"`
}
`SubjectAccessReviewStatus`
: This field contains authorization response for the request is wether allowed or denied.
`// SubjectAccessReviewStatus`
type SubjectAccessReviewStatus struct {
// Allowed is required. True if the action would be allowed, false otherwise.
Allowed bool `json:"allowed" protobuf:"varint,1,opt,name=allowed"`
// Denied is optional. True if the action would be denied, otherwise
// false. If both allowed is false and denied is false, then the
// authorizer has no opinion on whether to authorize the action. Denied
// may not be true if Allowed is true.
// +optional
Denied bool `json:"denied,omitempty" protobuf:"varint,4,opt,name=denied"`
// Reason is optional. It indicates why a request was allowed or denied.
// +optional
Reason string `json:"reason,omitempty" protobuf:"bytes,2,opt,name=reason"`
// EvaluationError is an indication that some error occurred during the authorization check.
// It is entirely possible to get an error and be able to continue determine authorization status in spite of it.
// For instance, RBAC can be missing a role, but enough roles are still present and bound to reason about the request.
// +optional
EvaluationError string `json:"evaluationError,omitempty" protobuf:"bytes,3,opt,name=evaluationError"`
}
For more detailed explanation you can take a look to [Kubernetes Subject Access Review](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/subject-access-review-v1/).

## Writing Authorization Webhook
Do not fear from the title. It is a dead simple thing to create an authorization webhook. Actually, a webhook is a simple HTTP server.

Here is a simple authorization webhook that allows **list and get** operations but forbids **delete** operation for the service account named “test-user”:

`package main`
import (
"fmt"
"github.com/gofiber/fiber/v2"
authorizationv1 "k8s.io/api/authorization/v1"
)
func main() {
app := fiber.New()
app.Post("/authorize", func(ctx *fiber.Ctx) error {
var req authorizationv1.SubjectAccessReview
ctx.BodyParser(&req)
req.Status.Allowed = true
if req.Spec.User == "system:serviceaccount:default:test-user" {
if req.Spec.ResourceAttributes != nil {
if req.Spec.ResourceAttributes.Verb == "get" || req.Spec.ResourceAttributes.Verb == "list" {
req.Status.Allowed = true
}
if req.Spec.ResourceAttributes.Verb == "delete" {
req.Status.Allowed = false
}
}
if req.Spec.NonResourceAttributes != nil {
if req.Spec.NonResourceAttributes.Verb == "get" || req.Spec.NonResourceAttributes.Verb == "list" {
req.Status.Allowed = true
}
if req.Spec.NonResourceAttributes.Verb == "delete" {
req.Status.Allowed = false
}
}
}
return ctx.JSON(req)
})
app.Get("/healthz", func(ctx *fiber.Ctx) error {
fmt.Println("healthz")
return ctx.SendStatus(200)
})
if err := app.ListenTLS(":443", "/app/webhook.crt", "/app/webhook.key"); err != nil {
fmt.Println(err)
}
}
The following configuration is for our authorization webhook. It specifies our webhook server address and certificate authority.

`clusters:`
- name: devx-webhooks
cluster:
certificate-authority: /files/webhook.crt
server: https://devx-webhooks/authorize
users:
- name: api-server
user:
token: test-token
current-context: devx-webhooks
contexts:
- context:
cluster: devx-webhooks
user: api-server
name: devx-webhooks
Let’s run our webhook. Remember that we run our Kubernetes cluster via kind, we will run webhook with Docker in **kind** network.

`docker build -t go-kube-authz .`
docker run -it -d --name devx-webhooks --network kind -p 443:443 go-kube-authz
## Webhook Self Signed Certificate
We need to create a self signed certificate for the api-server to communicate securely with our webhook. We will use the generated webhook.cert and webhook.key in our authorization webhook server. Also we will pass webhook.cert to Kubernete api server in the webhook configuration file.

`openssl genrsa -out webhook.key 2048`
Let’s create a file named **webook.csr.cnf** and put following configuration in it:

`[req]`
default_bits = 2048
prompt = no
default_md = sha256
distinguished_name = dn
req_extensions = req_ext
[dn]
CN = devx-webhooks
[req_ext]
subjectAltName = @alt_names
[alt_names]
DNS.1 = devx-webhooks
`openssl req -new -key webhook.key -out webhook.csr -config webhook.csr.cnf`
Now create another file named and put following lines in

`authorityKeyIdentifier=keyid,issuer`
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names
[alt_names]
DNS.1 = devx-webhooks
`openssl x509 -req -in webhook.csr -signkey webhook.key -out webhook.crt -days 365 -extfile webhook.ext`
Our webhook.key and webhook.cert files are ready to use now 🚀

## What About kubectl Auth
As most of you know, there is a kubectl command called `auth.`
With the help of this command, you can check whether a ServiceAccount or your current `kubeconfig`
setting has access to specific resources on Kubernetes.

The basic usage of the auth command is like below:

`kubectl auth can-i get pods/logs`
Simply, it gives answers to the authorization questions. There is also another feature of auth command, which is to list your authorized operations on a specific resource.

For example, following command lists your all permissions on Kubernetes resources:

`kubectl auth can-i --list`
## Show Time - Running All Together
Now it is time to run our webhook in a Kubernetes cluster. We already created a local cluster using [Kind](https://github.com/kubernetes-sigs/kind/).

Now let’s try our authorization rules by creating a deployment. Remember that we allow our user to create deployments but not delete them.

Let’s create a deployment:

`>kubectl create deployment nginx --image=nginx -n default`
deployment.apps/nginx created
Let’s get pods:

`>kubectl get pods`
NAME READY STATUS RESTARTS AGE
nginx-77b4fdf86c-zjwhr 1/1 Running 0 52m
Our authorization webhook works well so far.

Now test it with the restricted service-account. To do so, we need to create a service account named **test-user**.

`kubectl create sa test-user`
Now we can use kubectl auth can-i command to check our service-account’s permissions.

First let’s check for list and get operations:

`>kubectl auth can-i list pods --as=system:serviceaccount:default:test-user`
yes
`>kubectl auth can-i get pods --as=system:serviceaccount:default:test-user`
yes
And then check for the delete operation:

`>kubectl auth can-i delete pods --as=system:serviceaccount:default:test-user`
no
As we see here, with our service account we can list and get pods but could not delete pods according to restrictions on our authorization webhook.

You can take a look at my demonstration repository.

## Where to Use
It is obvious that you can use it whenever you want to go beyond native solutions. But I think I could mention a couple of use cases.

Imagine that you have hundreds or thousands of developers/devops/SREs in your organization. And you want to dynamically change permissions of Kubernetes cluster users. It can be a quite cumbersome to do it via native RBAC.

👉 You may need to give permissions to users for a specific **time period**👉 You may want to add

**review&approve process**to grand permissions to users
👉 You may want to keep

**authorization rules in sync**across different Kubernetes clusters
👉 You may also want to sync authorization rules from

**another source like LDAP**or other
**identity providers**
👉 You may want to use a custom policy engine for your authorization rules
Of course we can create a long list that changes according to specific use cases. In this post, as an example, we restricted a specific user’s/service account’s permissions.

## References
## Webhook Mode
### A WebHook is an HTTP callback: an HTTP POST that occurs when something happens; a simple event-notification via HTTP…
kubernetes.io

## Controlling Access to the Kubernetes API
### This page provides an overview of controlling access to the Kubernetes API. Users access the Kubernetes API using…
kubernetes.io

I hope this article informed you about how authorization works in Kubernetes in general and how can we go beyond it.

See you on the next article. Till then, may the bug free code with you 🙏