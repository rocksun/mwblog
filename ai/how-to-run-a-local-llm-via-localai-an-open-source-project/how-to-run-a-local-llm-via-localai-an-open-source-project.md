
<!--
title: 如何通过开源项目 LocalAI 运行本地 LLM
cover: https://cdn.thenewstack.io/media/2024/04/643fba12-erik-mclean-ox72sudwbea-unsplash.jpg
-->

我们研究了一种开源方法，用于在本地运行大型语言模型。LocalAI 是私有公司 Ollama 的替代品。

> 译自 [How to Run a Local LLM via LocalAI, an Open Source Project](https://thenewstack.io/how-to-run-a-local-llm-via-localai-an-open-source-project/)，作者 David Eastman。

今年早些时候，我写了一篇关于 [如何使用 Ollama 和 Llama 2 设置并运行本地 LLM](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) 的文章。在本文中，我将探讨在本地运行大型语言模型的另一种选择。虽然 Ollama 是一家私营公司，但 [LocalAI](http://Localai.io) 是一个社区维护的开源项目。

从表面上看，它们各自为用户提供了一些略有不同的东西。从 Ollama，我实际上得到了一个带有 LLM 的平台供我使用。但是，LocalAI 提供了对 OpenAI 的 API 的替代方案。实际上，这意味着我可以使用 OpenAI URI，但只需指向容器即可。

另一个不同之处在于这两个产品如何处理容器。LocalAI 利用 Docker——这是它的主要方法——但它还允许你手动构建容器或二进制文件。Ollama 建议使用 Docker 来获得 GPU 加速，但除此之外还可以不使用它。

让我们开始吧。请注意，我在我的 Mac 上安装了 Docker Desktop。

LocalAI 提供了一个类似于 Ollama 提供的全包 (AIO) 设置。这是明智的，因为我可以在需要的时候进行专门化，同时从一个完整的设置开始。

我打开了我的 [Warp 命令行](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/)，并从文档中运行了下面的 docker 提示。我将以适中的速度进行本教程，但我确实假设读者 [熟悉 Docker](https://thenewstack.io/tutorial-create-a-docker-image-from-a-running-container/)。我让它去拉取，正如你所看到的，它花了一个小时左右：

![](https://cdn.thenewstack.io/media/2024/04/c0f38f36-untitled-1024x186.png)

完成后，你可以看到它通过 AIO 包提供的模型服务：

![](https://cdn.thenewstack.io/media/2024/04/dba814ed-untitled-1-1024x291.png)

更明确地说，对 curl http://localhost:8080/v1/models 的响应如下：

```
{"object":"list","data":[
{"id":"text-embedding-ada-002","object":"model"},
{"id":"whisper-1","object":"model"},
{"id":"stablediffusion","object":"model"},
{"id":"gpt-4-vision-preview","object":"model"},
{"id":"tts-1","object":"model"},{"id":"gpt-4","object":"model"},
{"id":"MODEL_CARD","object":"model"},
{"id":"bakllava-mmproj.gguf","object":"model"},
{"id":"voice-en-us-amy-low.tar.gz","object":"model"}]}
```

模型卡是一个元数据容器。

在 Docker 桌面中转动控制杆使我们开始运行：

![](https://cdn.thenewstack.io/media/2024/04/8d40d747-untitled-2-1024x125.png)

这个文档确实让你在这里有点独立行动的空间，但幸运的是，随着镜像通过了验证，最终消息中的测试 curl 提供了第一步的指引。

![](https://cdn.thenewstack.io/media/2024/04/87841a6b-untitled-3-1024x502.png)

值得注意的是，我停止并启动了安装几次，并且在我在 Docker 桌面中重新启动容器时捕获了上述消息。Docker Desktop 和 Warp 都具有足够好的日志处理功能，允许你稍后仔细查看这些消息。文档中还有类似的测试。

这是我尝试过的测试，因为正如我提到的，LocalAI 是 OpenAI 的替代方案。我们知道 [温度意味着什么](https://thenewstack.io/what-temperature-means-in-natural-language-processing-and-ai/)，并且我在第一次查看 [AI 包装器](https://thenewstack.io/the-promise-of-riches-from-ai-wrappers/) 时使用 JSON 有效负载执行了类似的 curl。请注意，模型名称与聊天界面模型不同。

由于错误，我无法让聊天客户端工作（稍后会详细介绍），但我使用 Docker 消息中给我的类似 curl 示例测试了镜像识别服务：

```bash
curl http://localhost:8080/v1/chat/completions -H "Content-Type: application/json" 
-d '{ 
  "model": "gpt-4-vision-preview", 
  "messages": [ 
    {"role":"user", 
     "content": [ 
      { "type":"text", 
        "text": "What is in the image?"
      }, 
      { "type": "image_url", 
        "image_url": {"url":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"} 
      } 
     ], 
    "temperature": 0.9 
   } 
  ] 
}' 
 
>>response
 
{
 "created":1711995490, 
 "object":"chat.completion", 
 "id":"f78380ca-fbcd-455f-9834-ddffcefd6b03", 
 "model":"gpt-4-vision-preview", 
 "choices":
  [
   {"index":0,
    "finish_reason":"stop",
    "message":
    {"role":"assistant",
     "content":"The image features a wooden walkway or boardwalk that is surrounded by lush grass and green foliage, creating a serene and picturesque scene."
    }
   }
  ],
  "usage":{"prompt_tokens":0,"completion_tokens":0,"total_tokens":0}}%
```

容器日志证实一切正常：

```
2024-04-02 14:16:53 1:16PM INF 加载模型 'bakllava.gguf'，后端为 llama-cpp
```

在我的 Apple Silicon 2015 MacBook Pro 之前，这花了 12 分钟。

> “The image features a wooden walkway or boardwalk that is surrounded by lush grass and green foliage, creating a serene and picturesque scene.” Here is the test image being described:

![](https://cdn.thenewstack.io/media/2024/04/a8813c7a-untitled-5-1024x667-1.jpg)

响应文本需要相当高的温度 (0.9) 才能产生叙事质量（即使用“繁茂”、“宁静”、“风景如画”）。大型语言模型的优势在于它们显然能够“智能地”根据主题进行发挥，并使用其他来源。但结果是好的。

为了测试模型和理论，让我们将温度改成 (0.1) 来确认我们得到了更简洁的描述。我们做到了：“图像中有一条木制小径或木板路，周围环绕着高草、鲜花和杂草。这条木板路似乎位于一个大田野或大草原的中央”。

完美，只陈述了事实。这花了 26 分钟！

虽然它不能很好地用于复制，但我还尝试了转录服务接口，而且它运行很快。我下载了一段著名的庄严演讲：

![](https://cdn.thenewstack.io/media/2024/04/c6653939-untitled-6-1024x110.png)

随后我把请求发送给该模型，并得到了冗长的回复：

![](https://cdn.thenewstack.io/media/2024/04/c55797e0-untitled-7-1024x253.png)

在 Docker 内部，我们可以看到启动了哪些操作：

```
2024-04-02 15:39:51 2:39PM INF Loading model 'ggml-whisper-base.bin' with backend whisper
```

全文按照末尾片段结合：

![](https://cdn.thenewstack.io/media/2024/04/cdb2d720-untitled-8-1024x444.png)

我对算法知之甚少，所以我无法评论少数未分离的词语，但文本中使用引号来表示引文给我留下了深刻的印象。但是，我们不是在这里详细考虑模型本身。

LocalAI并没有为用户提供一个真正的平台，这在错误出现时需要完全的开发者正确性来跟进反映出来。因为有更多的选项(一体机、GPU 处理等)以及像我这样使用旧规格机器的人，维护者全力确保用户体验质量的同时也有很多事要做。如果出现错误，有手动构建模型的说明 - 如果你期望长期使用这个项目,这是一条合理的路径。

我试图将本文的一部分作为 Ollama 和 LocalAI 在我低规格 MacBook 上并肩比较的一部分，但随着该领域的扩展，用户可以期待更多样化的选择。虽然现在有点粗糙，但 LocalAI 提供了更直接的途径来构建模型，并让你更接近系统。对于那些需要一次性、更简单体验的人来说，Ollama 可能更适合你。当你深入研究在工作流程中放置模型时，LocalAI 将提供更透明的选项来使用——前提是错误处理更有效。