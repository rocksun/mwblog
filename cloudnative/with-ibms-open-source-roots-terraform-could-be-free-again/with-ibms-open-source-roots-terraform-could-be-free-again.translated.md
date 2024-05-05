# Terraform 能否在 IBM 的所有权下回归开源？

![Terraform 能否在 IBM 的所有权下回归开源？的特色图片](https://cdn.thenewstack.io/media/2024/04/42186af6-charlie-harris-i99y2odfl_k-unsplash-1-1024x683.jpg)

[IBM](https://www.ibm.com?utm_content=inline+mention) 即将 [收购](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/) [HashiCorp](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/)，而 HashiCorp 对 Terraform 采取热情的版权执行，这引发了关于 [潜在转变](https://thenewstack.io/opentofu-amiable-to-a-terraform-reconciliation/) 的疑问，即 Terraform 将回归更自由的开源模式 [Terraform](https://thenewstack.io/terraform-cloud-now-offers-less-code-and-no-code-options/)。

关于在 IBM 的指导下，在完成对 HashiCorp 的收购后可能发生的变化的线索可以追溯到几十年前的 2000 年代初期。在 2003 年的一个透明时刻，IBM 在 [对 [软件提供商 SCO](https://www.eweek.com/servers/new-tool-roots-out-sco-code/) 提出的投诉的答复](http://www.groklaw.net/pdf/Doc-27.pdf) 中，不仅详细说明了其对社区开源的贡献，还说明了其开源理念。其立场已从之前的模式转变，即主要提供专有产品和服务，该模式可以追溯到 [半导体](https://thenewstack.io/silicon-genesis-stanfords-oral-histories-of-the-semiconductor-industry/) 尚未发明之前。

在诉讼中，SCO 声称 IBM 和众多其他软件供应商和服务提供商侵犯了 SCO 对 [Linux](https://thenewstack.io/past-25-years-linux-changed-world-around-us/) 代码的所有权主张，而 IBM 和其他组织为 Linux 开源操作系统做出了贡献。

IBM 不同意。

IBM 在对 SCO 投诉的答复中表示：“IBM 一直积极参与开源运动，在过去五年中对 Linux 业务投入了大量资金。”“该公司参与了对其运营至关重要的各种 Linux 项目，并为更广泛的开源社区做出了贡献。”

那时，IBM 已开始提供其在答复中描述的“全面的产品阵容”，该阵容支持 Linux，包括服务器、[大型机](https://thenewstack.io/the-key-for-a-successful-mainframe-devops-strategy/)、内存解决方案和广泛的软件产品，以及支持服务。IBM 指出，它一直在根据 [GNU 通用公共许可证 (GPL)](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/) 向 Linux 贡献源代码。IBM 表示，IBM 做出的贡献已包含在其他公司（如 SCO）根据 GPL 分发的 Linux 产品中。“因此，IBM 有权对其贡献获得 GPL 的保护”，IBM 说。

但随后事情发生了恶劣的转变，IBM 认为这反映了 SCO 无法创建成功的商业模式。“尽管进行了首次公开募股，但 SCO 仍难以围绕 Linux 建立成功的业务”，IBM 说。“其 Linux 业务模式从未盈利，该公司整体在放弃 Linux 业务后才实现盈利。相反，SCO 一直在寻求从 [Unix](https://thenewstack.io/fosdem-24-can-the-unix-shell-be-improved-hell-yes/) 技术中提取利润，尽管它在 Unix 的开发中没有发挥任何作用。”

快进到二十多年后，HashiCorp 向 Terraform 分叉版本创建者发送了一封 [停止并终止函](https://thenewstack.io/oracle-suse-tussle-with-red-hat-over-the-business-of-open-source/)，声称其侵犯了版权。HashiCorp 声称 [OpenTofu](https://thenewstack.io/opentofu-vs-hashicorp-takes-center-stage-at-open-source-summit/) 代码属于 HashiCorp 的 Terraform BSL 许可证。与此同时，[OpenTofu 声称](https://opentofu.org/blog/our-response-to-hashicorps-cease-and-desist/) 在答复中，所使用的代码在 BSL 许可证实施之前就已经在之前的 Mozilla 公共许可证 v2.0 (MPL 2.0) 下可用。此大胆举动是在 HashiCorp 宣布 [更改其领先的基础设施即代码平台 (IaC) Terraform 的许可条款](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/) 之后进行的，即 2023 年 8 月。它用商业源代码许可证 (BSL) v1.1 替换了其开源 MPL，该许可证限制了在生产中使用代码。

HashiCorp 和 OpenTofu 项目的代表拒绝置评。IBM 没有回复要求置评的电子邮件。

最大的问题是，在 IBM 最近决定对其使用进行限制后，HashiCorp 的 Terraform BSL 许可证在 IBM 的指导下如何改变，而过去 Terraform 的通用 MPL 许可证则更加自由。

## 现在如何
**如果我是 IBM 负责 HashiCorp 交易的领导者，我会做的第一个决定是将所有 HashiCorp 产品迁移到 Apache-2.0，并确保在最初的新闻稿中突出显示该决定。**
— Kelsey Hightower (@kelseyhightower)
[2024 年 4 月 23 日]

因此问题仍然存在：一旦 HashiCorp 落入 IBM 旗下，它是否会放弃其软件许可证，取消对 OpenTofu 制造商因涉嫌侵犯版权而提出的索赔，并恢复为限制较少的 GPL 许可证？这不仅仅是 IBM 应该或可以做什么的问题，而是它可能采取特定行动的原因。

对于许多人来说，尤其是开源倡导者，答案是 IBM 可能会将 HashiCorp 转移到 BSL 许可证中的 Terraform 许可证恢复到其最初的、更自由的开源特权。它甚至可能具有良好的商业意义，而争论的焦点也在于 HashiCorp 试图通过绝望地将 Terraform 中的投资货币化来收回其在该项目中的慷慨投资，该项目已成为 [Kubernetes](https://thenewstack.io/kubernetes/) 的领先 IaC 工具。 [Bryan Cantrill](https://www.linkedin.com/in/bryan-cantrill-b6a1/)，[Oxide Computer Company](https://oxide.computer/) 的联合创始人兼首席技术官。“SCO 诉讼的有趣之处在于，你也许可以将诉讼视为一种失败的商业模式的墓志铭，而诉讼的范围就是剥离专有基础设施软件的墓志铭，而 HashiCorp 对 Terraform 分支的禁止和停止以及 BSL 也许将成为受限开源时代的墓志铭，我们可以回归真正的开源时代。”

HashiCorp 旨在阻止 OpenTofu 项目的禁止和停止信函遭到了争议。Cantrill 说，HashiCorp 的要求代表了“非常糟糕的行为”。“这种行为与 IBM 不符。也许我在这里过于乐观，但我认为 IBM 有一个真正的机会向世界展示我们所了解的 IBM，”Cantrill 说。“我的意思是，我认为它再次错过了练习，除了这些之外，总是会有失误。但我认为 IBM 广泛地理解，对社区有利的事情最终将对 IBM 有利。”

## Red Hat 历史

尽管如此，Terraform 许可证在更大背景下的命运仍然不确定。IBM 以 64 亿美元收购 HashiCorp，而 IBM 在 2023 年的收入超过 620 亿美元，这笔交易很重要，但并不是公司的成败交易，因此 Terraform 许可证将代表 IBM 财富中相对较小的一部分。

IBM 历来利用其对 [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) 的收购来加强其在云原生基础设施中的地位，尤其是在 Linux 领域。但在 IBM 收购 Red Hat 之后，至少有一项举措偏离了纯粹的开源模式，继 Red Hat 去年决定 [限制对 RHEL 代码的访问](https://thenewstack.io/oracle-suse-tussle-with-red-hat-over-the-business-of-open-source/) 仅限付费客户，而之前任何人都可以免费下载该代码。

从这个更广泛的角度来看，IBM 和 HashiCorp 似乎会优先考虑做出最有利于业务的决策。这可能涉及在收购完成后从 Terraform 的商业实体许可证 (BEL) 中寻求收入。

“毫无疑问，当 HashiCorp 更改许可证时，他们知道会发生这样的事情。最本质的问题是如何在提供商业服务的能力与开源商业模式的结合之间取得平衡，并且没有正确答案——这在某种程度上是存在的，”
[Gary Orenstein](https://www.linkedin.com/in/garyorenstein/)，密码保护提供商 [Bitwarden](https://bitwarden.com/) 的首席客户官告诉 The New Stack。“所以，我认为 HashiCorp 肯定知道会发生这种情况，因此可能从一开始就‘说我们，你知道，我们将尽可能激进地合法地处理这件事，因为他们做出了一个决定，即我们现在正在这样做对公司有利，你必须执行它。’”

尽管如此，此次收购应该“总体上向开源倾斜”，“具体来说，IBM 在开发自己的云产品方面不太成功，可以说，HashiCorp 已经使用 Terraform 识别并填补了云部署的控制点。这对于处于正中间非常有价值，”Orenstein 说。“我可以想象 IBM 现在正在讲述一个故事，‘无论您想使用 [Amazon](https://aws.amazon.com/?utm_content=inline+mention)、Azure、

YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
[频道](https://youtube.com/thenewstack?sub_confirmation=1)，可流式播放我们所有的播客、访谈、演示等。