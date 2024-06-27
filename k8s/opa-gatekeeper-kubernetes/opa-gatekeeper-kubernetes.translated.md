# OPA Gatekeeper：如何在 Kubernetes 集群中编写策略

了解如何利用 OPA Gatekeeper 在 Kubernetes 集群中编写和执行策略，确保环境中的安全性和高效资源管理。

### 目录

- [什么是 Open Policy Agent (OPA)？](#什么是-open-policy-agent-opa)
- [OPA 和 Kubernetes 如何协同工作？](#opa-和-kubernetes-如何协同工作)
- [什么是 OPA Gatekeeper？](#什么是-opa-gatekeeper)
- [使用 OPA Gateway 在 Kubernetes 集群中编写策略](#使用-opa-gateway-在-kubernetes-集群中编写策略)
- [总结和结论](#总结和结论)

由于 Kubernetes 等工具的存在，管理和自动化微服务环境的日常工作流程变得更加容易。

在 Kubernetes 中使用策略将为您提供最大的控制和灵活性，尤其是在以下方面：

- 提高微服务的安全性
- 积极管理云基础设施中的有限资源
- 遵守和治理法规

阅读本文后，您将了解：

- 在 Kubernetes 环境中使用策略的优势。
- 如何建立一个策略分配系统；Kubernetes 和 OPA 在幕后如何运作。
- 在集群中编写和运行策略所需的一切。

## 什么是 Open Policy Agent (OPA)？

[Open Policy Agent (OPA)](https://www.openpolicyagent.org/) 帮助我们使用 Rego 编写策略即代码，Rego 是一种专门为此目的而设计的声明式语言。

借助 OPA，我们可以定义和执行跨越堆栈各个层的策略，从 Kubernetes 到微服务。

这种方法有助于在 Kubernetes 集群中管理策略时保持一致性、可扩展性和敏捷性。

此外，通过使用表达性语法，您可以有效地表示访问控制规则和组织达成的复杂策略决策。

总而言之，这将极大地确保您的 Kubernetes 环境合规且安全。

本文的重点是在 Kubernetes 设置中编写策略。

如果您不熟悉 OPA，可以快速了解其工作原理和实现细节，请参阅 [这篇文章](https://permify.co/post/implementing-opa/)

## OPA 和 Kubernetes 如何协同工作？

在本节中，让我们更深入地了解如何启动和运行 Open Policy Agent (OPA)。

OPA 为 Kubernetes 提供了良好的支持，这在它的文档中有所体现，因此我们将研究如何将其集成到您的 Kubernetes 环境中。

但首先，让我们谈谈一些重要的组件，并了解它在“幕后”是如何工作的。

Kubernetes 附带了一个名为准入控制器的组件。它是一段代码，充当 Kubernetes API 本身与任何发送的请求之间的中间人。

准入控制器还可以用于执行策略和安全措施，确保只有授权且配置正确的负载才能进入集群。

它们可能会更改请求以确保在处理之前它具有有效且可接受的形式。

因此，准入控制器可以分为两种类型：变异或验证。了解这一点很重要，因为这是 Open Policy Agent (OPA) 的切入点。

至于为什么我们需要在集群中使用准入控制器，[官方 Kubernetes 文档](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) 这样说：

"...没有正确配置了正确准入控制器集的 Kubernetes API 服务器是不完整的服务器，它将不支持您期望的所有功能..."

本质上，您可以选择使用 Open Policy Agent (OPA) 或编写自己的自定义准入控制器，具体取决于您计划在 Kubernetes 环境中实现的自定义范围。

## 什么是 OPA Gatekeeper？

没有准入控制器，Kubernetes 设置几乎是不完整的。[OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper) 就是这样一个控制器，它检查进入 Kubernetes API 的任何请求。

Gatekeeper 拦截请求并与预定义的策略进行检查。根据此检查，可以拒绝或授予请求。

从上面的图示中，我们可以看到 OPA Gatekeeper 如何**审查**进入 Kubernetes API 服务器的任何请求的工作流程。

它还不断**监视** API 服务器元素（如 Pod 和服务）的任何更改。

因此，本质上，当您在 Kubernetes 环境中安装 Gatekeeper 时，您可以编写策略并使其在集群中生效。我们将在稍后详细介绍。

## 使用 OPA Gateway 在 Kubernetes 集群中编写策略

为了进一步了解 OPA Gatekeeper 在 Kubernetes 中的优势和集成范围，我们将在这篇文章中涵盖以下用例：
```yaml
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

```yaml
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

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: demo-namespace
```

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: test-namespace
  annotations:
    team: "devops"
```

```yaml
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

```yaml
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
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: test-namespace-production-no-quota
  labels:
    env: production
```

```
kubectl apply -f test-namespace-production-no-quota.yaml
```

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: resource-quota
  namespace: default
spec:
  hard:
    requests.cpu: "1"
    requests.memory: "1Gi"
    limits.cpu: "2"
    limits.memory: "2Gi"
```

```
kubectl apply -f resource-quota.yaml
```

```
kubectl get resourcequotas -n default
```

```
minikube start
```

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)

@app.route('/validate', methods=['POST'])
def validate_pod():
    try:
        admission_review = request.get_json()
        pod_spec = admission_review['request']['object']['spec']
        # 在这里添加您的验证逻辑
        # 例如：检查 Pod 是否具有特定标签
        labels = pod_spec.get('labels', {})
        if 'app' not in labels:
            logger.error("Pod validation failed: Missing 'app' label")
            return jsonify({"response": {"allowed": False, "status": {"reason": "MissingAppLabel"}}}), 200
        # 如果所有验证检查都通过
        logger.info("Pod validation succeeded")
        return jsonify({"response": {"allowed": True}}), 200
    except Exception as e:
        logger.exception("An error occurred during pod validation")
        return jsonify({"response": {"allowed": False, "status": {"reason": "InternalServerError"}}}), 500

if __name__ == '__main__':
    # 配置日志记录
    logging.basicConfig(level=logging.INFO)
    # 启动 Flask 应用程序
    app.run(host='0.0.0.0', port=8080, debug=False)
```

```
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
CMD [ "python", "app.py" ]
```

```
docker build -t your-username/repository-name:latest .
```

```
docker login
```

```
docker tag <repository-name>:latest your-username/repository-name:latest
docker push your-username/repository-name:latest
```

```
openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -nodes -subj "/CN=pod-validation-webhook.default.svc"
```

```
kubectl create secret tls pod-validation-webhook-tls --cert=server.crt --key=server.key -n default
```

```yaml
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
**6.** 创建服务
我们需要创建一个 kubectl 服务资源来指向我们的 Python webhook 服务器
`touch webhook-service.yaml`
```yaml
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
**7.** 创建验证配置
验证配置是正式将我们的 webhook 注册为 kubernetes API 的一部分。换句话说，kubernetes 将会知道有一个新的中间人应该在每次发送 pod 创建请求时被调用。
`touch validating-webhook-config.yaml`
```yaml
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
**8.** 应用清单文件；让我们应用我们在前面步骤中创建的部署、服务和验证配置文件 YAML。
```
kubectl apply -f webhook-deployment.yaml
kubectl apply -f webhook-service.yaml
kubectl apply -f validating-webhook-config.yaml
```
**9.** 验证。
最后，如果部署顺利，您应该看到 pod 正在成功运行。验证 webhook 也应该处于活动状态。
为了验证我们的验证钩子现在是否处于活动状态，根据 webhook 中设置的验证规则，我们只需创建一个没有标签的测试 pod，该请求应该被拒绝。
## 总结和结论
在本篇综合指南中，我们讨论了在 kubernetes 中使用策略来扩展其功能并添加自定义增强功能或团队偏好。我们还逐步介绍了使用实际用例实现 kubernetes 策略。

在您的 kubernetes 设置中使用策略是一种创造性的方法，可以充分探索容器化部署中的功能，并使其更加安全。