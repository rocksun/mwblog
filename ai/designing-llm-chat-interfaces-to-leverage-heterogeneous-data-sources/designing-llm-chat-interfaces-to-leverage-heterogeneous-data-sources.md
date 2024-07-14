
<!--
title: 设计利用异构数据源的LLM聊天界面
cover: https://cdn.thenewstack.io/media/2024/07/2ce5c343-ai-generated-7982424_1280.jpg
-->

构建有用的 LLM 聊天界面并非没有复杂性和挑战。Deepak Jayablalan 向我们展示了如何做到这一点。

> 译自 [Designing LLM Chat Interfaces to Leverage Heterogeneous Data Sources](https://thenewstack.io/designing-llm-chat-interfaces-to-leverage-heterogeneous-data-sources/)，作者 Deepak Jayablalan。

大型语言模型（[LLM](https://thenewstack.io/llm/)）近年来改变了自然语言处理的游戏规则，使开发人员能够[构建能够像人类一样对话的复杂聊天界面](https://thenewstack.io/top-5-large-language-models-and-how-to-use-them-effectively/)。这些界面的潜力涵盖了客户服务、虚拟助手、培训和教育，以及娱乐平台。但是，构建有用的 LLM 聊天界面并非没有其复杂性和挑战。

我一直致力于整合 AI 功能，并研究如何构建聊天界面以使用 LLM 和代理来导航和利用各种数据源。对于这个概念验证，我使用了 Azure OpenAI 和 Azure 中的其他 AI 功能。它展示了各种用例、设计模式和实现选项。

目标是为架构师和 AI 爱好者提供一个基础，让他们探索 Azure AI 的潜力，并对解决方案方法做出明智的决定。这些用例利用了各种数据源，例如 SQL DB、Cosmos DB、CSV 文件、多个数据源等。该项目的首要目标不仅是展示不同的用例，而且是探索各种实现选项。

## 先决条件：
如果您还没有设置 [Azure](https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart?tabs=command-line%2Cpython-new&pivots=programming-language-studio) 帐户，您可以[在这里](https://azure.microsoft.com/en-us/free#all-free-services) 使用一些免费积分设置一个帐户。

## 与 CSV 聊天：

以下是一个示例，展示了如何使用 LLM 和代理在任何 CSV 文件上构建自然语言界面。通过利用示例代码，用户可以上传预处理的 CSV 文件，询问有关数据的问题，并从 AI 模型中获得答案。

您可以在[此处](https://github.com/deepakj16/chatInterface/blob/main/Chat_with_CSV.py)找到 chat_with_CSV 的完整文件。

### 第 1 步：定义所需的变量，例如 API 密钥、API 端点、加载格式等

我使用了环境变量。您可以将它们放在配置文件中，也可以在同一个文件中定义它们。

```python
file_formats = {
    "csv": pd.read_csv,
    "xls": pd.read_excel,
    "xlsx": pd.read_excel,
    "xlsm": pd.read_excel,
    "xlsb": pd.read_excel,
 
}
 
aoai_endpoint = os.environ["AZURE_OPENAI_ENDPOINT" ]
aoai_api_key = os.environI "AZURE_OPENAI_API_KEY" ]
deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME" ]
aoai_api_version = os.environ[ "AZURE_OPENAI_API_VERSION" ] #"2023-05-15"
aoai_api_type = os.environ["AZURE_OPENAI_API_TYPE"]
```

### 第 2 步：上传文件并创建数据帧

```python
uploaded_file = st. file_uploader(
    "Upload a Data file",
    type=list (file_formats. keys()), 
    help="Supports CSV and Excel files!", 
    on_change=clear_submit,
 
}
 
if uploaded_file:
    df = load_data(uploaded_file)
```

### 第 3 步：使用 AzureChatOpenAI 创建 LLM

为此，我们需要从 langchain_openai 导入 [AzureChatOpenAI](https://python.langchain.com/v0.1/docs/integrations/chat/azure_chat_openai/)，并使用以下参数，

```python
llm = AzureChatOpenAI (azure_endpoint=aoai_endpoint,
    openai_api_key = aoai_api_key,
    temperature=0,
    azure_deployment=deployment_name,
    openai_api_version=aoai_api_version,
    streaming=True)
```

- **azure_endpoint**:Azure 端点，包括资源。
- **openai_api_key**:这是一个用于验证和控制对 OpenAI API 访问的唯一标识符。
- **openai_api_version**:服务 API 使用 API 版本查询参数进行版本控制。所有版本都遵循 YYYY-MM-DD 日期结构。
- **streaming**:默认情况下，此布尔值为 False，表示流是否具有结果。
- **Temperature**:温度是一个参数，用于控制 AI 模型生成的输出的随机性。较低的温度会导致更可预测和更保守的输出。较高的温度允许在响应中具有更多创造力和多样性。这是一种微调模型输出中随机性和确定性之间平衡的方法。
- **deployment_name**:模型部署。如果给出，则将基本客户端 URL 设置为包含 /deployments/{azure_deployment}。注意：这意味着您将无法使用非部署端点。

如果需要，您可以添加更多参数；详细信息请参见此[链接](https://api.python.langchain.com/en/latest/chat_models/langchain_openai.chat_models.azure.AzureChatOpenAI.html)。

### 第 4 步：使用 CSV 和 LLM 创建代理

为此，我们需要从 langchain_experimental.agents 中导入 [create_pandas_dataframe_agent](https://api.python.langchain.com/en/latest/agents/langchain_experimental.agents.agent_toolkits.pandas.base.create_pandas_dataframe_agent.html)，并从 langchain.agent 中导入 [AgentType](https://api.python.langchain.com/en/latest/agents/langchain.agents.agent_types.AgentType.html)。

```python
pandas_df_agent = create_pandas_dataframe_agent(
    llm, 
    df,
    verbose=True,
    agent_type=AgentType.OPENAI_FUNCTIONS,
    handle_parsing_errors=True,
    number_of_head_rows=df.shape[0] #send all the rows to LLM
)
```

pandas 代理是一个使用 create_pandas_dataframe_agent 函数创建的 [LangChain](https://python.langchain.com/v0.2/docs/introduction/) 代理，它接受以下输入和参数，

- 一个 **语言模型 (LLM)** 作为输入。 
- 一个 **pandas 数据帧 (CSV 数据)** 包含数据作为输入。
- **Verbose**: 如果代理返回 Python 代码，检查此代码以了解问题所在可能会有所帮助。您可以通过在创建代理时设置 verbose=True 来做到这一点，这应该会打印出生成的 Python 代码。
- **agent_Type**: 这显示了如何使用 OPENAI_FUNCTIONS 代理类型初始化代理。这将创建一个使用 OpenAI 函数调用来传达其关于采取哪些操作的决定的代理。
- **handle_parsing_error**: 偶尔，LLM 无法确定要采取的步骤，因为其输出格式不正确，无法由输出解析器处理。在这种情况下，默认情况下，代理会出错。但是，您可以使用 handle_parsing_errors 轻松控制此功能。
### 第 5 步：与代理聊天
为此，我们需要使用从 [langchain.callbacks](https://python.langchain.com/v0.1/docs/modules/callbacks/) 中导入 [StreamlitCallbackHandler](https://api.python.langchain.com/en/latest/callbacks/langchain_community.callbacks.streamlit.streamlit_callback_handler.StreamlitCallbackHandler.html)。

当在 panda 代理上调用 run 方法时，它会使用来自提示的输入消息和回调参数，它会经过一系列步骤来生成答案。

```python
        with st.chat_message("assistant"):
            st_cb = StreamlitCallbackHandler (st.container(), expand_new_thoughts=False)
            response = pandas_df_agent.run(st. session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write (response)
if __name__ == "__main__":
    main()
```

最初，代理会识别任务并选择适当的操作从数据帧中检索所需信息。之后，它会观察输出，组合观察结果，并生成最终答案。

## 与数据库聊天：

以下示例代码展示了如何在结构化数据（如 SQL DB 和 NoSQL，如 Cosmos DB）上构建自然语言界面，并利用 Azure OpenAI 的功能。这可以用作 SQL 程序员助手。目标是生成 SQL 代码（SQL Server）以检索对自然语言查询的答案。

您可以在 [此处](https://github.com/deepakj16/chatInterface/blob/main/Chat_with_DB.py) 找到与 chat_with_DB 相关的完整文件。

## 结构化数据，如 SQL DB：

### 第 1 步：加载 Azure 和数据库连接变量

我使用了环境变量；您可以将其作为配置文件或在同一个文件中定义。

```python
#Load environment variables 
load_dotenv ("credentials.env")
 
aoai_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
aoai_api_key = os.environ["AZURE_OPENAI_API_KEY"]
deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]
aoai_api_version = os.environ["AZURE_OPENAI_API_VERSION"]
aoai_api_version_For_COSMOS = "2023-08-01-preview"    #### for cosmos other API versio
aoai_embedding_deployment = os.environ["AZURE_EMBEDDING_MODEL" ]
 
sql_server_name = os.environ["SQL_SERVER_NAME"]
sal_server_db = os.environ["SQL_SERVER_DATABASE"]
sal_server_username = os.environ["SQL_SERVER_USERNAME"]
sal_Server_pwd = os.environ["SQL_SERVER_PASSWORD"]
SQL_ODBC_DRIVER_PATH = os.environ["SQL_ODBC_DRIVER_PATH"]
 
COSMOS_MONGO_CONNECTIONSTRING = os.environ["COSMOS_MONGO_CONNECTIONSTRING"]
COSMOS_MONGO_DBNAME = os.environ["COSMOS_MONGO_DBNAME"]
COSMOS_MONGO_CONTAINER = os.environ["COSMOS_MONGO_CONTAINER"]
COSMOS_MONGO_API = os.environ["COSMOS_MONGO_API"]
```

### 第 2 步：创建 Azure OpenAI 客户端和聊天对话的模型响应

为此，我们需要 python 库 openai。安装完成后，您可以通过导入 openai 和您的 api 密钥来运行以下操作：

为了创建客户端，我们利用 Openai 中的 [AzureOpenAI](https://python.langchain.com/v0.1/docs/integrations/llms/azure_openai/)。

- **api-version**: 有效的 Azure OpenAI API 版本，例如您在导入 API 时选择的 API 版本。
- **api_key**: 用于对 OpenAI 的 API 进行身份验证和控制访问的唯一标识符。


```python
client = openai.AzureOpenAI(
    base_url=f"{aoai_endpoint}/openai/deployments/{deployment_name}/",
    api_key=aoai_api_key,
    api_version="2023-12-01-preview"
)
 
response = client.chat.completions.create(
    model=deployment_name, # The deployment name you chose when you deployed the ChatGPT or GPT-4 model.
 
    messages=messages, 
    temperature=0, 
    max_tokens=2000
 
)
```

获取客户端后，API [ChatCompletions](https://platform.openai.com/docs/guides/text-generation/chat-completions-api) 获取用户提示并为自然语言查询生成 SQL 查询

- **model**: OpenAI 使用模型关键字参数来指定要使用的模型。Azure OpenAI 具有独特的模型[部署](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource?pivots=web-portal#deploy-a-model)的概念。当您使用 Azure OpenAI 时，模型应引用您在部署模型时选择的底层部署名称。有关哪些模型适用于 Chat API 的详细信息，请参阅[模型端点兼容性](https://platform.openai.com/docs/models/model-endpoint-compatibility)表。
- **max_tokens**: 在聊天完成中可以生成的[令牌](https://platform.openai.com/tokenizer)的最大数量。输入令牌和生成令牌的总长度受模型上下文长度的限制。
- **temperature**: 应该使用什么采样温度？介于 0 和 2 之间。较高的值（如 0.8）将使输出更加随机，而较低的值（如 0.2）将使输出更加集中和确定性。我们通常建议更改此值或 top_p，但不要同时更改两者。
- **messages**: 包含迄今为止对话的一系列消息。

如果需要，您可以根据要求添加更多[参数](https://platform.openai.com/docs/api-reference/chat/create)。

### 第 3 步：使用 Panda 读取 sql 以获取查询结果

利用[panda 读取 sql](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html) (**pandas.read_sql( sql, con)**) 将 sql 查询或数据库表读入数据帧，并返回包含查询运行结果的 pandas 数据帧。

```python
def run_sql_query(aoai_sqlquery):
    '''
    Function to run the
    generated SQL Query on SQL server and retrieve output.
    Input: AOAI completion (SQL Query)
    Output: Pandas dataframe containing results of the query run
    '''
    conn = connect_sql_server ()
    df = pd.read_sql(aoai_sqlquery, conn)
    return df
```

## 像 COSMOS DB 这样的 NO SQL：

### 第 1 步：创建 Azure OpenAI 客户端

要创建客户端，我们利用 Openai 的[AzureOpenAI](https://python.langchain.com/v0.1/docs/integrations/llms/azure_openai/)。

- **api-version**: 有效的 Azure OpenAI API 版本，例如您在导入 API 时选择的 API 版本。
- **api_key**: 用于对 OpenAI 的 API 进行身份验证和控制访问的唯一标识符。

```python
client = openai.AzureOpenAI(
    base_url=f"{aoai_endpoint}/openai/deployments/{deployment_name}/extensions/",
    api_key=aoai_api_key,
    api_version=aoai_api_version_For_COSMOS
)
```

### 第 2 步：为聊天对话创建模型响应

获取客户端后，API [ChatCompletions](https://platform.openai.com/docs/guides/text-generation/chat-completions-api) 获取用户提示并为自然语言查询生成查询以及响应。根据要求添加[参数](https://platform.openai.com/docs/api-reference/chat/create) 详细信息。

请确保在使用 Cosmos 作为数据源时包含“extra_body”参数。

```python
return client. chat.completions.create(
    model=deployment_name, 
    messages=[
        {"role": m["role"], "content": m["content"]} 
        for m in messages
],
stream=True, 
extra_body={
    "dataSources": [
        {
            "type": "AzureCosmosDB",
            "parameters": {
                "connectionString": COSMOS._MONGO_CONNECTIONSTRING,
                "indexName" : index_name,
                "containerName": COSMOS_MONGO_CONTAINER,
                "databaseName": COSMOS_MONGO_DBNAME,
                "fieldsMapping": {
                    "contentFieldsSeparator": "\n",
                    "contentFields": ["text"],
                    "filepathField": "id",
                    "titleField": "description",
                    "urlField": None,
                    "vectorFields": ["embedding"],
                },
                "inScope": "true",
                "roleInformation": "You are an AI assistant that helps people find information from retrieved data",
                "embeddingEndpoint": f"{aoai_endpoint}/openai/deployments/{aoai_embedding_deployment}/embeddings/",
                "embeddingKey": aoai_api_key,
                "strictness": 3,
                " topNDocuments": 5,
        }
```

## 通过多种数据源进行聊天：

此 POC 展示了用于使用 Azure AI 服务和编排器通过多种数据源构建聊天界面的多种实现模式。

您可以在[此处](https://github.com/deepakj16/chatInterface/blob/main/Chat_with_Multiple_Data.py)找到通过多种数据源进行聊天的完整文件。


### 第 1 步：定义 Azure 和连接变量

```python
load_dotenv("credentials.env")
 
aoai_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
aoai_api_key = os.environ["AZURE_OPENAI_API_KEY"]
deployment_name = os.environI "AZURE_OPENAI_DEPLOYMENT_NAME"]
aoai_api_version = os.environI "AZURE_OPENAI_API_VERSION"]
 
sal_server_name = os.environ "SQL_SERVER_NAME"]
sal_server_db = os.environ "SQL_SERVER_DATABASE"]
sql_server_username = os. environ[" SQL_SERVER_USERNAME"]
sql_Server_pwd = os.environ "SQL_SERVER_PASSWORD"]
 
blob_connection_string = os.environI "BLOB_CONNECTION_STRING"]
blob_sas_token = os.environ["BLOB_SAS_TOKEN"]
 
azure_cosmos_endpoint = os.environ["AZURE_COSMOSDB_ENDPOINT"]
azure_cosmos_db = os.environ["AZURE_COSMOSDB_NAME"]
azure_cosmos_container = os.environ["AZURE_COSMOSD_CONTAINER"]
azure_cosmos_connection = os.environ["AZURE_COSMOSDB_CONNECTION_STRING"]
```

### 第 2 步：使用 AzureChatOpenAI 创建 LLM 

为此，我们需要从 langchain_openai 导入 AzureChatOpenAI 并使用以下参数，

```python
# Set LLM
llm = AzureChatOpenAI(azure_endpoint=aoai_endpoint,
                        openai_api_key = aoai_api_key,
                        azure_deployment=deployment_name,
                        openai._api_version=aoai_api_version,
                        streaming=False,
                        temperature=0.5,
                        max_tokens=1000
                        ,callback_manager=cb_manager
                    )
```

### 第 3 步：工具方法

所有方法 DocSearchAgent、BingSearchAgent、SQLSearchAgent 和 ChatGPTTool 都在 utils 调用中。

```py
# Initialize our Tools/Experts
text_indexes = [azure_search_covid_index] #, "cogsrch-index-csv"]
doc_search = DocSearchAgent(llm=llm, indexes=text_indexes,
                    k=10, similarity_k=4, reranker_th=1, 
                    sas_token=blob_sas_token, name="docsearch", 
                    verbose=False) #callback_manager=cb_manager
 
www_search = BingSearchAgent(llm=llm, k=5,verbose=False)
sal_search = SQLSearchAgent(llm=llm, k=10,verbose=False)
chatgpt_search = ChatGPTTo01(llm=llm)    #callback_manager=cb_manager
tools = [www_search, sql_search, doc_search, chatgpt_search] #csv_search,
```

### 第 4 步: 创建代理并执行它

为此，我们需要从 langchain.agents 导入 AgentExecutor，create_openai_tools_agent。 

此外，为了运行代理，从 langchain_core.runnables.history 导入 RunnableWithMessageHistory

```py
agent = create_openai_tools_agent(llm, tools, CUSTOM_CHATBOT_PROMPT)
agent_executor = AgentExecutor(agent=agent, tools=tools)
brain_agent_executor = RunnableWithMessageHistory(
    agent_executor, 
    get_session_history, 
    input_messages_key="question", 
    history_messages_key="history", 
    history_factory_config=[
        ConfigurableFieldSpec( 
            id="user_id",
            annotation=str, 
            name="User ID",
            description="Unique identifier for the user.",
            default="",
            is_shared=True,
        ),
        ConfigurableFieldSpec( 
            id="session_id",
            annotation=str, 
            name="Session ID",
            description="Unique identifier for the conversation.",
            default="",
            is_shared=True,
        ),
    ],
)
```

使用 create_openai_tools_agent 创建使用 OpenAItools 和 

- LLM（[BaseLanguageModel](https://api.python.langchain.com/en/latest/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel)）：用作代理的 LLM。
- tools（[Sequence[BaseTool]](https://api.python.langchain.com/en/latest/tools/langchain_core.tools.BaseTool.html)）：此代理可访问的工具。
- prompt（[ChatPromptTemplate](https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.ChatPromptTemplate.html#langchain_core.prompts.chat.ChatPromptTemplate)）：要使用的提示。

在此处引用文件。通过传入代理和工具来创建代理执行器，并使用 RunnableWithMessageHistory 运行代理。必须始终使用包含聊天消息历史记录工厂的适当参数的配置来调用 RunnableWithMessageHistory。

### 第 5 步：使用提示和配置调用代理执行器

```py
response = brain_agent_executor.invoke({"question": prompt},config=config)[ "output"]
```