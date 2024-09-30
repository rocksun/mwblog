
<!--
title: 是什么促使用户使用基础设施即代码？
cover: ./cover.png
-->

用户采用基础设施即代码 (IaC) 的原因，既有 GUI 和 CLI 的局限性，也有 IaC 的优势。

> 译自 [What drives users to Infrastructure as Code?](https://itnext.io/what-drives-users-to-infrastructure-as-code-848e8640a506)，作者 Brian Grant。

在我的 [Infrastructure as Code 和声明式配置系列的前几篇文章中](https://medium.com/@bgrant0607/list/infrastructure-as-code-and-declarative-configuration-8c441ae74836)，我写到了 [Infrastructure as Code 的优点](https://medium.com/@bgrant0607/reflections-on-declarative-configuration-c2fe1c1e50d5)和[一些挑战](https://itnext.io/why-are-so-many-companies-working-to-improve-infrastructure-as-code-6c29bacdd1e1)。为什么云和 Kubernetes 用户一开始就采用 Infrastructure as Code (IaC)？相对于其他常见的用户界面，例如图形用户界面 (GUI) 和命令行界面 (CLI)，优缺点是什么？

## GUI

图形用户界面是无处不在的服务接口。它们相当流行，尤其在非开发人员用户中，甚至在许多应用程序开发人员中也是如此。

这是一个示例表单：

![Image of a GUI form](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*61TV38cqe9AgHZa-)

*用于运行容器的示例 GUI*

GUI 可以提供更简单的体验，特别是对于不熟悉所有产品功能和术语的新用户。许多用户体验设计专注于 GUI。

用户喜欢的 GUI 特征包括： 

- 逐步指导
- 渐进式披露
- 早期验证
- 自动完成和默认值
- 上下文帮助 / 文档 
- 错误解决协助 
- 导航工具 
- 复杂信息的组织 
- 动态、交互式更新 
- 数据的图形表示

那么，为什么用户从使用 GUI 转向 IaC 呢？一个原因是缺少重要功能，例如： 

- 可再现性/可重复性——创建配置的类似变体的功能 
- 从多个服务调配资源 
- 审查和批准 
- 组织政策强制 
- 执行版本控制和撤销 
- 注释/备注 
- 记录谁在何时、为何更改了内容 
- 共享/协作

这些功能可以通过 IaC 实现。

请注意，其中许多功能（例如撤消、评论、共享，以及谁更改了什么内容的详细信息）都可以通过其他产品的 GUI 使用。云 GUI 的 UX 远不及它本应达到的水平。

很常见的情况是，即使是相对常见的用例也没有在云 GUI 中得到明确支持。相反，冗长的文档教程和解决方案可能需要用户访问多个单独的 GUI 页面才能完成其任务。

以下是一个简单的示例，需要导航到五个不同的页面才能完成任务。我只展示 Google Cloud 的示例，因为我对此最熟悉。其他供应商（例如 AWS、Azure）看起来并不简单。

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SI4OJhnBnCueH61ofdUb0w.png)

*教程摘录*

## CLI

好的，命令行界面如何？对于精通供应商的服务、资源、功能、术语等且经常执行类似任务并且可以使用脚本和/或其 shell 历史记录执行类似命令的经验丰富的用户而言，CLI 可能很有效。

以下是使用 gcloud CLI 的上述示例。它看起来更长，主要是因为我将上面的 GUI 示例简写为仅显示页面转换。

```bash
gcloud compute networks subnets update SUBNET \
    --network=NETWORK \
    --stack-type=IPV4_ONLY \
    --range=10.1.2.0/24 \
    --region=REGION
gcloud compute instance-templates create TEMPLATE_NAME \
  --region=REGION \
  --network=NETWORK \
  --subnet=SUBNET \
  --stack-type=IPV4_ONLY \
  --tags=allow-health-check \
  --image-family=debian-10 \
  --image-project=debian-cloud \
  --metadata=startup-script='#! /bin/bash
    apt-get update
    apt-get install apache2 -y
    a2ensite default-ssl
    a2enmod ssl
    vm_hostname="$(curl -H "Metadata-Flavor:Google" \
    http://metadata.google.internal/computeMetadata/v1/instance/name)"
    echo "Page served from: $vm_hostname" | \
    tee /var/www/html/index.html
    systemctl restart apache2'
gcloud compute instance-groups managed create lb-backend-example \
   --template=TEMPLATE_NAME --size=2 --zone=ZONE_A
gcloud compute instance-groups set-named-ports lb-backend-example \
    --named-ports http:80 \
    --zone ZONE_A
gcloud compute firewall-rules create fw-allow-health-check \
    --network=NETWORK \
    --action=allow \
    --direction=ingress \
    --source-ranges=130.211.0.0/22,35.191.0.0/16 \
    --target-tags=allow-health-check \
    --rules=tcp:80
gcloud compute addresses create lb-ipv4-1 \
    --ip-version=IPV4 \
    --network-tier=PREMIUM \
    --global
gcloud compute addresses describe lb-ipv4-1 \
    --format="get(address)" \
    --global
 gcloud compute health-checks create http http-basic-check \
     --port 80
gcloud compute backend-services create web-backend-service \
    --load-balancing-scheme=EXTERNAL \
    --protocol=HTTP \
    --port-name=http \
    --health-checks=http-basic-check \
    --global
gcloud beta compute backend-services add-backend web-backend-service \
  --instance-group=lb-backend-example \
  --instance-group-zone=ZONE_A \
  --global
gcloud beta compute url-maps create web-map-https \
  --default-service web-backend-service
gcloud compute target-https-proxies create https-lb-proxy \
  --url-map=web-map-https \
  --ssl-certificates=www-ssl-cert
gcloud compute forwarding-rules create https-content-rule \
  --load-balancing-scheme=EXTERNAL \
  --network-tier=PREMIUM \
  --address=lb-ipv4-1 \
  --global \
  --target-https-proxy=https-lb-proxy \
  --ports=443
gcloud compute ssl-policies create my-ssl-policy \
  --profile MODERN \
  --min-tls-version 1.0
gcloud compute target-https-proxies update https-lb-proxy \
  --ssl-policy my-ssl-policy
gcloud compute backend-services update BACKEND_SERVICE_NAME \
    --iap=enabled,oauth2-client-id=ID,oauth2-client-secret=SECRET \
    --global
```

显然，这个“简单”的例子相当复杂。交互式资源创建可能不是 CLI 的最佳用例。基础设施资源往往包含大量属性，而像这样的场景需要相当多的资源。此外，这可能不是你每天都会做的事情，因此命令的精确顺序可能很难记住，需要记录在脚本或笔记本中。

用户喜欢的 CLI 属性包括：

- 可重复
- 减少上下文切换和导航
- 增量和迭代
- 可以处理和使用输出
- 使用脚本和笔记本自动化任务
- 可共享

然而，我个人认为，复杂命令长序列的脆弱性促使用户转向 IaC：

- 不同的初始状态通常需要不同的命令。特别是，更新通常需要与创建不同的命令。此外，CLI 命令不一定是幂等的。
- 错误处理比在通用编程语言中更难
- 不一定能够在不执行命令的情况下验证命令（例如，通过 dry run）

IaC 更健壮，因为它会根据初始状态自动确定要采取的操作，并且在发生短暂故障（例如，由于 API 配额耗尽或竞争条件）时，通常可以安全地再次应用。

## IaC

因此，用户采用 IaC 有充分的理由。它提供了一些特定的功能，并解决了常见的问题。

然而，虽然 IDE 中有一些语法自动完成，但从历史上看，与 GUI 和 CLI 相比，从头开始编写 IaC 模板/代码的帮助较少。很多重点都放在了 [重用现有模板](https://medium.com/@bgrant0607/what-is-it-with-template-catalogs-7637c24d5200) 上。

当然，也有一些例外。Azure 门户具有 [导出 ARM 模板](https://learn.microsoft.com/en-us/azure/azure-resource-manager/templates/export-template-portal) 的功能，这似乎非常有用。

这种情况似乎正在随着一些 [较新的 IaC 产品](/infrastructure-as-code-landscape-overview-2024-a066124e5989) 的出现而改善。例如，Firefly 可以 [为现有资源创建 IaC](https://www.firefly.ai/use-cases/iac-adoption)。

模板/模块的组合似乎是多个类别产品正在解决的领域，例如基于图表的界面，如 Brainboard 和 Massdriver，以及来自代码的基础设施产品，如 [Nitric](https://thenewstack.io/maximizing-terraform-modules-for-platform-engineering/)。

至于编写模块本身的帮助，有 [Structura](https://www.structura.io/)，它有点像 [Scratch](https://scratch.mit.edu/projects/editor/?tutorial=getStarted)，至少可以帮助确保语法正确。当然，还有新的尖端 AI 产品，它们目前无法始终如一地生成正确的 IaC。

IaC 有一个显著的学习曲线，并伴随着 [复杂性和工作量](https://medium.com/itnext/complexity-and-toil-in-infrastructure-as-code-6ca9a6d2af37)。在我看来，为了采用 IaC，我们不得不放弃很多东西。

我们也遇到了这种范式的局限性，这种范式是围绕 [人为驱动的、手工的流程](/infrastructure-as-code-is-artisanal-automation-2b6b7545c100) 设计的。但是 [经过 30 年](https://medium.com/@bgrant0607/infrastructure-as-code-reminds-me-of-make-run-all-15eb6628f306) 之后，我们应该进行范式转变。

你怎么看？如果你能提供等效的功能，你会更喜欢 GUI 或 CLI 而不是 IaC 吗？你对任何新的以 GUI 为中心的基于 IaC 的产品感兴趣吗？你希望从新的基础设施管理范式中得到什么？你使用过任何有趣的 IaC 替代方案吗？

欢迎在这里回复，或者在 [LinkedIn](https://www.linkedin.com/in/bgrant0607/) 或 [X/Twitter](https://x.com/bgrant0607/) 上给我发消息，我计划将此内容交叉发布。

如果您觉得这篇文章有趣，您可能还会对我在 [基础设施即代码和声明式配置系列](https://medium.com/@bgrant0607/list/infrastructure-as-code-and-declarative-configuration-8c441ae74836) 中的其他文章感兴趣。