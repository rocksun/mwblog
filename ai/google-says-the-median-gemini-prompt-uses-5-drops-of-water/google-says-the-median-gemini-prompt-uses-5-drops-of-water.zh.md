[Google](https://cloud.google.com/?utm_content=inline+mention) 今天发布了一篇新的论文，旨在量化其 Gemini 模型对环境的影响。研究人员发现，“Gemini 应用文本提示的中位数”（稍后会详细介绍）消耗 0.24 瓦时 (Wh) 的能量和 0.26 毫升的水——或者相当于观看 9 秒电视所用的能量和 5 滴水的量。

Google 表示，一年前，能源消耗量仍然高出 33 倍（碳排放量高出 44 倍）。它将这些收益归功于其全栈方法，即优化从[定制芯片](https://thenewstack.io/google-ai-infrastructure-pm-on-new-tpus-liquid-cooling-and-more/)到模型本身的所有内容。

这些能源和用水量乍一看似乎很小，但值得注意的是，在最近的[财报电话会议](https://abc.xyz/2025-q2-earnings-call/)中，Google 表示其 Gemini 移动应用（仅是使用 Gemini 的一个界面）现在拥有 4.5 亿月活跃用户，并且其数据中心现在每月处理近 1 万亿个 token。

Google 没有提供任何数据来比较这与平均搜索查询的能耗相比如何，也没有提供其音频、照片和视频模型消耗多少能量。该公司也没有定义“Gemini 应用文本提示的中位数”的大小及其生成的 token 数量。目前尚不清楚为什么 Google 不能简单地用数据中心每百万个 token 的耗电量和用水量来表示这些数据。

[![](https://cdn.thenewstack.io/media/2025/08/f00c085c-energy-components.png)](https://cdn.thenewstack.io/media/2025/08/f00c085c-energy-components.png)

图片来源：Google。

## 仅限文本提示

当被问及图像和视频模型的功耗影响（或使用 Gemini 的深度研究模型）的相关问题时，Google 高级能源实验室负责人 Savannah Goodman 表示，“本文的重点是 Gemini 应用文本提示，我们报告策略的一部分是不断评估如何提高这些影响的透明度。”

Google 还辩称，这些模型及其功能在过去一年中发生了很大变化（例如，增加了深度研究），这意味着查询的中位数也发生了变化，底层硬件也发生了变化。

至于为什么 Google 不提供 Gemini 查询中位数和搜索查询的比较数字，Google 的 Partha Ranganathan 负责设计其下一代系统和数据中心，他认为这是“苹果和橘子”。

他说：“访问 Gemini 应用的人与进行 Google 搜索的人的互动方式截然不同。因此，我认为很难对此进行比较，并且鉴于我们拥有一种技术方法——我们试图对该方法背后的技术和科学非常严谨——因此感觉我们无法进行适当的科学的苹果对苹果的比较。所以我们这里没有这个数字。”

[![](https://cdn.thenewstack.io/media/2025/08/3e13d5a4-methodologies.png)](https://cdn.thenewstack.io/media/2025/08/3e13d5a4-methodologies.png)

图片来源：Google。

事实上，Google 已经有一段时间没有提供有关单个搜索查询消耗多少能量的数据了，但在 2009 年，这一数字为 0.3 瓦时。该公司从未更新此数字，并且它仍然被广泛引用，但如果 Google 在过去一年中能够使 Gemini 的能源效率提高 33 倍，那么其搜索团队在过去 16 年中也取得了一些进展。

尽管如此，值得注意的是，Google 的数字明显低于我们在过去两年中看到的大多数公开估计，但与 Sam Altman 今年早些时候的断言相差不远，即平均 ChatGPT 查询[消耗 0.34 瓦时的能量](https://towardsdatascience.com/lets-analyze-openais-claims-about-chatgpt-energy-use/#:~:text=OpenAI%20CEO%20Sam%20Altman%20recently,about%200.000085%20gallons%20of%20water.)和 0.3 毫升的水。目前尚不清楚 OpenAI 如何得出这个数字以及它包括系统的哪些部分。例如，Google 专门排除网络、最终用户设备以及用于训练其模型和存储数据的电力。

虽然很高兴看到一种不同于“Gemini 应用提示的中位数”的指标，部分原因是这使得比较文本、音频、图像和视频提示以及 API 使用和其他方式变得更加困难，但仍然很高兴看到 Google 发布这项工作并提供一些具体的指标和方法。