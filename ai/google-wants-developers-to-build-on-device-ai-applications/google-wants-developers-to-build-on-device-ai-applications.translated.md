# Google 鼓励开发者构建设备内 AI 应用程序

![Google 鼓励开发者构建设备内 AI 应用程序的特色图片](https://cdn.thenewstack.io/media/2024/05/acc90dc8-googleio_2024-1024x682.jpg)

当今的手机和电脑配备了直接在设备上运行 AI 的新硬件；在今年的 [Google I/O](https://thenewstack.io/devs-get-ai-pixie-dust-at-google-i-o-but-no-search-updates/) 上，Google 鼓励编码人员利用它。

其理念是在本地存储的数据上运行大型语言模型，即使没有互联网连接。数据保持私密，不会离开设备，这种方法可以节省资金。

在 Google I/O 的一场会议上，产品经理组 [Sachin Kotwani](https://www.linkedin.com/in/sachinkotwani/) 说：“作为一名开发者，你减少或消除了处理服务器端维护、容量、限制或成本的需要。”

**工作原理**

开发设备内 AI 应用程序的能力是当今 AI 处理方式的重大进步。

新手机和电脑中的神经处理器使设备内 AI 成为可能。

如果你没有注意到，AI 已经存在于设备中。它运行基本的智能手机活动，例如建议短信、改进图像和分析功耗以节省电池电量。

新手机和电脑中的神经处理器使设备内 AI 成为可能。但是，在没有 AI 加速器的情况下，在电脑上运行具有十亿或更多参数的 LLM（例如 TinyLlama 或 Phi-2）非常缓慢。你只能在 CPU 上使用 [Jan.ai](https://jan.ai/) 或 [GPT4All](https://gpt4all.io/index.html) 运行 LLM，但这会给你的电脑带来负担。

在配备 [强大 GPU](https://thenewstack.io/free-gpus-and-ai-chips-are-available-to-run-ai/) 的电脑上运行 LLM 非常棒。但设置很麻烦——你需要下载模型、加载神经网络环境（例如 Nvidia 的 CuDNN）、安装开发者工具并编译它。

新一代能够在设备上进行矩阵运算的加速器和 GPU 使 AI 在手机上成为可能。

因此，大多数 AI 都在功能强大的 GPU 上的云中发生，这可能像将 GPT-4 API 加载到聊天机器人界面中一样简单，然后将查询卸载到 OpenAI 服务器基础设施中的 GPU。但这些 API 不是免费的，你必须付费才能使用 OpenAI 的基础设施。

新一代能够在设备上进行矩阵运算的加速器和 GPU 使 AI 在手机上成为可能。

Google 的新 Pixel 8A 手机有一个用于 AI 的 Edge TPU（张量处理单元），英特尔和 AMD 在电脑上拥有神经处理单元。设备内 AI 还可以与基于云的 AI 资源相结合。

## 开发工具

来自 AMD、英特尔和 Nvidia 等芯片制造商的开发工具可用于在设备上运行 LLM。

最近，Google 讨论了开发套件、API 和其他工具，这些工具利用其自己的 [Gemini](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/) Nano LLM 用于移动设备。此 LLM 是多模态的，这意味着开发者可以在其周围构建语音、图像、视频或聊天机器人应用程序。

“Gemini Nano 是 Android 推荐的生产路径。”

– Google 的 Thomas Ezan

Google 代表表示，Gemini Nano 是设备内 AI 最有能力的模型，它还可以很好地集成到 Android 应用程序中。

Google 的高级开发者关系工程师 [Thomas Ezan](https://www.linkedin.com/in/tezan/) 在 I/O 上表示：“Gemini Nano 是 Android 推荐的生产路径。”

对于那些不想陷入 Google 专有的 AI 开发环境的人，Google 将支持介于 20 亿到 30 亿参数之间的开源 LLM。

Ezan 说：“如果你想在设备上运行通用推理，开放的大语言模型在过去一年中也越来越受欢迎，尽管由于性能和内存挑战，它们不适合生产。”

其中包括 Falcon 1B（13 亿参数）、Flan-T5（27 亿参数）、StableLM 3B（28 亿参数）和 Llama 2B（25 亿参数）。Google 还将支持其开源 Gemma LLM 的 70 亿参数模型。

## Google 自有工具

开发者可以通过 Edge AI SDK 将 Nano AI 集成到应用程序和开发中。SDK 提供高级 API、管道、模型推理和硬件挂钩，以高效运行 AI 模型。

移动设备在计算能力、带宽和内存方面受到限制。开发者可以通过访问名为 AICore 的系统服务来微调模型，该服务集成在运行在合格设备（例如 Pixel 8A 和三星的 S24）上的 Android 14 中。

开发者可以使用量化来优化移动设备的模型，以减少模型大小和处理要求。

LoRA 被认为是将 AI 微调到设备和应用程序的重要组成部分。
### 正确的 Markdown 格式

**张哲浩** ([https://www.linkedin.com/in/zhehaozhang1997/](https://www.linkedin.com/in/zhehaozhang1997/))，谷歌的开发者关系工程师。

AICore 还包括一个名为低秩自适应 (LoRA) 的微调层，它允许应用开发者自定义模型以执行特定任务。LoRA 被认为是将 AI 微调到设备和应用的重要构建模块。

谷歌软件工程师 **王淼** ([https://www.linkedin.com/in/miao-wang-108b072b/](https://www.linkedin.com/in/miao-wang-108b072b/)) 表示：“应用可以训练自己的专门 LoRA 微调模块，以优化 Gemini Nano 模型的性能。”

## 支持开源 LLM

MediaPipe 是一个关键的 API，允许开发者使用多个开源 LLM（包括 Falcon 和 Gemma）创建设备上 AI 应用。

开发者将依赖 MediaPipe API 为 Android 和 iOS 设备编写 AI 网页应用。

MediaPipe API 提供预优化模型，开发者必须引入权重才能运行设备上应用。它支持视觉、文本和音频应用。一些 LLM 擅长特定任务，而该 API 为开发者提供了选择其模型的灵活性。

开发者将依赖 MediaPipe API 为 Android 和 iOS 设备编写 AI 网页应用。Chrome 126（[处于测试阶段](https://developer.chrome.com/blog/chrome-126-beta)）集成了对低代码 API 的支持，该 API 将网页应用连接到 Nano 和开源 LLM。

谷歌 I/O 的核心机器学习首席软件工程师 **科马克·布里克** ([https://www.linkedin.com/in/cbrick/](https://www.linkedin.com/in/cbrick/)) 表示：“所有这些都在浏览器中完全本地运行，而且速度很快。这是因为它是通过 [WebGPU](https://thenewstack.io/google-talks-web-platform-os-integration-webgpu-and-more/) 在计算机的 GPU 上加速的。这使得它足够快，可以构建非常引人注目的完全本地网页应用。”

## TensorFlow Lite

谷歌还使用了 TensorFlow Lite 开发环境，它是 TensorFlow 机器学习框架的轻量级版本。TFLite 还包括一个工具包，用于将 TensorFlow 模型转换为可以在设备上运行的更紧凑的版本。

布里克表示：“你可以在现成的模型中找到模型，或在所选框架中训练模型。它将你的模型一步转换为 TensorFlow Lite。然后，你可以在 Android、网页和 iOS 上使用你的应用运行所有这些模型。”

上周，芯片制造商高通表示，开发者将能够使用其最新芯片将其 LLM 移植到智能手机上。

## 挑战

应用开发者正在争先恐后地利用他们所能利用的每一盎司处理能力，以提高其应用的效率。

新一代设备将拥有更强大的 AI 算力，这将提升设备上的 AI 大脑。

另一个挑战是将应用与合适的 AI 芯片相匹配。新一代设备将拥有更强大的 AI 算力，这将提升设备上的 AI 大脑。

戴尔产品管理总监 **扎克·诺斯基** ([https://www.linkedin.com/in/zach-noskey-86660951/](https://www.linkedin.com/in/zach-noskey-86660951/)) 表示，戴尔已经推出了搭载英特尔 NPU 的新 PC，但只有当开发者发现相关应用时，设备上的 AI 才会真正起飞。

开发者参与英特尔 [OpenVino](https://thenewstack.io/intel-openvino-brings-ai-inferencing-to-the-desktop/) 等工具非常重要，以推动行业发展。供应商还需要与开发者密切合作，做好应用准备工作，因为开发者可能不知道从哪里开始。

例如，OpenVino 为 Gimp 提供了一个英特尔 NPU 插件，以支持 Stability Diffusion 图像生成提示。

诺斯基表示：“这关乎在社区中继续启用它——这有点像过去几年 CPU 和 GPU 利用应用的速度一样。”

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)