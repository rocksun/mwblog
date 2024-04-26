# Apache NiFi 2.0.0: Building Python Processors
![Featued image for: Apache NiFi 2.0.0: Building Python Processors](https://cdn.thenewstack.io/media/2024/04/12717baa-python-processors-2-1024x576.jpg)
[Apache NiFi](https://nifi.apache.org/), a robust platform tailored for [dataflow management](https://thenewstack.io/the-architects-guide-to-the-modern-data-stack/), offers lots of features aimed at enhancing efficiency and flexibility in handling data. Its web-based user interface provides a seamless experience for designing, controlling and monitoring dataflows.
NiFi supports the building of custom processors and extensions, enabling users to tailor the platform to their specific needs.
With a multitenant user experience, NiFi ensures that multiple users can interact with the system concurrently, each with their own set of access privileges.
[Python processors](https://medium.com/cloudera-inc/building-a-library-of-python-processors-6b5517404a58) offer a powerful means to extend NiFi’s functionality, enabling users to leverage the rich ecosystem of [Python](https://thenewstack.io/python/) libraries and tools within their dataflows. Here we’ll discuss the advantages of incorporating Python into NiFi workflows and explore practical use cases where Python processors can streamline data processing tasks, enhance flexibility and accelerate development.
Whether you’re aiming to integrate machine learning algorithms, perform custom data transformations or interact with external systems, building Python processors in Apache NiFi can help you meet those data integration needs.
## What’s Apache NiFi Good for?
One of NiFi’s standout features is its highly configurable nature, allowing users to tailor data routing, transformation and system mediation logic to their specific requirements. NiFi helps users achieve the data processing outcomes they want, such as prioritizing loss tolerance over guaranteed delivery or optimizing for low latency versus high throughput.
Dynamic prioritization enables real-time adjustment of data priorities within the flow, while the ability to modify flows at runtime adds a layer of flexibility to adapt to changing requirements. NiFi also incorporates back pressure mechanisms to regulate data flow rates and prevent overload, ensuring smooth and efficient operation even under varying workloads.
NiFi is designed to support both vertical and horizontal scaling. Whether scaling up to leverage the full capabilities of a single machine or scaling out with a zero-leader clustering model, NiFi can accommodate data processing tasks of any magnitude.
Data provenance is another critical feature, allowing users to track the journey of data from its inception to its final destination. This provides invaluable insights for auditing, troubleshooting and ensuring data integrity throughout the process.
[Security](https://thenewstack.io/security/) is paramount in NiFi, with support for SSL, SSH, HTTPS and encrypted content, among other security measures. Pluggable fine-grained role-based [authentication and authorization](https://thenewstack.io/how-do-authentication-and-authorization-differ/) mechanisms ensure that access to dataflows is carefully controlled, allowing multiple teams to manage and share specific portions of the flow securely.
NiFi’s design philosophy, inspired by concepts like
[flow-based programming ](https://github.com/samuell/awesome-fbp)and [staged event-driven architecture](https://thenewstack.io/the-rise-of-event-driven-architecture/), offers several compelling advantages:
- Intuitive visual interface for designing and managing data flows, enhancing productivity and ease of use.
- Asynchronous processing model, supporting high throughput and natural buffering to accommodate fluctuating workloads.
- Built-in concurrency management, abstracting away the complexities of multithreaded programming.
- Emphasis on component reusability and testability, promoting a modular and robust design approach.
- Native support for back-pressure and error handling, ensuring robustness and reliability in data processing pipelines.
- Comprehensive visibility into data flow dynamics, enabling effective monitoring and troubleshooting.
## Why Build with Python in Apache NiFi?
[Apache NiFi ](https://github.com/apache/nifi)is a powerful tool for data ingestion, transformation and routing. Python processors in NiFi provide a flexible way to extend its capabilities, particularly for processing unstructured data or integrating with external systems like AI models or vector stores such as the cloud native vector database [Milvus](https://milvus.io/).
When dealing with unstructured file types that tools like
[Cloudera Data Flow](https://thenewstack.io/pulsar-nifi-better-together-for-messaging-streaming/) can ingest, Python processors can be invaluable for implementing custom logic to parse and manipulate the data. For example, you might use Python to extract specific information from text documents, perform sentiment analysis on text data or preprocess images before further analysis.
Structured file types, on the other hand, can often be processed using NiFi’s built-in processors without the need for custom Python code. NiFi provides a wide range of processors for handling structured data formats like CSV, JSON, Avro, etc., as well as for interacting with
[databases](https://thenewstack.io/data/), [APIs](https://thenewstack.io/api-management/), and other enterprise systems.
When you need to interface with AI models or other external systems like Milvus, Python processors offer a convenient way to integrate this functionality into your NiFi dataflows. For tasks such as text-to-text, text-to-image or text-to-speech processing, you can write Python code to interact with the relevant models or services and incorporate this processing into your NiFi pipelines.
## Python: A New Era in NiFi 2.0.0
[Apache NiFi 2.0.0](https://nifi.apache.org/documentation/v2/) has introduced some significant improvements to the platform, especially in terms of Python integration and performance enhancements. The ability to seamlessly integrate Python scripts into NiFi dataflows opens up a wide range of possibilities for working with diverse data sources and leveraging the power of generative AI.
Before this version, while it was possible to work with Python in NiFi, the flexibility may have been limited, and executing Python scripts might not have been as streamlined as users might want. With the latest version, however, Python integration has been greatly improved, allowing for more seamless execution of Python code within NiFi pipelines.
Additionally, the support for JDK 21+ brings performance improvements, making NiFi faster and more efficient, particularly in handling multithreading tasks. This can significantly enhance the scalability and responsiveness of NiFi dataflows, especially when dealing with large volumes of data or complex processing tasks.
The introduction of features like
Run Process Group as Stateless and
Rules Engine for Development Assistance further enhances the capabilities and usability of NiFi, providing developers with more flexibility and tools to build robust dataflow pipelines.
## A Sample Processor: Watson SDK to Foundation AI Model
This Python code defines a NiFi processor called
that interacts with IBM WatsonX AI services to generate responses based on input prompts. Note everything with NiFi 2.0.0 – Python3.10+ is the minimum.
[CallWatsonXAI](https://github.com/tspannhw/FLaNK-python-watsonx-processor/blob/main/WatsonXAI.py)
Let’s break down the code and explain each part.
### Imports
These are the necessary imports for the script:
jsonand
reare Python’s built-in modules for handling
[JSON data](https://thenewstack.io/python-for-beginners-how-to-use-json-in-python/)and [regular expressions](https://thenewstack.io/how-to-speed-up-regular-expressions-under-production-pressure/), respectively.
FlowFileTransformand
FlowFileTransformResultare classes from a custom module (nifiapi.flowfiletransform) related to NiFi processing.
PropertyDescriptor,
StandardValidators, and
ExpressionLanguageScopeare classes from another custom module (nifiapi.properties) used for defining processor properties.
### Class Definition
- This defines a class called
CallWatsonXAIthat extends the
FlowFileTransformclass, which presumably handles transformation of data within NiFi.
### Processor Details
- Defines details about the processor such as version, description and tags. But note that 2.0.0-M2 is the current version.
### Property Descriptors
- Defines properties that can be set for the processor. In this case,
PROMPT_TEXT,
WATSONXAI_API_KEY, and
WATSONXAI_PROJECT_ID.
### Constructor
- Initializes the processor class and appends property descriptors to the list of properties.
### getPropertyDescriptors Method
- This method is required by NiFi processors to retrieve the list of properties.
### transform Method
- This is the main method responsible for processing data. It receives a
contextobject containing information about the processor’s execution environment and a
flowfile objectcontaining the data to be processed.
### IBM WatsonX Integration
- Imports IBM Watson Machine Learning modules.
- Gets input values such as prompt text, WatsonX API key, and project ID from NiFi processor properties.
- Configures and calls the IBM WatsonX model to generate a response based on the prompt text.
### Output Handling
- Defines output attributes and converts the generated response to JSON format.
### Logging and Return
- Logs the prompt text.
- Returns the result of the transformation, indicating success and providing the output data and attributes.
## Pre-Packaged Python Processors
NiFi 2.0.0 comes with a diverse set of Python processors that offer a wide range of functionalities.
**VectorDB Interface for Pinecone:**This processor facilitates interaction with [Pinecone](https://thenewstack.io/vector-databases-are-having-a-moment-a-chat-with-pinecone/), a vector database service, allowing users to query and store data efficiently. **ChunkDocument:**This processor breaks down large documents into smaller chunks, making them suitable for processing and storage, especially in vector databases where size constraints may apply. **ParseDocument:**This processor seems quite versatile, capable of parsing various document formats like Markdown, PowerPoint, Google Docs and [Excel](https://thenewstack.io/python-delights-excel-data-nerds-plus-data-lake-enthusiasts/), extracting text content for further processing or storage. **ConvertCSVtoExcel:**As the name suggests, this processor converts data from CSV format to Excel format, providing flexibility in data interchange and processing. **DetectObjectInImage:**This processor appears to leverage deep learning techniques for [object detection within images,](https://medium.com/@tspann/image-processing-with-custom-python-and-nifi-2-0-06eadc62c03c)enabling users to analyze image data and extract valuable insights. **PromptChatGPT:**This processor sounds intriguing—it integrates with ChatGPT or a similar conversational AI model, allowing users to generate responses or engage in conversations based on prompts. **PutChroma and QueryChroma:**These processors are related to [Chroma](https://thenewstack.io/exploring-chroma-the-open-source-vector-database-for-llms/), an open source database for large language models (LLMs). They facilitate data storage (PutChroma) and retrieval/querying (QueryChroma) within a Chroma database or similar system.
## Conclusion
Prioritizing Python integration in Apache NiFi marks a significant milestone in bridging the gap between
[data engineers](https://thenewstack.io/what-data-engineering-is-and-why-its-not-just-about-data-science/) and [data scientists](https://thenewstack.io/is-the-answer-to-your-data-science-needs-inside-your-it-team/) while expanding the platform’s versatility and applicability.
By enabling Python aficionados to develop NiFi components seamlessly in Python, development cycles are streamlined, accelerating the implementation of data pipelines and workflows.
It’s an exciting time for
[Python processors in NiFi](https://github.com/tspannhw/EverythingApacheNiFi), and contributing to the ecosystem can be immensely valuable. Developing and sharing Python processors can extend NiFi’s capabilities, and address specific use cases.
To get started with NiFi, users can refer to the quickstart guide for development and the
[NiFi Developer’s Guide](https://nifi.apache.org/documentation/v2/) for more comprehensive information on contributing to the project. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)