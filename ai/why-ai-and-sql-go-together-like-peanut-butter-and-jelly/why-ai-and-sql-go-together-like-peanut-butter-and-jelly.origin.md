# Why AI and SQL Go Together Like Peanut Butter and Jelly
![Featued image for: Why AI and SQL Go Together Like Peanut Butter and Jelly](https://cdn.thenewstack.io/media/2025/06/ab0e7bd3-ai-sql-go-together-pbj-1024x576.jpg)
Natural human language is the ideal interface for accessing data, and making it conversational is the ultimate goal. Advanced AI, powered by [large language models (LLMs)](https://thenewstack.io/what-is-a-large-language-model/), excels at interpreting human intent and translating conversational queries into precise responses. A scalable framework for 21st-century information retrieval needs to span human language queries and expansive datasets. This requires an AI-SQL synergy.

[Structured query language (SQL)](https://thenewstack.io/3-foundational-principles-for-writing-efficient-sql/), grounded in relational algebra and set theory, abstracts programming and storage complexities to focus on data retrieval, including data location, filtering and complex combinations. Modern SQL runs on distributed systems with thousands of CPU cores and advanced indexing for rapid searches (e.g., account IDs, vectorized text, images, videos) alongside extensible functions like fraud detection.
Petabyte-scale and distributed object-relational SQL databases that contain extensible data types like geographic, image, graph and time-series data can be made accessible directly to end users. This will make information retrieval easier and more efficient without requiring advanced skills in SQL query writing.

## A Word on Retrieval-Augmented Generation
[Retrieval-augmented generation (RAG)](https://thenewstack.io/advanced-retrieval-augmented-generation-rag-techniques/) is a widely adopted framework for integrating language models into external database queries and resources; it’s often used as a technique to make chatbots more intelligent.
Though there are similarities between RAG patterns and the concepts in this article, this article proposes a first-principles approach to information retrieval, focusing on AI paired with distributed, object-relational SQL systems. Where RAG patterns make AI apps more intelligent, I’m examining how to make massively scalable complex database systems more easily accessible with human chat.

## AI Is the Human Interface
Language is necessary to express ideas and intentions. But even well-crafted language can sometimes be confusing. For instance, a phone call often clarifies an email exchange more quickly than going back and forth online. This is because conversation allows for nuanced, direct interaction. Unlike coding, which requires technical expertise, natural language is intuitive and widely accessible through manual typing or spoken word.

Advances in AI enable computers to understand and process human language, capturing content, context and intent, to generate relevant responses. By translating conversational input into structured queries, AI serves as an effective interface for data access, connecting human needs to complex database systems in a way that aligns with our natural communication patterns.

## LLMs Are Not Enough
LLMs excel at processing human language, delivering answers based on patterns learned from internet-scale training datasets. For example, when asked the most populated city in Southern California, an LLM correctly responds “Los Angeles,” drawing on ingrained cultural knowledge built into its deep neural network rather than searching raw data. However, LLMs falter with specific, data-driven queries.

Consider a query asking how many people live within a 30-minute drive during rush hour to the Port of Los Angeles. An LLM may guess, but it lacks the precise, real-time data needed to provide an accurate answer. In cases where people’s lives are on the line, having precise information is crucial.

While LLMs understand intent, they require supplemental data sources to provide reliable, actionable responses. This limitation underscores the need for AI to interface with robust data systems like SQL to deliver precise, context-specific answers for complex, real-world scenarios.

## SQL as the Data Layer for AI
To deliver precise, data-driven answers for personal and enterprise needs, AI requires a robust backend system. Interfacing with disparate, nonstandardized systems is inefficient and lacks scalability. Similarly, relying on AI to write ad hoc code in languages like [C++](https://roadmap.sh/cpp), [Java](https://thenewstack.io/introduction-to-java-programming-language/), [Python](https://thenewstack.io/what-is-python/) or [Rust](https://thenewstack.io/rust-programming-language-guide/) to query unstructured data is impractical and prone to errors. Nonrelational databases, such as key-value stores, may support sorting, joining or aggregating, but often lack SQL’s standardized, expressive framework, which can hinder AI’s ability to efficiently process complex queries.

SQL databases, widely adopted in enterprises for managing most structured data, offer a declarative, standardized architecture that simplifies locating, filtering and combining data.

However, learning to [write large, complex SQL queries](https://thenewstack.io/how-to-write-sql-queries/) is not trivial and takes engineers several years to master. By developing specialized AI models that excel in writing SQL queries and speaking and understanding human language, we create a bridge that transcends human intent with the power to create fine-grained and complex queries to match the user intent.

In consequence, AI will be able to easily create complex SQL queries using a single well-defined language that AI can master to access all the data it needs.

## SQL Will Be Object-Relational and Extensible
Traditional SQL databases, such as MySQL, primarily handle basic data types including integers, floats, dates and text. However, modern object-relational databases, such as PostgreSQL, support extensible, context-aware data types, including geographic, image, graph and time series data. This extensibility enables SQL to manage diverse types of data, aligning with the varied queries humans ask AI interfaces.

By accommodating dynamic data types, extensible SQL systems empower AI to process and retrieve complex, context-rich information efficiently. Object-relational and extensible-data SQL databases are therefore essential for ensuring AI can answer a broad spectrum of human inquiries that include access to diverse data types.

## AI Needs Distributed Systems
Traditional SQL databases ran on single systems with limited processing power, typically four to 200 CPU cores. This is not adequate to meet the demands of today’s databases, like querying massive data sets for AI applications that require thousands of CPU cores.

The scale required of today’s data processing capabilities is beyond a single computer’s capacity. It needs distributed SQL databases that intelligently partition and distribute data and query processing across a grid or farm of computers. These systems help ensure scalability, speed and reliability by leveraging parallel processing across numerous nodes.

For AI to deliver real-time, accurate responses to complex queries, distributed SQL databases will provide the robust, high-performance backend needed to handle the world’s growing data volumes efficiently.

## The Elegance of SQL
SQL’s elegance lies in its intellectual purity, rooted in mathematical foundations. It emerged in the early 1970s at IBM’s San Jose Research Laboratory, driven by [Dr. Edgar F. Codd’s groundbreaking 1970 paper](https://thenewstack.io/to-sql-or-not-to-sql-that-is-not-the-question/), “A Relational Model of Data for Large Shared Data Banks.” Codd, a mathematician, introduced the relational model, using mathematical principles like relational algebra and tuple relational calculus to structure data into tables (relations) with rows (tuples) and columns, ensuring data integrity and query efficiency.

His goal was to simplify data retrieval, making it accessible without complex programming. Designed for nonprogrammers, SQL’s declarative syntax allows users to specify “what” data to retrieve, not “how,” abstracting physical storage. Standardized by ANSI/ISO in the 1980s, SQL became the universal language for relational databases, enabling robust, scalable querying across diverse systems.

A relation is a table, a structured set of data with columns defining attributes and rows as [tuples](https://en.wikipedia.org/wiki/Tuple#:~:text=In%20mathematics%2C%20a%20tuple%20is,tuple%2C%20called%20the%20empty%20tuple.), each representing a data instance. A set is a collection of unique elements, forming the basis of set theory, which underpins SQL’s operations. Relational algebra, a formal system for manipulating relations, defines operations like join (combining tables based on shared attributes), projection and selection, directly translating into SQL’s declarative syntax (e.g., SELECT, JOIN).

The brilliance of SQL is most evident in the SQL optimizer component, which separates logical query intent from physical execution. Using cost-based query planning, the optimizer employs dynamic programming and other algorithms to evaluate billions of potential query plans, selecting the lowest-cost option in subsecond time. It performs logical transformations (e.g., rewriting queries for efficiency) and maps them to physical data access patterns, such as index scans or hash joins, ensuring robust, scalable performance. This mathematical alignment makes SQL timelessly beautiful.

## AI-SQL: Like Peanut Butter and Jelly
The future of information retrieval combines the power of AI’s natural language capabilities with advanced SQL systems for data access, redefining how humans access the largest and most complex datasets. AI generates precise SQL queries using schema knowledge, while distributed SQL systems, scaling across thousands of CPU cores, ensure speed and reliability. Object-relational SQL, with extensible data type support for geographic, text, image, video and graph data, handles diverse datasets.

This AI-SQL framework, combining natural language, distributed processing and data type extensibility, is what we need in today’s digital environments.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)