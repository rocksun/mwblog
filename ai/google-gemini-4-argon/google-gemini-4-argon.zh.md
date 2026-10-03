**谷歌于周三宣布推出 Gemini 4 Argon**，这是该公司备受期待的旗舰模型，看起来它绝对不负众望。

在大多数基准测试中，Gemini 4 Argon 击败了 OpenAI 和 Anthropic 的顶级模型，有时甚至优势巨大，尽管在它落后的项目上，差距也可能达到 10 分左右。

谷歌指出，他们正在采取分阶段的方法，“在逐步扩大访问权限的同时，积极参与美国政府关于预发布模型访问的自愿流程。”

> Gemini 4 Argon 以巨大优势击败了 OpenAI 和 Anthropic 的顶级模型。

这一宣布是在谷歌 CEO Sundar Pichai 与美国总统唐纳德·特朗普会面后，[共同签署了一项](https://www.cnn.com/2026/09/29/business/amodei-huang-karp-trump)“自我约束”承诺的仅仅一天之后发布的。Anthropic、Meta、Nvidia、OpenAI 和 SpaceX 也签署了这项“承诺”，不过该承诺似乎并未附带任何强制执行机制。

| 类别 | 基准测试 | Gemini 4 Argon | GPT-6 Astra | Claude Fable 5.1 | Claude Opus 5.5 |
| --- | --- | --- | --- | --- | --- |
| 知识工作 | Vals Index | **68.9%** | 63.1% | 65.8% | 67.0% |
| 知识工作 | AutomationBench (Score) | **51.3%** | 41.4% | 31.4% | 42.5% |
| 知识工作 | Vals Finance Agent v2 | **65.4%** | 53.5% | 58.9% | 58.6% |
| 知识工作 | Harvey’s Legal Agent Benchmark | **19.6%** | 5.4% | 6.7% | 3.8% |
| 智能体编程 | DeepSWE v1.1 | **77.9%** | 74.1% | 67.4% | 74.2% |
| 智能体编程 | FrontierSWE v2 | 55.0% | **65.5%** | 56.3% | 62.3% |
| 智能体编程 | 氛围编程 Code Bench | **91.9%** | 89.6% | 90.3% | 90.3% |
| 智能体编程 | Terminal-bench 4.0 | 57.4% | 58.2% | 57.9% | **66.4%** |
| ML 工程 | PostTrainBench | 45.3% | 44.3% | 40.2% | **49.3%** |
| 科学与数学 | Terminal-Bench Science 0.1 | 57.6% | **68.1%** | 52.6% | 63.3% |
| 科学与数学 | RiemannBench | **76.0%** | 72.0% | 65.6% | 69.6% |
| 长文本 | GraphWalks (Up to 128k, BFS (F1)) | **99.7%** | 98.7% | 91.4% | 90.6% |
| 长文本 | GraphWalks (256k to 1M, BFS (F1)) | **84.2%** | 71.8% | 65.0% | 66.8% |
| 计算机使用 | Agent’s Last Exam (Pass rate) | **39.5%** | 34.2% | — | 38.2% |
| 计算机使用 | OSWorld-2.0 (Offline subset, Partial reward) | 69.2% | **72.6%** | — | — |
| 多模态理解 | Chartography | **71.6%** | 71.0% | 46.2% | 66.3% |
| 多模态理解 | LVBench | **91.7%** | 87.5% | 79.7% | 83.7% |
| 网络安全 | CWE-bench v1 | **68.0%** | **68.0%** | 58.0% | 67.0% |

谷歌表示，在向 Fairwind 计划之外提供该模型之前，他们将收集早期测试人员的反馈并对 Argon 的安全护栏进行迭代。一旦这一天到来，付费 API 客户和 AI Ultra 订阅者将首先试用新模型，之后才会向开发者、企业和消费者发布。

与它那乏味、无臭且惰性的同名元素不同，Gemini 4 Argon 很可能会引起不小的轰动。谷歌最初在 5 月份的 I/O 开发者大会上宣布了推出新 Pro 模型[Gemini 3.5 Pro](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/)的计划——而 Argon 基本上就是它的替代品。最初的计划是在 6 月份推出新模型，但我们最终迎来的却是一系列 Flash 模型。

## 编程：一般。知识工作：A+

在谷歌包含各种任务的基准测试中，在与 Anthropic 的 Opus 5.5 和 Fable 5.1 以及 OpenAI 的 GPT-6 Astra 的 18 项测试对比中，Argon 在 13 项测试中名列榜首（独占或并列）。

然而，尽管谷歌特别提到了 Argon 的编程能力，但结果却喜忧参半。

谷歌强调 Argon 在 DeepSWE v1.1 上获得了 77.9% 的分数，创下了最新领先水平，但在 FrontierSWE v2 和 Terminal-Bench 4.0 这两个竞争项目中，Argon 的表现却垫底，GPT-6 Astra 和 Opus 5.5 分别领先其 10.5 分和 9 分。它在编程方面的另一个胜局是在氛围编程 Code Bench 上，得分为 91.9%，不过所有四个模型在此项上的得分都超过了 89%。

但 Argon 真正擅长的是知识工作。

Argon 在 Zapier 的 AutomationBench 上得分为 51.3%，比 Opus 5.5 高出近 9 分；在输入长度介于 256K 到 1M Token 之间的 GraphWalks 测试中得分为 84.2%，比 GPT-6 Astra 高出 12 分以上。

> 它在 Harvey 的法律智能体基准测试中得分为 19.6%，几乎是 Fable 5.1 得分的三倍，尽管这意味着它仍然只能完整完成大约五分之一的任务。

在其他领域，Argon 的优势较小。虽然它在 Vals Index、氛围编程 Code Bench、Agent’s Last Exam、Chartography 以及较短的 GraphWalks 测试中领先，但这些领先优势通常在 2 分以内。

在文中列出且包含竞争对手得分的网络安全基准测试 CWE-bench v1 上，Argon 与 GPT-6 Astra 以及 xAI 的 Grok 4.7 以 68% 的成绩并列，Opus 5.5 落后 1 分，但值得注意的是，OpenAI 和 Anthropic 的模型在其各自的[智能体框架](https://blog.collinear.ai/p/cwe-bench-v1)（Codex 和 Claude Code）中运行，因此该排行榜衡量的是模型与其工具的综合表现。

同往常一样，基准测试并不能说明全部问题，但看起来谷歌专注于让这个模型对标准办公任务格外有用。

鉴于其令人印象深刻的 DeepSWE 得分，开发者肯定也会想要测试这个模型。

## 100万输出 Token

在大多数竞争对手目前尚未开拓的前沿领域中，一个有趣的新特性是该模型输出 Token 的限制。对于前沿模型而言，100 万输入 Token 现在已是标准配置，但 Gemini 4 Argon 还可以生成高达 100 万的输出 Token，高于此前 Gemini 模型的 64,000 个。

谷歌在公告中写道：“当模型拥有足够的空间去深度思考并在单个轨迹中生成数十万个 Token 时，它将为解决一次性攻克难题带来全新深度的推理能力。”

至于网络安全，谷歌表示，他们训练 Argon 能够自主发现、验证和修补软件漏洞，并且对于 Fairwind 参与者和公司内部团队，他们在发布该模型时并未添加网络安全护栏。

谷歌在 3 月份以[320 亿美元收购](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/wiz-acquisition/)的 Wiz 已经在其“Scan for Good”计划中使用了 Argon，谷歌称该模型发现了一个全球医院都在使用的医疗软件中的关键漏洞，而此前的前沿模型并未发现该漏洞。

Argon 在谷歌内部的漏洞发现基准测试中得分为 85.8%，在 Wiz 的渗透测试基准测试中得分为 70.9%，不过谷歌仅将这些结果与其自身的 Gemini 3.8 Flash Cyber（分别为 71.0% 和 58.2%）进行了比较。

## 定价？

谷歌[表示](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)，在推广期内，Argon 的定价为每百万输入 Token 2 美元，每百万输出 Token 10 美元；之后价格将分别上涨至 4 美元和 20 美元。后者的输出费率与 Anthropic 对 Opus 5.5 收取的[每百万输出 Token 20 美元](https://www.anthropic.com/claude/opus)相当，并且随着 Argon 的推出……