# API 状况： 微服务到 Macro 和 僵尸 API

在最新的 API 状况报告中，开发人员提到了僵尸 API 和微服务扩大化等问题。

翻译自 [State of the API: Microservices Gone Macro and Zombie APIs](https://thenewstack.io/state-of-the-api-microservices-gone-macro-and-zombie-apis/) 。

![](https://cdn.thenewstack.io/media/2023/06/be92e3e6-pexels-denys-gromov-14145588-1024x683.jpg)
*图片来自 Pexels*

微服务扩张成为难以控制的混乱和僵尸 API 是今年 [Postman API 状况调查](https://www.postman.com/state-of-api/)中出现的一些关注点。尽管存在这些问题，调查还发现 API 对组织来说是有回报的——四万名受访者中有近三分之二表示他们的 API 可以带来收入。

其中 43% 的人表示 API 为公司创造了超过四分之一的收入。对于少数几家公司来说，API 产生的收入超过了总收入的 75% 。报告指出，这些公司涉足金融服务业的可能性几乎是其他行业的两倍。

考虑到 API 的盈利能力，不难理解为什么 92% 的全球受访者表示在接下来的 12 个月里 API 的投资将增加或保持不变。这比[去年的报告](https://thenewstack.io/state-of-the-api-monetizing-apis-deployment-is-on-the-rise/)增加了三个百分点。

报告指出：“这一增长可能反映了某些领域对技术经济萎缩的最糟情况已经过去的感觉。与此同时，更少的受访者表示他们预计今年会削减对 API 的投资。”

## 微服务、Mesoservices 和 单体应用

微服务仍然是大多数组织中主要的 API 架构风格，但似乎情况并不总是按计划进行。在今年的报告中，10% 的受访者表示为微服务提供动力的 API 已经变得庞大而难以控制，形成了 “[macroservices](https://thenewstack.io/lets-take-our-conversations-about-microservices-to-the-next-level/)” 而不是微服务。

微服务被定义为独立工作以执行单一职责的小型服务，而 macroservices 被定义为已经变得庞大且难以控制的微服务，接近单体应用。[单体应用](https://thenewstack.io/monoliths-to-microservices-an-api-first-approach/)是接口和数据访问合并为一个包的单层应用程序。最后， Mesoservices 则是“合适”的选择：既不太大也不太小。

[单体应用](https://thenewstack.io/return-of-the-monolith-amazon-dumps-microservices-for-video-monitoring/)和 Mesoservices 各自占调查的略多于 20% 。

![](https://cdn.thenewstack.io/media/2023/06/79871db1-macroservices-microservices-and-monoliths.png)
*根据 Postman 的 2023 年 API 状况报告，关于 API 架构风格的图示*

Postman 的联合创始人兼首席技术官 [Ankit Sobti](https://www.linkedin.com/in/ankit-sobti/) 告诉 The New Stack：“很明显，这些观察来自微服务主流化的十年以及公司对其的思考。我们通过这项调查想要指出的是，微服务的概念是指它们的发展变得庞大且难以控制，从而失去了作为微服务的本质。”

使用微服务的一个理论上的优势是微服务及其 API 可以更容易地被重复使用。因此，值得注意的是，自认为 “API优先” 的领导者中有 21% 提到重复使用 API 或微服务是他们组织中的一个痛点。

Sobti 表示：“可重复使用性的方面是 API 的可消费性，而我们与客户交流时看到的挑战在于首先是如何发现 API 。API 是否一致、符合规范并且易于设置？在刚开始使用 API 时，身份验证可能是一个大问题。因此，我认为这些推动 API 消费的因素对于 API 在网络中的集成方式产生了重大影响。”

## 随着裁员的发生，僵尸 API 不断增加

几乎 60% 的受访者对僵尸 API 表示担忧，这些 API 缺乏适当的文档和所有权，在开发人员离开组织后仍然存在。在开发人员离开后，僵尸 API 排名第二位的关注点，仅次于文档质量差。与高管相比，工程师和开发人员更关注僵尸API，高管们则将“机构记忆的丧失”略微比维护丧失（也就是僵尸API）更令人担忧。

报告指出：“这些 API 没有所有者、监督或维护，有时被公司遗忘。最糟糕的情况下，僵尸 API 会带来安全风险；最好的情况下，它们会提供糟糕的用户体验。”

![](https://cdn.thenewstack.io/media/2023/06/4ed5b670-when-developers-leave.png)
*当开发人员离职时的图表，根据 Postman 的 2023 年 API 状况报告*

一种解决方案是保持一个使用的 API 目录，Sobti 建议。

Sobti 告诉 The New Stack：“这就是僵尸 API 的出现，因为很多机构知识都掌握在构建它的人手中。一旦这些人离职，变更管理就变得复杂，这就是为什么对 API 进行目录化，特别是对内部 API 进行目录化非常关键的地方。”

API 目录可以将内部 API 集中管理起来。现在有专门的团队负责不仅构建允许目录存在的基础架构，还负责管理目录并创建构建实践，以将这些 API 纳入目录。这就是重复使用变得关键的地方，他补充说。

调查还发现，缺乏文档被认为是使用 API 的主要障碍。

根据一半的受访者表示，不到 20 个 API 更改中只有不到 1 个失败。在各行业中，医疗保健行业的失败率最低，有 55% 的受访者表示不到 20 个 API 部署中只有不到 1 个失败。教育行业则处于另一端；只有 43% 的受访者表示他们的失败率达到这个水平。也许这与另一个重要发现有关：教育行业也是最有可能跳过 API 测试并在 API 开发上花费最少时间的行业。

相较于所有受访者，API 优先的领导者遇到的失败情况较少，有 60% 的人表示失败次数少于 20 次中的 1 次。

## API优先的开发

报告还注意到了一个趋势，即所谓的 API 优先公司在各种 API 问题上的表现比非 API 优先公司更好。API 优先公司将 API 置于开发过程的起始位置，将 API 视为软件构建的基石。超过 75% 的受访者在某种程度上同意或强烈同意，在 API 优先公司，开发人员更具生产力，创建更好的软件，并与合作伙伴更快地集成。

![作为API优先的好处](https://cdn.thenewstack.io/media/2023/06/e3bf8c8a-api-first.png)
*通过Postman的2023年API状况调查，了解API优先的好处。*

API 优先意味着在编写其他代码之前先[开发 API](https://thenewstack.io/can-agile-teams-have-a-design-first-approach-to-apis/) ，而不是将其视为事后补充的内容，根据 Postman 的定义，这个术语是针对调查受访者而定义的。

Sobti 表示：“ API 优先的公司是那些承认 API 是其软件策略的基石的公司。因此，您在思考一个开发模型，即将应用程序构想为内部和外部服务通过这些 API 进行连接。API 优先的组织越来越意识到 API 的商业和技术影响。”

他说，公司正在意识到 API 对业务的战略价值：更多公司报告称， API 在公司的收入中占据了重要比例。调查还发现，收入是除了使用量之外，API 访问的第二重要指标。调查发现，随着公司规模和开发人员数量的增长，API 优先公司获得的好处也增加。

报告指出：“在拥有 100 名或更少开发人员的小公司中，32% 的受访者强烈同意 API 优先的公司入职速度更快。但是当开发人员数量超过 100 时，这个比例稳步上升。”“当公司的开发人员达到 5,000 人时， 42% 的受访者强烈同意这一说法。当回答按公司规模排序时，我们在几乎所有指标上都看到了类似的增长。”

他说：“从技术上讲，我们看到 API 优先的公司能够更快地构建 API ，报告的失败情况较少，当 API 出现问题时，能够在不到一个小时内恢复和响应。我们看到 API 在组织内部和外部的数量确实在增加，其中一部分原因是能够更多地重复使用在您的组织内部或外部创建的功能，现在您可以使用、订阅或购买。”

他还表示，利用重复使用的能力可以使开发人员在人员减少的情况下做更多的工作，无论是因为人员减少还是因为开发人员不必创建业务功能，因为他们可以订阅 Stripe 并通过 Stripe 的 API 管理计费等。

GraphQL作为API架构的地位有所提高
调查还发现，尽管REST仍然是迄今为止使用最广泛的API架构，但它在一些新进入者面前略微失去了一些优势。今年，86%的受访者表示他们使用REST，比去年的报告下降了3个百分点，前一年下降了6个百分点。

SOAP 的使用率今年下降到了 26% ，而去年则为 34% 。GraphQL 的使用率上升到了 29% 。

在 API 规范方面，JSON Schema 是最受欢迎的，其次是 Swagger/OpenAPI 2.0 和 OpenAPI 3.x 几乎持平。GraphQL 在受欢迎程度上排名第四。

![API规范偏好图像通过Postman的2023年API现状报告。](https://cdn.thenewstack.io/media/2023/06/9f2bc362-json-schema.png)
*API规范偏好图像通过Postman的2023年API现状报告。*

编辑说明：于 2023 年 6 月 29 日更新了此篇文章，以显示最新的规范图表。