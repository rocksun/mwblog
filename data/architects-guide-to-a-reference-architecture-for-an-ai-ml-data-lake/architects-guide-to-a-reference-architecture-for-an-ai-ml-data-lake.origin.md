# Architect’s Guide to a Reference Architecture for an AI/ML Data Lake
![Featued image for: Architect’s Guide to a Reference Architecture for an AI/ML Data Lake](https://cdn.thenewstack.io/media/2024/03/c20d5e17-lake-1024x577.jpg)
In enterprise artificial intelligence, there are two main types of models: discriminative and generative. Discriminative models are used to classify or predict data, while generative models are used to create new data. Even though generative AI has dominated the news of late, organizations are still pursuing both types of AI.
Discriminative AI still remains an important initiative for organizations that want to operate more efficiently and pursue additional revenue streams. These different types of AI have a lot in common, but there are significant differences that must be taken into account when building your AI data infrastructure.
Organizations should not build an infrastructure dedicated to AI and AI only while leaving workloads like data analytics and data science to fend for themselves. It is possible to build a
[complete data infrastructure](https://thenewstack.io/the-architects-guide-to-storage-for-ai/) that supports all the needs of the organization — data analytics, data science, discriminative AI and generative AI.
## The Modern Data Lake
Let’s start by defining a modern data lake, as that will serve as the foundation for our reference architecture. This architecture is not “recycled”; rather, it reflects engineering-first principles that are broadly applicable.
A modern data lake is one-half data warehouse and one-half data lake, and uses object storage for everything.
[Using object storage for a data lake](https://thenewstack.io/how-to-build-a-modern-data-infrastructure-using-a-lakehouse/) makes perfect sense, as object storage is for unstructured data, which is what a data lake is meant to store.
However, while using object storage for a data warehouse may sound odd, a data warehouse built this way represents the next generation of data warehouses. This is made possible by the open table format specifications (OTFs) authored by Netflix, Uber and Databricks, which make it seamless to employ object storage within a data warehouse.
The OTFs are Apache Iceberg, Apache Hudi and Delta Lake. Essentially, they define, in different ways, a data warehouse that can be built on top of object storage. Object storage provides a combination of scale and performance that other storage solutions can’t match. (This is often described as “performance at scale.”)
Since these are modern specifications, they have advanced features that old-fashioned data warehouses don’t have such as partition evolution, schema evolution and zero-copy branching.
Finally, since the data warehouse is
[built with object storage](https://thenewstack.io/the-architects-guide-to-using-ai-ml-with-object-storage/), you can use this same object store for unstructured data like images, video files, audio files and documents. MLOps tools will use this same object store for model checkpoints, log files and data sets. Unstructured data is usually stored in what the industry calls a data lake.
Using an object store as the foundation for both your data lake and your data warehouse results in a solution capable of holding all your data. Structured storage resides in the OTF-based data warehouse and unstructured storage lives in the data lake. The same instance of your object store can be used for both.
At MinIO, we call this combination of an OTF-based data warehouse and a data lake the modern data lake, and we see it as the foundation for all your AI and ML workloads. It’s where data is collected, stored, processed and transformed. Training models using discriminative AI (supervised, unsupervised and reinforcement learning) often require a storage solution that can handle structured data that can live in the data warehouse.
On the other hand, if you are training
[large language models (LLMs)](https://roadmap.sh/guides/introduction-to-llms), you must manage unstructured data or documents in their raw and processed form in the data lake.
This post focuses on those areas of the modern data lake reference architecture that support the different AI and ML workloads — specifically, discriminative AI and generative AI.
## Discriminative AI
Discriminative AI models require data of all types for training. Models for image classification and speech recognition will use unstructured data in the form of images and audio files. On the other hand, models for fraud detection and medical diagnosis make predictions based on structured data. Let’s look at options available within the modern data lake for storing and manipulating the data needed by discriminative AI.
### Storage for Unstructured Data
Unstructured data will reside in the data lake, where it can be used for training and testing models. Training sets that can fit into memory can be loaded prior to training (before your epoch loop starts). However, if your training set is large and will not fit into memory, you will have to load a list of objects before training and retrieve the actual objects while processing each batch in your epoch loop. This could put a strain on your data lake if you do not build it using a high-speed network and high-speed disk drives.
If you are training models with data that cannot fit into memory, then we strongly recommend building your data lake with a 100 GB network and nonvolatile memory express (NVMe) drives.
### Storage for Semi-Structured Data
There are a few options available within the modern data lake for storing semi-structured files like Parque, AVRO, JSON and even CSV files. It’s easiest to store them in your data lake and load them the same way you’d load unstructured objects. If the data in these semi-structured files is not needed by other workloads that the modern data lake supports (data analytics and data science), this is the best option.
Another option is to load these files into your data warehouse, where other workloads can use them. When data is loaded into your data warehouse, you can use
[zero-copy branching to perform experiments](https://blog.min.io/parallel-ml-experimentation-leveraging-minio-lakefs/) with your data.
### Zero-Copy Branching in the Data Warehouse
Feature engineering is a technique for improving data sets used to train a model. OTF-based data warehouses include a very slick feature called zero-copy branching. This allows data to be branched the same manner that code can be branched within a git repository. As the name suggests, this feature does not make a copy of the data. Rather, it uses the metadata layer of the open table format that was used to implement the data warehouse to create the appearance of a unique copy of the data.
Data scientists can experiment with a branch; if their experiments are successful, then they can merge their branch back into the main branch for other data scientists to use. If the experiment is not successful, then the branch can be deleted.
## Generative AI
All models, whether they are small models built with Scikit-Learn, custom neural networks built with PyTorch or TensorFlow, or large language models based on transformer architecture, require numbers as inputs and produce numbers as outputs. This places additional requirements on your data infrastructure for generative AI, where words have to be turned into numbers (or vectors, as we shall see).
A generative AI-based solution gets more involved if you want to use private documents that contain your company’s proprietary knowledge to enhance the answers produced by the LLMs. This enhancement could be in the form of retrieval-augmented generation or LLM fine-tuning.
This section will discuss all these techniques (turning words into numbers, RAG and fine-tuning) and their impact on AI data infrastructure. Let’s start by discussing how to build a custom corpus and where it should reside.
## Creating a Custom Corpus with a Vector Database
If you are serious about generative AI, then your custom corpus should define your organization. It should contain documents with knowledge that no one else has, and should only contain true and accurate information. Furthermore, your custom corpus should be built with a vector database. A vector database indexes, stores and provides access to your documents alongside their vector embeddings, which are the numerical representations of your documents. (This solves the number problem described above.)
Vector databases facilitate semantic search. Understanding how this is done requires a lot of mathematical background and is complicated. However, semantic search is conceptually easy to understand. Let’s say you want to find all documents that discuss anything related to artificial intelligence. To do this on a conventional database, you would need to search for every possible abbreviation, synonym and related term of “artificial intelligence.” Your query would look something like this:
Not only is the manual similarity search arduous and prone to error, but the search itself is very slow. A vector database can take a request like the one shown below and run the query faster, with greater accuracy. The ability to run semantic queries quickly and accurately is important if you wish to use retrieval-augmented generation.
Another important consideration for your custom corpus is security. Access to documents should honor access restrictions on the original documents. (It would be unfortunate if an intern could gain access to the CFO’s financial results that have not been released to Wall Street yet.) Within your vector database, you should set up authorization to match the access levels of the original content. This can be done by integrating your vector database with your organization’s identity and access management solution.
At their core, vector databases store unstructured data. Therefore, they should use your data lake as their storage solution.
## Building a Document Pipeline
Unfortunately, most organizations do not have a single repository with clean and accurate documents. Rather, documents are spread across the organization in various team portals in many formats. Consequently, the first step in building a custom corpus is to build a pipeline that takes only documents that have been approved for use with generative AI and place them in your vector database. For large global organizations, this could potentially be the hardest task of a generative AI solution.
It is common for teams to have documentation in draft format in their portals. There may also be documents that are random musings about what could be. These documents should not become a part of a custom corpus as they do not accurately represent the business. Unfortunately, filtering these documents will be a manual effort.
A document pipeline should also convert the documents to text. Fortunately, a few open source libraries can do this for many of the common document formats. Additionally, a document pipeline must break documents into small segments before saving them in the vector database. This is due to limitations on prompt size when these documents are used for retrieval-augmented generation, which will be discussed in a later section.
## Fine-Tuning Large Language Models
When we fine-tune a
[large language model](https://thenewstack.io/llm/), we train it a little more with information from the custom corpus. This could be a good way to get a domain-specific LLM. While this option does require compute resources to perform the fine-tuning against your custom corpus, it is not as intensive as training a model from scratch, and can be completed in a modest time frame.
If your domain includes terms not found in everyday usage, fine-tuning may improve the quality of the LLM’s responses. For example, projects that use documents from medical research, environmental research and anything related to the natural sciences may benefit from fine-tuning. Fine-tuning takes the highly specific vernacular found in your documents and bakes them into the parametric parameters of the model. The advantages and disadvantages of fine-tuning should be understood before deciding on this approach.
**Disadvantages**
- Fine-tuning will require compute resources.
- Explainability is not possible.
- You will periodically need to fine-tune again with new data as your corpus evolves.
- Hallucinations are a concern.
- Document-level security is impossible.
**Advantages**
- The LLM has knowledge from your custom corpus via fine-tuning.
- The inference flow is less complicated than RAG.
While fine-tuning is a good way to teach an LLM about the language of your business, it dilutes the data since most LLMs contain billions of parameters, and your data will be spread across all of them. The biggest disadvantage of fine-tuning is that document-level authorization is impossible. Once a document is used for fine-tuning, its information becomes a part of the model. It is not possible to restrict this information based on the user’s authorization levels.
Let’s look at a technique that combines your custom data and parametric data at inference time.
## Retrieval-Augmented Generation (RAG)
Retrieval-augmented generation (RAG) is a technique that starts with the question being asked. It uses a vector database to marry the questions with additional data, then passes the question and data to an LLM for content creation. With RAG, no training is needed because we educate the LLM by sending it relevant text snippets from our corpus of quality documents.
It uses a question-answering task that works like this: A user asks a question in your application’s user interface. Your application will take the question — specifically, the words in it — and, using a vector database, search your corpus of quality documents for text snippets that are contextually relevant. These snippets and the original question are sent to the LLM.
This entire package — question plus snippets (context) — is known as a prompt. The LLM will use this information to generate your answer. This may seem like a silly thing to do. If you already know the answer (the snippets), why bother with the LLM? Remember, this is happening in real time, and the goal is to generate text that you can copy and paste into your research. You need the LLM to create the text that incorporates the information from your custom corpus.
This is more complicated than fine-tuning. However, user authorization can be implemented since the documents (or document snippets) are selected from the vector database at inference time. The information in the documents never becomes a part of the model’s parametric parameters. The advantages and disadvantages of RAG are listed below.
**Disadvantages**
- Inference flow is more complicated.
**Advantages**
- The LLM has direct knowledge from your custom corpus.
- Explainability is possible.
- No fine-tuning is needed.
- Hallucinations are significantly reduced and can be controlled by examining the results from the vector database queries.
- Authorization can be implemented.
## Conclusion
This post outlines our experience in working with enterprises to construct an AI data infrastructure. It identifies the core components, the key building blocks and the tradeoffs of different AI approaches. The foundational element is a modern data lake built on top of an object store. The object store must be capable of delivering performance at scale, where scale is hundreds of petabytes and often exabytes.
By following this modern data lake reference architecture for AI and ML, we anticipate the user will be able to build a flexible, extensible data infrastructure, which while targeted at AI and ML, will be equally performant on all online analytical processing (OLAP) workloads. To get specific recommendations on the component parts, please don’t hesitate to reach out to me at
[keith@min.io](mailto:keith@min.io). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)