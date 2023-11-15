<!-- 
# KubeCon 2023：养宠物，养牛还是养海星？
https://cdn.thenewstack.io/media/2023/11/fab18c98-starfish-1851289_1280-1024x679.jpg
 -->

今年大会的主题演讲探讨了安全性、复杂性、AI等参会者对采用Kubernetes心存疑虑的问题。

译自 [KubeCon 2023: Managing Pets， Cattle … and Starfish?](https://thenewstack.io/kubecon-2023-managing-pets-cattle-and-starfish/) 。

今年[KubeCon+CloudNativeCon北美大会](https://thenewstack.io/what-will-be-hot-at-kubecon-platform-engineering-of-course/)的主题演讲探讨了许多关于采用和[管理Kubernetes](https://thenewstack.io/tim-hockin-kubernetes-needs-a-complexity-budget/)的挑战，而不是仅仅宣传采用云原生的好处。

尽管啰嗦的Kubernetes可以说是跨分布式环境规模化运维和软件部署的最佳方式，但今年的主题演讲着眼于安全性、复杂性、AI和参会者采用云原生时的其他疑虑。

## 当事情出错时

事情可能会也确实会出错，对Kubernetes来说，事情可能错的离谱。在他的演讲“容器可能短暂，但你的业务能承受吗？”中，数据管理工具提供商Veritas产品和解决方案营销副总裁[Chris Wiborg](https://www.linkedin.com/in/cwiborg/)列举了组织可能遭遇数据丢失的方式。他提到了常见的数据丢失威胁，包括基本的人为错误、不足的备份、地理位置分布不足等。

“[云原生计算基金会](https://cncf.io/?utm_content=inline-mention)有这么多侧重增强云数据安全的项目，展馆里也有这么多提供可能解决方案的优秀供应商，你应该尝试它们来防止最大的风险发生”，Wiborg说，“但正如我们从新闻头条看到的，这些事还是发生了。我猜现在这个房间里的人不需要再吓唬勒索软件之类的事情了——我们现在都在与之共存。但也有更为平常的方式可能导致数据丢失。”

复原是关键。回顾一下管理应用程序是养宠物还是养牛的类比，Wiborg 为等式添加了另一种动物符号：海星。这是因为，如果海星失去一条腿，它可以再生。“换句话说，海星更能承受伤害......数据和基础设施需要以同样的方式进行考虑。我们能使它们更具弹性，以便即使某些部分消失也能保持应用程序继续运行吗？”

监控软件提供商[Datadog](https://www.datadoghq.com/?utm_content=inline-mention)对Kubernetes运行失败时可能发生的事情以及过程中学到的教训进行了透明的回顾。

监控软件提供商Datadog在主题演讲“一切，处处，全都是”中，该公司的首席工程师[Laurent Bernaille](https://fr.linkedin.com/in/laurentbernaille)和高级软件工程师[Hemanth Malla](https://www.linkedin.com/in/hemanthmalla)表示，Datadog遭遇了大规模的全球故障，花费了近24小时才得以缓解，在完全恢复应用程序可用性后，又用了24小时才能补齐恢复后的数据。

他们描述了Datadog在不到1小时内丢失了超过60%的Kubernetes节点，以及在数以百计的集群中试图恢复数万个受影响节点时所面临的挑战。

他们的目的是详细描述“Datadog遇到的最艰难的事故”，Malla说。

Datadog拥有充足的工程支持(但创业公司可能就不具备这些资源)。约400名工程师值班应对这不仅仅是一次停机事故。他们通过简单重启Google Cloud上的实例来恢复部分丢失的Kubernetes节点。节点恢复后，他们开始分析日志，“那些系统日志告诉我们，这些节点上发生了无人值守的升级”，

自事故以来，Datadog一直在“努力”构建更多生命周期自动化模块，可以每天用“最小影响”替换成千上万个节点。“它在Kubernetes中完成这项工作。可以想象，这需要大规模的迁移。”

在[Tim Hockin](https://www.linkedin.com/in/tim-hockin-6501072/)的主题演讲“对远景的展望——Kubernetes的第二个十年”中，不可避免地讨论了人工智能带来的深刻变革。他是Google Cloud的著名工程师。

他说，当被问及Kubernetes未来10年时，许多Kubernetes维护者、使用者和其他云原生人士表达的最关切是“机遇和威胁”。但对于AI，它在未来20年将[如何体现](https://thenewstack.io/how-to-boost-developer-productivity-with-generative-ai/)还是个谜，“这很正常”，Hockin说。“这对Kubernetes意味着什么？老实说，我不确定。我并不真正理解它”，Hockin说。

然而，Kubernetes“非常有可能成为AI ML和流程的首选平台”，Hockin说。然而，“本次大会将向您展示这一点，但我们还不真正知道需要做些什么来确保它获得成功，所以我们需要倾听、观察、探索并提出问题，”Hockin说。

除了AI，房间里的另一头大象是气候变化。是的，有许多举措通过降低计算资源来间接减少二氧化碳排放。我认为，必要的是支持气候和天气分析、资源消耗以及纯科研所需的计算框架。

对于Kubernetes和信息技术整体而言，仅CPU消耗以及减少云和数据中心冗余CPU服务器的消耗就代表了降低功耗和二氧化碳排放的低垂果实。

然而，正如Grafana Labs的软件工程师[Niki Manoledaki](https://www.linkedin.com/in/niki-manoledaki-9b505111b/?originalSubdomain=es)在小组主题演讲“云计算中的环境可持续性不是神话生物”中指出的，遗憾的是，我们才刚刚起步。“测量和降低我们软件的能源和碳足迹还不是很普遍，但这正在改变，我们看到了动力”，Manoledaki说。

但遗憾的是，全球变暖已经接近超过1.5摄氏度的临界点，“我们在某些地区已经超过了这一临界点”，Manoledaki说。“想到这一点让人担忧。”
