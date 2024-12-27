# AI、硬件和开放模型：走向Linux之路

![AI、硬件和开放模型：走向Linux之路的特色图片](https://cdn.thenewstack.io/media/2024/09/38d69a92-does-your-open-source-project-need-foundation-oversight-2-1024x576.jpg)

从20世纪60年代开始，IBM的大型机系统开启了专有硬件和软件的时代，这一趋势延续到了PC时代。在20世纪90年代初，Linux打破了这种垄断，成为一种开源替代方案，为那些厌倦了专有操作系统和硬件的人们提供了选择。

AI市场正在走同样的道路，但环境有所不同。兴起的开放AI模型正在撼动AI市场，打破了专有模型在专有硬件上运行的垄断地位。

包括谷歌和亚马逊在内的云提供商正争先恐后地将开放模型部署到其专有芯片上。这是因为AI模型的消费者希望获得与开放AI大型语言模型相关的更低成本和更高的灵活性。这一趋势与Linux发展壮大并最终运行大部分互联网的方式相符。

“如果你想跑得快，就独自一人；如果你想跑得远，就一起同行，”AI硬件公司Axelera的首席执行官说。

## 我们是如何走到这一步的？

AI时代伊始与PC时代非常相似，专有的Windows软件只能在x86硬件上运行。

Linux的兴起是由x86驱动的，“正是Linux加上x86才成为了web栈/LAMP栈，”AI基准测试组织MLCommons的创始人说。

“现实情况是，Linux已经真正取代了专有的Unix系统。Solaris消失了；HP-UX消失了；Tru64肯定消失了；AIX还在，”说。

像Meta的Llama和谷歌的Gemma这样的开放模型，也正在打破专有模型（如谷歌的Gemini和OpenAI的GPT-4）在企业AI领域的主导地位。

谷歌的TPU AI芯片以前只运行其专有的Gemini大型语言模型，但该公司今年早些时候在其芯片上部署了其自主研发的Gemma开放模型。

亚马逊在re:Invent大会上在其自主研发的Trainium2芯片上提供了拥有4050亿参数的Meta Llama 3.1模型。

“Trainium2比同类Nvidia实例更便宜，因此使用Llama2 405B并针对客户专有数据对其进行训练以创建自定义模型是一种经济实惠的方法，”TechInsights的分析师说。

## 什么是开放模型？

可以肯定的是，开放模型和开源AI模型并不相同。在软件领域，您可以随意修改开源代码。对AI中“开放”的含义有多种定义。

开源倡议组织两个月前[定义了开源AI](https://thenewstack.io/the-open-source-ai-definition-is-out/)，将其定义为“应用于系统、模型、权重和参数或其他结构元素”。这包括所有训练数据。

Meta的Llama不符合OSI的定义，但它大部分是开放的，但也有一些限制。用户可以使用Llama作为预训练模型，并根据特定需求对其进行微调。但用户无法访问或修改Llama的预训练数据，因为Meta不想透露其用于预训练模型的数据来源。

像Gemini、Claude和GPT-4这样的专有模型是完全封闭的。

## 像Linux一样，锁定客户

云提供商正在效仿Red Hat等Linux操作系统提供商——将开源操作系统与专有技术结合起来，并将客户锁定在其软件栈中。

开放AI模型是吸引客户使用云服务的低成本方式。一旦客户被锁定到某个云服务提供商，就很难离开。

“其动机是让更多客户使用其围绕AI的服务，例如计算、数据管理、安全和存储，”Moor Insights and Strategy的首席分析师说。

AWS的Trainium2并没有风靡全球，因此将Llama移植到Trainium2为其芯片带来了更多价值。在re:Invent大会上，AWS还宣布了其自主研发的Nova模型，该模型将在Trainium上运行。

AWS希望广泛覆盖用例，Databricks人工智能副总裁说。在2023年，他以13亿美元的价格将其公司MosaicML出售给了Databricks。

“支持更多模型会提高硬件的相关性，这可能是主要原因。而且对他们来说，这并不是一个巨大的挑战，”说。

## 开放的优势

开源和开放模型有利于云专用AI加速器。

“理想状态是在更低的成本下提供熟悉且摩擦最小的环境，”说。

开放模型还允许创建开放源模型的衍生产品，这些衍生产品更小、更优化，可以更好地满足行业特定需求。
“将开放模型添加到目录中，可以帮助他们扩大客户群并实现服务的货币化，”Del Maffeo 说。

Groq、Sambanova、Cerebras以及其他小型硬件提供商也正在以非常低的token成本提供开放模型即服务。

## 开放AI模型的Linus
将开放AI模型加载到谷歌的TPU和AWS的Trainium上可能会非常困难。开放模型需要针对定制芯片的专用分支。

开放模型通常构建在PyTorch、JAX或TensorFlow等框架和工具链上。开发人员使用框架的内置工具和API来衡量性能，并使用包括针对架构和芯片进行优化的技术来修复它。

相比之下，英伟达的GPU是通用的AI加速器，可以运行任何PC或AI应用程序。

Hugging Face正在推动专有硬件上的开源AI发展。它提供了数百个开放模型，这些模型已被证明具有与更耗电的模型相似的准确性和性能。

AWS正在与Hugging Face [合作](https://aws.amazon.com/ai/hugging-face/)，在Trainium上训练和部署模型。

“现在市场正在加速发展，很自然地会看到亚马逊将其基础设施上的访问权限开放给任何其他开源模型，”Del Maffeo说。

Hugging Face在7月份宣布，AI模型可在Google Cloud TPU上[部署](https://huggingface.co/blog/tpu-inference-endpoints-spaces)。

“随着人们越来越关注大型模型日益增长的功耗、冷却需求和训练成本，来自社区的有助于减轻这些挑战的创新受到欢迎，”Del Maffeo说。

越来越多的开发人员也正在获得机器学习开发经验，并且社区的能力可以满足很大一部分AI市场的需求。

## 变化的定义
企业已经使用混合的开放和闭源模型。

“目前，所有模型的架构基本相同，”Rao说。

他表示，从硬件的角度来看，开放模型和闭源模型之间的区别更多地在于数据和训练方案，而不是模型的架构。

“你可以说，所有在硬件上运行的模型都是开源的，或者说是开源架构的衍生品。随着[GPT-4o1](https://openai.com/index/introducing-openai-o1-preview/)这样的推理时间缩放理念的出现，未来这种情况可能会发生变化，”Rao说。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)