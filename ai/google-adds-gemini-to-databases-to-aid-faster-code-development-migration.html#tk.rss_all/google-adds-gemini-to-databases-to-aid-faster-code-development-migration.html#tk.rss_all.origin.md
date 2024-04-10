Google Cloud is adding capabilities driven by its proprietary
[large language model](https://www.infoworld.com/article/3709489/large-language-models-the-foundations-of-generative-ai.html), Gemini to its database offerings, which include Bigtable, Spanner, Memorystore for Redis, Firestore, CloudSQL for MySQL, and AlloyDB for PostgreSQL, the company announced at its annual Next conference.
The Gemini-driven capabilities, which are currently in public preview, include
[SQL](https://www.infoworld.com/article/3219795/what-is-sql-the-lingua-franca-of-data-analysis.html) generation, and [AI](https://www.computerworld.com/article/1647870/what-is-artificial-intelligence.html) assistance in managing and migrating databases.
Last year, the company
[added Duet AI, now rebranded to Gemini, in Spanner and its Database Migration Service](https://www.infoworld.com/article/3705374/google-expands-duet-ai-features-across-its-cloud-services.html).
The SQL generation capability can be accessed via the company’s SQL editor named Database Studio to be found inside Google’s Cloud Console.
As the name suggests, this capability allows developers to easily generate, summarize, and fix SQL code with intelligent code assistance, code completion, and guidance directly inside Database Studio, which in turn improves productivity, the company said, adding that Database Studio supports both
[MySQL](https://www.infoworld.com/article/2615974/applications-how-to-get-started-with-mysql.html) and [PostgreSQL](https://www.infoworld.com/article/3698688/serverless-is-the-future-of-postgresql.html) dialects.
In addition, Database Studio comes with a context-aware chat interface that can take input in natural language to help build database applications faster, according to the company.
Google is not the only database provider that has added SQL code generation to its list of capabilities, analysts said.
“SQL code generation with assistance from generative AI has become one of the low-hanging fruits for
[generative AI](https://www.infoworld.com/article/3689973/what-is-generative-ai-artificial-intelligence-that-creates.html) over the past year,” said Tony Baer, principal analyst at dbInsight.
“The new breed of generative AI database code assistants should eventually have a key advantage over those assistants that cater to general-purpose languages, which is that they are database-specific and can therefore read the metadata of databases to not just form, but also optimize SQL code,” Baer explained.
## Managing and migrating databases with Gemini
In order to help manage databases better, the cloud service provider is adding a new feature called the Database Center, which will allow operators to manage an entire fleet of databases from a single pane.
Database Center also provides intelligent dashboards to proactively assess availability, data protection, security, and compliance posture, the company said.
Further, the company is infusing Gemini into the Database Center via a natural language-based chat window that will allow enterprise teams to interact with the databases and find more insights about them.
The chat window also can be used to generate troubleshooting tips for database-related issues, the company said.
Google’s idea to have a single pane to manage multiple databases takes inspiration from Oracle, according to Baer.
While Oracle provides the capability for multiple instances of the same databases, which is multimodal, Google extends the capability to a heterogenous collection of databases, Baer said.
“Having central control means that enterprises can be consistent with their policies for security, data access, and service level agreements (SLAs). That’s a major step toward the simplification that we expect from the cloud,” the principal analyst explained.
Google has also extended Gemini to its Database Migration Service, which earlier had support for Duet AI.
Gemini’s improved features will make the service better, the company said, adding that Gemini can help convert database-resident code, such as stored procedures, functions to PostgreSQL dialect.
Additionally, Gemini-powered database migration also focuses on explaining the translation of the code with a side-by-side comparison of dialects, along with detailed explanations of the code and recommendations.
The focus on explaining the code has been planned to help upskill and retrain SQL developers, the company said.
## AlloyDB AI gets new features
In addition to powering databases with Gemini, Google has added new features to AlloyDB AI.
AlloyDB AI, which was
[introduced last year](https://www.infoworld.com/article/3705374/google-expands-duet-ai-features-across-its-cloud-services.html) as part of its [AlloyDB for PostgreSQL database service](https://www.infoworld.com/article/3660548/why-google-cloud-will-battle-aws-azure-in-a-red-hot-postgresql-market.html), is a suite of integrated capabilities targeted at helping developers build generative AI-based applications using real-time data.
The new features include allowing generative AI-based applications to query data with natural language and a new type of database view.
The enablement of querying data with natural language will allow AI-based applications to respond to more sets of questions from enterprise teams, the company said.
On the other hand, the new type of database view — parameterized secure view — allows enterprise teams to secure data based on the end-users’ context.
AlloyDB AI can be downloaded using
[AlloyDB Omni](https://www.infoworld.com/article/3691825/google-ambushes-on-prem-postgresql-with-alloydb-omni.html), which has been made generally available. AlloyDB Omni is a downloadable version of Google Cloud's PostgreSQL-compatible database service.
Other updates include the addition of Bigtable Data Boost, similar to Spanner Data Boost released last year, and performance enhancements to Memorystore for Redis.