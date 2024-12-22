
<!--
title: 亚马逊通过从Apache Spark迁移到Ray节省数百万美元
cover: https://cdn.thenewstack.io/media/2024/11/9632b561-patrick_ames-ato2024.jpg
-->

将数据湖表压缩工作从Apache Spark转移到基于Python的Ray后，亚马逊发现其效率提高了82%。  ATO 2024报告。

> 译自 [Amazon to Save Millions Moving From Apache Spark to Ray](https://thenewstack.io/amazon-to-save-millions-moving-from-apache-spark-to-ray/)，作者 Joab Jackson。

对于像亚马逊这样的大型电商公司来说，即使是微小的性能提升也能带来可观的节省。

通过在2024年第一季度将数据湖表压缩任务从[Apache Spark](https://thenewstack.io/enhancing-the-flexibility-of-sparks-physical-plan-to-enable-execution-on-various-native-engines/)迁移到基于Python的[Ray](https://www.ray.io/)，该公司发现可以提高82%的效率。

鉴于压缩是其内部商业智能服务的必备功能，这家电商公司或许能够节省超过22万年的EC2 vCPU计算时间。从典型的AWS客户的角度来看，这相当于每年节省约1亿美元的亚马逊EC2按需R6g实例费用。

是的，亚马逊在内部使用了大量的BI。

亚马逊首席工程师在[All Things Open 2024](https://allthingsopen.org/)会议（上周在北卡罗来纳州罗利举行）上讨论了[其迁移到Ray](https://aws.amazon.com/blogs/opensource/amazons-exabyte-scale-migration-from-apache-spark-to-ray-on-amazon-ec2/)。

他的信息是？Ray不仅仅用于构建机器学习管道；这是它目前最受欢迎的用途。

“Ray的核心是一个非常通用的分布式计算框架，我认为它几乎可以胜任任何你决定放大并集中注意力的分布式系统领域，”Ames说，他也是[Ray项目](https://github.com/ray-project/ray)的贡献者。

## 压缩的必要性

迁移到Ray加快了亚马逊最昂贵操作之一——压缩的速度。每当像Apache Iceberg或Apache Hudi这样的数据湖表格式提供写时复制或读时合并功能时，最终它将使用压缩来协调对表的更新。

以前，Apache Spark负责这项工作。

在他的演讲中，Ames描述了亚马逊如何从2016年使用大型Oracle数据仓库转变为运行其自己的完全可扩展的EB级[数据湖仓](https://thenewstack.io/showdown-at-the-lakehouse-databricks-muscles-up-with-tabular/)，同时保持[ACID一致性](https://thenewstack.io/acid-transactions-change-the-game-for-cassandra-developers/)。其理念是将存储与计算解耦，以便数据库表可以存储在S3存储桶中，用户可以自带查询引擎。

最初，表是通过仅追加语句更新的，很快，即使是最强大的平台也难以处理它们。

因此，他们让Spark开始去除重复项，事实证明，这项工作相当棘手。

“从理论上讲，查找重复项是一个很简单的问题，但当你的数据开始增长到PB级甚至更大时，它就会变得有点棘手，你无法再将其放入单个节点中，”Ames说。

亚马逊内部的商业数据技术部门随后寻求Ray以进一步优化。

与Spark一样，Ray也来自加州大学伯克利分校。一些参与Ray研究的学者后来创立了[Anyscale，](https://www.anyscale.com/platform)该公司为该平台提供商业支持。

由于其Pythonic API和处理大型数据集的能力，Ray已经在亚马逊数据科学家群体中找到了自己的位置。[Pandas](https://thenewstack.io/pandas-a-vital-python-tool-for-data-scientists/)非常适合单节点数据集，但Ames解释说，为TB级数据构建数据管道可能很困难。

这就是Ray的用武之地。

基本上，你可以采用任何可以并行化的[Python](https://thenewstack.io/what-is-python/)应用程序，为其添加分布式函数和分布式类的任务注释，然后你可以将该代码部署到任意大的集群中，它将为你管理大量的集群扩展，”Ames解释道。

![Chart: Business Data Technologies](https://cdn.thenewstack.io/media/2024/11/d604e2bb-heterogenous-ray-clusters.png)

*商业数据技术如何使用Ray配置集群（亚马逊）。*

Ames说，在亚马逊，这项技术将来有可能成为亚马逊所有数据管道中“统一”的计算框架。

## 亚马逊BI

亚马逊的内部数据湖拥有“数万用户”，不仅来自AWS商业分析师，也来自合作伙伴。

亚马逊的Ray压缩器目前每天运行超过25000个作业，每天需要大约150万个EC2 vCPU。每天合并约40PB的Apache Arrow数据，成本约为0.59美元/TB。

内部客户按消耗的数据量（字节）付费，这笔费用用于维护数据目录。令人惊讶的是，成本最大的变化来自数据压缩。

“所以我们一直在往Spark上投入资金，数据集也越来越大，”Ames说，并补充道这不是“最优雅的解决方案”。

团队研究了Ray，发现它很有前景，并重新设计了其压缩算法以在该平台上运行。他们还研究了Ray的数据科学工具如何帮助提高数据质量。亚马逊的大量代码库是用Java编写的，因此做了大量工作来创建与Ray的Python API的链接。

迄今为止，亚马逊一直在并行运行Spark和Ray压缩作业以确保一致性。但是，今年Spark将被淘汰，所有操作都将迁移到Ray。

## 使用Ray的结果

早期结果显示Ray具有明显的性能优势。

业务部门发现，Spark在一个[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention)的EC2实例上压缩1GB数据大约需要半分钟。但Ray只需要十分之一分钟，根据2024年第一季度的数据，Ames将其描述为82%的效率提升。

![Ray vs. Spark in terms of efficiency (Amazon)](https://cdn.thenewstack.io/media/2024/11/6f40cf1d-ray-v-spark-efficiency-chart.png)

*Ray与Spark的效率对比（亚马逊）。*

对于这些作业，他们还发现Ray压缩器消耗了集群总可用内存的大约55%，Ames承认这并非最佳状态，他更希望将其提高到80%左右。每个服务器集群总共提供约36TB的可用内存。

![](https://cdn.thenewstack.io/media/2024/11/ef85edcc-ray-compactor-memory-chart.png)

一个令人担忧的方面是可靠性，这可能会像Ames所说的那样，“损害你的成本优势”，因为需要额外成本重新运行作业。最初，在2023年10月，Ray第一次尝试压缩表仅成功了85%的时间。

同样，这也不是理想状态，但到2024年2月，团队将其提高到99.15%，这更接近Spark的99.91%。

![Chart: Ray vs. Apache in terms of reliability](https://cdn.thenewstack.io/media/2024/11/00adbcea-ray-v-spark-reliability.png)

*Ray与Spark的可靠性对比（亚马逊）。*

迁移完成后，预计每年将减少约220,000年的vCPU时间计算需求，按照典型的AWS客户的Amazon EC2按需R6g实例收费计算，这相当于大约1亿美元。

## Ray的未来

Ames总结道，Spark仍然具有一些优势。它仍然比Ray拥有更多通用的数据处理功能。例如，Ray仍然没有简单的SQL接口。因此，一些定制仍然不可避免。

“你不能只是将Spark作业放到Ray上，然后期望获得这种性能提升，”Ames说。

项目团队还计划调整压缩算法以用于[Apache Iceberg](https://thenewstack.io/snowflake-databricks-and-the-fight-for-apache-iceberg-tables/)，他们希望在2025年发布。

“如果你们中有任何人在使用Apache Flink编写Iceberg表，然后尝试使用Spark或其他工具读取它们，这应该会大大改善这个过程，”Ames说。

但总的来说，对于大规模数据操作，Ray值得认真考虑。

“Ray核心足够灵活，可以让你为非常具体的问题设计非常优化的解决方案，”Ames说。“如果你能专注于你组织中一个特别繁重且昂贵的问题，那么这可能是一个好领域——如果你的企业愿意与你一起投资——将Ray的放大镜对准这个问题。”
