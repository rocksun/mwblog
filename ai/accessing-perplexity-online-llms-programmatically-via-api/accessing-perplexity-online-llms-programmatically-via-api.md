<!--
title: 编程方式访问Perplexity在线LLM
cover: https://cdn.thenewstack.io/media/2024/01/8e691618-david-clode-qy9s1umfwcu-unsplash-1024x683.jpg
-->

Perplexity的在线LLM引领潮流，提供了超越今日最佳合作者和人工智能助手的新功能。

> 译自 [Accessing Perplexity Online LLMs Programmatically Via API](https://thenewstack.io/accessing-perplexity-online-llms-programmatically-via-api/)，作者 Janakiram MSV。




接下来的步骤是构建包含系统和用户角色的提示模板。用户角色将包含我们在前一步中初始化的提示。

```python
messages = [
    {
        "role": "system",
        "content": (
            "您是一位人工智能助手，需要进行一场有帮助、详细、礼貌的对话。"
        ),
    },
    {
        "role": "user",
        "content": (
            prompt
        ),
    },
]
```

我们准备调用API并检查响应。您可以使用与OpenAI ChatCompletion相同的API来访问该模型，通过将Perplexity的URI作为终端传递。

请注意，我们如何使用URL初始化客户端对象，并将模型标识符传递给ChatCompletion方法。

```python
client = OpenAI(api_key=API_KEY, base_url="https://api.perplexity.ai")
response = client.chat.completions.create(
    model=model,
    messages=messages
)
```

输出可以在response对象中轻松访问。有关详细信息，请参阅OpenAI Python SDK。

```python
print(response.choices[0].message.content)
```

Zoom

我得到的回答是基于2020年举办的世界杯！这是预期的，因为Llama 2无法访问实时数据。

现在，让我们尝试在Perplexity AI的在线LLM，pplx-7b-online上使用相同的提示。
```mark```mark