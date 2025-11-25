Anthropic 今日发布了其旗舰 Opus 模型的最新版本：Opus 4.5。

该公司称其为迄今为止最智能的模型，并指出它在解决编码任务方面尤其强大，从 OpenAI 的 [GPT-5.1-Codex-Max](https://thenewstack.io/openai-says-its-new-codex-max-model-is-better-faster-and-cheaper/) 和 Google 一周前发布的 [Gemini 3](https://thenewstack.io/google-launches-gemini-3-pro/) 模型手中夺得桂冠，SWE-Bench 验证准确率达到 80.9%。

该公司还大幅降低了 Opus 4.5 的使用成本，API 定价从每百万输入/输出 token 的 15 美元/75 美元降至每百万输入 token 5 美元、每百万输出 token 25 美元。

Anthropic 订阅计划的用户现在也将获得更多使用 Opus 4.5 的空间。

## 基准测试

随着 OpenAI 的 GPT-5.1 和 5.1-Codex-Max、Google 的 [Gemini 3](https://thenewstack.io/google-launches-gemini-3-pro/)（及其热门的 Nano Banana Pro 图像模型）的发布，对于大型模型构建者来说，这是一个非常活跃的十一月。尤其是 Gemini 3，获得了非常积极的评价。

与 Google 不同，Anthropic 从未专注于图像处理或视频创作，而是始终坚持其在编码和生产力用例方面的优势。最新的 Opus 也不例外，Anthropic 强调该模型现在可以“以一致性、专业性和领域意识”生成文档、电子表格和演示文稿。

但一如既往，Claude 模型在编码方面表现出色。这反映在基准测试中，Opus 4.5 在所有方面都优于竞争对手，但当然，基准测试并不总是反映真实世界的用例。

![](https://cdn.thenewstack.io/media/2025/11/b1f343c5-claude-opus-4-5-swe-bench.png)

来源：Anthropic。

对于此次发布，Anthropic 还对 Opus 4.5 进行了与公司未来招聘的性能工程师候选人相同的测试。这项测试仅侧重于技术能力，时长两小时，Opus 4.5 的得分高于 Anthropic 任何招聘候选人的历史得分。

正如 Anthropic 开发者关系负责人 Alex Albert 告诉我的那样，他感觉“模型就是能理解”。他指出，过去的模型通常非常擅长从不同渠道（如 Slack 和电子邮件）收集数据，但在有效整合所有这些信息方面却遇到困难。

“我发现，使用这个模型，情况不再如此，”他告诉我，“我真的可以相信它能直接从那些 Slack 消息生成良好的输出，然后我就想，哇，它真的可以直接发送这个。我仍然在审查它和其他内容，但我真的可以放手不管了。”

## 低、中、高工作量

Opus 4.5 的一个新功能是它具有一个“工作量”（effort）参数（低、中、高），类似于其一些竞争对手的模型，这使得开发者可以控制模型用于解决给定问题的时间（以及 token 数量）。设置为中等时，该模型在 SWE-bench 验证基准上与 Sonnet 4.5 持平，但使用的 token 数量减少了 76%；即使在高级设置下，它超越了 Sonnet 4.5，也只使用了 Sonnet 模型大约一半的 token。

这是我们一直看到的趋势，OpenAI 上周推出其最新的 [Codex-Max](https://thenewstack.io/openai-says-its-new-codex-max-model-is-better-faster-and-cheaper/) 模型时也强调了这种效率。

总的来说，该模型还在其他方面（包括视觉推理和数学）改进了 Opus 系列（和 Opus 4.1）的其余模型。

![](https://cdn.thenewstack.io/media/2025/11/2ea75080-claude-opus-4-5-evals.png)

来源：Anthropic。

## 用于计算机使用的 Opus 4.5

该公司表示，Opus 4.5 也是 Anthropic 迄今为止最适合计算机用例的模型。为了进行测试，Anthropic 现在向所有 Claude Max 订阅者（每月支付 100 美元以上）开放其 Chrome 扩展。

计算机和浏览器使用感觉仍处于起步阶段，并且通常相当缓慢且容易出错，但 Anthropic 在这方面将技术水平提升了一个台阶，其得分远高于其以前的模型。

Anthropic 最近一直处于一个有趣的境地：其中档 Sonnet 模型的最新版本常常超越旧的 Opus 4.1 模型，这使得用户在日常工作中很少有理由使用更昂贵的模型。然而，其理念始终是拥有一个三层模型，而 Opus 4.5 在此恢复了平衡。

“对我而言，这次发布有趣的地方在于，它不一定意味着：‘哦，每个人现在都需要转向 Opus，’但它确实开启了新的可能性，”Albert 说，“现在我们进入了一个新的局面，我们实际拥有三个模型，它们都沿着这条曲线满足不同的需求：我们有一个月前发布的 Haiku 模型。有一个半月前发布的 Sonnet 4.5。现在这个完成了整个产品系列。”

## Claude 开发者平台更新

除了新模型之外，Anthropic 还宣布了 Claude 开发者平台的两项更新，这些更新与 Opus 4.5 的发布同步进行：Claude Code 的升级计划模式以及桌面应用中的 Claude Code 支持。

Anthropic 表示，新的计划模式现在可以为如何解决问题或添加新功能创建更精确的计划，并更直接地遵循这些计划。

如果您使用 Claude [桌面应用](https://www.claude.com/download)，您现在可以在桌面或云环境中在 Claude Code 中开始编码任务。这现在允许您并行运行多个本地和远程 Claude Code 会话。