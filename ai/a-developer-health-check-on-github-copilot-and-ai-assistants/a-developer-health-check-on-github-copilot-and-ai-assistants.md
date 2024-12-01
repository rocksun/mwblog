
<!--
title: GitHub Copilot 和 AI 助手开发者健康检查
cover: https://cdn.thenewstack.io/media/2024/11/fd9615a1-pexels-divinetechygirl-1181287b.jpg
-->

我们回顾了过去几年 GitHub Copilot 的情况，并探讨它究竟是在帮助还是阻碍开发者。此外，定期使用 Copilot 是否可行？

> 译自 [A Developer Health Check on GitHub Copilot and AI Assistants](https://thenewstack.io/a-developer-health-check-on-github-copilot-and-ai-assistants/)，作者 Alexander T Williams。

根据 Stack Overflow 的数据，AI 驱动的编码助手迅速普及——[高达 76% 的开发者正在使用或打算使用它](https://survey.stackoverflow.co/2024/ai#sentiment-and-usage-ai-select)。而没有哪个[AI 编码工具](https://thenewstack.io/top-5-code-completion-services/)像 GitHub Copilot 那样引起轰动，它[于 2021 年 7 月推出](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/)（远早于[ChatGPT 的出现](https://thenewstack.io/just-out-of-the-box-chatgpt-causing-waves-of-talk-concern/)）。

GitHub Copilot 的核心是一个 AI 驱动的编程搭档，而不是一个被动的助手。它可以辅助代码建议，自动化重复性任务，甚至根据最少的输入生成复杂的函数。

但回顾 Copilot 的发展历程，我们不禁要问几个关键问题：

- Copilot 是炒作多还是实际应用多？
- 对于普通开发者来说，定期使用它是否可行？
- 我们真的准备好迎接这种转变了吗？

为了充分解答这些问题，让我们深入了解 Copilot 如何影响生产力、代码质量、团队协作以及更广泛的伦理环境。

## 对开发者生产力的影响

GitHub Copilot 最常被提及的好处之一是它有可能提高开发者的生产力。理论上，Copilot 旨在[减少在样板代码和重复性任务上花费的时间](https://graphite.dev/guides/github-copilot-productivity)，使开发者能够更多地关注问题的解决和工作的创造性方面。但这在实践中是否属实呢？

根据[埃森哲和 GitHub 自己的一项调查](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-in-the-enterprise-with-accenture/)：

- 67% 的开发者每周至少使用 GitHub Copilot 五次；
- 43% 的人认为该工具“极其”易于使用，另有 35.5% 的人认为它“相当”易于使用；
- 51% 的受访者表示 Copilot“极其”有用，30% 的人表示它“相当”有用；
- 88% 的 Copilot 生成的代码保留在编辑器中，没有被删除。

显而易见，开发者不仅对 Copilot 这个产品感到兴奋，而且对其性能也感到满意。但是，这究竟是为什么呢？

首先，便利性因素不容忽视。当开发者遇到一个琐碎的问题或需要编写一个以前写过无数次的标准函数时，Copilot 会介入并提供一个节省时间和精力的解决方案。这种“[自动完成效应](https://stackoverflow.com/questions/2083467/does-autocomplete-have-an-impact-on-code)”——Copilot 帮助完成未完成的想法——可以作为生产力的催化剂，尤其是在编码的早期阶段。

然而，事情还有另一面。自动完成效应有时会使开发者走向意想不到的道路，特别是如果他们依赖建议而不进行彻底审查的话。事实上，[这种情况已经发生，开发者也注意到了](https://github.com/orgs/community/discussions/7323)。此外，开发者可能会发现自己反复编辑生成的代码，从而减慢工作流程而不是加快工作流程。

因此，生产力提升是取决于具体情况的；Copilot 的帮助在与开发者的警惕性和经验相结合时最有价值。

好的，但是代码本身呢？

## 2024 年机器生成的代码好吗？

除非你一直生活在与世隔绝的地方，否则你可能已经注意到许多初级开发者吹嘘他们如何仅仅使用 AI 就能构建应用程序、游戏或整个公司。最初，没有人理会这些说法，直到 Sundar Pichai [表示 Google 生产的所有代码中有 25% 是 AI 生成的](https://arstechnica.com/ai/2024/10/google-ceo-says-over-25-of-new-google-code-is-generated-by-ai/)。

显然，如果世界上最大的公司之一依赖机器生成的代码，那么它一定很好，对吧？不完全是，尤其是在 Copilot 的背景下。

Copilot 生成的代码的质量引发了相当大的争议。一方面，Copilot 庞大的训练数据集——从数十亿行代码中收集而来——提供了一个广泛的基础，使它能够为各种情况生成功能代码。许多开发者欣赏它能够创建可以改进的初始草稿的能力。
然而，必须承认机器生成代码的局限性。Copilot 的好坏取决于其训练数据，这意味着它也可能无意中复制有缺陷的做法，引入细微的错误，甚至放大已知的漏洞。

与人类开发者不同，Copilot 缺乏对项目特定上下文和细微决策的直观理解。

[Alessandro Benetti 和 Michele Filannino 的一篇研究论文支持这一观点](https://ceur-ws.org/Vol-3762/489.pdf)。该研究表明，15% 的开发者认为 Copilot 在代码优化方面表现不佳，而约 40% 的开发者认为它在调试和理解其他代码方面无效。那么开发的互联性呢？

## Copilot 的协作性
将 Copilot 引入协作编码环境，引发了关于团队合作和责任的有趣问题。传统上，协作项目依赖于团队成员之间的清晰沟通，通过代码审查、每日站会和共享工具来促进。随着 AI 的加入，团队动态不可避免地会发生变化。

一个结果是 Copilot [可以让单个开发者感觉更自给自足](https://docs.kedehub.io/kede-manage/kede-copilot.html)。然而，反过来，这可能会减少对同伴支持的需求，使团队合作减少。

开发者可能会求助于 Copilot 而不是向同事寻求帮助，这可能会限制指导和知识共享的机会。这种转变有可能造成孤立的工作环境，尤其是在开发者远程工作的情况下。另一方面，像 Copilot 这样的 AI 助手也可以通过加快编码过程并解放开发者[专注于项目更复杂、更具创造性的方面](https://www.deloitte.com/uk/en/Industries/technology/blogs/2024/the-future-of-coding-is-here-how-ai-is-reshaping-software-development.html)来支持协作。

这里的警告是，这需要有意识地努力平衡个人 AI 支持的生产力与一直以来对成功软件项目至关重要的协作精神。

## 伦理和知识产权挑战
虽然关于[数据提取](https://apryse.com/capabilities/extraction)和半秘密抓取有很多宣传，但机器生成的代码在很大程度上一直没有受到关注。即使是 AI 生成的文字也引起了更多争议，主要是因为它非常显眼。

然而，Copilot 本身就存在争议——它是在一个多样化的数据集上进行训练的，从公开可用的存储库中提取代码，其中一些可能具有限制性许可证。[已经有一起针对微软和 OpenAI 的诉讼](https://www.theverge.com/2022/11/8/23446821/microsoft-openai-github-copilot-class-action-lawsuit-ai-copyright-violation-training-data)，指控他们未经适当署名就使用开源软件。

这引发了重要的问题：如果 AI 助手生成的代码类似于受保护存储库中的代码片段，[谁拥有该代码的权利](https://www.bloomberglaw.com/external/document/X4H9CFB4000000/copyrights-professional-perspective-ip-issues-with-ai-code-gener)? 开发者是否无意中违反了许可协议？微软是否只是为了囤积数据而收购了 GitHub？

更广泛的软件社区仍在努力解决如何规范和管理这些伦理挑战，开发者必须谨慎行事，以避免潜在的法律和道德陷阱。

## 有限的控制、隐私和能力（目前）
有效使用 Copilot 的一个关键方面是保持开发者控制和自主权。AI 生成的建议很有帮助，但它们也可能造成开发者开始毫无疑问地依赖 AI 的情况——[导致自动化偏差](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/)，开发者认为 AI 总是正确的。这可能是危险的，尤其是在代码质量至关重要的关键项目中。

然后，还有一个由来已久的问题，即[将你的代码交给第三方](https://www.compliancepoint.com/cyber-security/protecting-data-in-the-hands-of-a-3rd-party/)。如果微软遭受数据泄露，所有已轻松交给 Copilot 的数据都将被抢夺。

这[并不意味着 AI 是网络安全的敌人](https://www.businessinsuranceusa.com/news/technology/artificial-intelligence-cybersecurity-friend-foe-business-insurance/)——相反，它可以大大增强网络安全，但将如此多的数据交给一家公司在没有防护措施的情况下是冒险的。在这一点上，现在判断还为时过早，尤其是在当前政府围绕 AI 的立法努力[充其量只是探索性的](https://www.whitehouse.gov/briefing-room/statements-releases/2023/10/30/fact-sheet-president-biden-issues-executive-order-on-safe-secure-and-trustworthy-artificial-intelligence/)。
并非全是坏消息，因为使用开源LLM作为更传统的助手可以轻松解决隐私问题和审查问题。当然，它不像Copilot那样与VSC集成，但是[在Huggingface等平台上有多种选择](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Instruct)。您可以轻松选择所需的规格并在本地运行它，而数据永远不会离开您的网络。

## 结论

GitHub Copilot充分证明了其潜力和局限性。[提高生产力](https://www.infoq.com/news/2024/09/copilot-developer-productivity/)、更高效的工作流程和简化的编码承诺很有吸引力，但这些好处却被对代码质量、开发者依赖性、伦理考虑和协作性质变化的担忧所抵消。

同样，对于初学者和高级开发人员来说，好处并不相同，因为Copilot的可用性在达到一定程度后会递减。

那么，最终结论是什么？

如果您还没有尝试过Copilot，绝对应该尝试一下，但在任何情况下都不要完全依赖它。它在分析现有代码、调试和优化方面的缺陷使其无法完全胜任。
