
<!--
title: 使用ChromaDB和Python构建RAG驱动的LLM聊天应用
cover: https://cdn.thenewstack.io/media/2024/03/dfa91eb2-rag-llm-chat-app-python.jpg
-->

利用检索增强生成 (RAG) 和大型语言模型 (LLM) 的强大功能来创建生成式 AI 应用程序。

> 译自 [How to Build a RAG-Powered LLM Chat App with ChromaDB and Python](https://thenewstack.io/how-to-build-a-rag-powered-llm-chat-app-with-chromadb-and-python/)，作者 Oladimeji Sowole。

生成式 AI 正以其创建上下文相关内容的能力彻底改变技术，开创了 AI 可能性的新时代。其核心是 [检索增强生成 (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/)，它将信息检索与 [大型语言模型 (LLM)](https://www.cloudflare.com/en-gb/learning/ai/what-is-large-language-model/) 相结合，从外部文档中生成智能、明智的响应。

本教程解释了如何使用 [ChromaDB](https://www.trychroma.com/) 构建 RAG 驱动的 LLM 应用程序，ChromaDB 是一款以 AI 为本、开源的嵌入式数据库，以其高效处理大型数据集而闻名。我将指导你完成每一步，展示 RAG 在创建高级 LLM 应用程序中的实际适用性。

## 你需要什么

要开始构建你的 LLM 应用程序，你需要 [Python](https://thenewstack.io/python/)（可从 [Python 官方网站](https://www.python.org/downloads/) 下载）、OpenAI API 密钥（可在 [OpenAI 平台](https://platform.openai.com/signup) 上获得）以及对 Python 和 Web API 的基本了解。这些技术将帮助确保在遵循本教程和开发生成式 AI 驱动的聊天应用程序时获得顺畅的体验。

## 设置项目

下载完所需的应用程序和技术后，开始设置你的项目环境。

**1. 创建并导航到项目目录：** 在你的终端中，创建一个新目录：

```
mkdir rag_lmm_application
```

将你的工作目录更改为项目文件夹：

```
cd rag_lmm_application
```

**2. 创建你的虚拟环境：** 这是依赖项管理的关键步骤。你可以使用以下命令创建一个虚拟环境：

```
python -m venv venv
```

并激活它。

对于 Mac 或 Linux：

```
source venv/bin/activate
```

对于 Windows：

```
Venv\Scripts\activate
```

**3. 安装必需的包：** 使用以下命令为你的项目安装必要的库：

```
pip install -r requirements.txt
```

requirements.txt 内容为：

```
openai
langchain
docx2txt
pypdf
streamlit
chromadb
tiktoken
```

完成这些步骤后，你的环境已准备就绪，你可以开始使用 ChromaDB 构建最先进的 RAG 聊天应用程序。

## 加载和处理文档

此 LLM 应用程序使用 [LangChain](https://thenewstack.io/how-to-build-a-qa-llm-application-with-langchain-and-gemini/) 加载器熟练地处理各种文档格式，包括 PDF、DOCX 和 TXT。这对于启用外部数据可访问性、确保高效的数据处理和维护后续阶段的统一数据准备至关重要。以下代码片段说明了该过程：

```python
# loading PDF, DOCX and TXT files as LangChain Documents 
def load_document(file): 
	import os 
	name, extension = os.path.splitext(file) 
 
	if extension == '.pdf': 
    	from langchain.document_loaders import PyPDFLoader 
    	print(f'Loading {file}') 
    	loader = PyPDFLoader(file) 
	elif extension == '.docx': 
    	from langchain.document_loaders import Docx2txtLoader 
    	print(f'Loading {file}') 
    	loader = Docx2txtLoader(file) 
	elif extension == '.txt': 
    	from langchain.document_loaders import TextLoader 
    	loader = TextLoader(file) 
	else: 
    	print('Document format is not supported!') 
    	return None 
 
	data = loader.load() 
	return data
```

数据分块——将不同信息分组到更易于管理或更有意义的块中——简化了处理和嵌入，并实现了高效的上下文保留和信息检索。以下代码片段演示了这一重要过程：

```python
# splitting data in chunks 
def chunk_data(data, chunk_size=256, chunk_overlap=20): 
	from langchain.text_splitter import RecursiveCharacterTextSplitter 
	text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap) 
	chunks = text_splitter.split_documents(data) 
	return chunks 
```

## 使用 OpenAI 和 ChromaDB 创建嵌入

在此应用程序中，RAG 使用 [OpenAI](https://thenewstack.io/why-microsoft-has-to-save-openai/) 语言模型创建嵌入——文本的基本向量表示，以便高效地理解数据。这些嵌入对于 RAG 的检索至关重要，允许访问相关外部数据。它们有效地存储在 ChromaDB 中，可以快速检索信息，如下面的代码片段所示。此过程极大地增强了应用程序的 AI 能力。

```python
# create embeddings using OpenAIEmbeddings() and save them in a Chroma vector store 
def create_embeddings(chunks): 
	embeddings = OpenAIEmbeddings() 
	vector_store = Chroma.from_documents(chunks, embeddings) 
 
	# if you want to use a specific directory for chromadb 
	# vector_store = Chroma.from_documents(chunks, embeddings, persist_directory='./mychroma_db') 
	return vector_store 
```

## 使用 Streamlit 构建聊天界面

[Streamlit](https://streamlit.io/) 是一款应用程序，它可以在[几分钟内将数据脚本转换为可共享的 Web 应用程序](https://thenewstack.io/streamlit-an-app-builder-for-the-data-science-team/)。此 RAG LLM 应用程序将用户输入链接到后端处理。通过 Streamlit 的初始化和布局设计，用户可以上传文档和管理数据。后端处理这些输入，并直接在 Streamlit 界面中返回响应，显示前端和后端操作的无缝集成。

以下代码显示了如何在 Streamlit 中创建文本输入字段和处理用户输入。

```python
def ask_and_get_answer(vector_store, q, k=3): 
	from langchain.chains import RetrievalQA 
	from langchain.chat_models import ChatOpenAI 
 
	llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=1) 
	retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k': k}) 
	chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever) 
 
	answer = chain.run(q) 
	return answer 
 
# calculate embedding cost using tiktoken 
def calculate_embedding_cost(texts): 
	import tiktoken 
	enc = tiktoken.encoding_for_model('text-embedding-ada-002') 
	total_tokens = sum([len(enc.encode(page.page_content)) for page in texts]) 
	# print(f'Total Tokens: {total_tokens}') 
	# print(f'Embedding Cost in USD: {total_tokens / 1000 * 0.0004:.6f}') 
	return total_tokens, total_tokens / 1000 * 0.0004 
 
# clear the chat history from streamlit session state 
def clear_history(): 
	if 'history' in st.session_state: 
    	del st.session_state['history'] 
 
 
if __name__ == "__main__": 
	import os 
 
	# loading the OpenAI api key from .env 
	from dotenv import load_dotenv, find_dotenv 
	load_dotenv(find_dotenv(), override=True) 
 
	st.image('img.png') 
	st.subheader('LLM Question-Answering Application 🤖') 
	with st.sidebar: 
    	# text_input for the OpenAI API key (alternative to python-dotenv and .env) 
    	api_key = st.text_input('OpenAI API Key:', type='password') 
    	if api_key: 
        	os.environ['OPENAI_API_KEY'] = api_key 
 
    	# file uploader widget 
    	uploaded_file = st.file_uploader('Upload a file:', type=['pdf', 'docx', 'txt']) 
 
    	# chunk size number widget 
    	chunk_size = st.number_input('Chunk size:', min_value=100, max_value=2048, value=512, on_change=clear_history) 
 
    	# k number input widget 
    	k = st.number_input('k', min_value=1, max_value=20, value=3, on_change=clear_history) 
 
    	# add data button widget 
    	add_data = st.button('Add Data', on_click=clear_history) 
 
    	if uploaded_file and add_data: # if the user browsed a file 
        	with st.spinner('Reading, chunking and embedding file ...'): 
 
            	# writing the file from RAM to the current directory on disk 
            	bytes_data = uploaded_file.read() 
            	file_name = os.path.join('./', uploaded_file.name) 
            	with open(file_name, 'wb') as f: 
                	f.write(bytes_data) 
 
            	data = load_document(file_name) 
            	chunks = chunk_data(data, chunk_size=chunk_size) 
            	st.write(f'Chunk size: {chunk_size}, Chunks: {len(chunks)}') 
 
            	tokens, embedding_cost = calculate_embedding_cost(chunks) 
            	st.write(f'Embedding cost: ${embedding_cost:.4f}') 
 
            	# creating the embeddings and returning the Chroma vector store 
            	vector_store = create_embeddings(chunks) 
 
            	# saving the vector store in the streamlit session state (to be persistent between reruns) 
            	st.session_state.vs = vector_store 
            	st.success('File uploaded, chunked and embedded successfully.') 
```

完成此设置后，用户可以与 AI 应用程序无缝直观地交互。

## 检索答案并增强用户交互

此 RAG 聊天应用程序利用 [LangChain 的 RetrievalQA](https://python.langchain.com/docs/modules/data_connection/) 和 ChromaDB，从 ChromaDB 的嵌入数据中提取相关、准确的信息，高效地响应用户查询，展示了高级生成式 AI 能力。

以下代码片段演示了在 Streamlit 应用程序中实际实现此过程：

```python
# user's question text input widget 
	q = st.text_input('Ask a question about the content of your file:') 
	if q: # if the user entered a question and hit enter 
    	if 'vs' in st.session_state: # if there's the vector store (user uploaded, split and embedded a file) 
        	vector_store = st.session_state.vs 
        	st.write(f'k: {k}') 
        	answer = ask_and_get_answer(vector_store, q, k) 
 
        	# text area widget for the LLM answer 
        	st.text_area('LLM Answer: ', value=answer) 
 
        	st.divider() 
 
        	# if there's no chat history in the session state, create it 
        	if 'history' not in st.session_state: 
            	st.session_state.history = '' 
 
        	# the current question and answer 
        	value = f'Q: {q} \nA: {answer}' 
 
        	st.session_state.history = f'{value} \n {"-" * 100} \n {st.session_state.history}' 
        	h = st.session_state.history 
 
        	# text area widget for the chat history 
        	st.text_area(label='Chat History', value=h, key='history', height=400) 
```

此代码集成了 Streamlit 中的用户输入和响应生成。它使用 ChromaDB 的矢量数据获取准确的答案，增强了聊天应用程序的交互性，并提供了信息丰富的 AI 对话。

## 结论

本教程探讨了使用 OpenAI、ChromaDB 和 Streamlit 构建 LLM 应用程序的复杂性。它解释了如何设置环境、处理文档、创建和存储嵌入，以及构建用户友好的聊天界面，突出了 RAG 和 ChromaDB 在生成式 AI 中的强大组合。

此 [GitHub 存储库](https://github.com/sowole-aims/chat-with-documents-app) 涵盖了该过程。要运行该应用程序，请在终端中执行以下命令：

```
streamlit run ./chat_with_documents.py
```

您现在可以通过导航到 http://localhost:8501 来测试该应用程序。

我鼓励您尝试此应用程序，使其成为您自己的应用程序，并与他人分享您的经验！
