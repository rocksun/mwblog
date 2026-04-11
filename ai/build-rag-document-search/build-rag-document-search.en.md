As AI advances, more tools are being introduced into the ecosystem, enabling engineers and developers to experiment and build custom AI apps. But it’s not that simple.

In fact, each advantage of AI is accompanied by a disadvantage. For example, with vector databases such as Chroma, the major challenge was efficient data processing. And many of the latest AI applications rely on vector embeddings as [the core of LLMs](https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/).

Vector databases are designed to store and query unstructured data—inputs that lack a fixed schema, such as text, images, and audio. This is a clear departure from traditional SQL databases, which usually query for rows where values match specific criteria, as with the “SELECT” statement.

> “Vector databases are designed to store and query unstructured data—inputs that lack a fixed schema, such as text, images, and audio.”

This tutorial is meant to help you connect an LLM with LangChain to your own data sources (in this case, a PDF document) while using ChromaDB as a vector database to serve as memory. This is where RAG enters the picture, introducing the ability to store and retrieve data during the conversation, as well as adding chat history that gives you the power to build complex apps with memory.

Here’s what the pipeline of the entire product will look like:

![Diagram of the workflow involved with connecting a PDF document to an LLM with LangChain, while using ChromaDB as a vector database.](https://cdn.thenewstack.io/media/2026/04/77eac6f8-3.png)

## Project workflow with steps

Now, you have a basic introduction of the type of app we’re building. This section will cover the implementation steps required to: load the data into LangChain documents; split it into chunks; rank the vectors by similarity to the question’s embedding; and, finally, ask where you insert the question to get the most relevant chunks into a message to a GPT model while returning the GPT’s answer.

Let’s dive in.

### Step 1: Install dependencies

In your Notebook, run these [Python packages](https://thenewstack.io/the-top-5-python-packages-and-what-they-do "Python packages"):

```

pip install pypdf docx2txt openai langchain chromadb langchain-community langchain-openai "langchain-chroma&gt;=0.1.2"

```

* `pypdf:` responsible for splitting and transforming PDF files
* `docx2txt:` extracts text from your docx file
* `openai:` gives access to the model
* `langchain:` acts as a wrapper to the LLM
* `chromadb:` open-source vector database for storing and querying embeddings
* `langchain-community:` loads data into the standard LangChain document format
* `langchain-openai:` packages connecting OpenAI and LangChain
* `"langchain-chroma>=0.1.2":` to access the Chroma vector store

These tools all work together to create the LLM-powered Q&A application.

### Step 2: Load your secret

```

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

```

Consistent with every Python project, you should load your environment variables in a .env file that won’t commit to source control when you decide to share it on GitHub.

### Step 3: Loading the documents

Here, we would use LangChain documents to load the PDF file using the function `load_document`. This will convert the file into an array of documents with the library, `pypdf`, where each document contains the page content and metadata associated with a page number using the `loader.load()` function.

```

def load_document(file): 
    import os
    name, extension = os.path.splitext(file)

    if extension == '.pdf':
        from langchain_community.document_loaders import PyPDFLoader
        print(f'Loading {file}')
        loader = PyPDFLoader(file)
    elif extension == '.docx':
        from langchain_community.document_loaders import Docx2txtLoader
        print(f'Loading {file}')
        loader = Docx2txtLoader(file)
    elif extension == '.txt':
        from langchain_community.document_loaders import TextLoader
        loader = TextLoader(file)
    else:
        print('Document format is not supported!')
        return None

    data = loader.load()
    return data

```

### Step 4: Chunking data

```

def chunk_data(data, chunk_size=256):

    from langchain.text_splitter import RecursiveCharacterTextSplitter
    
    overlap = int(chunk_size * 0.15)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)

    chunks = text_splitter.split_documents(data)

    return chunks

```

The `chunk_data` function will handle splitting the documents into text chunks of a specified size using LangChain’s `RecursiveCharacterTextSplitter`. With this approach, you can access the specified text of the page content with an index.

### Step 5: Query and response

```

def ask_and_get_answer(vector_store, q, k=3):
    from langchain_openai import ChatOpenAI
    from langchain.chains import create_retrieval_chain
    from langchain.chains.combine_documents import create_stuff_documents_chain
    from langchain_core.prompts import ChatPromptTemplate

    llm = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.0)

    retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k': k})

    # Define a prompt template for better control
    prompt = ChatPromptTemplate.from_template("""
    Answer the following question based only on the provided context:
    &lt;context&gt;
    {context}
    &lt;/context&gt;
    Question: {input}""")

    document_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    response = retrieval_chain.invoke({"input": q})
    return response

```

Since we need the answers in natural language, LLMs come in handy. This particular function uses the GPT-3.5-turbo model to generate an answer and queries the vector store for the document.

### Step 6: Using Chroma as a vector database

```

def create_embeddings_chroma(chunks, persist_directory='./chroma_db'):
    from langchain_chroma import Chroma
    from langchain_openai import OpenAIEmbeddings

    embeddings = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=1536)  

    vector_store = Chroma.from_documents(chunks, embeddings, persist_directory=persist_directory) 

    return vector_store

```

This code instantiates an embedding model from OpenAI. In the process, it creates a vector store using the provided text chunks and embedding model, as well as configuring it to save the data to a specified directory `chroma_db`.

```

def load_embeddings_chroma(persist_directory='./chroma_db'):
    from langchain_chroma import Chroma
    from langchain_openai import OpenAIEmbeddings

    embeddings = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=1536) 
    
    vector_store = Chroma(persist_directory=persist_directory, embedding_function=embeddings) 

    return vector_store

```

Here, we define a function that passes the persist directory as an argument, which loads the existing embeddings from disk to a vector store object. Next, instantiate the same embedding model used during creation. The returned loaded vector store will load a Chroma vector store from the specified directory using the provided embedding function.

### Step 7: Running the code

After writing lots of code, it is time to test and run the code.

First, load the PDF document into LangChain as files represent the directory for the file:

```

data = load_document('files/rag_powered_by_google_search.pdf') # use any file you have

chunks = chunk_data(data, chunk_size=256)

vector_store = create_embeddings_chroma(chunks)

```

Next, you should observe that running this code leads to this message, “Loading files/rag\_powered\_by\_google\_search.pdf”—indicating a successful load.

```

db = load_embeddings_chroma() 

q = 'How many pairs of questions and answers had the StackOverflow dataset?'

answer = ask_and_get_answer(vector_store, q)
print(answer)

```

Here, we [retrieve the answer from the vector](https://thenewstack.io/writer-coms-graph-based-rag-alternative-to-vector-retrieval/) store as an object.

![Image of the output retrieved from the vector store.](https://cdn.thenewstack.io/media/2026/04/e6a4303a-4-1024x614.png)

If you ask a follow-up question, it will be clear that you won’t receive an accurate answer from the vector store. This is due to the absence of chat history (memory).

```

q = 'Multiply that number by 2.'
answer = ask_and_get_answer(vector_store, q)

print(answer['answer'])

```

The result of this response should look something like: “Since no specific number is provided in the context, it is not possible to multiply it by 2.”

### Step 8: Adding chat history memory to your RAG application

```

from langchain_openai import ChatOpenAI
from langchain.chains import (
    create_history_aware_retriever,
    create_retrieval_chain,
)
from langchain.chains.combine_documents import (
    create_stuff_documents_chain,
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

llm = ChatOpenAI(
    model_name='gpt-3.5-turbo',
    temperature=0.0
)

retriever = vector_store.as_retriever(
    search_type='similarity',
    search_kwargs={'k': 5}
)

contextualize_q_system_prompt = (
    "Given a chat history and the latest user question "
    "which might reference context in the chat history, "
    "formulate a standalone question which can be understood "
    "without the chat history. Do NOT answer the question, just "
    "reformulate it if needed and otherwise return it as is."
)

contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", contextualize_q_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

history_aware_retriever = create_history_aware_retriever(
    llm, retriever, contextualize_q_prompt
)

qa_system_prompt = (
    "You are an assistant for question-answering tasks. Use "
    "the following pieces of retrieved context to answer the "
    "question. If you don't know the answer, just say that you "
    "don't know. Use three sentences maximum and keep the answer "
    "concise."
    "\n\n"
    "{context}"
)

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", qa_system_prompt),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])

question_answer_chain = create_stuff_documents_chain(
    llm, qa_prompt
)

rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

```

For a RAG application, a basic requirement is support for follow-up questions—including those that reference past chat history.

The code here depicts a way to build conversational AI chains that act as an implementation to store the conversation memory and track the conversation using the `ConversationBufferMemory` class during interaction.

### Step 9: Create a function to ask questions

```

from langchain_core.messages import HumanMessage, AIMessage

chat_history = []

query = "How many pairs of questions and answers had the StackOverflow dataset?"

def ask_question(query, chain):
    response = rag_chain.invoke({
        "input": query,
        "chat_history": chat_history
    })
    return response

result = ask_question(query, rag_chain)
print(result['answer'])

# Update memory manually
chat_history.append(HumanMessage(content=query))
chat_history.append(AIMessage(content=result["answer"]))

```

The function accepts the parameters as a “query” and “rag\_chain” variable in step 8 to display the result.

![Image of the result to the query from step 8.](https://cdn.thenewstack.io/media/2026/04/e6800f28-5-1024x69.png)

Now, for a follow-up question, run this code in another cell block:

```

query = 'Multiply the answer by 4.'

result = ask_question(query, rag_chain)

print(result['answer'])

```

The response should give you a figure of “32 million,” and you can continue passing different prompts to get an answer from the result.

### Step 10: Interactive question loop in your RAG app

For a dynamic and interactive workflow, run this code:

```

while True:
    query = input('Your question: ')
    if query.lower() in ['exit', 'quit', 'bye']:
        print('Bye bye!')
        break
    result = ask_question(query, rag_chain)
    print(result['answer'])
    print('-' * 100)

```

![Result to some example questions from the code in step 10.](https://cdn.thenewstack.io/media/2026/04/ac3e3d61-6-1024x238.png)

## Welcome to AI’s RAG era

[Retrieval augmented generation](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/) is more than a flashy phrase for AI engineers. Its deeper usefulness stems from being a technique that leverages and combines an LLM with a method for searching for information.

> “Retrieval augmented generation is more than a flashy phrase… Its deeper usefulness stems from being a technique that leverages and combines an LLM with a method for searching for information.”

By following the steps above, devs and engineers can ensure that adopting this system will help people retrieve vital information from documents. This will also render answers more factual because it reads and learns from the data without compromising its integrity, avoiding the common issue of biased thoughts and reasoning.

Let’s embrace RAG as we continue to build with AI. Check out [this repository](https://github.com/Terieyenike/langchain-rag) for the complete workflow.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/6ad341ca-cropped-76c4e396-teri-eyenike.jpg)

Teri Eyenike is a software engineer and a member of the Andela talent network, a private global marketplace for digital talent. With more than five years of experience focused on creating usable web interfaces and other applications using modern technologies,...

Read more from Teri Eyenike](https://thenewstack.io/author/teri-eyenike/)