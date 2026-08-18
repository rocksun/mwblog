<!--
title: 五家欧洲公司预购了尚不存在的 AI 算力：Mistral 的战略转型之路
cover: https://cdn.thenewstack.io/media/2026/05/1add10bc-by-yuniaz-gkl8wko39hm-unsplash-scaled.jpg
summary: Mistral AI 宣布开始托管第三方开源模型（如 GLM-5.2），并提供区域推理及优先级服务。同时，Mistral 获得了五家欧洲大型企业的长期算力承诺，意在通过统一的基础设施服务绑定企业客户，淡化模型差异，提升其平台的核心地位。
-->

Mistral AI 宣布开始托管第三方开源模型（如 GLM-5.2），并提供区域推理及优先级服务。同时，Mistral 获得了五家欧洲大型企业的长期算力承诺，意在通过统一的基础设施服务绑定企业客户，淡化模型差异，提升其平台的核心地位。

> 译自：[Five European companies just agreed to buy AI compute that doesn't exist yet](https://thenewstack.io/mistral-third-party-open-models/)
> 
> 作者：Amanda Caswell

Mistral AI 这家以[发布开放权重模型](https://thenewstack.io/mistral-vibe-cloud-agents/)而闻名的法国人工智能公司，希望企业即使在选择非 Mistral 模型时，也能使用其基础设施。

该公司[周二表示](https://mistral.ai/news/regional-inference-open-models-new-compute/)，将开始托管第三方开源模型，首先从中国的 Z.ai 推出的 GLM-5.2 开始。该模型将在与 Mistral 自家模型相同的基础设施上运行，并可访问其区域处理控制功能和新的优先级服务层。

> 该公司希望为企业提供一个运行不同开源模型的场所，而不必强制它们在每次切换时都从头开始。

Mistral 的区域端点目前已在欧洲和美国广泛可用。其优先级层级（Priority Tier）目前处于公开预览阶段，该层级将符合条件的请求排在标准流量之前，并提供 99.5% 的正常运行时间服务水平协议。

该公司希望为企业提供一个运行不同开源模型的场所，而不必强制它们在每次切换时都从头开始。

## 第三方模型，同样的管道

第一个是来自 Z.ai 的 GLM-5.2 模型，拥有 100 万 token 的上下文窗口。Mistral 将编码和长上下文代理工作列为其主要用途。GLM-5.2 可通过该公司的 API（标识为 zai-glm-5-2）使用，每百万输入 token 费用为 1.40 美元，每百万输出 token 费用为 4.40 美元，每百万缓存输入 token 费用为 0.14 美元。

一个团队可能使用 GLM-5.2 进行编码，使用 Mistral Medium 处理涉及图像和文本的工作，并使用 Small 进行更便宜的日常请求。使用相同的 API 并不意味着这些模型可以互换。每个模型都有其独特之处，因此团队在投入生产之前仍需要进行测试。

虽然 GLM-5.2 拥有[开放权重](https://thenewstack.io/microsoft-nvidia-meta-and-open-weights/)，但通过 Mistral 使用它仍然是一项托管服务。Mistral 决定了哪个版本可用，并负责运行其背后的基础设施。

> 每个模型都有其独特之处，因此团队在投入生产之前仍需要进行测试。

## 区域边界存在缝隙

借助 Mistral 的区域推理服务，开发人员可以通过更改 API 端点来决定他们的请求是在欧洲还是美国进行处理。常规端点则不提供此保证。Mistral 表示，将推理保持在靠近用户的地方可以减少延迟并帮助企业满足数据位置要求，尽管这会使每个输入、输出和缓存 token 的成本增加 10%。

Mistral 表示，某些账户和使用数据可能仍会离开所选区域。根据其信任中心（Trust Center）的安全措施，信息也可能与外部公司共享。

处理金融、健康或政府数据的公司仍有一些工作要做。提示词（prompts）可能保留在欧洲，但团队还需要查明 Mistral 记录了什么、信息存储在哪里、谁可以看到这些信息，以及什么信息会流向外部公司。[Microsoft-Mistral 主权计算合作伙伴关系](https://thenewstack.io/microsoft-mistral-sovereign-ai/)为 Azure 客户解决了一些此类问题，但直接在 Mistral 自身端点上运行工作负载的团队面临着不同的一套保障措施。

区域端点目前尚未支持所有功能，且根据区域的不同，某些模型也会缺失。开发人员可以使用函数调用，但不能使用代理（Agents）、批处理（Batch）或文件 API（Files API）。这表明将现有应用程序迁移到欧盟端点不仅仅是替换基础 URL 那么简单。如果应用程序依赖于不支持的功能，Mistral 的区域处理保证将不再覆盖该工作负载。

## 优先级并不总是得到保证

Mistral 的优先级层级（Priority Tier）在基础设施繁忙时，会将符合条件的 API 调用排在标准层级请求之前。客户必须与 Mistral 商定访问权限，并为每个模型商定自定义限制。设置完成后，开发人员可以在完成请求中添加 `service tier: auto`。如果不包含该字段，请求将通过标准层级进行。

只有在组织拥有有效授权、所选模型在覆盖范围内、请求处于其自定义速率限制内且 Mistral 在该区域有该模型的容量时，请求才会被优先处理。缺少其中任何一个条件，请求都可能降级到标准层级。

Mistral 在响应的 usage 对象中包含了处理该请求的层级。开发人员可以记录该字段，以了解请求被降级的频率，而不是假设每个标记为 auto 的调用都得到了优先处理。如果延迟突然上升，团队需要知道是模型变慢了，还是请求悄悄回退到了标准队列。

## 未经明确的算力承诺

该公司正在召集一批愿意做出多年期算力承诺的欧洲企业和机构。ASML、Amadeus、Capgemini、Caisse des Dépôts 和 CMA CGM 在公告中被点名，但该公司并未透露他们中任何一家承诺购买的容量是多少。Mistral 将由此产生的分配称为欧洲计算单元（European Compute Units，简称 ECUs）。随着需求的改变，客户将能够在 Mistral 计算产品中应用这些单元。

对于客户来说，这是一个提前几年做出的赌注。他们可能知道自己需要 AI 算力，但不知道会使用哪些模型，这些模型会有多大，或者工作负载是推理、微调还是尚未产品化的其他内容。让 ECU 在 Mistral 的产品之间流动，旨在为这种不确定性留出空间。

Mistral 没有说明一个 ECU 能购买多少算力、成本是多少、客户是否可以结转未使用的容量，或者如果基础设施没有按时准备好会发生什么。但很明显，Mistral 需要客户持续使用其基础设施，无论他们选择哪个模型。同样的赌注——[基础设施层比任何单一模型都重要](https://thenewstack.io/karp-mensch-ai-lockin/)——正是[许多企业已经做出的选择](https://thenewstack.io/enterprise-ai-model-routing/)。GLM-5.2 是这可能如何运作的第一个迹象。

> Mistral 需要客户持续使用其基础设施，无论他们选择哪个模型。