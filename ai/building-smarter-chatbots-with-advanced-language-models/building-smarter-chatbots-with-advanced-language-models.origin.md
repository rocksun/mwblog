# Building Smarter Chatbots With Advanced Language Models
![Featued image for: Building Smarter Chatbots With Advanced Language Models](https://cdn.thenewstack.io/media/2024/05/0673cbee-ai-chatbots-featured-image-1024x768.png)
The development of chatbots is evolving rapidly, with new tools and frameworks making it easier and more efficient to build sophisticated systems. But current
[large language models (LLMs)](https://thenewstack.io/llm/) suffer from limitations: They lack current knowledge and can’t access domain-specific information, such as the contents of a company’s knowledge base. [Retrieval-augmented generation (RAG)](https://thenewstack.io/retrieval-augmented-generation-for-llms/) can solve this problem by finding knowledge beyond the LLM’s training data, and then passing that information to an LLM.
In this technical article, I’ll explain how to leverage LangChain Community, Mixtral 8-7B and ChromaDB to create an advanced chatbot capable of processing diverse file types for retrieving information from a vector database, searching via semantic search and interacting with users through an intuitive interface.
## Evolving Chatbot Technologies
The tools and processes for chatbot development are evolving very quickly. They are expanding chatbots’ capabilities and changing how they interact with users and process information. I’ve identified five that I believe are particularly important, and I’ll be using them in this tutorial.
**Transitioning to LangChain Community and Mixtral 8-7B:**The shift from LangChain and Mistral to their more advanced counterparts, LangChain Community and Mixtral 8-7B, marks a significant evolution in chatbot development. These tools extend the application range of chatbots, enabling document processing and enhancing natural language understanding across various domains. **Transitioning from graph databases to ChromaDB:**ChromaDB supports storing and querying large-scale, high-dimensional data. This makes ChromaDB a superior choice for managing complex data types and structures in diverse applications. **Using conversational retrieval chain:**While RAG enhances chatbot responses by enabling access to external data beyond the LLM’s training dataset, the conversational retrieval chain builds on this by dynamically retrieving information from vector databases during the conversation. This shift retains the benefits of RAG while also improving chatbot interactivity and relevance by integrating real-time, context-specific data retrieval via advanced language models. **Advanced file handling and processing:**The new scenario expands the types of files handled, including PDF, M4A, CSV, Excel and EML, and introduces advanced processing techniques. This involves using ChromaDB for storing and querying extracted information and integrating voice recognition for audio files, expanding the chatbot’s ability to handle various data sources. **Deployment with the Gradio interface:**Gradio provides an interactive and user-friendly interface for testing and deploying AI models, including chatbots. This makes it easier for users to interact with the system in real time.
I’ll put these tools into action in this tutorial. But first, a note on RAG for the uninitiated.
## Understanding RAG
RAG plays a pivotal role in enhancing the functionality of LLMs. RAGs facilitate LLMs’ access to external data, enabling them to generate responses with added context. The result is an app that gives end users a superior, next-gen LLM experience. Your LLM is simply more helpful and effective with RAG.
RAG operates through a sequence of four key steps:
**Loading encoded documents:**The process begins by loading a vector database with documents that have been encoded into machine-readable format. **Query encoding:**The user’s query is transformed into a vector using a sentence transformer. This vectorized format of the query makes it compatible with the encoded documents in the database. **Context retrieval:**The encoded query is used to retrieve relevant context from the vector database. This context contains the information needed to generate a response that appropriately addresses the user’s query. **Prompting the LLM:**The retrieved context and the query are used to prompt the LLM. The LLM generates a contextually appropriate and information-rich response.
## Demonstrating the Impact of RAG
To illustrate the effectiveness of RAG in enhancing the chatbot’s capabilities, I prepared screenshots comparing the answers provided by the model with and without the use of RAG:
### Without RAG
The model lacks the ability to access up-to-date pricing information since it was not part of the training dataset. This limitation results in responses that do not reflect current company data.
### With RAG
After saving the
[pricing page](https://gcore.com/pricing/cloud) as a PDF file and using it as extra content for RAG, the model effectively parsed and utilized the file, accurately answering questions regarding up-to-date pricing. This demonstrates RAG’s capability to enhance the chatbot’s performance by integrating dynamic, external information.
## System Requirements and Performance
To ensure optimal performance of our chatbot system, I tested the setup on a virtual machine equipped with 4x GeForce GTX 1080 Ti GPUs. The average utilization of these resources is crucial for sustaining the demanding processes of the chatbot.
By implementing the command
export CUDA_VISIBLE_DEVICES=0, I restricted the system to utilize only one GPU. This adjustment significantly changed GPU resource utilization, with the model taking about 6GB of GPU memory to process the requests efficiently.
## How to Run the Code
This setup process gives you all the necessary tools and dependencies correctly configured to run and interact with the chatbot efficiently. The code you’ll need is available in GitHub, so I’ve avoided writing it in full here. I ran the model using Ubuntu 22.04, but it’ll work on any up-to-date
[Linux operating system](https://thenewstack.io/linux/).
### Create a Virtual Environment
Initialize a new
[Python](https://roadmap.sh/python) virtual environment to manage dependencies:
### Activate the Virtual Environment
Activate the created environment to use it for the following steps:
### Clone the Repository
Download the project code from our GitHub repository:
### Install Dependencies:
Install all required libraries from the provided requirements file:
### Run the Inference Script:
Launch the chatbot application using Python:
### Access the Chatbot
#### Local Machine
If you are running the chatbot on your local machine, open a web browser and navigate to the local server URL:
|
1
|
http://127.0.0.1:5050
You’ll see this screen appear:
#### Remote Machine
If you are running the chatbot on a remote machine, such as in the cloud, you will need to use port-forwarding techniques. To make the bot accessible on all network interfaces, modify the server configuration in your code by changing
127.0.0.1 to
0.0.0.0:
Note: Exposing the bot on a public interface can pose security risks, so ensure you have proper
[security measures](https://thenewstack.io/how-a-popular-combo-provides-ddos-protection/) in place.
## Conclusion
The development process that I’ve shared here opens the door to creating more knowledgeable, responsive and helpful chatbots that can transcend traditional limitations by accessing updated information and providing answers informed by a comprehensive understanding of uploaded documents. This journey into chatbot development underscores the importance of integrating new technologies and the need for regularly updated development strategies that adapt to and incorporate new advancements for the creation of more intelligent, efficient and user-friendly chatbot applications.
As technology continues to advance, the potential for chatbots as tools for information retrieval, customer engagement and personalized assistance is bound only by the creativity and innovation of developers.
*At Gcore, we pave the way for the future of AI, supporting the AI development lifecycle: training, inference and applications. We use cutting-edge NVIDIA GPUs for outstanding performance across our 180+ point-of-presence global network. Our mission is to connect the world to AI, anywhere, anytime.* [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)