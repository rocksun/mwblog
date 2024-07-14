# 亚马逊 Q 应用：面向所有人的 AI 驱动的开发

![Featued image for: Amazon Q Apps: AI-Powered Development for All](https://cdn.thenewstack.io/media/2024/07/5eebb191-jean-woloszczyk-lk-f47mlmtk-unsplash-1024x683.jpg)

领先的云服务提供商正处于快速扩张的 [生成式 AI](https://thenewstack.io/generative-ai-tools-for-infrastructure-as-code/) (GenAI) 市场竞争的早期阶段，所有公司都在努力确保备受追捧的开发人员选择他们的平台进行工作。

正如 The Enderle Group 的首席分析师 [Rob Enderle](https://www.linkedin.com/in/rob-enderle-03729/) 对 The New Stack 所说：“如果你没有开发人员，你不仅会失去他们作为客户，还会显著降低你的云产品对其他潜在客户的吸引力，可能使你的云服务变得无关紧要。”

在本周的 [AWS 纽约峰会](https://aws.amazon.com/events/summits/new-york/) 上，[亚马逊网络服务](https://aws.amazon.com/?utm_content=inline+mention)（在某些圈子里被认为落后于 [GenAI 曲线](https://thenewstack.io/decoding-amazons-generative-ai-strategy/)，落后于 [微软](https://news.microsoft.com/?utm_content=inline+mention) 及其 [Azure 云](https://thenewstack.io/microsoft-copilot-for-azure-managing-cloud-ops-through-chat/)）推出了两个具有类似目标的工具：让开发人员和其他技术水平较低的员工能够通过 GenAI 提示启动企业应用程序。

[AWS](https://thenewstack.io/aws-gifts-java-rust-developers-with-useful-tools/) 的 AI 和数据副总裁 [Swami Sivasubramanian](https://www.linkedin.com/in/swaminathansivasubramanian/) 在 [博客文章](https://aws.amazon.com/blogs/machine-learning/empowering-everyone-with-genai-to-rapidly-build-customize-and-deploy-apps-securely-highlights-from-the-aws-new-york-summit/) 中写道：“我们正在为客户提供工具，将生成式 AI 的力量赋予所有员工手中，提供更多方法来创建个性化和相关的生成式 AI 驱动的应用程序，并解决诸如减少幻觉等难题，以便更多公司能够从生成式 AI 中获益。”

**简化 AI 应用程序开发**

[Amazon Q Apps](https://aws.amazon.com/blogs/aws/amazon-q-apps-now-generally-available-enables-users-to-build-their-own-generative-ai-apps/) 是 [Amazon Q Business](https://aws.amazon.com/q/business/) 中的一项新功能，员工可以使用它来构建自己的 GenAI 应用程序，以回答问题、创建和汇总内容以及利用企业数据。Amazon Q Apps 允许员工通过在 Amazon Q Business（于 4 月推出的 GenAI 助手）中描述所需的应用程序来快速创建基于公司数据的 AI 驱动的应用程序。这项新工具现已全面上市，将立即生成应用程序。

据 Sivasubramanian 介绍，在 Amazon Q Apps 的预览期间，用户能够创建用于各种用途的应用程序，从汇总反馈和创建入职计划到撰写文案和备忘录。他提到了数据安全公司 Druva，该公司通过该工具创建了一个应用程序，用于几乎立即汇总提案请求的信息，将 RFP 响应时间缩短了 25%。

同时，[AWS App Studio](https://aws.amazon.com/blogs/aws/build-custom-business-applications-without-cloud-expertise-using-aws-app-studio-preview/) 现已进入预览阶段。这是一项基于 AI 的服务，面向 IT 项目经理、数据工程师、开发人员和企业架构师等技术人员，他们可以使用 [自然语言](https://thenewstack.io/what-temperature-means-in-natural-language-processing-and-ai/) 描述他们想要构建的应用程序，概述其功能，并包含要利用的数据源，App Studio 将在几分钟内构建它——他表示，这个过程通常需要开发人员几天时间。

Sivasubramanian 写道：“App Studio 的生成式 AI 驱动的助手消除了典型 [低代码工具](https://thenewstack.io/the-highs-and-lows-of-low-code-tools/) 的学习曲线，加速了应用程序创建过程，简化了设计 UI、构建工作流和测试应用程序等常见任务。”“每个应用程序都可以立即扩展到数千个用户，并且由 AWS 安全且完全管理，无需任何操作专业知识。”
此外，AWS 还将其 [Amazon Bedrock](https://thenewstack.io/amazon-bedrock-expands-palette-of-large-language-models/) 生成式 AI 框架扩展了更多功能，包括扩展开发人员可用于 [检索增强生成](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/) (RAG) 的数据源，其中已经包括文档存储库、数据库和 API。现在 AWS 正在为 [Salesforce](https://thenewstack.io/salesforce-gets-on-the-gpt-3-train-with-einsteingpt/)、Confluence 和 Microsoft SharePoint（处于预览阶段）添加连接器，为开发人员提供更广泛的业务数据选项来定制其 AI 模型。该公司还为 Amazon MemoryDB 添加了 [向量搜索](https://thenewstack.io/vector-databases-long-term-memory-for-artificial-intelligence/)，加入了 OpenSearch Service 和 OpenSearch Serverless、Aurora 以及 Amazon Relational Database Service 等其他 AWS 服务。

**走在正确的道路上**
TECHnalysis Research 首席分析师 [Bob O’Donnell](https://www.linkedin.com/in/bobodonnell/) 告诉 The New Stack，他对 AWS 声称 Amazon Q Apps 或 App Studio 可以根据提示中的几个命令立即启动应用程序表示怀疑——他怀疑任何云提供商的工具都无法做到这一点——但他表示，该公司正在朝着正确的方向发展，减少了开发人员或任何其他人构建云中 AI 应用程序所需的功能。
O’Donnell 表示，这两个工具的引入“在哲学和技术上都是一大步”，并补充说，确保公司中的每个人都能访问和使用正在生成和收集的大量数据将非常重要。

与 Enderle 一样，他表示，构建丰富的开发人员 AI 工具集对于 AWS 和所有其他云服务提供商来说都将非常重要。

“归根结底，每个云提供商在 AI 领域获得吸引力的关键是他们的应用程序开发工具，”O’Donnell 说。“这是他们需要的，因为 AI 的魔力只有在获得这些 AI 应用程序后才会发生。”

Enderle 补充说，“几乎所有 AI 应用程序都是基于云的，因此所有云提供商都专注于使他们为这些开发人员提供的服务尽可能有吸引力。AI 使用大量资源，因此它可以产生同样多的收入。”

**开发人员的激烈竞争**
AWS 在其所做的事情上并不独特。[Microsoft](https://thenewstack.io/microsoft-one-ups-google-with-copilot-stack-for-developers/)、[Google](https://cloud.google.com/?utm_content=inline+mention)、[Oracle](https://developer.oracle.com/?utm_content=inline+mention)、[IBM](https://thenewstack.io/ibm-anaconda-partner-to-embed-python-into-enterprise-ai/) 以及其他公司也都在积极扩展其开发人员服务组合，提供可以使各种人更快、更轻松地构建 AI 应用程序的工具。在 [5 月份的一篇博文中](https://azure.microsoft.com/en-us/blog/3-ways-microsoft-azure-ai-studio-helps-accelerate-the-ai-development-journey/)，Azure AI 总经理 [David Seda](https://www.linkedin.com/in/david-seda-4a9501128/) 指出，公司自己的 AI 应用程序的学习曲线很陡峭，[52% 的公司](https://news.microsoft.com/source/wp-content/uploads/2023/11/US51315823-IG-ADA.pdf) 指出，缺乏熟练的工人是实施和扩展 AI 的最大障碍。

“为了真正发挥生成式 AI 的价值，组织需要工具来简化 AI 开发，以便他们可以专注于解决业务需求的大局，”Seda 写道，并指出 Azure AI Studio——微软的生成式 AI 平台——“将您开始开发自己的 AI 应用程序所需模型、工具、服务和集成整合在一起。”

同月，Google Cloud 云 AI 和行业解决方案副总裁兼总经理 [Burak Gokturk](https://www.linkedin.com/in/burak-gokturk-8983792/) 吹嘘了其公司四年前的 [Vertex AI](https://thenewstack.io/an-introduction-to-google-vertex-ai-automl-training-and-inference/) 平台，称在过去一年中，“我们扩展了生成式 AI 的产品，为开发人员带来了任何超大规模提供商中最广泛的基础模型、强大的基础设施选项以及用于模型开发和 [MLOps](https://thenewstack.io/kitops-is-the-open-source-tool-that-turns-devops-pipelines-into-mlops-pipelines/) 的工具。”

**蓬勃发展的市场**
毫不奇怪，Gartner 在 4 月份的[云 AI 开发者服务魔力象限](https://www.gartner.com/doc/reprints?id=1-2HEDHS4Z&ct=240425&st=sb)中将 AWS、微软、谷歌和 IBM 列为市场领导者。这是一个快速增长的市场。NexusTrend Research 分析师本月表示，他们预计全球云 AI 开发者服务市场将从去年的 610 亿美元增长到[2031 年的 1089.6 亿美元](https://www.linkedin.com/pulse/global-cloud-ai-developer-services-market-size-pioneering-efo1c/)，年均增长率为 8.64%，并指出“在云 AI 开发者服务市场运营的公司正在迅速扩展其运营并增强其能力以满足这种不断增长的需求，为预测期内持续增长奠定了基础。”

根据 Synergy Research Group 的数据，生成式 AI 技术和服务的加速创新和采用也正在影响云基础设施服务领域。第一季度的全球支出[超过 760 亿美元](https://www.srgresearch.com/articles/huge-cloud-market-sees-a-strong-bounce-in-growth-rate-for-the-second-consecutive-quarter)，同比增长 21%。AWS 继续占据榜首，占市场份额的 31%，微软以 25% 位居第二，谷歌以 11% 位居第三，后两者同比增长率高于 AWS。

TECHnalysis 的 O’Donnell 表示，这三家公司都将继续推出面向开发者的 AI 服务，但没有一家公司能明显领先于其他公司。

“这将是一场马拉松，他们可能会互相超越，”他说。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。