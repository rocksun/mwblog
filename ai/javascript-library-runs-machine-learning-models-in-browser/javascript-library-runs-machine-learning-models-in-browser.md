<!--
title: JavaScript库在浏览器中运行机器学习模型
cover: https://cdn.thenewstack.io/media/2025/10/601d1bfd-neuralnetworkmodel.png
summary: Julian Wilkison-Duran发布AsterMind-ELM，一个JavaScript开源库，将轻量级机器学习ELM带入浏览器。无需GPU或服务器，实现设备上实时、低内存训练与预测，革新前端AI应用。
-->

Julian Wilkison-Duran发布AsterMind-ELM，一个JavaScript开源库，将轻量级机器学习ELM带入浏览器。无需GPU或服务器，实现设备上实时、低内存训练与预测，革新前端AI应用。

> 译自：[JavaScript Library Runs Machine Learning Models in Browser](https://thenewstack.io/javascript-library-runs-machine-learning-models-in-browser/)
> 
> 作者：Loraine Lawson

[Julian Wilkison-Duran](https://www.linkedin.com/in/julianduran/) 创造了他所谓的针对浏览器的“穷人的机器学习模型”。

“我真正想做的是将机器学习带入前端，而且我认为模型不需要十亿个参数就能做一些非常酷的事情，尤其是在前端，”他说。“我着手创建一种新模型，它不需要大量参数和巨大内存就能运行，但仍然能够在网络浏览器中完成非常实用的事情。”

结果就是 [AsterMind-ELM](https://github.com/infiniteCrank/AsterMind-ELM)，一个用 [JavaScript](https://thenewstack.io/introduction-to-javascript/) 编写的开源机器学习库，他补充说，这**不是**一个带有 JavaScript 包装器的 [Python](https://thenewstack.io/new-python-cli-tool-catches-mcp-server-issues-before-agents-do/) 库。他上周在布鲁克林举行的 [devmio 国际 JavaScript 大会](https://devm.io/experiences/the-javascript-community/)上介绍了这个开源项目。

Wilkison-Duran 是 Ippon Technologies 的一名全栈软件工程师，他将 AsterMind-ELM 构建成一个模块化的极限学习机（Extreme Learning Machine, ELM）库，用于 JavaScript 和 [TypeScript](https://thenewstack.io/what-is-typescript/)。他用 JavaScript 重写了 [极限学习机 (ELM)](https://www.geeksforgeeks.org/machine-learning/extreme-learning-machine/) 网络，供前端开发人员使用。

## 理解 ELM

[ELM](https://www.linkedin.com/school/ntusg/) 是一种神经网络算法，由 [Guang Bin Huang](https://www.linkedin.com/in/guang-bin-huang-5949a9b3/?originalSubdomain=sg) 于 2006 年开发，他在新加坡南洋理工大学的研究专注于神经网络。ELM 用于机器学习和人工智能。它在分类、回归和聚类等训练任务中快速高效。

但在 2006 年，研究人员试图解决如何平衡数据集最佳学习率的问题。

“很多人都在各地问这个问题，因为他们不想在数据中心上花费数十亿美元，”他说。

Huang 的解决方案是，如果我们创建一个完全随机且从未触及的隐藏层，那么我们是否可以不训练所有这些东西呢？它还会奏效吗？

“对许多工程师来说，尤其是在他那个时代，这听起来就像是未经单元测试就发布生产代码。这听起来太疯狂了，”Wilkison-Duran 说。“他所做的只是一个我们高中都学过的简单数学技巧。他说，‘如果我们把隐藏层当作一张地图呢？’”

他补充说，所有的魔力都发生在隐藏层中。这就像俯瞰一座城市并试图指路——你无法看到单独的街道，因为建筑物太高了。但 Wilkison-Duran 说，如果你在城市上放一个网格呢？

“突然之间，[它]有点像战舰游戏：你可以说，‘哦，银行在三、五格，或者公园在四、三格，’”他解释道。

> “我发现，神经网络，它们就是矩阵数学。”
> 
> **—— Julian Wilkison-Duran，AstroMind ELM 创始人**

他说，这为开发人员提供了一个不精确也永远不会精确的参考，但它是一个足够好的数据地图，能够说明事物在哪里。

现在你有了地图，如何找出从 A 点到 B 点的路线呢？答案是 [莫尔-彭罗斯逆](https://www.cantorsparadise.com/demystifying-the-moore-penrose-generalized-inverse-a1b989a1dd49)，也称为伪逆。

“这是一种简单的矩阵运算，我们大多数人在高中都学过，但我们并没有真正理解为什么要学习它；直到大约一年前，我才真正理解高中为什么要学习 [矩阵数学](https://math.libretexts.org/Bookshelves/Applied_Mathematics/Applied_Finite_Mathematics_(Sekhon_and_Bloom)/02%3A_Matrices/2.01%3A_Introduction_to_Matrices)，”Wilkison-Duran 说。“我发现神经网络，它们就是矩阵数学。”

Wilkison-Duran 解释说，可以这样看待隐藏层：当数据放入隐藏层时，它就像一张揉皱的纸。Astro-Mind ELM 使用输出层作为隐藏层地图的 GPS。

“假设我拿一张纸，然后把它揉成一团。我现在很难分辨纸上的句子，甚至它写了什么，但如果我把纸展开，突然之间它又开始变得有意义了，”他说。

ELM 用于实时训练速度和计算效率比实现绝对最高准确性更关键的场景。用途包括训练速度至关重要的工业应用——例如金融预测、社交媒体情感分析、实时控制系统和复杂模式识别。

## AstroMind ELM 将机器学习带入浏览器

他表示，与普通神经网络不同，Astro-Mind ELM 不解决所有隐藏层。它只解决最后一层，因此内存消耗和所有设置都显著降低。

“你不需要训练数十亿个参数，你只需训练最后一层，”他说。

AstroMind-ELM 将 ELM 的能力带入浏览器，并使其可供 JavaScript 开发人员使用。

“我把它放进了浏览器，然后说现在它在浏览器里，你能用它做什么？”Wilkison-Duran 说。“我将 ELM 的技术、数学和所有这些东西重新用 JavaScript 编写……这样你就可以即时训练模型，并且它在浏览器中运行，而无需大量内存。”

他再次强调，AsterMind-ELM 并非用 Python 编写，然后用 JavaScript 封装，而是完全用 JavaScript 重写的。

他补充说，AstroMind-ELM 并非旨在处理生成大量文本的巨大 [大型语言模型](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)。相反，它是非常特定的模型，你可以即时创建和训练，然后像乐高积木一样串联起来。

Wilkison-Duran 在 GitHub 仓库中解释道：“AsterMind 将即时、微型、设备上的机器学习带到网络上。”“它让你能够交付在几毫秒内训练、以微秒级延迟预测，并完全在浏览器中运行的模型——无需 GPU，无需服务器，无需跟踪。”

除了 ELM，该库现在还包括 kernel ELM。

“在这种情况下，kernel ELM 不使用网格，”他说。“相反，它们使用某种地标。如果你想象一个社区，你在其中行走，那里有一棵树，它很大，我能认出来。那里有一个邮箱。kernel ELM 所做的就是利用这些地标来找出你的数据在哪里。”

## 演示 AsterMind ELM

他演示了如何仅用 20 个句子实时训练模型。模型随后将数据分类为世界、体育、商业和科技。它预测一个句子将属于科技类，这是正确的。但有趣的是，它在给出句子有 48% 的机会属于科技类时是正确的，而其他选项仅被评为 18% 和 17%。

“它所做的就是将所有数据分类到世界、体育、商业和科技中，然后在列方面，这些都是你的向量，”他说。“向量在给它们命名之前没有任何意义，但在这种情况下，向量代表句子，我在这张幻灯片中想指出的另一件事是它不大，所以模型本身实际上只是一个 [JSON 文件](https://thenewstack.io/working-with-json-data-in-python/)。”

> “AsterMind 将即时、微型、设备上的机器学习带到网络上。”
> 
> **—— AstroMind GitHub 仓库**

他 [还演示了训练模型识别他的声音并区分左右](https://www.youtube.com/watch?v=F_S5M_60fRY&t=2755s)，然后玩了一个使用语音命令控制动作的游戏。

“这将是一个游戏规则改变者，因为每个人都在说，‘哦，前端现在已经不行了（到院即死）。你可以用 LLM 来生成它，它能生成丰富而动态的 UI，你可以用它做一些惊人的事情，’”他说。“我们作为 JavaScript 开发人员真正喜欢做的是，创建令人惊叹的小部件，创建非常棒的视觉效果。”

他演示了用四拍落地鼓点（典型的摇滚鼓点）训练 ELM。它迅速生成了鼓点，无需等待任何东西启动或任何后端干预。

AstroMind ELM 库还允许开发人员将模型串联起来，并同时在浏览器中运行多个模型。他演示了该库中的几个不同模型。

“重点是你可以用这个模型构建奇妙的东西，”他说。“你可以 [用非常少的数据训练它](https://thenewstack.io/machine-learning-for-real-time-data-analysis-training-models-in-production/)。你甚至可以使用合成数据进行初步训练。”

ELM 也不要求你保留数据。一旦训练完成，数据就可以被丢弃以释放内存。

至于上下文窗口——这可能是 LLM 的一个问题——他说，限制在于隐藏层和 JavaScript 本身的内存限制。

“我对此进行了大量的实验，我可以使用 Web Worker 和在线学习达到 1,000 个参数，”他说。“这意味着，我可能有 1,000 个参数，但它在 Web Worker 中，并且我以流式传输训练数据，这样它就不会一次性占用所有内存。”

## 你能用它构建什么？

该仓库解释说，借助 AstroMind ELM 库组件，例如 Kernel ELMS、Online ELM、DeepELM 和 Web Worker 卸载，开发人员可以创建：

*   私有的、设备上的分类器，例如用于语言、意图、毒性或垃圾邮件的分类器，这些分类器可以根据用户反馈进行再训练；
*   实时检索和重新排名，结合紧凑的嵌入用于搜索和 RAG；
*   交互式创意工具，例如鼓点生成器和即时响应的自动完成功能；
*   边缘分析：从不离开页面的数据中获取回归器/分类器；以及
*   强大的 Deep ELM 链式管道，它们仍然微小且透明。

Wilkinson-Duran 希望围绕这个开源项目建立一个社区。他说，那些希望参与的人目前可以提交拉取请求，他会进行审查。他希望实现的一个成果是建立一个开发人员可以共享的权重生态系统。

“我真正希望的是人们能够改进这些模型，所以我把它开源了，这样每个人都可以深入研究，帮助我找出如何让它们比现在更强大，”他说。“我的意思是，这不需要太多。你可以喂它任何你想要的数据，即时训练它，而且即使它不能立即奏效又如何，因为你没有像 LLM 那样花费数十亿美元。你用你拥有的，用你得到的数据进行训练。”