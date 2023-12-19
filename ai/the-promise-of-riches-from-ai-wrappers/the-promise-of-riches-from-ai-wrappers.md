<!--
title: AI封装工具蕴藏丰厚商机
cover: https://cdn.thenewstack.io/media/2023/12/fb7aefb8-ai_wrappers2-1024x575.jpg
-->

David Eastman受YouTube上介绍AI副业的视频启发，演示了如何基于OpenAI API开发AI封装应用。

> 译自 [The Promise of Riches from AI Wrappers](https://thenewstack.io/the-promise-of-riches-from-ai-wrappers/)，作者 David Eastman 一直是伦敦的专业软件开发人员，曾在甲骨文公司和英国电信任职，也是一个顾问，帮助团队以更敏捷的方式工作。他写了一本关于用户界面设计的书，从那时起一直在撰写技术文章......

无论您决定观看什么，YouTube 最终会在您的订阅源中放入一个标题中包含夸大声明的视频。就像马戏团的广告员一样，他们宣布视频涵盖的惊人事物，只是随着视频的进行这些都被淡化了。一个吸引了我注意力的标题大声喊道“**人工智能应用每月产生2万美元以上收入，只需要1人团队。**”如果忽略无法证实的收入数字，这个视频是相当理性的，指出大多数的想法只是人工智能的封装，开始并不需要太多工作。我将在下面看一些特色网站。

尽管与这篇文章的目标受众完全不同，但我确实同意人工智能为满足特定需求的应用提供了新的机遇。如果您是一个开发者或者一个小型开发团队，使用人工智能创建一个小型最简可行产品是个不错的主意——不管是用于一次临时项目还是解决您组织内部的问题。我感觉到15年前初创公司的技术风潮再次升温，[人工智能也许正处于从“兴奋”向“实际部署”转变的2024年](https://www.goldmansachs.com/intelligence/pages/ai-poised-to-begin-shifting-from-excitement-to-deployment-in-2024.html)。尽管抓住大好机会获得丰厚回报并非不可能，但我会鼓励您满足于抓住契机并实践推出一个产品。如果您突然产生雄心壮志要做点事，可以从“副业”开始。

尽管企业家精神在于发现市场中的空白并在大公司注意到并发布免费版本之前将其开发利用，但有美德的开发者应该关注客户体验。好，让我们从开始讲起。

## 那么什么是人工智能封装？

人工智能应用程序构建在什么之上或包装了什么？它是对中间商大型语言模型(LLM)的基本API调用。要获得基本的API体验，我们不需要任何代码:

1. 加入OpenAI。这现在是人工智能界的麦当劳，所以我们从这里开始。
2. 创建一个[API密钥](https://platform.openai.com/api-keys)。这可以标识您和您的请求。我在下面的示例查询中使用了一个明显错误的密钥xx-xxxxXX。

![](https://cdn.thenewstack.io/media/2023/12/3142b838-screenshot_2023-12-15_at_13.25.20-1024x425.png)

3. [支付](https://platform.openai.com/account/billing/overview)5美元就可以购买一些计算能力。我们不得不承认，萨姆·阿尔特曼最近至少提供了这么多[娱乐](https://thenewstack.io/pivot-ai-devs-move-to-switch-llms-reduce-openai-dependency/)。
4. 打开终端(即命令行)。我使用 [Warp](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) 作为我的终端，所以很容易将命令与响应分开。使用[OpenAI提供的curl命令](https://platform.openai.com/docs/introduction)示例调用他们的基本GPT模型。这里是我的查询:

```bash
curl https://api.openai.com/v1/chat/completions
  -H "Content-Type: application/json"
  -H "Authorization: Bearer xx-xxxxXX"
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "What is TheNewStack?"}],
     "temperature": 0.7
   }'
```

把这个视为一个标准的REST调用，带有JSON载荷。重要的一点是将您长长的API密钥放在xx-xxxxXX的位置。如果您愿意，可以使用不同的 **model** ，但这可能会花费更多。请注意，我们的 **content** 是问题“What is TheNewStack?”。**temperature** 控制响应的创造力。我们想要一些生动的描述，但不要幻想。

5. 这是响应:

```json
{
  "id": "chatcmpl-8W2kkV9PHAycrcPPsIlJ1cusPignO",
  "object": "chat.completion",
  "created": 1702647770,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "TheNewStack is a technology media company that covers the latest trends and developments in the world of software, cloud computing, and infrastructure. They provide news, analysis, and in-depth articles on topics such as containers, microservices, DevOps, and emerging technologies. TheNewStack aims to provide insights and information to help businesses and developers navigate the rapidly evolving landscape of technology and make informed decisions."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 13,
    "completion_tokens": 79,
    "total_tokens": 92
  },
  "system_fingerprint": null
}
```

**prompt tokens** 不是问题中的字面单词数，而是与查询的分解方式有关。如您所见，答案是一个相当好的摘要。快速查看[使用情况](https://platform.openai.com/usage)可以看出，这花费了不到1分钱。如果查询错误，请仔细阅读错误代码。

## 广告语示例

现在我们已经了解了人工智能后端必须做的最少事情，让我们来看一些工作网站的示例。

首先是[公式机器人](https://formulabot.com/)，它可以帮助用户使用 Excel 公式——或者说是“由人工智能提供的公式生成”。你可能会争辩说，如果电子表格仍然难以使用，那么问题肯定出在该工具上，但这忽略了现实。电子表格无处不在，经常出现在完全不关心数字或公式的人手中。

简短注册后，它会提供一些测试市场表格数据来帮助您了解事情的工作原理。在查看测试数据并询问“哪种饮料产品获利最多？”后，一条绿线从左向右缓慢移动，最终得出正确答案。步骤被逐一显示，包括由于没有“必要的pandas”而失败的Python代码。为什么Python需要pandas这一点我不太清楚。

虽然远非流畅，但从注册到获得解决方案的时间很快。和往常一样，有各种升级选项可供付费产品。页面上甚至有一个正则表达式查找器——这表明页面已经扩展提供更多服务。

接下来是[PhotoAI](https://photoai.com/)，用于“在不使用相机的情况下创建漂亮的人工智能照片”。连续滚动的美丽人物画面——全部来自自拍——是一个完美的广告。然后是一个简单的图表，展示了如何使用4幅普通自拍生成背景酷炫的全身照。同样，它提到了视频生成——一旦吸引了观众，就可以销售更多产品。它还展示了一个异常诚实的广告；毫无疑问，情况确实如此。

![](https://cdn.thenewstack.io/media/2023/12/2b9e7c8d-untitled.png)

最后，我们有[PDF AI](https://pdf.ai/)。显然，域名“pdf.ai”花了1万美元，所以这确实强调了确保网站匹配用户预期的必要性，同时提醒我们成功的努力远非随意。所有示例都会紧密匹配网站域名和任务。

当您试图买房时，会有大量文件送到您面前；能够从中提取隐藏信息当然很有价值。在生活中会有许多时候，您可能需要在短时间内高度集中使用某种服务，较小的费用会没那么大问题。

## 开发人工智能应用程序的方法

如果您是经验丰富的开发人员，您可以直接将良好的习惯带入制作最小可行产品(MVP)。这可能更少是技术挑战，更多是常规训练的挑战。首先用手工测试步骤；从用户查询，将查询输入人工智能，并隔离响应。注意您看到的问题和答案的类型。

现在有很多人工智能平台助手，比如[Fixie](https://thenewstack.io/fixie-and-its-agent-approach-to-leveraging-llms/)，它们提供了直接使用我们上面用过的OpenAI API的替代方案。

当然，利用像[Stripe](https://thenewstack.io/the-state-of-apis-in-2021/)这样的解决方案从渴望的用户那里收集资金现在要简单得多。始终试图成立有限责任公司(取决于您所在地区的法律)，以在财务上隔离您的产品。

确保您可以使用代码将所需的API响应转换为用户HTML页面。使用您最熟悉的Web解决方案。对于大多数开发人员来说，这将是JavaScript驱动的，但如果您想直接避免使用JavaScript，可以使用[Blazer](https://thenewstack.io/web-app-development-sans-javascript-with-microsoft-blazor/)等开发工具。网站现在可以存在于您的笔记本电脑上。

一旦您在最简单的源代码控制中构建了本地版本和代码，您只需要尽可能地自动化。我的“[如何启动项目](https://thenewstack.io/how-to-start-a-software-project-a-guide-for-junior-devs/)”文章涵盖了这些主题的大部分。

尽快发布公共网站应该是您的第一个MVP的目标。从那时起，它就是不断迭代。您现在正在从内向外工作——不专注于您发布的内容，而是专注于其他人所看到并做出的反应，从而铺平客户体验之路。

如果您正在抓痒，您会发现像Reddit这样的地方，人们会问“我怎样才能......？”正是您用MVP回答的事情。从那时起，这就是营销工作的问题。如果您正在寻求财富，我祝您好运。

