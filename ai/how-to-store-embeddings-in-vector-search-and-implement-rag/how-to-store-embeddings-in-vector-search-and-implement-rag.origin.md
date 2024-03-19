# How to Store Embeddings in Vector Search and Implement RAG
![Featued image for: How to Store Embeddings in Vector Search and Implement RAG](https://cdn.thenewstack.io/media/2024/03/9c7d3ec6-chuttersnap-eh_ftjyhaty-unsplash-1024x684.jpg)
[Vector Search](https://cloud.google.com/vertex-ai/docs/vector-search/overview) is a component of Google Cloud’s Vertex AI platform and it enables the searching of billions of semantically similar or related items, leveraging the power of vector similarity-matching services. Such capabilities have a wide array of applications, including recommendation engines, search engines, chatbots, and text classification, making it a versatile tool for businesses and developers alike. It’s one of the core building blocks of the [Retrieval Augmented Generation](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/) (RAG) framework.
In this hands-on tutorial, we will firstly explore how to generate embeddings for a PDF and store them in a Vertex AI Vector Search Index. Following that, we will leverage the semantic search capabilities of Gemini to implement RAG.
## Part 1: Generate Embeddings and Store Them in a Vertex AI Vector Search Index
The process of using Vector Search for semantic matching involves several steps:
**Generate an Embedding**: First, create [embedding](https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/)representations of items outside of Vector Search, or use Generative AI on Vertex AI to create embeddings. **Upload Embedding to Cloud Storage**: Upload your embedding to Cloud Storage to make it accessible to the Vector Search service. **Insert to Vector Search**: Connect your embeddings to Vector Search by creating an index from your embedding, which can then be deployed to an index endpoint for querying.
For this use case, we are going to use the employee handbook of a fictitious company called Lakeside Bicycles. The ultimate goal is to build a chatbot for employees to retrieve the policies mentioned in this document.
Start by enabling the Google Cloud APIs for the services we are going to use.
|
1
|
gcloud services enable compute.googleapis.com aiplatform.googleapis.com storage.googleapis.com
Login to GCP and cache the credentials locally.
|
1
|
gcloud auth application-default login
Create a requirements.txt with the below content and install the dependencies in a Python virtual environment.
|
1
2
3
4
|
pypdf2
google-cloud-storage
google-cloud-aiplatform
jupyter
|
1
2
|
python -m venv venv
source venv/bin/activate
|
1
2
|
pip install -r requirements.txt
jupyter notebook
We are now ready to import the modules. Start a new Jupyter Notebook and add the below code snippets:
|
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
|
from google.cloud import storage
from vertexai.language_models import TextEmbeddingModel
from google.cloud import aiplatform
import PyPDF2
import re
import os
import random
import json
import uuid
|
1
2
3
4
5
6
7
8
|
project=”YOUR_GCP_PROJECT”
location="us-central1"
pdf_path="lakeside_handbook.pdf"
bucket_name = "lakeside-content"
embed_file_path = "lakeside_embeddings.json"
sentence_file_path = "lakeside_sentences.json"
index_name="lakeside_index"
We will now create a set of helper functions that assist us in the workflow.
The first function accepts a PDF and splits it into a list of sentences. This will be used to generate embeddings per sentence.
|
1
2
3
4
5
6
7
8
9
|
def extract_sentences_from_pdf(pdf_path):
with open(pdf_path, 'rb') as file:
reader = PyPDF2.PdfReader(file)
text = ""
for page in reader.pages:
if page.extract_text() is not None:
text += page.extract_text() + " "
sentences = [sentence.strip() for sentence in text.split('. ') if sentence.strip()]
return sentences
Next, we need a function that accepts one or more sentences and converts them into embeddings by passing them through the
*textembedding-gecko@001* model.
|
1
2
3
4
5
6
|
def generate_text_embeddings(sentences) -> list:
aiplatform.init(project=project,location=location)
model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001")
embeddings = model.get_embeddings(sentences)
vectors = [embedding.values for embedding in embeddings]
return vectors
We will wrap the above two functions in another function that helps us split the PDF into two JSON files — one that has a unique ID for the sentence and one that has the same unique id but the corresponding embeddings for each sentence.
|
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
|
def generate_and_save_embeddings(pdf_path, sentence_file_path, embed_file_path):
def clean_text(text):
cleaned_text = re.sub(r'\u2022', '', text) # Remove bullet points
cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip() # Remove extra whitespaces and strip
return cleaned_text
sentences = extract_sentences_from_pdf(pdf_path)
if sentences:
embeddings = generate_text_embeddings(sentences)
with open(embed_file_path, 'w') as embed_file, open(sentence_file_path, 'w') as sentence_file:
for sentence, embedding in zip(sentences, embeddings):
cleaned_sentence = clean_text(sentence)
id = str(uuid.uuid4())
embed_item = {"id": id, "embedding": embedding}
sentence_item = {"id": id, "sentence": cleaned_sentence}
json.dump(sentence_item, sentence_file)
sentence_file.write('\n')
json.dump(embed_item, embed_file)
embed_file.write('\n')
To simplify uploading the embeddings to Google Cloud Storage, we will create another helper function called
upload_file that accepts the bucket name and the file name.
|
1
2
3
4
5
|
def upload_file(bucket_name,file_path):
storage_client = storage.Client()
bucket = storage_client.create_bucket(bucket_name,location=location)
blob = bucket.blob(file_path)
blob.upload_from_filename(file_path)
Finally, we will create a Vector Search Index pointed to the GCS bucket and deploy the endpoint.
|
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
|
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
We are now ready to invoke the functions to create, configure, and deploy Vector Search Index.
### Step 1: Generate Embeddings for the PDF
|
1
|
generate_and_save_embeddings(pdf_path,sentence_file_path,embed_file_path)
Calling the above method generates two files that look like the below:
The UUID is common between both the files. This will help us in identifying the corresponding sentences when Vector Search returns the matching IDs of the embeddings based on a similarity search.
Our goal is to upload the JSON file with embeddings to a Cloud Storage bucket and initiate the creation of Vector Search Index Endpoint.
We will call the below methods to complete the workflow:
### Step 2: Uploading the Embeddings file to Cloud Storage
|
1
|
upload_file(bucket_name,file_path)
This results in the creation of a bucket and uploads the JSON file to it. You can verify this from the Cloud Console.
### Step 3: Creating and Deploying Vector Search Index Endpoint
|
1
|
create_vector_index(bucket_name, index_name)
The last step takes at least 20 minutes to complete. Please be patient. When it’s done, you can verify the Cloud Console.
You can access the entire code below:
With the index in place, we are ready to implement RAG with Gemini Pro, Google’s most capable LLM available on Vertex AI.
## Part 2: Implementing RAG with Gemini and Vector Search on Google Cloud Vertex AI
We are now ready to import the modules. Start a new Jupyter Notebook and add the below code snippets:
|
1
2
3
4
5
6
7
8
|
from vertexai.language_models import TextEmbeddingModel
from google.cloud import aiplatform
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part
import json
import os
|
1
2
3
4
5
6
|
project=”YOUR_GCP_PROJECT”
location="us-central1"
location="us-central1"
sentence_file_path = "lakeside_sentences.json"
index_ep="2223340054711894016"
You can get the Vector Search Index Endpoint from the Console.
Go ahead and initialize the model and the vector index
|
1
2
3
4
|
aiplatform.init(project=project,location=location)
vertexai.init()
model = GenerativeModel("gemini-pro")
lakeside_index_ep = aiplatform.MatchingEngineIndexEndpoint(index_endpoint_name=index_name)
We will now create helper functions to generate embeddings for the query, load the local file with ids and sentences, and map the matching ids returned by Vector Search with the sentences.
|
1
2
3
4
5
|
def generate_text_embeddings(sentences) -> list:
model = TextEmbeddingModel.from_pretrained("textembedding-gecko@001")
embeddings = model.get_embeddings(sentences)
vectors = [embedding.values for embedding in embeddings]
return vectors
Load file and populate each line into a Python list.
|
1
2
3
4
5
6
7
|
def load_file(sentence_file_path):
data = []
with open(sentence_file_path, 'r') as file:
for line in file:
entry = json.loads(line)
data.append(entry)
return data
When Vector Search returns matching ids of the embeddings based on the similarity search, we will map those with the local sentence file and then concatenate all matching sentences into one large sentence. This acts as the context to the model.
|
1
2
3
4
5
6
7
|
def generate_context(ids,data):
concatenated_names = ''
for id in ids:
for entry in data:
if entry['id'] == id:
concatenated_names += entry['sentence'] + "\n"
return concatenated_names.strip()
We are now ready to implement RAG. The first step is to accept the query and then generate the embeddings for that. Before that, let’s make sure that the sentences JSON file is loaded into list that we can access later.
|
1
|
data=load_file(sentence_file_path)
|
1
2
3
4
5
|
#query=["How many days of unpaid leave in an year"]
#query=["Allowed cost of online course"]
#query=["process for applying sick leave"]
query=["process for applying personal leave"]
qry_emb=generate_text_embeddings(query)
We will now perform semantic search based on the generated embeddings and stored embeddings in Vector Search.
|
1
2
3
4
5
|
response = lakeside_index_ep.find_neighbors(
deployed_index_id = index_name,
queries = [qry_emb[0]],
num_neighbors = 10
)
Vector Search now returns a set of UUIDs that correspond to the embeddings.
The next step is retrieving the ids and turning them into a list.
|
1
|
matching_ids = [neighbor.id for sublist in response for neighbor in sublist]
We will now call the
generate_context helper method to generate the context that can be injected into the prompt. This is the most crucial step in the RAG pipeline.
|
1
|
context = generate_context(matching_ids,data)
For the query, “
*process for applying personal leave*”, we got the below context by concatenating the sentences from the local file.
Now, it’s time to generate the augmented prompt with both the context and original query.
|
1
|
prompt=f"Based on the context delimited in backticks, answer the query. ```{context}``` {query}"
When we finally invoke the model, it comes back with the expected answer derived from the context, which is factually correct.
|
1
2
3
|
chat = model.start_chat(history=[])
response = chat.send_message(prompt)
print(response.text)
Below is the complete code for this part of the tutorial.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)