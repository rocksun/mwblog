# 2025年开发者需要了解的3大AI趋势

![2025年开发者需要了解的3大AI趋势的特色图片](https://cdn.thenewstack.io/media/2024/12/4e34f0d8-ai-1024x576.png)

自2020年以来，人们对AI的兴趣[激增](https://thenewstack.io/the-year-in-ai-whats-behind-in-2020-and-whats-ahead/)，此后一直主导着各大新闻头条和董事会议题的讨论。因此，业务发展也随之而来——根据Confluent的数据流报告中的调查结果，[81%的IT领导者](https://report.confluent.io/key-findings/data-streaming-roi)将AI和机器学习列为其2024年预算中的重要或首要任务。

但是，所有这些关注和投资是否会导致AI在近期未来无处不在并按预期运行？这完全取决于企业是否拥有足够数量的工程师队伍，他们具备新的技能、合适的工具和值得信赖的数据，以将AI的承诺转化为现实世界的能力。

让我们来看看对工程团队影响最大的[AI趋势](https://thenewstack.io/ai/)，以及我们关于如何克服这些挑战的建议。

**趋势#1：随着LLM用例的增长，幻觉将继续成为生产中的重大障碍。**

[大型语言模型(LLM)](https://roadmap.sh/guides/introduction-to-llms)继续遵循摩尔定律的推论，随着它们考虑的训练数据量、定义它们的参数量以及它们注意力可以考虑的上下文窗口的大小呈指数级增长。然而，模型的可解释性总体上仍然难以捉摸。LLM通常是糟糕的推理代理，因此将它们与我们已知有效的机器结合起来，将使我们在[克服幻觉](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/)方面取得更大的进展，而仅仅依赖LLM会导致幻觉。

**对开发者的影响**

LLM本质上是随机的，而许多传统的QA最佳实践假设被测试的系统是确定性的。开发者将不得不依靠不同的方法来测试和建立对LLM启用应用程序的信心。我们可以应用历史上有效的机器学习(ML)技术和其他技术来衡量输出质量并最大限度地减少幻觉。通过应用特定的防护措施，工程师可以构建能够可靠地识别何时出现幻觉或提供低置信度分数信息的LLM。

与LLM相比，使用经过微调的小型语言模型将提供更好的响应。但是，开发者需要为其提供正确的见解，例如事件以及及时和个性化的数据，才能使其成功。开发者可以用来减少幻觉影响的一种有前景的模式是[检索增强生成](https://thenewstack.io/how-to-scale-rag-and-build-more-accurate-llms/) (RAG)，在推理时将提示与相关的特定领域信息结合起来。

**趋势#2：自主AI将更能够进行独立决策。**

自主AI系统承诺代表特定业务职能、团队甚至业务中的个人做出决策并独立行动。然而，随着AI模型变得越来越复杂，它们往往会失去透明度，这为工程团队在构建和部署AI代理时带来了难以回答的问题。

**对开发者的影响**

与自动化程度较低的系统相比，在相关系统使用输出之前识别AI中的错误要困难得多。使用实时数据管道实现RAG可以帮助增强自主AI解决方案的重要上下文，以提高环境感知能力和决策能力。

随着这些解决方案从概念到开发和生产，越来越多的组织将需要一个[数据流平台](https://www.youtube.com/watch?v=hrB71pMVjpw) (DSP)，它具有流式处理、处理和治理功能，以便长期可持续地构建和扩展这些能力。由DSP支持的事件驱动架构为自主系统提供了一个实现框架，将其建模为可组合微服务的异步工作流。这种方法促进了自主系统各个组件的可重用性，并使大型系统比作为大型单体创建时更容易分析和扩展。

**趋势#3：工程团队正在转向动态数据访问以用于AI模型。**

对动态或实时数据访问的需求增长并非仅限于AI/ML计划，但它促进了实时智能的发展。在过去十年中，工程团队越来越多地使用开源流引擎，如[Apache Kafka](https://kafka.apache.org/)和[Apache Flink](https://flink.apache.org/)来支持实时推荐、预测和异常检测。

**对开发者的影响**
This trend will also impact the infrastructure and teams behind these projects.  The shift to real-time data access will allow for more flexible and dynamic data organization, enabling human users, chatbots, and even AI agents to quickly access and query diverse data.


## Empowering Engineers with New AI Skills and Better Data

Companies seeking to reduce complexity and costs when building real-time AI solutions need to shift data processing left and use data contracts to enable dynamic access to trusted data products.  The resulting data products can be consumed as data streams or open table formats. This approach allows data teams to facilitate efficient data processing, providing engineers with data in a clean and consistent format and enabling them to build dynamic AI applications with more confidence and lower risk.


However, simply providing engineers with trusted data isn't enough to ensure AI project success. Leaders also need to incentivize experienced engineers to dedicate time, resources, and support to train and mentor junior team members focused on building differentiated applications.


Data engineers can leverage large language models and generative AI tools to develop their prompt engineering skills and improve their familiarity with coding templates. It will help if engineers maintain a sharp understanding of fundamental computer science, improve their proficiency in popular languages for data and AI/ML such as [Python](https://thenewstack.io/5-python-libraries-every-data-engineer-should-know/) and [Java](https://thenewstack.io/oracle-unveils-java-23-simplicity-meets-enterprise-power/), and understand real-time data processing and event guarantees.


[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)  Technology is moving fast – don't miss an episode. Subscribe to our YouTube channel for all our podcasts, interviews, demos, and more.