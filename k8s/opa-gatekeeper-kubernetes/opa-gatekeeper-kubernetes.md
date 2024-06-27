
<!--
title: 如何利用Opa Gatekeeper为Kubernetes集群编写策略
cover: ./cover.png
-->

了解如何利用 OPA Gatekeeper 在 Kubernetes 集群中编写和执行策略，确保环境的安全性和高效资源管理。

> 译自 [Opa Gatekeeper: How To Write Policies For Kubernetes Clusters](https://permify.co/post/opa-gatekeeper-kubernetes/)，作者 None。

由于 Kubernetes 等工具的存在，管理和自动化微服务环境的日常工作流程变得更加容易。

在 Kubernetes 中使用策略将为您提供最大的控制和灵活性，尤其是在以下方面：

- 提高微服务的安全性
- 积极管理云基础设施中的有限资源
- 遵守和治理法规

阅读本文后，您将了解：

1. 在 Kubernetes 环境中使用策略的优势。
2. 如何建立一个策略分配系统；Kubernetes 和 OPA 在幕后如何运作。
3. 在集群中编写和运行策略所需的一切。

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

![](https://github.com/Permify/permify/assets/34595361/94429606-c884-40af-893b-6a24903967a2)

至于为什么我们需要在集群中使用准入控制器，[官方 Kubernetes 文档](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) 这样说：

> "...没有正确配置了正确准入控制器集的 Kubernetes API 服务器是不完整的服务器，它将不支持您期望的所有功能..."

本质上，您可以选择使用 Open Policy Agent (OPA) 或编写自己的自定义准入控制器，具体取决于您计划在 Kubernetes 环境中实现的自定义范围。

## 什么是 OPA Gatekeeper？

没有准入控制器，Kubernetes 设置几乎是不完整的。[OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper) 就是这样一个控制器，它检查进入 Kubernetes API 的任何请求。

Gatekeeper 拦截请求并与预定义的策略进行检查。根据此检查，可以拒绝或授予请求。

![](https://github.com/Permify/permify/assets/34595361/7a36c62b-c5f0-4d85-9337-8856edc8f8c6)

从上面的图示中，我们可以看到 OPA Gatekeeper 如何**审查**进入 Kubernetes API 服务器的任何请求的工作流程。

它还不断**监视** API 服务器元素（如 Pod 和服务）的任何更改。

因此，本质上，当您在 Kubernetes 环境中安装 Gatekeeper 时，您可以编写策略并使其在集群中生效。我们将在稍后详细介绍。

## 使用 OPA Gateway 在 Kubernetes 集群中编写策略

为了进一步了解 OPA Gatekeeper 在 Kubernetes 中的优势和集成范围，我们将在这篇文章中涵盖以下用例：

- [定义命名空间策略](https://hackmd.io/ot-49MTSQNyOws_oFwt4sw#1-Namespace-policy) 
- [分配资源配额](https://hackmd.io/ot-49MTSQNyOws_oFwt4sw#2-Resource-quota-allocation) 
- [编写自定义控制器](https://hackmd.io/ot-49MTSQNyOws_oFwt4sw#3-Custom-validation-webhook)


本教程分成两部分，将一步步引导你完成在 Kubernetes 集群中使用开放策略代理 (OPA) 编写和测试策略的整个过程。

在第一部分中，我们将利用 OPA gatekeeper 准入控制器来执行我们编写的策略，然后，在第二部分中，我们将编写自己的自定义验证控制器。

因此，本指南结束时，你将：

- 了解 OPA 策略在 Kubernetes 中的工作原理。
- 如何编写和应用自己的策略。
- 更好的理解 Kubernetes 中的准入控制器 webhook；工作流以及如何实现您自己的验证控制器。

## 先决条件

要充分利用本实用指南，需要在您的本地计算机上设置以下内容： 

- 确保已安装 OPA 
- Minikube：确保您拥有 Minikube 和一个正在运行的 Kubernetes 集群 
- kubectl：确保您已将 kubectl 配置为与集群进行交互。 
- OPA gatekeeper ：确保 OPA gatekeeper 已安装在您的集群中。 
- Docker 和 DockerHub 帐户 

立即开始。

## 1. 定义命名空间策略

对于此用例，我们写一个 OPA 策略，其中指出每个命名空间创建请求都应该添加一个注释。

**步骤 1**：创建一个约束模板文件一个 ConstraintTemplate 定义策略的结构和逻辑。这个模板将强制要求每个命名空间必须有 team 注释。


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

将此 YAML 保存到名为 constrainttemplate.yaml 的文件中，然后将其应用到你的群集：

```
kubectl apply -f constrainttemplate.yaml 
```

**步骤 II**：创建约束文件 约束使用 ConstraintTemplate 对特定资源（在本例中为命名空间）强制实施策略。

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

将此 YAML 保存至名为 constraint.yaml 的文件中，并将其应用于集群： 

```
kubectl apply -f constraint.yaml  
```

**步骤 III**：验证策略  

为验证策略是否正常工作，尝试在没有团队注释的情况下创建名称空间。创建应被拒绝。


```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: demo-namespace
```

将此 YAML 保存到名为 demo-namespace.yaml 的文件中并应用此文件：

```
kubectl apply -f demo-namespace.yaml
``` 

如预期的那样，我们得到了一个错误响应： 

![](https://github.com/Permify/permify/assets/34595361/6c6fb7e9-5154-45ac-86fc-bbb8cfd94b05)

现在让我们通过使用 team 注释创建名称空间来遵守该策略。


```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: test-namespace
  annotations:
    team: "devops"
```

将上述 YAML 文件另存为 test-namespace-with-annotation.yaml 并将其应用到集群。

这一次，它成功创建了该命名空间。

![](https://github.com/Permify/permify/assets/34595361/0375c733-a4c0-4e47-b5a8-9acba6f6a338)

## 2. 分配资源配额

接下来，我们想要编写更高级的政策，该政策指出标记为 env:production 的命名空间必须向其应用资源配额。

当您想要控制或监视资源的使用并提高效率时，这样的政策会很有帮助。我们开始吧。

**步骤 I**：创建约束模板文件


此模板将检查标记为 env:production 的命名空间是否有资源配额。


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

将此 YAML 保存到名为 constrainttemplate.yaml 的文件中，并将其应用到您的集群： 

```yaml
kubectl apply -f constrainttemplate.yaml 
```

**步骤 2**：创建约束文件

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

将以下 YAML 内容保存到名为 constraint.yaml 的文件中，并将其应用到你的集群中： 

```
kubectl apply -f constraint.yaml 
```

**步骤 III**：验证该策略 为了验证该策略是否有效，我们创建一个简单的测试命名空间，其中带有生产标签，但不指定任何资源配额。它应当被拒绝。

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: test-namespace-production-no-quota
  labels:
    env: production
```

将此 YAML 保存到文件 test-namespace-production-no-quota.yaml 并应用：

```
kubectl apply -f test-namespace-production-no-quota.yaml
```

正如所料，当尝试创建命名空间时，我们收到一个错误响应，提示我们必须分配一个限额，就像我们的 policy 文件中声明的那样： 

![](https://github.com/Permify/permify/assets/34595361/c52c8685-3925-47d8-80cc-9f12cddd00bf)

太棒了。让我们继续为我们的命名空间分配一个配额。

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

将此 YAML 保存到名为 resource-quota.yaml 的文件中并应用它：

```
kubectl apply -f resource-quota.yaml
```

![](https://github.com/Permify/permify/assets/34595361/cd075440-698a-42f6-bc95-dbd5df76dd5a)

按照上述说明操作后，即可成功创建命名空间并申请配额。

您还可以进一步使用下列命令，实际检查分配给该命名空间的配额：

```
kubectl get resourcequotas -n default
```

到目前为止，我们已经看到 OPA Gatekeeper 在我们想要在 Kubernetes 中执行特定操作时充当中间人或拦截者。

现在让我们进入最后一个部分，即创建我们自己的自定义验证 Webhook。

## 3. 编写自定义控制器 

首先，创建一个独立的文件夹专门用于整个训练，您可以将其称为 webhook_server。 

1. 启动 Minikube 集群。 minikube start 
2. 编写 webhook 的验证逻辑。我们用 Python 编写此部分，但也可以用任何其他选择的语言编写。创建一个文件 app.py 并复制以下内容。


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

3. 我们需要容器化此 webhook 服务器，构建它并将其推送到 DockerHub 存储库。I. 在你的 Dockerhub 账户上创建一个存储库。II. 在包含以下内容的文件夹中创建一个 Dockerfile：

```
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD [ "python", "app.py" ]
```

III. 构建镜像 docker build -t your-username/repository-name:latest . 

IV. 将其推送到 DockerHub

```
docker login
docker tag <repository-name>:latest your-username/repository-name:latest
docker push your-username/repository-name:latest
```

现在，该镜像应在 Dockerhub 上生效。这意味着我们现在可以在部署 yaml 文件中使用它。

故障排除提示：如果您在将 Docker 镜像推送到 DockerHub 时遇到请求被拒绝的错误，请确保在终端上登录 Docker，仔细检查镜像名称、存储库名称和标记名称是否存在任何错别字或不匹配。

4. 生成 TLS 证书。这有助于保护 webhook 服务器与 kubernetes 之间的通信。这是必须注意的关键步骤。如果未正确配置，则最终可能会出现 TLS 错误。

```
openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 -nodes -subj "/CN=pod-validation-webhook.default.svc"
```

```
kubectl create secret tls pod-validation-webhook-tls --cert=server.crt --key=server.key -n default
```

5. 创建部署 YAML 文件。touch webhook-deployment.yaml 。

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


6. 创建一个服务，指向我们 Python webhook 服务器 touch webhook-service.yaml

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


7. 创建验证配置。验证配置是正式将我们的 webhook 注册为 kubernetes API 的一部分。换句话说，kubernetes 将会知道有一个新的中间人应该在每次发送 pod 创建请求时被调用。

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

8. 应用清单文件；让我们应用我们在前面步骤中创建的部署、服务和验证配置文件 YAML。

```
kubectl apply -f webhook-deployment.yaml
kubectl apply -f webhook-service.yaml
kubectl apply -f validating-webhook-config.yaml
```

9. 验证。最后，如果部署顺利，您应该看到 pod 正在成功运行。验证 webhook 也应该处于活动状态。为了验证我们的验证钩子现在是否处于活动状态，根据 webhook 中设置的验证规则，我们只需创建一个没有标签的测试 pod，该请求应该被拒绝。

## 总结和结论

在本篇综合指南中，我们讨论了在 kubernetes 中使用策略来扩展其功能并添加自定义增强功能或团队偏好。我们还逐步介绍了使用实际用例实现 kubernetes 策略。

在您的 kubernetes 设置中使用策略是一种创造性的方法，可以充分探索容器化部署中的功能，并使其更加安全。