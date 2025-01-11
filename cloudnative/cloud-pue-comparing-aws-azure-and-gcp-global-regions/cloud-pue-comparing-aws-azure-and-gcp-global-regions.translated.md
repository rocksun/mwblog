# 云PUE：比较AWS、Azure和GCP全球区域

![Featued image for: Cloud PUE: Comparing AWS, Azure and GCP Global Regions](https://cdn.thenewstack.io/media/2025/01/0d3403a6-img_2476-1024x917.jpg)

2024年12月，亚马逊发布了其许多[AWS](https://aws.amazon.com/?utm_content=inline+mention)云区域的[功耗效率 (PUE)](https://en.wikipedia.org/wiki/Power_Usage_Effectiveness_(PUE))数据，加上微软Azure和[谷歌云](https://cloud.google.com/?utm_content=inline+mention)的现有数据，终于有足够的数据可以对全球各区域进行一些比较，看看2022年到2023年发生了哪些变化。

PUE是衡量数据中心能源使用效率的指标。除了计算机本身使用的能源外，还需要能源来冷却数据中心，以及电力在传输和转换到计算机过程中的损耗。能源是在电力进入建筑物时通过电表测量（并付费），PUE为1.15意味着计算机使用的总能量中额外有15%用于冷却和管理费用。实际上，PUE在约1.04到2.0之间变化。

所有[云提供商](https://thenewstack.io/the-complex-relationship-between-cloud-providers-and-open-source/)都运行非常高效的数据中心硬件配置，而且它们总体上随着时间的推移效率越来越高。然而，在温暖潮湿的环境中[冷却数据中心](https://thenewstack.io/next-generation-sustainable-data-center-design/)更难，因此热带地区数据中心的PUE往往处于范围的高端，而世界寒冷干燥地区的数据中心的PUE处于范围的低端。

减少冷却能耗的一种方法是使用更多水，因此PUE和用水效率（WUE，单位为升/千瓦时）之间也存在自然张力。云提供商最近都大力投资于优化WUE，因此最新的数据中心往往具有良好的PUE *和*良好的WUE，但这需要最好和最新的技术。企业拥有的那种典型的低成本和旧数据中心往往接近2.0 PUE，并且WUE也很高。WUE已在[我为The New Stack撰写的文章](https://thenewstack.io/sustainability-how-did-amazon-azure-google-perform-in-2023/)（2024年7月）中进行了解释和跨云提供商的比较。

云提供商在世界各地部署的一些区域是由本地服务提供商托管的，而不是由云提供商建造的专用数据中心。在这种情况下，PUE不包含在公开数据中，原因有两个：一是当没有关于数据中心其余部分的信息时，很难对共享资源进行归属和分配；二是整体PUE通常是服务提供商拥有的专有信息，他们不允许公开共享。根据保密协议，可能还有一些额外的PUE估算可供私下获取，因此如果您在没有公开PUE数据的区域运营，值得向您的提供商咨询。

## 亚马逊/AWS PUE数据

亚马逊在其[可持续发展页面](https://sustainability.aboutamazon.com/products-services/aws-cloud)上描述了新的PUE信息。他们还详细介绍了新的数据中心技术，这将导致他们目前正在建设的数据中心的PUE达到1.08。有一个简短的[PUE方法论pdf](https://sustainability.aboutamazon.com/pue-methodology.pdf)，基本上说明他们遵循相关的国际（ISO）和欧洲（CEN）标准。AWS 2023年全球平均PUE为1.15，美洲为1.14，欧洲、中东和非洲为1.12，亚太地区为1.28。他们表示，他们在欧洲最好的单个数据中心设施的PUE为1.04。尽管如此，他们最好的区域是澳大利亚墨尔本，PUE为1.08，最差的是印度海得拉巴，PUE为1.50。AWS逐年显示许多区域都有改进。

![](https://cdn.thenewstack.io/media/2025/01/35b93950-amazon-pue-547x1024.png)

2025年1月公布的AWS PUE数据。

## 微软Azure PUE数据

微软在2022年发布了许多详细的信息，作为数据中心情况说明书，其中包括其所有区域的PUE估算值，但在2024年12月更新时，省略了数值数据。相反，[一个网页提供了一个摘要](https://datacenters.microsoft.com/sustainability/efficiency/)，只提供了27个区域中的11个区域的信息，该信息与日历年不符，并且没有涵盖整个2023年。我们联系了微软内部目前负责的团队，发现披露原始2022年数据的人员已经离职，并且2022年数据已从其网站上删除。我们已将其存档为[GSF云区域元数据表](https://github.com/Green-Software-Foundation/real-time-cloud)的一部分。
2025年1月微软网页上的PUE数据。

微软公布其在美国怀俄明州的最佳PUE值为1.11，在伊利诺伊州的最低PUE值为1.35。他们的可持续发展目标中没有提及PUE。

## 谷歌云平台GCP PUE数据
多年来，谷歌一直在按季度披露PUE数据，并在其2024年度可持续发展报告中包含了2019-2023年的数据。由于上述AWS和Azure的原因，他们不会在其运营的每个区域公布公开的PUE数据。

![](https://cdn.thenewstack.io/media/2025/01/a2e3ea6b-google-pue-1-701x1024.png)
2025年1月公布的GCP PUE数据。

谷歌的最佳PUE结果为俄勒冈州的1.07，最差的是新加坡和内华达州的1.19。AWS PUE讨论中提到，随着新的空数据中心建筑添加到某个区域，在它们开始充满设备之前，PUE可能会暂时变差。这在GCP区域数据中可见。一些地点支持并非GCP区域一部分的谷歌产品，并且我们在[GSF云区域元数据表](https://github.com/Green-Software-Foundation/real-time-cloud)的制作过程中，在谷歌工程师的帮助下，对GCP云区域与谷歌PUE数据进行了映射。

## AWS、GCP和Azure之间的比较
虽然所有主要的云提供商都拥有业界领先的PUE数字，这些数字可能远优于本地数据中心替代方案，但上述数据显示，GCP拥有最佳的透明度，拥有更长时间段内的更多数据，以及所披露区域的最佳整体PUE。微软从2022年提供最多数据转变为2023年提供最少数据，并且整体PUE值最高。AWS处于中间位置，拥有两年的数据，PUE值比GCP差，但总体上大多优于Azure。AWS包含了诸如海德拉巴等PUE较高的区域数据，而其他云提供商根本没有披露这些数据，并且他们设定了其新建数据中心建筑的优秀目标值1.08。

## 区域比较
如果您可以选择在特定区域使用哪个云提供商，并且您希望最有效地利用所需的能源，那么上述PUE数据可以提供一些场景的数据。

弗吉尼亚州是世界上最大的云区域，AWS PUE为1.15，Azure为1.14，GCP为1.08。对于俄亥俄州附近的区域，AWS PUE为1.12，GCP为1.10。

新加坡是所有云提供商在亚洲的主要区域，气候具有挑战性的热带气候。AWS PUE为1.30，Azure为1.34，GCP为其两个设施中的每一个的1.13或1.19。

爱尔兰是欧洲最大的区域之一。AWS PUE为1.10，Azure为1.19，GCP为1.08。

## 为支持AI热潮的GPU做出良好的PUE假设是什么？
人们非常担心大规模建设GPU能力需要多少电力。GPU直接使用的电力需要乘以该数据中心或云区域的PUE，然后才能计算其对电网的需求或其碳足迹。查看上述数据，我认为需要考虑两种情况。放入较旧的企业数据中心的GPU往往会压垮现有的基础设施（这些基础设施并非设计用于非常高的功率密度），因此PUE可能很差，我估计为1.5或更高。但是，为GPU部署而专门建造的大型新数据中心在许多情况下受到可用电源的限制。最新、最高效的设计将允许在给定位置为更多GPU供电和冷却，我假设PUE为1.08，无论谁在建造它。

## 绿色软件基金会实时云项目
过去一年左右的时间里，我一直领导着GSF[实时云项目](https://github.com/Green-Software-Foundation/real-time-cloud)。我们花费大量时间发现许多收集和报告能源和碳数据的来源、接口和产品，并在大型Miro流程图中记录了它们之间的关系。我们还发布了从GCP、AWS和Azure收集的区域元数据，并将其总结成一个涵盖2022年数据集的单一表格。我们正在更新它以包含最新的数据版本以涵盖2023年，并计划在云提供商披露其数据之前生成2024年和2025年的估计值，以便今天运行的工作负载可以使用我们认为是最佳可用猜测的一些数据。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)