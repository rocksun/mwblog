<!--
title: 如何使用 Google Cloud 工具保护 Vertex AI 管道
cover: https://cdn.thenewstack.io/media/2026/01/c33a23cd-security.jpg
summary: 本文介绍如何使用 Google Cloud 工具保护 Vertex AI 管道，通过分层防御策略，利用 IAM、DLP 等工具，防范数据泄露、模型窃取等风险，确保 AI 模型安全。
-->

本文介绍如何使用 Google Cloud 工具保护 Vertex AI 管道，通过分层防御策略，利用 IAM、DLP 等工具，防范数据泄露、模型窃取等风险，确保 AI 模型安全。

> 译自：[How to secure Vertex AI pipelines with Google Cloud tools](https://thenewstack.io/how-to-secure-vertex-ai-pipelines-with-google-cloud-tools/)
> 
> 作者：Advait Patel

AI 模型如今为许多行业的关键系统提供动力。你会在医疗保健、银行、网络安全和国防领域发现它们。当你在 [Vertex AI](https://thenewstack.io/an-introduction-to-google-vertex-ai-automl-training-and-inference/) 上将这些模型投入生产时，攻击面会迅速扩大。你的数据、模型权重、管道和 API [都面临风险](https://thenewstack.io/googles-vertex-ai-platform-gets-freejacked/)。

在本指南中，你将学习如何使用 Google Cloud 中已有的工具来保护使用 Vertex AI 构建的模型，包括数据源、模型文件、管道和端点。这些工具包括身份和访问管理 (IAM)、[VPC Service Controls](https://cloud.google.com/security/vpc-service-controls)、数据丢失防护、Artifact Registry 和 Cloud Audit Logs。每个工具都会为你的防御策略添加一个新层。它们共同帮助为你的[机器学习工作负载](https://thenewstack.io/a-close-look-at-cloud-based-machine-learning-platforms-microsoft-azure-ml-google-vertex-ai/)构建[零信任保护](https://thenewstack.io/what-is-zero-trust-data-protection/)。

## **为什么保护 Vertex AI 管道很重要**

AI 管道是攻击者的诱人目标。一旦被攻破，它们可能会影响模型、系统，甚至最终用户。下面是关键的威胁向量及其如何影响实际系统。

| **威胁向量** | **实际影响** |
| --- | --- |
| 数据中毒 | 操纵训练数据 → 有偏见/不准确的模型 |
| 模型窃取（数据外泄） | 专有 LLM 或分类器的 IP 泄露 |
| 不安全的管道执行 | 未经授权的访问或横向移动 |
| 未受保护的推理 API | 提示注入、模型滥用或 DoS 攻击 |

这些威胁会影响你的机器学习 (ML) 工作流程的各个部分。如果没有正确的安全措施，这些风险可能会导致数据泄露、系统故障，甚至信任丧失。因此，及早了解每一个威胁有助于你构建更安全、更强大的 AI 系统。

## **Vertex AI 工作负载的安全层**

![](https://cdn.thenewstack.io/media/2026/01/126b37b2-inset-1024x128.png)

每一层都必须单独加固并持续监控。

## **分步指南：在 GCP 上保护 Vertex AI 模型**

### **1. 对数据集和管道强制执行 IAM**

首先，管理谁可以访问你的数据和管道。使用 Google Cloud 中的身份和访问工具来设置明确的规则。只向每个人或服务授予他们真正需要的访问权限。

例如，如果某人只需要读取数据，则不要允许他们运行训练作业。这可以防止错误，并阻止攻击者在你的系统中移动。

严格的访问控制可以保护你的数据并确保你的机器学习项目安全。

```

gcloud projects add-iam-policy-binding genai-project \
  --member="user:ml-engineer@example.com" \
  --role="roles/aiplatform.user"
```

限制对训练数据集的访问：

```

gcloud projects add-iam-policy-binding genai-project \
  --member="serviceAccount:training-sa@genai-project.iam.gserviceaccount.com" \
  --role="roles/bigquery.dataViewer"
```

### **2. 使用 DLP 扫描训练数据中的 PII**

在训练模型之前，审查数据中是否存在敏感或个人身份信息 (PII)。使用 Google Cloud 的数据丢失防护工具来识别并移除不应包含的任何内容。

```

gcloud dlp inspect bigquery \
  --dataset-id=training_dataset \
  --table-id=users_raw \
  --min-likelihood=LIKELY \
  --info-types=EMAIL_ADDRESS,PHONE_NUMBER,NAME
```

在敏感数据进入你的管道之前自动进行标记。

### **3. 使用 VPC Service Controls 隔离 ML 项目**

将你的机器学习项目与公共互联网隔离。设置 VPC Service Controls 以在你的数据和服务周围创建安全边界。这有助于阻止来自网络外部的未经授权的访问。

```

gcloud access-context-manager perimeters create genai-perimeter \
  --resources=projects/genai-project \
  --restricted-services=aiplatform.googleapis.com,bigquery.googleapis.com
```

这可以防止数据从 AI 工作负载外泄到未经授权的服务。

### **4. 在 Artifact Registry 中保护模型工件**

使用 Artifact Registry 安全地存储你的模型。此工具允许你跟踪模型版本和管理访问。它降低了被盗或被篡改的风险。

```

gcloud artifacts repositories create genai-models \
  --repository-format=docker \
  --location=us-central1 \
  --description="Private AI Model Store"
```

仅限于授权服务账户的访问：

```

gcloud artifacts repositories add-iam-policy-binding genai-models \
  --location=us-central1 \
  --member="serviceAccount:ci-cd@genai-project.iam.gserviceaccount.com" \
  --role="roles/artifactregistry.writer"<strong>5. 使用工作负载身份强化 Vertex AI 管道</strong>
```

使用与 Google Cloud 身份关联的 Kubernetes 服务账户。这样，每个管道组件都有其自己的安全身份。这可以防止未经授权的操作并确保你的管道安全。

```

gcloud iam service-accounts add-iam-policy-binding \
  pipeline-sa@genai-project.iam.gserviceaccount.com \
  --member="serviceAccount:genai-project.svc.id.goog[ml-pipelines/pipeline-runner]" \
  --role="roles/aiplatform.customCodeServiceAgent"
```

这可以防止 Kubeflow 或 Cloud Build 作业中出现硬编码凭据。

### **6. 使用 IAP 和速率限制保护推理端点**

使用 Cloud Endpoints 和 Identity-Aware Proxy 保护你的模型端点。这可以控制谁可以访问你的模型。添加速率限制以阻止滥用并降低攻击风险。

```

gcloud compute backend-services update genai-inference \
  --iap=enabled,oauth2-client-id=CLIENT_ID,oauth2-client-secret=SECRET
```

添加配额限制以防止滥用：

```

Quota:
  limits:
    - name: predict-requests
      metric: "ml.googleapis.com/predict"
      unit: "1/min/{project}"
      values:
        STANDARD: 100
```

### **7. 启用审计日志以实现全面的可观测性**

启用审计日志以跟踪你的 AI 资源上的所有操作。这有助于你快速发现异常活动并在问题扩大之前解决它们。

```

gcloud logging sinks create vertex-logs-sink \
  bigquery.googleapis.com/projects/genai-project/datasets/audit_logs \
  --log-filter='resource.type="aiplatform.googleapis.com/PipelineJob"'
```

使用 Looker Studio 或 BigQuery 进行可视化：

**管道执行**

* 使用 BigQuery 查询执行日志
* 使用 Looker Studio 从这些日志创建图表

**模型部署事件**

* 使用 BigQuery 查询部署事件数据
* 使用 Looker Studio 可视化部署时间线和状态

**数据访问日志**

* 使用 BigQuery 查询访问日志
* 使用 Looker Studio 构建显示访问模式的仪表板

## **Vertex AI 安全清单**

| **安全控制** | **GCP 工具/层** |
| --- | --- |
| 管道和数据的 IAM | Cloud IAM + 条件 |
| 敏感数据检测 | Cloud DLP + BigQuery |
| 工件完整性 | Artifact Registry + 签名镜像 |
| 网络隔离 | VPC Service Controls |
| 管道身份验证 | Workload Identity Federation |
| 推理访问控制 | IAP + 配额 + OAuth2 |
| 审计和漂移检测 | Cloud logging + Security Command Center + Recommender |

此表列出了关键的安全控制及其相关的 GCP 工具。它涵盖了访问管理、数据保护、工件安全和网络隔离。Cloud IAM、Cloud DLP、Artifact Registry、VPC Service Controls 和 Workload Identity 等工具有效地实施了这些控制。

## **结论**

保护 AI 模型不仅仅关乎基础设施。它更关乎维护系统信任。你可以使用 Vertex AI 部署强大的机器学习模型。然而，如果没有正确的控制措施，你将面临数据泄露、IP 盗窃和攻击的风险。采用分层防御方法有助于保护你的 AI 工作负载，从原始数据到部署。关键工具包括 IAM、DLP、VPC Service Controls 和 Artifact Registry。

到 2026 年，AI 安全就是云安全。如果你在 Google Cloud 上部署 ML 管道，请将你的模型视为宝贵资产。构建强大的防御措施以确保它们安全。