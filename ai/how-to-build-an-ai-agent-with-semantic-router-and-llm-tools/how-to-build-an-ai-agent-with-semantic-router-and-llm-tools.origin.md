# How to Build an AI Agent With Semantic Router and LLM Tools
![Featued image for: How to Build an AI Agent With Semantic Router and LLM Tools](https://cdn.thenewstack.io/media/2024/10/25b311e9-allison-saeng-7sp_xmpmfho-unsplashb-1024x576.jpg)
In the previous post, I [introduced the semantic router](https://thenewstack.io/semantic-router-and-its-role-in-designing-agentic-workflows/): a pattern that enables [AI agents](https://thenewstack.io/ai-agents-key-concepts-and-how-they-overcome-llm-limitations/) to choose the right LLM for the right task, while also reducing their LLM dependency. In this follow-up tutorial, we will use the [Semantic Router](https://github.com/aurelio-labs/semantic-router) project to intelligently handle user queries by choosing the best way to retrieve information, such as whether to use a [vector database](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/) and/or a tool-based retriever for real-time data.

Similar to [previous tutorials](https://thenewstack.io/how-to-build-a-real-time-app-with-gpt-4o-function-calling/), in our example we will track the flight status of planes in real-time using data from [FlightAware’s AeroAPI](https://www.flightaware.com/commercial/aeroapi).

First, note that the router dynamically routes queries based on intent, ensuring the retrieval of the most relevant context, making this approach unique. The semantic router takes OpenAI’s LLM and structured retrieval methods and combines them to make an adaptive, highly responsive assistant that can quickly handle both conversational queries and data-specific requests.

Semantic Router suggests calling the tool for queries about flight schedules and status while it routes queries about baggage policy to a search function that provides the context.

Let’s break it down step by step.

## Step 1: Setting Up Your Environment
Before we dive into the code, ensure you have the required libraries installed. You can do this using pip:

1 |
pip install openai chromadb requests pytz semantic-router |
Let’s import the required modules.
123456789101112131415 |
import osfrom typing import Dict, Anyfrom datetime import datetime, timedeltaimport pytzimport requestsfrom openai import OpenAIimport chromadbfrom chromadb.utils import embedding_functionsfrom semantic_router import Route, RouteLayerfrom semantic_router.encoders import OpenAIEncoderfrom semantic_router.llms.openai import get_schemas_openaifrom semantic_router.llms import OpenAILLM |
Next, set up your environment variables for OpenAI and FlightAware AeroAPI keys:
12 |
export OPENAI_API_KEY="your_openai_api_key"export AEROAPI_KEY="your_flightaware_api_key" |
These keys will be essential for accessing the external services used in the tutorial.
## Step 2: Initializing OpenAI and ChromaDB Clients
We begin by initializing the clients for OpenAI and ChromaDB. OpenAI will generate embeddings for our queries, while ChromaDB will store and retrieve the embeddings for contextual data such as baggage policies.

123456789101112 |
# Initialize OpenAI clientopenai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])# Initialize ChromaDB client with a persistent storage pathchroma_client = chromadb.PersistentClient(path="./chroma_db")# Set up embedding function using OpenAI's modelembedding_function = embedding_functions.OpenAIEmbeddingFunction( api_key=os.environ["OPENAI_API_KEY"], model_name="text-embedding-3-small")COLLECTION_NAME = "baggage_policy" |
## Step 3: Fetching Flight Data From AeroAPI
FlightAware’s AeroAPI provides real-time flight data. The function `get_flight_context`
retrieves flight information for a specific flight ID, including departure, arrival times and status.

1234567891011121314151617181920212223242526 |
AEROAPI_BASE_URL = "https://aeroapi.flightaware.com/aeroapi"AEROAPI_KEY = os.getenv("AEROAPI_KEY")def get_flight_context(flight_id: str) -> str: def _get_flight_data() -> dict: session = requests.Session() session.headers.update({"x-apikey": AEROAPI_KEY}) start_date = datetime.now().strftime('%Y-%m-%d') end_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d') response = session.get(f"{AEROAPI_BASE_URL}/flights/{flight_id}?start={start_date}&end={end_date}") response.raise_for_status() return response.json()['flights'][0] def _utc_to_local(utc_date_str: str, local_timezone_str: str) -> str: utc_datetime = datetime.strptime(utc_date_str, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc) local_timezone = pytz.timezone(local_timezone_str) local_datetime = utc_datetime.astimezone(local_timezone) return local_datetime.strftime('%Y-%m-%d %H:%M:%S') flight_data = _get_flight_data() depart_time = _utc_to_local(flight_data['scheduled_out'], flight_data['origin']['timezone']) arrival_time = _utc_to_local(flight_data['scheduled_in'], flight_data['destination']['timezone']) return ( f"Flight {flight_id} from {flight_data['origin']['city']} to {flight_data['destination']['city']} " f"departs at {depart_time} and arrives at {arrival_time} with a status of {flight_data['status']}." ) |
This function fetches flight data from the AeroAPI and converts UTC times to the local time zones of the departure and arrival airports, which acts as the context to the LLM in providing real-time information about the flight schedules.
## Step 4: Querying Baggage Policies Using ChromaDB
Next, we define a method to query baggage policy information. This information is stored in ChromaDB, a vector database, and we can query it using embeddings based on user input.

123456 |
def get_baggage_context(query: str) -> str: collection = chroma_client.get_collection(name=COLLECTION_NAME, embedding_function=embedding_function) results = collection.query(query_texts=[query], n_results=3) if results and results['documents']: return " ".join(results['documents'][0]) return "No relevant baggage information found." |
Here, we fetch relevant baggage policy information based on the user’s query by searching through the ChromaDB collection.
## Step 5: Setting Up the LLM for Conversational Responses
Now, we will use OpenAI’s GPT-40-mini to generate a response that incorporates the context (flight status or baggage policy).

123456789 |
def get_llm_response(query: str, context: str) -> str: response = openai_client.chat.completions.create( model="gpt-4o-mini", messages=[ {"role": "system", "content": "You are a helpful airline assistant. Answer the user query based on the context provided."}, {"role": "user", "content": f"Query: {query}\nContext: {context}"}, ], ) return response.choices[0].message.content |
The language model takes in both the user query and the context (i.e., flight status or baggage policy) and generates a response.
## Step 6: Indexing Baggage Policies
Let’s index the baggage policy rules in ChromaDB so that we can query them when needed.

12345678910111213141516171819 |
def index_baggage_policy(): baggage_rules = [ "Emirates Airlines offers a generous baggage policy that varies based on route, fare type, and cabin class.", "Economy passengers are allowed one carry-on bag up to 7 kg with dimensions of 55 x 38 x 20 cm.", # ... more rules ] if COLLECTION_NAME not in [col.name for col in chroma_client.list_collections()]: collection = chroma_client.create_collection( name=COLLECTION_NAME, embedding_function=embedding_function, metadata={"hnsw:space": "cosine"} ) for idx, rule in enumerate(baggage_rules): collection.add(documents=[rule], ids=[f"baggage_rule_{idx}"]) print(f"Stored {len(baggage_rules)} baggage rules in ChromaDB.") else: collection = chroma_client.get_collection(name=COLLECTION_NAME) return collection |
## Step 7: Routing Queries Using Semantic Router
To enhance the user experience, we set up a router that intelligently determines whether the query is related to flights, baggage or other conversational tasks like jokes or poems.

123456789101112131415161718 |
def setup_router(): encoder = OpenAIEncoder() flight_info = Route( name="flight_info", utterances=["What's the status of my flight?", "When does my flight depart?"], function_schemas=get_schemas_openai([get_flight_context]) ) baggage_policy = Route( name="baggage_policy", utterances=["What's the baggage allowance?", "How many bags can I bring?"], function_schemas=get_schemas_openai([get_baggage_context]) ) chat = Route( name="chat", utterances=["Write a poem", "Tell me a joke"] ) llm = OpenAILLM() return RouteLayer(encoder, routes=[flight_info, baggage_policy, chat], llm=llm) |
This step is the most crucial. It sets up a semantic router to intelligently route user queries to the appropriate function based on intent. It defines routes for flight information, baggage policies and general conversations. Each route links specific utterances to functions, using OpenAIEncoder to understand the query context. The router then determines if the query requires flight data and baggage details from ChromaDB, or a conversational response — ensuring accurate and efficient processing by the right handler within the system.
Notice that we have three routes mapped to possible user queries. The first route maps to the FlightAware API by mapping the function and arguments to the `get_flight_context`
function. The second route has utterances related to the baggage policy, which is pointing to the `get_baggage_context`
function responsible for retrieving data from the vector database. The third route has no function associated with it; it acts as a “catch all” route.

## Step 8: Processing User Queries and Invoking the Workflow
Finally, we process user queries through the router and provide an appropriate response.

1234567891011121314 |
def process_query(query: str, router_layer: RouteLayer): response = router_layer(query) context = "No relevant context found." if response.function_call: for call in response.function_call: if call["function_name"] == "get_flight_context": context = get_flight_context(**call["arguments"]) elif call["function_name"] == "get_baggage_context": context = get_baggage_context(**call["arguments"]) llm_response = get_llm_response(query, context) print(f"Query: {query}") print(f"Context: {context}") print(f"LLM Response: {llm_response}\n") |
Here’s the main function that ties everything together.
123456789101112131415 |
def main(): index_baggage_policy() router_layer = setup_router() queries = [ "What's the status of flight EK524?", "What's the size limit for cabin baggage?", "Write a poem about a cat." ] for query in queries: process_query(query, router_layer)if __name__ == "__main__": main() |
Here is the complete code available as a [GitHub Gist](https://gist.github.com/janakiramm/978806b1476c2a98a226c353808df82f).
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)