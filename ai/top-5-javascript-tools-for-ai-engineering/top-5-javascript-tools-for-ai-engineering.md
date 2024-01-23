<!--
title: JavaScript领域的五大AI工程利器
cover: https://cdn.thenewstack.io/media/2024/01/664551e8-jigar-panchal-ltay0_ounkc-unsplash-1024x576.jpg
-->

五大引领AI工程的JavaScript工具，为欲将LLM融入项目的开发者提供关键资源。

> 译自 [Top 5 JavaScript Tools for AI Engineering](https://thenewstack.io/top-5-javascript-tools-for-ai-engineering/)，作者 Alexander T. Williams。

传统上以在网页开发中扮演角色而闻名的JavaScript，令许多人惊讶的是，它在开发[使用大语言模型（LLM）的应用程序](https://thenewstack.io/4-key-tips-for-building-better-llm-powered-apps/)方面也被证明是无价的。在本文中，我们将探讨五个主要用于AI工程的工具，突出一些对于希望将LLMs纳入其项目的开发人员而言至关重要的资源。我们选择这些工具是因为它们在简化复杂的AI流程和增强模型训练方面具有独特的能力，适用于经验丰富的AI工程师和刚接触AI的JavaScript开发人员。

Python或Mojo[对于AI工程](https://thenewstack.io/python-gets-its-mojo-working-for-ai/)更为直接，然而，在[2023年已经价值1420亿美元](https://bluetree.ai/ai-industry-growth-metrics/)的市场中，为具有不同技能集的专业人士提供了丰富的机会。高级AI功能将随着时间的推移越来越容易访问更广泛的开发人员；即使在现在，存在许多JavaScript工具可以[帮助开发](https://thenewstack.io/why-viable-uses-next-js-and-node-js-for-ai-applications/)、训练和部署AI模型。

让我们更仔细地看看五个可以帮助促进和改进AI工程的JavaScript工具。

## 1. TensorFlow.js

作为由Google创建的著名[TensorFlow库](https://www.tensorflow.org/)的JavaScript适配版，TensorFlow.js专门面向Web和Node.js环境，以直接将机器学习能力带到浏览器和服务器端应用程序中。

TensorFlow.js的一个关键优势是其在浏览器内直接[运行机器学习模型](https://thenewstack.io/google-touts-web-based-machine-learning-with-tensorflow-js/)的能力。这个功能对于需要实时AI功能的应用程序特别有价值，比如LLMs以启用快速、无需服务器的处理。

其与[Node.js的兼容性](https://www.tensorflow.org/js/guide/nodejs)对于需要利用强大计算资源的服务器端应用程序同样重要，这些资源对满足LLMs的重要计算需求至关重要。

该库与现有JS应用程序的无缝集成使其成为许多开发人员的首选，因为它允许他们在其Web应用程序中整合AI功能，而无需进行大规模的重新工程或学习新语言。TensorFlow.js还提供了一系列[预训练模型](https://www.tensorflow.org/js/models)，以简化LLM集成的初始步骤。

在使用JavaScript进行[AI工程](https://thenewstack.io/ai-engineer-summit-wrap-up-and-interview-with-co-founder-swyx/)时，TensorFlow.js是开发者工具包中引人注目的资源。它不仅降低了为应用程序添加复杂的AI功能（如LLM）的门槛，还支持在Web上创建实时、交互式的AI体验，从而为用户参与和应用功能开辟了新的途径。

## 2. AI.JSX（Fixie.ai）

[由Fixie开发](https://blog.fixie.ai/introducing-fixie-ai-a-new-way-to-build-with-large-language-models-d4e1aeee6b81)的AI.JSX是一个专为使用JavaScript和JSX构建基于React项目的对话式AI应用程序而设计的动态框架。

AI.JSX在AI工程工具中脱颖而出，因为它对提示工程提供了强大的支持，并且与外部API轻松集成。它代表了在开发交互式、以AI为驱动的应用程序方面的重大进步，特别是对于专注于对话式AI的应用程序。

AI.JSX的核心功能之一是其在运行时动态构建用户界面的独特能力，这是一个称为[GenUI](https://www.fixie.ai/post/the-future-of-application-development-is-generative)的特性。在这里，开发人员可以向LLM提供一组React组件，从而可以创建具有互动性且适应应用程序需求的UI。

Fixie的DocsQA允许模型以各种真实来源为基础，例如URL、文档、PDF，甚至是视频和音频文件。这[增强了模型的理解](https://thenewstack.io/fixie-and-its-agent-approach-to-leveraging-llms/)和响应能力，以确保AI是互动的、知情的，并且准确无误。

AI.JSX还通过其工具功能扩展了应用程序的能力，该功能侧重于通过API启用面向行动的功能，以使最终用户能够更高效、更有效地完成任务。

## 3. ConvNetJS

ConvNetJS是一个JavaScript库，旨在直接在浏览器或Node.js环境中[实现深度学习](https://cs.stanford.edu/people/karpathy/convnetjs/started.html)，使其对各种技能和经验水平的JavaScript开发人员都具有可访问性和便利性。

ConvNetJS以其实现深度学习架构的能力而脱颖而出，包括[卷积神经网络](http://deeplearning.stanford.edu/tutorial/supervised/ConvolutionalNeuralNetwork/)，而无需外部依赖项或专业软件。

从理论上讲，像ConvNetJS这样的基于识别的库可以用于开发以[威胁情报丰富](https://thenewstack.io/automated-threat-enrichment-an-overview/)为重点的安全应用程序，帮助识别未经授权的访问、恶意软件特征模式、网络钓鱼尝试、[借记卡欺诈](https://www.aura.com/learn/debit-card-fraud)、身份盗窃等[数字犯罪形式](https://www.ic3.gov/Media/PDF/AnnualReport/2022_IC3Report.pdf)，这些犯罪留下可搜索的痕迹。

这个库的主要优势之一是其易用性，提供了一个直观的API，使开发人员能够相对轻松地[定义、训练和部署神经网络](https://openai.com/research/techniques-for-training-large-neural-networks)。这种简单性对于可能在深度学习方面经验不丰富但试图将先进的AI功能整合到其应用程序中的JS开发人员来说尤为有价值。

该库促进了能够理解和生成人类语言的神经网络的创建和集成，这对于诸如聊天机器人、[自动内容生成](https://cs.stanford.edu/~karpathy/convnetjs/demo/image_regression.html)和语言翻译服务等应用程序至关重要。其神经网络模型可以在大型数据集上进行训练，以使它们能够捕捉人类语言的细微差别，并提高AI驱动应用程序的整体响应性和准确性。

## 4. Brain.js

Brain.js是我们列表中的一个显著条目，因为它提供了[在JavaScript中实现神经网络](https://developer.ibm.com/tutorials/build-a-neural-network-with-nothing-but-javascript-using-brainjs/)的简化和易接近的方式，适用于浏览器和Node.js环境。[Brain.js](https://thenewstack.io/brain-js-brings-deep-learning-to-the-browser-and-node-js/)的一个关键潜在应用是自动化诸如文本分析、[PDF文档合并](https://xodo.com/merge-pdf)、文档转换、图像分析等过程，总体上解决涉及处理大量数据的任何任务。

Brain.js的设计注重简单性和易用性，使其成为JavaScript开发人员的理想选择，尤其是那些在机器学习方面经验不丰富的开发人员。该库提供了一个直观的API，让您能够快速创建、训练和部署神经网络。

这个强大的工具在LLM开发中发挥着关键作用，通过创建能够处理和解释大量文本数据的神经网络，来增强人工智能应用的效果和准确性。通过在广泛的文本数据集上训练神经网络模型，Brain.js帮助捕捉人类语言的微妙差异。

## 5. Tabnine

Tabnine是一款由[人工智能驱动的代码补全助手](https://thenewstack.io/top-5-code-completion-services/)，显著增强了编码体验。具体而言，它加速了更广泛的开发过程，同时积极维护代码的完整性。

Tabnine的人工智能从代码库中学习，并根据自然语言注释提供相关的代码片段、函数完成，甚至整个代码块。这种支持水平在管理涉及人工智能应用开发的复杂细节方面非常宝贵。

Tabnine的集成能力引人注目，因为它与一系列流行的IDE和代码编辑器无缝配合，包括[Visual Studio Code](https://code.visualstudio.com/)、[IntelliJ IDEA](https://www.jetbrains.com/idea/)等等。这种强大的兼容性有助于确保开发人员可以在不干扰其现有工作流程的情况下访问Tabnine的人工智能辅助编码功能。

Tabnine的另一个重要方面是其致力于维护代码的隐私和安全性。该工具经过精心设计，注重尊重开发人员代码的隐私，确保您正在处理的代码保持私密和安全。

## 用JavaScript轻松进行AI工程

今天我们在这里突出展示的每个工具都带来了自己独特的优势，它们共同代表了JavaScript在AI开发中可以发挥的重要作用。

在AI工程中，JavaScript因其在浏览器和服务器端环境中的无缝集成而脱颖而出，提供了无与伦比的灵活性。与经常局限于服务器端操作的Python不同，JavaScript直接在Web浏览器中实现实时、交互式的AI应用程序。

这使得开发人员能够创建更具动态性和响应性的AI驱动体验，利用JavaScript的全栈能力弥合后端AI算法与前端用户交互之间的差距。
