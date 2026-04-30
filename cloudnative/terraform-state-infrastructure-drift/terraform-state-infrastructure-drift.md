<!--
title: 为什么云环境挂了，Terraform 依然显示一切正常？
cover: https://cdn.thenewstack.io/media/2026/04/08b3a6ec-rizki-kurniawan-bksdivcgtrk-unsplash-scaled.jpg
summary: 本文探讨了 Terraform 状态文件与云环境实际状态脱节的问题。由于手动变更或服务自动缩放，IaC 往往无法反映真实情况。作者建议利用 CloudQuery 等工具通过 SQL 查询实时状态，从而更有效地识别配置漂移。
-->

本文探讨了 Terraform 状态文件与云环境实际状态脱节的问题。由于手动变更或服务自动缩放，IaC 往往无法反映真实情况。作者建议利用 CloudQuery 等工具通过 SQL 查询实时状态，从而更有效地识别配置漂移。

> 译自：[Why Terraform is green when your cloud is broken](https://thenewstack.io/terraform-state-infrastructure-drift/)
> 
> 作者：Joe Karlsson

那是一个周二的下午。Terraform plan 的结果很干净，没有任何变更。我反复检查了一遍，因为之前的几次部署都很混乱，我想确保万无一失。结果依然显示正常。于是我合并了 PR，接了杯咖啡，去参加一个下午 3 点关于第三季度路线图优先级的会议，其实我完全没必要参加那个会。

四十五分钟后，我有五条 Slack 消息在等着我。

我们的 API 在某个特定端点上返回 403 错误。服务日志毫无用处，正如当真正出问题时服务日志总是不给力一样（噪音很多，没有信号）。我们花了两个小时才追溯到 S3 存储桶策略。在三周前的一次事故中，有人在 AWS 控制台中手动收紧了策略以防止潜在的泄露。事故结束了，工单关闭了，Slack 讨论组也安静了。

没有人更新 [Terraform](https://thenewstack.io/your-platform-engineering-toolkit-for-terraform-and-beyond/ "你的 Terraform 及其他平台工程工具包") 配置。没有人提交 PR。状态文件没有这次变更的记录，因为这次变更从未经过 Terraform。

从 Terraform 的角度来看，策略与声明的完全一致。而从现实世界的角度来看，它已经变了三周，最后一次新部署终于在它面前碰了壁。

这不是什么恐怖故事。这只是一个普通的周二。

## 状态文件是如何失去同步的

!["This is fine" 表情包，关联到 Terraform 服务返回两周 403 错误的情景](https://cdn.thenewstack.io/media/2026/04/596d12c0-1.jpg)

[Terraform 状态](https://developer.hashicorp.com/terraform/language/state) 并不是实时记录。它是一个快照，一个捕获了上次 `terraform apply` 成功运行后基础设施样貌的 JSON 文档。env zero 对[该文件包含的内容及其重要性进行了深入阐述](https://www.env0.com/blog/a-guide-to-the-terraform-state-file "Terraform 状态文件指南")，其核心点就在于这个框架：“基础设施在上次 apply 后的快照”。而不是它现在的样子。

这种区别比听起来更重要。IaC（基础设施即代码）是一种意图声明。你声明的是*应该*存在什么。Terraform 将该声明与上次 apply 时*确实*存在的情况进行协调。但在那之后，云端一直在变动。

以下是 S3 存储桶策略的 Terraform 状态文件的实际样子（简略版；实际文件还包括 `terraform_version`、`lineage`、资源 `mode` 和提供者引用）：

```
{
  "version": 4,
  "serial": 47,
  "resources": [
    {
      "type": "aws_s3_bucket_policy",
      "name": "api_data",
      "instances": [
        {
          "attributes": {
            "bucket": "prod-api-data-bucket",
            "policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",...}]}"
          }
        }
      ]
    }
  ]
}
```

Serial 47。这是 Terraform 已知的状态写入次数：包括 apply、`terraform apply -refresh-only` 运行以及 `terraform state` 命令。每一次都被跟踪。而发生在 Terraform 操作之外的一切：都未被跟踪。如果存储桶策略在 serial 47 之后发生了手动更改，此文件反映的仍然是 serial 47 视角下的世界。

显而易见的问题是：`terraform refresh` 呢？（它在 Terraform 0.15 中被弃用；目前的等效命令是 `terraform apply -refresh-only`。）默认情况下，`terraform plan` 在比较之前也会从提供者那里刷新状态。它能捕获 Terraform 已经知道的资源的漂移。但对于某人在三个月前手动创建的存储桶，或者在事故期间作为临时方案添加的 IAM 角色，它无能为力。Terraform 没有这些记录，因此无从刷新。[这种差距不仅仅是已知资源的陈旧数据](https://thenewstack.io/bridging-the-data-gap-real-time-user-facing-analytics/ "缩小数据差距：实时面向用户的分析")。它是那些从未进入状态文件的资源。

> “这种差距不仅仅是已知资源的陈旧数据。它是那些从未进入状态文件的资源。”

手动变更是显而易见的罪魁祸首：凌晨 2 点应用的紧急修复、清理不彻底的实验、没人回来记录的控制台更改。但更隐蔽的问题是[服务管理的漂移](https://thenewstack.io/the-engineers-guide-to-controlling-configuration-drift/ "工程师控制配置漂移指南")。[AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) 会更改你的实例数量。RDS 在达到阈值时会[自动扩展存储](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PIOPS.StorageTypes.html#USER_PIOPS.Autoscaling)。[ECS 应用自动扩展](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html)会根据负载调整服务的期望任务数，而 Terraform 对此一无所知。这些都不经过 Terraform。这不属于人为错误。这是云端正在按照你配置的方式运行，只是你的状态文件设计之初就没打算跟踪这些。第三方集成、策略执行工具和成本优化器又在上面增加了一层复杂性。

我们通过 [env zero](https://www.env0.com/solutions/cloud-asset-management) 建立了稳健的流水线纪律：一致的运行、策略执行、团队级控制。但任何部署工具只知道经过它的东西。它告诉你通过流水线管理的资源。它不会告诉你某个 S3 存储桶在周四晚上 11 点被收紧了权限。

状态文件是一个快照。在人们工作、修补、尝试实验和做出务实妥协的环境中，这个快照可能会在某些关键方面过时几天甚至几周。

而危险的部分不仅仅是你不知道漂移的存在。而是你的下一次 `terraform apply` 将基于它所相信的世界版本进行操作。那位为了阻止泄露而在凌晨 2 点收紧 S3 存储桶策略的工程师？你的下一次部署会悄无声息地再次将其打开。Terraform 忠实执行了你的指令。它只是不知道在两次 apply 之间发生了什么。

## “只执行流水线”带来的问题

好吧，所以修复方案很显而易见，对吧？只要不做手动变更就行。强制执行流水线。如果没经过 Terraform，就不算发生过。

当然可以。祝你在规模扩大后依然能成功做到这一点。

一个 AWS 账号，一个区域，一个小团队：你或许能守住底线。你能感觉到基础设施的边界。漂移仍然会发生，但你能很快发现，因为覆盖面小，而且团队成员都知道运行着什么。

现在增加账号。预发布、生产、灾难恢复、跨区域冗余。增加一个拥有自己 AWS 组织、命名规范和在任何 IaC 规范建立之前就存在的一堆手动配置资源的被收购团队。现在你要维护几十个状态文件。AWS 控制台一次只能显示一个账号。GCP 控制台一次只能显示一个项目。脚本在失效前一直好用，而且你必须在知道要找什么*之前*就写好它们。这就是问题所在。漂移不会自我声明。

**控制台考古**：逐个打开账号，通过点击 EC2、S3、IAM、RDS 来尝试构建心理画像。对两个账号来说还行。到十个账号时就完全不可持续了。我刚查完一个账号，就会立刻对查过的第一个账号失去信心。我曾经花了一个周五下午手动比对三个账号的安全组与状态文件的描述。我发现了两处差异，但我也无法摆脱“我还漏掉了三处”的感觉。

**boto3 脚本阶段**：写一个脚本来枚举资源，转储到 CSV，然后与状态进行比对。我有一个脚本运行得很好，直到我们的规模超过了默认的页面大小，它开始静默地漏掉实例。`DescribeInstances` 是分页的，如果你没有正确实现分页循环，它只会返回第一页然后停止。没有任何错误。修复了那个问题后，S3 枚举脚本又因为不相关的原因停止工作了。最后我手里攒了一堆小脚本，每个覆盖不同的服务，每个都需要按照与我实际需求毫无关系的日程进行维护。

**手动审计**：要求团队负责人盘点他们团队正在运行的内容。这产生了一份人们*经常能想到*的清单。它漏掉了所有因为太熟悉而变得“隐形”的东西。

每种方法都撞到了同一堵墙：我必须先知道我要找什么，然后才能去找它。

## 查询实际运行的情况

![支持使用 SQL 查询云状态而非手动检查 Terraform 状态文件的表情包](https://cdn.thenewstack.io/media/2026/04/a91e80e4-2.jpg)

真正改变我工作方式的是：我不再将基础设施视为一组需要浏览的控制台，而是开始将其视为数据库。

[CloudQuery](https://www.cloudquery.io/product/cloud-asset-inventory) 将你真实的云状态同步到 SQL 表中：即你的 AWS 账号中现在存在什么，而不是 Terraform 上次记录了什么。你将其连接到账号，运行同步，然后像查询数据库一样查询基础设施。以下是我处理标签问题时的样子：

```
SELECT account_id, region, instance_id, tags
FROM aws_ec2_instances
WHERE tags->>'owner' IS NULL
ORDER BY account_id, region;
```

该查询会返回所有没有所有者（owner）标签的 EC2 实例，[跨越每个账号](https://www.cloudquery.io/hub/plugins/source/cloudquery/aws/latest/tables/aws_ec2_instances)，并显示在一个结果集中。不是按账号查询，不是按区域查询。我不需要编写特定于账号的脚本，也不需要记住我部署到了哪些区域。数据是标准化的且可查询的，写这个查询大概只花了面试两分钟。

你可以针对任何你关心的内容编写类似的查询：具有公共访问权限的 S3 存储桶、具有开放入口规则的安全组、具有 `*` 权限的 IAM 角色、未加密的 RDS 实例。[CloudQuery Hub](https://www.cloudquery.io/hub/) 为最常见的情况提供了预构建的查询，如果你不想从头开始的话。

状态文件告诉你 Terraform 认为什么在运行。而这会告诉你实际上什么在运行。

> “状态文件告诉你 Terraform 认为什么在运行。而这会告诉你实际上什么在运行。”

当你确实发现漂移时，修复方式取决于漂移的方向。如果 Terraform 正在管理一个在云端已不存在的资源，`terraform state rm` 可以将其从状态中移除而不会销毁任何东西。如果云端有一个资源*应该*受 Terraform 控制，`terraform import` 可以将其拉入。Terraform 1.5+ 增加了 `-generate-config-out` 来自动生成初始配置，尽管你仍需要进行审查和清理（它只是个脚手架，不是最终文件）。这两条路径都不轻松。但清楚你处于哪种情况，并在引发事故前发现它，才是工作的核心。

## 你不知道要去寻找的漂移

![展示寻找漂移的四个阶段的表情包模板](https://cdn.thenewstack.io/media/2026/04/7aad18fb-3.jpg)

不过，这种方法也有局限性：它仍然需要你知道该问什么。

大多数情况下，这没问题。我知道我关心的问题。我可以针对已知的风险模式编写查询并按计划运行。这很有效。

更难的问题是我*不知道要去寻找*的漂移。在事故期间被收紧的 S3 存储桶策略；某人在调试期间“临时”扩大且从未缩减回来的 IAM 角色；本应在实验后关闭但并未关闭的 EC2 实例。这些都不会产生响亮的报错。它们存在于声明状态和实际状态之间的鸿沟中，在某些东西撞上它们之前是不可见的。

我一直在思考的是，如果工具具有前瞻性而不仅仅是提供数据，会是什么样子——它能自行发现异常，而不是等待你的查询。例如：存在于云端但不在任何 IaC 状态中的资源；自上次同步以来发生更改的配置；跨账号看起来异常的模式。查询层涵盖了你已知的风险。我想要的是一个拥有足够上下文、能在不被询问的情况下告诉我什么值得关注的东西。

这种差距无法通过更频繁地运行 apply 或更严格地执行流水线来消除。只有当你不再将状态文件视为唯一的事实来源时，差距才会缩小。

我开头提到的 S3 事故是我最后一次“意外”捕获到的。因为在那之后，我有了可以观察的工具，而不是等待故障来告诉我真相。

如果你正在跨多个云提供商处理这个问题（如果你经历过合并或收购，你很可能正在经历），漂移问题会变得更加复杂。我在另一篇文章《[多云架构是我们的意外之举](https://markdowntohtml.com/multicloud-accident-thenewstack-2026.md)》中专门讨论了这一点。

如果你想亲自尝试这种查询方法，[CloudQuery 的产品页面](https://www.cloudquery.io/product/cloud-asset-inventory)有连接第一个云账号的设置说明。