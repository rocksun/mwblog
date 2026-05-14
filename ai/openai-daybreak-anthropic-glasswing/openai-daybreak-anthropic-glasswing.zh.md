本周，OpenAI [推出了](https://openai.com/daybreak/) Daybreak，这是其围绕 [GPT-5.5](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/) 构建的网络安全倡议，采用了分层访问框架，并以 [Codex Security](https://thenewstack.io/openai-anthropic-open-source/) 作为智能体驱动。Daybreak 页面紧随 OpenAI 先前的公告发布，该公告描述了 [网络安全受信任访问](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/) 将如何为经过验证的防御者扩展 GPT-5.5 和 GPT-5.5-Cyber。

本周的消息发布于 Anthropic 推出 [Project Glasswing](https://www.anthropic.com/project/glasswing) 六周之后。Glasswing 是一个由 [Claude Mythos Preview](https://thenewstack.io/claude-mythos-preview-simulation/) 驱动的行业联盟，承诺实现类似的目标：以机器速度发现以前未知的漏洞，在授权环境中验证可利用性，并帮助防御者在攻击者行动之前完成补丁。

这两家实验室之间的趋同几周来显而易见：Mozilla 在 4 月 [披露](https://blog.mozilla.org/en/privacy-security/ai-security-zero-day-vulnerabilities/)，Firefox 150 修复了在 Mythos Preview 评估期间发现的 271 个漏洞，而随后发布的 GPT-5.5 结果也处于类似范围。

**本周公告中引人注目的是合作伙伴的重叠。** OpenAI 为 Daybreak 设立的三家启动合作伙伴已经加入了 Anthropic 的 Glasswing 联盟。Cisco、CrowdStrike 和 Palo Alto Networks 正在并行运行这两个技术栈，而不是选边站队。

> OpenAI 为 Daybreak 设立的三家启动合作伙伴中，有三家已经加入了 Anthropic 的 Glasswing 联盟。Cisco、CrowdStrike 和 Palo Alto Networks 正在并行运行这两个技术栈，而不是选边站队。

## Glasswing 走窄，Daybreak 走宽

Daybreak 和 Glasswing 做出了重叠的承诺。使用前沿模型配合智能体驱动来执行安全代码审查、威胁建模、漏洞分类、补丁验证和检测工程。尽管底层的驱动和部署模型不同，但公开的工作流语言惊人地相似。OpenAI 将 Daybreak 描述为结合了“最强大的 OpenAI 模型、Codex 以及我们的安全合作伙伴”。Anthropic 则将 Glasswing 描述为让防御者“利用我们最新的前沿模型 Claude Mythos Preview 抢占先机”。去掉品牌名称，两者的产品简介读起来大同小异。

不同之处在于准入门槛。

Anthropic 构建了一个围墙花园。Project Glasswing 启动时有 12 家指定合作伙伴，包括 AWS、Apple、Google、Microsoft、Nvidia、JPMorganChase、Cisco、CrowdStrike 和 Palo Alto Networks，并向大约 40 个维护关键软件基础设施的其他组织开放访问权限。Mythos Preview 本身是受限的。Anthropic 明确表示不打算向公众发布该模型。定价为每百万输入 token 25 美元，每百万输出 token 125 美元，并承诺提供 1 亿美元的积分，以支持联盟运行至研究预览期结束。该模型仅通过 Claude API、Amazon Bedrock、Vertex AI 和 Microsoft Foundry 提供，且仅限于 Anthropic 审核通过的参与者。

OpenAI 则构建了一个分层的信任框架。Daybreak 运行在三个模型变体上。GPT-5.5 是默认版本，带有标准安全防护，旨在用于一般的安全工作流。带有“网络安全受信任访问”的 GPT-5.5 旨在供经过验证的防御者处理代码审查、漏洞分类、恶意软件分析、检测工程和补丁验证。GPT-5.5-Cyber 是经过红队测试的受限变体，用于授权的红队演练、渗透测试和受控验证。启动合作伙伴包括 Cloudflare、Cisco、CrowdStrike、Palo Alto Networks、Oracle 和 Akamai，组织可以直接向 OpenAI [请求](https://www.macrumors.com/2026/05/11/openai-launches-daybreak/) 漏洞扫描。该框架读起来像是旨在让访问权限在验证层级内扩展。相比之下，Glasswing 的设计初衷似乎是坚守一条更窄的防线。

## “两头下注”的三家厂商

5 月 11 日公告中最能说明问题的细节是合作伙伴的重叠。Cisco、CrowdStrike 和 Palo Alto Networks 早已是 Glasswing 的启动合作伙伴。他们在 4 月初签署了 Anthropic 的审核联盟协议。六周后，他们又签署了 OpenAI 更广泛的框架。这种模式看起来不像是为了避险，更像是一种蓄意的双栈策略。

安全平台承担不起选错获胜模型的代价。如果 Mythos Preview 最终成为持久的前沿模型，Cisco 希望在其检测工程中使用 Claude。如果 Daybreak 因为访问模型更广泛而扩展得更快，Cisco 也希望 GPT-5.5-Cyber 参与其中。同样的逻辑解释了为什么 CrowdStrike 的 CTO 公开支持 Glasswing 为“首日”关键技术，随后 CrowdStrike 又出现在 OpenAI 的启动合作伙伴名单中。防御性安全工具在平台层必须与模型无关，否则平台就会暴露在单一供应商的路线图、定价和访问策略风险之下。

双栈策略背后的赌注是：模型现在已成为一个可替换的组件。驱动、集成表面和合作伙伴网络才是真正的产品。OpenAI 押注 Codex Security 加上更广泛的合作伙伴网能赢。Anthropic 押注于具有更深集成度的更窄联盟能赢。而在这两边同时下注的三家安全供应商则赌定：在足够长的时间内，两份押注都不会出错。

> 前沿实验室并不喜欢其旗舰产品在别人的平台中被平庸化为商品。

这里还有一个更难解读但值得指出的深层含义。前沿实验室并不喜欢其旗舰产品在别人的平台中被平庸化为商品。Anthropic 一直明确表示，Mythos Preview 不会作为通用 API 出售，且仅限于 Glasswing 联盟和一小部分云中介渠道。

OpenAI 则通过分层信任走向了相反的方向，但 GPT-5.5-Cyber 变体受到验证和账户级控制的限制，这看起来非常像换汤不换药的 Glasswing 访问规则。两家实验室都在努力将具备网络能力模型的价值保留在自己的商业版图内，且双方的合作伙伴名录都旨在将最大的安全厂商拉拢在身边，以便实验室仍能控制与终端客户的关系。

## 基准测试显示模型几乎相同

英国 AI 安全研究所 (AISI) 针对 GPT-5.5 [评估](https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities) 了与其 4 月份测试 Mythos Preview 时相同的 95 项夺旗赛任务套件。在专家级任务中，GPT-5.5 的平均通过率为 71.4%。Mythos Preview 为 68.6%。这一差距处于统计误差范围内，AISI 指出 GPT-5.5 可能是其迄今为止测试过的最强模型。作为对比，在相同的专家级任务中，GPT-5.4 的得分为 52.4%，Opus 4.7 为 48.6%。半年内的能力跨越巨大，但两家前沿实验室之间的差距却很小。

AISI 还运行了“最后的任务”（The Last Ones），这是一项包含 32 个步骤的模拟企业网络攻击，人类专家大约需要 20 小时才能完成。Mythos 在十次尝试中完成了三次。GPT-5.5 在十次尝试中完成了两次。绝对数值虽然较低，但六个月前还没有模型能完成这种模拟。两家不同的实验室，两种不同的访问模型，两个不同的驱动。底层能力看起来是一样的。AISI 本身将 GPT-5.5 的结果定性为：网络能力正作为通用自主性和编程改进的副产品出现，而非某个模型特有的功能。

这是一个值得深思的结构性洞察。当能力近乎相同，而访问模式不同时，访问模式就成了产品。Daybreak 真正的差异化在于信任框架、合作伙伴名录、审计追踪以及包裹模型的验证工作流。Glasswing 真正的差异化在于其联盟、信用承诺、披露协议和开源维护者访问层。模型是引擎，而访问模式是包裹它的汽车。

## 在 Daybreak 和 Glasswing 之间选择

安全团队现在必须对两者都进行评估。选择很少是二选一的，但权衡取舍已足够清晰。

| 需求 | 推荐平台 | 理由 |
| --- | --- | --- |
| 在多个安全团队中广泛部署 | Daybreak | 分层访问可扩展至更多经过验证的防御者 |
| 与少数关键系统深度集成 | Glasswing | 联盟模式包括 Anthropic 的深度参与 |
| 开源维护者访问权限 | Glasswing | 基于当前公布的承诺。Linux 基金会是启动合作伙伴，且有 400 万美元拨给开源安全捐赠 |
| 红队演练和渗透测试工作流 | Daybreak (带附加条件) | GPT-5.5-Cyber 专门为进攻性工作流分层，Glasswing 也支持经过审核的渗透测试工作 |
| 通过现有基础设施进行云原生部署 | 任意 | Mythos 可在 Bedrock、Vertex 和 Foundry 上使用，Daybreak 通过 OpenAI API 运行 |
| 防范供应商锁定 | 两者 | Cisco、CrowdStrike 和 Palo Alto Networks 都已签约加入两者 |

现实世界中的安全运营将结合使用两者。在实践中，不同之处在于驱动（harness）。Codex Security 是一个具备代码感知能力的智能体，在代码库范围界定、补丁生成和 CI 集成方面拥有强大的工具。Mythos Preview 则通过标准的 Anthropic 界面提供，联盟层增加了治理和披露结构。同时运行两者的团队最终会将不同类别的工作路由到不同的技术栈中，这正是 Cisco、CrowdStrike 和 Palo Alto Networks 所占据的有利位置。

## 下一步

前沿模型竞赛产生了一个可辨识的模式。一家实验室发布了一项能力。竞争对手在几周内发布同等能力。差异化从模型转向了包装。Cursor 和 Replit 在编程智能体上经历了这一过程。Anthropic 和 OpenAI 现在正通过安全智能体经历这一过程。驱动、访问模型和合作伙伴网络正在承担过去由模型承担的工作。

对于构建安全工具的开发者来说，实际意义在于从第一天起就针对模型的可替换性进行设计。驱动是长期存在的资产。其下的模型将会轮换。Daybreak 和 Glasswing 是首批发布前沿能力的两个网络 AI 平台。接下来的平台将来自 Google（它已经通过 Vertex AI 运行 Mythos Preview 并发布自己的安全运营智能体），以及来自 AISLE 和其他机构展示过的开源权重竞争者，这些竞争者被证明能以极低的成本复制旗舰级的漏洞分析能力。平台之战将围绕访问权限而非能力展开。