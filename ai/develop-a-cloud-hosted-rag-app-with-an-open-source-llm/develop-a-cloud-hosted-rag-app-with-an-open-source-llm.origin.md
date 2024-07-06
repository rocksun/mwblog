# Develop a Cloud-Hosted RAG App With an Open Source LLM
![Featued image for: Develop a Cloud-Hosted RAG App With an Open Source LLM](https://cdn.thenewstack.io/media/2024/07/64386c29-albert-einstein-1024x576.jpg)
[Retrieval-augmented generation (RAG)](https://myscale.com/blog/how-does-retrieval-augmented-generation-system-work/) is often used to develop customized AI applications, including [chatbots](https://myscale.com/blog/build-chatbot-google-gemini-myscale-db/), [recommendation systems](https://myscale.com/blog/build-a-recommendation-system-with-openai-and-myscale/) and other personalized tools. This system uses the strength of vector databases and [large language models (LLMs)](https://thenewstack.io/what-is-a-large-language-model/) to provide high-quality results.
Selecting the right LLM for any RAG model is very important and requires considering factors like cost, privacy concerns and scalability. Commercial LLMs like [OpenAI’s GPT-4](https://openai.com/index/gpt-4/) and [Google’s](https://cloud.google.com/?utm_content=inline+mention) [Gemini](https://gemini.google.com/) are effective but can be expensive and raise data privacy concerns. Some users prefer [open source LLMs](https://myscale.com/blog/open-source-llm-comparison-guide/) for their flexibility and cost savings, but they require substantial resources for [fine-tuning](https://myscale.com/blog/how-to-fine-tune-llm-from-huggingface/) and deployment, including GPUs and specialized infrastructure. Additionally, managing model updates and scalability can be challenging with local setups.

A better solution is to select an [open source](https://thenewstack.io/open-source/) LLM and deploy it on the [cloud](https://thenewstack.io/cloud-native/). This approach provides the necessary computational power and scalability without the high costs and complexities of local hosting. It not only saves on initial infrastructural costs but also minimizes maintenance concerns.

Let’s explore a similar approach to develop an application using cloud-hosted open source LLMs and a scalable vector database.

## Tools and Technologies
Several tools are required to develop this RAG-based AI application. These include:

[BentoML](https://www.bentoml.com/): BentoML is an open source platform that simplifies deployment of machine learning models into production-ready APIs, ensuring scalability and ease of management.[LangChain](https://www.langchain.com/): LangChain is a framework for building applications using LLMs. It offers modular components for easy integration and customization.[MyScaleDB](https://myscale.com/): MyScaleDB is a high-performance, scalable database optimized for efficient data retrieval and storage, supporting advanced querying capabilities.
In this tutorial, we will extract data from Wikipedia using LangChain’s `WikipediaLoader`
module and build an LLM on that data.

## Preparation
### Set Up the Environment
Start setting your environment to use BentoML, MyScaleDB and [LangChain](https://thenewstack.io/lets-get-agentic-langchain-and-llamaindex-talk-ai-agents/) in your system by opening your terminal and entering:
This should install all three packages in your system. After this, you’re ready to write code and develop the RAG application.

### Load the Data
Begin by importing the [WikipediaLoader](https://python.langchain.com/v0.2/docs/integrations/document_loaders/wikipedia/) from the `langchain_community.document_loaders. wikipedia `
module. You’ll use this loader to fetch documents related to [“Albert Einstein” from Wikipedia](https://en.wikipedia.org/wiki/Albert_Einstein).

This uses the `load`
method to retrieve the “Albert Einstein” documents, and the `print`
method to print the contents of the first document to verify the loaded data.

### Split the Text Into Chunks
Import the
from [CharacterTextSplitter](https://python.langchain.com/v0.2/docs/integrations/document_loaders/wikipedia/)`langchain_text_splitters`
, join the contents of all pages into a single string, and then split the text into manageable chunks.
The `CharacterTextSplitter`
is configured to split this text into chunks of `400`
characters with an overlap of `100`
characters to ensure no information is lost between chunks. The `page_content`
or text is stored in the `splits`
array, which contains only the text content. You will use the `splits`
array to get the [embeddings](https://myscale.com/blog/understanding-embeddings-in-machine-learning/).

## Deploy the Models on BentoML
Your data is ready, and the next step is to deploy the models on BentoML and use them in your [RAG](https://myscale.com/blog/build-rag-app-with-myscale-and-llamaindex/#what-is-retrieval-augmented-generation) application. Deploy the LLM first. You’ll need a free BentoML account, and you can [sign up for one on BentoCloud](https://cloud.bentoml.com/signup) if needed. Next, navigate to the **Deployments** section and click on the **Create Deployment** button in the top-right corner. A new page will open that looks like this:

![BentoML deployments page](https://cdn.thenewstack.io/media/2024/07/fd77ff44-bentoml-deployments-page.png)
BentoML deployments page

Select the [bentoml/bentovllm-llama3-8b-instruct-service](https://github.com/bentoml/BentoVLLM/tree/main/llama3-8b-instruct) model from the drop-down menu and click “Submit” in the bottom-right corner. This should start deploying the model. A new page like this will open:

![LLM configuration page](https://cdn.thenewstack.io/media/2024/07/8307bf03-llm-config-page.png)
LLM configuration page

The deployment can take some time. Once it is deployed, copy the endpoint.

Note: BentoML’s free tier only allows the deployment of a single model. If you have a paid plan and can deploy more than one model, follow the steps below. If not, don’t worry — we will use an open source model locally for embeddings.

Deploying the embedding model is very similar to the steps you took to deploy the LLM:

- Go to the
**Deployments**page. - Click the
**Create Deployment**button. - Select the
`sentence-transformers`
model from the list and click**Submit**. - Once the deployment is complete, copy the endpoint.
Next, go to the [API Tokens page](https://docs.bentoml.com/en/latest/bentocloud/how-tos/manage-access-token.html) and generate a new API key. Now you are ready to use the deployed models in your RAG application.

### Define the Embeddings Method
You will define a function called `get_embeddings`
to generate embeddings for the provided text. This function takes three arguments. If the BentoML endpoint and API token are provided, the function uses BentoML’s embedding service; otherwise, it uses the local `transformers`
and `torch`
libraries to load the `sentence-transformers/all-MiniLM-L6-v2 `
model and generate embeddings.

This setup allows flexibility for free-tier BentoML users, who can deploy only one model at a time. If you have a paid version of BentoML and can deploy two models, you can pass the BentoML endpoint and Bento API token to use the deployed embedding model.

### Get the Embeddings
Iterate over the text chunks (`splits`
) in batches of `25`
to generate embeddings using the `get_embeddings`
function defined above.

This prevents overloading the embedding model with too much data at once, which can be particularly useful for managing memory and computational resources.

## Create a DataFrame
Now, create a [pandas](https://pandas.pydata.org/) DataFrame to store the text chunks and their corresponding embeddings.
This structured format makes it easier to manipulate and store the data in MyScaleDB.

## Connect to MyScaleDB
The knowledge base is complete, and now it’s time to save the data to the vector database. This demo uses MyScaleDB for vector storage. Start a MyScaleDB cluster in a cloud environment by following the [quickstart guide](https://myscale.com/docs/en/quickstart/#how-to-launch-your-first-cluster). Then you can establish a connection to the MyScaleDB database using the `clickhouse_connect`
library.
The client object created here will be used to execute SQL commands and interact with the database.

### Create a Table and Insert Data
Create a table in MyScaleDB to store the text chunks and embeddings. The table schema includes an `id`
, the `page_content`
and the `embeddings`
.
This ensures the embeddings have a fixed length of `384`
. The data from the DataFrame is then inserted into the table in batches to manage large data efficiently.

### Create a Vector Index
The next step is to add a vector index to the `embeddings`
column in the `RAG`
table. The vector index allows for efficient similarity searches, which are essential for retrieval-augmented generation tasks.

### Retrieve Relevant Vectors
Define a function to retrieve relevant documents based on a user query. The query embeddings are generated using the `get_embeddings`
function, and an advanced SQL vector query is executed to find the closest matches in the database.
The results are ordered by distance, and the top `k`
matches are returned. This setup finds the most relevant documents for a given query.

Note: The `distance`
method takes an embedding column and the embedding vector of the user query to find similar documents by applying cosine similarity.

## Connect to BentoML LLM
Establish a connection to your hosted LLM on BentoML. The `llm_client`
object will be used to interact with the LLM for generating responses based on the retrieved documents.
Replace the `BENTO_LLM_END_POINT`
and `token`
with the values you copied earlier during the LLM deployment.

## Perform RAG
Define a function to perform RAG. The function takes a user question and the retrieved context as input. It constructs a prompt for the LLM, instructing it to answer the question based on the provided context. The response from the LLM is then returned as the answer.

## Make a Query
Finally, you can test it out by making a query to the RAG application. Ask the question “Who is Albert Einstein?” and use the `dorag `
function to get the answer based on the relevant documents retrieved earlier.
The output provides a detailed response to the question, demonstrating the effectiveness of the RAG setup.

![LLM response provides biographical information about Albert Einstein](https://cdn.thenewstack.io/media/2024/07/30eca4d5-llm-response-einstein-bio1.png)
LLM response

If you ask the RAG model about Albert Einstein’s death, the response should look like this:

![LLM response provides information about Albert Einstein's death](https://cdn.thenewstack.io/media/2024/07/681122ab-llm-response-einstein-death2.png)
LLM response

## Conclusion
BentoML stands out as an excellent platform for deploying machine learning models, including LLMs, without the hassle of managing resources. With BentoML, you can quickly deploy and scale your AI applications on the cloud, ensuring they are production-ready and highly accessible. Its simplicity and flexibility make it an ideal choice for developers, enabling them to focus more on innovation and less on deployment complexities.

On the other hand, MyScaleDB is explicitly developed for RAG applications, offering a high-performance SQL vector database. Its familiar SQL syntax makes it easy for developers to integrate and use MyScaleDB in their applications, as the learning curve is minimal. MyScaleDB’s [Multi-Scale Tree Graph (MSTG)](https://myscale.com/blog/optimizing-filtered-vector-search/#multi-scale-tree-graph-algorithm) algorithm significantly outperforms other vector databases in terms of speed and accuracy. Additionally, MyScaleDB offers each new user free storage for up to 5 million vectors, making it a desirable option for developers looking to implement efficient and scalable AI solutions.

What do you think about this project? Share your thoughts on [Twitter](https://twitter.com/MyScaleDB) and [Discord](https://discord.gg/D2qpkqc4Jq).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)