# 云原生开发中 AI 的安全悖论

![云原生开发中 AI 的安全悖论的特色图片](https://cdn.thenewstack.io/media/2025/05/dc4631f3-oleksandr-chumak-zguburggmdy-unsplash-1024x612.jpg)

[Oleksandr Chumak](https://unsplash.com/@olalandro?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 在 [Unsplash](https://unsplash.com/photos/black-framed-eyeglasses-on-computer-screen-zGuBURGGmdY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)发布。

随着 AI 和其他类似技术（如生成式 AI (GenAI)）不断渗透到企业的各个环境中，业务领导者们不断努力寻找、构建和部署新的用例，从营销人员的数据收集助手到销售团队的分析师代理。

对于负责保护广泛且通常分散的云生态系统的安全团队来说，监控可能成百上千个 AI 项目（所有项目都处于不同的复杂性和成熟度阶段）感觉就像用水管喝水一样——一场巨大的混乱，而且速度极快。

近期对近 [3,000 名](https://www.paloaltonetworks.com/resources/research/state-of-cloud-native-security-2024) 云安全和 DevOps 专业人士的调查发现，超过一半 (54%) 的人认为云环境的复杂性和碎片化是主要的数据安全问题，71% 的组织因仓促部署而面临漏洞。毫不奇怪，三分之一的受访者表示，他们难以[跟上快速的技术变革和不断演变的](https://thenewstack.io/ai-is-evolving-rapidly-heres-how-developers-can-keep-pace/)威胁。

**云开发中的 AI：注意差距**

毫无疑问，AI（尤其是 GenAI）一直是[软件工程师和开发人员](https://thenewstack.io/three-software-development-challenges-slowing-ai-progress/)的数字 B12 助推剂，提高了生产力，加速了代码生成和云原生创新的整体步伐。Google 和 Alphabet 的 CEO Sundar Pichai 在 10 月份的第三季度财报电话会议上透露，[他们超过四分之一的新代码是由 AI 生成的](https://blog.google/inside-google/message-ceo/alphabet-earnings-q3-2024/#search)，但仍在其工程师的密切关注下。

正如 Sundar 所说，虽然快速采用 AI 进行编码辅助和其他用途 *“帮助我们的工程师做得更多、更快”*，但它也引入了动态的[安全问题和云](https://thenewstack.io/what-we-can-learn-from-the-top-cloud-security-breaches/)漏洞，无论使用是否经过批准。这可能包括不安全的代码（增加威胁暴露）到逃避传统检测工具的 AI 自动化云入侵。一份[最新报告](https://www.paloaltonetworks.com/resources/research/state-of-cloud-native-security-2024)发现，尽管 38% 的受访者认为 AI 驱动的攻击是主要的云安全风险，但所有受访者 (100%) 已经在使用 AI 辅助开发。

当涉及到 AI 在云开发中的影响时，风险因素可以分为三个同样令人担忧的支柱：

**不知道你不知道的：** 如此多的 AI 项目（从实验到生产）在云环境中运行，对于[安全团队来说，要保持](https://thenewstack.io/open-source-needs-maintainers-but-how-can-they-get-paid/)对整个情况的全面了解，更不用说其潜在影响，是一项艰巨的任务。这种可见性的缺乏导致了治理的不足，即使存在全面的策略，并且可能因未经批准的使用而导致代价高昂的监管和法律影响，从而进一步加剧这种情况。
**更多模型，更多问题：** AI 生成的代码和更广泛的 AI 基础设施将新元素引入云环境，所有这些都可能引入新的风险，例如提示注入或中毒的[数据，这些数据会改变模型](https://thenewstack.io/pulumi-templates-for-genai-stacks-pinecone-langchain-first/)的行为。鉴于模型交互非常非结构化，攻击和规避的变化可能只是与工作过度和人手不足的安全团队之间的一场消耗战。
**不要忘记你的数据：** 就像花生酱和果冻一样，没有数据就根本无法拥有 AI，而且这些数据（通常用于通过[检索增强生成](https://thenewstack.io/advanced-retrieval-augmented-generation-rag-techniques/)(RAG) 等过程来微调模型）必须受到保护。[已经证明](https://www.scworld.com/brief/hugging-face-compromised-with-malicious-ai-models)，如果不良行为者访问模型，他们可以访问其原始的专有或敏感的组织和客户数据。因此，经验法则是：任何使用敏感[数据训练的模型都应被视为包含](https://thenewstack.io/container-security-a-troubling-tale-but-hope-on-the-horizon/)该敏感数据。

**云开发中的 AI：风险并不意味着退缩**
虽然 AI 在云环境中的风险是无可辩驳的，但其带来的回报也是如此。关于云安全，可以将 AI 视为一个数字双面间谍——它既有突破边界的潜力，也有加强边界的能力。这就是为什么组织创新和[投资必须与你的安全态势同步](https://thenewstack.io/want-to-mitigate-risk-invest-in-automation/)——如果你的右腿想跑，你的左腿就不能只想走路。

对于安全团队来说，有三个简单的最佳实践，可以帮助确保 AI 安全[采用和集成到云原生](https://thenewstack.io/5-things-to-know-before-adopting-cloud-native/)工作流程中：

**维护 AI 清单：** 你必须完全了解你的 AI 基础设施——模型、代理、应用程序、工作区——以及它如何映射到数据。这可以通过定期与开发人员同步以了解和编目他们正在使用的资产，或者通过特定的工具和解决方案自动完成。
**执行风险评估：** 你知道他们对假设的看法……投入工作并绘制与每个 AI 管道、项目、生态系统和基础设施相关的可想到的风险——潜在的影响是什么？有哪些威胁？它是否涉及敏感数据？它仅供内部使用还是面向客户？它用于什么？哪些业务流程依赖于它？
**投资于威胁防护：** 利用端到端平台和高级产品，如 AI 代理，可以实时保护模型交互。检测、响应和缓解发生的威胁中断，并帮助理解组织上下文（谁需要知道，谁需要批准行动，谁拥有所有权，这将影响谁）以快速分类问题并降低风险。

**云开发中的 AI：负责任的前进方式**

几十年来，安全团队一直被贴上“否决部门”的标签——这是一个不幸的绰号，源于夸大的事实。Gartner[预测](https://www.gartner.com/en/webinar/566448/1276680#:~:text=By%202028%2C%20cloud%20computing%20will,execution%20will%20impact%20business%20effectiveness.)，到 2028 年，AI 的采用将最终占据超过 50% 的云计算资源，这使得组织更加需要平衡 AI 驱动的效率和云环境中的强大安全性。

这将需要工程师和开发人员做出同样的承诺，拥抱开放性，并更加关注他们基于云的工作流程，以及安全团队摆脱这种阻挠者的标签，并使他们的组织和同事能够迅速而安全地行动。通过保持对威胁环境的 360 度全方位观察，了解 AI 基础设施中的每一件硬件和软件，并投资于先进的威胁防护，安全团队可以避免混乱，只需专注于旅程。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)