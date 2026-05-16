<!--
title: AWS发现60%的软件需求存在Bug：解决之道并非更多AI，而是50年前的逻辑引擎
cover: https://cdn.thenewstack.io/media/2026/05/bcfbe12f-gustopo-sw7be_guk3i-unsplash.jpg
summary: AWS调查发现60%的软件需求存在矛盾或模糊。为此，AWS在其Kiro平台引入需求分析功能，结合大模型与拥有50年历史的自动推理技术，从源头确保代码逻辑的正确性。
-->

AWS调查发现60%的软件需求存在矛盾或模糊。为此，AWS在其Kiro平台引入需求分析功能，结合大模型与拥有50年历史的自动推理技术，从源头确保代码逻辑的正确性。

> 译自：[AWS found bugs in 60% of software requirements. Its fix isn't more AI — it's a 50-year-old logic engine.](https://thenewstack.io/kiro-requirements-analysis-automated-reasoning/)
> 
> 作者：Darryl K. Taft

软件中最昂贵的Bug并不在代码中。它们存在于指导代码构建的需求中。

这就是 AWS 试图通过其 [Kiro](https://thenewstack.io/aws-kiro-brings-automated-reasoning-to-agentic-development/) [代理开发平台](https://thenewstack.io/antigravity-is-googles-new-agentic-development-platform/)中的新功能来消除的问题。最主要的新功能是[需求分析](https://kiro.dev/blog/deep-spec-analysis/)，专门解决需求 Bug。这些是规范中的矛盾、模糊和缺失，在任何人发现它们之前就已经固化到了设计和代码中。当它们在生产环境中浮出水面时，追溯到被误读的需求可能意味着数周的调试工作。

AWS AI 产品管理总监 [Mike Miller](https://www.linkedin.com/in/camikemiller/) 告诉 *The New Stack*：“需求中的 Bug 可能是指相互矛盾的需求——暗示了两种不同的事情，或者是模糊不清或存在缺失——即一个需求对一个开发人员意味着一件事，但对另一个开发人员来说可能意味着略有不同的东西。”

“因此，在实施、代码测试以及随后的生产过程中，也许某些东西没有达到预期效果，你就开始回溯，”领导需求分析计划的 Miller 说道。

Miller 解释说，该功能分为三个阶段。首先，大语言模型（LLM）将模糊的自然语言需求重写为精确、可测试的标准。其次，该输出被转化为形式化的数学逻辑——AWS 称之为“形式化表示”。第三，一个 [SMT（可满足性模理论）求解器](https://en.wikipedia.org/wiki/Satisfiability_modulo_theories)（一种自动推理引擎）针对该逻辑进行证明，以识别矛盾、歧义、未定义的行为和缺失。发现的问题会以平实的语言向开发人员展示，Miller 表示，每个问题都是包含两个选项的选择题，大约只需 10 到 15 秒即可解决。

AWS 反复提到的术语是“证明”。该公司表示，这不只是 LLM 标记一个可能的问题，而是一个形式化推理引擎在论证没有任何可能的实现能够同时满足两条冲突的规则。

“自动推理使我们能够获取这些需求，对其进行检查，识别缺失和模糊之处，并在前期解决它们，”Miller 说，“LLM 侧负责它最擅长的事情，而自动推理负责它最擅长的事情。”

Moor Insights & Strategy 的分析师 [Jason Andersen](https://www.linkedin.com/in/jasontandersen/) 告诉 *The New Stack*：“AWS 一直是利用多样化算法模型评估 LLM 模型正确性以提高准确性这一理念的先驱。”

“这始于在 IAM 等访问控制产品中使用自动推理，”Andersen 继续说道，“这种成功已经开始扩展到 AWS 的其他产品线。这并不是判断 LLM 输出的唯一方法。更典型的方法是使用额外的 LLM 来检查输出并判断它们是否合理。”

## 神经符号定位

Miller 表示，[神经符号 AI](https://thenewstack.io/allegrograph-8-0-incorporates-neuro-symbolic-ai-a-pathway-to-agi/) 术语指的是神经网络（LLM 背后统计性、模式匹配的机器）与符号逻辑（在形式验证和模型检测中已使用了数十年的基于规则、数学严谨的 AI 分支）的结合。

> “没有正确性的速度只意味着你编写错误软件的速度更快。”

他用[勾股定理](https://en.wikipedia.org/wiki/Pythagorean_theorem)作为类比来解释方法的不同。一个在数千个直角三角形上训练过的 LLM 可能会推断出边与斜边之间的关系。但它是推断出来的。它可能是错误的。相比之下，Miller 说，自动推理系统使用数学符号来证明这种关系在每一个可能的直角三角形中都成立——不是作为一种概率，而是一种确定性。

基于这种符号逻辑的形式验证技术自 20 世纪 70 年代起就已应用于硬件设计和安全关键软件中，比 LLM 的出现早了约 50 年。

“这不仅仅关乎速度，”他指出，“没有正确性的速度只意味着你编写错误软件的速度更快。”

Miller 说，Kiro 从一开始就是围绕着[规范驱动开发](https://thenewstack.io/vibe-coding-spec-driven/)构建的，将生成的每一行代码都追溯到记录在案的需求。需求分析旨在使这种追溯不仅是有记录的，而且在逻辑上是严密的。

Miller 表示，在涵盖 1400 多个验收标准的 35 个 Kiro 项目的内部测试中，大约 60% 的初稿需求在能够可靠实施之前需要进行完善。但他表示这是预料之中的，因为初稿只是一个起点。

## 为什么是现在

AWS 多年来一直在悄悄进行自动推理工作。Miller 表示，这项技术已经出现在 [Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) 中，类似的数学逻辑管道可以编码聊天机器人的行为策略，并据此对回复进行数学验证。它还出现在 [Bedrock AgentCore 策略](https://aws.amazon.com/about-aws/whats-new/2026/03/policy-amazon-bedrock-agentcore-generally-available/)中，该策略使用相同的推理引擎来确定代理在什么情况下可以使用哪些工具。

Miller 声称，需求分析代表了这种能力首次被直接嵌入到开发工作流中，即在编写规范的时刻。

> “我们目前在开发工具链中还没有看到太多应用评估的情况，更不用说采用更先进的算法技术了。”

“我对 Kiro 的发现是，他们在突破功能界限和率先进入市场方面非常成功。在这种情况下，”Andersen 说道，“我同意他们在这种水平的需求审查方面处于领先地位。我们目前在开发工具链中还没有看到太多应用评估的情况，更不用说采用更先进的算法技术了。”

AWS 发现，医疗保健、金融和其他对正确性要求极高的行业一直被其自动推理能力所吸引，正是因为他们需要一种在敏感环境下不会产生幻觉的 AI。AWS 表示，同样的模式也正出现在代理编码工具中。

除了需求分析外，Kiro 的其他新功能还包括：并行任务执行（Parallel Task Execution），可并发运行独立的编码任务，将大型规范的实施时间缩短约 75%；以及快速计划（Quick Plan），在前期询问澄清问题后，一次性生成完整的需求集、设计规范和任务细分。

Kiro 在市场上与几种流行的 AI 编码工具竞争，包括 Cursor、Codex、[Claude Code](https://thenewstack.io/claude-code-can-now-do-your-job-overnight/)、[GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) 和 Windsurf 等。

然而，AWS 表示 Kiro 在行业中被广泛使用。

Kiro 更广泛的客户群已经跨越了那些“做对”和“做完”同样重要的行业。[Socure](https://www.socure.com/) 是一家数字身份验证和欺诈预防公司，它利用 Kiro 的规范驱动开发在两天内完成了从 [Scala](https://thenewstack.io/scala-creator-proposes-lean-scala-for-simpler-code/) 到 [Go](https://thenewstack.io/go/) 的迁移。该项目最初预计耗时三周。

银行技术提供商 [Nymbus](https://www.nymbus.com/) 使用 Kiro 生成了 80% 的 [Terraform](https://thenewstack.io/terraform-competitor-formae-expands-to-more-clouds/) 代码、单元测试和 [Playwright](https://thenewstack.io/a-practical-guide-to-data-driven-tests-with-playwright/) 对象模型，将一个项目的测试时间从 32 周缩短到 7 周。达美航空（Delta Air Lines）提前两个季度实现了其试点项目目标。尼尔森（Nielsen）的测试覆盖率增加了 25%，文档编写时间减少了 40%。Hughes Network Systems 表示，Kiro 规范消除了在整个开发工作流程中反复重新建立上下文的需求。

Kiro 的采用名单还包括西门子（Siemens）、Rackspace Technology、亿滋国际（Mondelez International）、Appian 和爱立信（Ericsson），以及亚马逊自己的内部团队——包括 Alexa+、Prime Video、Amazon Stores 和 Fire TV。

## 领导力信号

除了 Kiro 功能发布外，AWS 还宣布 [Shawn Bice](https://www.linkedin.com/in/shawn-bice-9205423/) 已加入公司，担任代理 AI（Agentic AI）部门 AI 服务副总裁，向 AWS 代理 AI 副总裁 [Swami Sivasubramanian](https://www.linkedin.com/in/swaminathansivasubramanian/) 汇报。Bice 将领导 AWS 的自动推理小组。

在一份发给员工的内部备忘录中，Sivasubramanian 写道：“我们正处于代理 AI 的转折点，我再怎么强调 AI 和自动推理需要结合起来以构建可靠且值得信赖的代理都不为过。”

“对我来说，这是否是一种更好或更精确的方法并不是问题，”Andersen 说道，“我的问题是：这对人类参与环节（human-in-the-loop）有什么影响？如果 AWS 更擅长定位问题，那是件好事，但最终还是要由开发人员来决定在这一点上该做什么。在未来某个我们自动化更多工具链的时间点，任何此类改进都可能非常有价值。”

AWS 押注于 AI 辅助开发的下一个竞争轴心不是生成代码的速度有多快，而是你对生成的内容有多大的信任度。需求分析是这一押注的关键。