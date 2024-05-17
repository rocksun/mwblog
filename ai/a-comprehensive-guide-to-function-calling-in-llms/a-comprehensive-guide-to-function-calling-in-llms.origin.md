# A Comprehensive Guide to Function Calling in LLMs
![Featued image for: A Comprehensive Guide to Function Calling in LLMs](https://cdn.thenewstack.io/media/2024/05/0d3fe93b-allison-saeng-rv7vwjki4fg-unsplash-1024x768.jpg)
One of the proven techniques to reduce hallucinations in large language models is
[retrieval-augmented generation](https://thenewstack.io/retrieval-augmented-generation-for-llms/), or RAG. RAG uses a retriever that searches external data to augment a prompt with context before sending it to the generator, which is the LLM.
While RAG is the most popular approach, it is best suited for building context from unstructured data that has been indexed and stored in a
[vector database](https://thenewstack.io/vector-databases-long-term-memory-for-artificial-intelligence/). Before RAG can retrieve the context, a batch process converts the unstructured data into text embeddings and stores that in the vector database. This makes RAG ideal when dealing with data that doesn’t change often.
When applications require context from real-time data — such as stock quotes, order tracking, flight statuses or inventory management — they rely on the function-calling capability of LLMs. The goal of both RAG and function calling is to supplement the prompt with context — whether from existing data sources or real-time APIs — so that the LLM has access to accurate information.
LLMs with function-calling capabilities are foundational to the development of
[AI agents](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/) that perform specific tasks autonomously. For instance, these capabilities allow for the integration of LLMs with other APIs and systems, enabling the automation of complex workflows that involve data retrieval, processing and analysis.
## A Closer Look at Function Calling
Function calling, also known as tool use or API calling, is a technique that allows LLMs to interface with external systems, APIs and tools. By providing the LLM with a set of functions or tools, along with their descriptions and usage instructions, the model can intelligently select and invoke the appropriate functions to accomplish a given task.
This capability is a game-changer, as it enables LLMs to break free from their text-based limitations and interact with the real world. Instead of merely generating text, LLMs can now execute actions, control devices, retrieve information from databases, and perform a wide range of tasks by leveraging external tools and services.
Not every LLM is capable of utilizing function-calling capabilities. Those LLMs that are exclusively trained or fine-tuned possess the ability to determine whether the prompt demands function calling. The
[Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html) provides insight into how LLMs perform across various programming languages and API scenarios, showing the versatility and robustness of function-calling models in handling multiple, parallel and complex function executions. This versatility is crucial for developing AI agents that can operate across different software ecosystems and handle tasks that require simultaneous actions.
Applications typically invoke the LLM with function-calling capabilities twice: once to map the prompt into the target function name and its input arguments, and again to send the output of the invoked function to generate the final response.
The workflow below shows how the application, function and LLM exchange messages to complete the entire cycle.
**Step 1**: The user sends a prompt that may demand access to the function — for example, “What’s the current weather in New Delhi?” **Step 2**: The application sends the prompt along with all the available functions. In our example, this may be the prompt along with the input schema of the function
get_current_weather(city). The LLM determines whether the prompt requires function calling. If yes, it looks up the provided list of functions — and their respective schemas — and responds with a JSON dictionary populated with the set of functions and their input arguments.
**Step 3**: The application parses the LLM response. If it contains the functions, it will invoke them either sequentially or in parallel. **Step 4**: The output from each function is then included in the final prompt and sent to the LLM. Since the model now has access to the data, it responds with an answer based on the factual data provided by the functions.
## Integrating RAG and Function Calling
The integration of RAG with function calling can significantly enhance the capabilities of LLM-based applications. RAG agents based on function calling utilize the strengths of both approaches — leveraging external knowledge bases for accurate data retrieval while executing specific functions for efficient task completion.
Using function calling within a RAG framework enables more structured retrieval processes. For instance, a function can be predefined to extract specific information based on user queries, which the RAG system retrieves from a comprehensive knowledge base. This method ensures that the responses are not only relevant but also precisely tailored to the needs of the application.
For example, in a customer support scenario, the system could retrieve product specifications from a database and then use a function call to format this information for user queries, ensuring consistent and accurate responses.
Moreover, the RAG agents can handle complex queries by dynamically interacting with external databases and APIs through predefined functions, thereby streamlining application workflows and reducing the need for manual intervention. This approach is particularly beneficial in environments where quick decision-making is crucial — such as in financial services or medical diagnostics, where the system can pull the latest research or market data and immediately apply functions to analyze this information.
## Choosing LLMs With Function Calling Support
It’s important to choose the right LLM that supports function calling to build
[agentic workflows](https://www.quixl.ai/blog/the-integration-of-ai-agents-in-enterprise-systems-a-guide-to-agentic-workflows/) and RAG agents. Below is a list of commercial and open LLMs that are ideal for function calling.
**OpenAI GPT-4 and GPT-3.5 Turbo**
OpenAI’s
[GPT-4](http://GPT-4) and [GPT-3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5-turbo) models are the most well-known commercial LLMs that support function calling. This allows developers to define custom functions that the LLM can call during inference, to retrieve external data or perform computations. The LLM outputs a JSON object containing the function name and arguments. The developer’s code can then execute this and return the function output to the LLM.
**Google Gemini**
Google’s
[Gemini](https://deepmind.google/technologies/gemini/#introduction) LLM also supports function calling through the [Vertex AI](https://thenewstack.io/an-introduction-to-google-vertex-ai-automl-training-and-inference/) and Google AI Studio. Developers can define functions and descriptions, which the Gemini model can invoke during inference by returning structured JSON data.
**Anthropic Claude**
Anthropic’s
[Claude 3](https://www.anthropic.com/claude) family of LLMs has an API that enables function-calling capabilities similar to OpenAI’s models.
**Cohere Command**
Cohere’s
[Command R](https://cohere.com/command) and [Command R+](https://cohere.com/command) LLMs also provide an API for function calling, allowing integration with external tools and data sources.
**Mistral**
The open source
[Mistral 7B](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) LLM has demonstrated function-calling capabilities, allowing developers to define custom functions that the model can invoke during inference.
**NexusRaven** [NexusRaven](https://huggingface.co/Nexusflow/NexusRaven-V2-13B) is an open source 13B LLM that has been specifically designed for advanced function calling, surpassing even GPT-4 in some benchmarks for invoking cybersecurity tools and APIs.
**Gorilla OpenFunctions**
The
[Gorilla OpenFunctions](https://huggingface.co/gorilla-llm/gorilla-openfunctions-v2) model is a 7B LLM that is fine-tuned on API documentation. It can generate accurate function calls and API requests from natural language prompts.
**Fireworks FireFunction** [FireFunction V1](https://huggingface.co/fireworks-ai/firefunction-v1) is an open source function calling model based on the [Mixtral 8x7B model](https://mistral.ai/news/mixtral-of-experts/). It achieves near GPT-4 level quality for real-world use cases of structured information generation and routing decision-making.
**Nous Hermes 2 Pro** [Hermes 2 Pro](https://huggingface.co/NousResearch/Hermes-2-Pro-Mistral-7B) is a 7B parameter model that excels at function calling, JSON-structured outputs and general tasks. It achieves 90% accuracy on function-calling evaluation and 81% on structured JSON output evaluation built with Fireworks.ai. Hermes 2 Pro is fine-tuned on both the Mistral 7B and Llama 3 8B models, offering developers a choice.
In upcoming articles on function calling, I will explore how to implement this capability with both commercial and open LLMs, in order to build a chatbot that has access to real-time data.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)