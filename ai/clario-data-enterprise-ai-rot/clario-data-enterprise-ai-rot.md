<!--
title: AI没坏，坏的是你的数据
cover: https://cdn.thenewstack.io/media/2026/06/9e5705cd-elantro-nax1wlfchak-unsplash.jpg
summary: 企业在AI上投入巨大却成效甚微，核心原因是数据中充斥着冗余、过时和琐碎的“腐烂数据”。初创公司Clario通过自动化识别并清理这些垃圾数据，旨在提升企业数据质量，从而让AI项目真正产生商业价值。
-->

企业在AI上投入巨大却成效甚微，核心原因是数据中充斥着冗余、过时和琐碎的“腐烂数据”。初创公司Clario通过自动化识别并清理这些垃圾数据，旨在提升企业数据质量，从而让AI项目真正产生商业价值。

> 译自：[Your AI isn't broken. Your data is.](https://thenewstack.io/clario-data-enterprise-ai-rot/)
> 
> 作者：Darryl K. Taft

企业正投入数十亿美元开发AI，但得到的结果却一团糟。一家新初创公司表示，他们知道原因所在，并构建了首个旨在解决此问题的平台。

Clario 周三宣布结束隐身状态，并获得了 600 万美元的种子轮融资，旨在解决联合创始人兼首席执行官 [Yousuf Khan](https://www.linkedin.com/in/yousufakhan/) 所称的“数据 ROT”问题：即冗余、过时和琐碎的文件，它们不仅推高了存储成本，还在源头上“毒害”了 AI 项目。

“在 ChatGPT 发布四年后，企业已经在那些未能产生重大影响的项目上花费了数十亿美元，”Khan 在一份声明中表示。“‘垃圾进，垃圾出’不再是一句陈词滥调，而是一个代价极其高昂的错误。”

行业估计显示，超过三分之一的存储[企业数据](https://thenewstack.io/how-precog-adds-business-context-to-make-enterprise-data-ai-ready/)属于垃圾类别。Gartner 预测，到今年年底，60% 的 AI 项目将因为数据质量差而被放弃。Khan 表示，Clario 早期的客户工作显示这一比例更高。在与设计合作伙伴的测试中，该公司发现垃圾率高达 60%。

Khan 曾五次担任 CIO，曾在 Pure Storage 和 Moveworks 任职，之后成为 Ridge Ventures 的合伙人。他说他在每一个职位上都遇到了同样的障碍。“我曾多次尝试用所有的大型文件系统解决这个问题，但都失败了，”他告诉 *The New Stack*。随着 ChatGPT 发布后 AI 生成的内容开始涌入企业存储库，这个问题变得更加严重。

联合创始人兼首席技术官 [Madhu Vohra](https://www.linkedin.com/in/madhu-vohra/) 带来了基础设施方面的经验。她的职业生涯致力于构建这些数据的归宿系统——曾在 NetApp 设计集群 SAN，在 Nutanix 扩展工程团队，并领导了 Oracle 在 OCI 中的块存储和对象存储业务。

“我构建了主要系统，让人们能够积累数据，”她告诉 *The New Stack*。“所以，我现在是在赎罪。”

## 工作原理

Clario 直接连接到企业文件和内容系统，包括 [Google Drive](https://thenewstack.io/address-high-scale-google-drive-data-exposure-with-bulk-remediation/)、SharePoint、OneDrive、Box 和 Confluence，并通过扫描元数据来找出垃圾文件，而无需打开文件本身。Vohra 表示，目前的分类是基于启发式的，利用文件校验和、命名模式、访问时间戳和格式支持状态进行分析。她指出，AI 和基于嵌入（embedding）的检测已在路线图中。

当 Clario 标记出一个文件时，它会通过 Slack 或 Teams 触发一个工作流，通知内容的创建者或所有者，并询问他们是保留、归档还是删除。系统会从这些决定中学习，从而随着时间的推移构建一个日益自主的清理引擎。Clario 只有在客户对标记文件采取行动时才会获得报酬。这是一种基于成果的模型，将公司的激励机制与实际的数据减少量保持一致。

ROT 分为三类：冗余文件（重复和近似重复文件）、过时文件（无人能打开的旧格式、多年未触碰的文档、已离职员工的内容）和琐碎文件（隐藏文件、杂讯）。Vohra 说，早期客户分析发现了 TB 级的垃圾，包括已停产产品线的知识库文章，以及前员工下载的完整长度电影。

为了避免误报，Clario 的模型针对精确度进行了优化，旨在仅标记出其确定为垃圾的文件。

“任何我们认为难以辨认的内容，我们都想提出来，”Khan 说。他补充道，目标是先处理“低垂的果实”，在进入更模糊的领域之前建立信任。

## AI 成本角度

时机的争论不仅仅关乎存储账单。当企业构建内部代理（Agent）和基于 [RAG](https://thenewstack.io/a-blueprint-for-implementing-rag-at-scale/) 的系统时，底层数据的质量直接决定了这些系统是否有效。Vohra 直言不讳地指出：“我的 AI 出现幻觉，是因为你喂给它 1500 万个文件吗？”

Khan 表示，他从 Token 经济学的角度看待这个问题：构建在不干净知识库上的内部代理，迫使 [LLM](https://thenewstack.io/llm/) 筛选过时的政策、停产的产品文档和过时的支持文章，从而在杂讯上浪费了计算预算。

“你实际上是在处理垃圾 Token，”他指出。

一位拥有 550 万个文件的早期客户发现，超过 20% 是“数据 ROT”，而且这些数据主要追溯到四名离职员工。

## 竞争格局

Khan 承认该领域参与者很少。他说，备份供应商和归档公司只触及了数据清理的边缘，但没有一家构建了从分类到员工通知，再到采取行动和学习的端到端工作流。“如果他们能做到，我早就用了，”他说。“我还没见过一家公司能做到这一点。”

Vohra 指出，压缩和存储效率工具解决的是存储成本问题，而不是存储数量的问题。“问题的核心仍然是，你拥有的 1500 万个文件，依然是那 1500 万个问题。”

## 投资者与客户

“企业数据危机并不是新鲜事，但今天忽视它的代价变得让人无法接受，”Preface Ventures 合伙人 [Saad Siddiqui](https://www.linkedin.com/in/saadsiddiqu/) 在一份声明中说。“我们支持 Clario，因为他们是唯一一家致力于在基础层面让企业实现 AI 就绪的公司。”

Clario 在早期分析和部署中拥有大约十几家客户。该公司成立约六个月，计划从文件和内容系统扩展到图像存储库、视频存储以及 ServiceNow 和 Salesforce Service Cloud 等平台中的知识库。

Khan 用简单的话概括了产品愿景：“我们的目标是确保数据卫生在企业中成为一个持续的过程。”