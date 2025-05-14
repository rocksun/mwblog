# A Practical Guide To Building a RAG-Powered Chatbot
![Featued image for: A Practical Guide To Building a RAG-Powered Chatbot](https://cdn.thenewstack.io/media/2025/05/6a69f156-chat-7767694_1280-1024x724.jpg)
“Can you build us a chatbot?” If your IT team hasn’t received the request yet, trust me, it’s on the way. With the rise of LLMs, chatbots are the new must-have feature — whether you’re shipping SaaS, managing internal tools, or just trying to make sense of sprawling documentation. The problem? Duct-taping a search index to an LLM isn’t enough.

If your chatbot needs to surface answers from documentation, logs, or other internal knowledge sources, you’re not just building a chatbot — you’re building a retrieval pipeline. And if you’re not thinking about where your data lives, how it’s retrieved, and how much it costs to move around, you’re setting yourself up for a bloated, brittle system.

Today, I’m breaking down how to build a real conversational chatbot — one that leverages Retrieval-Augmented Generation (RAG), minimizes latency, and avoids the cloud egress fee trap that silently kills your margins. LLMs are the easy part. Infrastructure is where the real work — and cost — lives.

I’ll present a simple, conversational AI chatbot web app with a ChatGPT-style UI that you can easily configure to work with OpenAI, DeepSeek, or any of a range of other large language models (LLMs).

## First: RAG Basics
Retrieval-Augmented Generation, or RAG for short, is a technique that applies the generative features of an LLM to a collection of documents, r[esulting in a chatbot that can effectively answer questions](https://thenewstack.io/build-a-python-chatgpt-3-5-chatbot-in-10-minutes) based on the content of those documents.

A typical RAG implementation splits each document in the collection into several roughly equal-sized, overlapping chunks and generates an [embedding](https://stackoverflow.blog/2023/11/09/an-intuitive-introduction-to-text-embeddings/) for each chunk. Embeddings are vectors (lists) of floating-point numbers with hundreds or thousands of dimensions. The distance between two vectors indicates their similarity. Small distances indicate high similarity, and large distances indicate low similarity.

The RAG app then loads each chunk, along with its embedding, into a vector store. The vector store is a special-purpose database that can perform a similarity search — given a piece of text, the vector store can retrieve chunks ranked by their similarity to the query text by comparing the embeddings.

Let’s put the pieces together:

Given a question from the user (1), the RAG app can query the vector store for chunks of text that are similar to the question (2). Those chunks form the context that helps the LLM answer the user’s question. Here’s what that looks like using the documentation collection as an example: given the question, “Tell me about object lock”, the vector store returns four document chunks, each of about 170 words, to the app (3). Here is a link to the text of, and a short extract from, each chunk:

[Object Lock](https://www.backblaze.com/docs/en/cloud-storage-object-lock#:~:text=before%20the%20set,on%20the%20file.): With Object Lock Legal Hold, files are prevented from being changed or deleted; however, immutability does not have a defined retention period.[Object Lock](https://www.backblaze.com/docs/en/cloud-storage-object-lock#:~:text=From%20a%20functionality,than%20I%20wanted%3F): You can enable Object Lock on a bucket when you create a new bucket or on an existing bucket.[Object Lock](https://www.backblaze.com/docs/en/cloud-storage-object-lock#:~:text=Backblaze%20B2%20SDKs,check%20the%20retention): Object Lock was designed with the Immutability feature in Veeam Backup & Replication in mind.[Enable Object Lock with the S3-Compatible API](https://www.backblaze.com/docs/en/cloud-storage-enable-object-lock-with-the-s3-compatible-api#:~:text=Powered%20by-,Enable%20Object%20Lock%20with%20the%20S3%2DCompatible%20API,Backblaze%20API%20operations%20and%20their%20corresponding%20documentation%2C%20see%20API%20Documentation.,-Was%20this%20article): To enable Object Lock on an existing S3-compatible bucket, add the x-amz-bucket-object-lock-token header with a value of 1 to the S3 Put Object Lock Configuration API call.
Unsurprisingly, three of the four results are extracts from the main documentation article on object lock.

In order to provide a conversational experience, the RAG app maintains a chat history in a message store. The RAG app retrieves the message history (4) to form part of the query it will send to the LLM. Steps 2 and 4, retrieving data from the vector and message stores, can be performed concurrently, since neither depends on the other.

A system prompt sets the guidelines for the LLM to generate responses. In a RAG, the system prompt typically specifies that the response should be based on retrieved document data rather than model memorization and attempts to prevent hallucinations by ensuring that the model does not fabricate information if no relevant documents are found. Here is the system prompt from the RAG app:


1 Use the following pieces of context and the message history to answer the question at the end. If you don't know the answer, just say that you don't know; don't try to make up an answer.

The RAG submits the system prompt, the context, the last few messages in the conversation, and the user’s question to the LLM (5), which generates a, hopefully, helpful response (6). Here’s the answer it provided to the above question:

Object Lock is a feature that allows users to enforce immutability on files stored in cloud storage. Here are the key points about Object Lock:

**Immutability:**Once a file is locked, it cannot be modified or deleted until a specified retention period expires or a legal hold is lifted.**Retention Periods:**Users can set a retention period when locking a file. During this time, the file remains immutable, meaning it cannot be changed or deleted.**Legal Hold:**Users can place files under a legal hold, which prevents modifications or deletions indefinitely until the hold is removed.**Enabling Object Lock:**Object Lock can be enabled for new buckets or existing ones, but it must be turned on at the bucket level before files are uploaded.**Integrations:**Some applications, such as Veeam Backup and Replication, offer built-in support for Object Lock, making the process easier for users who want to ensure file immutability during backups.**No Extra Cost:**There is no additional fee for using Object Lock; however, standard storage charges still apply for the locked files.**Mistakes in Locking:**If a user locks a file for longer than intended, they may need to contact support to resolve the situation, which could involve closing their storage account in some cases.
Overall, Object Lock is a crucial feature for organizations that need to ensure data integrity and compliance with regulations concerning data retention.

The RAG app adds the user’s question and the LLM’s response to the message store (7), returns the answer to the user (8), and awaits the next question.

## A Quick Tour of the Sample App
The sample app is [published on GitHub](https://github.com/backblaze-b2-samples/ai-rag-examples). The app is open source, under the MIT license, so you can use it as a basis for your experimentation without any restrictions. The app uses an S3-compatible API, so it works well with any S3-compatible object store.

Note that, as with any sample application that integrates with one or more cloud service providers (CSPs), you may incur charges when running the sample app, both for storing and for downloading data from the CSP. Download fees are commonly known as “egress charges” and can quickly exceed charges for storing your data. AI applications often integrate functionality from several specialist providers, so you should carefully check your cloud storage provider’s pricing to avoid a surprise bill at the end of the month. Shop around — several specialized cloud storage providers provide a generous monthly egress allowance free of charge, up to three times the amount of data you are storing, plus, in one case, unlimited free egress to that storage provider’s partners.

The README file covers configuration and deployment in detail; in this blog post, I’ll provide a high-level overview. The sample app is written in Python using the [Django web framework](https://www.djangoproject.com/). API credentials and related settings are configured via environment variables, while the LLM and vector store are configured via Django’s settings.py file:

123456789101112131415161718192021222324 |
CHAT_MODEL: ModelSpec = { 'name': 'OpenAI', 'llm': { 'cls': ChatOpenAI, 'init_args': { 'model': "gpt-4o-mini", } },}# Change source_data_location and vector_store_location to match your environment# search_k is the number of results to return when searching the vector storeDOCUMENT_COLLECTION: CollectionSpec = { 'name': 'Docs', 'source_data_location': 's3://rag-app-bucket/pdfs', 'vector_store_location': 's3://rag-app-bucket/vectordb/docs/openai', 'search_k': 4, 'embeddings': { 'cls': OpenAIEmbeddings, 'init_args': { 'model': "text-embedding-3-large", }, },} |
The sample app is configured to use OpenAI GPT-4o mini. Still, the README explains how to use different online LLMs, such as DeepSeek V3 or Google Gemini 2.0 Flash, or even a local LLM like Meta Llama 3.1, via the [Ollama](https://ollama.com/) framework. If you do run a local LLM, be sure to pick a model that fits your hardware. I tried running Meta’s Llama 3.3, which has 70 billion parameters (70B), on my MacBook Pro with the M1 Pro CPU. It took nearly 3 hours to answer a single question! Llama 3.1 8B was a much better fit, answering questions in less than 30 seconds.
Notice that the document collection is configured with the location of a vector store containing a library of technical documentation as a sample dataset. The README file contains an application key with read-only access to the PDFs and vector store so you can try the application without having to load your own set of documents.

If you want to use your document collection, a pair of custom commands allows you to load them from a cloud object store into the vector store and then query the vector store to test that it all worked.

First, you need to load your data:

123456789101112131415161718192021 |
% python manage.py load_vector_storeDeleting existing LanceDB vector store at s3://rag-app-bucket/vectordb/docsCreating LanceDB vector store at s3://rag-app-bucket/vectordb/docsLoading data from s3://rag-app-bucket/pdfs in pages of 1000 resultsSuccessfully retrieved page 1 containing 618 result(s) from s3://rag-app-bucket/pdfsSkipping pdfs/.bzEmptySkipping pdfs/cloud_storage/.bzEmptyLoading pdfs/cloud_storage/cloud-storage-add-file-information-with-the-native-api.pdfLoading pdfs/cloud_storage/cloud-storage-additional-resources.pdfLoading pdfs/cloud_storage/cloud-storage-api-operations.pdf...Loading pdfs/v1_api/s3-put-object.pdfLoading pdfs/v1_api/s3-upload-part-copy.pdfLoading pdfs/v1_api/s3-upload-part.pdfLoaded batch of 614 document(s) from pageSplit batch into 2758 chunks[2025-02-28T01:26:11Z WARN lance_table::io::commit] Using unsafe commit handler. Concurrent writes may result in data loss. Consider providing a commit handler that prevents conflicting writes.Added chunks to vector storeAdded 614 document(s) containing 2758 chunks to vector store; skipped 4 result(s).Created LanceDB vector store at s3://rag-app-bucket/vectordb/docs. "vectorstore" table contains 2758 rows |
Don’t be alarmed by the “unsafe commit handler” warning — our sample vector store will never receive concurrent writes, so there will be no conflict or data loss.
Now you can verify that the data is stored by querying the vector store. Notice how the raw results from the vector store include an S3 URI identifying the source document:

123456789 |
% python manage.py search_vector_store 'Which S3 API operation would I use to upload a file?'2025-04-07 16:24:51,615 ai_rag_app.management.commands.search_vector_store INFO Opening vector store at s3://blze-ev-ai-rag-app/vectordb/docs/openai2025-04-07 16:24:51,615 ai_rag_app.utils.vectorstore DEBUG Populating AWS environment variables from the b2-ev profileFound 4 docs in 5.25 seconds2025-04-07 16:24:57,386 ai_rag_app.management.commands.search_vector_store INFO page_content='b2_list_parts b2_list_unfinished_large_files b2_start_large_file b2_update_file_legal_hold b2_update_bucket b2_upload_file b2_update_file_retention b2_upload_part S3-Compatible API To go directly to the detailed S3-Compatible API operations, click here. To learn more about using the S3-Compatible API, click here. API Operations Object Operations S3 Copy Object S3 Delete Object S3 Get Object S3 Get Object ACL S3 Get Object Legal Hold S3 Get Object Retention S3 Head Object S3 Put Object S3 Put Object ACL S3 Put Object Legal Hold S3 Put Object Retention S3 Abort Multipart Upload S3 Complete Multipart Upload S3 Create Multipart Upload S3 Upload Part S3 Upload Part Copy S3 List Multipart Uploads Bucket Operations S3 Create Bucket S3 Delete Bucket S3 Delete Bucket CORS S3 Delete Bucket Encryption S3 Delete Objects S3 Get Bucket ACL S3 Get Bucket CORS S3 Get Bucket Encryption S3 Get Bucket Location S3 Get Bucket Versioning' metadata={'source': 's3://blze-ev-ai-rag-app/pdfs/cloud_storage/cloud-storage-api-operations.pdf'}... |
The core of the sample application is the RAG class. Several methods create the basic components of the RAG, but here we’ll look at how the _create_chain() method uses the open source [LangChain AI framework](https://python.langchain.com/v0.2/docs/introduction/) to bring together the system prompt, vector store, message history, and LLM.
First, we define the system prompt, which includes a placeholder for the context–those chunks of text that the RAG will retrieve from the vector store:

12345678 |
# These are the basic instructions for the LLMsystem_prompt = ( "Use the following pieces of context and the message history to " "Answer the question at the end. If you don't know the answer, " "just say that you don't know, don't try to make up an answer. " "\n\n" "Context: {context}") |
Then we create a prompt template that combines the system prompt, message history and the user’s question:
12345678 |
# The prompt template brings together the system prompt, context, message history and the user's questionprompt_template = ChatPromptTemplate( [ ("system", system_prompt), MessagesPlaceholder(variable_name="history", optional=True, n_messages=10), ("human", "{question}"), ]) |
Now we use [LangChain Expression Language](https://python.langchain.com/docs/concepts/lcel/) (LCEL) to form a chain from the various components. LCEL allows us to define a chain of components declaratively; that is, we provide a high-level representation of the chain we want, rather than specifying how the components should be linked together:
12345678910111213141516 |
# Create the basic chain# When loglevel is set to DEBUG, log_input will log the results from the vector storechain = ( { "context": ( itemgetter("question") | retriever | log_data('Documents from vector store', pretty=True) ), "question": itemgetter("question"), "history": itemgetter("history"), } | prompt_template | model | log_data('Output from model', pretty=True)) |
Notice the log_data() helper method — it simply logs its input data and hands it off to the next component in the chain.
Assigning a name to the chain allows us to add instrumentation when we invoke it. You’ll see later in the article how we add a callback handler that annotates the chain output with the amount of time taken to execute the chain:

12 |
# Give the chain a name so the handler can see itnamed_chain: Runnable[Input, Output] = chain.with_config(run_name="my_chain") |
Now, we use LangChain’s RunnableWithMessageHistory class to manage adding and retrieving messages from the message store. The Django framework assigns each user a session ID, and we use that as the key for storing and retrieving the message history:
1234567 |
# Add message history managementreturn RunnableWithMessageHistory( named_chain, lambda session_id: RAG._get_session_history(store, session_id), input_messages_key="question", history_messages_key="history",) |
Finally, the log_chain() function prints an ASCII representation of the chain to the debug log. Note that we have to provide the expected configuration, even though the session_id will not be used:
1 |
log_chain(history_chain, logging.DEBUG, {"configurable": {'session_id': 'dummy'}}) |
This is the output — it provides a helpful visualization of how data flows through the chain:
The dumper components are inserted by the log_data() helper method to log data as it passes along the chain. In contrast, the Lambda components are inserted by the itemgetter() method to extract elements from the incoming Python dictionary.

The RAG class’ invoke() function, called in response to a user’s question, is very simple. Here is the key section of code:

1234567891011 |
response = self._chain.invoke( {"question": question}, config={ "configurable": { "session_id": session_key }, "callbacks": [ ChainElapsedTime("my_chain") ] },) |
The input to the chain is a Python dictionary containing the question, while the config argument configures the chain with the Django session key and a callback that annotates the chain output with its execution time. Since the chain output contains [Markdown](https://www.markdownguide.org/getting-started/) formatting, the API endpoint that handles requests from the front end uses the open source [markdown-it library](https://github.com/markdown-it/markdown-it) to render the output to HTML for display.
The remainder of the code is mainly concerned with rendering the web UI. One interesting facet is that the Django view, responsible for rendering the UI as the page loads, uses the RAG’s message store to render the conversation, so if you reload the page, you don’t lose your context.

## Take This Code and Run It!
As mentioned above, the [sample AI RAG application](https://github.com/backblaze-b2-samples/ai-rag-examples) is open source, under the MIT license, and I encourage you to use it as the basis for your own RAG exploration. The README file suggests a few ways you could extend it, and I also draw your attention to the conclusion of the README if you are thinking of running the app in production:

[…] in order to get you started quickly, we streamlined the application in several ways. There are a few areas to attend to if you wish to run this app in a production setting:

- The app does not use a database for user accounts or any other data, so it does not require authentication. All access is anonymous. If you want users to log in, you need to restore Django’s
[AuthenticationMiddleware](https://docs.djangoproject.com/en/5.1/ref/middleware/#module-django.contrib.auth.middleware)class to the MIDDLEWARE configuration and[configure a database](https://docs.djangoproject.com/en/5.1/ref/databases/). - Sessions are stored in memory. As explained above,
[you can use Gunicorn to scale the application to multiple threads](https://github.com/backblaze-b2-samples/ai-rag-examples), but you would need to[configure a Django session backend](https://docs.djangoproject.com/en/5.1/topics/http/sessions/)to run the app in multiple processes or on multiple hosts. - Similarly, conversation history is stored in memory, so you would need to use a persistent message history implementation, such as
[RedisChatMessageHistory](https://python.langchain.com/api_reference/redis/chat_message_history/langchain_redis.chat_message_history.RedisChatMessageHistory.html)to run the app in multiple processes or on multiple hosts.
Above all, have fun! AI is a rapidly evolving technology, with vendors and open source projects releasing new capabilities every day. I hope you find this app a valuable way to get started.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)