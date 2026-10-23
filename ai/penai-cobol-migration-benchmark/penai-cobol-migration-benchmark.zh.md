**本周，OpenAI 将 COBOL 推向了聚光灯下。**它[宣布](https://openai.com/index/low-resource-programming-languages/)了基准测试结果，表明其最新模型在迁移 COBOL 程序以及使用代码和文档较少（供模型学习）的语言构建软件方面变得更加出色。

在 OpenAI 自己的 COBOL 迁移测试中，GPT-6.1 Sol 在低推理强度下的准确率达到了 86.6%，高于 GPT-5.6 Sol 的 5.4%，同时成本降低了 39%。在更高的推理强度下，较新的模型达到了 97.9%。

但这两项评估背后的证据并不均衡。

OpenAI *尚未*公布其对 COBOL（“面向业务的通用语言”；AI 编码工具可用于维护或迁移的编程语言）评估的详细信息。它*已经*在 [GitHub](https://github.com/openai/MultiLangBench) 上发布了 MultiLangBench 设置和测试套件。该基准测试模型是否能够跨 20 种编程语言从头开始构建与 SQLite 兼容的数据库引擎。

OpenAI 的公告称这些结果是“两项评估的实质性改进，以更低的成本提供了更高精度的准确性。”

这些结果对于维护和现代化传统软件的团队至关重要。但如果没有公开的 COBOL 测试用例，开发者就无法独立审查该评估。

## **终于看到现代化 COBOL 的希望了吗？**

根据 OpenAI 的说法，其新的 COBOL 迁移评估“测试模型是否可以将现有程序迁移到另一种语言，同时保持其行为不变。”具体来说，它测试的是从 COBOL 到 C++、Java、Kotlin、Python 和 Rust 的迁移。

为了取得成功，每次迁移都必须通过一系列隐藏的测试，这些测试要求“可观测性输出的字节级奇偶校验”。凭借显著提高的准确性，GPT-6.1 Sol 确实显示出了实质性的进展。

![](https://cdn.thenewstack.io/media/2026/10/a7ebc9bc-cobol-migration-performance.png)

来源：OpenAI

测得的增幅令人惊叹，尽管 OpenAI 并不是第一家将 AI 引入 COBOL 现代化的公司。

尽管 COBOL 支撑了世界上大部分的金融交易和业务记录——[IBM](https://www.ibm.com/think/topics/cobol) 报告称，COBOL 支撑了超过 40% 的在线银行业务系统，支持 80% 的线下信用卡交易，并处理了 95% 的所有 ATM 交易——它仍然是 AI 编码工具的一个难点。

与 Python 和 JavaScript 相比，模型可用于学习的 COBOL 代码和文档较少。经验丰富的 COBOL 开发者也很难找到，而且文档往往滞后于他们维护的系统。

## **跨 20 种语言的 AI 编码增益**

除了 COBOL 迁移测试之外，OpenAI 还开发了第二项评估，以衡量模型从头开始构建软件的能力：MultiLangBench。该基准测试“测试模型是否可以跨 20 种不同的编程语言构建与 SQLite 兼容的数据库引擎。”

首先，程序获取数据库和 SQL 查询。然后，它生成一个修改后的数据库。参考的 SQLite 实现作为基本真相，以检查生成的数据库是否包含预期的数据。

![](https://cdn.thenewstack.io/media/2026/10/6d2a35c9-average-test-pass-rate-multilangbench.png)

来源：OpenAI

平均而言，GPT-6 Astra（[OpenAI 的旗舰模型](https://thenewstack.io/openai-gpt6-astra-benchmarks/)）在 20 种编程语言中的测试通过率达到了 87.4%，比 GPT-5.6 Sol 的 26.8%（ modest）有了大幅跃升。它在 20 种语言中的 19 种语言上得分超过 83%，并在所有语言上都做出了改进。

不出所料，[GPT-6 Luna](https://thenewstack.io/openai-gpt-6-sol-luna-release/) 的表现不如 Astra，这个低成本选项的平均通过率仅为 40.3%。话虽如此，它确实在测试的每种语言上都表现得比 GPT-5.6 Sol 更好，其估计的 API 成本降低了约 78%。

## **好吧，那就保守你的秘密吧。**

OpenAI 报告了其 COBOL 迁移评估和 MultiLangBench 的丰硕成果，但基准测试并不能说明全部问题。截至周四，使用私有代码库的 [Real-SWE 1.1](https://realswe.withspecific.com/) 将 Claude Opus 5.5 排在第一位，解决率为 56.8%。*The New Stack* 报道的[早期 Real-SWE 运行](https://thenewstack.io/real-swe-coding-benchmark/)有着不同的领先者和更低的分数。

另外，开发者仍然无法审查 OpenAI 的 COBOL 迁移基准测试。该公告将开发人员和企业客户的反馈归功于指导这项工作，但在没有基础测试和数据集的情况下，局外人无法独立检查结果。

OpenAI 承认了一个关键限制，并指出“将其应用于生产软件仍然需要专家审查以及根据系统的业务规则和依赖项进行测试。”

OpenAI 正在进入一个其他人已经工作了一段时间的领域。Anthropic 在 [2月23日](https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization) 概述了 Claude Code 如何协助 COBOL 现代化。正如 *The New Stack* 报道的那样，AWS 在 2024 年推出了用于大型机迁移的[智能体](https://thenewstack.io/aws-launches-new-ai-agents-to-simplify-legacy-migrations/)。