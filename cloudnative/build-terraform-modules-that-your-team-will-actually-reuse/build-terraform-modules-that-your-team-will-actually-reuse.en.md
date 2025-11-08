Many organizations struggle with Terraform module adoption, experiencing challenges such as:

* **Version fragmentation:** Different projects/teams end up on different versions.
* **Breaking changes:** Teams can’t upgrade without risking errors during or post-deployment.
* **Shadow modules:** Teams write their own when modules don’t fit their needs.

This guide shows how two software engineering principles can transform [Terraform modules](https://thenewstack.io/maximizing-terraform-modules-for-platform-engineering/) into components teams actually want to use.

## **From Monolithic to Modular: 2 Patterns**

### **Starting Point: What Most Teams Have**

Most teams start with working infrastructure: a bucket, some identity and access management (IAM) permissions and basic security settings. The problem isn’t that it’s broken; it’s just that everything is tangled together in one module:

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

This module has bundled in the bucket, the IAM role and the policies, but what happens when you need:

* The same bucket for an Elastic Container Service (ECS) task instead of Lambda? You can’t reuse this module because the role is hardcoded for Lambda.
* Multiple services to access one bucket? You’d need to copy and modify the entire module for each service.
* Just the bucket without the IAM role? They’re inseparably coupled.

This is why teams end up with slightly different copies of the same thing – `s3-module-lambda`, `s3-module-ecs`, `s3-module-ec2`.

## **Pattern 1: Separation of Concerns — 1 Module, 1 Purpose**

The first problem: Modules try to do too much. When your S3 module also creates IAM roles and policies, it becomes impossible to reuse for different services.

Single responsibility says each module does one thing well. Let’s separate our concerns with a module that only manages S3 buckets. No IAM roles. No policies. Just buckets with sensible defaults.

### **S3 Module — Just Manages Buckets**

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

**In practice:** Your S3 module will be more complex, requiring encryption, cross-origin resource sharing (CORS), life cycle policies and more. Keep IAM, networking and compute resources in separate modules so that they [become reusable](https://thenewstack.io/your-platform-engineering-toolkit-for-terraform-and-beyond/) across different services and teams.

## **Pattern 2: Composability — Modules That Work Together**

The second principle: Modules should compose cleanly. Each module requires a clear interface with predictable outputs that other [modules can use](https://thenewstack.io/experts-share-best-practices-for-building-terraform-modules/).

First, create your infrastructure resources using the separated modules:

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

Then wire them together with explicit permissions:

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

Because modules have predictable interfaces:

* Any service can use any bucket.
* Permissions are explicit and auditable.
* No hidden dependencies between modules.
* Each piece can be tested independently.

**In practice:** Your modules will be larger units — an “application stack” or “data pipeline” rather than individual resources. Standardized interfaces and outputs let modules work together, whether you’re composing buckets and policies or entire Virtual Private Clouds (VPCs) and Amazon Elastic Kubernetes Service (EKS) clusters. Predictable interfaces enable composition.

## **From Patterns to Platform**

These patterns solve the shadow module problem. Teams won’t need to bypass well-designed, composable modules. But you still face version fragmentation and breaking changes. When half your teams are on an older version and only new projects gain access to the latest version, every update now involves the added complexity of migration.

The gap between good modules and a good platform is coordination. You need to make sure every team benefits from improvements without forcing them to change their workflows.

We’ve built a new platform that makes this possible. With [Suga](https://addsuga.com), your Terraform modules become visual building blocks. Every team gets the same secure defaults. Platform updates benefit all apps automatically, not just new ones. Developers compose infrastructure through drag-and-drop, while your standards enforce themselves invisibly.

[![](https://cdn.thenewstack.io/media/2025/11/de12750b-image1.png)](https://cdn.thenewstack.io/media/2025/11/de12750b-image1.png)

Good modules get reused. Great modules become platforms. [Request early access today](https://www.addsuga.com/#early-access).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/08/a2faa3ef-cropped-c8b10469-rak-siva.jpg)

Rak Siva, vice president of engineering at Team Nitric, is deeply committed to elevating the experience for software developers. With a rich 15-year tenure in the software industry, he began his engineering journey immersed in the exhilarating challenges of the...](https://thenewstack.io/author/raksiva/)