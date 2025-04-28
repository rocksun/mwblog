# 如何掌握向量数据库

![Featued image for: How To Master Vector Databases](https://cdn.thenewstack.io/media/2025/04/618414f4-master-vector-databases-1024x576.jpeg)

机器学习 (ML)、人工智能和无尽的数据流正在重塑我们解决问题的方式。但是，在处理图像、音频或文本嵌入等非结构化数据时，传统数据库通常会捉襟见肘。这就是[向量数据库](https://thenewstack.io/elasticsearch-was-great-but-vector-databases-are-the-future/)的用武之地。它们旨在快速有效地存储、索引和搜索高维向量。

当平台推荐完美的视频、查找相似的产品或以惊人的准确度匹配面孔时，向量数据库很可能在幕后默默地工作。本指南将分解向量数据库的基础知识，探索它们的实际应用，并向您展示如何有效地开始使用它们。

## 什么是向量数据库？

向量数据库旨在存储和搜索向量，向量也称为多维空间中数据的数字表示。这些向量由 ML 模型创建，用于捕获非结构化数据的关键特征。

例如，可以使用像 [BERT](https://towardsdatascience.com/a-complete-guide-to-bert-with-code-9f87602e4a11/) 这样的语言模型将一个句子转换为 512 维的向量，而使用 [ResNet](https://thenewstack.io/how-to-get-the-right-vector-embeddings/) 可以将图像表示为 2048 维的向量。

这些数据库擅长通过计算向量之间的距离来进行相似性搜索，这使它们非常适合推荐系统、图像检索和异常检测等任务。

## 为什么要使用向量数据库？

向量数据库在传统数据库无法跟上步伐的领域中大放异彩：

- 它们在高维数据管理方面非常高效：向量数据库可以完美地处理具有数千个维度的嵌入。
- 快速
[近似最近邻 (ANN)](https://thenewstack.io/vector-search-what-you-need-to-know-before-getting-started/) 搜索：它们有助于使用高级算法（如分层可导航小世界 (HNSW) 或 Faiss）快速找到与您的查询最相似的向量。
- 专为扩展而构建：您可以管理数百万（甚至数十亿！）个向量，而不会牺牲性能。
- 无缝 AI 集成：向量数据库可以轻松地与 ML 工作流程集成，以驱动 AI 驱动的应用程序。

## 流行的向量数据库

近年来，为了满足对高维数据管理日益增长的需求，涌现出了几个向量数据库和工具。以下是三个需要注意的重要向量数据库：

[Milvus](https://milvus.io) 是一个开源的、高度可扩展的向量数据库，它支持多种索引算法，如 HNSW 和 [倒排文件索引](https://towardsdatascience.com/similarity-search-knn-inverted-file-index-7cab80cc0e79/) (IVF)。您可以将其与 TensorFlow 和 [PyTorch](https://thenewstack.io/why-pytorch-gets-all-the-love/) 等 ML 框架集成。[Pinecone](https://www.pinecone.io/?utm_content=inline+mention) 是一个托管的向量数据库，旨在易于使用，帮助您自动扩展到数百万个向量。它具有与云平台的原生集成，并提供低延迟搜索，而无需基础设施开销。[Weaviate](https://weaviate.io) 是一个开源向量数据库，非常注重知识图谱。它为语义搜索和 ML 提供原生支持，以及用于轻松集成的 RESTful API。

## 前提条件：了解嵌入

在深入研究向量数据库之前，掌握向量嵌入的概念至关重要，因为它们构成了这些数据库的基础。

### 什么是嵌入？

简而言之，嵌入是数据的密集数值表示，例如文本、图像或音频。这些表示是使用 ML 模型生成的，这些模型经过训练可以捕获数据中的底层模式、关系或特征。

嵌入不是处理原始数据，而是允许您将每个数据点表示为一个向量（一个数字列表），可以在数学空间中对其进行分析和比较。这些向量通常是高维的，并编码数据的“本质”。

例如：

- 像“The cat sat on the mat”这样的句子可以表示为 512 维的向量。
- 狗的照片可以转换为 2048 维的向量，以捕获其视觉特征，如形状、颜色和纹理。

### 为什么要使用嵌入？

嵌入对于处理传统数据库难以处理的非结构化数据特别强大。它们允许您：
**衡量相似度：** 通过计算两个数据点的向量之间的距离，比较它们的关联程度。

**对相似数据进行分组：** 在向量空间中，对具有共同特征的数据点进行聚类变得直观。

**执行高级任务：** 支持图像搜索、情感分析、推荐系统等应用。

### 如何创建嵌入？

要生成嵌入，可以使用预训练的 ML 模型或训练自己的模型。以下是不同数据类型的常见示例：

**文本嵌入：** 像 Hugging Face Transformers、BERT 或 GPT 模型这样的工具通常用于编码文本数据。

- 输入：一个句子或文档
- 输出：一个固定大小的向量（例如，512 维）
- 代码示例：

```
from transformers import AutoTokenizer, AutoModel
import torch

# Load a pre-trained model
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

# Encode a text input
text = "Understanding vector embeddings is crucial."
inputs = tokenizer(text, return_tensors="pt")
embeddings = model(**inputs).last_hidden_state.mean(dim=1)

print(embeddings.shape) # Output: torch.Size([1, 384])
```

**图像嵌入：** 像 ResNet、EfficientNet 或 [VGG](https://viso.ai/deep-learning/vgg-very-deep-convolutional-networks/) 这样的深度学习模型可以从图像中提取视觉特征。

- 输入：一张图片
- 输出：一个表示视觉模式的向量

像 [TensorFlow](https://thenewstack.io/python-tutorial-use-tensorflow-to-generate-predictive-text/) 或 PyTorch 这样的**框架**提供了预训练模型，简化了这个过程。

**音频嵌入：** 像 [OpenL3](https://github.com/marl/openl3) 这样的模型或基于自定义频谱图的神经网络将音频数据表示为向量。

**自定义嵌入：** 您还可以训练自己的模型，为特定领域的任务生成嵌入（例如，医学影像、DNA 序列或金融数据）。

### 嵌入的关键特征

**固定大小：** 嵌入通常是固定维度的，与输入大小无关。

**连续表示：** 与原始数据不同，嵌入存在于连续向量空间中，使其适用于基于距离的操作。

**特定于任务：** 嵌入经过定制，可以捕获与特定任务相关的模式（例如，文本的语义相似性或图像的视觉相似性）。

### 可视化嵌入

高维嵌入可能难以解释，但像 t-distributed stochastic neighbor embedding ([t-SNE](https://thenewstack.io/3-new-techniques-for-data-dimensionality-reduction-in-machine-learning/)) 或 Uniform Manifold Approximation and Projection for Dimension Reduction ([UMAP](https://umap-learn.readthedocs.io/en/latest/)) 这样的技术可以帮助在 2D 或 3D 中可视化它们。这些可视化揭示了数据点如何在嵌入空间中聚集和关联。

这是一个在 [Python](https://thenewstack.io/what-is-python/) 中使用 t-SNE 可视化文本嵌入的示例：

```
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np

# Generate sample embeddings
embeddings = np.random.rand(100, 512) # Replace with actual embeddings

# Reduce dimensionality
tsne = TSNE(n_components=2, random_state=42)
reduced_embeddings = tsne.fit_transform(embeddings)

# Plot
plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1])
plt.title("t-SNE Visualization of Embeddings")
plt.show()
```

## 掌握向量数据库：循序渐进

现在您了解了嵌入，让我们深入了解使用向量数据库的步骤。

### 1. 选择合适的向量数据库

选择错误的向量数据库可能会对您的产品造成灾难性的影响。要为您的用例选择合适的数据库，请考虑以下关键因素和指导。

#### 选择向量数据库时要考虑的因素

**用例要求：** 确定您希望通过向量数据库实现的目标。您是构建推荐引擎、视觉搜索平台还是欺诈检测系统？不同的数据库可能针对特定场景进行了优化，例如实时推荐与批量相似性搜索。

**是否具有足够的可扩展性？** 如果您正在处理小型数据集，则大多数向量数据库都能很好地运行。但是，随着您的数据集增长到数百万或数十亿个向量，您将需要一个支持水平扩展和优化索引以进行快速查询的数据库。

**了解索引技术：** 向量数据库依赖于索引算法来有效地搜索高维数据。常见的选项包括：

- HNSW（分层可导航小世界）：非常适合低延迟的最近邻搜索。
- IVF（倒排文件索引）：平衡了大型数据集的搜索准确性和速度。
- PQ（乘积量化）：压缩向量以节省空间，同时保持合理的准确性。
**将其与你的技术栈集成：** 确保数据库与你现有的工具和框架无缝集成。例如，如果你正在使用 Python，请寻找 Python SDK 或 API。

**你需要云端还是自托管？** 确定你需要完全托管的解决方案（如 Pinecone）还是更喜欢开源、自托管的选项（如 Milvus）。托管解决方案简化了部署，但成本更高。

**成本和许可：** 计算托管服务的成本或开源数据库的许可条款。开源工具可以免费使用，但需要额外的设置和维护工作。

#### 如何为你的项目选择最佳数据库

**定义你的数据集大小和增长：**

*   对于小型项目，请考虑轻量级和自托管的选项，如 Milvus。
*   对于大型项目，选择可扩展的解决方案，如 Pinecone 或水平扩展。

**评估你的查询速度需求：** 如果你需要实时查询（例如，推荐），请优先考虑具有低延迟 ANN 算法的数据库。

**考虑部署偏好：** 为了尽量减少开销，请选择像 Pinecone 这样的托管解决方案。为了经济高效和控制，请查看像 Milvus 或 Weaviate 这样的开源选项。

**测试多个选项：** 许多向量数据库提供免费试用版或开源版本。设置一个小规模的实现，并根据你的数据对其性能进行基准测试。

**关注社区和支持服务：** 像 Milvus 和 Weaviate 这样的开源数据库拥有活跃的社区。对于企业级支持，像 Pinecone 这样的托管解决方案可能更好。

### 2. 索引和查询你的数据

选择向量数据库后，下一步是索引和查询你的数据。这就是奇迹发生的地方；你的向量被存储、结构化，并可以搜索，用于各种应用，如推荐系统、语义搜索或异常检测。让我们以 Milvus 为例，详细了解这一步骤。

#### 向量数据库中的索引意味着什么？

向量数据库中的索引是指组织高维向量数据，以便能够快速、高效和准确地进行相似性搜索。如果没有适当的索引，在大型数据集中搜索向量可能会变得非常缓慢，使得实时应用几乎不可能实现。

常见的索引技术包括：

**HNSW：** 这提供了低延迟、高精度的搜索，非常适合实时应用。

**IVF：** 这对于平衡海量数据集上的速度和精度非常有效。

**Flat index：** 这执行详尽的搜索，最适合于较小的数据集或优先考虑精度的应用。

选择正确的索引方法取决于你的数据集大小、延迟要求和用例。

#### 示例：使用 Milvus 进行索引和查询

以下是如何使用 Milvus 索引和查询你的向量数据。

a. 设置你的 Milvus 环境：如果你没有安装和运行 Milvus，你可以使用 Docker 进行设置：

```
docker pull milvusdb/milvus:latest
docker run -d --name milvus -p 19530:19530 -p 9091:9091 milvusdb/milvus:latest
```

这将在你的本地机器上启动一个 Milvus 服务器，准备好接受连接。

b. 通过使用 `pymilvus` 库连接到 Milvus 以连接到数据库。

```
from pymilvus import connections
connections.connect("default", host="localhost", port="19530")
```

c. 定义你的数据模式。模式概述了你的向量数据将如何存储。此示例定义了一个集合，其中包含一个整数 ID 和一个 512 维的向量字段：

```
from pymilvus import FieldSchema, CollectionSchema, Collection

fields = [
    FieldSchema(name="id", dtype="INT64", is_primary=True, auto_id=True),
    FieldSchema(name="embedding", dtype="FLOAT_VECTOR", dim=512)
]
schema = CollectionSchema(fields, description="Vector collection")
collection = Collection(name="vector_data", schema=schema)
```

d. 插入数据 - 生成或加载向量嵌入（例如，来自 ML 模型）并将它们插入到集合中。这是一个使用随机向量的示例：

```
import numpy as np

embeddings = np.random.rand(10, 512).tolist()
collection.insert([embeddings])
print(f"Inserted {len(embeddings)} vectors!")
```

e. 索引你的数据。插入数据后，你可以选择一种索引方法以进行高效查询。例如，使用 HNSW：

```
index_params = {"index_type": "HNSW", "metric_type": "L2", "params": {"M": 16, "efConstruction": 500}}
collection.create_index(field_name="embedding", index_params=index_params)
print("Index created!")
```

f. 查询你的数据。最后，执行相似性搜索以查找最接近给定查询向量的向量。例如：

```
results = collection.search(
    data=[embeddings[0]],  # Query vector
    anns_field="embedding",
    param={"metric_type": "L2", "params": {"ef": 50}},
    limit=5
)

for result in results:
    print(result)
```

此代码使用 L2（欧几里得）距离度量检索与查询向量最接近的五个向量。

### 3. 优化性能
优化向量数据库的性能对于高效处理大规模数据集，同时保持低延迟和高准确性至关重要。无论您是构建推荐系统、进行语义搜索还是检测异常，性能调优都能确保您的应用程序可以扩展并满足用户期望。让我们探讨如何有效地优化您的向量数据库。

#### a. 选择正确的索引算法

索引算法决定了向量的存储和检索方式，直接影响查询速度和准确性。以下是三个流行的选项：

**IVF:** 将向量空间分成簇，并在查询期间仅搜索相关的簇。最适合在大型数据集中平衡速度和准确性。
**HNSW:** 一种基于图的方法，可确保低延迟和高精度搜索，非常适合个性化推荐等实时应用程序。
**PQ:** 将向量压缩为紧凑的代码，从而实现内存高效的存储和快速的近似搜索，使其适用于具有海量数据集和有限资源的场景。

*重要提示：首先在数据的子集上测试不同的算法，以找到最适合您特定用例的算法。*

#### b. 使用批量操作

在处理大规模数据集时，批量处理可以显着提高性能。与其一次插入或查询一个向量，不如使用批量插入将它们分组处理：

- 添加数据时，使用批量操作来最大限度地减少开销。大多数向量数据库（如 Milvus 和 Pinecone）都支持一次插入数千个向量，从而减少了花费在网络通信和数据处理上的时间。

```python
import numpy as np

# Generate a batch of 10,000 embeddings
batch_embeddings = np.random.rand(10000, 512).tolist()
collection.insert([batch_embeddings])
print(f"Inserted {len(batch_embeddings)} vectors in a batch!")
```

- 批量查询：同时执行多个查询以减少延迟，尤其是在并行检索多个用户的相似项目等场景中。

*它为什么有效：批量操作减少了发送到数据库的请求数量，并利用了底层优化（如并行处理）。*

#### c. 利用硬件加速

对于计算密集型任务（例如构建索引或对高维数据执行查询），使用专用硬件可以显着提高性能。

**GPU:** 图形处理单元擅长并行计算，使其非常适合加速向量运算（如索引和搜索）。许多现代向量数据库原生支持 GPU 加速。
**TPU:** 张量处理单元（可在 Google Cloud 等平台上使用）也可用于涉及向量计算的专用 ML 工作负载。
**高性能 CPU:** 通过使用多线程功能进行扩展来优化 CPU 使用率，确保服务器可以高效地处理并发查询。

*示例：如果您要部署支持 GPU 的 Milvus，请使用 `gpu.build_index` 配置来启用更快的索引。*

#### d. 监控和调整性能指标

持续的性能监控是确保向量数据库以最佳方式运行的关键。以下是一些需要关注的指标：

**查询延迟：** 衡量检索单个查询结果所需的时间。对于实时应用程序，目标是亚秒级延迟。
**索引构建时间：** 评估构建索引所需的时间，尤其是在您频繁更新数据集时。
**内存使用情况：** 监控内存消耗以避免瓶颈，尤其是在处理大型数据集或在资源受限的硬件上运行时。

*重要提示：使用 Prometheus 等工具或向量数据库中的内置监控功能来跟踪这些指标随时间的变化。*

#### e. 优化搜索参数

调整搜索参数可以进一步提高查询效率，而不会影响准确性。

**ef (HNSW):** 值越高，搜索准确性越高，但会增加延迟。从适中的值开始，并根据您的应用程序的要求进行调整。
**nprobe (IVF):** 定义要在 IVF 中搜索多少个簇。增加 `nprobe` 可以提高准确性，但会降低速度。

- 以下是 Milvus HNSW 索引的示例：

```python
search_params = {"metric_type": "L2", "params": {"ef": 50}}
results = collection.search(
    data=[query_vector],
    anns_field="embedding",
    param=search_params,
    limit=10
)
```

#### f. 缓存频繁访问的结果

对于具有重复查询的应用程序（例如，热门产品推荐），实施缓存层以立即提供结果。 [Redis](https://redis.com/?utm_content=inline+mention) 或 [Memcached](https://thenewstack.io/cache-vs-database-has-performance-converged/) 等工具可以与向量数据库很好地协同工作。

## 实际应用

向量数据库为各种创新用例提供支持，使其成为现代机器学习和 AI 应用程序不可或缺的一部分。

### 1. 推荐系统
通过利用向量相似性搜索，提供高度个性化的建议。

- 电子商务：通过比较相似商品的嵌入，根据用户的浏览历史或购买记录推荐商品。
- 娱乐：通过将用户偏好与内容嵌入进行匹配，推荐电影、音乐或文章。

向量嵌入捕获项目和用户之间细微的关系，提供感觉直观和个性化的推荐。

### 2. 视觉搜索

使用户能够使用图像而不是文本进行搜索：

- 零售：允许客户上传照片并找到视觉上相似的产品，例如服装或配饰。
- 医疗保健：将医学图像（如 X 射线或 MRI）与数据库进行比较，以进行模式识别和诊断。

从神经网络中提取的嵌入可以表示图像的视觉特征，即使在庞大的数据集中也能实现精确搜索。

### 3. 异常检测

实时识别罕见或不寻常的模式。

- 金融：通过将交易嵌入与典型的行为模式进行比较，检测欺诈交易。
- IoT 设备：监控传感器数据中的异常情况，这些异常情况可能表明硬件故障或网络安全威胁。

向量距离可以轻松地发现复杂数据集中的异常值，而无需手动创建规则。

### 4. 自然语言理解

改变机器处理和理解人类语言的方式。

- 搜索引擎：通过将用户查询与文档嵌入进行匹配以获得准确的结果，从而支持语义搜索。
- 聊天机器人：通过理解用户意图并提供相关响应来增强对话式[代理](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)。
- 翻译工具：通过分析单词、短语和句子之间的关系来改进上下文感知的翻译。

文本嵌入将单词和短语转换为捕获其含义和上下文的数学表示形式。

## 挑战和未来趋势

尽管向量数据库功能强大，但仍有一些挑战需要解决，并且令人兴奋的趋势正在塑造它们的未来。

### 挑战

当涉及到管理数十亿个向量同时保持闪电般快速的查询速度时，可扩展性绝非易事。 解决方案在于利用先进的索引方法和分布式架构。

混合查询，例如将结构化搜索（例如，“100 美元以下的产品”）与向量相似性搜索相结合，提出了另一个持续存在的挑战。 混合搜索引擎的创新正在迅速发展，以应对这种复杂性。

隐私是另一个关键问题。 如果没有适当的保护措施，嵌入可能会无意中暴露敏感信息。 这就是为什么像差分隐私和加密这样的方法对于确保数据安全至关重要。

### 未来趋势

索引方面的进步正在通过下一代算法（如可学习索引）改变游戏规则，这些算法将提高查询效率和精度。 在硬件方面，人工智能加速器和 GPU 等专用工具正在降低成本，同时显着加快向量数据库操作。 随着人工智能通过预训练模型和托管向量数据库服务变得更容易访问，即使是小型团队现在也可以轻松利用基于向量的解决方案的力量。

## 结论

向量数据库正在重新定义我们处理非结构化数据的方式，从而推动人工智能和机器学习的重大突破。 无论您是构建个性化推荐系统、启用语义搜索还是检测异常，利用向量数据库的力量都可以释放新的创新机会。

通过了解基础知识、选择正确的数据库并优化其在实际场景中的使用，您可以充分利用这些前沿工具。 随着技术的发展，向量数据库将在塑造人工智能驱动的解决方案方面发挥更大的作用。 现在是探索它们的潜力并将您的数据驱动项目提升到新水平的时候了。 让我们开始吧！

*从设置到优化，通过 Andela 的八步指南“如何在 Kubernetes 上运行数据库”释放 Kubernetes 的力量并掌握数据库管理。*
[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。 订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)