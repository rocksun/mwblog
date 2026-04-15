大语言模型非常擅长预测序列中的下一个单词。这是因为它们是在海量的非结构化文本——书籍、网页、代码上训练出来的。但企业数据看起来却大不相同。它存在于关系型数据库中：行和列将客户、订单、产品和交易联系在一起。LLM 无法原生对这些关系进行推理。

这就是关系型基础模型（relational foundation models）想要填补的空白。LLM 摄取文本语料库并学习 Token 之间的统计模式，而关系型基础模型则摄取结构化的表格数据，并学习连接跨表实体的模式。

周二，预测性 AI 专家 Kumo 详细介绍该领域的进展。该公司发布了 KumoRFM-2，这是一款旨在企业关系数据上表现优于完全监督机器学习的基础模型。

KumoRFM-2 由包括 [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/)（一个图机器学习库）共同创始人在内的团队构建，声称可以取代数月的特征工程和专用模型构建需求。

KumoRFM-2 是一个单一模型，可以在零训练的情况下使用自然语言进行查询，并且可以扩展到超过 5000 亿行数据。

Kumo 的首席执行官兼共同创始人 [Vanja Josifovski](https://www.linkedin.com/in/vjosifovski/) 将这项技术分解为最基本的术语。他表示，现在组织中的任何人都可以为每个预测任务生成自定义训练的模型。

“KumoRFM-2 是一款专门为关系型数据构建的基础模型，从底层开始就采用了自己的架构，”Vanja Josifovski 告诉 *The New Stack*。“工程师连接到他们现有的数据仓库，无论是 Snowflake、Databricks 还是任何 SQL 数据库，编写一个预测查询，然后就能收到结果。没有 [ETL 要求](https://thenewstack.io/from-etl-to-autonomy-data-engineering-in-2026/)，没有特征存储，也没有模型训练。”

## 基准测试晴雨表

在斯坦福 [RelBench v1](https://relbench.stanford.edu/) 深度学习基准测试中，KumoRFM-2 在分类和回归任务上的表现比其前代产品高出 10%，并比最强的监督机器学习模型高出 5%。

在 SAP SALT（销售自动完成关联业务表）企业基准测试中，KumoRFM-2 击败了诸如 [AutoGluon](https://aws.amazon.com/blogs/opensource/machine-learning-with-autogluon-an-open-source-automl-library/#:~:text=Using%20AutoGluon%2C%20you%20can%20train,prior%20experience%20in%20machine%20learning.)（来自 AWS 的开源机器学习框架）之类的表格模型集成，以及其他同类基础模型。团队表示，微调可以将模型的性能再提高 13%。

作为一种原生的关系型基础模型，KumoRFM-2 专为对数据库和数据仓库进行推理而构建。Kumo 的首席科学家兼共同创始人 Jure Leskovec 表示，这代表了真正的进步。毕竟，传统方法迫使数据科学团队在任何模型触及数据之前，必须将多表数据扁平化为单张表。

“KumoRFM-2 直接在连接表的图上运行，保留了每个外键关系，”Jure Leskovec 告诉 *The New Stack*。“它在单次前向传递中就能看到完整的关系结构，无需特定任务的训练，并且超越了在相同数据上进行端到端训练的监督基线。”

Jure Leskovec 同时也是斯坦福大学的教授，他进一步阐明了这里的运作结构，并表示团队还引入了分层上下文学习（hierarchical in-context learning），模型可以同时在单个表级别和跨表提取任务感知特征。其结果是一个开发人员可以指向数据仓库并立即获得预测的基础模型，而无需构建单个特征流水线。

## 其他基础模型技术

尽管 KumoRFM-2 声称实力强劲，但它并不是市场上唯一的基础模型技术。在该领域工作的工程师可能已经了解 [SAP-RPT-1](https://thenewstack.io/sap-expands-its-ai-stack-for-developers/)（关系型预训练 Transformer），这是一款旨在处理结构化、表格化业务数据的基础模型，无需为定制化机器学习训练提供大量负载。

MotherNet 是一个用于表格数据分类的超网络基础模型（或条件神经网络过程），它会创建一个小型神经网络。在发布该模型的论文中，团队指出 [MotherNet](https://arxiv.org/html/2312.08598v1) 经过训练可以生成网络，从而在任意表格数据集上执行多类分类，而无需任何针对特定数据集的梯度下降。

该领域的其他竞争者还包括 [TabICL](https://github.com/soda-inria/tabicl)，这是一个完全开源的学术项目，旨在提供一个无需超参数调优的表格基础模型，并可以通过 [上下文学习](https://github.com/soda-inria/tabicl) 扩展到拥有超过一百万行的数据集。

亚马逊 AWS 的 Mitra 也是一个表格基础模型。Amazon Science 将 [Mitra 描述为](https://www.amazon.science/blog/mitra-mixed-synthetic-priors-for-enhancing-tabular-foundation-models) 在“合成数据集上预训练”的模型，这些数据集由精心设计的先验分布（priors）混合生成。

## 预测信号存在于关系中

Kumo 的 Vanja Josifovski 提醒我们，最有价值的预测信号存在于数据仓库中跨多个表的关系中，但传统方法在建模开始前就将多表数据扁平化为单张表，这强调了其公司在市场中的地位。

“KumoRFM-2 改变了这一点：它是唯一真正理解表之间关系而不是破坏关系的模型，它可以扩展到数千亿行，并让任何团队都能用自然语言提出预测性问题，”他说道。

为了在现实用例中保持长期耐用性，Kumo 团队表示，该技术在构建时考虑了对噪声、缺失数据和结构退化的鲁棒性。通过汇总关系图中的信息，该模型有效地从相邻实体和表中“填补”缺失信息。

随着基础模型技术的许多开发工作仍处于研究机构、学术团体和供应商研发部门内，这可能是 AI 主导权争夺的下一个战场。