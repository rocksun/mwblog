## 如何通过开源项目 LocalAI 运行本地 LLM

![如何通过开源项目 LocalAI 运行本地 LLM 的特色图片](https://cdn.thenewstack.io/media/2024/04/643fba12-erik-mclean-ox72sudwbea-unsplash-1024x683.jpg)

今年早些时候，我写了一篇关于 [如何使用 Ollama 和 Llama 2 设置并运行本地 LLM](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) 的文章。在本文中，我将探讨在本地运行大型语言模型的另一种选择。虽然 Ollama 是一家私营公司，但 [LocalAI](http://Localai.io) 是一个社区维护的开源项目。

从表面上看，它们各自为用户提供了一些略有不同的东西。从 Ollama，我实际上得到了一个带有 LLM 的平台供我使用。但是，LocalAI 提供了对 OpenAI 的 API 的替代方案。实际上，这意味着我可以使用 OpenAI URI，但只需指向容器即可。

另一个不同之处在于这两个产品如何处理容器。LocalAI 利用 Docker——这是它的主要方法——但它还允许你手动构建容器或二进制文件。Ollama 建议使用 Docker 来获得 GPU 加速，但除此之外还可以不使用它。

让我们开始吧。请注意，我在我的 Mac 上安装了 Docker Desktop。

LocalAI 提供了一个类似于 Ollama 提供的全包 (AIO) 设置。这是明智的，因为我可以在需要的时候进行专门化，同时从一个完整的设置开始。

我打开了我的 [Warp 命令行](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/)，并从文档中运行了下面的 docker 提示。我将以适中的速度进行本教程，但我确实假设读者 [熟悉 Docker](https://thenewstack.io/tutorial-create-a-docker-image-from-a-running-container/)。我让它去拉取，正如你所看到的，它花了一个小时左右：

完成后，你可以看到它通过 AIO 包提供的模型服务：

更明确地说，对 curl http://localhost:8080/v1/models 的响应如下：

```
1
2
3
4
5
6
7
8
9
|
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

文档在这里让你有点不知所措，但幸运的是，在图像经过验证时，测试 curl 在最终消息中给出了第一步：

值得注意的是，我停止并启动了安装几次，并且在我在 Docker 桌面中重新启动容器时捕获了上述消息。Docker Desktop 和 Warp 都具有足够好的日志处理功能，允许你稍后仔细查看这些消息。文档中还有类似的测试。

这是我尝试过的测试，因为正如我提到的，LocalAI 是 OpenAI 的替代方案。我们知道 [温度意味着什么](https://thenewstack.io/what-temperature-means-in-natural-language-processing-and-ai/)，并且我在第一次查看 [AI 包装器](https://thenewstack.io/the-promise-of-riches-from-ai-wrappers/) 时使用 JSON 有效负载执行了类似的 curl。请注意，模型名称与聊天界面模型不同。

由于错误，我无法让聊天客户端工作（稍后会详细介绍），但我使用 Docker 消息中给我的类似 curl 示例测试了图像识别服务：

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
|
curl http://localhost:8080/v1/chat/completions -H "Content-Type: application/json"
-d '{
"model": "gpt-4-vision-preview",
"messages": [
{"role":"user",
"content": [
{ "type":"text",
"text": "图片里有什么？"
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
"content":"图片中有一条木制人行道或木板路，周围环绕着茂盛的草地和绿叶，营造出一种宁静而风景如画的场景。"
}
}
],
"usage":{"prompt_tokens":0,"completion_tokens":0,"total_tokens":0}}%
```

容器日志证实一切正常：

```
1
|
2024-04-02 14:16:53 1:16PM INF 加载模型 'bakllava.gguf'，后端为 llama-cpp
```

在我的 Apple Silicon 2015 MacBook Pro 之前，这花了 12 分钟。
**图片描述：**

图片中有一条木制人行道或木板路，周围环绕着茂盛的草地和绿叶，营造出宁静而如画的场景。

**测试图像描述：**

* 温度：0.9
* 描述：茂盛、宁静、如画

**简化描述：**

* 温度：0.1
* 描述：图片中有一条木制小路或木板路，周围环绕着高高的草、花朵和杂草。木板路似乎位于一片大草原或大草原的中央。

**转录服务界面：**

* 输入：著名的悲痛演讲
* 输出：冗长的答复，使用引号标记引文

**Docker 中的模型加载：**

```
2024-04-02 15:39:51 2:39PM INF 加载模型 'ggml-whisper-base.bin'，后端为 whisper
```

**LocalAI 与 Ollama 的比较：**

* LocalAI 提供更直接的模型访问，但错误处理需要改进。
* Ollama 提供更简单的体验，但功能较少。

**YouTube 订阅链接：**

[https://youtube.com/thenewstack?sub_confirmation=1](https://youtube.com/thenewstack?sub_confirmation=1)