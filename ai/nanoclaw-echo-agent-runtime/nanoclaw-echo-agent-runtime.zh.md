**当被问及迅速发展的AI攻击者与旨在遏制它们的软件防御之间的激烈竞争时**，NanoClaw联合创始人兼首席执行官 Gavriel Cohen 给出了这样的回答：

“这里出现了一种明显的氛围变革，” Cohen 告诉 *The New Stack*。他可能说得还比较保守。

上周发生的一件事是这种范式最清晰的迹象之一：OpenAI [披露](https://openai.com/index/hugging-face-model-evaluation-security-incident/) 称 [GPT-5.6 Sol](https://thenewstack.io/openai-gpt-56-live/) 和一个能力更强、在内部评估期间减少了网络拒绝次数的预发布模型，在高度隔离的测试环境中绕过了限制。这些模型串联了 OpenAI 研究系统和 Hugging Face 生产基础设施中的漏洞，最终访问了 Hugging Face 的生产数据库。OpenAI 将其称为“史无前例的网络事件”。

***另请参阅：*** [***Hugging Face 漏洞事件的真相***](https://thenewstack.io/openai-huggingface-sandbox-breach/)

**在此背景下**，Cohen 的 [NanoClaw](https://nanoclaw.dev/)（一个用于 AI 代理的开源框架）和 [Echo](https://www.echo.ai/)（一家安全软件基础设施提供商）周三宣布建立合作伙伴关系，以加固 NanoClaw 代理运行的软件环境。

两家公司表示，加固后的 NanoClaw 运行时（[现已在 GitHub 上提供](https://github.com/nanocoai/nanoclaw)）将保护范围扩展到了代理使用的浏览器、工具和库。其目的是关闭隔离代理本身无法解决的攻击面。

“通过 Echo 加固版的 NanoClaw 代理运行时，NanoClaw 成为第一个为社区提供加固代理环境的开源代理框架，从底层运行的软件开始进行全方位安全保护，”两家公司在联合声明中表示。

此次合作建立在 NanoClaw 最初的安全主张之上。在[此前接受 *The New Stack* 采访时](https://thenewstack.io/nanoclaw-openclaw-agent-security/)，Cohen 将 OpenClaw 大约 50 万行的代码库描述为“致命缺陷”，因此他将 NanoClaw 构建为一个更小、更易于审计的替代方案，并将代理置于[隔离容器](https://thenewstack.io/nanoclaw-containerized-ai-agents/)中，以便它们可以在不获得对主机无限访问权限的情况下运行命令。

但隔离只能处理单一方向的威胁。

当被问及发生了什么变化时，[Cohen](https://il.linkedin.com/in/gavrielco) 指向了新一代具备网络攻击能力的模型。

“像 Mythos 这样的新模型正在增强攻击者的能力，” Cohen 告诉 *The New Stack*。“现在，发起复杂的攻击，将多个漏洞串联成有效的利用手段变得容易多了。忍受已知的未修复漏洞曾经是生活中的常态，但现在不再可接受了。”

> “像 Mythos 这样的新模型正在增强攻击者的能力。”

“沙箱需要双向密封，” Cohen 继续说道。“代理不应该能够逃逸，而且由于代理现在正在执行实际工作，外部攻击者也不应该能够通过代理使用的工具侵入。”

## 一个双向加固的运行时

随着越来越多的人将代理投入使用，安全问题不能完全留给用户去解决。一个流氓代理对客户和社区都是一种风险。但一个通过其浏览器、文件解析器或其他工具入侵代理的攻击者可能同样危险。

Cohen 将现代提示注入比作社会工程学攻击。代理可能会被诱导到一个看起来无害的网页，在那里，一个已知的浏览器缺陷会将访问转变为一次入侵。一个易受攻击的解析器同样可以将打开文件变为代码执行。

NanoClaw 和 Echo 表示，他们共同构建了加固后的运行时。NanoClaw 定义了代理环境、隔离和策略层。Echo 仅使用必要的组件从源代码重新构建了该环境中的软件，然后应用了针对已知漏洞的补丁。

两家公司表示，该过程将已知漏洞的数量从数千个减少到接近零。由此产生的运行时包含了代理常用的组件：Chromium、Node.js、Bun、pnpm、Corepack、Git、curl 和 unzip。

> Echo 表示，每个新披露的漏洞都会在 24 小时内完成分流，严重和高危漏洞的修复会在数小时内根据其企业服务水平协议发布。

Echo 表示，其专门构建的 AI 代理会监控新披露的漏洞，确定受影响的软件，查找或开发修复程序，测试兼容性并为人工审查打开 pull requests。该公司表示，每个新披露的漏洞都会在 24 小时内完成分流，严重和高危漏洞的修复会在数小时内根据其企业服务水平协议发布。

## 没有分叉的 Chromium

Chromium 浏览器似乎是一个显而易见的攻击面。然而，其庞大的常见漏洞和披露（CVE）数量也反映了全球部署最广泛的软件项目之一所受到的审查。

[Eylam Milner](https://il.linkedin.com/in/eylamm)，Echo 的联合创始人兼首席技术官，告诉 *The New Stack*，公司不打算维护自己的 Chromium 分叉。

“与其维护一个分叉，Echo 不如直接从源代码重新构建 Chromium，并通过 Echo 的自动化 CVE 补丁管道进行处理，” Milner 说。“浏览器保持与上游一致，并以完全修补和加固的状态交付。这为 Echo 用户提供了快速的修复，同时又不牺牲兼容性。”

Milner 表示，仅 Chromium 就包含约 3000 万行代码，并遵循着无情的发布节奏。Echo 的目标是在持续修补已知漏洞的同时保留现代浏览器的功能，而不是用兼容性去换取一个定制浏览器。

## 一种选择，而非强制

加固后的运行时不会取代 NanoClaw 的标准版本。NanoClaw 将继续维护和开发该项目，每个版本都将提供标准容器镜像和 Echo 提供的加固版本。

Milner 表示，Echo 在隔离环境中独立地从源代码重新构建加固镜像，对其进行签名，附带可验证的软件物料清单，并在公司的 CVE 服务水平协议下持续进行补丁更新。用户可以选择使用该镜像，而本地构建代理运行时的未认证路径仍然可用。

NanoClaw 将推荐安全的配置，并将良好的默认设置作为开源项目的一部分，但不会强制执行。

> “NanoClaw 采用 MIT 许可证，旨在可被分叉。”

“NanoClaw 采用 MIT 许可证，旨在可被分叉，” Cohen 告诉 *The New Stack*。“任何人都可以根据自己的需求进行调整。”

前沿模型使情况复杂化，因为它们既能识别漏洞，又能利用漏洞。Cohen 表示，NanoClaw 在开发过程中广泛使用了 Fable，但获取 Mythos 进行防御性网络安全工作受到高度限制。

这种失衡有助于解释其紧迫性。NanoClaw 一直将代理定位为安全、负责任的工具，而不是[今年早些时候看到的“英雄式法外之徒”](https://thenewstack.io/openclaw-github-stars-security/)。此次合作将这种逻辑从代理的行为扩展到了其底层的软件。

尽管技术合作紧密，但 Cohen 表示 NanoCo 和 Echo 目前没有合并的计划。

这是一场军备竞赛的早期阶段，还是仅仅是在不安全空间中开展业务的成本？Cohen 并未对此进行过多区分。

“竞赛已经开始，让防御者获得能力以保持领先于攻击者是整个游戏的关键，” Cohen 告诉 *The New Stack*。

围墙正在筑起，我们知道原因。