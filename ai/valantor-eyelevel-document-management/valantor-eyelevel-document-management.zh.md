AI 数据摄取流水线对[语言](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)、数值和表格数据的渴求似乎永无止境，同时其他外围平台也在同步构建大型音频、图像和视频模型。

横跨所有这些领域的，是复杂文档和各类[非结构化数据](https://thenewstack.io/what-is-unstructured-data/)所处的存储结构；在现代 AI 所汲取的“源 DNA”方面，这曾是一条鲜有人走的路。

## 无模式、自由格式、未经整理的数据湖

为了建立与所有组织自然拥有的无模式、自由格式、未经整理的信息之间的连接，企业视觉智能公司 [Valantor](https://www.valantor.com/) 于周二宣布收购非结构化信息 RAG 专家 [EyeLevel](https://www.eyelevel.ai/)。此次收购正式推出了 Valantor 的企业视觉智能平台，将 EyeLevel 的文档智能与其自身的运营专业知识相结合。

EyeLevel 的首席执行官兼联合创始人 [Benjamin Fletcher](https://www.linkedin.com/in/benjamin-fletcher-bb73334/) 告诉 *The New Stack*，在 AI 时代，如果组织未能采用视觉智能，仅靠人工的处理方式很快就会崩溃。

“大约 [80% 的企业知识](https://www.databricks.com/blog/pdfs-production-announcing-state-art-document-intelligence-databricks)存在于数以百万计视觉上极其复杂的 PDF、PPTX 和 DOCX 文件中，”Fletcher 说道。“这些信息远远超出了任何大语言模型（LLM）上下文窗口的容量，实际上 LLM 和智能体无法直接访问它们。”

> “我们发现，团队手工构建的黄金数据集通常带有 10% 到 25% 的错误率。具有讽刺意味的是，这些团队往往用比对待人类员工严苛得多的标准来要求 AI。”

## 人工处理：缓慢、昂贵且易出错

他解释说，事务性工作流（如发票和索赔处理）通常涉及“视觉上极其复杂且多样化”的文档，以至于企业仍然依赖人工来处理，而人工处理往往速度慢、成本高且容易出错。

“我们发现，团队手工构建的黄金数据集通常带有 10% 到 25% 的错误率，”Fletcher 说。“具有讽刺意味的是，这些团队往往用比对待人类员工严苛得多的标准来要求 AI。如果数据主权对企业很重要，那么现在一切都变得更难了：在文档保存在您自己的基础设施内的情况下，利用 AI 解决这些问题是该领域的高难度模式，很少有工具能做到。”

## 不可见的企业信息存储在哪里？

Valantor 指出，虽然大多数 AI 公司专注于模型，但该公司本身今天“专注于那些模型无法看见的信息”。这种未被发掘的海量宝贵数据被锁在文档、索赔文件、合同、工程图纸、报告、表格、演示文稿以及其他视觉复杂的原始内容中。

Valantor 的旗舰平台产品 GroundX 在数据驻留的地方运行，包括私有云、主权基础设施、本地部署和完全物理隔离的环境。

“GroundX 是非结构化文档的摄取和检索层，”Fletcher 解释道。“它是一个高度调优的系统，检索的内容正是摄取过程所生成的。一切都通过 REST API、SDK 和 MCP 暴露。它以 REST API、SDK 和 MCP 的形式发布，Helm 图表可以直接放入团队现有的部署流水线中，我们的智能体工具包赋予了像 Claude 和 Codex 这样的编码智能体构建集成的技能。”

作为收购公告的一部分，Valantor 推出了 [GroundX Studio](https://www.valantor.com/#groundx-studio)。GroundX Studio 中的工具包功能与现代 AI 开发环境集成，使开发人员能够在保持现有基础设施的同时，构建基于企业知识的各种安全 AI 应用。

GroundX Studio 还将功能扩展到业务用户，使组织无需进行大量的定制开发即可创建基于 AI 的工作流和应用程序。

> “每个智能体只做一项小任务，因此更便宜的模型通常就足够了，而希望直接控制成本的团队可以在自己的硬件上使用 Helm 运行整个技术栈。”

## 延迟性能和成本螺旋上升的风险？

如果觉得这种新的数据摄取流会对云工作负载、应用程序执行延迟、数据库检索时间和（当然）整体 Token 使用量造成额外负担，那么 Valantor 和 EyeLevel 表示，通过其自身平台的编排层，这些考虑因素已被纳入考量。

**“**我们从不将整个原理图发送给语言模型；我们的视觉模型首先将每一页拆解为各个元素，”Fletcher 证实。“处理过程在文档的不同级别上分多次运行，且每次运行中的所有内容都并行处理，因此存在最小处理时间，但它不会随页数的增加而线性扩展。每个智能体只做一项小任务，因此更便宜的模型通常就足够了，而希望直接控制成本的团队可以在自己的硬件上使用 Helm 运行整个技术栈。”

## AI 与手写体的交叉点

虽然我们已经知道 AI 和手写体在同一个鸡尾酒杯中混合——[ViWoods AiPaper](https://viwoods-eu.com/?utm_source=Google_CPC&utm_medium=Google_CPC&utm_campaign=Search-12&gad_source=1&gad_campaignid=23263953290&gbraid=0AAAABAvr13pEXv0R7LZAuPWJ4_awxrrLs&gclid=Cj0KCQjwsMLSBhD9ARIsAIpUTDq3CDtec8WME1EQkMXFJHCCxRFCXOjxpAkBJ1bL_PnaxhUZf4a6OCMaAqMFEALw_wcB) 数字电子墨水手写板内置了一套实用的 AI 功能，而包括 [reMarkable](https://remarkable.com/products/remarkable-paper/pure?utm_source=google&utm_medium=paid&utm_campaign=tt01-co01-dn01%7Cgse%7Cprosp%7Cpurchase%7Cbrand-uk%7C0226&utm_content=tt01-co01-dn01%7Cuk%7Ckeyword%7Cbrand-exactsearch%7C0226&utm_term=23646619836,195097822238,807817876021&gad_source=1&gad_campaignid=23646619836&gbraid=0AAAAACTQ8CyvJMCFr1CpcmQJFJmkFdAk6&gclid=Cj0KCQjwsMLSBhD9ARIsAIpUTDq9Yl5TNt4z6caf3jWoXRMDtmIEKY3Ptuust0dc0_5cS9osWGm5naIaAtUsEALw_wcB) 在内的制造商也提供了类似产品——但这还不是一个被广泛部署的用例。Valantor 声称其底层数据模型和自定义启发式算法在处理手写标注时弥合了“数据理解差距”。

“我们专有的视觉模型在超过一百万页的企业文档上进行了微调，它以人类的方式查看页面：识别表格、段落和图形，”Fletcher 强调道。

他说，手写标记被捕获为页面元素，同时保留了其布局上下文。随后，精简的智能体将每个元素提炼成一个专门用于搜索和 LLM 补全的上下文对象。

“碎片化程度更低，认知负荷更小——这就是我们弥合差距的方式，以更低的成本实现更高的准确性，从而推动更好的性能和显著的成本优势，”他补充道。

该技术的成功案例包括法航荷航集团（Air France-KLM），他们使用 GroundX 开发了一个 AI 驱动的客户服务助理，该助理基于数千份政策文件进行了训练，在处理复杂的政策相关问题时实现了超过 96% 的准确率。AskVet 使用该平台将其十多年来的专有兽医数据投入运营，使高达 85% 的客户咨询得以自主解决，同时显著提高了运营效率。

## 文档管理现在变得性感了吗？

考虑到所有这些，我们是否达到了可以问“文档管理是否变得有趣、引人注目且性感”的程度？

当然没有；可以说它将永远受到某种程度的蔑视。未来随着我们更直接地与开始分析那些组织长期囤积的非结构化信息的 AI 工具交互，这种情况可能会发生变化。就目前而言，它可能仍然是企业界的“吃蔬菜”——请递给我[球芽甘蓝](https://www.healthyseasonalrecipes.com/wp-content/uploads/2023/11/simple-steamed-brussels-sprouts-1200-024-scaled.jpg)和清蒸芜菁，谢谢。