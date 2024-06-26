<!--
title: 持续交付：软件开发的黄金标准
cover: https://cdn.thenewstack.io/media/2024/03/8607abf8-gold-1024x576.jpg
-->

可发布性的高分意味着保持高质量的同时，能够快速发现和解决问题，并获得及时反馈和快速恢复。

> 译自 [Continuous Delivery: Gold Standard for Software Development](https://thenewstack.io/continuous-delivery-gold-standard-for-software-development/)，作者 Mandi Walls 是 PagerDuty 的 DevOps 倡导者。她是技术会议的常年演讲者，也是"构建 DevOps 文化"这本 O'Reilly Media 白皮书的作者。她对新工具和新实践的兴起很感兴趣。

任何一家企业如果想为客户提供一流的产品和服务，都应该乐于拥抱变革。当然，这可能会比较困难。变革往往会带来不确定性，因为已有的流程和服务都必须转变以满足新的标准。但变革不能是为了变革本身。企业必须将这些新的方法、产品和不同的[工作方式与可衡量的、具体的结果](https://thenewstack.io/deep-work-a-better-way-to-measure-developer-velocity/)联系在一起。

[DevOps Research and Assessment (DORA)](https://thenewstack.io/google-says-you-might-be-doing-dora-metrics-wrong/) 提出了一个非常有效的框架，用于衡量这些变革对性能的影响。DORA 是一个长期的研究项目，"旨在理解推动软件交付和运营性能的能力"。

在这个框架中，一个突出的性能指标是"releasability"。这个衡量指标主要强调软件开发团队始终能够将其产品推向市场，并作为衡量企业[持续交付 (CD) 流水线](https://thenewstack.io/ci-is-not-cd/)效率的具体指标。

实际上，获得高 releasability 分数意味着要保持持续高质量，并具备快速事件检测和解决能力，以及在开发人员工作的平台中内置了快速反馈和恢复功能，以便为客户交付高质量软件。

## DORA 持续交付的核心指标

在 DORA 框架内，有大量可以衡量的指标，以及它们对组织的软件开发绩效的影响。这些指标可以是技术能力和流程，例如人工智能 (AI)、持续集成 (CI) 或代码审查速度，也可以是更直接与绩效相关的指标。

这第二组指标对于衡量 [CD 绩效](https://thenewstack.io/ci-cd/)非常重要。该组中两个关键指标是稳定性和吞吐量。前者展示了组织的变更失败率和从这些故障中恢复所需的时间，而后者衡量了任何变更的前置时间和变更频率。这两个指标共同描绘了组织的软件开发成功状况，以及在变更失败时所需的恢复时间。鉴于组织都将 CD 作为标准，了解它们的绩效(尤其是在变更失败时)至关重要。 

## 了解产品出现故障原因的挑战

在 CD 的背景下，开发人员必须能够轻松快速地了解产品或更新失败的原因。考虑到软件更新有 [50% 到 80%](https://acqnotes.com/acqnote/careerfields/common-software-failure-causes#:~:text=Most%20software%20projects%20fail%20completely,between%2050%25%20%E2%80%93%2080%25.)会失败，开发人员需要能够快速确定确切的失败点并加以解决。减少事件解决时间(或修复漏洞的时间)是开发人员持续努力实现"releasability"指标的一个重大好处。这意味着，当出现问题时，它们都很容易修复，恢复周期也很快。

为了满足越来越快的开发目标，开发人员需要找到减少事件响应和故障排查时间的方法。为此，他们需要获得实时洞见，以便能够在事件发生时识别、诊断和解决任何问题。这些洞见可以让开发人员即时、清晰地了解变更对其[软件开发流水线](https://thenewstack.io/software-supply-chain-secure-3/)的影响，即使变更本身不足以导致事件。

这些"变更事件"为产品在整个开发周期中所做的每个变更提供了蛛丝马迹，让开发人员看到每个更新的直接影响。这些影响范围从应用程序代码的部署，一直到扩大或缩小服务对其性能的影响。也许最有用的是，它们不仅在产品的开发周期中可用，在产品上市后也可用。这样一来，任何事件或性能下降都可以在发生时立即得到解决。

## 变更关联: 持续、高质量交付的关键

虽然变更事件提供的信息对开发人员很有用，但变更关联则将事件解决进一步提升了一步。它为致力于将产品恢复到可发布状态的开发人员提供了与事件最相关的最新变更事件。这些事件的数据随后可以被输入机器学习模型并加以分析，从而在过去的变更事件与事件之间建立关联，实现快速诊断和解决事件。要将这种事件解决策略再进一步，所有这些数据都可以集中在一个单一平台上，该平台不仅跟踪变更事件，还帮助将单个变更与产品中的故障关联起来。

由于每个变更事件都包含了与其时间和应用的服务相关的上下文信息，因此可以检测到变更对产品的确切影响。这是非常有价值的数据，当它一目了然地可用时，就可以让事件响应团队快速对事件进行分类，缩短解决时间，从而确保组织提供的服务稳定可靠。

## 理解变更的好处

变更事件提供的洞见让开发人员能够精确定位影响其产品的变更及其影响方式。这直接导致了大量不计划内工作的减少。通过智能变更关联，识别导致产品故障的确切变更这一耗时过程可以自动化，进一步减轻了关键时刻开发人员的工作负担。这让开发人员可以专注于创新，为客户创造价值，而不只是简单地修复产品故障。
