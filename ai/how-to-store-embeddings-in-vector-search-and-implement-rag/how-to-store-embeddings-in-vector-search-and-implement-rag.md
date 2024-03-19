
<!--
title: 如何将嵌入存储在向量搜索中并实现 RAG
cover: https://cdn.thenewstack.io/media/2024/03/9c7d3ec6-chuttersnap-eh_ftjyhaty-unsplash.jpg
-->

在本动手教程中，我们将向您展示如何生成嵌入，将它们存储在 Vertex AI 向量搜索索引中，并实现 RAG。

> 译自 [How to Store Embeddings in Vector Search and Implement RAG](https://thenewstack.io/how-to-store-embeddings-in-vector-search-and-implement-rag/)，作者 Janakiram MSV。


## How to Store Embeddings in Vector Search and Implement RAG

![Featured image for How to Store Embeddings in Vector Search and Implement RAG](https://cdn.thenewstack.io/media/2024/03/9c7d3ec6-chuttersnap-eh_ftjyhaty-unsplash-1024x684.jpg)

[Vector Search](https://cloud.google.com/vertex-ai/docs/vector-search/overview) is a component of Google Cloud's Vertex AI platform that supports searching billions of semantically similar or related items, leveraging the power of vector similarity matching services. Such capabilities have a wide range of applications, including recommendation engines, search engines, chatbots, and text classification, making it a versatile tool for businesses and developers alike. It is one of the core building blocks of the [Retrieval Augmented Generation](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/) (RAG) framework.

In this hands-on tutorial, we will first explore how to generate embeddings for a PDF and store them in a Vertex AI Vector Search index. Next, we will leverage Gemini's semantic search capabilities to implement RAG.

## Part 1: Generating Embeddings and Storing Them in a Vertex AI Vector Search Index

The process of performing semantic matching using Vector Search involves the following steps:

**Generate Embeddings:** First, create an [embedding](https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/) representation of your items outside of Vector Search, or use generative AI on Vertex AI to create embeddings.

**Upload Embeddings to Cloud Storage:** Upload your embeddings to Cloud Storage so that the Vector Search service can access it.

**Ingest into Vector Search:** Connect your embeddings to Vector Search by creating an index from the embeddings, which can then be deployed to an index endpoint for querying.

For this use case, we will use the employee handbook of a fictional company called Lakeside Bicycles. The end goal is to build a chatbot for employees to retrieve policies mentioned in this document.

First, enable the Google Cloud APIs for the services we will be using.

```
1
gcloud services enable compute.googleapis.com aiplatform.googleapis.com storage.googleapis.com
```

Log into GCP and cache your credentials locally.

```
1
gcloud auth application-default login
```

Create a `requirements.txt` with the following contents and install the dependencies in a Python virtual environment.

```
1
2
3
4
pypdf2
google-cloud-storage
google-cloud-aiplatform
jupyter
```

```
1
2
python -m venv venv
source venv/bin/activate
```

```
1
2
pip install -r requirements.txt
jupyter notebook
```

We can now import the modules. Start a new Jupyter Notebook and add the following code snippet:

```
1
2
3
4
5
6
7
8
9
10
11
from google.cloud import storage
from vertexai.language_models import TextEmbeddingModel
from google.cloud import aiplatform
import PyPDF2
import re
import os
import random
import json
import uuid
```

```
1
2
3
4
5
6
7
8
project=”YOUR_GCP_PROJECT”
location="us-central1"
pdf_path="lakeside_handbook.pdf"
bucket_name = "lakeside-content"
embed_file_path = "lakeside_embeddings.json"
sentence_file_path = "lakeside_sentences.json"
index_name="lakeside_index"
```

We will now create a set of helper functions to assist us with our workflow.

The first function takes a PDF and splits it into a list of sentences. This will be used to generate embeddings for each sentence.

```
1
2
3
4
5
6
7
8
9
def extract_sentences_from_pdf(pdf_path):
with open(pdf_path, 'rb') as file:
reader = PyPDF2.PdfReader(file)
text = ""
for page in reader.pages:
if page.extract_text() is not None:
text += page.extract_text() + " "
sentences = [sentence.strip() for sentence in text.split('. ') if sentence.strip()]
return sentences
```

Next, we need a function that takes one or more sentences and converts them into embeddings by passing them through the `textembedding-gecko@001` model.

```
1
2
3
4
5
6
def generate_text_embeddings(sentences) -> list:
aiplatform.init(project=project,location=location)
model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001")
embeddings = model.get_embeddings(sentences)
vectors = [embedding.values for embedding in embeddings]
return vectors
```

We will wrap the above two functions in another function that helps us split the PDF into two JSON files — one with unique IDs for sentences and another with the corresponding embeddings for each sentence with the same unique ID.

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
def generate_and_save_embeddings(pdf_path, sentence_file_path, embed_file_path):
def clean_text(text):
cleaned_text = re.sub(r'\u2022', '', text) # Remove bullet points
cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip() # Remove extra whitespaces and strip
return cleaned_text
sentences = extract_sentences_from_pdf(pdf_path)
if sentences:
embeddings = generate_text_embeddings(sentences)
with open(embed_file_path, 'w') as embed_file, open(sentence_file_path, 'w') as sentence_file:
For sentences, embedded in `zip(sentences, embeddings)`:
```python
cleaned_sentence = clean_text(sentence)
id = str(uuid.uuid4())
embed_item = {"id": id, "embedding": embedding}
sentence_item = {"id": id, "sentence": cleaned_sentence}
json.dump(sentence_item, sentence_file)
sentence_file.write('\n')
json.dump(embed_item, embed_file)
embed_file.write('\n')
```

To simplify uploading the embeddings to Google Cloud Storage, we will create another helper function called `upload_file` that takes a bucket name and a file path.

```python
def upload_file(bucket_name,file_path):
    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name,location=location)
    blob = bucket.blob(file_path)
    blob.upload_from_filename(file_path)
```

Finally, we will create a vector search index pointing to the GCS bucket and deploy an endpoint.

```python
def create_vector_index(bucket_name, index_name):
    lakeside_index = aiplatform.MatchingEngineIndex.create_tree_ah_index(
        display_name = index_name,
        contents_delta_uri = "gs://"+bucket_name,
        dimensions = 768,
        approximate_neighbors_count = 10,
    )
    lakeside_index_endpoint = aiplatform.MatchingEngineIndexEndpoint.create(
        display_name = index_name,
        public_endpoint_enabled = True
    )
    lakeside_index_endpoint.deploy_index(
        index = lakeside_index, deployed_index_id = index_name
    )
```

We can now call the functions to create, configure, and deploy the vector search index.

### Step 1: Generate Embeddings for the PDF

```python
generate_and_save_embeddings(pdf_path,sentence_file_path,embed_file_path)
```

Calling the above method will generate two files that look like the ones below:

```json
{"id": "00000000-0000-0000-0000-000000000000", "sentence": "The Lakeside School is a private, coeducational, college-preparatory day school for grades 7-12, located in the Laurelhurst neighborhood of Seattle, Washington."}
{"id": "00000000-0000-0000-0000-000000000001", "sentence": "The school was founded in 1914 by a group of parents who wanted to create a school that would provide a rigorous academic program in a supportive and nurturing environment."}
```

The UUID is common between the two files. This will help us identify the corresponding sentence when vector search returns matching IDs of embeddings based on similarity.

Our goal is to upload the JSON files with embeddings to a Cloud Storage bucket and initiate the creation of a vector search index endpoint.

We will call the following method to complete the workflow:

### Step 2: Upload the Embedding Files to Cloud Storage

```python
upload_file(bucket_name,file_path)
```

This will result in a bucket being created and the JSON files being uploaded to it. You can verify this from the Cloud Console.

### Step 3: Create and Deploy the Vector Search Index Endpoint

```python
create_vector_index(bucket_name, index_name)
```

The final step takes at least 20 minutes to complete. Please be patient. Once done, you can verify from the Cloud Console.

You can access the entire code below:

With the index in place, we can now implement RAG on Vertex AI using Google’s most powerful LLM, Gemini Pro.

## Part 2: Implementing RAG with Gemini and Vector Search on Google Cloud Vertex AI

We can now import the modules. Start a new Jupyter Notebook and add the following code snippet:

```python
from vertexai.language_models import TextEmbeddingModel
from google.cloud import aiplatform
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
import json
import os
```

```python
project=”YOUR_GCP_PROJECT”
location="us-central1"
location="us-central1"
sentence_file_path = "lakeside_sentences.json"
index_ep="2223340054711894016"
```

You can get the vector search index endpoint from the console.

Proceed to initialize the model and the vector index

```python
aiplatform.init(project=project,location=location)
vertexai.init()
model = GenerativeModel("gemini-pro")
lakeside_index_ep = aiplatform.MatchingEngineIndexEndpoint(index_endpoint_name=index_name)
```

We will now create helper functions to generate embeddings for the query, load a local file with IDs and sentences, and map the matching IDs returned by vector search back to sentences.

```python
def generate_text_embeddings(sentences) -> list:
    model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001")
    embeddings = model.get_embeddings(sentences)
    vectors = [embedding.values for embedding in embeddings]
    return vectors
```

Load the file and populate a Python list with each line.

```python
def load_file(sentence_file_path):
    data = []
    with open(sentence_file_path, 'r') as file:
        for line in file:
            entry = json.loads(line)
            data.append(entry)
    return data
```

When vector search returns matching IDs of embeddings based on similarity, we will map them to sentences using the local sentence file and then concatenate all the matching sentences into one big sentence. This serves as context for the model.

```python
def generate_context(ids,data):
    concatenated_names = ''
    for id in ids:
        for entry in data:
            if entry['id'] == id:
                concatenated_names += entry['sentence'] + "\n"
    return concatenated_names.strip()
```

We can now implement RAG. The first step is to take a query and generate its embedding. Before that, let's make sure to load the sentences JSON file into a list that we can access later.

```python
data=load_file(sentence_file_path)
```

```python
#query=["How many days of unpaid leave in an year"]
```
## query=["在线课程允许的费用"]
## query=["申请病假的流程"]
query=["申请个人假期的流程"]
qry_emb=generate_text_embeddings(query)

我们现在将基于生成的嵌入和存储在 Vector Search 中的嵌入执行语义搜索。

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
response = lakeside_index_ep.find_neighbors(
deployed_index_id = index_name,
queries = [qry_emb[0]],
num_neighbors = 10
)

Vector Search 现在返回一组与嵌入相对应的 UUID。
下一步是检索 ID 并将它们转换为列表。

| 1 |
|---|---|
matching_ids = [neighbor.id for sublist in response for neighbor in sublist]

我们现在将调用
generate_context 帮助器方法来生成可以注入提示符的上下文。这是 RAG 管道中最关键的一步。

| 1 |
|---|---|
context = generate_context(matching_ids,data)

对于查询“
*申请个人假期的流程*”，我们通过连接本地文件中的句子获得了以下上下文。

现在，是时候使用上下文和原始查询生成扩充提示符了。

| 1 |
|---|---|
prompt=f"基于以反引号分隔的上下文回答查询。 ```{context}``` {query}"

当我们最终调用模型时，它会返回从上下文中得出的预期答案，这是事实正确的。

| 1 | 2 | 3 |
|---|---|---|
chat = model.start_chat(history=[])
response = chat.send_message(prompt)
print(response.text)

以下是本教程此部分的完整代码。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)