<!--
title: 开源何其重要，岂容掺沙
cover: https://cdn.thenewstack.io/media/2025/07/c6fe18df-software1.jpg
summary: 文章讨论了开源定义的模糊化问题，以及由此可能带来的信任危机和创新减缓。强调了维护开源原则的重要性，并介绍了分叉作为社区自我保护和保持生态系统健康的手段。
-->

文章讨论了开源定义的模糊化问题，以及由此可能带来的信任危机和创新减缓。强调了维护开源原则的重要性，并介绍了分叉作为社区自我保护和保持生态系统健康的手段。

> 译自：[Open Source Is Too Important To Dilute](https://thenewstack.io/open-source-is-too-important-to-dilute/)
> 
> 作者：Dan Lorenc

[开源软件 (OSS)](https://thenewstack.io/open-source/) 正受到攻击——而且不仅仅是来自那些植入恶意软件或玩弄漏洞扫描器的常见嫌疑人。

如今，“开源”的定义正在悄然瓦解。一些公司正在将“源代码可用”的代码重新包装成开源，从而对社区和更广泛的生态系统产生下游影响。当这些界限变得模糊时，信任就会破裂——而没有信任，开源就行不通。

如果我们希望开源保持可持续性和影响力，我们不仅需要捍卫代码，还需要捍卫支撑它的原则。

## 开源的定义至关重要

[开源促进会 (OSI)](https://thenewstack.io/open-source-initiative-hits-the-road-to-define-open-source-ai/) 是一个非营利组织，它为开源软件生态系统奠定了基础，并在几十年前努力定义了开源。它确定了 [10 项标准](https://opensource.org/osd)，其中包括免费再分发、作者源代码的完整性以及不歧视个人和团体等。这些标准是保证公司可以使用 OSS，而不必每次开发人员安装软件包时都致电其法律部门。

对这些原则的信任推动了创新。这就是为什么开源占据了我们今天使用的应用程序中 [90% 的代码](https://www.sonatype.com/blog/the-transformation-of-open-source-lessons-from-the-past-decade)。每次我们允许不符合开源定义的许可证被视为开源时，这些保证都将不再有效，从而减缓了开源所能实现的创新。

## 许可变更的连锁反应

不幸的是，这些标准并非适用于所有用例。我们已经看到供应商通过一个真正的开放项目来建立吸引力。然后，由于担心货币化或竞争，他们根据“源代码可用”模型重新许可它，并带有诸如“禁止商业用途”或“仅当您不是竞争对手时”之类的限制。

但这不是开源的运作方式。今天的软件是深度互连的。每个项目——无论多么小或孤立——都依赖于依赖项，而这些依赖项又依赖于其他依赖项，一直到链的末端。限制该链中一个环节的许可证可能会破坏整个链。

当开发人员开始犹豫是否可以使用某个库时，创新就会减缓。贡献枯竭。整个项目停止工作。安全漏洞无法修复。维护变得更加困难。使 OSS 具有魔力的网络效应开始瓦解。

最健康的开源项目之所以蓬勃发展，是因为竞争对手可以对其进行协作。看看 [Kubernetes](https://github.com/kubernetes/kubernetes) 和 [Linux 内核](https://en.wikipedia.org/wiki/Linux_kernel)。这些项目由通常是竞争对手的个人和组织维护。如果许可条款根据他们的工作对象或公司的赚钱方式排除他们中的任何一个，那么这些项目将永远不会成功。

## 分叉保持生态系统的诚实和健康

分叉是 OSS 社区保护自己的方式。当 HashiCorp 根据商业源代码许可证 (BSL) [重新许可 Terraform](https://www.hashicorp.com/en/blog/hashicorp-adopts-business-source-license)——阻止竞争对手基于该工具构建时——社区启动了 [OpenTofu](https://opentofu.org/blog/opentofu-announces-fork-of-terraform/)，这是一个在 OSI 批准的许可证下分叉的项目，[得到了主要贡献者和供应商的支持](https://thenewstack.io/how-opentofu-happened-and-whats-next/)。

Redis [从](https://redis.io/blog/redis-adopts-dual-source-available-licensing/) 伯克利软件发行版 (BSD) 过渡到专有许可证是一个商业决策。但它留下了一个漏洞——社区对其进行了分叉。该分叉变成了 [Valkey](https://valkey.io/)，该项目由最依赖它的人员和平台继续管理。如今，[Valkey 由一个中立基金会维护](https://thenewstack.io/valkey-will-not-just-be-a-redis-retread/)，以确保没有任何一家公司可以将其从开源中夺走。它的用户社区来自全球各地，并与其他许多技术社区重叠。

这就是健康的生态系统所做的。当项目改变方向时，分叉允许社区掌控并坚持价值观。最重要的是，它们是创新持续进行的方式。

## 开源值得捍卫

开源品牌花了数十年才建立起来。它是软件历史上最成功、最受信任的想法之一。但它之所以值得信赖，是因为它意味着什么。

组织可以根据自己的意愿许可他们的代码。但如果他们要使用“开源”一词，他们应该言行一致。如果不是，他们应该称其为其他名称——并承担责任。

OSI 无法单独强制执行其定义。它依赖于社区来维护它。如果我们希望开源蓬勃发展，我们必须保护使其强大的因素：许可证、治理、社区以及对它意味着什么的共同理解。