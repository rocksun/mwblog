
<!--
title: 平台团队：自动化基础设施需求收集
cover: https://cdn.thenewstack.io/media/2024/07/53b35cfb-automate.png
-->

通过使用自动化的资源规范来弥合开发和运维团队之间的差距，您可以创建一个更加和谐和高效的部署流程。

> 译自 [Platform Teams: Automate Infrastructure Requirement Gathering](https://thenewstack.io/platform-teams-automate-infrastructure-requirement-gathering/)，作者 Rak Siva。

应用开发中最具挑战性的问题之一是开发团队和运维团队之间的脱节。沟通挑战很容易导致期望不一致和部署失败。这两个团队之间最关键和最脆弱的沟通领域之一是基础设施需求，多年来似乎无法解决。

但现在终于有了解决这种沟通差距的方案：自动化来简化基础设施需求收集。

## 沟通挑战

平台工程团队经常面临从开发团队收集有关其应用程序的准确需求的困难。开发人员通常不知道所需的特定[基础设施信息](https://thenewstack.io/infrastructure-from-code-gives-ops-needed-freedom/), 可能会提供不完整或不正确的数据。

当然，还有更极端的“扔过围栏”的情况。一旦开发人员完成应用程序逻辑的构建，他们就会将其交给[平台团队，让他们费力地弄清楚需要哪些基础设施](https://thenewstack.io/your-platform-engineering-toolkit-for-terraform-and-beyond/), 配置和权限才能在云中可靠、安全且高效地运行它。

基础设施需求沟通不畅会导致基础设施漂移，即部署的基础设施不再符合应用程序的实际需求。这种漂移会导致应用程序失败，从而导致压力重重的部署日、深夜故障排除会议和令人恐惧的战情室。

## 基础设施漂移及其后果

基础设施漂移是指基础设施的实际状态偏离了[基础设施即代码 (IaC)](https://thenewstack.io/infrastructure-as-code-is-dead-long-live-infrastructure-from-code/)脚本中定义的预期状态。鉴于手动沟通基础设施需求的挑战，团队遇到漂移并不奇怪。问题包括：

* **手动更改**：开发人员或运维团队可能会对基础设施进行手动更改，而不会更新 IaC 脚本。
* **更新不一致**：对应用程序的更新可能不会反映在基础设施配置中。
* **缺乏沟通**：开发人员可能无法将新的需求或更改有效地传达给运维团队。

基础设施漂移的后果很严重：

* **部署失败**：配置不匹配会导致部署失败，从而导致应用程序停机。
* **压力增加**：运维团队经常不得不处理最后一刻的修复，导致长时间工作和高压力水平。
* **信任度降低**：频繁的部署问题会损害开发团队和运维团队之间的信任，使未来的部署更加困难。
* **成本更高**：基础设施漂移会因停机造成的收入损失、配置错误的资源造成的额外支出、解决问题所需的劳动力成本增加以及需要修复的安全漏洞而产生成本。

解决这些基础设施漂移问题的方案在于自动化，这些问题源于沟通基础设施需求的挑战。让我介绍一下资源规范的概念，它可以自动将运行时应用程序需求传达给运维团队。

## 解决方案：自动化的资源规范

想象一下，一个系统可以从应用程序代码中直接推断出所需的基础设施资源。该系统将生成一个资源规范，充当实时文档，详细说明应用程序的运行时需求。然后，可以使用此规范来自动配置基础设施，确保部署的资源与应用程序的需求完全匹配。

还可以想象，虽然基础设施需求是从应用程序代码中推断出来的，但运维团队仍然保留对关键决策的控制权。他们为每个资源选择云提供商、服务和安全配置，使他们能够运用自己的专业知识并执行最佳实践。这确保了基础设施保持健壮并符合组织标准，将自动化与专家监督相结合。

这就是[基础设施即代码 (IfC)](https://thenewstack.io/terraform-isnt-dead/)这一新概念的核心，它建立在基础设施即代码 (IaC) 的基础之上。这意味着[像 Nitric 这样的 IfC 框架](https://github.com/nitrictech/nitric)可以为运维团队提供他们一直在寻找的解决方案：应用程序所需资源和权限的实时、详细规范。

### 自动化资源规范示例

以下是如何从应用程序代码生成资源规范的示例。此应用程序每天运行一次，并发布包含 URL 的更新事件。

```py
from nitric.resources import api, bucket
from nitric.application import Nitric
from nitric.resources import schedule, bucket, topic
from nitric.application import Nitric

images = bucket("reports").allow("deleting","writing")
updates = topic("updated").allow("publish")

processor = schedule("process-reports")
@processor.every("5 days")
async def process_transactions(ctx):
    download_url = await images.file('report.csv').download_url(3600)
    await updates.publish({
        'url': download_url
    })

Nitric.run()
```

从这段代码片段中，Nitric 框架收集了以下信息：

1. 存储桶资源：
    - ID：reports
    - 配置：默认设置。
2. 主题资源：
    - ID：updated
    - 配置：默认设置。
3. 定时任务资源：
    - ID：process-reports
    - 配置：目标服务 `hello-world_services-hello`，每五天执行一次。
4. 策略资源：
    - ID：eccfffd7a5e31407be6f7a5663665df4
    - 配置：允许 `hello-world_services-hello` 服务对 reports 存储桶进行读写操作的策略。
5. 策略资源：
    - ID：74e4fa18c1527363767c00582b792ed9
    - 配置：允许 `hello-world_services-hello` 服务对 updated 主题执行自定义操作 200 的策略。
6. 服务资源：
    - ID：`hello-world_services-hello`
    - 配置：具有镜像 `hello-world_services-hello`、一个工作进程和一个环境变量 `NITRIC_BETA_PROVIDERS` 设置为 true 的服务。

此信息被编译成资源规范，确保所有必要的资源都得到准确且一致的配置。

注意：ID 是自动生成的，用于唯一标识资源。

## 自动应用资源规范

自动生成资源规范解决了上面讨论的通信和漂移问题的大部分。但平台团队可以从自动将这些规范应用到他们创建的 IaC 模块中获得更多好处。像我上面示例中使用的 [Nitric](https://nitric.io) 这样的框架也会自动为平台团队编写部署脚本。

使用资源规范，每个组件都映射到相应的 IaC 模块。例如，如果应用程序指定了一个存储桶资源，目标云提供商是 AWS，系统将使用 Terraform 模块来配置一个计划处理程序：

```py
# Create role and policy to allow schedule to invoke lambda
resource "aws_iam_role" "role" {
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "scheduler.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy" "role_policy" {
  role = aws_iam_role.role.id
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = "lambda:InvokeFunction",
        Resource = var.target_lambda_arn
      }
    ]
  })
}

# Create an AWS eventbridge schedule
resource "aws_scheduler_schedule" "schedule" {
  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression_timezone = var.schedule_timezone

  schedule_expression = var.schedule_expression

  target {
    arn      = var.target_lambda_arn
    role_arn = aws_iam_role.role.arn

    input = jsonencode({
        "x-nitric-schedule": var.schedule_name
    })
  }
}
```

这种自动映射确保部署的基础设施与应用程序的要求保持同步，防止漂移并降低部署失败的可能性。

## 不再“抛砖引玉”

通过使用自动资源规范弥合开发和运维团队之间的差距，可以创建一个更加和谐和高效的部署流程。这种方法不仅降低了基础设施漂移和部署失败的风险，而且促进了团队之间更好的沟通和信任。采用这种方法可以带来更可靠、更轻松的部署和更强大的基础设施。

1. **一致性**：自动资源规范确保部署的基础设施与应用程序的需求相匹配，降低了漂移的风险。
2. **效率**：通过自动生成和配置资源，缩短了部署时间，并将手动干预的需求降至最低。
3. **减少压力**：运维团队可以相信基础设施将被正确配置，从而实现更顺畅的部署和更少的深夜故障排除。
4. **改进沟通**：开发人员无需担心手动指定基础设施需求；系统会自动处理，确保准确传达需求。

通过查看我们使用 [开源 Nitric 框架](https://github.com/nitrictech/nitric) 构建的内容，了解更多关于这种方法的信息。我们很乐意收到您的反馈、想法和贡献，以帮助自动化平台工程中最繁琐的部分。
