# 教程：基于 ChatGPT 构建奥斯卡金像奖问答机器人

本教程将引导您通过一个实际示例，使用 GPT 3.5 的检索增强生成功能，根据自定义数据集回答问题。

翻译自 [Tutorial: Build a Q&A Bot for Academy Awards Based on ChatGPT](https://thenewstack.io/tutorial-build-a-qa-bot-for-academy-awards-based-on-chatgpt/) 。

![](https://cdn.thenewstack.io/media/2023/07/bda650c3-usa-g2dcb5592f_1280-1024x682.jpg)
*照片来自 Pixaba 的 Mirko Fabian*

在之前的文章中，我介绍了检索增强生成（Retrieval Augmented Generation，RAG）的概念，该方法用于为大型语言模型（Large Language Models，LLMs）提供上下文信息，以提高其响应的准确性。

本教程将带您进行一个实际示例，展示如何使用GPT 3.5中的RAG功能来根据自定义数据集回答问题。由于GPT 3.5的训练截止日期为2021年，它无法回答基于最近事件的问题。因此，我们将使用与奥斯卡金像奖相关的数据集来实现RAG，并让GPT 3.5回答关于第95届奥斯卡金像奖的问题，该奖项于2023年3月举行。

在开始之前，请确保您拥有OpenAI的活跃账号，并已将您的API密钥填入OPENAI_API_KEY环境变量中。

第一步 - 准备数据集
从Kaggle下载奥斯卡金像奖数据集，并将CSV文件移动到名为"data"的子目录中。该数据集包含了1927年至2023年的所有奥斯卡金像奖的类别、提名和获奖情况。我将CSV文件重命名为"oscars.csv"。

首先，导入Pandas库并加载数据集：
```python
import pandas as pd
df = pd.read_csv('./data/oscars.csv')
df.head()
```

数据集结构良好，包含列标题和表示每个类别详情的行，包括演员/技术人员的姓名、电影名称以及提名是否获奖。

由于我们主要关注与2023年相关的奖项，让我们将其过滤出来并创建一个新的Pandas数据帧。同时，我们还将把类别转换为小写，并删除电影值为空的行。这样有助于我们设计发送给GPT 3.5的上下文提示。
```python
df = df.loc[df['year_ceremony'] == 2023]
df = df.dropna(subset=['film'])
df['category'] = df['category'].str.lower()
df.head()
```

通过过滤和清洗后的数据集，我们将为数据帧添加一个新列，其中包含表示每个提名的完整句子。当将这些完整句子发送给GPT 3.5时，它能够在上下文中找到相关信息。
```python
df['text'] = df['name'] + ' got nominated under the category, ' + df['category'] + ', for the film ' + df['film'] + ' to win the award'
df.loc[df['winner'] == False, 'text'] = df['name'] + ' got nominated under the category, ' + df['category'] + ', for the film ' + df['film'] + ' but did not win'
df.head()['text']
```

请注意，我们将值连接起来以生成完整的句子。例如，数据帧的前两行中“text”列的值如下：

1. Austin Butler got nominated under the category, actor in a leading role, for the film Elvis but did not win
2. Colin Farrell got nominated under the category, actor in a leading role, for the film The Banshees of Inisherin but did not win

第二步 - 生成数据集的词嵌入
现在，我们有了从数据集构建的文本，让我们将其转换为词嵌入。这是一个关键的步骤，因为嵌入模型生成的令牌将帮助我们执行语义搜索，从数据集中检索具有相似含义的句子。
```python
import ast
import openai

def text_embedding(text):
    response = openai.Embedding.create(model="text-embedding-ada-002", input=text)
    return response["data"][0]["embedding"]

df = df.assign(embedding=(df["text"].apply(lambda x: text_embedding(x))))
df.head()
```

在上面的步骤中，我们将嵌入模型设置为"text-embedding-ada-002"，然后使用lambda函数为数据帧添加一个名为"embedding"的新列。这与同一行中相应的文本直接映射。

第三步 - 执行搜索以检索相似文本
有了每行生成的嵌入，我们现在可以使用一个简单的技术称为余弦相似度来比较两个向量的相似性。

让我们导入本步骤所需的模块。
```python
import tiktoken
from scipy import spatial
```

我们将创建一个帮助函数来执行余弦相似度搜索。它将查询转换为嵌入，并将其与数据帧中的每个嵌入进行比较。函数将返回文本以及用于排名相似性的分数。top_n参数定义要返回的句子数量。
```python
def strings_ranked_by_relatedness(
    query: str,
    df: pd.DataFrame,
    relatedness_fn=lambda x, y: 1 - spatial.distance.cosine(x, y),
    top_n: int = 100
) -> tuple[list[str], list[float]]:
    
    query_embedding_response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=query,
    )
    query_embedding = query_embedding_response["data"][0]["embedding"]

    strings_and_relatednesses = [
        (row["text"], relatedness_fn(query_embedding, row["embedding"]))
        for i, row in df.iterrows()
    ]

    strings_and_relatednesses.sort(key=lambda x: x[1], reverse=True)
    strings, relatednesses = zip(*strings_and_relatednesses)
    return strings[:top_n], relatednesses[:top_n]
```

让我们通过发送关键字"Lady Gaga"来测试这个函数。目标是从具有关键字引用的数据帧中获取前三个值。
```python
strings, relatednesses = strings_ranked_by_relatedness("Lady Gaga", df, top_n=3)
for string, relatedness in zip(strings, relatednesses):
    print(f"{relatedness=:.3f}")
    display(string)
```

显然，第一个值的得分为0.821，最接近搜索。现在我们可以将它注入到我们的提示中来增强上下文。

第四步 - 基于RAG构建提示
我们想确保标记数不超过模型支持的上下文长度。对于GPT 3.5，上下文长度为4K。以下函数处理这一点。
```python
def num_tokens(text: str) -> int:
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    return len(encoding.encode(text))
```

让我们创建辅助函数，通过在数据帧中执行相似性搜索的方式来轻松创建提示，并同时考虑标记大小。
```python
def query_message(
    query: str,
    df: pd.DataFrame,
    model: str,
    token_budget: int
) -> str:
    strings, relatednesses = strings_ranked_by_relatedness(query, df)
    introduction = 'Use the below content related to the 95th Oscar awards to answer the subsequent question. If the answer cannot

 be found in the content, write "I could not find an answer."'
    question = f"\n\nQuestion: {query}"
    message = introduction
    for string in strings:
        next_row = f'\n\nOscar database section:\n"""\n{string}\n"""'
        if (
            num_tokens(message + next_row + question)
            > token_budget
        ):
            break
        else:
            message += next_row
    return message + question
```

基于前一个函数生成的上下文，我们将创建一个调用OpenAI API的函数。
```python
def ask(
    query: str,
    df: pd.DataFrame = df,
    model: str = "gpt-3.5-turbo",
    print_message: bool = False,
) -> str:
    message = query_message(query, df, model=model, token_budget=token_budget)
    if print_message:
        print(message)
    messages = [
        {"role": "system", "content": "You answer questions about 95th Oscar awards."},
        {"role": "user", "content": message},
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    response_message = response["choices"][0]["message"]["content"]
    return response_message
```

现在是时候向与第95届奥斯卡金像奖相关的GPT 3.5提问了。
```python
print(ask('What was the nomination from Lady Gaga for the 95th Oscars?'))
```
让我们再试一次。

即使模型没有关于最近事件的知识，该机器人似乎工作得很好。

您可以在下面找到完整的代码：

```python
import openai
import tiktoken
from scipy import spatial 
import pandas as pd

df=pd.read_csv('./data/oscars.csv')
print(df.head())

df=df.loc[df['year_ceremony'] == 2023]
df=df.dropna(subset=['film'])
df['category'] = df['category'].str.lower()
df.head()

df['text'] = df['name'] + ' got nominated under the category, ' + df['category'] + ', for the film ' + df['film'] + ' to win the award'
df.loc[df['winner'] == False, 'text'] = df['name'] + ' got nominated under the category, ' + df['category'] + ', for the film ' + df['film'] + ' but did not win'
print(df.head()['text'])

df=df.assign(embedding=(df["text"].apply(lambda x: text_embedding(x))))
print(df.head())

def strings_ranked_by_relatedness(
    query: str,
    df: pd.DataFrame,
    relatedness_fn=lambda x, y: 1 - spatial.distance.cosine(x, y),
    top_n: int = 100
) -> tuple[list[str], list[float]]:
    
    EMBEDDING_MODEL = "text-embedding-ada-002"
    query_embedding_response = openai.Embedding.create(
        model=EMBEDDING_MODEL,
        input=query,
    )
    query_embedding = query_embedding_response["data"][0]["embedding"]
    strings_and_relatednesses = [
        (row["text"], relatedness_fn(query_embedding, row["embedding"]))
        for i, row in df.iterrows()
    ]
    strings_and_relatednesses.sort(key=lambda x: x[1], reverse=True)
    strings, relatednesses = zip(*strings_and_relatednesses)
    return strings[:top_n], relatednesses[:top_n]

strings, relatednesses = strings_ranked_by_relatedness("Lady Gaga", df, top_n=3)
for string, relatedness in zip(strings, relatednesses):
    print(f"{relatedness=:.3f}")
    display(string)
    
def num_tokens(text: str) -> int:
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    return len(encoding.encode(text))    

def query_message(
    query: str,
    df: pd.DataFrame,
    model: str,
    token_budget: int
) -> str:
    strings, relatednesses = strings_ranked_by_relatedness(query, df)
    introduction = 'Use the below content related to 95th Oscar awards to answer the subsequent question. If the answer cannot be found in the articles, write "I could not find an answer."'
    question = f"\n\nQuestion: {query}"
    message = introduction
    for string in strings:
        next_row = f'\n\nOscar database section:\n"""\n{string}\n"""'
        if (
            num_tokens(message + next_row + question)
            > token_budget
        ):
            break
        else:
            message += next_row
    return message + question
  
def ask(
    query: str,
    df: pd.DataFrame = df,
    model: str = "gpt-3.5-turbo",
    token_budget: int = 4096 - 500,
    print_message: bool = False,
) -> str:
    message = query_message(query, df, model=model, token_budget=token_budget)
    if print_message:
        print(message)
    messages = [
        {"role": "system", "content": "You answer questions about 95th Oscar awards."},
        {"role": "user", "content": message},
    ]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    response_message = response["choices"][0]["message"]["content"]
    return response_message  

print(ask('What was the nomination from Lady Gaga for the 95th Oscars?'))  
print(ask('What were the nominations for the music awards?'))
```