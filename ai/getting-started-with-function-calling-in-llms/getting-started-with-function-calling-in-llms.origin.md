# Getting Started With Function Calling in LLMs
![Featued image for: Getting Started With Function Calling in LLMs](https://cdn.thenewstack.io/media/2024/08/3a32a684-phone-1024x576.jpg)
[Function calling](https://thenewstack.io/a-comprehensive-guide-to-function-calling-in-llms/) is a powerful capability in [large language models (LLMs)](https://thenewstack.io/llm/) like GPT-4, allowing these models to interact seamlessly with external tools and APIs. This functionality enables LLMs to convert natural language into actionable API calls, making them more versatile and useful in real-world applications. For instance, when a user asks, “What is the weather like in Lagos?” an LLM equipped with function calling can transform this query into a function call to a weather API in Lagos, Nigeria, retrieving the current weather data there.
This integration is essential for building advanced conversational agents or chatbots that require real-time data or need to perform specific actions. Function calling allows developers to define various functions that the LLM can call based on the context and requirements of the conversation. These functions act as tools within your LLM application, enabling tasks such as data extraction, knowledge retrieval and API integration.

With function calling, developers can enhance LLMs’ capabilities, making them conversational, interactive and responsive to user needs. This guide will walk you through the steps to implement function calling using [OpenAI APIs](https://thenewstack.io/beyond-chatgpt-exploring-the-openai-platform/), providing a simple, practical example to illustrate the process to enhance the capabilities of our language model (LLM) application. This step-by-step guide with code snippets will demonstrate how to define and call functions dynamically based on user input. We’ll use a movie database to fetch movie details.

**Prerequisites**
- Python is installed on your machine.
- OpenAI API key.
- dotenv library to manage environment variables.
**Setting Up the Environment**
First, let’s set up our environment and install the necessary libraries.

`pip install openai python-dotenv`
Next, create a
file in your project directory and add your OpenAI API key:**.env**

`OPENAI_API_KEY=your_openai_api_key`
**Initialize OpenAI API**
Load the API key from the
file and set it up in your script.**.env**

**Set OpenAI API Key**
`openai.api_key = os.getenv('OPENAI_API_KEY')`
**Define a Function to Get Movie Details**
We’ll create a function that fetches movie details from a dummy movie database.

**Define the Function of the API**
Now, we’ll define this function as a tool for the OpenAI API to use.

**Define a Helper Function to Get Completion**
This function will handle the API requests and process the responses.

**Example: Fetching Movie Details**
Let’s create a conversation where the user asks for movie details and the LLM calls our function to get the necessary information.

**Controlling Function Calling Behavior**
You can control whether the model should call a function automatically.

**Automatic Function Calling**
The model decides on its own whether to call a function.

`get_completion(messages, tools=tools, tool_choice="auto")`
**No Function Calling**
If you want to force the model to not use any of the functions provided, the code snippet below gives an example of how to implement this.

`get_completion(messages, tools=tools, tool_choice="none")`
**Forced Function Calling**
To force the model to call a specific function, you can implement:

`get_completion(messages, tools=tools, tool_choice={"type": "function", "function": {"name": "get_movie_details"}})`
**Handling Multiple Function Calls**
The OpenAI API supports calling multiple functions in one turn. For example, fetching details for multiple movies:

**Passing Function Results Back to the Model**
You might want to pass the result obtained from your API back to the model for further processing.

**Conclusion**
In this tutorial, we explored how to use function calling with OpenAI API to dynamically fetch and use data based on user input. By defining functions and controlling their invocation, you can create more interactive and capable applications. This method can be applied to various use cases, such as querying databases, calling external APIs or performing calculations.

Feel free to extend this example to suit your specific needs and experiment with different functions and behaviors. Happy coding!

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)