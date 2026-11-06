<!--
title: Dropbox弃用AWS S3转向自研系统后，又收购Tigris进军AI开发者存储市场
cover: https://cdn.thenewstack.io/media/2026/11/89299b13-tri-wiranto-dlfzo0l9r74-unsplash-scaled.jpg
summary: Dropbox宣布以3.5亿美元收购AI对象存储初创公司Tigris，旨在向AI开发者和企业出售S3兼容存储基础设施，并推出DBX Agent Cloud服务。同时，Dropbox对其核心产品进行了重大AI升级，允许用户直接对文件执行编辑、整理等复杂任务。
-->

Dropbox宣布以3.5亿美元收购AI对象存储初创公司Tigris，旨在向AI开发者和企业出售S3兼容存储基础设施，并推出DBX Agent Cloud服务。同时，Dropbox对其核心产品进行了重大AI升级，允许用户直接对文件执行编辑、整理等复杂任务。

> 译自：[Dropbox ditched AWS S3 for its own in-house system. Now it’s buying Tigris to sell S3-compatible storage to AI developers.](https://thenewstack.io/dropbox-acquires-tigris-s3-alternative/)
> 
> 作者：Paul Sawers

Dropbox正在大规模进军AI基础设施领域，于周四宣布计划收购 [Tigris](https://www.tigrisdata.com/)，这是一家为AI应用提供对象存储的初创公司。

这家云存储巨头告诉 *The New Stack*，其收购Tigris的金额为3.5亿美元，此举旨在加速Dropbox自身向开发者和企业销售存储基础设施的雄心。事实上，在宣布收购消息的同时，Dropbox还公布了即将推出的 DBX Agent Cloud，该服务最初将允许开发者直接从Dropbox购买对象存储。

值得一提的是，Dropbox在构建存储基础设施方面并不陌生。从2015年开始，该公司[将超过90%](https://www.wired.com/2016/03/epic-story-dropboxs-exodus-amazon-cloud-empire/)的用户数据从亚马逊的S3云存储服务迁移到了名为 [Magic Pocket](https://dropbox.tech/infrastructure/how-we-optimized-magic-pocket-for-cold-storage) 的自研系统上，旨在提升性能并降低成本。但正如Dropbox首席商业官 [Eric Webster](https://www.linkedin.com/in/eric-webster-70a08b5/) 所解释的那样，向*外部*客户销售存储基础设施面临着完全不同的挑战。

Webster告诉 *The New Stack*：“为Dropbox运营基础设施与向开发者提供存储产品有着不同的需求。Tigris带来了成熟的商业产品、经验丰富的团队、开发者关系以及早期的客户吸引力。”

> “Tigris带来了成熟的商业产品、经验丰富的团队、开发者关系以及早期的客户吸引力。”

这种“客户吸引力”涵盖了一批诸如Amplified、Railway、Runpod和Replicate等公司，业务范围从开发者托管平台到GPU基础设施以及AI模型部署。这正是那些需要快速、可靠地访问大量数据的企业，通常它们需要在不同的环境中运行应用程序和AI模型。

## Tigris之眼

![首席架构师Yevgeniy Firsov，两侧分别为CTO Himank Chaudhary（左）和CEO Ovais Tariq](https://cdn.thenewstack.io/media/2026/11/3c97d500-team-photo-97abcf36bb0b26ba8e461bf4df5664fd-1024x683.jpg)

*首席架构师Yevgeniy Firsov，两侧分别为CTO Himank Chaudhary（左）和CEO Ovais Tariq*（图片来源：Tigris）

Tigris由前Uber工程师 [Ovais Tariq](https://www.linkedin.com/in/ovaistariq/)（CEO）、[Himank Chaudhary](https://www.linkedin.com/in/himankchaudhary/)（CTO）和首席架构师 [Yevgeniy Firsov](https://www.linkedin.com/in/efirsov/) 于2022年创立，构建了一个兼容S3的存储平台，允许开发者在不同的云和计算环境中保持其数据的可访问性。

对于训练AI模型的开发者来说，这意味着可以将大型数据集存储在一个地方，同时从多个提供商处租用计算能力。在这种情况下使用亚马逊S3可能会产生额外的跨区域数据传输成本（称为出口费用）以及延迟，特别是当计算发生在AWS之外时。Tigris通过自动将数据保持在所需位置附近来解决这个问题，同时对流出其存储服务的传输不收取任何出口费用。

该公司于2025年10月宣布获得了一轮 [2500万美元的A轮融资](https://www.tigrisdata.com/blog/series-a/)，投资方包括Spark Capital和现有支持者Andreessen Horowitz。

虽然Tigris的大部分吸引力在于其现有的产品、客户和开发者关系，但Dropbox看到了一个机会，可以将这种立足点转化为商业存储基础设施市场中规模更大的业务。

Webster说：“将这些优势与Dropbox大规模运营存储的经验相结合，将为我们提供进入该市场的更快途径。这次收购让我们能够建立在两个团队已经开发的内容以及从客户那里学到的经验基础之上。”

因此，这一雄心最清晰的体现之一就是 DBX Agent Cloud，Dropbox计划通过该服务向构建AI应用的开发者销售存储基础设施，如果该收购通过常规的监管审批程序，Tigris预计将提供底层的对象存储技术。

但为什么Dropbox要大力进军AI基础设施？为什么是现在？  
  
Webster表示：“AI应用正在创建和处理不断增长的内容量，从图像和视频到训练数据集和模型构件。随着模型和计算提供商的变化，这些内容需要一个稳定的家。”

> “AI应用正在创建和处理不断增长的内容量，从图像和视频到训练数据集和模型构件。”

Dropbox成立于2007年，近二十年来一直在应对存储和管理海量客户数据的挑战，对象涵盖从普通消费者到企业。现在，它希望将这些经验用于为构建自己应用的开发者服务。

Webster说：“DBX Agent Cloud将这一专业知识扩展到构建应用的公司和开发者，从独立的对象存储开始。”

最终的计划是接下来添加文件系统和内容处理功能，允许AI应用处理不同类型的内容、追踪文件并跨会话从上次中断的地方继续。

Dropbox尚未公布 DBX Agent Cloud的发布日期，也没有确切解释这两家公司的技术将如何整合。

Webster表示：“随着这些计划的推进，我们将分享更多关于技术整合和可用性的信息。”

至于现有的TigrisTigris客户，Dropbox承诺至少在最初阶段一切照常。Webster表示，当收购完成时，他们将“无需迁移或改变使用该服务的方式”，并且将“继续获得对Tigris产品的支持”。

未来的发展则不太确定，特别是随着Dropbox在Tigris的基础之上构建自己的文件系统和内容处理功能时。

Webster补充道：“随着产品的演进，我们将在做出任何影响客户的变更之前与他们直接沟通。”

## Dropbox让AI在文件上发挥作用

在周四宣布收购消息的同时，Dropbox还公布了其称之为核心产品“重大演进”的内容，该公司表示，这将“把AI驱动的功能直接带到客户现有的文件和工作流中”。

早在2023年，Dropbox就[推出了Dash](https://blog.dropbox.com/topics/product/introducing-AI-powered-tools)，这是一款由AI驱动的搜索工具，允许用户查找分散在Google Workspace、Microsoft 365以及Dropbox本身等服务中的信息。现在，该公司正在将事情推向更远，允许用户指示AI直接在他们的文件上工作，从编辑PDF和图像、重组文件夹、转录录音到完成多步骤任务。

Dropbox首席产品官 [Mike Torres](https://www.linkedin.com/in/miketorreshq) 告诉 *The New Stack*：“客户告诉我们，他们希望这些AI驱动的功能直接集成在他们内容和工作流已经存在的产品中。”

![Dropbox AI提出整理文件的计划](https://cdn.thenewstack.io/media/2026/11/bec4012b-product-static-proposed-plan-600x700-1.png)

*Dropbox AI提出整理文件的计划*

该公司去年已经开始[将Dash集成到Dropbox中](https://blog.dropbox.com/topics/news/fall-2025-release-dropbox-dash-context-aware-ai-teammate)，将AI驱动的搜索、文档摘要以及针对存储内容提问的能力引入到核心产品中。

Torres继续说道：“新体验建立在该基础以及我们从客户那里学到的经验之上，帮助他们从查找和理解信息转变为整理文件、编辑内容以及完成受支持的多步骤任务。”

> “我们希望客户拥有自由，能够使用最适合他们的AI工具。”

Dropbox表示，已有超过7万个团队获得了新功能的访问权限，不过该公司并未透露有多少团队正在积极使用它们。关于定价，Torres表示符合条件的标准版和高级版套餐包含一定配额的AI额度，客户可以根据需要购买更多。

![Dropbox内部的模型选择器](https://cdn.thenewstack.io/media/2026/11/c4dbf5f6-product-static-model-picker-600x700-1.png)

*Dropbox内部的模型选择器*

该公司还允许用户在Dropbox内部选择AI模型，并集成了包括ChatGPT和Claude在内的第三方工具。这些连接允许客户通过外部AI服务处理其Dropbox文件，而无需重复上传，生成的内容随后会被保存回Dropbox。

Torres说：“我们希望客户拥有自由，能够使用最适合他们的AI工具。”

这背后或许隐藏着与收购Tigris相似的理念：允许开发者选择他们在*哪里*运行AI应用，同时保持底层数据的可访问性。Dropbox正押注于能够将这一主张转化为一个可观的新基础设施业务，尽管收购尚未完成且 DBX Agent Cloud也没有发布日期，这种雄心将如何转化为开发者真正想要使用的产品还有待观察。