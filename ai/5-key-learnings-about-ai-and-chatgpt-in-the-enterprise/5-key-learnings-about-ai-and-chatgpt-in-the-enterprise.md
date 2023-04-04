# 企业中关于 AI 和 ChatGPT 的 5 项重要学习

翻译自 [5 Key Learnings about AI and ChatGPT in the Enterprise](https://thenewstack.io/5-key-learnings-about-ai-and-chatgpt-in-the-enterprise/) .

2023 年是人工智能在企业中取得突破的一年。但在您的 CIO 专注于 ChatGPT 之前，需要了解以下五件事。

![](https://cdn.thenewstack.io/media/2023/04/3ae1b7b2-enterpriseai-1024x683.jpg)

如果说 2022 年是人工智能突破成为改变社会的技术的一年，那么 2023 年就是人工智能在企业领域突破的一年。可以这样说：生成式人工智能和大型语言模型已经成为全球 IT 部门中常见的词汇。你们公司的首席信息官现在更可能提到 ChatGPT 而不是 Kubernetes 。

AI 在企业领域已经取得了巨大进展，以下是我们迄今为止学到的五件事情。

## 1. ChatGPT 不是企业的唯一选择

3 月，OpenAI 宣布推出了 ChatGPT 的企业版。但在这种情况下，OpenAI 是一个快速的追随者而不是市场上的第一家。我发现当时已经有一家名为 Cohere 的多伦多公司与谷歌有密切联系，并向企业销售生成式人工智能。

Cohere 的首席执行官 Martin Kon 告诉我们：“我们正在与组织中的开发人员、AI/ML 团队合作，将这些功能引入他们的组织。”他补充说，其方法基本上与 OpenAI 不同。“OpenAI 希望您将数据带到其专属于 Azure 的模型中。Cohere 希望将我们的模型带到您感觉舒适的任何环境中。”

到目前为止，公司主要使用生成式 AI 为自己私有数据创建语义搜索引擎——无论是用于内部使用还是外部客户。相关用例是知识管理（KM）。想象一下员工能够与受过大量基于公司数据训练过的语言模型训练过的 AI 进行对话。

试图以聊天机器人形式实现 KM 的众多新 AI 公司之一是 Vectara。其首席执行官 Amr Awadallah 告诉我，“在五年内，每个应用程序——无论是在消费者端还是在商业/企业端——都将以更加人性化的方式重新架构，以表达我们试图实现和要做什么。

## 2. 大型科技平台正在推动低代码工具

上个月，谷歌云和谷歌的 Workspace 部门宣布了一系列新的人工智能功能。其中包括生成式 AI 应用程序构建器，“允许组织构建自己的基于 AI 的聊天界面和数字助手”，以及 Google Workspace 中的新生成式 AI 功能。

谷歌为由生成式 AI 提供支持的应用程序创造了一个通常很别扭的术语：“gen apps”。它声称 gen apps 将成为继 Web 应用程序和移动应用程序之后第三大互联网应用类别。

我愿意打赌，作为一个术语，gen apps 永远不会流行起来，但无论如何，在企业公司中将广泛使用谷歌提供的基于人工智能的工具。

同样地，微软也在发布新的人工智能工具，例如 Semantic Kernel（SK），被描述为“帮助开发者快速轻松地将尖端人工智能模型集成到他们的应用程序中”的开源项目。SK 在很多方面都是经典微软低代码工具，只是它专注于帮助用户对 AI 聊天机器人进行“提示”。

## 3. LLM 的规模差异很大，但规模不是一切

如果你浏览[斯坦福大学的 HELM 网站](https://crfm.stanford.edu/helm/latest/?models=1)，该网站以多种方式衡量 LLMs ，你会发现这些模型的大小差异很大。简单来说，模型大小和其工作速度之间存在权衡。

OpenAI 有几个模型，从13亿参数（其 Babbage 模型）到1750亿参数（其 DaVinci 模型）不等。

Cohere 甚至将其[模型大小](https://docs.cohere.ai/changelog/new-improved-generation-and-representation-models)区分为星巴克杯子一样：小、中、大和超大。

![Cohere 模型](https://cdn.thenewstack.io/media/2023/03/ddf94146-cohere_models_3mar23.jpg)
*Stanford HELM目录中 Cohere 的模型列表*

![OpenAI 模型](https://cdn.thenewstack.io/media/2023/03/01d5735e-openai_models_3mar23.jpg)
*OpenAI 的主要模型*

然而，斯坦福还测试了“[准确性](https://crfm.stanford.edu/helm/v0.2.0/?group=core_scenarios)”，在这些统计数据中，尺寸似乎并不重要：

![HELM 准确性](https://cdn.thenewstack.io/media/2023/03/e67b1f4a-stanford_helm_accuracy_3mar2023.jpg)
*斯坦福 HEML 测试 ML 模型的准确性*

## 4. 像 Ray 这样的工具正在帮助扩展 AI

在这个新时代的生成式 AI 中，像 Ray 这样的框架现在与 Kubernetes 一样重要，可以创建现代化大规模应用程序。一个名为 Ray 的开源平台提供了分布式机器学习框架。它被 OpenAI 和 Cohere 用于训练他们的模型，并且也被其他高度规模化的产品使用，例如 Uber 。

Ray 背后的公司是 Anyscale，其首席执行官 Robert Nishihara 今年早些时候告诉我，该公司非常以开发人员为中心。他说，Ray 的所有功能都设计成易于开发人员使用。这与 Kubernetes 面向开发人员的用户体验不同，后者以难以处理而著称。Ray 是为 Python 开发人员设计的，Python 是人工智能系统中使用的主要编程语言。

Anyscale 联合创始人 Ion Stoica 告诉我，Ray “就像 Python 的扩展”，并且与 Python 一样，有一组针对不同用例的 Ray 库。名称笨拙的 RLlib 用于强化学习，但也有类似的库用于训练、服务、数据预处理等。

## 5. 商业智能在人工智能时代被重塑

正如云计算引入了一系列“大数据”解决方案，生成式人工智能是新一波数据智能公司的催化剂。

我最近与 Alation 的联合创始人 Aaron Kalb 进行了交谈，Alation 将自己定位为“数据智能”平台，并推广一种称为“数据目录”的概念。这将“机器学习与人工管理”相结合，为企业创建自定义数据存储。

Kalb 指出，无论是 AI 还是常见的企业缩写 BI（商业情报），都是“垃圾进去、垃圾出来”。他说，数据智能是“在 AI 和 BI 之前的一层，它确保您可以找到、理解和信任正确的数据，以将其放入您的 AI 和 BI 中。”

他说，在这种情况下，从公共互联网上获取诸如 ChatGPT 之类的东西并将其引入企业是非常冒险的。他认为，在企业内部的人工智能系统使用数据之前，数据需要变得更加智能。此外，他认为企业不需要 ChatGPT 和类似系统的“互联网规模”。他解释说，每个组织都有自己的术语——可能是行业术语，也可能是该公司特有的术语。

## 总结：人工智能企业已经到来

很难相信生成式 AI 才刚出现一年。这一切始于 OpenAI 的 DALL-E 2，该服务在去年 4 月份宣布推出，并在 7 月份作为私有测试版发布。DALL-E 2 是一个由深度学习模型驱动的图像生成服务，对整个行业来说是一个重要的进步。同样在去年 7 月，Midjourney 公司发布了其同名文本到图像生成器。

然而真正引起人们关注的是8月份 Stable Diffusion 的发布——另一个基于深度学习技术实现文本到图像转换的系统。与 DALL-E 2 和 Midjourney 不同，Stable Diffusion 采用了开放许可证结构。此时人们开始更加关注所有这些服务背后所使用的模型——LLMs（语言模型） 。DALL-E 2 使用了 GPT-3 的一个版本，这是 OpenAI 当时的主要 LLM。

但是，事后看来，我们可以看到图像生成器只是开胃菜。 11 月底，OpenAI 推出了 ChatGPT，这是一个建立在 GPT-3.5 之上的聊天机器人。这是生成式人工智能进入企业的催化剂，从那时起它迅速接管了 IT 部门。

