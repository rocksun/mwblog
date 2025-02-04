# 使用机器学习容器简化AI开发

![使用机器学习容器简化AI开发的特色图片](https://cdn.thenewstack.io/media/2025/01/0f393dc3-getty-images-0w9_dz4sjdg-unsplashb-1024x576.jpg)

Replicate 的理念非常简单：使用[容器](https://thenewstack.io/containers/)技术在云端运行和共享机器学习模型。听起来熟悉吗？这可能是因为 Replicate 的创始人兼首席执行官之前是 Fig 的创建者，Fig 被[Docker 收购](https://thenewstack.io/docker-at-10-3-things-we-got-right-3-things-we-got-wrong/)，之后成为 Docker Compose。

[Replicate](https://replicate.com/) 是他和他的商业伙伴想要为[机器学习](https://thenewstack.io/how-machine-learning-works-an-overview/)创建类似技术的结果。

## 将容器引入AI

和首先创建了一个名为[Cog](https://cog.run/)的产品，他[将其描述为](https://replicate.com/blog/machine-learning-needs-better-tools)“机器学习的 Docker”。据介绍，Cog“使将机器学习模型打包到容器中变得容易，以便您可以共享它并将其部署到生产环境中”。此工具是开源的，但与许多开源其作品的开发者一样，和随后创建了一个云平台来将这项技术商业化，称为 Replicate。

根据其[文档](https://replicate.com/docs)，“Replicate 允许您使用云 API 运行 AI 模型，而无需了解机器学习或管理您自己的基础设施。”

Cog 本质上是对部署机器学习应用程序的技术方面的抽象。但与我上周介绍的用于 AI 应用程序的[无服务器平台 Modal](https://thenewstack.io/serverless-for-ai-devs-modals-python-and-rust-based-platform/) 类似，Replicate 主要租赁运行这些模型所需的计算资源。

去年在[Latent Space 播客](https://www.latent.space/p/replicate)上解释说：“我们不拥有自己的 GPU。”“我们有一些用于测试的 GPU，但不用于生产工作负载。我们主要构建在公共云上，主要是 GCP 和 CoreWeave，以及其他一些零星的云平台。”

## 帮助开发者试用 LLMs

Replicate 的一个关键在于它允许开发者定制、微调和试用开源 LLM 模型。正如在播客中提到的那样，“开源的重点在于您可以对其进行修改、定制、微调，并将其与其他模型结合使用。”

当 Meta 发布其[开源 Llama 模型](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/)时，Replicate 真正地发展壮大，因为这当然允许开发者比使用 OpenAI 和[Google](https://cloud.google.com/?utm_content=inline+mention) 等公司的 API 进行更多的尝试。“Llama 2 作为基础模型的美妙之处在于……您可以用 50 美元对其进行微调，”说。“这就是开源生态系统如此美妙的地方。”

就在本周，开源 LLM 生态系统又获得了新的动力，中国公司 DeepSeek 突然出现，[声称已经构建](https://www.theverge.com/24353060/deepseek-ai-china-nvidia-openai)了一个推理 LLM（称为 R1），其能力与 OpenAI 最强大的模型 o1 相当。这一说法仍在受到开发者和媒体的检验，但无论如何，这对开发者来说无疑是个好消息——用户可以使用的开源模型越多越好！

“只需开始尝试使用它，感受一下语言模型的工作方式，感受一下这些扩散模型的工作方式，感受一下微调是什么以及它是如何工作的……”

– Replicate 首席执行官

从开发者的角度来看，像 Replicate 和 Modal 这样的平台是一个福音，因为它们使在应用程序中使用机器学习技术成为可能。在 Latent Space 播客中，将其比作 20 世纪 90 年代开发者接触 web 开发平台时的场景。

“如果您不想深入到[PyTorch](https://thenewstack.io/why-pytorch-gets-all-the-love/) 层级，您就不需要这样做——就像 90 年代的软件工程师不需要了解网络堆栈的工作原理就能构建网站一样。但您需要了解这个东西的形状。”

他敦促开发者学习现代 AI，因为它在应用程序开发领域变得越来越重要。
“动手试试，感受一下语言模型的工作原理，感受一下这些扩散模型的工作原理，了解一下微调是什么以及它是如何工作的——因为你的一些工作可能就是构建数据集。感受一下提示词的工作原理，因为你的一些工作可能就是编写提示词。这些都是非常重要的技能。”


## AI模型的泛滥
去年十一月，在与他的投资者之一A16Z的采访中，[Firshman表示](https://a16z.com/podcast/building-developers-tools-from-docker-to-diffusion-models/)Replicate生态系统中大约有20,000个模型。[这些模型包括](https://replicate.com/explore)生成或增强图像和视频的模型、转录模型、用于聊天或音乐的模型、帮助你“制作3D内容”的模型等等。截至撰写本文时，最受欢迎的模型是[SDXL-Lightning](https://replicate.com/bytedance/sdxl-lightning-4step)，拥有7.269亿次“运行”，由TikTok母公司字节跳动开发，被描述为“一个快速的文本到图像模型，可在4个步骤中生成高质量图像”。

Firshman还在[与Assembly AI的采访中](https://www.assemblyai.com/assembly-required/assemblyai-replicate)表示，“我们主要为初创公司构建”。

他澄清道：“当我们说初创公司时，既包括真正的初创公司，也包括大型公司内部像初创公司一样运作的小团队。这些团队在构建方面取得了很大的成功，例如，构建完全基于AI的完整产品，或者构建产品内部某些特定问题的特定解决方案。”

他补充说，Replicate的一些客户正在使用它来微调语言模型，但这并不是主要用例。


## AI民主化：开源模型为何重要
Replicate和Modal都是这类新型平台的良好示例，这类平台为开发者提供了价值：通过抽象化机器学习技术的许多复杂性，使将AI集成到应用程序中变得更容易。

你也可以认为Replicate正在帮助实现对开源LLM模型的访问民主化，使开发人员能够自定义和/或微调模型，例如Meta的[Llama 3](https://thenewstack.io/llama-3-how-metas-new-open-llm-compares-to-llama-1-and-2/)（最新的Llama版本）——甚至可以尝试使用DeepSeek的R1等尖端模型。

虽然这仍然是发展初期——鉴于OpenAI和其他行业巨头仍然将其最强大的模型作为专有模型——但像Replicate这样的平台展示了开源如何在AI工程生态系统中蓬勃发展。开放并可供爱好者使用的模型越多，对开发人员就越好。

[YOUTUBE.COM/THENEWSTACK 科技发展日新月异，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)