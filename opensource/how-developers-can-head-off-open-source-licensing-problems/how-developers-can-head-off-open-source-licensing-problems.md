
<!--
title: 开发者如何避免开源许可问题
cover: https://cdn.thenewstack.io/media/2024/06/6153560b-problems-with-open-source.jpg
-->

即使是前端也无法避免开源许可带来的问题。了解开发人员可以采取哪些措施来避免潜在的麻烦。

> 译自 [How Developers Can Head Off Open Source Licensing Problems](https://thenewstack.io/how-developers-can-head-off-open-source-licensing-problems/)，作者 Loraine Lawson。

使用开源可能会出现问题，前端也不例外。从软件损坏到许可证变更，开源软件可能会“背叛”开发人员。

“[Logz.io](https://logz.io/)” 首席布道师 [Dotan Horovits](https://www.linkedin.com/in/horovits/?originalSubdomain=il) 表示：“前端与任何其他软件没有区别。当然，它存在风险。” Horovits 作为云原生计算基金会 (CNCF) 大使，是开源倡导者，但他也会谈论开源的负面影响。

## 开源变质

他指出了 [2022 年 Marak Squires 事件](https://thenewstack.io/is-open-source-really-free-if-we-arent-allowed-to-break-it/)，该事件中，Marak Squires 恶意破坏了 faker.js（当时有 250 万次下载）和 colors.js（事件发生时有 2240 万次下载）库。

Horovits 说：“这影响很大，直到 [npm](https://thenewstack.io/npm-security-woes-continue-amidst-a-series-of-cdn-attacks/) 回滚并阻止了连锁反应的进一步蔓延。所以是的，前端就像我们一样容易受到攻击。这不是关于领域，而是关于软件。”

还有其他例子，例如 [HashiCorp 更改 Terraform 许可证](https://thenewstack.io/opentofu-vs-hashicorp-takes-center-stage-at-open-source-summit/)。Terraform 最初是在 Mozilla 公共许可证 v2.0 (MPL 2.0) 下发布的，后来更改为商业源代码许可证 (BSL) v1.1，该许可证不是开源的，而是被认为是“源代码可用”。这导致 Terraform 社区创建了 OpenTF，并由 [Linux 基金会将其作为 OpenTofu](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/) 采用。

Horovits 告诉 The New Stack：“这不仅仅是重新许可。它还将 Terraform 注册表（一个权威的地方，可以说是放置所有 Terraform 模块的中心）对其他工具关闭。”

[Elasticsearch 是另一个例子](https://www.elastic.co/blog/licensing-change)。Elastic 将 Elasticsearch 及其数据分析工具 Kibana 从 Apache 2.0 许可证更改为双重许可，即服务器端公共许可证 (SSPL) 和 Elastic 许可证。但 Horovits 说，这不仅仅是许可证变更。

他说：“他们有从应用程序本地收集遥测数据的发送器，然后将其发送到后端 Elasticsearch 集群进行存储、索引等；并且十多年来，它一直是开源的。现在他们改变了后端——这一点众所周知。人们可能不太了解的是，即使是那些仍然使用 Apache 许可证的发送器——这对于所有目的来说都是一个开源许可证，获得了 OSI [开源计划] 的批准——他们也进行了更改，以便他们检查发送到的后端集群，这并不属于开源。如果目标集群、远程集群没有……授权，那么它将无法工作。它会崩溃。”

Linkerd 提供了另一个有问题的例子。在那里，源代码仍然在开源许可证下，但 [Linkerd 不再发布可部署的工件](https://linkerd.io/releases/)。

“除了许可证之外，还有合同，可以说是协议，与社区的协议。长期以来，社区一直同意该项目发布可部署的工件，您可以使用这些工件在生产环境中部署和使用，但现在情况不再如此，”他说。

“不再如此的原因不是由代表整个社区的所有 [人员] 的治理委员会共同决定的。它主要是由单个供应商驱动的，目的是引导希望将 Linkerd 部署到生产环境中的组织使用其商业产品。”

## 开源项目变质的预警信号

Horovits 说，许可证只是故事的开始。使用 [开源软件的开发人员和组织需要采取更成熟](https://thenewstack.io/3-ways-to-drive-open-source-software-maturity/) 的使用方式。

他说：“人们需要更成熟地看待开源，理解并提出更多问题，而不仅仅是哪种许可证。还要问谁在开源背后？是单个供应商，还是可持续的多样化实体，甚至可能是供应商和最终用户的混合体，这将保证更好的可持续性和降低此类事件发生的可能性？” “是否有明确的治理策略来 [明确定义开源](https://thenewstack.io/open-source-initiative-hits-the-road-to-define-open-source-ai/) 中可以进行的修改方式——当然包括许可证，甚至更小的修改——以及谁可以加入？”

他表示，早期的一个麻烦信号可能是突然间外部贡献被阻止，或者项目维护者对社区的建议没有做出回应。

“为什么会出现这种情况？可能是因为，在某种程度上，它与他们围绕开源开发的商业产品相冲突，或者他们认为这并不是他们的优先事项，”他说。“这些事情不应该发生在开源中。”

他补充说，治理政策也可能发出警告信号，开源代码和专有代码的混合也是如此。

## 检查许可证
Horovits 说，如果有人决定更改许可证，开发人员能做的事情并不多，除了可能从早期版本中分叉项目。许可证更改不会追溯到早期版本。

开发人员可以做的是与法律或[开源程序办公室](https://thenewstack.io/does-your-organization-need-an-open-source-program-office/)合作解决许可问题。这是因为即使有开源许可证，也可能存在对开发人员及其组织造成影响的条款。

开发人员还应在每次更新[开源代码](https://thenewstack.io/how-donating-open-source-code-can-advance-your-career/)时执行许可证检查，以确保许可证没有更改。

“如果你自动更新到下一个版本，如果下一个版本已经重新授权，那么你就会自动暴露，而没有人对此进行任何判断，仅仅因为你拉取了最新版本，就是这样，”他说。

## 检查源代码
他还建议进入代码以了解其工作原理，并检查可能表明未来问题的异常代码。

“当你进入那里时，保持你的眼睛和耳朵开放，如果你看到一些可能表明这些非开源模式的东西，”他说。“当 Elasticsearch 更改许可证，社区分叉项目以创建 OpenSearch 时，愿景是你只需点击分叉按钮，你就可以拥有自己的分叉，对吧？但实际上这是一个非常非常繁琐的过程，以至于一些开发人员需要逐行分离专有代码。在 Elastic 的案例中，它被称为[XPack](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/setup-xpack.html)，从开源代码中获得许可。”

## 了解治理
开发人员也可以采取主动措施。例如，开发人员可以选择不受单个供应商控制的代码。

“除了许可证之外，另一面是查看并了解谁在许可证、治理、政策的背后，”他说。

另一个提供一些保护缓冲的选项是使用专门分发特定开源解决方案的供应商。他表示，分发商可以提供免受暴露的赔偿。他们还提供其他好处，例如支持和在特定硬件设置上运行的认证。

他建议，开发人员还可以寻找[由基金会支持的开源解决方案](https://thenewstack.io/value-investing-open-source-foundations/)，而不是单个公司，但他警告说，即使这样也不是万无一失的措施。

“即使基金会也不是防弹的，”他说。“基金会提供一些监督、一些治理和其他一些减少风险的方法。但如果最终，在未来的道路上，它最终又由单个供应商支持，那么即使在基金会下也是一个问题。”

他补充说，基金会还需要学习如何更好地以透明的方式引导和管理项目。

“在 CNCF 内部，我们正在重新审视对预期内容的更严格的理解，或者至少让项目非常清楚地说明预期是什么，”他说。
