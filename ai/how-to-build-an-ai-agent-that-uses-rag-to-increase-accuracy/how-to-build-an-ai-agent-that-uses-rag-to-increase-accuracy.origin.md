# How To Build an AI Agent That Uses RAG To Increase Accuracy
![Featued image for: How To Build an AI Agent That Uses RAG To Increase Accuracy](https://cdn.thenewstack.io/media/2024/07/e25239a7-rick-rothenberg-x3mylqmg9u8-unsplash-1024x683.jpg)
The combination of [retrieval augmented generation](https://thenewstack.io/retrieval-augmented-generation-for-llms/) (RAG) and [function calls](https://thenewstack.io/a-comprehensive-guide-to-function-calling-in-llms/) can greatly improve the capabilities of LLM-based applications. [RAG agents based on function calling](https://thenewstack.io/federated-language-models-slms-at-the-edge-plus-cloud-llms/) combine the benefits of both approaches, relying on external knowledge bases for accurate data retrieval and executing specific functions for efficient task completion.

Function calling within the RAG framework enables more structured retrieval processes. For example, a function can be predefined to extract specific information based on user queries, which the RAG system will retrieve from a comprehensive knowledge base. This method ensures that the responses are both relevant and precisely tailored to the application’s requirements.

In this tutorial, we will build an agent that’s designed to help the product manager of an ecommerce company analyze sales and the product portfolio. It uses a retriever to extract context from unstructured data stored in PDFs, while invoking an API to get sales information.

The agent has access to a set of tools and also to a vector database. The initial prompt and the registered tools are sent to the LLM. If the LLM response includes a subset of tools, the agent executes them and collects the context. If the LLM doesn’t recommend executing any of the tools, the agent then performs a semantic search in the vector database and retrieves the context. Irrespective of where the context is gathered from, it is added to the original prompt and sent to the LLM.

To simplify the configuration, I created a Docker Compose file to run the MySQL database and Flask API layers. The PDFs are indexed separately and ingested into ChromaDB. It’s assumed that you have access to the OpenAI environment.

Start by cloning the [Git repository](https://github.com/janakiramm/rag-agent) and follow the steps below to configure the agent on your machine.

1 |
git clone https://github.com/janakiramm/rag-agent.git |
## Step 1: Launch the DB and the API server
Switch to the `api`
directory and run the Docker Compose file to launch the database and the corresponding API server.

1 |
docker compose up -d --build |
The API server exposes four API endpoints:
`get_top_selling_products`
`get_top_categories`
`get_sales_trends`
`get_revenue_by_category`
You can invoke these endpoints from curl.

1 |
curl "http://localhost:5000/api/sales/top-products?start_date=2023-04-01&end_date=2023-06-30" |
1 |
curl "http://localhost:5000/api/sales/top-categories?start_date=2023-04-01&end_date=2023-06-30" |
1 |
curl "http://localhost:5000/api/sales/trends?start_date=2023-04-01&end_date=2023-06-30" |
1 |
curl "http://localhost:5000/api/sales/revenue-by-category?start_date=2023-04-01&end_date=2023-06-30" |
## Step 2: Index PDFs and Store Vectors in Chroma DB
Under the `data`
directory, you will find a PDF that contains a description of a few products from the electronics category. Our task is to index it and store the embedding vectors in Chroma.

For this, launch the `Index-Datasheet`
Jupyter Notebook and run all the cells.

This loads the PDF, performs chunking, generates the embeddings and finally stores the vectors in ChromaDB.

The last cell of this Notebook performs a simple semantic search to validate the indexing process.

Now, we have two entities that can help us get the context: 1) API, and 2) vector database.

## Step 3: Run the RAG Agent
The agent code is available in the `RAG-Agent`
Jupyter Notebook. Launch it and run all the cells to see it in action.

This Notebook contains the logic to decide between executing the tools and performing a semantic search.

I wrapped the REST API calls within the `tools.py`
which is available in the root directory of the repo, which we import into the agent.

123456 |
from tools import ( get_top_selling_products, get_top_categories, get_sales_trends, get_revenue_by_category) |
Since we decided to persist the Chroma collection from the indexing process performed in the previous step, we will simply load it.
123 |
chroma_client = chromadb.PersistentClient(path="./data")embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")collection = chroma_client.get_or_create_collection(name="products", embedding_function=embedding_function) |
Based on the available tools, we pass them along with the prompt to the LLM to map. The LLM then recommends the right functions to invoke. Below is a partial code snippet from the `map_tools`
function.
123456789101112131415161718192021222324 |
….messages = [{"role": "user", "content": prompt}] response = llm.chat.completions.create( model=model, messages=messages, tools=tools, tool_choice="auto" ) # Ensure response has valid tool_calls response_message = response.choices[0].message tool_calls = getattr(response_message, 'tool_calls', None) functions = [] if tool_calls: for tool in tool_calls: function_name = tool.function.name arguments = json.loads(tool.function.arguments) functions.append({ "function_name": function_name, "arguments": arguments }) return functions |
Similarly, we have a retriever responsible for extracting the context from the vector database.
123456789 |
def retriever(query): vector = embedding_function([query]) results = collection.query( query_embeddings=vector, n_results=5, include=["documents"] ) res = " \n".join(str(item) for item in results['documents'][0]) return res |
We have a simple helper function to send the gathered context and the original prompt to the LLM.
12345678910111213141516 |
def generate_response(prompt,context): input_text = ( "Based on the below context, respond with an accurate answer. If you don't find the answer within the context, say I do not know. Don't repeat the question\n\n" f"{context}\n\n" f"{prompt}" ) response = llm.chat.completions.create( model= model, messages=[ {"role": "user", "content": input_text}, ], max_tokens=150, temperature=0 ) return response.choices[0].message.content.strip() |
The job of the agent is to first check whether the LLM recommends any tools and then execute them to generate the context. If not, it relies on the vector database to generate the context.
1234567891011 |
def agent(prompt): tools = map_tools(prompt) if tools: tool_output = execute_tools(tools) context = json.dumps(tool_output) else: context = retriever(prompt) response = generate_response(prompt, context) return response |
In the below screenshot, the first response is coming from the tools/API and the second from the vector database.
## Extending RAG Agent to Use Federated Language Models
In this scenario, we relied on OpenAI’s GPT-4o for mapping the function calls and generating the final response based on the context. By relying on the idea of federated models, we can entirely avoid sending the context to the cloud-based LLM and use a local LLM deployed at the edge to respond to queries.

In my next post (the last and final part of this series), we will see how to combine the idea of the RAG agent with federated language models. Stay tuned.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)