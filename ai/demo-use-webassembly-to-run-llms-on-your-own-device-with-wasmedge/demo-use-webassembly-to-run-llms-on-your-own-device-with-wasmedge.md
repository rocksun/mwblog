<!--
title: 在设备上通过WebAssembly本地执行LLM
cover: https://cdn.thenewstack.io/media/2024/01/772b3fc7-demo_kccnc-na_second-state_thumbnail-1024x576.png
-->

在这个WasmEdge演示中，Second State的Michael Yuan展示了如何创建一个轻量级执行环境，以运行大型语言模型。

> 译自 [Demo: Use WebAssembly to Run LLMS on Your Own Device with WasmEdge](https://thenewstack.io/demo-use-webassembly-to-run-llms-on-your-own-device-with-wasmedge/)，作者 B. Cameron Gain。

11月在北美KubeCon+CloudNativeCon大会上，Second State联合创始人[Michael Yuan](https://www.linkedin.com/in/myuan/)(该公司为云原生环境提供Wasm，同时也是CNCF项目WasmEdge的维护者)向The New Stack记者B. Cameron Gain展示了WasmEdge的工作原理。

Yuan展示了开源的WasmEdge如何使用[WebAssembly](https://thenewstack.io/webassembly/)在您自己的设备上本地运行大型语言模型，无论是Mac、笔记本电脑还是像树莓派这样的边缘设备。使用轻量级的执行环境，可以在这些不同类型的设备上高效地运行更大的语言模型。

Yuan表示: "ChatGPT无法在这些环境中运行，但是使用像WasmEdge这样轻量级的[大型语言模型](https://thenewstack.io/what-is-a-large-language-model/)，你就可以运行它"。

通常与机器学习相关的Python不是方程式的一部分。Yuan说:"为什么不使用Python？在Python中进行大规模语言推理，您需要整个PyTorch和GPU驱动程序等等，这些东西大约是3GB，我不敢在我的电脑上安装它。"

Yuan补充说:Python代码不是为了可移植性而设计的，因为在不同的计算机上运行LLM意味着“您必须重新开始”。他表示:"Wasm运行时是一个虚拟机，类似于JVM，所以它提供了跨平台兼容性，不仅跨CPU，还跨GPU。"

此外，Yuan表示，Python是一种解释型语言，在某种程度上其速度很慢，因为在将[Python用于机器学习](https://thenewstack.io/intel-oneapis-unified-programming-model-for-python-machine-learning/)时，用户必须依赖底层的基于C的库(如PyTorch)“才能真正完成工作”。他补充说:“因此，通过Wasm，我们使用了更多类似C的语言，比如Rust，来弥合这一差距。”

## 小步快跑

正如Yuan展示的，只有三个步骤。第一步是安装Water Manage，这里是命令。如您所见，会议的网络连接很糟糕，所以下载和安装的过程可能需要一分钟左右。一旦安装完成，您将不需要互联网连接来进行未来的安装。  

第二步是下载一个大型语言模型。这里是命令，您可以参考文档获得更多详细信息。这是Llama模型之一。

最后，第三步只涉及简单地剪切和粘贴Wasm应用程序。

Yuan推荐了从何处找到要插入WasmEdge的LLM数据:Hugging Face仓库，这里有成千上万的LLM教程模型可供下载。他表示:“其中一些可以生成SQL查询，一些可以生成代码，一些可以回答各种不同的问题，所以您可以下载喜欢的模型，并将其放入WasmEdge中。”
