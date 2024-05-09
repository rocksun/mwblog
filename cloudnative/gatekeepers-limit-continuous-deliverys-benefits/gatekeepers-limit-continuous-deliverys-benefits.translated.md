## 守门人限制持续交付的优势
![持续交付优势的守门人限制专题图片](https://cdn.thenewstack.io/media/2024/05/0f7b4026-restrain-1024x576.jpg)

开发人员体验和倦怠可能使平台工程成为焦点，但专注于持续交付很可能在贵组织中最大程度地改善开发人员体验 (DevEx)。

然而，对于那些自动化其部署管道的人来说，有一个障碍：部署守门人。

如果您不增加具有部署权限的人数，您将错过许多 [持续交付的优势](https://thenewstack.io/ci-cd/)。一个部署守门人会降低您在头 100 天内获得投资回报的机会，并永久限制您的软件交付绩效。

那么，这是如何发生的？

## 无法响应变化

一旦您自动化 [部署管道](https://thenewstack.io/ci-is-not-cd/)，您的工作系统就会发生巨大变化。您将节省许多小时的手动工作，并使部署过程更加可靠。这些好处通常非常明显，您可能会停止寻找进一步的收益。

接受当前部署过程的更快版本意味着无法响应变化。这会阻碍您的软件交付绩效，并降低您的软件对其用户和组织的影响。

在 [Octopus 部署调查](https://octopus.com/whitepapers/deployment-survey-report-2023) 中，我们发现，与部署人员多于一个的团队相比，只有一个部署守门人的团队在头 100 天内不太可能看到效率提升。

CD 工具带来了细粒度的基于角色的访问控制，因此部署人员不需要特权基础设施访问权限。您的自动化捕获了该过程，因此您的 CD 工具每次都会以相同的方式部署。您的 IT 服务管理工具可以捕获并简化变更审批。部署更具可重复性和可靠性。对自动化部署按“开始”应该是低风险和低仪式。它甚至可能不再是一项技术任务。

当您未能使用工具的特定于部署的功能时，会有两个隐藏的成本。它会延迟投资回报，并阻止自动化实现其全部承诺。与部署守门人相比，拥有多个部署人员的 96% 的组织在头 100 天内获得了效率提升，而部署守门人的组织只有 83%。

![在 100 天内报告效率节省的组织数量](https://cdn.thenewstack.io/media/2024/05/a2879b62-image2.png)

在 100 天内报告效率节省的组织数量 (n=250)。

您必须承认，[持续交付](https://thenewstack.io/continuous-delivery-gold-standard-for-software-development/) 和自动化部署管道改变了软件交付的性质。不要满足于可靠性改进。在您的组织之外寻找灵感，您会发现加快软件交付速度的行业同行。

充分利用现代软件交付优势团队、用户和组织。

## 守门对软件交付绩效的影响

自调查以来，我们进一步测试了我们对守门人的调查结果。我们研究了部署人员数量与 [加速 DevOps 报告](https://dora.dev/research/) 中吞吐量指标之间的关系。

**部署频率：**您的组织将代码部署到生产环境的频率

**变更前置时间：**代码变更进入生产环境所需的时间

拥有四个或更多部署人员的团队实现了最高的吞吐量绩效水平。他们的变更前置时间更短，部署更频繁。就其他两组而言，有一个有趣的结果：守门人的部署频率高于拥有两到三个部署人员的团队，但他们的前置时间更长。

图表显示了性能差异，最佳点位于左上角。

![守门对软件交付绩效的影响](https://cdn.thenewstack.io/media/2024/05/00797aef-image1.png)

守门对软件交付绩效的影响 (n=212)。

对守门的一种解释是部署仅部分自动化。

没有完全自动化的部署管道的团队可能需要守门人，因为他们必须执行需要特权访问的任务。他们可能会手动更新负载均衡器上的流量，或运行脚本来执行部署后任务，例如清除缓存。

找到一种方法来自动化这些最终任务将有可能安全地增加部署人员的数量。培训额外的部署人员是免费且匿名的 Octopus [部署能力评估](https://octopus.com/deployment-capability-assessment) 中的关键改进机会，您可以将其用作持续改进过程的一部分。

## 众多因素之一
**High-Performance Software Delivery**

High-performance software delivery requires many skills, but gatekeeping can throttle most other improvement attempts. If you have to wait for a single person or a small group of authorized deployers, then you are constrained from increasing your deployment frequency and decreasing your change lead time.

Gatekeeping is a constraint, so optimizing other parts of your software delivery will not have as much impact. Add more deployers and see how it changes your performance.

[YouTube.com/TheNewStack](https://youtube.com/thenewstack?sub_confirmation=1)

Technology moves fast, don't miss an episode. Subscribe to our YouTube channel to stream all of our podcasts, interviews, demos, and more.