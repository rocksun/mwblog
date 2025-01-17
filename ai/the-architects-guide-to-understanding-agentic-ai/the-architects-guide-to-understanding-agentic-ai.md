
<!--
title: 架构师理解自主式AI指南
cover: https://cdn.thenewstack.io/media/2025/01/6061276b-ai.jpg
-->

自主式AI是基于现有能力和即将实现的能力的AI的下一个合乎逻辑的进化发展。

> 译自 [The Architect’s Guide to Understanding Agentic AI](https://thenewstack.io/the-architects-guide-to-understanding-agentic-ai/)，作者 Keith Pijanowski。

通常，在评估一项备受炒作的新技术的合法性时，研究其现有的核心能力和历史是有帮助的。如果所讨论的新技术并非基于现有或即将具备的能力，我们可以将其标记为炒作并继续前进。

另一个历史可以帮助我们应用的试金石只需要常识。这项新技术是否符合现有趋势？它是否是进步方向上的下一个逻辑步骤？它是否解决了以前难以解决或无法解决的问题？

在本架构师关于[理解自主 AI](https://thenewstack.io/agentic-ai-tools-for-building-and-managing-agentic-systems/)的指南中，我希望展示自主 AI 是基于现有能力和触手可及的能力的 AI 的下一个逻辑进化。

让我们从回顾 AI 多年来是如何发展的开始。许多人认为 AI 经历了三个浪潮，因此我将在下一节中介绍每个 AI 浪潮。为了趣味性，我还将指出企业为了在每个 AI 浪潮中取得成功而需要获取的额外资源。

## AI 的三个浪潮

AI 的第一个浪潮是传统 AI，有时称为预测性 AI，这非常简单。给模型一个输入，就会做出预测。预测可以是一个唯一值（回归）、输入的分类或输入的分类。这些功能对于图像分类、邮件排序（分类）和预测销售额（回归）等任务很有用。

第一个浪潮为我们带来了神经网络，这是一个复杂的相互连接的节点（神经元）系统，它可以从数据中学习并根据在训练数据中识别的模式做出预测。（以前，模型是使用预先构建的算法创建的，这些算法具有明确的步骤以实现特定结果。）神经网络可以找到数百甚至数千个值的输入中的模式。为了在传统 AI 中取得成功，组织必须添加一个[数据湖](https://thenewstack.io/the-architects-guide-a-modern-data-lake-reference-architecture/)来存储训练集、验证集、测试集和模型本身。此外，通常需要改进计算能力，例如向数据中心添加 GPU，因为这允许工程师在模型开发过程中运行更多实验。

![AI 的三个浪潮](https://cdn.thenewstack.io/media/2025/01/033b257d-image1.png)

*AI 的三个浪潮。*

AI 的第二个浪潮为我们带来了生成式 AI，它可以生成新的内容。这可以采取回答问题、总结冗长复杂的文档甚至以能够通过图灵测试的流畅度进行完整对话的形式。

[生成式 AI](https://thenewstack.io/the-architects-guide-to-the-genai-tech-stack-10-tools/) 为我们带来了[大型语言模型 (LLM)](https://roadmap.sh/guides/introduction-to-llms)，它们比第一波中介绍的神经网络更加复杂。这些神经网络基于 2017 年论文“[注意力是你所需要的一切](https://arxiv.org/abs/1706.03762)”中概述的编码器/解码器架构。

如今，最先进的 LLM 具有数十亿个参数，很快我们将拥有一个万亿参数的 LLM。为了在 LLM 中取得成功，组织必须向其数据中心添加一些额外的资源和工作负载，例如数据湖仓储、检索增强生成 (RAG)、LLM 微调、向量数据库和自定义语料库（通常使用对象存储构建）。

现在，我们正在进入第三个浪潮，即自主 AI。自主 AI 系统可以规划、采取行动，甚至修改原始计划以改进结果。虽然前两个 AI 浪潮侧重于进行预测和生成内容，但我们现在正在见证更复杂事物的出现：能够独立规划、执行任务并在产生不良结果时修改原始计划的 AI 智能体。AI 的第三个浪潮代表了人工智能用于解决问题的方式的转变。在自主 AI 中取得成功将需要比前几个浪潮更多的计算能力，并且可能需要编排工具来帮助 LLM 管理规划。

诚然，最后一个浪潮听起来有点像科幻小说。这听起来像是从前一个浪潮迈出了太大的飞跃。毕竟，我们怎么能从能够回答问题、总结和对话的生成式 AI 转向能够规划、采取行动和修改的自主 AI 呢？为了解决这个问题，我们需要看看我们今天如何使用 LLM，并看看仅仅通过一点点工程就能实现什么。我们还需要研究业务流程的构成，并寻找自主 AI 可以增加价值的领域。

## 我们今天如何使用 LLM

如今的LLM使用的是所谓的“零样本提示”。换句话说，LLM被要求尽可能快地仅使用“心智中的”信息或参数记忆中 readily accessible 的信息来创建响应。例如，假设你有一个问题“X”要发送给LLM。本质上，你是在要求LLM执行以下操作：“请一步到位地回答我的问题‘X’，不要使用Backspace键、Delete键或箭头键返回并重做答案的任何部分。不要将我的问题分解成更小的任务，也不要检查答案的准确性。”这有时被称为要求LLM快速思考。

令人惊讶的是，LLM能够使用零样本提示组合出一个连贯且组织良好的响应，因为它们是机器。如果人类试图以这种方式交流，结果将是一连串毫无意义的词语。如果你思考一下自己回答问题时的思维过程，你会发现自己会将原始问题分解成更容易回答的更小的问题——将所有答案组合起来形成对原始问题的答案，然后，在你说话之前，你会检查答案并可能修改它。所有人类都是这样思考的——没有人聪明到他们的思维能够以零样本的方式运作并产生与计划和修改后的响应一样好的结果。即使是威廉·福克纳在创作《喧嚣与骚动》中认知能力受损、感知支离破碎的本吉·康普森的“零样本思想”时，也进行了计划和修改。

以上两个例子引出了一个问题：“如果我们允许LLM进行计划和修改，它们能做什么？”这就是自主AI的承诺：让LLM超越一次性响应，并允许它们计划、审查和修改响应。但在讨论LLM如何进行计划和修改之前，我们需要了解当今业务流程的构成。

## 业务流程的构成

所有业务流程都可以分解成两个层面：控制层面和工具层面。见下图。工具层面是API、存储过程和与业务伙伴的外部网络调用的集合。但是，对于已经开始AI之旅的组织来说，它还可以包括对传统机器学习模型（第一波）和以“一次性”模式运行的LLM（第二波）的调用。

![业务流程的控制层面和工具层面](https://cdn.thenewstack.io/media/2025/01/48e648aa-image2-1024x586.png)

*业务流程的控制层面和工具层面。*

控制层面包含业务流程的逻辑。在这里，条件分支、循环和对组织工具层面的调用被协调起来以解决问题或实现自动化。要理解自主AI的价值和前景，你必须了解控制层面及其当前构建方式的两个方面：

- 它在设计时是硬编码的。在运行时，它不能更改。
- 它是由可能并不完全了解组织运营领域范围的工程师构建的。此外，他们可能不熟悉工具层面内的所有功能。这在运营于金融服务等复杂行业的庞大组织中尤其如此。即使是独立的服务也可以被认为具有控制层面和工具层面。控制层面是用编程语言的条件语句和循环结构构建的。工具层面是内置库和引用的第三方库的集合。底线是，任何你用软件构建的东西都有控制层面和工具层面。

## 自主AI的承诺
自主AI的承诺是使用LLM全面了解组织的工具层面，并允许它们构建和执行控制层面所需的逻辑。这可以通过向在组织的工具层面经过微调的LLM提供“少样本”提示来实现。下面是一个“少样本”提示的示例，它回答了前面提出的相同假设问题。这也称为让LLM缓慢思考。

少样本提示示例：

1. 将我的问题“X”分解成更小的问题。
2. 为每个较小的问题编写一份草稿回复。
3. 考虑需要修改或进一步研究的较小问题。
4. 你需要任何额外的研究吗？
5. 修改你的答案。
6. 将所有内容整合在一起。
7. 检查你的最终回复。

上述任务的假设是，较小的问题可以与LLM意识到的内部工具配对，并且响应（或答案）伴随着一个确定性等级，该等级指示工具对答案的信心程度。像修改任务和审查最终答案这样的防护措施是上述过程中最重要的步骤。

如果智能代理AI仍然显得过于神奇，那么请考虑以下简单的例子。每个每天都要编写代码的开发人员可能都会问LLM类似于以下的问题：

“写一个连接到MinIO的迭代式数据集函数。”

```python
from minio import Minio
from minio.error import S3Error

class MinIOIterableDataset:
    def __init__(self, endpoint, access_key, secret_key, bucket_name, prefix='', secure=True):
        """
        Initialize the MinIOIterableDataset.
        :param endpoint: The endpoint of the MinIO server (e.g., 'localhost:9000').
        :param access_key: Access key for MinIO.
        :param secret_key: Secret key for MinIO.
        :param bucket_name: The bucket name to fetch objects from.
        :param prefix: Prefix to filter objects by (optional).
        :param secure: Use HTTPS if True, otherwise HTTP.
        """
        self.client = Minio(endpoint, access_key, secret_key, secure=secure)
        self.bucket_name = bucket_name
        self.prefix = prefix
        # Check if the bucket exists
        if not self.client.bucket_exists(bucket_name):
            raise ValueError(f"Bucket '{bucket_name}' does not exist.")

    def __iter__(self):
        """
        Iterator to fetch objects from the bucket.
        Yields: A dictionary containing object metadata and data content.
        """
        try:
            for obj in self.client.list_objects(self.bucket_name, prefix=self.prefix, recursive=True):
                data = self.client.get_object(self.bucket_name, obj.object_name)
                yield {
                    "object_name": obj.object_name,
                    "size": obj.size,
                    "etag": obj.etag,
                    "last_modified": obj.last_modified,
                    "content": data.read()
                }
                data.close()
                data.release_conn()
        except S3Error as e:
            raise RuntimeError(f"Error accessing MinIO bucket: {str(e)}") from e

# Example usage
if __name__ == "__main__":
    # Configuration
    endpoint = "localhost:9000"
    access_key = "your-access-key"
    secret_key = "your-secret-key"
    bucket_name = "my-bucket"
    prefix = "data/"  # Optional: Specify a prefix to filter objects
    dataset = MinIOIterableDataset(endpoint, access_key, secret_key, bucket_name, prefix)
    # Iterate over the dataset
    for item in dataset:
        print(f"Object Name: {item['object_name']}, Size: {item['size']} bytes")
        # Access the content with item['content'], e.g., item['content'].decode('utf-8')

```

ChatGPT被用来生成上面的响应。我们在响应中看到的是使用Python作为控制平面来协调对MinIO SDK和PyTorch中函数的调用，它们是工具平面的例子。响应还告诉我们ChatGPT已经接受过Python、MinIO和PyTorch文档的训练。通过从LLM的知识及其知识获取方式的角度分析这些结果，我们可以得出结论，训练LLM使用编排工具和组织内部工具来动态生成业务流程的控制平面并非难事。

## 结论

智能代理AI是AI的下一个逻辑发展阶段。它基于在AI的第一和第二波浪潮中拥有坚实基础的能力。其前景是利用AI来解决更复杂的问题，使其能够进行规划、执行任务和修正——换句话说，使其能够缓慢地思考。这也承诺会产生更准确的响应。

智能代理AI没有捷径可走。智能代理AI可能是AI的第三波浪潮，但它并没有取代前两波浪潮——它是在前两波浪潮的基础上构建的。因此，最好的方法是从构建具有对象存储的AI数据基础设施开始。[对象存储](https://thenewstack.io/the-architects-guide-to-using-ai-ml-with-object-storage/)也可用于云回迁和构建数据湖仓。从那里开始，通过添加MLOps工具和工作负载来支持LLM，例如微调、检索增强生成、分布式计算和MLOps，逐步构建堆栈。
