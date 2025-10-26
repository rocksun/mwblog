<!--
title: 告别Python：5大JavaScript机器学习库
cover: https://cdn.thenewstack.io/media/2025/10/d934ed3d-javascriptlibrariesforml.jpg
summary: JavaScript正成为机器学习新选择。文章介绍了5个JS库：Danfo.js用于数据处理，The Natural Library用于NLP，Synaptic构建神经网络，TensorFlow.js用于深度学习，Scikit.js用于传统ML。
-->

JavaScript正成为机器学习新选择。文章介绍了5个JS库：Danfo.js用于数据处理，The Natural Library用于NLP，Synaptic构建神经网络，TensorFlow.js用于深度学习，Scikit.js用于传统ML。

> 译自：[Ditch Python: 5 JavaScript Libraries for Machine Learning](https://thenewstack.io/ditch-python-5-javascript-libraries-for-machine-learning/)
> 
> 作者：Loraine Lawson

[Python](https://thenewstack.io/what-is-python/)长期以来一直是训练和使用机器学习模型的主导语言，但这种情况正在发生变化。

Ippon Technologies的高级软件工程师Laurie Lay表示：“我们正在将[机器学习工具引入JavaScript](https://thenewstack.io/the-rise-of-javascript-in-machine-learning/)生态系统。” “通过这样做，我们正在将这项技术普及到世界上最大、最活跃的开发者社区，即JavaScript社区。”

在今年的[devmio国际JavaScript大会](https://javascript-conference.com/new-york/)上，Lay演示了五个开源[JavaScript](https://thenewstack.io/introduction-to-javascript/)库，这些库现已可供希望深入研究机器学习的前端和[Web开发者](https://roadmap.sh/roadmaps?g=Web+Development)使用。Lay专注于全栈开发，并且是Ippon Technology人工智能卓越中心的一员。

她说，这五个库为JavaScript开发者提供了一种开始使用机器学习并在JavaScript中处理模型的方式。

## 1. Danfo.js

Lay说，Python的Pandas可以清理、转换和构建数据。[Pandas](https://thenewstack.io/python-pandas-ditches-numpy-for-speedier-pyarrow/)基本上是C语言的Python封装，使数据操作变得更容易。

在JavaScript生态系统中，有[Danfo.js](https://github.com/javascriptdata/danfojs)，她说它“深受Pandas启发”。她概述了Danfo.js提供的功能：

*   数据操纵和处理；
*   模型训练前的数据准备和清理；
*   类似Pandas的API，易于数据整理并与TensorFlow.js集成。

她说：“它将数据帧和序列数据结构引入JavaScript，用于处理关系型和带标签的数据。” “Danfo.js只是为了理解数据中发生了什么，能够识别是否有任何偏差或任何需要回去修复的异常值。”

她补充说，它还有一个VS Code扩展。

## 2. The Natural Library

Lay说，[**The Natural Library**](https://naturalnode.github.io/natural/)是一个用于自然语言处理的轻量级工具。她指出The Natural Library提供：

*   [自然语言处理](https://thenewstack.io/service-simplifies-natural-language-processing-for-developers/)（NLP），包括分词、将文本拆分为单词或词干提取（将单词简化为词根形式）；
*   用于分词、词干提取、分类和情感分析的简单[API](https://thenewstack.io/your-apis-are-costing-more-than-you-think/)；
*   快速有效的基于文本的机器学习任务。

## 3. Synaptic

[Synaptic](https://github.com/cazala/synaptic)是一个用于构建神经网络的JavaScript库。

Lay说：“我之所以说这个库更容易在JavaScript中[构建神经网络](https://thenewstack.io/airbnb-builds-a-second-neural-network-to-diversify-listings/)，是因为它不需要你掌握Python等其他语言。” “设置一个Synaptic神经网络真的很容易。”

Lay的幻灯片显示Synaptic用于：

*   神经网络；
*   无架构限制，高度模块化，支持复杂的网络类型；以及
*   试验自定义神经网络架构。

## 4. TensorFlow.js

[**TensorFlow.js**](https://www.tensorflow.org/js)是一个开源JavaScript库，允许开发者直接在Web浏览器或Node.js环境中运行和构建机器学习模型。

Lay说：“如果你需要执行图像或音频分类等复杂任务，那么你会希望利用TensorFlow.js强大且预训练好的模型。” “这是生产级深度学习领域无可争议的重量级冠军。”

[TensorFlow.js用于](https://thenewstack.io/googles-new-tensorflow-tools-and-approach-to-fine-tuning-ml/)：

*   通用和深度学习；
*   强大的GPU加速大型生态系统，预训练模型；以及
*   重型模型训练、深度学习、图像/音频任务。

## 5. Scikit.js

[**Scikit.js**](https://github.com/transitive-bullshit/scikit-learn-ts)用于预测数据分析和机器学习。根据其[npm说明](https://www.npmjs.com/package/scikitjs-node)，它的目标是成为scikit-learn Python库的TypeScript移植版。

Lay说：“最后，如果你希望利用你可能熟悉来自Python机器学习生态系统的经典机器学习算法，或者你对Python中的scikit-learn API感到满意，那么你可能需要选择Scikit.js之类的库，它的API几乎完全相同。”

使用Scikit.js用于：

*   传统[机器学习模型](https://thenewstack.io/use-these-tools-to-build-accurate-machine-learning-models/)；
*   熟悉的scikit-learn API，广泛的经典算法；
*   从Python的scikit-learn过渡的开发者。

Lay说：“这些工具现在都可以使用。” “社区正在不断壮大，利用这一点的最佳方式是选择一个库，找到你感兴趣的数据集并开始构建，因为我们作为JavaScript开发者可以塑造智能、数据驱动的Web未来。”

后记：Lay在Ippon Technologies的同事Julian Wilkison-Duran在同一次会议上分享了在浏览器中处理机器学习模型的第六种选择。在“[JavaScript库在浏览器中运行机器学习模型](https://thenewstack.io/javascript-library-runs-machine-learning-models-in-browser/)”中阅读更多相关内容。