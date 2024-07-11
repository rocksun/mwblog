# Goodbye Manual Prompting, Hello Programming With DSPy
![Featued image for: Goodbye Manual Prompting, Hello Programming With DSPy](https://cdn.thenewstack.io/media/2024/07/582bf2b8-prompt-1024x576.jpg)
The development of scalable and optimized AI applications using [large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms) is still in its growing stages. Building applications based on LLMs is complex and time-consuming due to the extensive manual work involved, such as writing prompts.

Prompt writing is the most important part of any LLM application as it helps us to extract the best possible results from the model. However, [crafting an optimized prompt](https://roadmap.sh/prompt-engineering) requires developers to rely heavily on hit-and-trial methods, wasting significant time until the desired result is achieved.

The conventional method of manually crafting prompts is time-consuming and error-prone. Developers often spend significant time tweaking prompts to achieve the desired output, facing issues like:

**Fragility**: Prompts can break or perform inconsistently with slight changes.**Manual adjustments**: Extensive manual effort is required to refine prompts.**Inconsistent handling**: Different prompts for similar tasks lead to inconsistent results.
## What Is DSPy
[DSPy](https://github.com/stanfordnlp/dspy) (Declarative Self-improving Language Programs) is a framework designed by [Omer Khattab](https://omarkhattab.com/) and his team at [Stanford NLP Group](https://nlp.stanford.edu/). It aims to resolve the consistency and reliability issues of prompt writing by prioritizing programming over manual prompt writing. It provides a more declarative, systematic and programmatic approach to building data pipelines allowing developers to create high-level workflows without focusing on low-level details.
It lets you define what you want to achieve rather than how to achieve it. So, to accomplish that, DSPy has made advancements:

**Abstraction over prompts**: DSPy has introduced the concept of signatures. Signatures aim to replace manual prompt wording with a template-like structure. In this structure, we only need to define the inputs and outputs for any given task. This will make our pipelines more resilient and flexible to changes in the model or data.**Modular building blocks**: DSPy provides modules that encapsulate common prompting techniques (like[Chain of Thought](https://www.promptingguide.ai/techniques/cot.en#chain-of-thought-cot-prompting)or[ReAct](https://www.promptingguide.ai/techniques/react)). This eliminates the need for manually constructing complex prompts for these techniques.**Automated optimization**: DSPy supports built-in optimizers, also referred to as “teleprompters” that automatically select the best prompts for your specific task and model. This functionality eliminates the need for manual prompt tuning, making the process simpler and more efficient.**Compiler-driven adaptation**: The DSPy compiler optimizes the entire pipeline, adjusting prompts or fine-tuning models based on your data and validation logic, ensuring the pipeline remains effective even as components change.
## Building Blocks of a DSPy Program
Let’s explore the essential components that form the foundation of a DSPy program and understand how they interact to create powerful and efficient natural language processing (NLP) pipelines.

### Signatures
Signatures serve as the blueprint for defining what you want your LLM to do. Instead of writing the exact prompt, you describe the task in terms of its inputs and outputs.

For example, a signature for summarizing text might look like this: `text -> summary`
. This tells DSPy that you want to input some text and receive a concise summary as output. More complex tasks might involve multiple inputs, like a question-answering signature: `context, question -> answer`
. Signatures are flexible and can be customized with additional information, such as descriptions of the input and output fields.

### Modules: Building Blocks for LLM Behavior
Modules are pre-built components that encapsulate specific LLM behaviors or techniques. They are the building blocks you use to assemble your LLM application. For instance, the `ChainOfThought`
module encourages the LLM to think step by step, making it better at complex reasoning tasks. The `ReAct`
module allows your LLM to interact with external tools like calculators or databases. You can chain multiple modules together to create sophisticated pipelines.

Each module takes a signature and, using the `defined`
method like `ChainOfThought`
constructs the necessary prompt based on the defined inputs and outputs. This method ensures that the prompts are systematically generated, maintaining consistency and reducing the need for manual prompt writing.

In this way, the module takes the signature, applies its specific behavior or technique, and generates a prompt that aligns with the task’s requirements. This integration of signatures and modules allows for the building of complex and flexible LLM applications with minimal manual intervention.

### Teleprompters (Optimizers): The Prompt Whisperers
Teleprompters are like coaches for your LLM. They use advanced techniques to find the best prompts for your specific task and model. They do this by automatically trying out different variations of prompts and evaluating their performance based on a metric you define. For example, a teleprompter might use a metric like accuracy for question-answering tasks or [ROUGE score](https://aclanthology.org/W04-1013.pdf) for text summarization.

### DSPy Compiler: The Master Orchestrator
The DSPy compiler is the brains behind the operation. It takes your entire program — including your signatures, modules, training data and validation logic — and optimizes it for peak performance. The compiler’s ability to automatically handle changes in your application makes DSPy incredibly robust and adaptable.

The DSPy compiler takes the basic prompt, training examples and DSPy program to generate an optimized and best-performing prompt. This process involves simulating various versions of the program on the inputs and bootstrapping example traces of each module to optimize the pipeline for your task.

This automated optimization process eliminates the need for manual prompt tuning, making DSPy robust and adaptable to changes, ultimately delivering a highly effective and efficient NLP pipeline

## Practical Example: Build a RAG Model Using DSPy and MyScaleDB
Now that we have covered the basics of DSPy, let’s create a practical application. We will build a question-answering RAG pipeline and use MyScaleDB as a vector database.

### Loading Documents from Wikipedia
We start by loading documents related to “Albert Einstein” from Wikipedia. This is done using the `WikipediaLoader`
from the `langchain_community.document_loaders`
module.

### Transforming Documents to Plain Text
Next, we transform the loaded documents into plain text using the `Html2TextTransformer`
.

### Splitting Text into Chunks
The text is split into manageable chunks using the `CharacterTextSplitter`
. This helps in handling large documents and ensures the model processes them efficiently.

### Defining the Embeddings Model
We use the `transformers`
library to define an embedding model. We will use the `all-MiniLM-L6-v2`
model to transform the [text into vector embeddings](https://thenewstack.io/an-sql-vector-database-to-enhance-text-search-how-we-did-it/).

### Getting the Embeddings
We generate embeddings for the text chunks using the above embedding model.

### Connecting to the Vector Database
We will use [MyScaleDB](https://myscale.com/) as a vector database to develop this sample application. You can create a free account on MyScaleDB by visiting the MyScale [Sign Up page](https://console.myscale.com/passport/login?screenHint=signup). After that, you can follow the [Quickstart tutorial](https://myscale.com/docs/en/quickstart/) to start a new cluster and get the connection details.

Copy and paste the connection details into your Python notebook and run the code block. It will connect with your MyScaleDB cluster on the cloud.

### Creating a Table and Pushing Data
Let’s break down the process of creating a table on the MyScaleDB cluster. First, we’ll create a table named RAG. This table will have three columns:`id`
, `page_content`
and `embeddings`
. The id column will hold the unique `id`
of each row, the `page_content`
column will store the textual content, and the `embeddings`
column will save the embeddings of corresponding page content.

After creating the table, we save the data to the newly created RAG table in the form of batches.

### Configuring DSPy with MyScaleDB
We connect DSPy and MyScaleDB, and configure DSPy to use our language and retrieval models by default.

Note: The embedding model we use here should be the same one defined above.

### Defining the Signature
We define the `GenerateAnswer`
signature to specify the inputs and outputs for our question-answering task.

### Defining the RAG Module
The `RAG`
module integrates retrieval and generation steps. It retrieves relevant passages and generates answers based on the context.

The `forward`
method accepts the question as input and uses the retriever to find relevant chunks from the integrated database. These retrieved chunks are then passed to the `ChainOfThought`
module to generate a foundational prompt.

### Setting Up Teleprompters
Next, we will use the `BootstrapFewShot`
teleprompter/optimizer to compile and optimize our basic prompt.

This code tasks the `RAG`
class defined above and uses the examples along with the optimizer to generate the best possible prompt for our LLM.

### Running the Pipeline
Finally, we run our compiled RAG pipeline to answer questions based on the context stored in MyScaleDB.

## Conclusion
DSPy framework has revolutionized our interaction with LLMs by replacing hard-coded prompts with a programmable interface, significantly streamlining the development process. This transition from manual prompt writing to a more structured, programming-oriented methodology has [enhanced AI applications’ efficiency](https://thenewstack.io/enhance-your-rag-application-with-advanced-sql-vector-queries/), consistency and scalability. By abstracting the complexities of prompt engineering, DSPy allows developers to focus on defining high-level logic and workflows, thereby accelerating the deployment of sophisticated AI-driven solutions.

MyScaleDB, a vector database specifically developed for AI applications, plays a crucial role in enhancing the performance of such systems. Its advanced, proprietary algorithms boost the speed and accuracy of AI applications. Additionally, MyScaleDB is cost-effective, offering new users free storage for up to 5 million vectors. This makes it an attractive option for startups and researchers looking to use robust database solutions without the initial investment.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)