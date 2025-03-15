
<!--
title: 在Amazon Bedrock上部署DeepSeek-R1模型
cover: https://cdn.thenewstack.io/media/2025/03/682542ab-deploy-deepseek-r1-amazon-bedrock.jpg
summary: 在 Amazon Bedrock 部署 DeepSeek-R1 模型，解锁强大 AI 应用！本文详解如何将 Hugging Face 的 DeepSeek-R1 Distill Llama 模型导入 Bedrock，利用 AWS S3 存储，并通过 Bedrock API 调用。更有自动缩放、性能监控、API 安全等优化技巧，助力高效、安全地运行 LLM。
-->

在 Amazon Bedrock 部署 DeepSeek-R1 模型，解锁强大 AI 应用！本文详解如何将 Hugging Face 的 DeepSeek-R1 Distill Llama 模型导入 Bedrock，利用 AWS S3 存储，并通过 Bedrock API 调用。更有自动缩放、性能监控、API 安全等优化技巧，助力高效、安全地运行 LLM。

> 译自：[Deploy DeepSeek-R1 Models on Amazon Bedrock](https://thenewstack.io/deploy-deepseek-r1-models-on-amazon-bedrock/)
> 
> 作者：Oladimeji Sowole

DeepSeek 是一项先进的 AI 研究计划，旨在开发与基础专有模型（如 [OpenAI](https://thenewstack.io/mastering-openais-realtime-api-a-comprehensive-guide/) 的 GPT 系列和 [Google](https://cloud.google.com/?utm_content=inline+mention) 的 BERT）相媲美的最先进的开源大型语言模型 (LLM)。[DeepSeek-R1 系列](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/) 是 DeepSeek 训练的高性能开源模型，旨在提供优化的推理能力，使其成为各种应用的强大工具，包括自然语言理解、代码生成和科学研究。

随着 AI 应用的扩展，高效部署此类模型对于企业和开发人员至关重要。AI 部署的主要挑战之一是需要一个可扩展的基础设施，该基础设施可以处理密集的计算需求，同时提供可靠且快速的推理。[Amazon Bedrock](https://thenewstack.io/building-llm-based-genai-applications-with-amazon-bedrock/) 通过提供一种完全托管的服务来解决这一问题，该服务使开发人员能够将基础模型集成到他们的应用程序中，而无需管理底层基础设施。

通过利用 Bedrock 的自定义模型导入，开发人员可以将像 DeepSeek-R1 这样的预训练模型引入到安全、高可用性和低延迟的环境中，该环境针对生产工作负载进行了优化。它还使组织能够利用 AI 的强大功能，同时受益于 [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) 的安全性、可扩展性和成本效益。

本教程将指导您完成在 Amazon Bedrock 上部署 DeepSeek-R1 Distill Llama 模型的端到端过程，从下载模型并准备部署到通过 AWS Bedrock API 调用它。它还将探讨优化技术、安全最佳实践和性能监控策略，以帮助确保平稳高效的 AI 部署。

在本指南结束时，您将拥有一个在 Amazon Bedrock 上运行的完全可操作的 DeepSeek-R1 模型，该模型能够为各种 AI 驱动的应用程序提供高质量的响应。

## 先决条件

在开始之前，请确保您具备以下条件：

- 一个有效的 Amazon Web Services (AWS) 账户，并具有访问 Amazon S3 和 Amazon Bedrock 服务的权限。
- 模型兼容性。Amazon Bedrock 支持 Llama 2 等架构，使其与 DeepSeek-R1 Distill 模型兼容。
- Hugging Face 模型文件，包括：
    - 模型权重（`.safetensors` 格式）
    - 配置文件（`config.json`）
    - 分词器文件（`tokenizer_config.json`, `tokenizer.json`, `tokenizer.model`）
- 模型权重 (
- 一个可访问的 Amazon S3 存储桶，用于存储模型文件。
- 基础设施和访问管理 (IAM) 角色和策略已配置为允许模型部署和 API 访问。

完成这些准备工作后，您可以继续进行部署。

## 步骤 1：安装所需的依赖项

首先，在您的 Python 环境中安装必要的依赖项：

```bash
pip install huggingface_hub boto3
```

这将安装 Hugging Face Hub 以进行模型检索，并安装 Boto3 以进行 AWS 交互。

## 步骤 2：下载 DeepSeek-R1 模型

接下来，从 Hugging Face 下载 DeepSeek-R1 Distill Llama 模型：

```python
from huggingface_hub import snapshot_download

# Define model ID
model_id = "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"

# Download the model to the local directory
local_dir = snapshot_download(
    repo_id=model_id,
    local_dir="DeepSeek-R1-Distill-Llama-8B"
)
```

此命令获取模型文件并将它们存储在指定的目录中。

## 步骤 3：将模型文件上传到 Amazon S3

要在 Amazon Bedrock 上部署，请将模型文件上传到 Amazon S3 存储桶：

```python
import boto3
import os

# Initialize S3 client
s3_client = boto3.client('s3', region_name='us-east-1')

# Define S3 bucket name
bucket_name = 'your-s3-bucket-name'

# Specify local directory
local_directory = 'DeepSeek-R1-Distill-Llama-8B'

# Upload files to S3
for root, dirs, files in os.walk(local_directory):
    for file in files:
        local_path = os.path.join(root, file)
        s3_key = os.path.relpath(local_path, local_directory)
        s3_client.upload_file(local_path, bucket_name, s3_key)
```

将 `your-s3-bucket-name` 替换为您实际的 S3 存储桶名称。

## 步骤 4：将模型导入到 Amazon Bedrock

将模型放入 S3 后，将其导入到 Amazon Bedrock：

1. 在 AWS 控制台中导航到 Amazon Bedrock。
2. 选择**自定义模型**→**导入模型**。
3. 输入 S3 URI（例如，`s3://your-s3-bucket-name/DeepSeek-R1-Distill-Llama-8B/`）。
4. 确认并开始导入过程。

Amazon Bedrock 将处理并验证模型以进行部署。

## 步骤 5：部署和调用模型

导入后，使用 Bedrock API 调用模型：

```python
import boto3
import json

# Initialize Bedrock client
bedrock_client = boto3.client('bedrock', region_name='us-east-1')

# Define model ID
model_id = 'your-model-id'

# Define input prompt
input_data = {
    'prompt': 'Explain the significance of transformers in NLP.',
    'max_tokens': 150
}

# Invoke model
response = bedrock_client.invoke_model(
    ModelId=model_id,
    ContentType='application/json',
    Body=json.dumps(input_data)
)

# Process response
output = json.loads(response['Body'].read())
print(output)
```

将 `your-model-id` 替换为您分配的 Bedrock 模型 ID。

## 优化模型部署

在 Bedrock 上部署模型后，请考虑以下优化方法。

1. **启用自动缩放**：配置自动缩放以根据流量动态分配计算资源，从而实现高效的资源利用率。
2. **监控模型性能**：使用 AWS CloudWatch 记录诸如推理延迟和请求量之类的指标。
3. **保护 API 端点**：确保您的 Bedrock 端点通过 IAM 角色和 [API 网关](https://thenewstack.io/what-is-api-management/) 授权进行保护。
4. **优化成本**：使用按需缩放而不是固定配置，如果响应时间不重要，则选择成本较低的计算实例。

除了基本部署之外，还可以考虑以下高级集成：

1. **微调**：使用其他特定于领域的数据集自定义模型。
2. **API 集成**：通过 REST API 公开模型，以便与 Web 或移动应用程序无缝交互。

## 结论

在 Amazon Bedrock 上部署 DeepSeek-R1 Distill Llama 模型为运行 AI 驱动的应用程序提供了一个强大、可扩展且高效的解决方案。借助 Bedrock 的无服务器基础设施，您可以集成和管理 LLM，只需极少的精力，从而帮助确保快速推理、可扩展性和安全性。

通过利用 Amazon Bedrock，您可以灵活地部署最先进的 AI 模型，同时受益于 [AWS 强大的云基础设施](https://roadmap.sh/best-practices/aws)。无论您是数据科学家、AI 研究人员还是开发人员，将 DeepSeek-R1 集成到 Bedrock 中，您都可以创建强大的 AI 驱动的应用程序，而无需管理 GPU、推理端点或扩展操作的复杂性。有关更多详细信息，请浏览官方 [Amazon Bedrock 文档](https://aws.amazon.com/bedrock/)。 祝您构建顺利！

*想要扩展您的 AI 知识吗？ 探索具有结构化输出的 OpenAI！ 探索 Andela 专为开发人员设计的逐步指南，以简化流程、提高精度和优化结果。*
