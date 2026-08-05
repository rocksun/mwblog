大多数开源维护者都熟悉那种感觉：打开 GitHub，面对堆积如山的 Issue，而一个小团队根本无法有效地进行维护。AI 编码工具[让情况变得更糟了](https://thenewstack.io/ai-generated-code-crisis/)：现在只需几秒钟就能生成低质量的错误报告、未经审查的补丁或推测性的漏洞描述，但要搞清楚其中哪些有效，依然像过去一样耗费人力。

然而，一个热门开源项目的背后团队报告称，通过将繁重的琐事交给一组代理（agents），他们即将彻底清空 Issue 积压。

[Astro](https://github.com/withastro/astro) 是一个用于构建快速、内容丰富网站的 JavaScript 框架。在撰写本文时，其 GitHub 上遗留的未解决 Issue 已从年初的 200 多条减少到[约 20 条](https://github.com/withastro/astro/issues)——该团队预计在下个月内将其降至零，这将是该项目五年历史上的第一次。它之所以能做到这一点，是利用了其团队自研的 AI 子代理团队。Cloudflare 在[一月份收购了该团队](https://thenewstack.io/cloudflare-acquires-team-behind-open-source-framework-astro/)，并于周二[宣布](https://blog.cloudflare.com/astro-issue-triage)将这些系统开源，供其他维护者使用。

## Astro 找到了解决方案

该工具名为 [triagebot-action](https://github.com/withastro/triagebot-action)，以 GitHub Action 的形式运行。当有人提出一个 Issue 时，它会启动一个四阶段流程：在沙盒中重现 Bug、诊断根本原因、验证其是否为真实 Bug，并尝试修复。每个阶段由独立的 AI 代理处理，整个过程由编码在 GitHub 标签中的状态机驱动，因此任何人都可以准确看到给定的 Issue 处于哪个阶段以及原因。

> “‘修复’总是最难的，因为标准太高了。”

Astro 联合创始人、现任 Cloudflare 高级工程经理 Fred Schott 表示，“修复”步骤是系统中非核心的部分——即便没有这一步，对 Issue 进行分类并将报告交给人工维护者，用他的话说，“仍然是一个非常棒的成果”。但修复是最难做好的环节。

“‘修复’总是最难的，因为标准太高了，”Schott 告诉《The New Stack》。“其他所有任务只是‘*你能完成你的阶段吗*——*重现 Bug、诊断原因等*’。而在‘修复’环节，它必须编写出质量足够高、可以合并的代码。”

![标记 Bug 修复](https://cdn.thenewstack.io/media/2026/08/549bdcca-image3-1024x819.png)

*标记 Bug 修复*

这种差距正是“分类优先于修复”的原因。Schott 将其追溯到他观察代理在哪些地方表现可靠，在哪些地方表现不佳。

“我认为（这只是）逐渐意识到 Issue 分类是代理非常擅长的事情，同时不会陷入它们在代码质量方面不擅长的陷阱，”他说。“而且对于我们维护者来说，Issue 分类非常耗时，所以意识到自动化处理它，而不需要维护者手动触发，可以为我们节省大量时间。”

> “对于我们维护者来说，Issue 分类也非常耗时。”

## Astro 的主场

简单回顾一下，Astro 于 2021 年作为开源项目启动，Schott 在次年创办了 The Astro Technology Company，获得了包括 Lightspeed Venture Partners 和 Google 旗下 Gradient Ventures 在内的一系列支持者提供的 700 万美元种子资金。

Cloudflare 于 1 月份宣布收购该公司，吸收了这个框架背后的团队。该框架已被 IKEA、Unilever 和 Visa 等公司使用。与 React 等倾向于为整个页面发送较大 JavaScript 包的框架不同，Astro 默认将页面作为纯 HTML 发送，并且只为实际需要的页面部分加载 JavaScript。这种方法最终与 Cloudflare 让网络更快的业务目标相吻合。

当时，《The New Stack》[思考了这笔交易对 Astro 未来的意义](https://thenewstack.io/why-platform-companies-keep-buying-frontend-framework-teams/)，指出了平台公司收购前端框架团队的模式——其中一些，例如[ Netlify 在 2023 年收购 Gatsby](https://thenewstack.io/netlify-acquires-gatsby-its-struggling-jamstack-competitor/)，在创造者离开后，该框架逐渐因缺乏支持而没落。问题在于 Cloudflare 是会继续投资 Astro，还是会任其陷入同样的忽视中。

六个月过去了，Schott 表示几乎没有什么改变。Astro 仍然有四名全职工程师，包括 Schott 本人，所有通过收购加入的人员仍全职从事该项目，尽管志愿者和 Open Collective 资助的贡献者像往常一样来来去去。Schott 说，Astro “仍然作为一个独立的团队运作”，拥有开放的路线图、发布节奏等。值得注意的是，该团队在 1 月份作为 Astro 6 测试版的一部分[发布了一个重新设计的开发服务器](https://thenewstack.io/astro-redesigns-its-development-server/)，但 triagebot-action 也许是它还有空间去构建新事物的最明确信号。

该工具在 Astro 之外的采用仍处于早期阶段。Schott 表示 Cloudflare 的 [workers-sdk](https://github.com/cloudflare/workers-sdk) 团队正在内部对其进行原型设计，但“目前只有 Astro”在生产环境中运行它。其背后的基础代理框架[名为 Flue](https://flueframework.com/)，归属于 Astro 组织而非 Cloudflare，并且这两个项目都旨在运行在任何基础设施上，不依赖于 Cloudflare 特定的工具。

## 为代理而生

退一步看，triagebot-action 是 Cloudflare 本周开源的第二个以 AI 代理为主要用户的工具。在 7 月底，[Cloudflare 发布了 pvcli](https://thenewstack.io/cloudflare-pvcli-privacy-debugger-agents/)，这是一个用于 Apple 和 Microsoft 等产品中隐私协议的命令行调试器。Cloudflare 系统工程师 Fisher Darling 当时表示，pvcli 是“明确为基于代理的调试而设计的”。

Triagebot-action 解决了不同的问题，但其基本思想是相似的：将传统上需要人坐在键盘前完成的工作封装成软件，让 AI 代理能够自主执行。

> “当它奏效时固然很好，但它是否正确且值得接受，或者不如自己动手去写修复方案，这始终由维护者决定。”

展望未来，像 triagebot-action 这类工具的下一个显而易见的进步是“修复”元素本身。Schott 表示，他不知道系统何时能达到其修复方案近乎 100% 可信的程度，但它的构建目标是朝着这个方向逐步演进——它最初在内部推出时根本没有修复能力，后来添加了留在一个分支上供审查者查看的建议修复方案，直到后来才获得了直接根据该建议打开 Pull Request 的能力。他可以想象它走得更远：代理评估自身的置信度或修复规模，并最终自主打开甚至合并 Pull Request。

“我们非常认真地对待这一部分，这就是为什么我们首先专注于 Issue 分类部分，而‘*为我编写代码来修复这个 Issue*’部分是次要的、锦上添花的功能，”Schott 说。“当它奏效时固然很好，但它是否正确且值得接受，或者不如自己动手去写修复方案，这始终由维护者决定。”