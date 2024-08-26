# Google 推出云端 GPU 并提供开源大型语言模型

![Google 推出云端 GPU 并提供开源大型语言模型的精选图片](https://cdn.thenewstack.io/media/2024/08/172dd2cf-george-c-hsyq2hk91lo-unsplash-1-1024x576.jpg)

如果您是开源 AI 的忠实粉丝，但没有足够的计算能力在本地运行 AI 模型，Google 可以为您提供支持（但需要付费）。

该公司正在将其云服务中引入 Nvidia 的 L4 GPU。L4 GPU 是 H100 GPU 的轻量级版本，Meta 的 Llama 3.1 和 OpenAI 的 GPT-4o 模型就是用 H100 GPU 训练的。

开发人员可以登录 Google 的 [Cloud Run](https://cloud.google.com/run?hl=en#build-applications-or-websites-quickly-on-a-fully-managed-platform)，将 Ollama 加载到容器中，启动[开源大型语言模型](https://thenewstack.io/linux-foundation-backs-open-source-llm-initiative/)（例如 Google 的 Gemma 2 或 Meta 的 Llama 3.1），指向 L4 GPU，然后开始进行推理。具体说明如下。

## 最终服务于开源社区

Google 终于有了一个完整的硬件和软件包，开源开发人员可以使用它从开源模型创建应用程序。

开发人员可以完全控制前端和后端，并且可以通过 Cloud Run 指向 Google Cloud 中的 L4 硬件。

到目前为止，Cloud Run 服务仅限于 Google 的专有模型，包括 Gemini 1.0 LLM、用于图像生成的 Imagen 以及用于多模态模型的 Gemini 1.5 Flash。

Cloud Run 现在拥有 Gemma 2（Gemini 的开源版本）和 Llama 3.1。L4 GPU 也是新增功能，可用于对开源模型进行推理。

亚马逊的 Bedrock 提供了各种封闭和开源大型语言模型。它在其 [EC2 G6 实例](https://aws.amazon.com/ec2/instance-types/g6/) 中提供了 L4 芯片和较旧的 AMD x86 芯片。由于兼容性问题，亚马逊仍然没有将 GPU 与其自主研发的 Graviton 芯片配对。

与此同时，微软围绕 OpenAI 的专有 LLM 和 Nvidia 的 GPU（拥有其专有的 [CUDA 开发堆栈](https://thenewstack.io/nvidia-wants-to-rewrite-the-software-development-stack/)）制定了 AI 战略。

## 在 PC 上本地运行大型语言模型的替代方案

Google 的产品是在 [PC 上本地加载 Ollama 和运行大型语言模型](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) 的漫长过程的替代方案。Google 的 Cloud Run 将在 30 秒内加载大型语言模型和 Ollama。

在大多数情况下，大多数 PC 没有在大型上下文窗口内运行大型语言模型所需的 GPU。LM Studio 等应用程序使下载大型语言模型成为可能（该软件会显示这些大型语言模型是否可以在本地 GPU 上运行），但这仍然需要时间。

Cloud Run 上提供的最新模型包括 90 亿参数的 Gemma 2 和 80 亿参数的 Llama 3.1。其他可用模型包括 130 亿参数的 Llama 2 和 20 亿参数的 Gemma。

Google 表示，配备 L4 GPU 的 Cloud Run 实例将在约 5 秒内加载，之后还需要几秒钟才能使用 Ollama 初始化框架和模型。整个大型语言模型（大小高达 7.4GB）将在几秒钟内下载并启动。

最小的 20 亿参数 Gemma 模型需要 11 到 17 秒，而最新的 90 亿参数 Gemma 2 需要 25 到 30 秒。80 亿参数的 Llama 3.1 需要 15 到 21 秒才能加载。

Cloud Run GPU 目前仅在 Google 的 us-central1（爱荷华州）地区提供，并将在今年年底前在欧洲和亚洲地区推出。

“我们将来可能会提供更多 GPU 选项并扩展到更多地区，”Google 在一封电子邮件中表示。

## 说明

Google 已经对其专有的 Gemini 模型进行了训练，使其能够在其 [TPU](https://thenewstack.io/train-and-deploy-tensorflow-models-optimized-for-google-edge-tpu/) 上运行，但构建了可下载的开源 Gemma，使其能够在商用硬件上运行。笔记本电脑将没有 TPU。

Google 在此产品方面获得了 Ollama 的帮助。开发人员需要指向大型语言模型和硬件。

Google 建议首先使用以下 Dockerfile 创建一个包含 Ollama 和模型的容器镜像：

```dockerfile
FROM ollama/ollama
ENV HOME /root
WORKDIR /
RUN ollama serve & sleep 10 && ollama pull gemma2
ENTRYPOINT ["ollama","serve"] 
```

然后使用以下命令进行部署：

```bash
gcloud beta run deploy --source . --port 11434 --no-cpu-throttling --cpu 8 --memory 32Gi --gpu 1 --gpu-type=nvidia-l4
```

`--gpu` 标志需要在命令行中指定 GPU 的数量，`--gpu-type` 标志需要指定 GPU 的类型。Google 表示，这也可以在 Google Console 中完成。

## 定价

Google 尚未公布在 L4 GPU 上运行开源 Llama 和 Gemma 模型的价格。但是，可以在 [Cloud Run 定价页面和计算器](https://cloud.google.com/run/pricing) 上计算出使用 L4 GPU 的成本。
如果时间就是金钱，而你又没有本地处理能力，那么 L4 可能是最便宜的 GPU。但如果你投资了一台配备顶级 GPU 的笔记本电脑，并且可以等待 10 到 20 分钟来下载、修改和加载 LLM，那就坚持下去。

## 谷歌的 AI 发展历程

谷歌用其诱饵式 AI 策略考验了开源社区的耐心。最初的 API 产品是免费的，很好地体现了其开源精神，直到它开始向开发者收取使用其工具的费用。

开发者以前借用 Google Colab 上可用的硬件来运行推理。这就像使用 Python 脚本的 Jupyter 笔记本一样简单，选择硬件（CPU、GPU 或 TPU），然后运行视频、图像、文本或语音 AI 应用程序。免费套餐仅供研究人员使用，因此从技术上讲，开发者滥用了它。

但 Google Colab 最终取消了对各种 GPU 的免费访问权限。大多数应用程序无法利用 Google 的 TPU，只能默认使用速度极慢的 CPU。Colab 现在提供的唯一 GPU 是 Nvidia 的 T4，它已经使用了将近八年。

谷歌严重依赖研究和开源社区来开发其 AI 产品，但后来却要求同一个社区付费使用其模型。

谷歌在 4 月份对开发者社区进行了全面调整，将其 AI 开发工具货币化，令开发者社区感到意外。

该公司限制了对其专有的 Google Gemini 模型的免费访问，并 [推出](https://ai.google.dev/pricing) 了按需付费模式。这惹恼了在 Gemini 上创建 AI 应用程序的开发者，因为他们现在必须付费。

谷歌面临着将其 AI 产品货币化的市场压力。它还必须支付为服务 AI 应用程序而投资数十亿美元建设数据中心的成本。

谷歌严重依赖研究和开源社区来开发其 AI 产品，但后来却要求同一个社区付费使用其模型。但这家公司——开源的坚定拥护者——将 Gemma 和 Gemma 2 LLM 吹捧为其对开源社区的贡献。

借助 Nvidia 的 L4 GPU，谷歌还提供了相对更实惠的硬件访问来运行 AI。性能快的 GPU 很难找到，而且非常昂贵，因此 L4 填补了这一空白。

谷歌最近发布了其自主研发的 AI 芯片 Trillium，该芯片专用于训练和要求苛刻的推理工作负载。Trillium 是继 TPUv5 系列之后的第六代 AI 芯片。

苹果公司在其 Google TPUv4 和 TPUv5 芯片上训练了其在 Apple Intelligence 中使用的自主研发 AI 模型。开发者可以通过 Google Colab 访问 TPUv4。

---

**YOUTUBE.COM/THENEWSTACK**

技术发展日新月异，请勿错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、采访、演示等内容。

[订阅](https://youtube.com/thenewstack?sub_confirmation=1)