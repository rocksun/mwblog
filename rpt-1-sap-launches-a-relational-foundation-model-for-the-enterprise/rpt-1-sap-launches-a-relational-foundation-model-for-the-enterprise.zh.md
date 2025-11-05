德国柏林——德国商业软件巨头 [SAP SE](https://www.sap.com/index.html?utm_content=inline+mention) 本周正在柏林举办其年度 TechEd 活动，该公司在其公告中将重点放在人工智能上不足为奇。毕竟，人工智能在今年早些时候已经是该公司[旗舰 Sapphire 大会](https://thenewstack.io/sap-unveils-new-ai-tools-for-developers/)的焦点。然而，令人意外的是，SAP 今天宣布了其首个基础模型：SAP-RPT-1。

SAP 将 SAP-RPT-1 称为“首个企业关系型基础模型”，它将于今年晚些时候全面上市，因为它天生旨在帮助用户处理关系型和结构化业务数据。今年晚些时候，它将以小型和大型模型的形式在 SAP 平台上提供（尽管 SAP 尚未披露这些模型的具体大小），但也将作为开放权重模型[在 Hugging Face 上](https://huggingface.co/SAP/sap-rpt-1-oss)提供。

“我们看到了行业中的空白，”SAP 业务技术平台 (BTP) 首席营销官 Bharat Sandhu 在我问他公司为何决定构建自己的模型时告诉我。传统上，大型语言模型主要通过大量非结构化数据进行训练。因此，Sandhu 指出，它们擅长预测文本，但在进行数学计算时却很困难。

[![](https://cdn.thenewstack.io/media/2025/11/27e30d5c-architecture.png)](https://cdn.thenewstack.io/media/2025/11/27e30d5c-architecture.png)

ConTextTab 模型（现为 SAP-RPT-1）的架构图（图片来源：SAP）。

RPT（发音为“rapid”）代表“关系型预训练转换器”，其重点在于预测常见业务场景的结果，而不是句子中的下一个词。长期以来，这是各种深度学习和机器学习算法的领域，但关系型基础模型目前是一个非常活跃的[研究领域](https://openreview.net/forum?id=HNKZJJ8xQV)，值得注意的是，有一些像 [Kumo](https://kumorfm.ai/get-started) 这样的初创公司也正在这个领域开展工作。

SAP 的研究团队今年早些时候发布了一篇关于其在人工智能和表格数据方面研究的深度论文。当时，该模型仍被称为 [ConTextTab](https://arxiv.org/pdf/2506.10707)。与大多数模型构建者不同，SAP 披露它使用了 [Tremendous TabLib Trawl](https://huggingface.co/datasets/mlfoundations/t4-full) (T4) 数据集来训练其开放权重模型。这个来自 Approximate Labs 的 1.34TB 数据集包含大约 310 万个表格，范围从体育数据到立陶宛工业设施的排放数据。

对于商业模型，SAP 用更广泛来源的数据丰富了该模型，这可能会使其性能优于开放模型。

[![](https://cdn.thenewstack.io/media/2025/11/31cc8d96-1762270606187.jpeg)](https://cdn.thenewstack.io/media/2025/11/31cc8d96-1762270606187.jpeg)

图片来源：SAP。

由于 SAP 的模型是针对此用例进行预训练的，SAP 认为，如果客户希望对结构化数据进行推理，这个新模型将允许他们跳过任何额外的训练或微调。通过上下文学习，SAP-RPT-1 可以通过简单的 API 调用对表格数据执行分类和回归。

“传统机器学习的问题在于你必须训练模型，”Sandhu 说。“你必须拥有数据。你必须确保它不会在某种程度上过度偏向。你必须训练它，所以这需要时间和专业知识。因此，RPT-1 本质上是一个通用的关系型模型，可以在表格数据上进行这些通用类型的预测和预报等等。”

对于想要尝试该模型的用户，SAP 还将推出一个免费的基于网络的体验，名为 [SAP-RPT Playground](https://rpt.cloud.sap/)（但文件类型仅限于最大 2,073 行和 50 列的 CSV 文件）。其中的示例侧重于 SAP 期望该模型实现的许多标准用例，例如预测即将到来的维护需求、支付风险和客户流失。