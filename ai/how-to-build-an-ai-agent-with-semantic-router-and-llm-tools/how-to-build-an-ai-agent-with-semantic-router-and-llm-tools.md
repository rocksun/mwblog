
<!--
title: 如何使用语义路由器和 LLM 工具构建 AI 代理
cover: https://cdn.thenewstack.io/media/2024/10/25b311e9-allison-saeng-7sp_xmpmfho-unsplashb.jpg
-->

在本 AI 代理教程中，我们使用语义路由器来选择从 OpenAI LLM 和其他 AI 工具检索信息的最佳方式。

> 译自 [How to Build an AI Agent With Semantic Router and LLM Tools](https://thenewstack.io/how-to-build-an-ai-agent-with-semantic-router-and-llm-tools/)，作者 Janakiram MSV。

在上一篇文章中，我[介绍了语义路由器](https://thenewstack.io/semantic-router-and-its-role-in-designing-agentic-workflows/): 一种使 [AI 代理](https://thenewstack.io/ai-agents-key-concepts-and-how-they-overcome-llm-limitations/) 能够为正确的任务选择正确的 LLM 的模式，同时还减少了它们对 LLM 的依赖。在本教程的后续内容中，我们将使用 [语义路由器](https://github.com/aurelio-labs/semantic-router) 项目通过选择最佳信息检索方式（例如是否使用[向量数据库](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/) 和/或基于工具的实时数据检索器）来智能地处理用户查询。

与[之前的教程](https://thenewstack.io/how-to-build-a-real-time-app-with-gpt-4o-function-calling/) 类似，在我们的示例中，我们将使用 [FlightAware 的 AeroAPI](https://www.flightaware.com/commercial/aeroapi) 中的数据实时跟踪飞机的航班状态。

首先，请注意，路由器会根据意图动态路由查询，确保检索到最相关的上下文，这使得这种方法独一无二。语义路由器采用 OpenAI 的 LLM 和结构化检索方法，并将它们结合起来，创建了一个自适应的、高响应的助手，可以快速处理对话查询和特定于数据的请求。

![](https://cdn.thenewstack.io/media/2024/09/e833a452-sr-t-1-1024x349.png)

语义路由器建议调用该工具来查询航班时刻表和状态，同时将有关行李政策的查询路由到提供上下文的搜索功能。

让我们逐步分解一下。

## 步骤 1：设置您的环境

在我们深入研究代码之前，请确保您已安装所需的库。您可以使用 pip 来完成此操作：

```bash
pip install openai chromadb requests pytz semantic-router
```

让我们导入所需的模块。

```python
import os
from typing import Dict, Any
from datetime import datetime, timedelta
import pytz
import requests
 
from openai import OpenAI
 
import chromadb
from chromadb.utils import embedding_functions
 
from semantic_router import Route, RouteLayer
from semantic_router.encoders import OpenAIEncoder
from semantic_router.llms.openai import get_schemas_openai
from semantic_router.llms import OpenAILLM
```

接下来，为 OpenAI 和 FlightAware AeroAPI 密钥设置您的环境变量：

```bash
export OPENAI_API_KEY="your_openai_api_key"
export AEROAPI_KEY="your_flightaware_api_key"
```

这些密钥对于访问教程中使用的外部服务至关重要。

## 步骤 2：初始化 OpenAI 和 ChromaDB 客户端

我们首先初始化 OpenAI 和 ChromaDB 的客户端。OpenAI 将为我们的查询生成嵌入，而 ChromaDB 将存储和检索上下文数据的嵌入，例如行李政策。

```python
# Initialize OpenAI client
openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
 
# Initialize ChromaDB client with a persistent storage path
chroma_client = chromadb.PersistentClient(path="./chroma_db")
 
# Set up embedding function using OpenAI's model
embedding_function = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.environ["OPENAI_API_KEY"],
    model_name="text-embedding-3-small"
)
COLLECTION_NAME = "baggage_policy"
```

## 步骤 3：从 AeroAPI 获取航班数据

FlightAware 的 AeroAPI 提供实时航班数据。函数 `get_flight_context` 检索特定航班 ID 的航班信息，包括出发、到达时间和状态。

```python
AEROAPI_BASE_URL = "https://aeroapi.flightaware.com/aeroapi"
AEROAPI_KEY = os.getenv("AEROAPI_KEY")
 
def get_flight_context(flight_id: str) -&gt; str:
    def _get_flight_data() -&gt; dict:
        session = requests.Session()
        session.headers.update({"x-apikey": AEROAPI_KEY})
        start_date = datetime.now().strftime('%Y-%m-%d')
        end_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        response = session.get(f"{AEROAPI_BASE_URL}/flights/{flight_id}?start={start_date}&amp;end={end_date}")
        response.raise_for_status()
        return response.json()['flights'][0]
 
    def _utc_to_local(utc_date_str: str, local_timezone_str: str) -&gt; str:
        utc_datetime = datetime.strptime(utc_date_str, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc)
        local_timezone = pytz.timezone(local_timezone_str)
        local_datetime = utc_datetime.astimezone(local_timezone)
        return local_datetime.strftime('%Y-%m-%d %H:%M:%S')
 
    flight_data = _get_flight_data()
    depart_time = _utc_to_local(flight_data['scheduled_out'], flight_data['origin']['timezone'])
    arrival_time = _utc_to_local(flight_data['scheduled_in'], flight_data['destination']['timezone'])
    return (
        f"Flight {flight_id} from {flight_data['origin']['city']} to {flight_data['destination']['city']} "
        f"departs at {depart_time} and arrives at {arrival_time} with a status of {flight_data['status']}."
    )
```

此函数从 AeroAPI 获取航班数据，并将 UTC 时间转换为出发和到达机场的当地时区，作为 LLM 提供有关航班时刻表的实时信息的上下文。

## 步骤 4：使用 ChromaDB 查询行李政策

接下来，我们定义一个查询行李政策信息的方法。这些信息存储在矢量数据库 ChromaDB 中，我们可以使用基于用户输入的嵌入来查询它。

```python
def get_baggage_context(query: str) -&gt; str:
    collection = chroma_client.get_collection(name=COLLECTION_NAME, embedding_function=embedding_function)
    results = collection.query(query_texts=[query], n_results=3)
    if results and results['documents']:
        return " ".join(results['documents'][0])
    return "No relevant baggage information found."
```

在这里，我们通过搜索 ChromaDB 集合，根据用户的查询获取相关的行李政策信息。

## 步骤 5：设置 LLM 以进行对话式响应

现在，我们将使用 OpenAI 的 GPT-40-mini 生成包含上下文（航班状态或行李政策）的响应。

```python
def get_llm_response(query: str, context: str) -&gt; str:
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful airline assistant. Answer the user query based on the context provided."},
            {"role": "user", "content": f"Query: {query}\nContext: {context}"},
        ],
    )
    return response.choices[0].message.content
```

语言模型接收用户查询和上下文（即航班状态或行李政策），并生成响应。

## 步骤 6：索引行李政策

让我们在 ChromaDB 中索引行李政策规则，以便我们可以在需要时查询它们。

```python
def index_baggage_policy():
    baggage_rules = [
        "Emirates Airlines offers a generous baggage policy that varies based on route, fare type, and cabin class.",
        "Economy passengers are allowed one carry-on bag up to 7 kg with dimensions of 55 x 38 x 20 cm.",
        # ... more rules
    ]
 
    if COLLECTION_NAME not in [col.name for col in chroma_client.list_collections()]:
        collection = chroma_client.create_collection(
            name=COLLECTION_NAME,
            embedding_function=embedding_function,
            metadata={"hnsw:space": "cosine"}
        )
        for idx, rule in enumerate(baggage_rules):
            collection.add(documents=[rule], ids=[f"baggage_rule_{idx}"])
        print(f"Stored {len(baggage_rules)} baggage rules in ChromaDB.")
    else:
        collection = chroma_client.get_collection(name=COLLECTION_NAME)
    return collection
```

## 步骤 7：使用语义路由器路由查询

为了增强用户体验，我们设置了一个路由器，可以智能地确定查询是与航班、行李相关，还是与笑话或诗歌等其他对话任务相关。

```python
def setup_router():
    encoder = OpenAIEncoder()
    flight_info = Route(
        name="flight_info", 
        utterances=["What's the status of my flight?", "When does my flight depart?"],
        function_schemas=get_schemas_openai([get_flight_context])
    )
    baggage_policy = Route(
        name="baggage_policy",
        utterances=["What's the baggage allowance?", "How many bags can I bring?"],
        function_schemas=get_schemas_openai([get_baggage_context])
    )
    chat = Route(
        name="chat",
        utterances=["Write a poem", "Tell me a joke"]
    )
    llm = OpenAILLM()
    return RouteLayer(encoder, routes=[flight_info, baggage_policy, chat], llm=llm)
```

这一步至关重要。它设置了一个语义路由器，根据意图将用户查询智能路由到适当的函数。它定义了航班信息、行李政策和一般对话的路由。每个路由都使用 OpenAIEncoder 将特定语句链接到函数，以理解查询上下文。路由器随后确定查询是需要来自 ChromaDB 的航班数据和行李详细信息，还是需要对话响应，从而确保系统内正确的处理程序能够准确有效地处理查询。

请注意，我们有三个路由映射到可能的 用户查询。第一个路由通过将函数和参数映射到 `get_flight_context` 函数来映射到 FlightAware API。第二个路由包含与行李政策相关的语句，这些语句指向负责从向量数据库检索数据的 `get_baggage_context` 函数。第三条路线没有关联的函数；它充当“包罗万象”的路线。

## 步骤 8：处理用户查询和调用工作流

最后，我们通过路由器处理用户查询并提供适当的响应。

```python
def process_query(query: str, router_layer: RouteLayer):
    response = router_layer(query)
    context = "No relevant context found."
    if response.function_call:
        for call in response.function_call:
            if call["function_name"] == "get_flight_context":
                context = get_flight_context(**call["arguments"])
            elif call["function_name"] == "get_baggage_context":
                context = get_baggage_context(**call["arguments"])
 
    llm_response = get_llm_response(query, context)
    print(f"Query: {query}")
    print(f"Context: {context}")
    print(f"LLM Response: {llm_response}\n")
```

这是将所有内容联系在一起的主要功能。

```python
def main():
    index_baggage_policy()
    router_layer = setup_router()
    
    queries = [
        "What's the status of flight EK524?",
        "What's the size limit for cabin baggage?",
        "Write a poem about a cat."
    ]
 
    for query in queries:
        process_query(query, router_layer)
 
if __name__ == "__main__":
    main()
```

完整的代码可在 [GitHub Gist](https://gist.github.com/janakiramm/978806b1476c2a98a226c353808df82f) 中找到。

```py
import os
from typing import Dict, Any
from datetime import datetime, timedelta
import pytz
import requests

from openai import OpenAI

import chromadb
from chromadb.utils import embedding_functions

from semantic_router import Route, RouteLayer
from semantic_router.encoders import OpenAIEncoder
from semantic_router.llms.openai import get_schemas_openai
from semantic_router.llms import OpenAILLM

# Constants
AEROAPI_BASE_URL = "https://aeroapi.flightaware.com/aeroapi"
export AEROAPI_KEY="your_flightaware_api_key"
COLLECTION_NAME = "baggage_policy"

# Initialize clients
openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
embedding_function = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.environ["OPENAI_API_KEY"],
    model_name="text-embedding-3-small"
)
chroma_client = chromadb.PersistentClient(path="./chroma_db")

def get_flight_context(flight_id: str) -> str:
    def _get_flight_data() -> Dict[str, Any]:
        session = requests.Session()
        session.headers.update({"x-apikey": AEROAPI_KEY})
        start_date = datetime.now().date().strftime('%Y-%m-%d')
        end_date = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
        api_resource = f"/flights/{flight_id}?start={start_date}&end={end_date}"
        response = session.get(f"{AEROAPI_BASE_URL}{api_resource}")
        response.raise_for_status()
        flights = response.json().get('flights', [])
        if not flights:
            raise ValueError(f"No flight data found for flight ID {flight_id}.")
        return flights[0]

    def _utc_to_local(utc_date_str: str, local_timezone_str: str) -> str:
        utc_datetime = datetime.strptime(utc_date_str, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc)
        local_timezone = pytz.timezone(local_timezone_str)
        local_datetime = utc_datetime.astimezone(local_timezone)
        return local_datetime.strftime('%Y-%m-%d %H:%M:%S')

    flight_data = _get_flight_data()
    dep_key = 'estimated_out' if flight_data.get('estimated_out') else 'scheduled_out'
    arr_key = 'estimated_in' if flight_data.get('estimated_in') else 'scheduled_in'

    flight_details = {
        'source': flight_data['origin']['city'],
        'destination': flight_data['destination']['city'],
        'depart_time': _utc_to_local(flight_data[dep_key], flight_data['origin']['timezone']),
        'arrival_time': _utc_to_local(flight_data[arr_key], flight_data['destination']['timezone']),
        'status': flight_data['status']
    }
    
    return (
        f"The current status of flight {flight_id} from {flight_details['source']} to {flight_details['destination']} "
        f"is {flight_details['status']} with departure time at {flight_details['depart_time']} and arrival time at "
        f"{flight_details['arrival_time']}."
    )

def get_baggage_context(query: str) -> str:
    collection = chroma_client.get_collection(name=COLLECTION_NAME, embedding_function=embedding_function)
    results = collection.query(query_texts=[query], n_results=3)
    if results and results['documents']:
        return " ".join(results['documents'][0])
    return "No relevant baggage information found."

def get_llm_response(query: str, context: str) -> str:
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful airline assistant. Answer the user query based on the context provided."},
            {"role": "user", "content": f"Query: {query}\nContext: {context}"},
        ],
    )
    return response.choices[0].message.content

def index_baggage_policy():
    baggage_rules = [
        "Emirates Airlines offers a generous baggage policy that varies based on route, fare type, and cabin class.",
        "For carry-on luggage, Economy passengers are allowed one piece weighing up to 7 kg with dimensions not exceeding 55 x 38 x 20 cm.",
        # ... (rest of the rules)
    ]

    if COLLECTION_NAME not in [col.name for col in chroma_client.list_collections()]:
        collection = chroma_client.create_collection(
            name=COLLECTION_NAME,
            embedding_function=embedding_function,
            metadata={"hnsw:space": "cosine"}
        )
        for idx, rule in enumerate(baggage_rules):
            collection.add(documents=[rule], ids=[f"baggage_rule_{idx}"])
        print(f"Stored {len(baggage_rules)} baggage rules in ChromaDB.")
    else:
        collection = chroma_client.get_collection(name=COLLECTION_NAME, embedding_function=embedding_function)

    return collection

def setup_router():
    encoder = OpenAIEncoder()
    schemas = get_schemas_openai([get_flight_context, get_baggage_context])

    flight_info = Route(
        name="flight_info", 
        utterances=["What's the status of my flight?", "When does my flight depart?", "Is my flight on time?", "What's the status of flight EK524?"],
        function_schemas=schemas                    
    )

    baggage_policy = Route(
        name="baggage_policy",
        utterances=["What's the baggage allowance?", "How many bags can I bring?", "What are the luggage restrictions?"],
        function_schemas=schemas    
    )

    chitchat = Route(
        name="chat",
        utterances=["Write a poem about a cat.", "Tell me a joke about a rat.", "Why did the chicken cross the road?", "Give me a fun fact."]
    )

    llm = OpenAILLM()
    return RouteLayer(encoder, routes=[flight_info, baggage_policy, chitchat], llm=llm)

def process_query(query: str, router_layer: RouteLayer):
    response = router_layer(query)
    context = "No relevant context found."
    if response.function_call:
        for call in response.function_call:
            if call["function_name"] == "get_flight_context":
                context = get_flight_context(**call["arguments"])
            elif call["function_name"] == "get_baggage_context":
                context = get_baggage_context(**call["arguments"])
    
    llm_response = get_llm_response(query, context)
    print(f"Query: {query}")
    print(f'Function call: {response.function_call}')    
    print(f"Context: {context}")
    print(f"LLM Response: {llm_response}\n")

def main():
    index_baggage_policy()
    router_layer = setup_router()

    queries = [
        "What's the status of flight EK524?",
        "What's the size limit for cabin baggage?",
        "Write a poem about a cat."
    ]

    for query in queries:
        print(f"\nProcessing query: {query}")
        process_query(query, router_layer)


if __name__ == "__main__":
    main()
```