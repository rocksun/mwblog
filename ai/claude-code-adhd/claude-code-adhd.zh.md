本周，独立研究员 [Udit Akhouri](https://www.linkedin.com/in/udit-akhouri-10160a168/) 在 Reddit 的 [r/ClaudeCode](https://www.reddit.com/r/ClaudeCode/comments/1tny93g/i_gave_claude_code_adhd_and_it_thinks_2x_better/) 版块发布了一款全新的第三方 Agent SDK 工具，标题为：“我给 Claude Code 注入了‘多动症’（ADHD）……现在它的思考能力提升了 2 倍。”

正如 [GitHub](https://github.com/UditAkhourii/adhd) 上的描述，ADHD 是一个基于 Claude Agent SDK 构建的编程 Agent 技能；它能够“在不同的认知框架下发散出平行的差异化想法、进行评分、剪枝陷阱，并加深对留存想法的探索。”

该工具在 GitHub 上的流量增长迅速，但一些研究人员对其新颖性以及“提升 2 倍”的说法仍持怀疑态度。

## 注入“多动症”后的 Claude Code 是什么样子的

Udit Akhouri 是 Brane Labs 的创始人，该实验室是一家致力于 AI 辅助医疗、药物研发和生命科学领域的 AI 合规与安全研究实验室。他同时也是 Exthalpy 的创始人，这是一个面向门诊诊所和医院的临床自主平台。

他的[论文](https://uditakhourii.github.io/adhd/)《ADHD：编程 Agent 的并行发散式构思》（ADHD: Parallel Divergent Ideation for Coding Agents）将 ADHD 描述为“具有认知框架分支、生成器-评论器分离以及剪枝功能的思维树”。在 Reddit 的帖子中，Udit Akhouri 表示该工具的灵感“来自于多动症患者的大脑运作方式——向多个方向思考，并深入探索其中少数几个”。换句话说，注入“多动症”的 Claude Code 会分化出多个孤立的推理分支，对其进行评估，并重点发展最有可能成功的分支。

当被问及该工具的真正用途时，Udit Akhouri 告诉 *The New Stack*，ADHD“非常适合头脑风暴和规划，而不是直接写代码”。

具体来说，他将 ADHD 定位为“AI Agent 的推理和规划层”。它的设计初衷并不是为了帮助更快地编写代码，而是在编写代码之前支持架构选择和研究决策。

## 这真的是什么新鲜事吗？

客观地说，可以说是，也可以说不是。

当被问及 ADHD 带来了什么新颖之处时，Empromptu.ai 的首席技术官兼联合创始人 [Sean Robinson 博士](https://www.linkedin.com/in/sean-robinson-phd/) 告诉 *The New Stack*：“我不认为这是一种严格意义上的全新 Agent 模式。它看起来像是一种常见的并行采样和选择策略，但以一种有趣的方式进行了包装，适用于工程决策。”

在 Udit Akhouri 发布其成果的 Reddit 帖子里，社区的一些观点呼应了 Sean Robinson 的评论。一位 Reddit 用户[表示](https://www.reddit.com/r/ClaudeCode/comments/1tny93g/comment/onxwgmn/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)：“这不就是 GPT Pro 所做的吗？它并发运行多个超高评估，然后对它们进行评估，并使用得分最高的那个。” 另一位用户[附和道](https://www.reddit.com/r/ClaudeCode/comments/1tny93g/comment/onxptf2/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)：“我还以为这已经是 Agent 团队背后的概念了呢？”

> “我不认为这是一种严格意义上的全新 Agent 模式。它看起来像是一种常见的并行采样和选择策略，但以一种有趣的方式进行了包装，适用于工程决策。”

当被直接问及 ADHD 的独特之处时，Udit Akhouri 告诉 *The New Stack*：“GPT Pro 的并行评估模式和 CrewAI 的 Agent 团队是并行处理的实现，但它们是封闭的、不透明的，且终端用户无法进行组合。” 相比之下，他表示 ADHD 是“一个存在于你的 Claude 环境中、显式且可读的层”。在与 GPT Pro 和 CrewAI 风格的 Agent 团队竞争时，他认为 ADHD 凭借“透明度和可组合性”脱颖而出。

当被问及看法时，Lovelace AI 的现任 CEO、前谷歌副总裁、卡内基梅隆大学前院长兼教授 [Andrew Moore](https://www.linkedin.com/in/andrew-moore-016b751/) 似乎理解 Udit Akhouri 的初衷。他告诉 *The New Stack*：“[ADHD 中]真正具有创新意义的想法是，找到了在平行思考者集合中创造多样性的另一种方法。”

## 它真的能让 Claude Code “思考能力提升 2 倍”吗？

这正是分歧所在。

当被问及他是如何得出“2倍”这一结论时，Udit Akhouri 指出了评估指标：“‘2倍’的表述是通过对各个维度取平均值后得出的。”

也就是说，在六个测试问题中，有五个问题显示 ADHD 的得分超过了基准。 [GitHub](https://github.com/UditAkhourii/adhd/blob/main/EVALS.md) 上的评估标准给出了以下增量：广度（breadth）+4.17；新颖性（novelty）+5.17；陷阱检测（trap\_detection）+7.67；可操作性（actionability）+3.00；对构建者的实用性（builder\_usefulness）+0.83。

![](https://cdn.thenewstack.io/media/2026/05/88a11732-claude-code-adhd-aggregate-scores.png)

图片来源：[GitHub](https://github.com/UditAkhourii/adhd/blob/main/EVALS.md)

Udit Akhouri 表示，这些评估是完全透明的，并已在 GitHub 上进行了记录，“任何人都可以通过运行 `npm run evals` 随时进行独立复现。”

但值得注意的是，陷阱检测（trap\_detection）对曲线的波动起到了多大作用。凭借 +7.67 的增量，陷阱检测在平均值计算中占有很大比重；将其移除后，平均值会从 2.52 倍缩水至 1.85 倍。

> “宣称‘好 2 倍’不仅需要几次开放式的胜利。它还需要一个经过验证的评估集、多名评委、消融实验，以及证明该方法确实有所改进，而不仅仅是奖励冗长性、新颖性或分支多样性。”

其次是关于基准测试规模的担忧。 Sean Robinson 表示：“六个工程问题确实很有意思，但不足以将这一结果视为具有普适性。宣称‘好 2 倍’不仅需要几次开放式的胜利。它还需要一个经过验证的评估集、多名评委、消融实验，以及证明该方法确实有所改进，而不仅仅是奖励冗长性、新颖性或分支多样性。”

Agiloft 的 AI 运营副总裁 [Noe Ramos](https://www.linkedin.com/in/noe-ramos-psyd-3a1808178/) 在被问及 ADHD 的评估时，向 *The New Stack* 表达了类似的观点：“在没有建立起评分者间信度的情况下，陷阱检测和新颖性等维度的提升虽然很有趣，但目前还不是稳定的发现。‘好 2 倍’的说法需要六个以上的问题支撑才站得住脚。”

还有一个问题是，同构栈熟悉度（即该方法建立在 Claude 的技术栈上，并由 Claude 家族的模型进行评判这一事实）是否与得分有关。Sean Robinson 和 Noe Ramos 都指出同构栈偏差（same-stack bias）可能在起作用——前者表示，“这并不意味着结果无效，但这意味着论文应该测试外部评委和其他模型家族。”

## 下一步的发展方向

尽管人们对新颖性或评估分数有一些质疑，但注入了 ADHD 的 Claude Code 似乎已经蓄势待发。 Udit Akhouri 告诉 *The New Stack*，Repowire “已自本周起积极将 ADHD 整合到他们的技术栈中”。在撰写本文时，GitHub 显示该技能已获得 286 个 Star 和 12 个 Fork。

但 RelationalAI 的机器学习研究副总裁 [Nikolaos Vasiloglou](https://www.linkedin.com/in/vasiloglou/) 告诉 *The New Stack*，带有 ADHD 的 Claude Code “只是位于大语言模型之上的又一种探索方法”，而且它出现的时候，行业正面临着 Token 消耗问题：“虽然 ADHD 的效果令人印象深刻，但它出现的时间节点，正值各大企业因过度消耗 Token 而苦恼不已之际。”

## 那么这个名字呢？

用一种神经发育障碍来命名编程 Agent 的技能是一个大胆的举动——这无疑会吸引人们的眼球。但 Udit Akhouri 坚持认为，这个命名是自然而然想到的，而非出于营销目的：

“我们 [Brane Labs] 在研究工作流程中大量使用 Claude Code，但总是遇到同样的瓶颈：它的推理深度足够，但过于狭窄，呈线性。它会沿着一条路走得很远，却完全忽略了横向的联系。就在那时，ADHD 的概念突然闪现在脑海中。”

Udit Akhouri 将自己描述为“亲身熟悉 ADHD 大脑运作方式的人”，他告诉 *The New Stack*，他希望在大语言模型的沙盒中模拟 ADHD 的思维结构，并期望借此“揭示纯线性思考者会忽略的模式”——不过他澄清说，这个名字只是一个比喻，并非神经科学层面的主张。

当被问及对第三方 Agent SDK 工具使用临床疾病名称进行品牌推广的立场时，Anthropic 未作回应。