
<!--
title: 打造团队乐于复用的Terraform模块
cover: https://cdn.thenewstack.io/media/2025/11/9d4d5769-modules.jpg
summary: Terraform模块挑战：版本碎片、破坏性变更、影子模块。解决策略：关注点分离（模块单一职责），可组合性（模块协同）。平台化可进一步管理版本和变更。
-->

Terraform模块挑战：版本碎片、破坏性变更、影子模块。解决策略：关注点分离（模块单一职责），可组合性（模块协同）。平台化可进一步管理版本和变更。

> 译自：[Build Terraform Modules That Your Team Will Actually Reuse](https://thenewstack.io/build-terraform-modules-that-your-team-will-actually-reuse/)
> 
> 作者：Rak Siva

许多组织在采用 Terraform 模块时面临困难，例如：

*   **版本碎片化：** 不同的项目/团队最终使用不同的版本。
*   **破坏性变更：** 团队在升级时，部署期间或部署后存在出错风险。
*   **影子模块：** 当模块不符合其需求时，团队会自行编写。

本指南展示了两个软件工程原则如何将 [Terraform 模块](https://thenewstack.io/maximizing-terraform-modules-for-platform-engineering/)转变为团队真正希望使用的组件。

## **从整体式到模块化：2 种模式**

### **起点：大多数团队的现状**

大多数团队都从正常运行的基础设施开始：一个存储桶、一些身份和访问管理 (IAM) 权限以及基本的安全设置。问题不在于它已损坏；而是所有东西都纠缠在一个模块中：

```
# modules/s3-with-access/main.tf
resource "aws_s3_bucket" "app_bucket" {
  bucket = "mycompany-app-uploads"  # Hardcoded name
}

resource "aws_iam_role" "app_role" {  # Creating roles inside storage module
  name = "app-s3-access-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "lambda.amazonaws.com" }  # Lambda only
    }]
  })
}

resource "aws_iam_role_policy" "app_bucket_access" {
  role = aws_iam_role.app_role.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = ["s3:GetObject", "s3:PutObject"]  # Raw IAM actions
      Resource = "${aws_s3_bucket.app_bucket.arn}/*"
    }]
  })
}
```

这个模块捆绑了存储桶、IAM 角色和策略，但是当您需要以下情况时会发生什么：

*   一个用于 Elastic Container Service (ECS) 任务而非 Lambda 的相同存储桶？您无法重复使用此模块，因为该角色是为 Lambda 硬编码的。
*   多个服务访问一个存储桶？您需要为每个服务复制和修改整个模块。
*   仅仅是存储桶，而不需要 IAM 角色？它们是不可分离地耦合在一起的。

这就是为什么团队最终会得到略有不同的相同副本 – `s3-module-lambda`、`s3-module-ecs`、`s3-module-ec2`。

## **模式 1：关注点分离 — 1 个模块，1 个用途**

第一个问题：模块试图做太多事情。当您的 S3 模块还创建 IAM 角色和策略时，它就无法在不同的服务中重复使用。

单一职责原则规定每个模块只做好一件事。让我们通过一个只管理 S3 存储桶的模块来分离关注点。没有 IAM 角色。没有策略。只有具有合理默认设置的存储桶。

### **S3 模块 — 只管理存储桶**

```
# modules/s3/main.tf

locals {
  bucket_name = "${var.environment}-${replace(lower(var.name), "_", "-")}"
}

resource "aws_s3_bucket" "this" {
  bucket = local.bucket_name
  tags   = var.tags
}

resource "aws_s3_bucket_public_access_block" "this" {
  bucket = aws_s3_bucket.this.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_versioning" "this" {
  count  = var.enable_versioning ? 1 : 0
  bucket = aws_s3_bucket.this.id
  versioning_configuration {
    status = "Enabled"
  }
}

output "arn" {
  value = aws_s3_bucket.this.arn
}

output "id" {
  value = aws_s3_bucket.this.id
}
```

**实践中：** 您的 S3 模块将更复杂，需要加密、跨域资源共享 (CORS)、生命周期策略等等。将 IAM、网络和计算资源保留在单独的模块中，以便它们可以在不同服务和团队之间[重复使用](https://thenewstack.io/your-platform-engineering-toolkit-for-terraform-and-beyond/)。

## **模式 2：可组合性 — 协同工作的模块**

第二个原则：模块应该清晰地组合。每个模块都需要一个清晰的接口，具有可预测的输出，供其他[模块使用](https://thenewstack.io/experts-share-best-practices-for-building-terraform-modules/)。

首先，使用分离的模块创建您的基础设施资源：

```
# Create storage with the S3 module
module "uploads" {
  source      = "./modules/s3"
  name        = "uploads"
  environment = "production"
}

module "backups" {
  source      = "./modules/s3"
  name        = "backups"
  environment = "production"
}

# Create compute resources
resource "aws_iam_role" "app_service" {
  name = "app-service"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = { Service = "ecs-tasks.amazonaws.com" }
    }]
  })
}
```

然后用显式权限将它们连接起来：

```
# Grant the service access to the buckets it needs
resource "aws_iam_role_policy" "app_access" {
  name = "app-bucket-access"
  role = aws_iam_role.app_service.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = ["s3:GetObject", "s3:PutObject"]
        Resource = "${module.uploads.arn}/*"
      },
      {
        Effect = "Allow"
        Action = ["s3:PutObject"]
        Resource = "${module.backups.arn}/*"
      }
    ]
  })
}
```

因为模块具有可预测的接口：

*   任何服务都可以使用任何存储桶。
*   权限是显式的且可审计的。
*   模块之间没有隐藏的依赖关系。
*   每个部分都可以独立测试。

**实践中：** 您的模块将是更大的单元——一个“应用程序堆栈”或“数据管道”，而不是单独的资源。标准化的接口和输出使模块能够协同工作，无论您是组合存储桶和策略，还是整个虚拟私有云 (VPC) 和 Amazon Elastic Kubernetes Service (EKS) 集群。可预测的接口实现了可组合性。

## **从模式到平台**

这些模式解决了影子模块问题。团队将不需要绕过精心设计、可组合的模块。但您仍然面临版本碎片化和破坏性变更。当您一半的团队使用旧版本，只有新项目才能访问最新版本时，每次更新现在都涉及到迁移的额外复杂性。

优秀模块和优秀平台之间的差距在于协调。您需要确保每个团队都从改进中受益，而无需强迫他们改变工作流程。

我们构建了一个新的平台，使这成为可能。通过 [Suga](https://addsuga.com)，您的 Terraform 模块将成为可视化构建块。每个团队都获得相同的安全默认设置。平台更新会自动使所有应用程序受益，而不仅仅是新应用程序。开发人员通过拖放来组合基础设施，而您的标准则在无形中自我强制执行。

[![](https://cdn.thenewstack.io/media/2025/11/de12750b-image1.png)](https://cdn.thenewstack.io/media/2025/11/de12750b-image1.png)

好的模块可以重复使用。优秀的模块则成为平台。[立即申请抢先体验](https://www.addsuga.com/#early-access)。