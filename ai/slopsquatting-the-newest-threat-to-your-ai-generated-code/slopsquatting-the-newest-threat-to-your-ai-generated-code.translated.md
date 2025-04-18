# Slopsquatting：AI 生成代码面临的最新威胁

![Featued image for: Slopsquatting: The Newest Threat to Your AI-Generated Code](https://cdn.thenewstack.io/media/2025/04/5ff2de77-toa-heftiba-ghlljhftdgw-unsplash-1-1024x683.jpg)

软件开发人员越来越多地使用 AI 来创建代码，考虑到他们面临着构建产品并更快地将其推向市场的日益增长的需求，这一趋势并不令人意外。

[GitHub](https://github.com/)去年的一项研究发现，[97% 的受访程序员](https://github.blog/news-insights/research/survey-ai-wave-grows/)表示他们正在使用 AI 编码工具。 [Stack Overflow](https://stackoverflow.com/questions)在 2024 年进行的一项类似调查发现，在 65,437 名开发人员中，有 76% 的人表示他们[正在使用或计划使用此类工具](https://survey.stackoverflow.co/2024/)。 原因清单不断增加，从提高生产力和增强代码质量到更快地[调试](https://thenewstack.io/master-the-art-of-python-debugging-with-these-tips/)以及提高团队之间的一致性。

然而，由于 AI 的双刃剑性质，[存在风险](https://www.legitsecurity.com/aspm-knowledge-base/ai-code-generation-benefits-and-risks)，包括代码可靠性、安全漏洞和[技术债务](https://thenewstack.io/technical-debt-continues-to-mount-heres-how-to-solve-it/)，这些风险可能会减慢流程并增加成本，[Legit Security](https://www.legitsecurity.com/)（一家[应用程序安全态势管理](https://thenewstack.io/consolidate-with-application-posture-security-management/) (ASPM) 公司）表示。

另一个风险是[大型语言模型](https://thenewstack.io/top-5-large-language-models-and-how-to-use-them-effectively/) (LLM)，正如自[OpenAI](https://openai.com/) 首次发布 [ChatGPT](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/) 在 2022 年以来，它们一直被认为会产生“[幻觉](https://thenewstack.io/ai-agentic-evaluation-tools-help-devs-fight-hallucinations/)”，即错误或误导性的输出。 对于世界上大多数人来说，这意味着对提示的回复可能会错误地陈述财务数字，在文章中包含不正确的信息，或者——在一个著名的案例中——[编造律师在法庭文件中使用的法庭引文](https://www.theguardian.com/technology/2023/jun/23/two-us-lawyers-fined-submitting-fake-court-citations-chatgpt)。

对于开发人员来说，这可能意味着生成对实际不存在的软件库、模块或其他代码包的引用。 这不是一种新现象。 [安全公司](https://vulcan.io/blog/ai-hallucinations-package-risk/)和分析师已经了解它一段时间了。

## 提防 Slopsquatting

也就是说，由于人们关注供应链攻击，它再次被提出，这种攻击可以通过利用代码存储库中的这些幻觉来发起，它有一个生动的名称——“[slopsquatting](https://fosstodon.org/@sethmlarson/114328275927451797)”——以及三所大学的研究人员最近的一项[研究](https://arxiv.org/pdf/2406.10279)，其中概述了如何做到这一点。

这个名字是对众所周知的网络威胁“域名抢注”的戏仿，在这种威胁中，不良行为者注册与合法网站名称非常相似的恶意域名，希望开发人员会拼写错误并无意中最终访问虚假网站。

在 slopsquatting 的情况下，威胁行为者可能会创建一个恶意软件包，该软件包使用 LLM 创建的不存在的库的名称，并将其放置在流行的代码存储库（如 GitHub、[Python Package Index](https://pypi.org/) (PyPI) 或 [npm](https://www.npmjs.com/)）上供下载，希望程序员会为了他们的工作而获取它。

[IDC](https://www.idc.com/) 分析师去年[撰写了有关此类威胁的文章](https://blogs.idc.com/2024/04/22/package-hallucination-the-latest-greatest-software-supply-chain-security-threat/)，指出“软件包幻觉为威胁行为者创造了新的机会，可以在软件供应链中植入恶意代码，并利用使用生成式 AI 编写代码的开发人员。”

## 处于“新生阶段”的研究

来自德克萨斯大学圣安东尼奥分校、俄克拉荷马大学和弗吉尼亚理工大学的研究人员进行了更深入的研究，他们认为，大多数关于 AI 幻觉的研究都集中在自然语言生成和预测工作（如摘要和机器翻译）中的幻觉。 他们写道，对[代码生成](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/)中的幻觉的研究“仍处于新生阶段”。
对于他们在 [Python](https://thenewstack.io/python/) 和 [JavaScript](https://thenewstack.io/javascript/) 代码中包幻觉方面的工作，研究人员测试了 16 种流行的代码生成模型，如 ChatGPT-4、[DeepSeek](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/)、[CodeLlama](https://ollama.com/library/codellama)、[Claude](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/)、[Mistral](https://mistral.ai/) 和 [OpenChat](https://oc.app/)，并使用了两个提示数据集来了解问题的范围。这些 LLM 生成了 576,000 个 Python 和 JavaScript 代码示例，其中 19.7% 的推荐包不存在。

那么，这些模型会在同一个包中重复出现幻觉吗？他们使用 500 个创建了包幻觉的提示的集合，为每个提示重复查询 10 次，发现 43% 的包幻觉在所有 10 个查询中都重复出现，并且 58% 的情况下，一个包在 10 次迭代中重复出现不止一次。

研究人员写道，测试结果表明“大多数幻觉不仅仅是随机错误，而是一种可在多次迭代中持续存在的可重复现象”。“这一点意义重大，因为对于希望利用此漏洞的恶意行为者来说，持久性幻觉更有价值，并使幻觉攻击向量成为更可行的威胁。”

该研究的另一个有趣的发现是，大多数模型能够检测到自身 75% 以上的幻觉，研究人员写道，这表明“这些模型对其自身生成模式具有内在的理解，可以利用这些模式进行自我改进，这是开发缓解策略的重要发现。”

## 开发者面临的 AI 挑战

这项研究以及对抢注风险的宣传，都在重要地提醒开发者在使用 AI 生成代码时需要谨慎。[Sonatype](https://www.sonatype.com/) 是 [软件成分分析](https://thenewstack.io/software-composition-analysis-and-sboms-a-united-defense/) (SCA) 市场中越来越多的供应商之一，预计该市场将从去年的 3.2884 亿美元增长到 2033 年的近 [17 亿美元](https://straitsresearch.com/report/software-composition-analysis-market)。SCA 工具可自动执行识别和管理开源组件的过程。

Sonatype 首席产品开发官 Mitchell Johnson 告诉 The New Stack，在软件开发中使用 AI 可以追溯到开源刚出现时——“有点像非法技术”——开发者被警告不要使用。现在，大多数软件都包含开源元素。
Johnson 说：“AI 有点像 20 年或 25 年前的开源，各个组织只是在试水。”“但实际上，开发者总是领先一步，因为我们作为开发者被要求提高生产力、加快速度、更快地交付、交付更高质量的产品。更快、更好、更便宜推动着我们。不幸的是，不良行为者也明白这一点，而且他们非常聪明。”

问题在于，AI 减轻了程序员的压力，他们被告知要快速行动，而安全往往被放在一边。在询问工程副总裁和开发经理今年的目标时，“你很少听到‘安全’这个词”，他说。“你听到的是，‘按时交付这个东西，按预算交付这个东西，交付这个创新，减少这笔开支’，但你就是听不到安全。这并不是说开发者不考虑它。我们看到的情况越来越多，但总的来说，不是。创新和速度发生得太快了。”

Bugcrowd 的创始人 Casey Ellis 告诉 The New Stack，开发者的动机“是‘让东西工作’，而不是‘确保东西不做所有它可能不应该做的事情’。当这种错位存在时，此类问题就会存在，并且 [当] 你添加像 AI 生成代码这样的加速功能时，像抢注这样的攻击就是自然的副产品。”

## 验证的必要性

即使有了 AI 的帮助，开发者仍有责任验证他们的代码，以确保其中没有任何恶意内容。Johnson 将其比作工程师的希波克拉底誓言：不要对代码造成伤害。

“你必须对每一行被签入的代码负责——对它的质量、安全性、功能和性能负责，”他说。“你不能说，‘好吧，AI 告诉我的。’作为工程师，使用这些大型语言模型和工具比以往任何时候都更容易编写代码，但我们有责任确保我们没有签入不安全或无法正常工作的代码。这正是抢注试图利用的东西。”
几位安全专家表示，开发人员不能盲目信任 AI 生成的内容。

[J Stephen Kowski](https://www.linkedin.com/in/jstephenkowski/)，[SlashNext Email Security+](https://slashnext.com/) 的现场 CTO，告诉 The New Stack：“大多数开发人员都知道 AI 可能会犯错，但许多人仍然过于信任输出，并且并不总是检查隐藏的问题。” “人们很容易沉迷于速度和便利性，但这可能导致错过安全漏洞或使用虚假软件包。最好的保护措施是使用自动化工具来检查依赖项和代码是否存在问题，并且始终在使用 AI 建议的内容之前进行审查。”

随着开发人员扩大 AI 的使用范围，使用此类保护措施将非常重要。Sonatype 的 Johnson 表示，他预计生成式 AI 将很快开始区分那些可以控制和管理该技术的组织和程序员，以及那些不能的组织和程序员。

他说：“那些真正优秀的、能够挑战机器、了解输出内容、判断其正确与否的开发人员，正在看到生产力的几何级增长。” “你会看到某些已经拥有良好安全和工程实践的企业，他们协同工作，变得更好。而那些松懈的企业将会更加落后，并面临重大问题和违规行为。这将从组织和个人层面区分和加剧富人和穷人之间的差距。”

[技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。（订阅我们的YouTube频道）](https://youtube.com/thenewstack?sub_confirmation=1)