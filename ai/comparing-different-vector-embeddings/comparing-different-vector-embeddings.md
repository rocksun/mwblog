<!-- 
# 比较不同的向量嵌入
https://cdn.thenewstack.io/media/2023/08/1f97e3fa-vector1-1024x683.jpg
Image from alice-photo on Shutterstock.
-->

不同神经网络生成的向量嵌入有什么区别，如何在Jupyter Notebook中评估它们？

译自 [Comparing Different Vector Embeddings](https://thenewstack.io/comparing-different-vector-embeddings/) 。

大语言模型(LLM)正在风靡，我们正面临着 [ChatGPT](https://zilliz.com/learn/ChatGPT-Vector-Database-Prompt-as-code) 等语言应用的新范式。向量数据库将是栈的核心部分。所以，理解向量及其重要性非常重要。

这个项目展示了不同模型之间的向量嵌入的区别，并展示了如何在一个 [Jupyter Notebook](https://zilliz.com/blog/exploring-magic-vector-databases-jupyter-notebooks) 中使用多个向量数据集合。在这篇文章中，我们将介绍什么是向量嵌入，为什么它们很重要，以及如何在 Jupyter Notebook 中比较不同的向量嵌入。

## 什么是向量嵌入以及为什么它们很重要？

![](https://cdn.thenewstack.io/media/2023/08/f3f2aed5-image1-e1690992552989.png)
*向量嵌入从何而来？*

简单来说，向量嵌入是数据的数值表示。它们主要用于表示[非结构化数据](https://zilliz.com/blog/introduction-to-unstructured-data)。非结构化数据是图像、视频、音频、文本、分子图像和[其他没有正式结构的数据](https://thenewstack.io/what-is-unstructured-data/)。向量嵌入是通过将输入数据馈送到预先训练的神经网络并获取倒数第二层的输出而生成的。

神经网络具有不同的架构，并在不同的数据集上进行训练，这使每个模型的向量嵌入都是独一无二的。这就是使用非结构化数据和向量嵌入为何具有挑战性的原因。后面我们将看到，在不同数据集上微调的具有相同基础的模型可以产生不同的向量嵌入。

神经网络的差异也意味着我们必须使用不同的模型来处理各种形式的非结构化数据并生成它们的嵌入。例如，您不能使用句子转换器模型为图像生成嵌入。另一方面，您不会想要使用ResNet50(一个图像模型)为句子生成嵌入。因此，找到适合您的数据类型的模型非常重要。

## 如何比较向量嵌入？

接下来，让我们看看如何比较它们。本节比较了基于 Hugging Face 的 MiniLM 的三种不同的多语言模型。比较向量有许多种方法。在这个示例中，我们使用 L2 距离指标和一个倒排文件索引作为向量索引。

对于这个项目，我开发了一些灵感来自 Taylor Swift 最近专辑发行的自己的数据，直接在 Jupyter Notebook 中定义。你可以使用我的例子，或者想出你自己的句子。一旦我们有了数据，我们就获取不同的嵌入，并将两组嵌入存储在像 Milvus 这样的向量数据库中。我们使用第三个模型的嵌入来查询它们进行比较。

我们希望看到搜索结果是否不同，以及搜索结果之间有多远。在生产环境中，您会想知道希望看到的结果，然后根据返回的结果进行检查。

### 比较不同模型的向量嵌入

我们比较的三个模型是 Sentence Transformers 的基于 MiniLM 的[多语言释义模型](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2)，一个[进行过意图检测微调](https://huggingface.co/hroth/psais-paraphrase-multilingual-MiniLM-L12-v2-5shot)的版本，以及一个 [Sprylab 进行了微调但没有详细说明调优目的](https://huggingface.co/Sprylab/paraphrase-multilingual-MiniLM-L12-v2-fine-tuned-3)的版本。 在我的笔记本电脑上运行这三个兼容模型是这个项目最艰难的部分之一。

为了比较向量嵌入，我们需要等长的向量。在这个例子中，我们使用 384 维向量，这是根据 MiniLM 句子变换器模型。请注意，这并不意味着我们为每个数据创建 384 个“特征”或“类别”，而是在 384 维空间中生成数据的抽象表示。例如，没有维度会表示任何词性，句子中的单词数，某事是否是专有名词或任何概念化的东西。

### 向量嵌入比较数据

我们使用句子转换器模型，这意味着我们的数据应该是句子的形式。我建议至少有 50 句话进行比较。示例笔记本包含 51 个。我也建议使用具有某些相似性的数据。在这个例子中，我使用了 Taylor Swift 的四首歌的歌词：“Speak Now,” “Starlight,” “Sparks Fly” 和 “Haunted”。

我选择这些歌曲，因为许多歌词形成完整的句子，所以从歌词格式转为句子格式很容易。我还想测试一个假设。前三首歌或多或少都是情歌，而最后一首“Haunted”更像是分手歌。所以我假设“Haunted”出现在前三首歌曲的返回结果中的可能性要小得多。

## 在 Jupyter 笔记本中比较向量嵌入

让我们进入代码。使用 Milvus Lite，Milvus 的轻量版本，您可以直接在 Jupyter Notebook 中比较向量嵌入。 对于这个示例代码，您需要 `! pip install pymilvus milvus sentence-transformers`。这个项目只需要少量导入;`time` 库是可选的。 运行导入后，从 Milvus 启动 `default_server` 并建立连接。

```python
from sentence_transformers import SentenceTransformer
from milvus import default_server
from pymilvus import connections, utility, FieldSchema, CollectionSchema, DataType, Collection
from time import time


default_server.start()
connections.connect(host="127.0.0.1", port=default_server.listen_port)
```

从 Hugging Face 获取 Sentence Transformer 模型

第 1 步是获取我们的向量嵌入模型。我们在这个例子中使用多语言释义 MiniLM 系列。第一个是规范版本。接下来的两个是调优过的不同版本。这个模型选择为我们提供了一个清晰的例子，说明微调如何明显改变你的向量。

```python
v12 = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
ft3_v12 = SentenceTransformer("Sprylab/paraphrase-multilingual-MiniLM-L12-v2-fine-tuned-3")
ft5_v12 = SentenceTransformer("hroth/psais-paraphrase-multilingual-MiniLM-L12-v2-5shot")
```

### 在向量数据库的两个集合中加载数据集

我在下面列出了 Taylor Swift “立即演讲”专辑中的 51 句话。随意复制粘贴这段代码。或者如果你愿意，可以读一读；她是位了不起的歌词作者。

```
# inspired by Speak Now (Taylor’s Version)
# Lyrics from: Speak Now, Starlight, Sparks Fly, Haunted
sentences = [
“I am not the kind of girl, who should be rudely barging in on a white veil occasion, but you are not the kind of boy who should be marrying the wrong girl”,
“I sneak in and see your friends and her snotty little family all dressed in pastel and she is yelling at a bridesmaid somewhere back inside a room wearing a gown shaped like a pastry”,
“This is surely not what you thought it would be.”,
“I lose myself in a daydream where I stand and say, ‘Don’t say yes, run away now I’ll meet you when you’re out of the church at the back door.'”,
“Don’t wait, or say a single vow you need to hear me out and they said, ‘Speak now’.”,
“Fond gestures are exchanged.”,
“And the organ starts to play a song that sounds like a death march.”,
“And I am hiding in the curtains, it seems that I was uninvited by your lovely bride-to-be.”,
“She floats down the aisle like a pageant queen.”,
“But I know you wish it was me you wish it was me don’t you?”,
“I hear the preacher say, ‘Speak now or forever hold your peace'”,
“There’s the silence, there’s my last chance.”,
“I stand up with shaky hands, all eyes on me”,
“Horrified looks from everyone in the room but I’m only looking at you.”,
“And you’ll say, ‘Let’s run away now’ I’ll meet you when I’m out of my tux at the back door”,
“Baby, I didn’t say my vows So glad you were around When they said, ‘Speak now'”,
“I said, ‘Oh my, what a marvelous tune'”,
“It was the best night, never would forget how we moved.”,
“The whole place was dressed to the nines and we were dancing, dancing like we’re made of starlight”,

“I met Bobby on the boardwalk summer of ’45”,
“Picked me up late one night out the window we were seventeen and crazy running wild, wild.”,
“Can’t remember what song he was playing when we walked in.”,
“The night we snuck into a yacht club party pretending to be a duchess and a prince.”,
“He said, ‘Look at you, worrying so much about things you can’t change You’ll spend your whole life singing the blues If you keep thinking that way'”,
“He was tryna to skip rocks on the ocean saying to me ‘Don’t you see the starlight, starlight don’t you dream impossible things'”,
“Ooh, ooh he’s talking crazy Ooh, ooh dancing with me Ooh, ooh we could get married Have ten kids and teach ’em how to dream”,
“The way you move is like a full on rainstorm.”,
“And I’m a house of cards”,
“You’re the kind of reckless that should send me running but I kinda know that I won’t get far”,
“And you stood there in front of me just close enough to touch”,
“Close enough to hope you couldn’t see what I was thinking of”,
“Drop everything now”,
“Meet me in the pouring rain”,
“Kiss me on the sidewalk”,
“Take away the pain”,
“Cause I see sparks fly, whenever you smile”,
“Get me with those green eyes, baby as the lights go down”,
“Gimme something that’ll haunt me when you’re not around”,
“My mind forgets to remind me you’re a bad idea”,
“You touch me once and it’s really something you find I’m even better than you imagined I would be”,
“I’m on my guard for the rest of the world but with you, I know it’s no good”
“And I could wait patiently but I really wish you would”
“I run my fingers through your hair and watch the lights go wild”,
“Just keep on keeping your eyes on me it’s just wrong enough to make it feel right”,
“And lead me up the staircase won’t you whisper soft and slow, I’m captivated by you, baby like a fireworks show”,
“You and I walk a fragile line I have known it all this time, But I never thought I’d live to see it break”,
“It’s getting dark and it’s all too quiet And I can’t trust anything now And it’s coming over you like it’s all a big mistake”,
“Oh, I’m holding my breath Won’t lose you again”,
“Something’s made your eyes go cold”,
“Come on, come on, don’t leave me like this I thought I had you figured out”,
“Something’s gone terribly wrong you’re all I wanted”,
“Can’t breathe whenever you’re gone can’t turn back now, I’m haunted”,
“I just know You’re not gone, you can’t be gone, no”,
]
```

我们必须首先定义模式以将数据放入向量数据库。 对于这个例子，我们为两个集合使用相同的模式，所以我们只需要做一个。 不过，请确保创建两个集合。

一旦集合准备就绪，我们就将所有句子编码为它们模型的嵌入，并定义向量索引参数。 我们使用 L2 作为距离度量，使用四个质心的倒排文件索引。 毕竟，只有 51 个条目。 然后我们获取格式化数据并将其加载到 Milvus 中。

```python
# object should be inserted in the format of (title， date， location， speech embedding)
fields = [
    FieldSchema(name="id"， dtype=DataType.INT64， is_primary=True， auto_id=True)，
    FieldSchema(name="sentence"， dtype=DataType.VARCHAR， max_length=500)，
    FieldSchema(name="embedding"， dtype=DataType.FLOAT_VECTOR， dim=DIMENSION)，
]
schema = CollectionSchema(fields=fields)
collection_v12 = Collection(name=COLLECTION_V12， schema=schema)
collection_v12_ft5 = Collection(name=COLLECTION_V12_Q， schema=schema)


v12_embeds = {}
v12_q_embeds = {}
for sentence in sentences:
    v12_embeds[sentence] = v12.encode(sentence)
    v12_q_embeds[sentence] = ft5_v12.encode(sentence)


index_params = {
    "index_type": "IVF_FLAT"，
    "metric_type": "L2"，
    "params": {"nlist": 4}， 
}
collection_v12.create_index(field_name="embedding"， index_params=index_params)
collection_v12.load()
collection_v12_ft5.create_index(field_name="embedding"， index_params=index_params)
collection_v12_ft5.load()


for sentence in sentences:
    v12_insert = [
        {
            "sentence": sentence，
            "embedding": v12_embeds[sentence]
        }
    ]
        ft_insert = [
        {
            "sentence": sentence，
            "embedding": v12_q_embeds[sentence]
        }
    ]


    collection_v12.insert(v12_insert)
    collection_v12_ft5.insert(ft_insert)


collection_v12.flush()
collection_v12_ft5.flush()
```

### 查询向量存储以比较嵌入

接下来，是时候进行比较了。 在这个例子中，我们将使用前两个句子。 我们使用第三个模型为它们生成向量嵌入。

```python
search_embeds = {}
search_data = []
for sentence in sentences[0:2]:
    vector_embedding = ft3_v12.encode(sentence)
    search_embeds[sentence] = vector_embedding
    search_data.append(vector_embedding)
```

现在我们查询 Milvus。 我也在跟踪时间。 我得到的搜索时间如下所示。 一定要在搜索参数下传递相同的度量类型。

![](https://cdn.thenewstack.io/media/2023/08/6ad1c5b6-screenshot-2023-08-02-at-11.58.59-am.jpg)

```python
start1 = time()
res_v12 = collection_v12.search(
    data=search_data， # Embeded search value 
    anns_field="embedding"， # Search across embeddings
    param={"metric_type": "L2"，
        "params": {"nprobe": 2}}， 
    limit = 3， # Limit to top_k results per search
    output_fields=["sentence"])
time1 = time() - start1
print(f"Time for first search: {time1}")
start2 = time()
res_v12_ft5 = collection_v12_ft5.search(
    data=search_data， # Embeded search value
    anns_field="embedding"， # Search across embeddings 
    param={"metric_type": "L2"，
        "params": {"nprobe": 2}}，
    limit = 3， # Limit to top_k results per search
    output_fields=["sentence"]) 
time2 = time() - start2
print(f"Time for second search: {time2}")
```

现在让我们看看结果并进行比较。 我们看到原始模型与 Sprylab 调优的版本之间出现惊人的相似结果。 唯一的区别是返回的第一个结果是句子本身。 这告诉我们结果在两个和三个对这两个向量空间中的两个示例搜索句子而言比它们相互之间更相似。

```python
for i， hits in enumerate(res_v12):
    for hit in hits:
        print(f"Query sentence: {sentences[i]}") 
        print(f"Nearest Neighbor Number {i}: {hit.entity.get('sentence')} ---- {hit.distance}\n")
```

![](https://cdn.thenewstack.io/media/2023/08/a22ba851-image5-e1690992374935.png)

接下来，让我们比较两个调优后的模型。 从这些结果中，我们将看到以“I’m on my guard for the rest of the world …”开头的句子在语义上与我们的搜索句子相似，因为它出现在两个比较中。 这里有两个有趣的要点：1)第一个查询的不同结果，2)第二个查询句子不出现在第一个的前三名，但相反情况也成立。

```python
for i， hits in enumerate(res_v12_ft5):
    for hit in hits:
        print(f"Query sentence: {sentences[i]}")
        print(f"Nearest Neighbor Number {i}: {hit.entity.get('sentence')} ---- {hit.distance}\n")
```

![](https://cdn.thenewstack.io/media/2023/08/46f1c813-image3-e1690992480165.png)

## 总结

在本教程中，我们学习了向量嵌入及如何比较它们，并使用自定义数据进行了一些比较。额外的收获是，我们还展示了一个如何同时使用两个不同集合的示例。 这就是您可以查询不同潜在向量空间的方式。

我们展示了一个模型及其一些微调版本之间的区别。 我们还看到一个结果在两个嵌入空间中都出现。 在多个向量表示中出现查询结果意味着该查询在许多方面都必须在语义上相似。 下一步，尝试用图像模型、不同维度的语言模型或您的数据来做这些。
