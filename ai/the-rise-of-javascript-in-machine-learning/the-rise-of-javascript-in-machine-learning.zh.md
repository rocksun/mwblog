纽约 — [Ippon Technologies](https://www.linkedin.com/in/laurie-lay/) 的高级软件工程师 Laurie Lay 为 JavaScript 开发者带来了一个好消息：你不必精通 [Python](https://thenewstack.io/what-is-python/) 也能进行 [机器学习](https://thenewstack.io/javascript-library-runs-machine-learning-models-in-browser/) (ML)。她说，虽然 Python 在该领域显然占据主导地位，但将 JavaScript 与 ML 结合使用将为 [前端开发者](https://roadmap.sh/frontend) 提供新方法，在设备上用 AI 增强应用程序的功能。

Lay 在 9 月 30 日至 10 月 1 日在布鲁克林举行的 [devmio 国际 JavaScript 大会](https://javascript-conference.com/new-york/) 上解释了 [JavaScript](https://thenewstack.io/introduction-to-javascript/) 和 [Node.js](https://thenewstack.io/a-backend-for-frontend-watt-for-node-js-simplifies-operations/) 为 AI 新前沿带来的优势。

## 为何 Python 是机器学习之王

Lay 表示，Python 迄今为止一直是执行机器学习任务的语言，但 Python 的语法本身并没有导致它成为机器学习的首选语言。

她说：“在过去十年中，任何关于机器学习的严肃讨论都与 Python 编程语言相关联，这种主导地位并非偶然，也不是因为 Python 是一种速度特别快的语言。真正的原因是 Python 成为绝大多数其他库的高级‘胶水’语言。”

她指出，机器学习中的繁重工作并非由 Python 代码本身完成，而是由诸如用于数值计算的 [NumPy](https://thenewstack.io/what-is-the-numpy-python-library-and-how-do-you-use-it/) 和用于数据操作的 [Pandas](https://thenewstack.io/pandas-a-vital-python-tool-for-data-scientists/) 等基础库处理。这些库实际上是围绕用 C 和 Fortran 编写的高度优化、低级代码的复杂 Python 封装。

[![全栈开发者 Laurie Lay 谈论使用 JavaScript 进行机器学习。](https://cdn.thenewstack.io/media/2025/10/ed5b3406-laurie_lay_presentation.jpg)](https://cdn.thenewstack.io/media/2025/10/ed5b3406-laurie_lay_presentation.jpg)

Laurie Lay 正在介绍 JavaScript 和机器学习。图片由 Loraine Lawson 拍摄。

她说：“正是这种架构使得科学家和研究人员能够使用简单、可读的 Python 语法，同时也能利用 C 语言在那些密集数学运算中的原始计算速度。这种易用性和高性能的结合推动了机器学习的发展。”

她补充说，Google 等公司早期的大量投资也功不可没，Google 支持了 [TensorFlow](https://thenewstack.io/python-tutorial-use-tensorflow-to-generate-predictive-text/) 的开发，并 [聘请了 Python 创始人 Guido van Rossum](https://www.forbes.com/sites/tomiogeron/2012/12/07/dropbox-snags-google-exec-and-python-god-guido-van-rossum/)。

她说：“资金、易用性和强大的社区帮助巩固了 Python 的地位，从而产生了丰富的生态系统、工具、框架和高质量的文档。”

## 如果不是 Python，那 JavaScript 呢？

因此，入门门槛并非 Python 语法本身，而是“复制这个庞大、经过实战检验的低级科学计算生态系统”，她说道。Python 在离线模型训练方面占据主导地位，但目前的格局正在发生显著变化。

她说：“现在，用 JavaScript 执行严肃的机器学习实际上已成为现实，因为它是由一系列技术进步驱动的。”

她解释说，首先是 JavaScript 引擎的速度，例如 [Google V8](https://v8.dev/)，通过即时编译等技术，其执行 JavaScript 的速度已达到解释型语言曾经无法想象的水平，这大大提高了速度。其次，Node.js 提供了一个强大、可扩展的服务器端环境，将 JavaScript 从浏览器限制中解放出来。

还有 npm 生态系统，它创建了世界上最大的软件注册中心。Lay 表示，该生态系统鼓励开放协作的文化，并使共享和构建复杂工具变得更容易。

npm 生态系统现在包含许多专门的机器学习库，为开发者提供了使用 JavaScript 构建和训练模型所需的工具。但她指出，自 Python 成为机器学习冠军以来，还发生了一个更重大的转变。

Lay 说：“可能最具影响力的转变是现代客户端硬件的持续改进，从笔记本电脑到口袋里的手机，它们现在都具备了在本地实际运行这些复杂机器学习模型的计算能力。这彻底改变了一切。”

## 用于机器学习的 JavaScript

Lay 提醒说，目标不是取代 Python。而是用 JavaScript 在客户端实现机器学习。

她说：“这是将机器学习引入 JavaScript 作为原生语言的环境中，即在网络浏览器中。这开启了一类新型应用程序，而这些应用程序用传统的、以服务器为中心的架构是很难甚至不可能实现的。”

> “这是将机器学习引入 JavaScript 作为原生语言的环境中，即在网络浏览器中……”
> **—— Ippon Technologies 高级软件工程师 Laurie Lay**

Lay 继续说，在客户端运行机器学习模型解锁了以前不可能实现的许多功能。

她说，传统的基于云的 AI 模型要求用户将其私人信息和数据——包括照片、私人消息或医疗信息——发送到第三方服务器进行处理。这带来了固有的隐私和安全风险。但在设备上，用 JavaScript 进行机器学习可以降低这些风险。

她说：“当学习模型直接在用户设备上运行时，数据无需离开设备，它保持私密和安全。这对于处理敏感信息的应用程序非常重要，比如医疗保健、金融和我们的企业应用程序。我们还可以看到，通过消除对网络连接的依赖，我们的应用程序更快、更可靠，预测也更即时，因为应用程序甚至可以离线运行。”

她补充说，模型还可以针对每个用户在他们自己的设备上进行微调和定制。

Lay 说：“例如，产品推荐模型可以通过查看用户的图片来适应他们独特的风格或服装，而无需让他们将私人图片发送到单独的服务器。”

## Node 的优势

根据 Lay 的说法，Node.js 也为机器学习架构带来了优势。

她指出，Node 支持的后端逻辑存在于一个世界中，而几乎完全用 Python 编写的复杂数值运算机器学习模型则存在于另一个世界。

为了让它们进行通信，开发者必须构建一个单独的 Python 微服务，将其封装在 [Flask](https://thenewstack.io/how-to-use-flask-a-lightweight-python-framework/) API 中——Flask 是一个轻量级、最小化的 Python Web 框架，也用于构建 API——然后从 Node 应用程序进行网络调用。她补充说，这部署起来既慢又复杂，还会引入另一个故障点。

Lay 说：“Node 的强大之处在于它建立在 Chrome 的 V8 驱动的事件驱动、非阻塞 I/O 模型之上。这使得 Node 在处理大量并发 Web 请求方面表现出色，通过将机器学习功能直接添加到 JavaScript 代码和 Node 服务器中，你就可以拥有一个理想的平台来提供来自已训练机器学习模型的预测。”

她补充说，Node 非常适合构建智能聊天机器人等实时应用程序，使其能够处理数千个并发对话，或处理来自连接设备的实时数据。这使得创建诸如可以根据房间里的人或宠物调整恒温器的家庭助理，或以最小延迟为大量用户提供个性化推荐的实时推荐引擎等功能成为可能。

## 机器学习为何需要 JavaScript 和 Python

Lay 说：“我想确保这次演讲传达的主要信息之一是，这不是 Python 或 JavaScript 的二选一。这并非总是一方优于另一方。这关乎充分利用每个生态系统在机器学习应用中的优势。”

她说，当开发者需要计算密集型模型训练时，Python 仍然表现出色。JavaScript 最适合与 Node 一起提供实时、可扩展的 API 以及客户端操作。它还支持应用程序的额外安全性和设备特定操作。

> “这是当前正在发生的网络平台的演进，作为开发者，我们有能力构建新一代的这些智能应用程序。”
> **—— Laurie Lay**

她解释说，甚至可以采取混合方法，开发者在 Python 中训练模型以优化复杂的机器学习模型。该模型可以保存为 JSON；在 Node 中，编码员可以使用像 TensorFlow 这样的库将预训练模型加载到内存中。然后，开发者可以暴露一个 API 端点，客户端应用程序可以调用并从该预训练模型获取预测。

她说：“这种方法结合了 Python 训练环境的强大和成熟性，以及 Node 的超快速、多请求性能和部署机器学习模型的稳健、可扩展架构。”

她补充说，不要认为 JavaScript 生态系统中的机器学习是一种“昙花一现的趋势”。

Lay 说：“这是当前正在发生的网络平台的演进，作为开发者，我们有能力构建新一代的这些智能应用程序。我们的许多已经用 JavaScript 构建的应用程序能够将应用程序数据本地化、私有化和实时化。这使得 JavaScript 成为在我们小型、资源受限的本地设备上部署机器学习模型的完美语言。”