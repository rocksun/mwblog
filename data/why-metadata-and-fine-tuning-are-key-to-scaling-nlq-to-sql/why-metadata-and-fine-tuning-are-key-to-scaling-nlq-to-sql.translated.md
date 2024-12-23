# 为什么元数据和微调是将 NLQ 扩展到 SQL 的关键

![Featued image for: 为什么元数据和微调是将 NLQ 扩展到 SQL 的关键](https://cdn.thenewstack.io/media/2024/10/48bddca9-kerde-severin-4ghhdwjwuak-unsplash-1024x683.jpg)
[Kerde Severin](https://unsplash.com/@kseverin?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/turned-on-macbook-4ghHDwjwUAk?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

大量数据以结构化数据的形式存储在数十万个组织中。数百万的商业用户每天都使用这些结构化数据来运营业务，从中获得可以帮助改进业务运营的见解。存储这些结构化数据最流行的方式是使用 MySQL。其他流行的关系数据库包括 PostgreSQL、Microsoft SQL Server 和 Oracle 数据库。据估计，大约 60% 到 70% 的商业用户缺乏[编写查询的技术专长](https://thenewstack.io/a-software-developers-guide-to-technical-writing/)，这将使他们能够有效地与关系数据库交互。

大型语言模型 (LLM) 最常见的[应用](https://thenewstack.io/building-llm-based-genai-applications-with-amazon-bedrock/)之一是使商业用户能够将他们的查询作为自然语言查询 (NLQ) 提问，并将它们转换为可以执行的 SQL 查询。然后，整体解决方案将结果返回给商业用户。LLM 生成图表和摘要，商业用户可以轻松地与结果一起使用。

一个 NLQ 的例子是“按销售收入排列前五名的子品牌是什么？” LLM 将使用输入查询以及底层表元数据来生成相应的 SQL 查询：

转换后的 SQL 查询：“SELECT sub_brand, sum(net_sales) AS total_sales FROM Sales_Details_Table where item_quantity > 0 group by sub_brand order by total_sales DESC LIMIT 5”

现在，让我们根据我过去两年与财富 500 强公司合作的个人经验，探讨在将 NLQ 扩展到 SQL 实现时可能面临的主要挑战。我们还将讨论一些可行的解决方案，以帮助您克服这些障碍。

**挑战 1：数千张表时成本急剧上升**

为了将 NLQ 转换为 SQL，LLM 的输入是输入问题以及表的元数据。元数据通常描述表中的列。它们与表中行的数量无关，因此表的大小（以行数衡量）不会影响传递给 LLM 的令牌数量。但是，想象一下拥有数千张表，并且为每个问题传递这数千张表的元数据。LLM 消耗的令牌数量以及相关的成本都会激增。

为了减轻这个问题，我们实施了一种表选择策略。此分类器接收查询和表对，并确定表是否可以回答给定的问题。当提出问题时，将运行此表选择模块，并且只有前五到十个相关的表元数据以及查询将传递给 LLM。LLM 使用此信息来提出相应的 SQL 查询。由于我们减少了传递给 LLM 的令牌数量，因此相关的成本也降低了。

**挑战 2：没有单一的最佳 LLM，但提示很有帮助**

我们[在各种 RDBMS 系统上工作过](https://thenewstack.io/putting-ai-to-work-systems-of-intelligence-and-actionable-agency/)，在性能最佳的 LLM 方面没有明确的赢家。GPT-X 模型是一个很好的起点。但是，根据业务需求（例如，某个组织的首选合作伙伴是 GCP），模型的选择差异很大。与选择预训练的通用模型相比，选择这些模型的特定领域版本更好。我们看到这些模型与其对应模型相比具有明显的优越性能（例如，CodeLLama 与 Llama，CodeGemma 与 Gemma）。

无论选择哪个模型，提示都有助于[实现约 10% 到 20% 的性能提升](https://thenewstack.io/5-tips-to-achieve-performance-engineering-at-scale/)。以下是 NLQ 到 SQL 提示的示例：“表中的列名可能与问题中询问的信息不完全匹配。您需要使用提供的列描述选择列，并且根据用户的提问，您可能还需要通过进行一些数学运算来使用现有列派生新列。” 正确的模型选择与有效的提示相结合对于良好的性能至关重要。

**挑战 3：NLQ 到 SQL 中出现幻觉**
大型语言模型(GenAI)在问答中出现幻觉是一个众所周知并被广泛研究的现象。然而，LLM在根据自然语言查询(NLQ)生成SQL查询时产生的幻觉却是一个鲜为人知的课题。以下是一个生成SQL时出错的示例：

原始NLQ | 生成的SQL查询 | 正确的SQL查询 |
---|---|---|
查找所有存在时间超过六个月的项目及其分配的员工。 | `select t1.project_name, t1.employee_id from projects as t1 join employees as t2 on t1.employee_id = t2.employee_id where t1.end_date > 6 months` | `SELECT p.project_name, e.employee_id FROM projects p LEFT JOIN employees e ON p.employee_id = e.employee_id WHERE DATEDIFF(p.end_date, p.start_date) > 180` |

在这个例子中，有两个表：Projects和Employees。对于给定的查询，需要根据员工ID进行连接，并且项目持续时间必须超过六个月。如所示，LLM生成的查询计算持续时间的计算方式不正确。另一个[LLM出现幻觉的例子](https://thenewstack.io/3-ways-to-stop-llm-hallucinations/)是LLM无法确定正确的列来构成表中的列名。

为了解决幻觉问题，可以考虑以下方法：

- 创建一个查询测试集，迭代检查结果，并改进提示以确保不会出现幻觉。
- 当列名被虚构时，在提示中添加明确的指令，如果列名不存在则不要虚构列名。
- 微调模型（使用几百个示例），以便LLM熟悉模式和[SQL查询的业务逻辑](https://thenewstack.io/sql-and-complex-queries-are-needed-for-real-time-analytics/)的形成方式。在我们的实验中，微调将幻觉减少了高达10%。

**挑战4：简单的评估指标不足**

传统的根据查询的正确性来评估查询的方法对于NLQ到SQL来说是不够的。创建不同复杂程度的数据集至关重要，例如简单、中等和困难。在下表中，我们为每个数据集类别提供了一个示例定义。这些定义应该根据底层模式、业务查询等进行调整。

创建数据集的动机是，根据业务用户的查询复杂程度，模型可能只需要在简单和中等类别中达到很高的准确率就足够了。这确保了解决方案可以在不达到高准确率的情况下使用。

问题类型 | 定义 |
---|---|
简单 | - 使用OR和AND的0、1或2个WHERE条件的简单SELECT语句 |
中等 | - 带有多于1个WHERE或HAVING条件的GROUP BY<br>- 带有多于2个WHERE条件的SELECT语句 |
困难 | - 嵌套查询<br>- CTE<br>- 多列GROUP BY<br>- 日期操作 |

除了准确性之外，一致性是另一个应该包含的指标。一致性定义为模型对给定的NLQ产生相同结果的能力。需要注意的是，SQL查询可能不同，但结果将保持不变。测试SQL查询是否保持不变将很有趣。最后，另一个需要评估的指标是生成的SQL查询的效率。

**挑战5：元数据仅适用于约10%的表**

构建解决方案质量的主要驱动力是底层表元数据的质量和覆盖率。当我们与不同的企业合作构建解决方案时，一个主要的挑战是缺乏表的元数据。

解决这个问题的不同方法：

- 识别业务用户最常用的表，并确保为这些表手动创建元数据。
- 自动创建元数据。
- 使用GenAI系统检查每个表中随机抽取的几行来创建所有表的元数据草稿。
- 让专家检查和编辑元数据，以确保它们为表中的列提供正确的描述。

本文总结了在实现生产级企业级NLQ到SQL系统中的五大挑战。使用这些系统可以持续地达到超过90%的准确率。为了达到这种性能水平，重要的是要尝试不同的LLM模型，微调这些模型，并确保底层表具有元数据描述。

此外，拥有具有正确指标的合适评估数据集对于衡量系统质量至关重要。最后，通过确保与查询共享正确的元数据来管理成本将有助于组织从已实施的系统中获得足够的投资回报。
本文是The New Stack投稿网络的一部分。对影响开发人员的最新挑战和创新有独到见解？我们很乐意听到您的声音。填写此表格或发送电子邮件至mattburns@thenewstack.io联系Matt Burns，成为我们的投稿人并分享您的专业知识。

[YOUTUBE.COM/THENEWSTACK 技术发展日新月异，不要错过任何一期。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)