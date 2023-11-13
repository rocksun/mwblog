<!-- 
# 
https://cdn.thenewstack.io/media/2023/10/30d3e836-algorithm-3859537_1280.jpg
 -->

在实时数据分析中，低延迟的数据对于选择和更新模型的特征和权重以获得更精确的结果非常有用。

译自 [Machine Learning for Real-Time Data Analysis: Training Models in Production](https://thenewstack.io/machine-learning-for-real-time-data-analysis-training-models-in-production/) 。

一些最复杂的[实时数据分析](https://thenewstack.io/the-pinnacle-of-real-time-data-analysis-stream-processing/)涉及在生产环境中部署先进的机器学习模型的同时对其进行训练。通过这种方法，模型的权重和特征会随着可获得的最新数据不断更新。

因此，对于任何特定用例的高度细分的情况，模型的输出会变得更加精致、准确和适用。

流数据平台和流数据引擎非常[适合](https://thenewstack.io/celerdata-upends-real-time-data-analytics-with-dynamic-table-joins/)这种形式的实时数据分析，因为它们可以提供调整模型响应所需的持续低延迟数据。这些数据为特征选择过程提供了信息，使得模型能够调整自身以适应各种影响其结果的情况。

正如 [SAS](https://www.sas.com/en_us/home.html) 高级分析总监 [Gul Ege](https://www.linkedin.com/in/gul-ege-4b513818) 所说: “随着产品和用户数据以及它们的特征和选择的变化，更新模型是非常有意义的。”

支持的用例涵盖从计算机视觉监控到为[广告技术](https://thenewstack.io/implementing-high-performance-ad-tech-demand-side-platforms/)、保险技术、电子商务等领域的在线推荐引擎等各个方面。随着应用范围如此广泛，同时进行机器学习模型的训练和部署的能力正日益成为推进实时数据分析的关键。

## 在生产环境中训练

推荐引擎很好地展示了在生产环境中训练[机器学习](https://thenewstack.io/lifelong-machine-learning-machines-teaching-other-machines/)模型的效用。不管具体的应用是什么，这种方法都被视为对传统离线训练模型、在线部署模型、然后比较其在线和离线表现的流程的进一步发展。这些应用程序的特征选择过程存在着二分法，比如在广告技术用例中，会根据用户在电商网站上的最新点击[实时推荐](https://thenewstack.io/real-time-recommendations-with-graph-and-event-streaming/)广告。

Ege指出: "你有产品的特征，也有用户的特征，推荐系统应推荐的内容取决于这两方面。" 尽管产品的特征可能没有用户浏览网站的特征那么动态，但能够[实时调整它们](https://thenewstack.io/apache-flink-for-real-time-data-analysis/)以获得最新数据对产生及时、相关的推荐至关重要。

Ege评论道: "特征就是最终用户的行为，他们与网站的互动方式。而产品自身也有特征。如果我在找红色的裙子，请不要给我推荐蓝色的裤子或手袋。"

## 历史数据的考量

尽管使用这种方法生成[推荐](https://thenewstack.io/explore-or-exploit-trivagos-ml-for-new-recommendations/)的数据非常迅速，但模型特征也会考虑到一定的历史数据。训练过程很少是瞬间的，往往是连续的，模型的表现也会[随时间变得更好](https://thenewstack.io/how-to-choose-and-model-time-series-databases/)。根据 Ege 的说法，[对于许多](https://thenewstack.io/arrikto-ml-model-deployments-on-kubernetes-can-get-better/)在线进行训练、部署和更新的模型，“它们中一些需要一段时间进行热身。可以从客户第一次交易开始优化，然后同一客户再次回来进行另一笔交易。所以模型的表现会随时间变好。”

每笔交易中的各种行为都会影响模型对该客户、类似用户或组织对数据进行的分割方式的了解。Ege 提到: "只要这些行为存在并被记录下来，你实际上可以在线构建历史，并进行推荐。" 通过部署多个模型和算法来解决特定的业务问题，结果通常会有所改善。

对于保险科技的用例(客户在线输入信息后立即提供报价和各种保险产品)，组织“可能运行多个算法以更好地适应情况”，Ege 指出。“它们有略微不同的数据可用性。这取决于你拥有多少历史数据和特征。这是同一问题的不同方面。”

## 离线训练，在线部署和评分

尽管存在通过在线同时训练和部署模型来加速数据科学过程的倾向，但在某些情况下，保持这两步分离对实时数据分析仍有好处。离线创建和训练模型，然后使用实时事件数据在线部署模型并评分，之后再与离线表现比较，这种做法并不少见。

采用这种成熟方法的决定性因素之一与模型训练所需的数据量和变化相关。Ege 指出，当“技术或问题需要的数据量大于将流入大型模型的数据量”时，这些问题尤其相关。

通过离线训练，组织可以利用更广泛的数据选择和更多的历史数据(例如遥远的几年前的确定流失的财务记录)来训练模型。其基本前提是这些模型“需要用足够的数据进行训练，以捕捉正常情况，这样在部署时才能捕捉异常情况”，Ege 说。

这一要求适用于某些异常检测应用。一旦这些模型的离线训练完成，用户仍可以使用流数据对其进行在线评分以监控性能。例如“质量控制的计算机视觉”，Ege说“如果你在制造某物发现裂缝等问题，你越早检测到并将其取下生产线，损失就越少。”

## 核心价值主张

使用机器学习模型进行实时数据分析现在已经相当普遍。这些应用的传统数据科学方法是在将模型投入在线生产前离线创建模型。正如 Ege 透露的，在某些情况下这种方法仍可取。

然而，在[生产环境中训练模型](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/)，并根据实时输入更新其特征和权重的能力，对确保模型对最新可用数据做出反应至关重要。能够做到这一点是[实时数据分析](https://thenewstack.io/clickhouse-optimizing-real-time-data-analysis-with-online-analytical-processing/)的核心价值所在，既可以实时行动，也可以最大化机器学习实现这一目标的效用。
