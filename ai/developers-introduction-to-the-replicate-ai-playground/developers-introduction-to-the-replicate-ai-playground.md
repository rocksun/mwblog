
<!--
title: 开发者Replicate AI Playground介绍
cover: https://cdn.thenewstack.io/media/2025/01/04e22e8b-zdenek-machacek-9o9nkvr8c6y-unsplashb.jpg
-->

Replicate 让开发者以可控的方式探索 AI 模型，同时让你与后端流程和代码保持连接。

> 译自 [Developer’s Introduction to the Replicate AI Playground](https://thenewstack.io/developers-introduction-to-the-replicate-ai-playground/)，作者 David Eastman。

目前，在 LLM 领域中，下一步该关注什么存在着一个旋转的漩涡。开发者应该使用现有模型、扩展现有模型，还是从头开始创建这些模型？在更新了我关于[使用 Ollama 的本地模型](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/)的文章后，我决定转而研究一个基于云的框架。

[Replicate](https://thenewstack.io/simplify-ai-development-with-machine-learning-containers/) 是一个云平台，允许用户轻松运行和微调各种开源 AI 模型。他们声称有大约 20,000 个开源模型可用，包括（不可避免地）DeepSeek。但是，使用这些模型的过程是什么呢？

首先，我们需要加入 Replicate，并可能投入一些资金来运行模型。我注意到有一个 [playground](https://replicate.com/playground)，所以我将直接进入它。对于表明一个框架正试图使其自身易于访问而言，Playground 几乎总是一个[好兆头](https://thenewstack.io/playgrounds-for-developers-uses-and-design-patterns/)。

与越来越常见的情况一样，您只能使用 GitHub 登录：

![](https://cdn.thenewstack.io/media/2025/01/6fe8b406-image-1024x428.png)

鉴于我们正在使用云模型，下一个重要的事情是支出控制：

![](https://cdn.thenewstack.io/media/2025/01/899f3fc3-image-1-1024x615.png)

如果没有上述内容，评估成本将更加困难。但是，如果您仔细阅读，您仍然可能会被少量超额收费。这不太可能超过一杯咖啡的价格；但是，他们应该允许一次性预付信用额度，而不是每月支出限制。

Playground（目前是 beta 版）似乎更偏向于图像和视频创建——而这些实际上是最难实验的东西。

![](https://cdn.thenewstack.io/media/2025/01/9863c3c8-image-2-827x1024.png)

甚至考虑到移动设备这一事实告诉你事情发展有多迅速。

所以，正如我们被邀请做的那样，让我们开始吧。大约有 20 个视频和图像模型可供选择，默认选择以下模型：

![](https://cdn.thenewstack.io/media/2025/01/a404f4db-image-3.png)

我们都见过很多文本到图像的解决方案，所以视频很有趣。

由于某种原因，我要求制作一个海豚堆叠箱子的视频。我们可以选择视频的高度和宽度（最大 1280 像素）。您还可以选择帧数（最多 200 帧）。我对默认的 129 帧感到满意。

您可以选择 1 到 10 之间的去噪级别。在较高的值下，它会变得更具想象力，忽略原始图像。（扩散模型通过逐渐细化基于噪声的图像来生成图像）。最后，我们可以控制每秒帧数 (fps)，默认为 24。相比之下，游戏喜欢以大约 60 fps 的速度运行以使其看起来流畅。

所有这些都可以表示为以下 Python 查询：

```python
import replicate

output = replicate.run(
    "tencent/hunyuan-video",
    input={
        "embedded_guidance_scale": 6,
        "fps": 24,
        "height": 480,
        "infer_steps": 50,
        "prompt": "A dolphin stacking crates",
        "video_length": 129,
        "width": 864
    }
)

print(output)
```

当我们要求运行模型时，我们会得到一个旋转的图标，但除此之外，没有其他指示。我得到了创建时间和“starting”状态。但没有别的。实际上，该请求已“排队”。

但是，当我深入研究“full prediction”时，我得到了我想要的一切：

![](https://cdn.thenewstack.io/media/2025/01/c7d80f64-image-4-1024x549.png)

我们看到了服务器通信日志和完成百分比滑块。最后，我得到了 5 秒钟的海豚在一些蓝色箱子上玩耍的视频。鉴于海豚没有相对的拇指，这是一个很好的表现。

![](https://cdn.thenewstack.io/media/2025/01/09c7e6a1-image-5-1024x572.png)

当然，虽然不是免费的，但这并没有超出预算，

![](https://cdn.thenewstack.io/media/2025/01/3861cac6-image-6-1024x333.png)

最终的 JSON 输出具有指导意义且结构良好：

```json
{
  "completed_at": "2025-01-30T15:46:02.616901Z",
  "created_at": "2025-01-30T15:38:40.721000Z",
  "data_removed": false,
  "error": null,
  "id": "mpnsqxjat5rme0cmpzesjjnhrr",
  "input": {
    "fps": 24,
    "width": 864,
    "height": 480,
    "prompt": "A dolphin stacking crates",
    "infer_steps": 50,
    "video_length": 129,
    "embedded_guidance_scale": 6
  },
  "logs": "[Cut for length]",
  "metrics": {
    "predict_time": 123.354543706,
    "total_time": 441.895901
  },
  "output": "https://replicate.delivery/xezq/MJwQYO6neiVZXSqvxR9ZGuH4JBUepizHJOrrxFsfAcH0FqUoA/output_48685.mp4",
  "started_at": "2025-01-30T15:43:59.262358Z",
  "status": "succeeded",
  "urls": {
    "stream": "https://stream.replicate.com/v1/files/bsvm-mwhlz4a7gckbdbosoa4kzxebkplhhoq3ji57bbe7q34tt4qceimq",
    "get": "https://api.replicate.com/v1/predictions/mpnsqxjat5rme0cmpzesjjnhrr",
    "cancel": "https://api.replicate.com/v1/predictions/mpnsqxjat5rme0cmpzesjjnhrr/cancel"
  },
  "version": "6c9132aee14409cd6568d030453f1ba50f5f3412b844fe67f78a9eb62d55664f"
}
```

请注意，该作业有一个关联的 ID，这就是它在 UI 中被引用的方式。

但重要的是，我们可以在制作模型后自由地调整它。我只需在调整运行中要求提供橙色箱。现在，有趣的是现在将完成多少工作以及成本是多少。我们被告知这个模型现在是不同的版本。

这个过程确实更短，耗时两分钟：

![](https://cdn.thenewstack.io/media/2025/01/0e48ea78-image-7-1024x589.png)

完成的 JSON 更准确地说明了所花费的时间：

```json
{
  "completed_at": "2025-01-31T14:05:41.469428Z",
  "created_at": "2025-01-31T14:01:32.512000Z",
  ...
  "started_at": "2025-01-31T14:03:38.143858Z",
  ...
}
```

我认为“started”和“created”之间的区别在于你的查询何时从队列中取出并开始处理。像 [Midjourney](http://midjourney.com) 这样的服务会给你一定的“优先级”时间，这可能是一种揭示这方面神秘性的方法。
虽然视频中的海豚确实剪切了箱子，而且箱子看起来有点奇怪，但基本功能似乎已经奏效。我的查询非常基本。

查看账单，费用与之前大致相同：

![](https://cdn.thenewstack.io/media/2025/01/6976e853-image-8-1024x281.png)

事实上，他们在花费第一个美元后很快就给我发了电子邮件，这很明智。

## 结论

我将自己限制在 playground 中，它目前是 beta 版本，但 Replicate 显示出它是一个相当复杂的系统。我喜欢它向你展示了如何将你在表单上提出的任何请求转换为 Python 或 Node 等。REST 风格的 JSON 输出以及指向输出的链接看起来很全面。

目前，一些定义还不是很清楚（比如“tweaking”是否是“tuning”，究竟是什么被版本化了，以及一个版本和另一个版本之间的关系），我希望他们所有的多模态模型最终都能进入 playground。如果他们保持警惕，那么我怀疑让最终用户了解成本是可以的——但固定信用额度仍然是明智的。

这里的优势在于，你可以以可控的方式探索如此多的模型，同时保持开发人员与后端流程和代码的连接。
