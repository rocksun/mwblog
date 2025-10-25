<!--
title: 周一AWS故障复盘：深度揭秘幕后真相
cover: https://substackcdn.com/image/fetch/$s_!JfEm!,w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf29953d-3248-4296-9bcb-050b60a061dc_6609x4406.jpeg
summary: AWS us-east-1中断源于DynamoDB DNS竞争条件，导致广泛服务受影响，需手动干预。教训是复杂系统需关注关键组件及故障影响。
-->

AWS us-east-1中断源于DynamoDB DNS竞争条件，导致广泛服务受影响，需手动干预。教训是复杂系统需关注关键组件及故障影响。

> 译自：[Demystifying the postmortem from Monday's AWS outage](https://thefridaydeploy.substack.com/p/demystifying-the-postmortem-from)
> 
> 作者：Tom Elliott

[![](https://substackcdn.com/image/fetch/$s_!JfEm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf29953d-3248-4296-9bcb-050b60a061dc_6609x4406.jpeg)](https://substackcdn.com/image/fetch/$s_!JfEm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf29953d-3248-4296-9bcb-050b60a061dc_6609x4406.jpeg)

*图片来源：cottonbro studio：[https://www.pexels.com/photo/man-in-gray-long-sleeve-suit-holding-a-pen-8369520/](https://www.pexels.com/photo/man-in-gray-long-sleeve-suit-holding-a-pen-8369520/)*

上周一发生的AWS中断事件很难被忽视。即使您没有亲身经历任何影响，您可能也听说了智能门铃不响、智能床过热以及智能冰箱“口吐芬芳”的故事。

早期关于原因的猜测很多，从流氓人工智能到关于“互联网终止开关”的阴谋论都有。但现在亚马逊已经发布了一份[官方摘要](https://aws.amazon.com/message/101925/)，详细说明了根本原因。

不幸的是，这份摘要读起来并不容易。有很多冗长、信息密集的段落。但幸运的是，我这周正为我的博客主题犯愁！所以，这是我的总结。

**DynamoDB错误影响了广泛的AWS服务**。摘要详细说明了对EC2和NLB的影响，但列出的其他服务还包括Lambda函数、SQS/Kinesis、EKS和Redshift等等。这导致了us-east-1区域服务的广泛但非完全中断，并对其他区域产生了一些影响。

更深入地分析一下，摘要详细说明了问题如何从DynamoDB级联到EC2，最终再到NLB。DynamoDB是管理EC2生命周期系统的关键，因此这些错误阻止了新实例的创建。这导致网络状态信息传播延迟，从而引起了错误的健康检查失败。这些失败使得NLB节点宕机，导致连接错误。

在SRE圈子里有一句老话：“总是DNS”。

DynamoDB DNS条目管理中的竞争条件导致了us-east-1区域所有IP的DNS条目被删除。这使得该区域无法与DynamoDB通信，从而引发了上述一系列级联效应。

此次故障的具体细节在一篇长达776个单词的段落中进行了详细描述，其中包含了相当多的架构细节。归结起来就是，多个“DNS执行器”（DNS Enactors）负责更新DynamoDB的DNS条目，并且有检查机制确保它们始终写入最新的信息。但这一次，一个执行器延迟的时间超出了预期，将旧信息应用在了新信息之上。这些旧信息被视为过时，并被“DNS规划器”（DNS Planner）清理，从而删除了所有DNS条目。

这属于那种罕见的停机事件，你无法将代码或配置更改指为根本原因。在这种情况下，它只是在错误的时间发生了错误的事件组合，暴露了一个缺陷。

这就引出了一个问题：为什么问题发生在us-east-1而不是其他区域。如果我来推测（我确实会），这可能归结于该区域的巨大受欢迎程度，来自用户和亚马逊服务的额外负载都可能导致了引发整个局面的延迟。

冗长的根本原因段落以这句话结尾：“*这种情况最终需要操作员手动干预才能纠正*”。这在EC2和NLB的下游故障中也得到了证实。我不会列出所有具体的行动，但它们包括手动修复数据和工具，以及应用限流以减少过多的负载。

摘要的末尾列出了亚马逊为防止此类问题再次发生而正在采取的行动。详细说明了针对DynamoDB、EC2和NLB的明确缓解措施。最重要的是，导致整个问题的竞争条件将被修复，EC2和NLB将收到“速度控制”和限流的更新（在我看来这听起来是一回事）。

有趣的是，他们已在竞争条件修复实施期间禁用了DNS规划器和DNS执行器的自动化功能。这可能意味着DNS正在手动管理，我猜测这可能会在一段时间内对DynamoDB的扩展性产生影响。

对我来说，这次事件的主要教训是，*复杂系统以复杂的方式运行*。AWS和其他超大规模平台可能是我们大多数人能接触到的最复杂的系统。

在DynamoDB中遇到错误的事件组合导致其完全宕机，而DynamoDB对其他系统又足够关键，以至于它们也陷入了需要手动干预的糟糕状态。

在查看解决方案时，不同事件的时间点很有趣。底层的DynamoDB问题在太平洋时间凌晨2:40得到解决，但对EC2和NLB的连锁反应却持续了近12个小时，分别在下午2:09和下午2:15才解决。这表明次要影响可以与主要影响同样严重，有时首先确定根本原因可以帮助您以最有效的顺序解决问题。

这会让人重新思考在AWS上构建吗？也许会有一部分人。这会导致基于简单VPS托管的复兴吗？可能不会。

但在设计我们自己的系统时，这表明了解最关键的组件是什么，以及如果它们突然停止工作可能会发生什么，这一点非常重要。