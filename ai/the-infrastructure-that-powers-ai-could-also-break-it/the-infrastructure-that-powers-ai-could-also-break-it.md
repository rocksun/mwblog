
<!--
title: 赋能AI的基建，也可能成为AI的阿喀琉斯之踵
cover: https://cdn.thenewstack.io/media/2025/10/e125b709-aisecurity.jpg
summary: AI安全需关注基础设施层而非仅模型。容器、GPU等底层存在漏洞，共享平台风险高。强化措施：安全默认、分层防御、明确责任。
-->

AI安全需关注基础设施层而非仅模型。容器、GPU等底层存在漏洞，共享平台风险高。强化措施：安全默认、分层防御、明确责任。

> 译自：[The Infrastructure That Powers AI Could Also Break It](https://thenewstack.io/the-infrastructure-that-powers-ai-could-also-break-it/)
> 
> 作者：Nir Ohfeld

在保护AI安全方面，大多数讨论都集中在模型层：[提示注入](https://thenewstack.io/6-key-security-risks-in-llms-a-platform-engineers-guide/)、训练数据泄露和不安全输出。但有一个更直接、却常常被忽视的风险：支撑这些模型的基础设施。

AI工作负载依赖于与现代云原生应用程序相同的基础。这意味着[容器](https://thenewstack.io/introduction-to-containers/)、[Kubernetes](https://thenewstack.io/kubernetes/)、共享GPU节点和编排层，这些从未在设计时考虑过AI特有的风险。由于这些组件被大规模重用，堆栈中的任何漏洞都可能在多个平台和用户之间连锁反应。

作为致力于攻破AI基础设施以提高其安全性的研究人员，我们亲眼目睹了这些风险在现实环境中已经显现。

## **GPU 是一个新的攻击面**

为了高效运行大型模型，组织依赖 NVIDIA Container Toolkit，这是运行支持GPU的容器的默认方式。它广泛应用于所有云提供商、AI平台以及任何使用NVIDIA GPU的组织。

因此，当我们发现 NVIDIA Container Toolkit 中存在两个独立的严重容器逃逸漏洞时，我们揭示了任何使用共享GPU基础设施的人都面临着重大风险。NVIDIAScape (CVE-2025-23266) 和 CVE-2024-0132 都不是边缘场景。

在同一年内发现两个不同的容器逃逸漏洞，都允许获得宿主机root权限，这表明了一个重要信息：这是一个新的攻击向量。它证明组织必须设计其系统以具备弹性，假设攻击者将突破第一道防线。容器逃逸不再是“是否”发生的问题，而是“何时”发生的问题。结论很明确：[保护AI不应止于模型](https://thenewstack.io/evil-models-and-exploits-when-ai-becomes-the-attacker/)。它始于其所构建的基础设施。

## **共享AI平台带来共享风险**

大多数组织不运行自己的AI基础设施。相反，他们转向像 Hugging Face 或 Replicate 这样的AI即服务提供商。两者都是旨在简化部署和扩展的平台。

在使用[Hugging Face](https://www.wiz.io/blog/wiz-and-hugging-face-address-risks-to-ai-infrastructure)时，我们发现一个问题：恶意模型可以突破其容器并访问相邻的工作负载。在使用[Replicate](https://www.wiz.io/blog/wiz-research-discovers-critical-vulnerability-in-replicate)时，我们识别出一个漏洞，允许我们拦截其他用户的提示和响应。幸运的是，两家公司都与我们迅速合作，解决了这些问题。

但模式很清晰：客户工作负载之间隔离薄弱、权限过于宽泛以及缺乏适当的网络分段仍然太普遍。随着AI快速发展，有时会跳过基本要素。

但我们之前已经吸取过这个教训：默认安全的架构至关重要，尤其是在这种规模下。

## **3种方法强化你的AI基础设施**

好消息是，我们不需要从头开始。云安全社区已经建立了强大的基础，从最小权限到网络分段，这些都直接适用于AI。以下是开始的方法：

1.  **从安全默认设置开始：** 容器隔离、范围受限的权限和网络分段应该是不可协商的。这些并非“锦上添花”，而是必不可少的基础构建块。
2.  **假设会出问题：** 没有哪一个控制是万无一失的。你可以假设第一道防线会被绕过。构建分层防御，限制爆炸半径并在故障升级前捕获它们。
3.  **了解你的共同责任：** 无论你是运行自己的模型还是使用平台，都要清楚提供商的责任止于何处，你的责任始于何处。保护你控制下的数据和管道。

AI正在改变我们构建和部署软件的方式，但它也在重塑我们的威胁模型。如果我们以应用于云的相同纪律来保护支撑AI的基础设施，我们就能在快速创新的同时，始终领先于风险。

*KubeCon + CloudNativeCon North America 2025 将于11月10日至13日在佐治亚州亚特兰大举行。*[立即注册](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/register/)*。*