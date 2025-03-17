
<!--
title: 通过这个简单技巧节省宝贵的GenAI Token
cover: https://cdn.thenewstack.io/media/2025/02/73ad05dd-afif-ramdhasuma-f3dfvkj6q8i-unsplash-scaled.jpg
summary: GenAI提速省钱绝招！告别直接上传大数据，用Prompt描述数据集Schema，让LLM生成代码本地执行！巧用Hugging Face Transformers API和Gradio，轻松构建AI应用Web前端，省Tokens防泄露，数据分析效率翻倍！
-->

GenAI提速省钱绝招！告别直接上传大数据，用Prompt描述数据集Schema，让LLM生成代码本地执行！巧用Hugging Face Transformers API和Gradio，轻松构建AI应用Web前端，省Tokens防泄露，数据分析效率翻倍！

> 译自：[Save Valuable GenAI Tokens With This One Simple Trick](https://thenewstack.io/save-valuable-genai-tokens-with-this-one-simple-trick/)
> 
> 作者：Joab Jackson

基于大型语言模型 (LLM) 的生成式 AI 服务，例如 [OpenAI](https://thenewstack.io/mastering-openais-realtime-api-a-comprehensive-guide/) 或 [Google Gemini](https://thenewstack.io/langchain-and-google-gemini-api-for-ai-apps-a-quickstart-guide/)，在某些任务上比其他任务更擅长。正如技术专家和 Developer Learning Solutions 创始人 Wei-Meng Lee 在上个月的 [ACM TechTalk](https://learning.acm.org/techtalks) 中所建议的那样，该讲座题为“[Unlock Hugging Face: Simplify AI with Transformers, LLMs, RAG, Fine-Tuning](https://events.zoom.us/ejl/AtbpEvtDc01b-yUPPB-RaiihAQSHdBrcul8bHTodQV2r7oXeUA17~A7komXmHD5-MXZeq-cUisLaWcaK1FM78X-1R-_5eobD6Cv2W23-dEaZlWgpa7Nk0UbY-BXm29DpDGudU1R7O-HVzqQ12BNoDqOg/home)”。

例如，令人惊讶的是，LLM [不擅长执行分析任务](https://thenewstack.io/small-language-models-vs-llms-what-theyll-mean-for-businesses-in-2025/)。即使你想使用 LLM 来完成这项任务，考虑到你的数据集的大小，它的成本也可能高得令人望而却步。

假设你有一个包含 20 列和 500 万行的 CSV 文件。它可能包括交易记录以及客户数据。你想问一个问题，例如这个客户在某一天购买了什么。你这个月赚了多少钱？这对 LLM 来说是简单的工作吗？

“问题是，不是的，”Wei Meng 解释说。“LLM 非常不擅长分析任务。”

当然，LLM 非常擅长基于文本的问题，以及从大型非结构化文本中提取信息。然而，数值分析[仍然是一个挑战](https://guides.nyu.edu/c.php?g=1308742&p=9997824#)。

但是，有一种方法仍然可以使用 LLM 来完成此类任务。

## Tokens 和费用

用户提供的信息以及与 GenAI 聊天服务交互时收到的答案被称为“上下文窗口大小”。这通常以 tokens 衡量。

粗略地说，一个 token 大约等于 3/4 个英语单词。单词的部分可以是完整的 token，前缀和后缀构成它们自己的 token。

![](https://cdn.thenewstack.io/media/2025/02/64ec34b1-hugging_face-tokens.png)

*来自 Hugging Face 关于[构建 AI Agents](https://huggingface.co/learn/agents-course) 的课程中的 tokenization 示例。*

不同的服务具有不同的上下文大小窗口。[OpenAI](https://thenewstack.io/mastering-openais-realtime-api-a-comprehensive-guide/) 的 GPT-40-mini 的内容窗口大小为 128,000 个 tokens，或大约 96,000 个单词和相关字符，包括问题和答案。

因此，你必须将整个问题以及所有支持数据塞入上下文窗口。

“对于正常的聊天，这不是问题，”Wei Meng 说。

但是，如果你使用非常大的数据集，这将花费你很多钱！

一个 20 列 500 万行的 CSV 值文件将迅速消耗掉该 token 窗口。

超过上下文窗口大小，你将收到错误消息或产生额外费用。

此外，将你的数据运送到外部会使你的数据隐私面临风险。

## 这样做

不要发送整个数据集，而是将数据保留在你的服务器上。然后，通过包含数据集格式的描述（可能带有 schema 本身），甚至可能包含一些示例（已匿名化）来制定提示。

然后，不要要求 GenAI 回答你的问题，而是要求 GenAI *生成必要的代码或查询*来回答这些问题。

然后，你在本地环境中执行代码。

“你不会违反上下文窗口大小。你不会牺牲数据的隐私，”他说。

在一个例子中，Wei Meng 展示了如何使用 OpenAI 和 [LM Studio](https://lmstudio.ai/) 分析[泰坦尼克号灾难性航行中所有乘客的数据集](https://titanicfacts.net/titanic-passenger-list/)。包含数据的 CVS 文件（有 891 行和 12 列）被加载到 [Python DataFrame](https://thenewstack.io/pandas-a-vital-python-tool-for-data-scientists/) 中。

这是他随后给 OpenAI 的提示：

```
{
'role':'userf',
'content':'''
Here is the schema of my data:
PassengerID,Survived,Pclass,Name,Sex,Age,Sib5p,Parch,Ticket,Fare,Cabin,Embarked
Note that for Survived, 0 means dead, 1 means alive
Return the answer in Python code only
For your info, I have already loaded the CSV file into a dataframe named df
'''

}
```

总的来说，提示越详细，你得到的答案就越好，Wei Meng 建议道。

加载所有提示后，你可以提出你的问题，例如

- 男女乘客的比例是多少？
- 你能可视化每个乘客舱位等级 (Pclass) 的生存率吗？
- 你能可视化单独旅行与与家人一起旅行的乘客的生存率吗？
请注意，如果您手头有 [Python 可视化工具](https://thenewstack.io/what-is-python/)，则答案不需要基于文本。

使用 [Jupyter Notebook](https://thenewstack.io/introduction-to-jupyter-notebooks-for-developers/) 或 LM Studio，您甚至可以自动执行查询，结果会在返回后立即显示在工作区中。

“好处是您不必上传数据，也不必学习数据分析，”他说。

![解决方案说明的屏幕截图。](https://cdn.thenewstack.io/media/2025/02/b7b312e8-llm-analytics.png)

*来自 Wei-Meng Lee 的 Hugging Face 演示文稿。*

## 什么是 Hugging Face？

Wei-Meng Lee 的演讲主要关注如何使用 [Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/)，这是一个协作平台，供开发人员和研究人员使用机器学习模型、数据集和应用程序并进行协作。

在演示中，Wei-Meng 展示了如何通过该公司的 [Transformers API](https://huggingface.co/docs/transformers/en/index) 使用 Hugging Face 的预训练模型。Hugging Face 的 pipeline 对象 [可以简化使用这些模型的任务](https://huggingface.co/docs/transformers/en/pipeline_tutorial)，然后他继续演示。他还展示了如何使用 [Gradio library](https://www.gradio.app/guides/quickstart) 轻松运行基于 LLM 的 Python 应用程序。

“Gradio 允许您仅用几行代码构建一个非常好的 Web 前端，”Wei-Meng 说。