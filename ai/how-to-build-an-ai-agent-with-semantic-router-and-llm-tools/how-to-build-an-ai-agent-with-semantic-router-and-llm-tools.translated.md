# 如何使用语义路由器和 LLM 工具构建 AI 代理

![如何使用语义路由器和 LLM 工具构建 AI 代理的特征图像](https://cdn.thenewstack.io/media/2024/10/25b311e9-allison-saeng-7sp_xmpmfho-unsplashb-1024x576.jpg)

在上一篇文章中，我[介绍了语义路由器](https://thenewstack.io/semantic-router-and-its-role-in-designing-agentic-workflows/): 一种使 [AI 代理](https://thenewstack.io/ai-agents-key-concepts-and-how-they-overcome-llm-limitations/) 能够为正确的任务选择正确的 LLM 的模式，同时还减少了它们对 LLM 的依赖。在本教程的后续内容中，我们将使用 [语义路由器](https://github.com/aurelio-labs/semantic-router) 项目通过选择最佳信息检索方式（例如是否使用[向量数据库](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/) 和/或基于工具的实时数据检索器）来智能地处理用户查询。

与[之前的教程](https://thenewstack.io/how-to-build-a-real-time-app-with-gpt-4o-function-calling/) 类似，在我们的示例中，我们将使用 [FlightAware 的 AeroAPI](https://www.flightaware.com/commercial/aeroapi) 中的数据实时跟踪飞机的航班状态。

首先，请注意，路由器会根据意图动态路由查询，确保检索到最相关的上下文，这使得这种方法独一无二。语义路由器采用 OpenAI 的 LLM 和结构化检索方法，并将它们结合起来，创建了一个自适应的、高响应的助手，可以快速处理对话查询和特定于数据的请求。

语义路由器建议调用该工具来查询航班时刻表和状态，同时将有关行李政策的查询路由到提供上下文的搜索功能。

让我们逐步分解一下。

## 第 1 步：设置您的环境

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

## 第 2 步：初始化 OpenAI 和 ChromaDB 客户端

我们首先初始化 OpenAI 和 ChromaDB 的客户端。OpenAI 将为我们的查询生成嵌入，而 ChromaDB 将存储和检索上下文数据的嵌入，例如行李政策。

```python
# 初始化 OpenAI 客户端
openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# 初始化 ChromaDB 客户端，使用持久存储路径
chroma_client = chromadb.PersistentClient(path="./chroma_db")

# 使用 OpenAI 的模型设置嵌入函数
embedding_function = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.environ["OPENAI_API_KEY"], model_name="text-embedding-3-small"
)
COLLECTION_NAME = "baggage_policy"
```

## 第 3 步：从 AeroAPI 获取航班数据

FlightAware 的 AeroAPI 提供实时航班数据。函数 `get_flight_context` 检索特定航班 ID 的航班信息，包括出发、到达时间和状态。

```python
def get_flight_context(flight_id: str) -> Dict[str, Any]:
    """
    使用 FlightAware AeroAPI 获取航班上下文。
    """
    url = f"https://aeroapi.flightaware.com/aeroapi/flights/{flight_id}"
    headers = {"x-apikey": os.environ["AEROAPI_KEY"]}
    response = requests.get(url, headers=headers)
    data = response.json()
    # ... (代码继续)
```
```python
AEROAPI_BASE_URL = "https://aeroapi.flightaware.com/aeroapi"
AEROAPI_KEY = os.getenv("AEROAPI_KEY")

def get_flight_context(flight_id: str) -> str: 
    def _get_flight_data() -> dict:
        session = requests.Session()
        session.headers.update({"x-apikey": AEROAPI_KEY})
        start_date = datetime.now().strftime('%Y-%m-%d')
        end_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        response = session.get(f"{AEROAPI_BASE_URL}/flights/{flight_id}?start={start_date}&end={end_date}")
        response.raise_for_status()
        return response.json()['flights'][0]

    def _utc_to_local(utc_date_str: str, local_timezone_str: str) -> str:
        utc_datetime = datetime.strptime(utc_date_str, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=pytz.utc)
        local_timezone = pytz.timezone(local_timezone_str)
        local_datetime = utc_datetime.astimezone(local_timezone)
        return local_datetime.strftime('%Y-%m-%d %H:%M:%S')

    flight_data = _get_flight_data()
    depart_time = _utc_to_local(flight_data['scheduled_out'], flight_data['origin']['timezone'])
    arrival_time = _utc_to_local(flight_data['scheduled_in'], flight_data['destination']['timezone'])
    return (
        f"航班 {flight_id} 从 {flight_data['origin']['city']} 到 {flight_data['destination']['city']} "
        f"起飞时间为 {depart_time}，到达时间为 {arrival_time}，航班状态为 {flight_data['status']}。"
    ) 

# 此函数从 AeroAPI 获取航班数据，并将 UTC 时间转换为出发和到达机场的当地时区，作为 LLM 提供有关航班时刻表的实时信息的上下文。

## 步骤 4：使用 ChromaDB 查询行李政策

接下来，我们定义一个查询行李政策信息的方法。这些信息存储在矢量数据库 ChromaDB 中，我们可以使用基于用户输入的嵌入来查询它。

```python
def get_baggage_context(query: str) -> str:
    collection = chroma_client.get_collection(name=COLLECTION_NAME, embedding_function=embedding_function)
    results = collection.query(query_texts=[query], n_results=3)
    if results and results['documents']:
        return " ".join(results['documents'][0])
    return "未找到相关的行李信息。"
```

在这里，我们通过搜索 ChromaDB 集合，根据用户的查询获取相关的行李政策信息。

## 步骤 5：设置 LLM 以进行对话式响应

现在，我们将使用 OpenAI 的 GPT-40-mini 生成包含上下文（航班状态或行李政策）的响应。

```python
def get_llm_response(query: str, context: str) -> str:
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "您是一位乐于助人的航空公司助理。请根据提供的上下文回答用户查询。"},
            {"role": "user", "content": f"查询：{query}\n上下文：{context}"},
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
        "阿联酋航空提供慷慨的行李政策，具体取决于航线、票价类型和舱位等级。",
        "经济舱乘客允许携带一件重量不超过 7 公斤的随身行李，尺寸为 55 x 38 x 20 厘米。",
        # ... 更多规则
    ]
    if COLLECTION_NAME not in [col.name for col in chroma_client.list_collections()]:
        collection = chroma_client.create_collection(
            name=COLLECTION_NAME,
            embedding_function=embedding_function,
            metadata={"hnsw:space": "cosine"}
        )
        for idx, rule in enumerate(baggage_rules):
            collection.add(documents=[rule], ids=[f"baggage_rule_{idx}"])
        print(f"已将 {len(baggage_rules)} 条行李规则存储在 ChromaDB 中。")
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
        utterances=["我的航班状态如何？", "我的航班何时起飞？"],
        function_schemas=get_schemas_openai([get_flight_context])
    )
    baggage_policy = Route(
        name="baggage_policy",
        utterances=["行李限额是多少？", "我可以带多少件行李？"],
        function_schemas=get_schemas_openai([get_baggage_context])
    )
    chat = Route(
        name="chat",
        utterances=["写一首诗", "给我讲个笑话"]
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

[YOUTUBE.COM/THENEWSTACK
技术发展日新月异，请勿错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、采访、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)