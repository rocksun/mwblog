# MinIO 的对象存储支持 Snowflake 的外部表

翻译自 [MinIO’s Object Storage Supports External Tables for Snowflake](https://thenewstack.io/minios-object-storage-supports-external-tables-for-snowflake/) 。

这种组合使用户能够以就像数据在 Snowflake 中一样的方式，在任何地方查询数据。

![](https://cdn.thenewstack.io/media/2023/06/524860f0-cloud-2570256_1280-e1687843197787.jpg)

[MinIO](https://thenewstack.io/how-minio-brings-object-storage-service-to-kubernetes/) 为各种工作负载提供与云环境无关的对象存储解决方案，可以在本地、共存和边缘环境中使用，支持包括高级机器学习、流式数据集、非结构化数据、半结构化数据和结构化数据等各种数据类型。

MinIO 对这些数据类型的影响对 Snowflake 用户来说不仅仅是学术上的兴趣。MinIO 几乎可以在数据存在的任何地方提供对象存储的能力，这与 [Snowflake](https://www.snowflake.com/en/) 的外部表概念相得益彰。外部表最大程度地减少了数据移动，降低了成本，并使组织能够在任何给定的用例中更充分地利用其数据。MinIO 公司在本周举行的 [Snowflake 峰会](https://www.snowflake.com/summit/)上占据重要地位，并与 The New Stack 就其与 Snowflake 的关系进行了交谈。

据 [MinIO](https://min.io/?utm_content=inline-mention) 首席营销官 [Jonathan Symonds](https://www.linkedin.com/in/jtsymonds?original_referer=https%3A%2F%2Fwww.gopher.com%2F) 表示，Snowflake 希望“访问更多数据而不是更少数据，因此他们基本上创建了这个称为外部表的概念。它允许您在数据所在的任何地方进行查询”。

使用 [MinIO](https://min.io/) 存储数据时，实际上几乎没有数据存在何处的限制。

## 外部表

按照这个模式，[Snowflake](https://thenewstack.io/snowflake-builds-out-its-data-cloud/) 用户可以在设置了[外部表](https://docs.snowflake.com/en/user-guide/tables-external-intro)的任何地方查询数据，而当与 MinIO 的对象存储一起使用时，这些地方可能是相邻的云环境、本地数据中心和边缘设备。从最终用户的角度来看，数据好像就在 Snowflake 中，无需进行所有的数据准备和数据流水线工作。MinIO 的高管 Satish Ramakrishnan 解释道：“唯一需要发生的事情就是管理员必须将 MinIO 设置为外部表，并为用户授予使用权限。因此，一旦他们将其视为外部表，就可以运行常规查询。对他们来说，它只是数据库中的行和列。”

Snowflake 负责查询外部数据，就好像它位于内部一样。Ramakrishnan 指出，对于外部表，云仓库“对其自身的内部系统所做的事情与对外部表所做的事情是一样的，例如缓存查询和创建材料化视图，它会自动完成所有这些。”性能问题似乎可以忽略不计，部分归功于缓存技术。Ramakrishnan 提到了一个使用案例，在该案例中，从 Snowflake 查询了外部表，“首次提取数据需要几秒钟，然后之后的查询都只需几毫秒...所以我们知道其中有很多缓存，他们已经在做这方面的工作。”

## 就地查询

Snowflake 的外部表在 MinIO 的对象存储中实现的就地查询功能为企业带来了许多优势。其中最值得注意的是，在分布式环境中的数据不再需要移动。传统上，数据移动被认为是一个瓶颈，并且往往是昂贵且繁琐的。

关于这种就地查询方法，Ramakrishnan 提到：“您可以在所有数据上运行查询，而不需要任何数据移动成本或清理数据。您可以在所有数据上运行查询，并且最重要的是，它是实时的。它不需要通过数据管道从数据湖传输到 Snowflake 。”根据使用情况和数据的速度，当涉及到数据管道时，新数据往往在数据传输到 Snowflake 之前就已经生成。

## 其他优势

传统方法的高昂成本通常会导致用户不得不选择移动哪些数据，从而无法查询或访问所有数据。外部表方法的另一个优势是可以从多个 Snowflake 实例访问数据，这对于在不同地理位置具有分散团队的组织非常有益。

Ramakrishnan 指出：“您可以在 AWS 上拥有一个 Snowflake 实例，在 GCP 上拥有另一个 Snowflake 实例，但仍然可以访问相同的表。不需要数据移动。”此外，数据的副本较少，这有助于安全性、访问控制和[数据治理](https://www.gartner.com/smarterwithgartner/7-key-foundations-for-modern-data-and-analytics-governance)工作。此外，用户可以获得其数据的统一版本，以支持所谓的真实单一版本。“您无需移动数据，可以运行所有常规的 Snowflake 作业；查询和应用程序将完全正常工作，” Ramakrishnan 补充道。

## 总体意义

对象存储的总体意义可能在于其提供高度详细的非结构化和半结构化数据的元数据描述，并且这些数据可以在规模上快速检索。然而，Snowflake 通过外部表的就地查询方式进一步扩展了这些优势，避免了数据管道的数据移动、成本和延迟。云数据仓库的广泛用户群体很可能会充分利用这一优势，就像它在其他对象存储应用中一样。

