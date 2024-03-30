# Tutorial: Using LangChain and Gemini to Summarize Articles
![Featued image for: Tutorial: Using LangChain and Gemini to Summarize Articles](https://cdn.thenewstack.io/media/2024/03/878e4b6d-maarten-van-den-heuvel-8eznkvlqosk-unsplash-1024x683.jpg)
In this tutorial, we’ll look at how to combine
[LangChain](https://thenewstack.io/langchain-the-trendiest-web-framework-of-2023-thanks-to-ai/) — a programming framework for using large language models (LLMs) in applications — and Google’s [Gemini LLM](https://thenewstack.io/how-to-get-started-with-googles-gemini-large-language-model/) to summarize blog posts or articles on the internet.
Make sure you have an API key from Google AI Studio before continuing with the tutorial.
This application aims to summarize web-based articles, providing concise overviews of their content. This is particularly useful for quickly understanding the gist of long articles without reading through the entire text.
## Step 1: Initializing the Environment
Create a Python virtual environment and install the required modules from the
requirements.txt file.
|
1
2
|
python -m venv venv
source venv/bin/activate
Create the
requirements.txt file with the below content:
|
1
2
3
4
5
|
google.generativeai
langchain-google-genai
langchain
langchain_community
jupyter
|
1
|
pip install -r requirements.txt
Set an environment variable to access the API key implicitly from the code.
|
1
|
export GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
Launch the Jupyter Notebook and get started with the code.
## Step 2: Import Modules
Begin by importing the necessary Python modules. These imports include classes and functions from LangChain and Google Generative AI, which are essential for building our application. Ensure these libraries are installed in your Python environment before proceeding.
|
1
2
3
4
5
6
|
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.prompts import PromptTemplate
from langchain.chains import StuffDocumentsChain
from langchain.chains.llm import LLMChain
## Step 3: Load the Blog
Load content from a web-based article. The URL provided in the code snippet below is just an example; feel free to replace it with any article URL you wish to summarize. The content is fetched and stored for further processing.
|
1
2
|
loader = WebBaseLoader("https://thenewstack.io/the-building-blocks-of-llms-vectors-tokens-and-embeddings/")
docs = loader.load()
## Step 4: Define the Summarize Chain
In this critical step, we’ll define the summarization template and configure the LangChain model to generate summaries. The template instructs the model on how to structure its output, focusing on creating a concise summary of the input text.
|
1
2
3
4
|
template = "Write a concise summary of the following:\n\"{text}\"\nCONCISE SUMMARY:"
prompt = PromptTemplate.from_template(template)
llm_chain = LLMChain(llm=llm, prompt=prompt)
stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")
## Step 5: Invoke Chain
The final step is to invoke the chain, which triggers the summarization process on the loaded document. The output is the model’s attempt at summarizing the article, providing you with a condensed version of its content.
|
1
2
|
response=stuff_chain.invoke(docs)
print(response["output_text"])
## More About LangChain and LLMs
The
[question-and-answering (Q&A) use case](https://thenewstack.io/how-to-build-a-qa-llm-application-with-langchain-and-gemini/), as demonstrated in the previous tutorial, and the summarization use case, as outlined above, harness the power of LangChain and Gemini, but serve distinct purposes and employ different methodologies.
The Q&A application focuses on extracting specific answers from a given text (such as a PDF document), requiring the system to understand the context and retrieve accurate information in response to queries. This process involves loading and splitting the document into manageable chunks, converting these chunks into embeddings and using a retrieval mechanism to find the most relevant sections of text for answering the questions posed.
On the other hand, the summarization use case is designed to condense long web-based articles into concise summaries. This application emphasizes the ability to grasp the overall theme and key points of an article, requiring a summarization chain that instructs the model to produce a brief overview of the content. Unlike the Q&A use case, summarization involves loading web content directly, applying a summarization template and generating a condensed version of the article — highlighting its core message without needing to dive into the specifics.
Both applications showcase LangChain’s versatility in handling natural language processing tasks, but they each cater to different needs. One focuses on pinpointing specific information within a document, while the other aims to provide a quick, digestible summary of lengthy articles.
You can find the complete code for summarization below:
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)