<!--
# 掌控机器：特性标记结合人工智能
https://cdn.thenewstack.io/media/2023/09/63eceac9-launchdarkly-01-1024x680.png
Feature image from LaunchDarkly.
 -->

随着组织开始在产品中集成人工智能，他们将需要采用开关模型来提高效率，甚至在必要时完全关闭系统。

> 译自 [Controlling the Machines: Feature Flagging Meets AI](https://thenewstack.io/controlling-the-machines-feature-flagging-meets-ai/) 。

你是否想过，如果使用特性标记，许多电影情节本可以轻易解决？好吧，你可能没有 —— 但由于我大多时间都在研究团队如何利用特性标记推出新功能，这经常出现在我脑海。《终结者》系列电影就有6部，如果Cyberdyne仅仅对Skynet使用特性标记，他们可以随时关闭所有问题！我们可以在《黑客帝国》等十几部电影中看到同样的对应。

抛开电影不说，这些控制发布场景在技术领域有现实意义。人工智能正在引领软件创新时代的来临。从OpenAI和GPT-3开始，随着每周似乎都有新模型推出，发展迅猛。

我们见证GPT-3升级到3.5版，然后是GPT-4。我们看到GPT-4的32K模型问世，可以处理更大量的内容交互。我们也看到了Meta的Llama、Anthropic的Claude、谷歌的BARD等文本类人工智能的出现，仅仅是文本类模型的冰山一角。新的人工智能模型涌现，具有图像生成、增强、文档审阅等更多功能。

而且，在每个人工智能领域内，都会随着新功能的开发和训练推出更多版本。我不禁看到人工智能模型的软件生命周期与软件开发之间的相似之处。这些语言模型自己也有软件生命周期，随着增强被推送给用户。

每个供应商都有自己的测试计划，部分用户可以试用这些模型。产品管理和工程团队会评估这些新模型与旧模型的效果，判断是否可以正式发布。这些新模型发布流程，就像软件发布一样，发布之后还可能回滚模型。

## 语言模型即特性

从这个角度看，人工智能模型与特性标记和特性管理有明显关联。我们在[LaunchDarkly](https://launchdarkly.com/?utm_content=inline-mention)经常讨论如何控制用户体验，实现测试版发布或基于场景的目标用户发布等功能。这些概念直接适用于用户使用人工智能模型的方式。

例如，你可以让大多数用户只使用GPT-3.5基础版，高级用户可以用GPT-4，顶级用户可以访问支持更长文本的GPT-4-32K。这在特性标记中是基本操作。[OpenAI的Sam Altman甚至提出GPT-4中存在一个“终结开关”](https://www.businesstoday.in/technology/news/story/can-chatgpt-gpt-4-be-shut-down-with-one-switch-openai-founder-sam-altman-reveals-details-374056-2023-03-20)，如果情况失控可以关闭它，回到《终结者》的例子。

以下JavaScript代码展示了在[NextJS 13.4应用](https://github.com/codyde/gptmodel-demo-ld)中，选择加入和退出不同人工智能API的实现:

```js
const model = await ldClient.variation("aimodel"， jsonObject， 'gpt-3.5-turbo');

  let tokens;

  if (model === 'gpt-3.5-turbo') {
    tokens = 3000
  } else {
    tokens = 8000
  }
  
  const query = JSON.parse(req.body);
  // console.log(query.prompt)
  const response = await fetch(OPENAI_API_URL， {
    method: 'POST'，
    headers: {
      'Content-Type': 'application/json'，
      Authorization: `Bearer ${OPENAI_API_KEY}`
    }，
    body: JSON.stringify({
      messages: [{"role": "user"， "content": query.prompt}]，
      model: model，
      temperature: 0.7，
      max_tokens: tokens，
      top_p: 1，
      frequency_penalty: 0，
      presence_penalty: 0
    })
  });
```

这里我们从LaunchDarkly特性标记获取模型，根据模型决定使用的token数量，然后将模型提供给OpenAI API调用。这是使用OpenAI API的示例，同样的概念也适用于Vercel的AI包，可以更流畅地在不同人工智能模型之间切换。

在应用里，登录后可以选择加入新模型或退出回到默认模型。

## 评估模型

随着这些模型越来越成熟，我们需要更多方法来评估不同供应商和类型模型的效果。我们需要考虑:

- 模型需要多长时间返回有效响应？
- 模型返回正确信息的频率比返回[无意义](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence))内容的频率高吗？
- 如何通过数据可视化来辅助我们理解哪种模型在什么场景下更合适？
- 如果想让50%用户试用新模型进行评估，该怎么做？

软件一直在不断演进，这在我们行业已成定律。但有趣的是它仍遵循同样的基本原则。软件交付生命周期依然存在。代码被部署到运行环境，发布给用户使用。在这一点上，人工智能也与软件无异。

随着语言模型被越来越多供应商应用，如持续集成、特性标记、软件发布等概念与人工智能的结合会越来越频繁。组织将人工智能整合到产品中，最后还要能切换模型以获得更高效率，这将是软件行业需要采用的实践。

在[LaunchDarkly Galaxy 23](https://launchdarkly.com/galaxy)用户大会上，我将通过示例演示这些概念，使用LaunchDarkly控制应用中的人工智能可用性。这将是一个聚焦实践的课程，展示模型在产品中的实时应用。希望我们能建立坚实基础，在掌控机器和防止机器失控方面做得更好。至少，我会展示如何编写一个[终止开关](https://launchdarkly.com/blog/what-is-a-kill-switch-software-development/)。
