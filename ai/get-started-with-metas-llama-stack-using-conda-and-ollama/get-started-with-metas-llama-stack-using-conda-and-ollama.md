
<!--
title: 使用 Conda 和 Ollama 开始使用 Meta 的 Llama 堆栈
cover: https://cdn.thenewstack.io/media/2024/10/f221e080-zdenek-machacek-w4oc9l5jmvc-unsplashb.jpg
-->

要设置 Meta 的新 Llama Stack 开发工具，您可以使用 Python 控制的环境或 Docker。我们选择了 Python 和 Ollama LLM。

> 译自 [Get Started With Meta’s Llama Stack Using Conda and Ollama](https://thenewstack.io/get-started-with-metas-llama-stack-using-conda-and-ollama/)，作者 David Eastman。

我喜欢在我的文章中展示技术，尤其是在我简陋的非硅基 MacBook 上。因此，当 Meta 发布了面向开发者的 [Llama 3.2 和 Llama Stack](https://thenewstack.io/llama-stack-released-to-help-developers-build-agentic-apps/) 时，我迫不及待地想要尝试一下。然而，我发现这个过程仍然有点复杂，而且不够灵活。

首先，什么是堆栈？Meta 试图定义一个平台的组件，可以帮助人们构建自己的大型语言模型 (LLM) 消费系统。主要组件是 *推理*，其中使用训练数据来预测标记响应——这也是我们都在这里的原因。这个有点尴尬的名字 *代理系统* 指的是 AI 将与其他实体（可能是其他 AI）协同工作，而不是仅仅响应聊天。但 [AI 代理](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) 的确切定义仍在热烈讨论中。还有很多 [其他组件](https://github.com/meta-llama/llama-stack)，尽管我认为其中一些将来可能会重新定义。它们可以通过 REST 端点的 API 访问。

另一个关键术语是 *分发* 的定义。这是 [“API 和提供者组合在一起，提供一致的整体。”](https://github.com/meta-llama/llama-stack/blob/main/docs/getting_started.md) 目前，这些有点临时，需要更多时间才能建立起来——平台的成功或失败将取决于这些的质量。

然而，堆栈的想法是合理的：为你不感兴趣的组件提供交钥匙解决方案，并选择你感兴趣的部分。

## 入门

你可以使用 Python 控制的环境来设置，或者使用 Docker。目前，使用 Docker 的参考资料并不多。

目前，该系统在 Windows 上无法运行——我发现一些引用交互式控制台的 Python 库是特定于 Unix 的。但这似乎无关紧要。堆栈中的主要示例模板在没有专用 GPU 的情况下无法正常运行，但我可以通过使用 [Ollama](https://ollama.com/) 分发来解决这个问题。（如果你有一个相当稳定的 Unix 机器，你应该会遇到更少的入门阻力。）

如果你使用 [本地分发](https://github.com/meta-llama/llama-stack-apps)，建议你使用 [Conda](https://docs.conda.io/projects/conda/en/stable/) 创建一个隔离的 Python 环境。

## 进入 Python

Conda 是一个开源工具，它与 Anaconda 和 [Miniconda](https://docs.anaconda.com/miniconda/miniconda-install/) 捆绑在一起，它既充当包管理器，也充当环境管理器。我们将使用这条小蛇。

我使用 homebrew 为我的可靠 MacBook 安装了 Miniconda：

```bash
brew install miniconda
```

版本检出：

![](https://cdn.thenewstack.io/media/2024/10/2806d6db-image-1024x189.png)

Conda 会将你的提示符更改为显示“base”或“stack”——因此你需要记住使用 `conda deactivate` 来关闭它。

以下是在设置方面的第一步：

```bash
#Clone the repo. Note the other directories below meta-llama
git clone https://github.com/meta-llama/llama-stack-apps.git
 
#Create your named conda python environment
conda create -n llama-stack python=3.10
 
#Activate the conda environment
conda activate llama-stack
 
cd llama-stack-apps
 
#install modules from requirements file
pip install -r requirements.txt
```


[Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) 很容易安装，我们将使用它来处理一个稍微早一点、更小的 LLM 模型 3.1。我们的想法是，我们将与 Ollama 在 localhost 上设置的服务器进行通信：

![](https://cdn.thenewstack.io/media/2024/10/4d08f2a2-image-1-1024x199.png)

请注意，我的提示符反映了我们为 conda 指定的名称“llama-stack”。

现在运行模型以检查它是否正常工作。该提示符就像一个带有模型的内联 ChatGPT：

![](https://cdn.thenewstack.io/media/2024/10/6d336eb4-image-2-1024x187.png)

是的，它花了 27 分钟来响应 hello——正如我之前提到的，我的非硅基 MacBook 真的太弱了，无法尝试这个。

请注意，Ollama 可以从内存中卸载，因此请查看此 API 响应以确认模型已加载：

![](https://cdn.thenewstack.io/media/2024/10/c09e68e7-image-3-1024x138.png)

推荐的安装 Ollama 分发的调用似乎不再有效：

![](https://cdn.thenewstack.io/media/2024/10/22d1d476-image-4-1024x94.png)

因此，使用新的构建命令，它是交互式的。请注意，选项使用 TAB 键很好地提供：

![](https://cdn.thenewstack.io/media/2024/10/c7a25872-image-5.png)

我们知道我们正在使用 Conda，而不是 Docker 来进行此分发。令人困惑的是，可用选项指的是“远程”Ollama，尽管它实际上是本地的。

此过程结束，下一个线索在路上：

![](https://cdn.thenewstack.io/media/2024/10/f89159dd-image-6-1024x66.png)

如您所见，它建议我配置我的新堆栈，我将其命名为 TheNewStackStack。到目前为止，我们已经创建、构建、安装和加载，现在我们需要配置。这就是 Meta 应该在更新版本中简化的内容。

但是，我运行了给定的行，我们得到了一个交互式表单，我们需要将推理提供程序与“远程”Ollama 服务器配对。其他使用的条目是 Meta 提供的默认值：

![](https://cdn.thenewstack.io/media/2024/10/d9b617cf-image-7-1024x286.png)

我确实想知道我是否没有完全理解这一点，但同样，这似乎有效。最后，它给出了实际运行堆栈的行：

![](https://cdn.thenewstack.io/media/2024/10/070d2fdf-image-8-1024x62.png)

不幸的是，我无法让我们的 TheNewStackStack 运行——它似乎没有意识到 Ollama 服务器。太接近了！

Meta 将其意图的早期版本提供给访问者使用，这很棒，如果您有一个好的 Unix 系统并且比我更幸运，它应该是可访问的。当一些奇特之处被解决时，我会在以后的版本中再试一次。但这篇文章应该让您了解您需要做的工作，以及您需要克服的体验，才能尝试一些示例脚本并实际使用堆栈！
