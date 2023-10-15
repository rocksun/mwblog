<!-- 
# Docker在DockerCon上推出GenAI Stack和AI Assistant
https://cdn.thenewstack.io/media/2023/10/1863c7f4-docker-cto-1024x616.png
Docker CTO Justin Cormack/Photo by Loraine Lawson
 -->


译自 [Docker Launches GenAI Stack and AI Assistant at DockerCon](https://thenewstack.io/docker-launches-genai-stack-and-ai-assistant-at-dockercon/) 。

Docker 为开发者提供了两种利用 AI 的方式：一个是可以用来构建的生成式 AI 模块堆栈，另一个是可以帮助 Docker 部署的 AI 机器人助手。

Docker 在上周的 DockerCon大会上发布了两款新的人工智能解决方案：一个是生成式AI模块组件堆栈，可以帮助开发者开始创建自己的AI应用程序；另一个是Docker AI，旨在帮助开发者部署和优化Docker本身。

Docker CEO [Scott Johnston](https://www.linkedin.com/in/scottcjohnston/)表示，这是第一个为像Docker这样的产品本身提供AI能力的解决方案，而Docker平台本身经常被用来构建流行的AI工具，比如[Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/)和Replicate等。许多项目通过[Docker容器](https://thenewstack.io/monitor-control-and-debug-docker-containers-with-whaledeck/)公开接口给社区，并要求社区成员以[Docker容器镜像](https://thenewstack.io/find-vulnerabilities-in-container-images-with-docker-scan/)的形式向服务提交模型。 

Johnston对The New Stack表示："容器镜像是所谓的不可变的，这意味着结果是可复制的。当你进行建模、科学分析时，你希望能重复获得结果，不管是哪个同事在操作，也不管是什么情况。所以容器镜像的不变性对此真的很有帮助。"

他补充说，Docker多年来一直与上游社区合作，为[AI/ML](https://thenewstack.io/ai-ml-best-practices-during-a-gold-rush/)活动和应用提供可信任的镜像。

他说："随着对这类技术的兴趣增加，近几年我们看到相关镜像的下载量飙升。我们看到社区下载这些镜像，进行调整和优化，然后再打包成Docker容器共享给其他人，主要通过Docker Hub。"

Docker [Hub是Docker的公共镜像注册表服务](https://thenewstack.io/docker-hub-limits-what-they-are-and-how-to-route-around-them/)。目前该平台上已经有500多种AI相关镜像被共享，他补充说。

## 回答社区的问题

Johnston表示，Docker社区经常询问如何开始使用AI/ML技术。

Johnston说:"我们经常听开发者社区问:'我该如何开始?可以用哪些技术?这些技术安全吗?'"

在本周三的DockerCon大会主题演讲时，Docker通过发布[GenAI Stack](https://www.docker.com/blog/introducing-a-new-genai-stack/)来回答这个问题。GenAI Stack结合了来自Docker及合作伙伴[Neo4j](https://thenewstack.io/try-a-neo4j-graph-database-right-here-right-now/)、[LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/)和[Llama](https://thenewstack.io/metas-llama-2-is-not-open-source-and-thats-ok/)的技术和工具。这是一个预配置的解决方案，其中Llama提供[大语言模型](https://thenewstack.io/top-5-large-language-models-and-how-to-use-them-effectively/)，Neo4j提供[向量和图数据库](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/)，LangChain提供框架。

他说:"我们定义了一个GenAI Stack，它解决生成式AI中最常见的用例，将这些技术打包成Docker容器，然后在外面加上Docker Compose的编排。开发者不必到处搜罗代码和资源，也不需要自己拼装和配置。一切准备就绪，可以直接使用。"

开发者可以在5分钟内开始，看到工作的效果并进行迭代，他表示。

## 另一个增长型产品 

周三发布的第二个产品是Docker AI，这是一个生成式对话机器人，旨在帮助用户使用Docker。它通过训练Docker的Compose文件和Docker产品与工具中的错误代码库，Johnston说。没有涉及任何客户数据，他补充说。

虽然GitHub [Copilot](https://thenewstack.io/microsoft-one-ups-google-with-copilot-stack-for-developers/)等代码补全型AI解决了应用程序的10%到15%需求，但应用程序通常还需要数据库、Web服务器、前端和基础镜像等其他组件。

Johnston表示，Docker已经通过提供容器镜像和[Docker Compose文件](https://thenewstack.io/ansible-update-lets-docker-compose-files-configure-networks-infrastructure/)来定义应用程序源代码周围的这些其它组件，约占应用的剩余85-90%。因此，Docker AI可以视为补充代码补全型AI，通过解决剩余85-90%的需求实现互补。

他说："Docker已经提供容器镜像、Docker文件和Compose文件来定义应用源代码周围的其他组件。这为我们提供了一个绝佳的机会，用一个覆盖剩余85%需求的AI助手来增强像Copilot和Ghostwriter等代码补全型AI。"

该AI助手旨在融入开发者的工作流程，帮助他们解决可能打断工作流的问题或错误，他进一步表示。它可以集成到[Visual Studio Code](https://thenewstack.io/this-week-in-programming-visual-studio-code-arrives-on-the-web/)和[JetBrains](https://thenewstack.io/dedicated-ide-for-rust-released-by-jetbrains/)的IDE中。

他形容该助手“不应被视为替代人类，而更像是增强人类能力的机甲”。它可以帮助开发者保持流畅的工作状态，不断迭代和构建，而不必跳出去查找第三方资源。

该AI助手目前通过[Docker早期访问计划](https://www.docker.com/ai-early-access-program/)开放申请。
