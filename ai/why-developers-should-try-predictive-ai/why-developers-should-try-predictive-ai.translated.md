# 为什么开发者应该尝试预测性AI
![Featued image for: 为什么开发者应该尝试预测性AI](https://cdn.thenewstack.io/media/2024/11/3444767d-ai_motherboard-1024x630.jpg)
每个人都在尝试使用[生成式人工智能 (Gen AI)](https://thenewstack.io/gen-ais-iphone-moment-what-it-means-for-developers/)，但根据Cloudflare开发者平台和AI产品副总裁的说法，开发者应该考虑将其他形式的机器学习整合到他们的应用程序中。

“每个人都在尝试，我认为这给人一种感觉，即在生产中，在真正重要的用例中，发生的事情比实际情况要多，”Kozlov说。“我们看到的是，许多聊天机器人正被推到用户体验的前沿。”

## AI聊天机器人的替代方案
她补充说，这未必是正确的方法。仅仅为了使用生成式AI而推出[聊天机器人](https://thenewstack.io/ai-beyond-chatbots-and-assistants-adaptive-applications/)，可能会让公司看起来像是“只是在勾选AI复选框”，而没有考虑它是否真的对用户有帮助。

她建议，预测性AI是开发者应该探索的另一个选择。预测性AI使用[机器学习算法](https://thenewstack.io/machine-learning-algorithm-sidesteps-the-scientific-method/)来识别过去事件中的模式，并对未来事件进行预测。它用于欺诈检测、信用风险评估、需求预测，甚至疾病诊断等任务。

例如，一个日历[应用程序可以使用机器学习](https://thenewstack.io/create-machine-learning-apps-in-your-notebook-with-tecton/)来帮助用户找到可用的预约时间。

“你不需要为此依赖生成式AI，”Kozlov说，并补充道，“显然，有很多用例表明生成式AI对当今的人们非常有用。”

预测性AI依赖于[推理AI](https://thenewstack.io/when-cloud-meets-intelligence-inference-ai-as-a-service/)，这是使用训练好的模型对新数据生成预测的特定行为。她说，运行推理AI实际上需要的资源比运行训练工作负载要少。

Cloudflare的[Workers AI](https://developers.cloudflare.com/workers-ai/)管理后端，并通过API为开发者提供无服务器AI推理访问权限。她补充说，该平台还提供[各种开源模型的访问权限](https://developers.cloudflare.com/workers-ai/models/)。

## 更广泛地采用小型模型
Kozlov注意到的另一个趋势是，组织应该部署在较少参数上训练的小型模型，而不是利用最大的模型。

“人们意识到，好的，有一些模型有4000亿个参数，但你实际上无法运行它们。它们太贵了，”她说。“我们也看到一种向小型模型回归的转变。”

开发人员发现，使用仅提供少量模型的流行GenAI提供商提供的[AI的API](https://thenewstack.io/the-future-of-apis-lessons-in-security-composability-ai/)非常容易。

“人们意识到，好的，有一些模型有4000亿个参数，但你实际上无法运行它们。它们太贵了。”

– Cloudflare产品副总裁说

当开发者想要部署某些开源大型语言模型或内部训练的模型时，情况就会变得棘手。然后，他们需要为基础设施配置虚拟机。

“如果你想利用一些非常棒的开源模型，或者是你自己训练的模型……你又回到了必须配置虚拟机，并真正考虑我将获得的峰值容量是什么，或者我将获得的峰值负载是什么，并围绕该峰值负载配置容量。”

她说，大多数工作负载并非一直以100%的速率运行——这非常罕见。这意味着开发人员在配置方面做了很多猜测工作，并且为不需要支付的资源支付了过多的费用。

“你正在减慢自己的速度，因为你必须考虑所有这些事情并进行管理，并设置负载平衡、路由等等，而不是做最初促使你使用AI的事情，那就是你想尽快进入市场，并通过将AI集成到你的应用程序中获得竞争优势，”她说。

## Cloudflare对预测性AI的使用
Kozlov说，Cloudflare一直在使用预测性AI来识别真实的攻击与网络流量的合法峰值。
她说：“我们意识到，我们可以利用我们已经构建的用于保护和加速应用程序的相同网络，并使用该网络为开发人员提供服务，以便他们直接在其之上构建应用程序。”

除了连接到推理 AI 的 API 外，基于云的 Web 平台还为开发人员提供：

* [Vectorize](https://developers.cloudflare.com/vectorize/)，其向量数据库，允许开发人员将自己的内存/特定领域信息带入模型；
* [Retrieval Augmented Generation 支持](https://developers.cloudflare.com/workers-ai/tutorials/build-a-retrieval-augmented-generation-ai/)，可用于根据领域知识微调模型；以及一个
* [AI 网关](https://developers.cloudflare.com/ai-gateway/)，有助于监控运行各种 AI 模型的成本。

她说：“AI 网关可以帮助你监控所有这些内容并进行实验，但它能够让你获取和比较结果，真正缩小对你特定工作负载而言重要的方面，无论是成本、性能还是准确性，并查看用户获得的响应。”

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。