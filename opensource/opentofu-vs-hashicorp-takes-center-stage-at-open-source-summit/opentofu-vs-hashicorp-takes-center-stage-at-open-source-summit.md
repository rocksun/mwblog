
<!--
title: OpenTofu与HashiCorp在开源峰会上占据中心舞台
cover: https://cdn.thenewstack.io/media/2024/04/361be1a9-zemlin-oss-na-2.png
-->

Linux 基金会负责人 Jim Zemlin 在活动开场主题演讲中支持 OpenTofu 对抗代码盗窃指控的斗争。

> 译自 [OpenTofu vs. HashiCorp Takes Center Stage at Open Source Summit](https://thenewstack.io/opentofu-vs-hashicorp-takes-center-stage-at-open-source-summit/)，作者 Alex Williams。

西雅图 — [InfoWorld](https://www.infoworld.com/article/3714980/opentofu-may-be-showing-us-the-wrong-way-to-fork.html) 的故事由 [Matt Asay](https://www.linkedin.com/in/mjasay/) 撰写，内容涉及 [OpenTofu](https://thenewstack.io/opentofu-1-6-general-availability-open-source-infrastructure-as-code/) 和 HashiCorp 发出的停止并终止函，在周二上午的 [北美开源峰会](https://events.linuxfoundation.org/open-source-summit-north-america/) 上占据了中心舞台。

4 月 3 日，InfoWorld 发表了 MongoDB 开发者关系副总裁 Asay 的一篇文章，他在文中声称 OpenTofu 是一个分支了 Terraform（一款广泛使用的基础设施即代码产品）的团队，“提取了与 Terraform V1.7 中首次实现的新移除块功能相关的 Terraform 代码，该功能是在 OpenTofu 分支创建几个月后根据 [商业软件许可证 (BUSL)](https://fossa.com/blog/business-source-license-requirements-provisions-history/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) 发布的”。

Hashicorp 运营着 Terraform 项目。该公司在s[大约七个月前](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/)将 Terraform 的许可证从 [Mozilla 开源公共许可证](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/) 更改为 [商业软件许可证](https://fossa.com/blog/business-source-license-requirements-provisions-history/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)。从那时起，真是经历了一段不平凡的旅程。

因此，Asay 撰写了这篇文章，并表示，“这看起来很像违反了 HashiCorp 的知识产权”。

OpenTofu 项目[否认了 HashiCorp 关于窃取代码的指控](https://thenewstack.io/opentofu-project-denies-hashicorps-allegations-of-code-theft/)。

在这种情况下，Asay 的文章之所以显得奇怪，是因为它的整体观感。他的雇主 MongoDB 在 [2018 年](https://techcrunch.com/2018/10/16/mongodb-switches-up-its-open-source-license/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) 转向了一个闭源许可证。而 Asay 撰写了这篇文章，同时发表的时间大约与 OpenTofu 从 Hashicorp 收到[停止并终止函](https://opentofu.github.io/legal-documents/2024-04-03%20HashiCorp%20C%26D/OpenTofu%20C&D%20-%20Redacted.pdf)的时间相同。

Linux 基金会执行董事 [Jim Zemlin](https://www.linkedin.com/in/zemlin/) 在开源峰会的开场主题演讲中表示，“不仅公开发生了这种情况，而且与此同时，OpenTofu 的维护者还收到了一家硅谷律师事务所的停止并终止函，要求他们删除该代码”。

## 调查“窃取代码”的指控

我非常同意 [Runtime 的 Tom Krazit 对 Asay 事件的分析：](https://www.runtime.news/hashicorps-threats-to-a-terraform-fork-fell-flat-and-might-have-made-it-stronger/)

> 对于 InfoWorld 来说，这似乎已经足够了，它在 Asay 文章的开头插入了一条编辑注释，称“根据这些文件，OpenTofu 社区似乎没有盗用 HashiCorp 的知识产权”（重点为他们所加），但保留了文章的标题和正文。
> 
> （一家备受尊敬的企业技术出版物为何继续给一位供应商营销主管提供空间，让他可以撰写任何他想要的内容，尤其是在他拥有巨大利益冲突的情况下，因为 MongoDB 和 HashiCorp 的开源许可策略之间存在相似之处，这一点令人费解。）

至于 OpenTofu？Zemlin 表示，该项目的负责人分析并驳斥了 Hashicorp 指控的每一个方面。

Zemlin 说：“我们拥有允许我们以自动化且准确的方式处理数万份贡献协议的工具。我们认真对待这些事情，幸运的是，OpenTofu 项目也这样做。”

“当他们听到这些指控时，他们立即进行了源代码起源分析。他们知道所有代码的位置、来源以及它在哪个许可证下。事实证明，这一分析驳斥了 HashiCorp 指控的每一个方面。”

这意味着什么？我们正在进入一个新时代——更多闭源许可和分支，随之而来的是更多律师和更多开发人员陷入困境。
