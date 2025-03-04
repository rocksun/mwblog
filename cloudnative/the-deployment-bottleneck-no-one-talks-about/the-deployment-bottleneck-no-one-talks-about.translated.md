# 人们从未谈论的部署瓶颈

![关于：人们从未谈论的部署瓶颈的特色图片](https://cdn.thenewstack.io/media/2025/03/a800b619-bottleneck-1024x577.png)

大多数应用程序依赖于云 SDK 来连接到消息代理、队列、数据库、API 等服务。这主要通过三种方式带来了部署摩擦：

**基础设施管理** – 开发人员必须单独配置服务，这通常会导致应用程序代码和基础设施之间出现错位。**云特定依赖项** – SDK 将代码紧密耦合到单个提供商，这使得许多任务变得复杂，例如迁移、本地开发、测试和多云策略。**漫长的调试和恢复时间** – 基础设施不匹配会导致部署失败，这些失败难以排查和回滚。

与其直接使用云 SDK，不如在应用程序和云服务之间引入一个标准化层。这允许开发人员与基本资源交互，而不会与特定提供商的 SDK 紧密耦合。像 Dapr 这样的框架通过提供与云资源交互的统一 API 来帮助实现这一点。

## Dapr：标准化云 API 的 Sidecar

Dapr（分布式应用程序运行时）是一个运行时抽象框架，它为云原生应用程序提供了一个一致的 API，用于与消息队列、存储和发布/订阅等服务交互。通过充当 sidecar 进程，Dapr 使应用程序能够保持与云无关，同时简化分布式系统开发。

#### 示例：使用对 AWS 的直接 SDK 调用发送消息

```
import boto3 # AWS-specific SQS setup
sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/123456789012/my-queue'

def send_message(message):
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=message
    )
    return response
```

这种方法有几个缺点：
- 代码与 AWS 紧密耦合，这意味着切换提供商或消息代理/队列需要重写 SDK 集成。
- 基础设施必须在包含基础设施即代码 (IaC) 部署脚本的单独项目中进行配置。
- 如果队列设置发生更改，则必须更新应用程序逻辑以匹配，否则存在基础设施风险。

#### 示例：使用 Dapr 发送消息

应用程序不是与特定的云服务交互，而是将消息发送到 Dapr 的发布 API，后者将它们路由到相应的后端。

```
import requests

DAPR_PORT = 3500
QUEUE_NAME = "azure-servicebus"

def send_message(message):
    url = f"http://localhost:{DAPR_PORT}/v1.0/bindings/{QUEUE_NAME}"
    payload = {"data": message, "operation": "create"}
    response = requests.post(url, json=payload)
    return response.status_code

send_message({"orderId": "12345"})
```

**使用 Dapr 的好处**

**更快的开发和降低的复杂性** – 消除了集成多个云 SDK 或编写自定义服务发现逻辑的需要。Dapr 提供了一个简单一致的 API，可以加快开发速度。**无缝的多云和混合部署** – 应用程序保持与云无关，从而更容易在 AWS、Azure、Google Cloud Platform (GCP) 或本地运行工作负载，而无需进行重大代码更改。**内置的弹性和可观测性** – 支持自动重试、断路器和分布式跟踪，从而提高系统可靠性并简化调试。**事件驱动且设计可扩展** – 对发布/订阅消息的原生支持使开发人员能够构建高效扩展的反应式、事件驱动架构。**更少的运营开销** – 自动处理服务通信模式，减少了为服务交互编写和维护粘合代码的负担。

由此可见，Dapr [简化了应用程序与云服务交互的方式](https://thenewstack.io/how-simplifying-our-architecture-saved-us-thousands-monthly/)，但是，在 Dapr 可以与队列交互之前，我们需要使用 Terraform 或其他 IaC 工具来配置它：

```
resource "azurerm_servicebus_namespace" "example" {
  name                = "example-namespace"
  location            = "East US"
  resource_group_name = azurerm_resource_group.example.name
  sku                 = "Standard"
}

resource "azurerm_servicebus_queue" "example" {
  name         = "example-queue"
  namespace_id = azurerm_servicebus_namespace.example.id
}
```

创建完成后，我们还需要通过定义组件文件来配置 Dapr 以使用正确的插件：

```
apiVersion: dapr.io/v1alpha1
kind: Component
metadata:
  name: azure-servicebus
  namespace: default
spec:
  type: bindings.azure.servicebusqueues
  version: v1
  metadata:
  - name: connectionString
    value: "Endpoint=sb://example-namespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=your-key"
  - name: queueName
    value: "example-queue"
```
即使使用了运行时抽象，开发人员仍然需要做相当多的工作才能运行一个基本的应用程序，所以这引出了我们的下一个问题。如果我们不必每次都创建 Terraform 项目和配置文件怎么办？

## 基于应用程序行为的自动化基础设施
Dapr 简化了与云服务的交互，但开发人员仍然必须单独定义和配置基础设施。下一个合乎逻辑的步骤是基于应用程序的资源使用情况自动化基础设施配置。

**工作原理：**
* **应用程序定义的基础设施** – 基础设施是从应用程序与云服务交互的方式推断出来的。
* **最小权限访问** – 每次重新部署应用程序时，权限都会动态调整，确保始终应用最小权限原则。

基础设施集成现在有两个用途，因为它们现在还可以识别应用程序的基础设施需求。

**示例：完全自动化的基础设施配置**
一个运行时感知系统可以根据应用程序的使用情况自动配置必要的资源。

在这个例子中：

- 公开了用于创建用户配置文件的 API。
- 使用键值存储来存储用户详细信息。
- 使用存储桶来上传个人资料图片。

```python
import json
from uuid import uuid4
from nitric.resources import api, kv, bucket
from nitric.application import Nitric
from nitric.context import HttpContext

# Create an API named public
profile_api = api("public")

# Access profile key-value store with permissions
profiles = kv("profiles").allow("get", "set", "delete")

# Define a storage bucket for profile pictures
profile_pics = bucket("profile-pics").allow("write", "read", "delete")

@profile_api.post("/profiles")
async def create_profile(ctx: HttpContext) -> None:
    pid = str(uuid4())
    name = ctx.req.json["name"]
    age = ctx.req.json["age"]
    hometown = ctx.req.json["homeTown"]
    await profiles.set(pid, {"name": name, "age": age, "hometown": hometown})
    ctx.res.body = {"msg": f"Profile with id {pid} created."}

Nitric.run()
```

这里的关键是应用程序能够自动与其所需的资源和权限进行通信，以生成可以映射到满足这些需求的预构建 IaC 模块的规范。
您可能还会注意到，我们没有在任何地方指定将为哪个云生成 IaC。这意味着只要我们有可以配置到该云的 Terraform 或 Pulumi 模块，[IaC 就可以自动化](https://thenewstack.io/achieve-gitops-on-day-one-with-iac-automation/) 到任何云。您可以[此处](https://nitric.io/blog/cloud-sdks)了解有关此工作原理的更多信息。

## 解决自动化问题
在将自动化引入企业工作流程时，自然会对安全、合规性和治理产生担忧。让我们分解这些挑战以及如何有效地管理它们。

**基础设施定义中的关注点分离**
对于[从应用程序代码生成基础设施](https://thenewstack.io/can-ai-generate-functional-terraform/) 的框架，最大的担忧之一是担心开发人员最终会直接定义基础设施。这是否模糊了应用程序和运营责任之间的界限？

这种方法在正确执行时实际上可以加强关注点分离。开发人员无需手动配置资源，而是描述其应用程序的运行时需求，而无需指定其部署方式。运营团队保留对执行、安全和成本管理的控制权，同时减少将应用程序需求转换为基础设施的摩擦。事实上，这[减少了错误配置并加快了交付速度](https://nitric.io/blog/dropbio)，因为基础设施始终与应用程序实际需求保持一致。

**IAM策略和配置中的安全风险**
自动化是否会无意中授予过多的权限或配置未经授权的资源？好消息是，自动化并不意味着失去控制；当正确执行时，它实际上可以增强安全性。通过使用代码强制执行策略，使用 Open Policy Agent (OPA)、AWS SCP（服务控制策略）或预定义的身份和访问管理 (IAM) 模板等工具，组织可以确保在部署之前始终应用和审查权限。事实上，自动化减少了人为错误，这是[安全漏洞的常见原因](https://thenewstack.io/how-iam-missteps-cause-data-breaches/)。

**遵守 SOC 2、HIPAA 和 PCI DSS**
许多组织担心自动化可能会与 SOC 2、HIPAA 或 PCI DSS 等严格的监管框架冲突。实际上，自动化是维护合规性而不是破坏合规性的强大工具。
规章制度强调可追溯性、可重复性和可控性，自动化技术可以增强这三方面。自动化工作流可以确保每次部署都符合合规性要求，而不是依赖容易出现不一致和错误的人工流程。预先批准的基础设施配置也有帮助。通过定义批准的模式并通过自动化强制执行，组织可以确保只部署符合要求的设置。

**企业工作流和预先批准的配置**

对于企业而言，自动化必须与结构化工作流保持一致。可以理解的是，人们会担心完全抽象基础设施配置可能会去除必要的防护措施。自动化不会允许不受限制的配置，而是可以强制执行企业批准的配置。平台团队仍然制定规则，定义批准的配置并确保跨环境的一致性。

## 最终想法

自动化并不会取代治理和合规流程，而是可以通过将安全和合规纳入开发工作流来加强它们。通过预定义策略、持续监控和标准化配置，组织可以提高安全性和效率，同时保持必要的控制。

您可以使用Nitric尝试这种自动化方法。[这里有一些教程](https://nitric.io/docs/guides)可以帮助您入门。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展日新月异，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。