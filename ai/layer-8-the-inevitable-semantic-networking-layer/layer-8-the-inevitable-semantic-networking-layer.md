
<!--
title: Layer 8：面向人工智能时代的语义网络层
cover: https://cdn.thenewstack.io/media/2024/06/ffe55292-layer.jpg
-->

Layer 8 和现有的应用程序交付基础设施将为更智能、更具上下文感知能力的网络铺平道路，这些网络可以适应人工智能驱动的应用程序。

> 译自 [Layer 8: A Semantic Networking Layer for the Age of AI](https://thenewstack.io/layer-8-the-inevitable-semantic-networking-layer/)，作者 Liam Crilly。

在经典伪纪录片《摇滚万岁》中最著名的台词中，主吉他手奈杰尔·塔夫内尔指着一个放大器，并指出了刻度盘上的额外数字，说它“可以调到 11”。

虽然“这个可以调到 8 ”这句话没有那么朗朗上口，但现在可能是用这句话来描述传统网络协议栈中新的一层——语义层的时候了。第 8 层的加入是由[人工智能应用](https://thenewstack.io/ai/)及其新需求驱动的。

[OSI（开放系统互连）模型](https://thenewstack.io/open-source-ai-osi-wrestles-with-a-definition/)是一个概念框架，几十年来一直指导着网络设计和通信，它在人工智能时代面临着新的挑战。随着人工智能不断渗透到包括网络在内的各种技术领域，传统的 OSI 模型七层可能不足以满足人工智能驱动的网络的全部需求和[现实](https://thenewstack.io/what-is-an-ai-gateway-and-do-you-need-one-yet/)。

第 8 层是我提出的 OSI 模型扩展，旨在解决人工智能在网络环境中的独特需求和能力。与现有的专注于数据传输技术方面的层不同，第 8 层关注的是对传输数据的语义理解和智能处理。

## 什么是第 8 层，为什么我们现在需要它？

如今的网络不仅仅是数据的管道，而是越来越智能的实体，能够根据其处理的数据内容和上下文做出决策。OSI 模型包含七层：物理层、数据链路层、网络层、传输层、会话层、表示层和应用层。每一层都有特定的功能和协议，使网络设备之间能够通信。

七层 OSI 模型主要关注数据传输的语法方面，例如编码、格式化和错误校正。在云原生世界中，第 4 层（传输层）和第 7 层（应用层）已成为最广泛关注的层。

由于 HTTP 和其他 Web 协议成为向用户和服务提供功能的主要关注点，这些层越来越混淆。即使是应用层也专注于性能，而忽略了内容。总的来说，OSI 层本身并不考虑传输数据的语义含义或上下文。

然而，我们已经看到人工智能应用中语义缓存的出现，其中应用交付和网络技术结合了对内容和用户对应用程序的期望的理解，以改善用户体验并加速应用程序性能。

这些新功能已经将 OSI 模型扩展到其当前范围之外，并将融合成一个更清晰的定义的第 8 层。第 8 层将位于应用层（第 7 层）之上，专注于理解数据中的含义、意图和上下文信息。通过结合语义分析，第 8 层将能够实现更智能、更具上下文感知的网络和应用程序交付决策。

## 第 8 层将如何工作？

就像应用传输技术和协议（HTTP）部署在第 7 层一样，人工智能技术（如机器学习、深度学习和自然语言处理 (NLP)）将在第 8 层使用，以分析和理解传输的数据。NLP 技术可用于处理和解释消息正文，提取关键信息，识别相关实体，并确定整体含义和上下文。

分类模型可能会将 HTTP 请求路由到最适合其中的人类语言的 API 端点。情感分析算法可以应用于评估数据背后的情感基调和意图。这可以帮助根据数据的紧急程度、重要性或复杂性来优先处理或路由数据。

在第 8 层，机器学习模型在这些技术的支持下，可以训练识别数据中的模式、异常和变化。这些模型可以从历史数据中学习，并适应不断变化的网络状况或用户行为。

基于人工智能的检查将在实时运行，在数据流经网络时进行处理。这需要高效的算法和硬件加速，以最大程度地减少延迟并确保及时做出决策。例如，它可以根据内容的重要性或紧急程度优先处理流量，根据其预期用途路由数据，或根据用户的意图调整网络行为。攻击性或有害内容可以在转发之前被过滤、标记或隔离到更复杂的內容审核系统。例如，可以根据通话内容以及与系统记录的类似攻击的比较来识别深度语音攻击。

## 新 ADC 的灵魂

第 8 层的逻辑归宿是在新兴的 AI 网关中，这些网关可以实时应用模型。也就是说，此类 [网关需要与现有的 API 网关](https://thenewstack.io/api-gateway-ingress-controller-or-service-mesh-when-to-use-what-and-why/)、应用交付控制器 (ADC) 和内容交付网络 (CDN) 共存并交互。这种合作必须无缝且超快，以提高第 7 层的性能、弹性和安全性。接近性将使双方受益；语义检查和理解会产生延迟，并且需要对 AI 模型进行密集且持续的推理流量。

通过将第 8 层功能直接集成到 API 网关、ADC 和 CDN 中，可以在更靠近边缘的位置执行语义处理，从而减少往返延迟并实现实时决策。第 8 层与现有应用交付基础设施之间的这种共生关系将为更智能、更具上下文感知能力和响应能力的网络铺平道路，这些网络可以适应人工智能驱动应用程序不断变化的需求——换句话说，就是将网络提升到 11 级。
