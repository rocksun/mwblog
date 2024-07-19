
<!--
title: 人工智能赋能的编码未来近在眼前
cover: https://media.wired.com/photos/669846f926dff233a54ff10c/191:100/w_1280,c_limit/AI-Coding-Agents-Fast-Forward-Business.jpg
-->

科技公司，包括 OpenAI，正在开发新一代 AI 助手，它们不仅可以编写代码，还可以调试、组织和评论代码。

> 译自 [The AI-Powered Future of Coding Is Near](https://www.wired.com/ai-powered-coding/)，作者 Condé Nast; Will Knight。


我虽然不是一个熟练的程序员，但多亏了一个名为 [SWE-agent 的免费程序](https://github.com/princeton-nlp/SWE-agent)，我最近成功地调试并修复了一个棘手的问题，该问题涉及软件托管网站 GitHub 上不同代码库中一个文件命名错误。

我将 SWE-agent 指向 GitHub 上的一个问题，并观察它如何遍历代码并推断可能出现的问题。它正确地确定了错误的根本原因是代码中指向文件错误位置的一行，然后它在项目中导航，找到该文件，并修改了代码，使所有内容都能正常运行。对于像我这样的经验不足的开发者来说，这可能需要花费数小时才能调试。

许多程序员已经使用 [人工智能](https://www.wired.com/tag/artificial-intelligence/) 来更快地编写软件。GitHub Copilot 是 [第一个利用人工智能的集成开发环境](https://www.wired.com/story/openai-copilot-autocomplete-for-code/)，但现在许多 IDE 在开发者开始输入时会自动完成代码块。您还可以向人工智能询问有关代码的问题，或者让它提供有关如何改进您正在进行的工作的建议。

去年夏天，普林斯顿大学的两名博士生 John Yang 和 Carlos Jimenez 开始讨论人工智能成为现实世界软件工程师需要什么。这促使他们和普林斯顿大学的其他研究人员提出了 [SWE-bench](https://www.swebench.com/)，这是一个用于测试人工智能工具在各种编码任务中的性能的基准测试集。在 10 月份发布该基准测试后，该团队开发了自己的工具——SWE-agent——来掌握这些任务。

SWE-agent（“SWE” 是“软件工程”的缩写）是众多功能更强大的 AI 编码程序之一，这些程序不仅仅编写代码行，而是充当所谓的软件代理，利用必要的工具来整理、调试和组织软件。初创公司 Devin 在 3 月份发布了 [一个演示视频](https://www.youtube.com/watch?v=fjHtjT7GO1c)，展示了其中一个工具。

普林斯顿大学团队成员 Ofir Press 表示，SWE-bench 可以帮助 OpenAI 测试软件代理的性能和可靠性。“这只是我的个人观点，但我认为他们很快就会发布一个软件代理，”Press 说。

OpenAI 拒绝置评，但一位了解该公司活动的人士（要求匿名）告诉 WIRED，“OpenAI 肯定正在开发编码代理。”

正如 GitHub Copilot 所示，[大型语言模型可以编写代码并提高程序员的生产力](https://www.wired.com/story/openai-copilot-autocomplete-for-code/)，像 SWE-agent 这样的工具可能会证明人工智能代理可以可靠地工作，从构建和维护代码开始。

许多公司正在测试用于软件开发的代理。在 SWE-bench 排行榜的榜首，该榜单衡量了不同编码代理在各种任务中的得分，是来自 [Factory AI](https://www.factory.ai/) 的一家初创公司，其次是 [AutoCodeRover](https://autocoderover.dev/)，这是新加坡国立大学团队的一个开源项目。

大型企业也纷纷加入。一个名为 [Amazon Q](https://aws.amazon.com/q/) 的软件编写工具是 SWE-bench 上的另一个顶级表现者。“软件开发不仅仅是打字，”亚马逊网络服务软件开发副总裁 Deepak Singh 说。

他补充说，AWS 已经使用该代理将整个软件堆栈从一种编程语言转换为另一种编程语言。“这就像有一个非常聪明的工程师坐在你旁边，和你一起编写和构建应用程序，”Singh 说。“我认为这很有变革意义。”

OpenAI 的一个团队最近帮助普林斯顿大学团队改进了一个基准测试，用于衡量像 SWE-agent 这样的工具的可靠性和有效性，这表明该公司可能也在磨练用于编写代码或在计算机上执行其他任务的代理。

Singh 说，许多客户已经使用 Q 构建复杂的后台应用程序。我自己使用 SWE-bench 进行的实验表明，任何编写代码的人很快就会想要使用代理来增强他们的编程能力，否则就会被淘汰。