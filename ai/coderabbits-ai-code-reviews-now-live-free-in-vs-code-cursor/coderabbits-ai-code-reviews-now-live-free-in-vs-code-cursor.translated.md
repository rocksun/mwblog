# CodeRabbit 的 AI 代码审查现已在 VS Code、Cursor 中免费上线

![Featued image for: CodeRabbit’s AI Code Reviews Now Live Free in VS Code, Cursor](https://cdn.thenewstack.io/media/2025/05/6082e96a-yunus-tug-gt1ar9ig1b8-unsplash-1024x683.jpg)

[CodeRabbit](https://www.coderabbit.ai/) 是一家成立两年的初创公司，使用 AI 进行自动化代码审查，现已通过直接集成到流行的代码编辑器中来扩大其覆盖范围，包括 [Visual Studio Code](https://thenewstack.io/this-week-in-programming-all-hail-visual-studio-code/)、[Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) 和 Windsurf。

此举将该公司的 AI 驱动的[代码审查](https://thenewstack.io/how-to-find-success-with-code-reviews/)功能免费提供给个人开发人员，这与该公司传统的以企业为中心的方法有所转变。

此次集成正值软件开发领域面临着一个新兴问题，即 AI 工具在显著加速代码生成的同时，也带来了新的质量控制挑战，而传统的手动审查流程难以应对这些挑战。

“如果你看看整个 [CI/CD](https://thenewstack.io/ci-cd/) 管道，代码审查是最后一个仍然是手动的过程 —— 并且它对软件交付的速度造成了代价高昂的拖累，” CodeRabbit 的联合创始人兼首席运营官 [Gur Singh](https://www.linkedin.com/in/guritfaq-singh-510175280/) 在一份声明中说。“通过将 CodeRabbit 引入 VS Code 和 Cursor 以及 Windsurf，我们正在开发的早期阶段嵌入 AI，就在工程师工作的地方。”

## 解决 AI 代码质量差距

CodeRabbit 创始人兼首席执行官 [Harjot Gill](https://www.linkedin.com/in/harjotsgill/) 在最近的一次采访中向 The New Stack 解释了 IDE 集成背后的基本原理。该公司拥有 75,000 名日活跃用户，已经发现了开发工作流程中的一个关键差距。

“所有这些 AI 编码和 AI 生成工具的最大瓶颈是它们并不完美，”他说。“已经存在缺陷和问题。我们的想法是，我们是否可以引入 AI 来解决这个问题？”

CodeRabbit 正在适时地采取这一举措。随着像 [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) 和 Cursor 这样的 [AI 编码助手](https://thenewstack.io/what-are-ai-code-assistants-and-how-should-you-use-them/) 得到广泛采用，开发团队正在以前所未有的速度生成代码。然而，这种加速已经产生了 Gill 所描述的“二阶效应”问题 —— 当 AI 生成的代码没有经过仔细审查时，就会出现质量和安全问题。

CodeRabbit 的产品提供了该公司所谓的“上下文 AI 代码审查”，它超越了传统的静态分析工具。与基于规则的系统不同，CodeRabbit 的 AI 能够理解代码更改背后的意图，并提供类似于人类的关于质量、安全和最佳实践的反馈，Gill 说。

Omdia 的分析师 [Michael Azoff](https://www.linkedin.com/in/michaelazoff/?originalSubdomain=uk) 表示，CodeRabbit 是一种流行的代码审查工具，已经迅速发展到拥有大量的客户。他指出，它很好地利用了 AI，包括大型语言模型 (LLM)，来自动化代码审查过程。
“与流行的 IDE 集成非常有意义，意味着该工具可以从开发人员选择的 IDE 中运行，这将有助于增加该工具的使用，” Azoff 告诉 The New Stack。“开发人员将可以选择代码审查工具，CodeRabbit 是一种专用工具，而许多代码优化和审查任务都可以作为基于 AI 的 IDE 代码助手以及独立的 AI 辅助 AppDev 平台中的功能（这两个类别最近都在 [Omdia Universes](https://omdia.tech.informa.com/vendor-selection) 中进行了审查）。因此，CodeRabbit 面临着激烈的竞争，需要表现得更好才能蓬勃发展，因为它的许多目标客户将采用其中的一些 AI 辅助编码工具。开发人员无疑会尝试所有可用的选项，并选择最好的。”

## 报告显示可节省大量时间

根据 CodeRabbit 的内部数据，该平台可显著提高效率。“我们听说与手动代码审查相比，可以节省 60% 到 70% 的时间，” Gill 说。该工具尤其有利于高级开发人员，他们传统上承担着架构分析和识别安全漏洞的重担。

“大部分反馈已经由 AI 提供，然后人类仍然需要介入，因为即使使用非常先进的推理模型，我们仍然不真正了解他们整个产品的全部部落知识，也许还有架构级别的知识，” Gill 解释说。“他们正在进行更高层次的审查和更具智慧的审查，而不是 AI 发现的许多这些容易解决的问题。”
该公司的做法创建了一个双层审查系统：开发人员现在可以在提交代码之前，在他们的 IDE 中私下运行 AI 审查，而中心化团队审查流程继续在 Git 平台级别运行。

## 通过免费增值策略进行市场扩张

免费的 IDE 集成代表了 CodeRabbit 的一项战略性免费增值策略。虽然单个开发人员可以在他们的编辑器中免费访问 AI 审查，但组织仍然需要购买企业许可证才能实现全面的 CI/CD 集成。

Gill 说：“对我们来说，这就像一个垫脚石。这就像一个免费增值模型，我们免费提供给单个开发人员，希望他们以更中心化的方式采用 CodeRabbit。”

这项策略似乎正在奏效。CodeRabbit 报告称，收入和用户每月增长 30-40%，这使其成为 Gill 所谓的“二阶效应”公司，该公司致力于解决第一波 AI 编码工具所产生的问题。

## 竞争格局

尽管面临来自包括 [AWS](https://aws.amazon.com/?utm_content=inline+mention) 、Microsoft 和 GitHub 在内的科技巨头的竞争——所有这些公司都推出了自己的 AI 代码审查功能——CodeRabbit 对其技术差异化保持信心。该公司指出其先进的沙盒技术和基于代理的架构是关键优势。

Gill 说：“CodeRabbit 的技术深度与捆绑的 GitHub 和 Amazon 工具相比，简直就是一个完全不同的水平”，他将 Datadog 与 Amazon CloudWatch 或 Snowflake 与 Amazon Redshift 等成功的专业工具进行了类比。

随着 AI 继续改变软件开发，CodeRabbit 扩展到 IDE 代表了一种押注，即质量控制工具必须像旨在审查代码生成能力一样快速发展。对于希望在利用 AI 的速度优势的同时保持标准的开发团队来说，集成的代码审查可以提高生产力。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)