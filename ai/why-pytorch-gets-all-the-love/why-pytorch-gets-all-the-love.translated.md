# PyTorch为何如此受欢迎

![PyTorch为何如此受欢迎的特色图片](https://cdn.thenewstack.io/media/2024/11/5aae1c0e-pytorch-love-1024x684.jpg)

自2016年从研究社区兴起并在数据科学领域占据一席之地以来，PyTorch 的发展呈指数级增长。根据GitHub数据，PyTorch在GitHub上的星标数量在2017年至2018年间增长了388%。尽管从2022年到2023年的增长稳定在约17%，并且TensorFlow仍然是顶级深度学习框架，[市场份额接近39%](https://6sense.com/tech/data-science-machine-learning/tensorflow-market-share)（根据6Sense的数据），而PyTorch为24%，[但PyTorch的势头正盛](https://survey.stackoverflow.co/2024/technology#1-other-frameworks-and-libraries)。

[Python编程语言的蓬勃发展](https://thenewstack.io/25000-python-devs-surveyed-on-tools-ides-and-python-2/)是这个[开源深度学习框架](https://thenewstack.io/genai-wont-replace-open-source-says-aws-exec/)成功的一个因素。但现在，生成式AI的增长使PyTorch成为数千名开发者的首选。它相对易于使用，并且性能很高。

那么，PyTorch的故事是什么？它为什么如此迅速地普及？它现在面临哪些权衡？

## PyTorch之前

[PyTorch诞生于](https://thenewstack.io/official-pytorch-documentary-revisits-its-past-and-its-future/)2016年，源自Facebook人工智能研究实验室(FAIR)，是对在[Torch](http://torch.ch/)中开发的概念的重新实现，Torch始于2002年，是瑞士Idiap研究所的一个机器学习(ML)和科学计算项目。最初是用[Lua](https://thenewstack.io/how-roblox-makes-programming-beginner-friendly-with-luau/)编写的，Torch后来采用了[LuaJIT](https://luajit.org/)，这是一种针对Lua编程语言的追踪式即时编译器，有助于提高性能。

Torch的开发者做了很多工作来使框架更易于使用。他们构建它以支持GPU加速。他们选择了Lua，这是一种相对容易学习的编程语言。Torch神经网络库因其易用性而获得了很高的评价。

根据[Torch网站](http://torch.ch/#why-torch)的说法，社区构建了用于机器学习、计算机视觉、信号处理、并行处理、多媒体（图像、视频、音频）和网络等的包。Torch开发了“易于使用的神经网络和优化库，同时在实现复杂的神经网络拓扑结构方面具有最大的灵活性”。开发人员可以构建“任意神经网络图并在CPU和GPU上对其进行并行化”。

总而言之，Torch社区拥有一个赢家。但是Lua？是的，它很棒，但其他趋势正在兴起。

## 早期

2017年，领导Torch 7的[Soumith Chintala]收到来自[Adam Paszke]的询问，后者是一位计算机科学家，当时是波兰的一名大学生，他自愿用Python替换Torch中的Lua。

但为什么？

根据[Stack Overflow](https://stackoverflow.blog/2017/09/06/incredible-growth-python/)的数据，Python发展势头强劲，同比增长27%。在之前的五年里，它的社区发展速度超过了几乎所有其他编程语言，包括Swift、Rust和Go。

2017年，PyTorch发布了0.2版本的API，直到今天，API的基础仍然基本相同。Chintala被认为是PyTorch的共同创造者，现在是Meta的“AI修复者”，Paszke在谷歌工作。

“[他们设计的东西真的很棒，”[Luca Antiga]在一次采访中说。“他们从[Chainer](https://stackshare.io/stackups/chainer-vs-pytorch)（一个在日本开发的框架）那里获得了一些灵感。然后当[PyTorch]出现时，我开始作为外部贡献者参与其中，其他人也加入了。是的，那是一段美好的时光。”

是什么让PyTorch独一无二？当然是易用性，但PyTorch的优势在于它的张量、梯度特性和动态图，James Birkenau去年在[TensorScience](https://www.tensorscience.com/posts/a-short-introduction-to-pytorch-in-python-2023.html)上写道。他说，理解PyTorch及其生态系统始于熟悉张量。“本质上，张量是多维数组——PyTorch中数据的构建块。它们类似于NumPy数组，但具有能够在GPU上运行的超能力，”他写道。

但是什么是动态图？本质上，它允许开发人员动态地构建图，特别是它增强了PyTorch对易用性的关注。

正如DevLearningDaily团队在一篇[比较TensorFlow和PyTorch的文章](https://learningdaily.dev/pytorch-vs-tensorflow-the-key-differences-that-you-should-know-534184a22f90)中所写：
“PyTorch计算图的动态特性在模型开发和调试过程中非常有利，因为我们可以在运行时打印、修改或分析计算图。”

写道，下一步是理解[Autograd](https://pytorch.org/tutorials/beginner/introyt/autogradyt_tutorial.html)，这是PyTorch用于管理微分的模块。描述Autograd为“计算图[它]具体化了张量上的操作是如何连接的。它就像一张蓝图，展示了数据如何流动以及如何通过不同的操作进行转换，直到我们得到输出。”

## Define-by-Run的突破
在PyTorch之前，架构师经常使用特定领域的语言来构建深度学习框架。但这会产生问题。某些东西可能会中断，研究人员必须一层一层地检查堆栈中的C++回溯以理解问题。如果例如错误出现在架构师编写代码很久之后，情况可能会变得复杂。

Chainer引入了[define-by-run原则的核心概念](https://pytorch.org/blog/pytorch-adds-new-tools-and-libraries-welcomes-preferred-networks-to-its-community/)来加快其开发速度。在其文档中，Chainer将define-by-run描述为一种方案，其中“网络是通过实际的前向计算动态定义的。更准确地说，Chainer存储计算的历史记录而不是编程逻辑。”

这是一个有趣的界限。当框架出现时，研究人员使用编程逻辑来构建图。PyTorch开始使用计算，动态构建图。使用计算，研究人员内置了自动微分，这意味着，正如Chainer解释的那样，他们可以向后遍历存储的操作。

内部结构随着时间的推移而改变。然而，说，人体工程学和对开发人员效率的关注仍然是PyTorch的核心。

动态图使PyTorch易于调试。以前，研究人员会构建一个图并开始调试——这是一个查找错误的重要任务。使用define-by-run原则，研究人员可以编写一行代码，并在执行时准确地知道哪一行代码出错。PyTorch变得自然易于调试和使用，允许更大的冒险而无需大量的时间投入。

## PyTorch生态系统
到2019年，PyTorch生态系统开始快速发展。当时由[Meta](https://about.meta.com/?utm_content=inline+mention)（当时的Facebook）管理，PyTorch尚未在Linux基金会的保护伞下，[2022年开始由其管理](https://thenewstack.io/pytorch-takes-ai-ml-back-to-its-research-open-source-roots/)。生态系统的增长意味着即使像Meta这样的大公司也需要将开源项目从其内部转移到开源组织手中。

而这个生态系统是巨大的：今天，PyTorch核心项目在GitHub上拥有近84,000颗星。它由核心项目、官方库（如Torchvision）以及基于PyTorch构建的流行技术（如PyTorch Lightning和Hugging Face）组成，这些技术允许开发人员训练和构建他们的模型。它还包括数千个社区库和工具。除了Meta之外，PyTorch基金会的理事会还包括[AWS](https://aws.amazon.com/?utm_content=inline+mention)、[AMD](https://www.amd.com/en/products/processors/server/epyc/google-cloud.html?utm_content=inline+mention)、[Arm](https://www.arm.com/campaigns/multi-arch-cloud-infrastructure?utm_content=inline+mention)、[Google](https://cloud.google.com/?utm_content=inline+mention)、[华为](https://www.huawei.com/en/)、[Hugging Face](https://huggingface.co/)、[英特尔](https://www.intel.com/content/www/us/en/now/data-centric/overview.html?utm_content=inline+mention)、[IBM](https://www.ibm.com?utm_content=inline+mention)、Lightning AI、[微软](https://news.microsoft.com/?utm_content=inline+mention) Azure和[英伟达](https://www.nvidia.com/en-us/)。

正如AWS开发人员体验副总裁[Adam Seligman](https://www.linkedin.com/in/adamseligman/)在9月份[2024 PyTorch大会](https://events.linuxfoundation.org/pytorch-conference/)上的一次采访中所说，“PyTorch非常令人兴奋。在Meta和更广泛的社区的支持下，它实现了令人惊叹的模型、AI和研究创新。”

[AWS参与PyTorch](https://aws.amazon.com/pytorch/)大约是在2018年或2019年，AWS生成式AI首席专家[Trevor Harvey](https://www.linkedin.com/in/trevorharvey1/)说。Harvey还作为AWS的[Brian Granger](https://www.linkedin.com/in/brian-granger-b9998662/)的替补成员担任[PyTorch理事会](https://pytorch.org/governing-board)成员。AWS希望其客户能够选择框架，而PyTorch已开始在研究界流行起来。这种流行程度是未来客户采用率的一个领先指标。Harvey说：
我们知道会有很多新的开发者和研究人员第一次接触机器学习，而PyTorch使得交互式学习和工作变得容易。这与我们在AWS的目标相呼应，即帮助普及机器学习，并使其能够被任何想要利用它的人所访问。

生态系统的大部分增长都来自于技术人员的工作，例如，在纽约大学攻读博士学位期间，看到一个机会可以使研究工作更容易更高效，并开发了PyTorch Lightning。Lightning使用户更容易进行大规模训练并更快地迭代。开发者不必担心许多细节，例如记录指标、记录指标和用于数据加载的分布式采样。它节省了时间，因为开发者不需要知道幕后运行的是什么。

Lightning AI的Antiga说：“我们并没有粉饰PyTorch，我们只是为用户代码添加了更多结构，以便我们可以处理某些方面，例如如何使其分布式，以及如何在不更改代码的情况下在不同的加速器上运行。”


## 社区发展壮大

2021年，[某人]写道，易用性是PyTorch深度学习框架的核心价值，并促进了其发展。他写道：

“这种观点在吸引人们参与方面非常有用。随着时间的推移，PyTorch整合了Caffe2和Chainer社区，并与JAX和Swift4TF保持友好关系。吸引其他人参与具有巨大的优势。社区越来越大，你可能会获得更广泛的视角，使项目随着时间的推移变得更好、更广泛。”

Chainer是一个灵活的神经网络开发框架，于2019年与PyTorch合并。它提供了一种简化的利用GPU的方法。JAX仍然作为PyTorch的替代方案存在，但开发者表示PyTorch更容易使用，并且拥有更强大的社区。Google于2022年存档了Swift for TensorFlow (Swift4TF)。

Caffe2和Chainer帮助拓宽了社区。2018年，Meta（当时的Facebook）管理着Caffe2，这是一个由在伯克利创建的深度学习框架。[某人]是Lepton AI的创始人，他帮助构建了Facebook的AI基础设施，后来又为云提供商阿里巴巴构建了AI和数据分析平台。


## PyTorch在2024年及以后

如今，PyTorch是最流行的深度学习框架之一。Meta PyTorch分析负责人[某人]，在9月的PyTorch大会上概述了该框架的增长情况。Li表示，在过去12个月中，开发者使用PyTorch创建了超过140,000个GitHub存储库，对PyTorch核心存储库进行了超过13,000次提交，并且有超过1,000名新的贡献者。

PyTorch 2.0于2023年3月发布，2.5于2024年10月发布。近几个月添加到PyTorch的功能显示了它自早期以来取得的进步：

- 2024年4月，社区添加了ExecuTorch Alpha，它将大型语言模型（LLM）和大型机器学习模型部署到边缘，稳定了API表面并改进了其安装过程。
- 社区在7月推出了TorchChat，它展示了如何在笔记本电脑、台式机和移动设备上运行Llama 3、3.1和其他LLM，重点是无缝性和性能。
- 8月，添加了FlexAttention，允许用几行惯用的PyTorch代码实现变体。
- 社区在9月添加了TorchAO。它对推理和训练的权重、梯度、优化器和激活进行量化和稀疏化。

在一次采访中，Meta的PyTorch维护者说，最新的PyTorch 2.5版本有来自504位贡献者的4,095次提交。


### 介绍编译模式和急切模式

PyTorch 2.0之后最近的开发表明生成式AI如何影响其发展。开发者希望有更有效的方法来调试模型并将其投入生产。急切模式是执行代码的默认方式。编译模式可以提供额外的提升。根据PyTorch文档，它“通过将PyTorch代码即时编译成优化的内核来加快PyTorch代码的运行速度，同时只需要最少的代码更改。”Antiga说，编译器一直是PyTorch 2.0之后开发的重点。
AWS一位首席工程师在九月份的PyTorch大会上发言，也肯定了这两种开发模式。AWS的客户既有开发和训练模型的客户，也有越来越多地将模型部署到生产环境中的客户。Nadampalli说，编译模式消除了很多Python的开销，使模型或工作负载非常接近使用模式。

“作为一名开发者，我同时使用这两种模式，”Nadampalli说。“例如，当遇到新的东西时，我会从渴望模式开始，这样我就可以在调试和提取主要硬件细节方面拥有很大的灵活性，同时也能轻松地进行实验和迭代。一旦我接近我想要的性能，我就切换到编译模式，并针对我们的生产用例进一步调整它。”

Antiga说，随着生成式AI越来越流行，开发者们正在构建更大的模型。GPU在计算方面也得到了越来越多的优化。对在不同加速器、机器上的不同GPU或不同机器上并行运行模型的需求正在增加。

Seligman表示，AWS“非常兴奋”能够为PyTorch做出贡献，并“确保数据科学家、机器学习研究人员和开发者拥有这个令人惊叹的库，他们可以用它来工作、创新、构建新模型并探索这个生成式AI的新世界”。

使PyTorch与多个后端兼容的工作展示了OpenAI的Triton的价值，以及PyTorch团队对简化开发者工作的重要性，这一主题继续将PyTorch与其他框架区分开来。

例如，Desmaison解释说，Triton是将特定编写的Python函数引入GPU内核的部分。它使开发者能够使用他们的Python代码并在另一个后端上使用它。这还处于早期阶段，但它已经存在。例如，开发者可以将代码移动到AMD GPU。工程师可以为Triton生成一些东西，并将其扩展到不同的后端。

“我们的目标是让用户将设备对象从CPU切换到CUDA，仅此而已，”Desmaison说。“他们不需要了解我们在后端所做的这些可怕的事情，以决定使用哪个以及我们如何为不同的编译器做出选择。”


## 未来展望

PyTorch花了八年时间才达到主导地位。但是，社区还能保持多久这样的速度？社区是否只是在广泛的基础上不断发展壮大？

这些是在未来几年需要解答的问题。更多专门的框架势必会涌现。

很多事情取决于社区采取何种广泛的方法。PyTorch支持很多应用程序。但是，如果出现更多专门的框架会发生什么？PyTorch社区将走向何方？

Antigua说，PyTorch将面临那些功能较少且可能针对某些方面进行了更多优化的框架的挑战。但他同时指出，由于PyTorch的设计允许它进行调整，正如其编译器方法所例证的那样，它有很大的发展空间，可以满足更多专门的工作负载。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)