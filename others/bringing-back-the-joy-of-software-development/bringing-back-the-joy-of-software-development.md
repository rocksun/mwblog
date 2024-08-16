
<!--
title: 重拾软件开发的乐趣
cover: https://cdn.thenewstack.io/media/2024/08/90353c94-priscilla-du-preez-xkkcui44im0-unsplash.jpg
-->

凭借其基于人工智能的 Knovva 平台和数字同事，Provoke 旨在承担“令人厌烦的任务”并减少冲突。

> 译自 [Bringing Back the Joy of Software Development](https://thenewstack.io/bringing-back-the-joy-of-software-development/)，作者 Jeffrey Burt。

在成为 CEO、投资者或高管之前，[Andy Lin](https://www.linkedin.com/in/andylin888/) 是一位软件工程师，他的手指深入到 1 和 0 中，每天工作 12 到 14 个小时，有时甚至连续 48 个小时编码，专注于他真正感兴趣的项目。

Lin 清楚地记得开发人员和项目经理之间持续不断的冲突，这些冲突源于对时间表和优先级的分歧，以及交付质量和速度之间的不断拉锯。

“当这种不匹配和缺乏理解发生时，我们开始将彼此视为最糟糕的人类，”Lin 现在是 [Provoke Solutions](https://provokesolutions.com/) 的 CEO，他对 The New Stack 说。“经理们会说，‘开发人员只是不够努力。为什么他们不努力工作，给我更多的小部件？’工程师看着经理们说，‘他们就是不理解我们。他们不在乎质量。他们只是一群算账的人。”

这种脱节归结于他所说的“我们所做的所有技术债务——我们作为开发人员所做的那些令人心烦意乱的任务。这并不是经理能够理解的。这也不是工作计划中的一部分。”

为了解决这个问题，Provoke 最近推出了 Knovva（发音为“nova”），这是一个基于生成式 AI 的平台和数字同事套件，可以用来完成这些例行公事、令人心烦意乱的任务，从而解放开发人员，让他们能够更快地创建经理们想要的函数和功能，为会议室带来更大的平静。

Lin 说，开发人员将高达 40% 到 90% 的时间花在这些低价值、重复性的工作上，比如运行测试自动化脚本或使用 [静态代码分析](https://thenewstack.io/how-static-analysis-can-save-your-software/) 工具测试代码质量，然后该工具会输出缺陷和改进，开发人员需要完成这些任务。这给已经不堪重负的工作周增加了几个小时。

“我记得开车去客户那里，知道这个星期将是‘代码质量清理周’，”他说。“我当时正处于典型的洛杉矶交通中，我比想到那里然后花接下来的三天时间试图解决代码质量问题更享受交通。”

## 生成式 AI 带来了帮助

为了解决技术债务问题，人们采取了一些措施，比如 [敏捷开发](https://thenewstack.io/heres-what-a-software-architect-does-in-an-agile-team/) 或使用产品思维，将代码视为产品，不将任何东西降级。但 Lin 说，这些都是权宜之计。没有解决问题。

然后出现了 [生成式 AI](https://thenewstack.io/generative-ai-tools-for-infrastructure-as-code/)。

“有了生成式 AI 和我们的数字同事，你就可以真正解决这个问题，”他说。“现在，作为一名开发人员，我不必再担心这些令人心烦意乱的任务，因为我们已经构建了数字同事来完成这些任务。投资回报率非常惊人。就像 10 倍。以前需要 300 个小时才能完成的任务，现在我们的数字同事只需要 30 个小时。”

Provoke 的 Knovva 平台拥有正在申请专利的数字同事，可以自动化软件开发生命周期中的许多任务，包括代码开发和质量、[测试自动化](https://thenewstack.io/test-automation-tools-unite/) 和 [DevOps](https://thenewstack.io/devops/)。其中一个旨在完成质量工程师的工作，确保产品和服务符合质量标准。

另一个专注于应用程序现代化，因为组织正在运行诸如将应用程序从 [Angular](https://thenewstack.io/google-angular-lead-sees-convergence-in-javascript-frameworks/) 迁移到 [React](https://thenewstack.io/meta-releases-open-source-react-compiler/) 或从 React v9 迁移到 React v18 之类的计划。数字同事将进行迁移，收集缺陷列表，并尝试修复它们。

另一个是 Align，它会获取 UI 规范，将其与构建的 UI 进行比较，并识别所有差异。Align 会将差异列表提供给开发人员，开发人员可以将其移至 [Jira](https://thenewstack.io/anti-agile-project-tracker-linear-the-latest-to-take-on-jira/) 或 Azure DevOps 并解决它们。在 Align 的第二次迭代中，数字同事不仅将差异放入队列中，然后留给开发人员处理，而是“进行所有这些调整，”Lin 说。“他们不仅识别问题，还会解决问题。”

## 仍处于早期阶段
该公司拥有约 75 个客户和 150 名员工，分布在达拉斯和新西兰的办事处，已经开发 Knovva 超过 8 个月。Provoke 的工程师在平台上构建了基础设施服务，并拥有其他正在申请专利的技术来维护内容窗口快照之间的状态，这些窗口最初很小，但现在变得越来越大。

“企业代码库有 600 万行代码，”他说。“这很容易遇到。无论你的上下文窗口有多大，你都需要我们开发的这种分块策略，并且能够跨所有上下文窗口的不同代码块维护状态。”

在所有这些过程中，人类仍然在循环中发挥着重要作用。平台中内置了人类反馈强化学习，并通过 [检索增强生成 (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/) 捕获。每个企业在修复缺陷时都会生成代码，Provoke 希望人类审查它是否符合编码标准。

“就像你审查每个开发人员一样，你会让技术主管审查开发人员的代码，然后你说，‘是的，这看起来不错。这个不太好。这个需要调整一下，”林说。“所有这些都会反馈到 Knovva 系统中，并在下次运行时成为 RAG。这段代码将更接近该企业或组织的标准。”

## 在云端运行
这是一项基于云的服务。Provoke 在其环境中构建了一个平台用于演示，然后将其放入容器中并交付给客户，客户可以将其放入他们想要的任何基于云的 [大型语言模型](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/) (LLM) 中，无论是 [亚马逊网络服务](https://aws.amazon.com/?utm_content=inline+mention) (AWS)、[微软](https://news.microsoft.com/?utm_content=inline+mention) Azure 还是其他。它也是自包含的，因此客户放入其中的任何数据都不会成为用于训练竞争对手 LLM 的公共数据。

该公司已进入 Knovva 开发的下一阶段，工程师正在开发一种方法，用于创建可以配置为满足组织特定需求的自定义代理，林说。

“我们不知道世界上所有业务问题，”他说。“我们专注于工程和用户体验问题，但存在这些 [特定] 类型的問題，我们仍然可以使用平台并使用我们构建自己的数字代码所使用的相同服务来构建我们称之为‘自定义数字同事’的东西。”

## 越来越多的流水线

Provoke 正在与一些企业合作，包括一家将整个产品开发运营外包给供应商的生物信息学公司。他们需要在招聘自己的团队的同时开始工作。通常，他们需要雇用两名质量工程师。有了 Knovva，他们只需要一半的质量工程师，Provoke 的技术可以达到 85% 到 90% 的代码覆盖率。

另一家公司正在使用 Knovva 及其同事来解决它从一个版本的 React 迁移到另一个版本的冲突。林还表示，该公司正在“冲刺”为 Align 获得第一个客户。“流水线很强劲，”他说。

林希望 Knovva 及其数字同事改变软件工程师的工作。

“使用 Knovva 的副作用是你可以节省资金，但我认为真正的原因，真正背后的动力——我们真正的北极星——是将快乐带回工作环境，”他说。“我们每天在工作中与人共度 8 到 10 到 12 个小时——虚拟的、物理的，无论如何。这段时间不应该更积极吗？不应该更快乐吗？不应该这样，这样当我们回家与家人团聚时，我们才能成为更快乐的人？”
