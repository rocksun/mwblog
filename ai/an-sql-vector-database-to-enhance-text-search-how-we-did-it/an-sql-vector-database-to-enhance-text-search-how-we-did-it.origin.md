# An SQL Vector Database To Enhance Text Search: How We Did It
![Featued image for: An SQL Vector Database To Enhance Text Search: How We Did It](https://cdn.thenewstack.io/media/2024/05/4ab1de9b-tanvity-1024x576.jpg)
The explosive growth of global data, projected to
[reach 181 zettabytes by 2025](https://explodingtopics.com/blog/data-generated-per-day) and 80% unstructured, poses a challenge for traditional [databases](https://thenewstack.io/sql-vector-databases-are-shaping-the-new-llm-and-big-data-paradigm/) unable to handle unstructured text data effectively. Full-text search addresses this by enabling intuitive and efficient access to unstructured text data, allowing users to search based on topics or key ideas.
To enhance text search capabilities,
[MyScaleDB](https://github.com/myscale/MyScaleDB), an open source fork of ClickHouse [optimized for vector search](https://thenewstack.io/how-to-run-complex-queries-with-sql-in-vector-databases/), integrated [Tantivy](https://github.com/quickwit-oss/tantivy), a full-text search engine library. This upgrade significantly benefits those who use ClickHouse for logging, often as a substitute for Elasticsearch or Loki. It also benefits users [leveraging MyScaleDB in retrieval-augmented generation (RAG)](https://thenewstack.io/build-an-advanced-rag-application-using-myscaledb-and-llamaindex/) with large language models ( [LLMs](https://thenewstack.io/llm/)), combining vector and text search for improved accuracy.
This article explores the technical details of the Tanvity integration and how we measured its impact on performance.
## Limitations of ClickHouse’s Native Text Search
ClickHouse provides basic text search functions like
hasToken,
startsWith and
multiSearchAny that are suitable for simple-term queries. However, these functions fall short for more complex requirements such as phrase queries, fuzzy text matching and Best Match 25 (BM25) relevance ranking. Hence, we introduced Tantivy as the underlying implementation for full-text indexing, empowering MyScaleDB with full-text search capabilities. Tantivy’s full-text index supports fuzzy text queries and BM25 relevance ranking, and accelerates existing functions like
hasToken and
multiSearchAny term matching.
## Why We Chose Tantivy
Tantivy is an open source full-text search engine library written in
[Rust](https://roadmap.sh/rust). It’s designed for speed and efficiency, particularly in handling large volumes of text data.
### Tantivy’s Core Principles
**Building the index**: Tantivy tokenizes the input text, splitting it into independent tokens. It then creates an inverted index (posting list) and writes it to index files (segments). Meanwhile, Tantivy’s background threads utilize merge strategies to merge and update these segment index files. **Executing text searches**: When a user initiates a text search query, Tantivy parses the query statement, extracts tokens and, on each segment, sorts and scores documents based on the query conditions and the BM25 relevance algorithm. Finally, the query results from these segments are merged based on relevance scores and returned to the user.
### Key Features of Tantivy
**BM25 relevance scoring**: Elasticsearch, Lucene and Solr all utilize BM25 as the default relevance ranking algorithm. The BM25 score evaluates the accuracy and relevance of text searches, enhancing user search experience. **Configurable tokenizers**: This feature supports various language tokenizers, catering to users’ diverse tokenization needs. **Natural language queries**: Users can flexibly combine text queries using keywords like
AND,
ORand
IN, reducing the complexity of SQL statement writing.
For more functionalities, refer to
[Tantivy’s documentation](https://github.com/quickwit-oss/tantivy?tab=readme-ov-file#features).
### Seamless Integration Capabilities
MyScaleDB, written in
[C++](https://roadmap.sh/cpp), was developed on the foundation of ClickHouse, and serves as a robust search engine for AI-native applications. To enrich full-text search functionality, we needed a library that could be directly embedded into MyScaleDB.
Tantivy is a full-text search library inspired by Apache Lucene. Unlike Elasticsearch, Apache Solr and other similar engines, Tantivy can be integrated into various databases, including MyScaleDB. Since Tantivy is written in Rust, it can be integrated with C++ programs easily using
[Corrosion](https://github.com/corrosion-rs/corrosion).
## The Integration Process
### Building a C++ Wrapper for Tantivy
The raw Tantivy library can’t be used directly in MyScaleDB. To tackle cross-language development (C++ and Rust), we developed
[tantivy-search](https://github.com/myscale/tantivy-search), a C++ wrapper for Tantivy. It provides a set of foreign function interfaces (FFIs) for MyScaleDB, enabling direct management of index creation, destruction, loading and flexible handling of text search requirements in various scenarios.
### Implementing Tantivy as a Skipping Index in ClickHouse
[ClickHouse’s skipping index](https://clickhouse.com/docs/en/guides/improving-query-performance/skipping-indexes/) is mainly used to accelerate queries with
WHERE clauses. We implemented a new skipping index type named Full-Text Search (FTS), with Tantivy as the underlying implementation. So, for each data part in ClickHouse with the FTS index, we build a Tantivy index for it. To reduce the number of segment files for each index that need to be stored in a data part, MyScaleDB serializes these segment files into two files and stores them in the data part. The
skp_idx_[index_name].meta file records the name and offset of each segment file, while the
skp_idx_[index_name].data file stores the original data of each segment file.
Tantivy utilizes memory mapping (
mmap) to access segment files. This approach not only improves concurrent search speed but also enhances index construction efficiency. Since Tantivy cannot map the
skp_idx_[index_name].data file to memory directly, when a user initiates a query that needs the FTS index, MyScaleDB deserializes the index files (
.meta and
.data) to Tantivy segment files into a temporary directory and loads the Tantivy index. Tantivy loads these deserialized segment files via memory mapping in order to execute various types of text searches. Hence, the initial query request from users may take several seconds to complete.
In our
[managed service](https://myscale.com/), we store Tantivy’s segment index files on NVMe SSDs. This reduces I/O wait time and improves mmap performance in scenarios requiring random access and handling of page fault exceptions.
### Enhancing ClickHouse’s Native Text Search Functions
When requests with filtering conditions are initiated on columns containing FTS indexes, MyScaleDB first accesses the FTS index. It retrieves all row IDs of the column that meet the SQL filter conditions, and stores these row IDs in an advanced bitmap data structure known as a
[roaring bitmap](https://roaringbitmap.org/). While traversing granules, it determines if a granule’s row ID range intersects with the bitmap, indicating whether the granule can be dropped. Ultimately, MyScaleDB accesses only the granules that haven’t been dropped, thus achieving query acceleration.
Ideally, the skipping index does accelerate queries, but we found its effect is limited. If the searched term appears in almost all granules, MyScaleDB skips a small number of granules. This requires access to a large number of granules for the query, rendering the skipping index ineffective in such cases.
### Addressing Inefficiencies With TextSearch
To address skipping index inefficiency and fully exploit Tantivy’s full-text search capabilities, we incorporated the
TextSearch function into MyScaleDB. This function allows users to execute fuzzy text retrieval requests and obtain a set of documents sorted by BM25 score relevance. Additionally, users can employ natural language queries within the TextSearch function, significantly reducing the complexity of SQL writing.
The
TextSearch function retrieves the top thousand (or
*k*) most relevant results from the table when searching text. In terms of execution, MyScaleDB concurrently performs TextSearch text retrieval on all data parts. Consequently, each part collects the thousand most relevant results sorted by BM25 score. MyScaleDB then aggregates the results obtained from data parts based on BM25 scores. Finally, it retains the top thousand results, per the
ORDER BY and
LIMIT clauses specified in the user’s SQL query. The TextSearch function does not directly read data from within the data part. Instead, it retrieves index search results directly through Tantivy, making it extremely fast.
It’s important to note that MyScaleDB utilizes multiple data parts for storing data, with each data part responsible for storing a portion of the entire table’s data. We can’t merely average the BM25 scores corresponding to the same answer texts obtained from each part and sort them. This is because each part only considers the “total docs number,” “total tokens number” and “doc frequency” within the current part when calculating BM25 scores, without taking into account other BM25 algorithm-related parameters within other parts. Therefore, this would lead to a decrease in the accuracy of the final merged results.
To address this issue, we first calculate the BM25 statistics within each part before initiating the TextSearch query. Then we consolidate them into logically corresponding BM25 statistics for the entire table. Additionally, we have modified the Tantivy library to support using shared BM25 information. This ensures the correctness of the TextSearch search results across multiple parts.
Below is a simple example of
[using the TextSearch function](https://myscale.com/docs/en/text-search/) to perform a basic text search on the ms_macro dataset.
Output:
|
id |
text |
score
|2717481
|Sasha Obama Biography. Name at birth: Natasha Obama. Sasha Obama is the younger daughter of former U.S. president Barack Obama. Her formal name is Natasha, but she is most often called by her nickname, Sasha. Sasha Obama was born in 2001 to Barack Obama and his wife, Michelle Obama, who were married in 1992. Sasha Obama has one older sister, Malia, who was born in 1998.
|15.448088
|5016433
|Sasha Obama Biography. Sasha Obama is the younger daughter of former U.S. president Barack Obama. Her formal name is Natasha, but she is most often called by her nickname, Sasha. Sasha Obama was born in 2001 to Barack Obama and his wife, Michelle Obama, who were married in 1992. Sasha Obama has one older sister, Malia, who was born in 1998.
|15.407547
|564474
|Michelle Obama net worth: $11.8 Million. Michelle Obama Net Worth: Michelle Obama is an American lawyer, writer and First Lady of the United States who has a net worth of $11.8 million.Michelle Obama was born January 17, 1964 in Chicago, Illinois.ichelle Obama net worth: $11.8 Million. Michelle Obama Net Worth: Michelle Obama is an American lawyer, writer and First Lady of the United States who has a net worth of $11.8 million.
|14.88242
|5016431
|Name at birth: Natasha Obama. Sasha Obama is the younger daughter of former U.S. president Barack Obama. Her formal name is Natasha, but she is most often called by her nickname, Sasha. Sasha Obama was born in 2001 to Barack Obama and his wife, Michelle Obama, who were married in 1992.
|14.63069
|1939756
|Michelle Obama Net Worth: Michelle Obama is an American lawyer, writer and First Lady of the United States who has a net worth of Michelle Obama Net Worth: Michelle Obama is an American lawyer, writer and First Lady of the United States who has a net worth of $40 million. Michelle Obama was born January 17, 1964 in Chicago, Illinois. She is best known for being the wife of the 44th President of the United States, Barack Obama. She attended Princeton University, graduating cum laude in 1985, and went on to earn a law degree from Harvard Law School in 1988.
|14.230849
## Performance Evaluation
We compared the search performance of MyScaleDB under different indexes using
, including MyScaleDB’s implemented FTS index, ClickHouse’s built-in Inverted Index and the scenario with no index.
[clickhouse-benchmark](https://clickhouse.com/docs/en/operations/utilities/clickhouse-benchmark/)
### Benchmark Setup
#### Dataset Details
To test TextSearch performance, we utilized the
[ms_macro dataset](https://microsoft.github.io/msmarco/#ranking) provided by Microsoft. The
ms_macro dataset consists of 8,841,823 text records, which we converted to the parquet format for easy import into MyScaleDB. Additionally, we created a set of SQL files for testing search performance based on different word frequencies. The dataset we used is publicly available via S3:
[ms_macro_text.parquet](https://myscale-datasets.s3.ap-southeast-1.amazonaws.com/ms_macro_text.parquet): 1.6GB [ms_macro_query_files.tar.gz](https://myscale-datasets.s3.ap-southeast-1.amazonaws.com/ms_macro_query_files.tar.gz): 5.8MB
The
ms_macro_query_files.tar.gz file encompasses all the SQL files used in this test. The name of each SQL file indicates the frequency of the searched term in the
ms_macro dataset and the number of queries included in the SQL file. For example, the
ms_macro_count_hastoken_100_100k.sql file contains 100,000 queries, and the word in each query appears 100 times in the dataset.
The following are examples of
hasToken and
TextSearch queries:
#### Testing Environment
Despite our testing environment having 64GB of memory, MyScaleDB’s memory consumption during testing remains around 2.5GB.
|
Item |
Value
|System Version
|Ubuntu 22.04.3 LTS
|CPU
|16 cores (AMD Ryzen 9 6900HX)
|Memory Speed
|64GB
|Disk
|512GB NVMe SSD
|MyScaleDB
|v1.5
#### Import Data
To import the data, create a table for the
ms_macro dataset:
Directly import data from S3 into MyScaleDB:
Merge the data parts of
ms_macro into one to enhance search speed. Note that this operation is optional.
Output:
|
count()
|1
Verify
ms_macro contains 8,841,823 records:
|
1
|
SELECT count(*) FROM default.ms_macro;
Output:
|
count()
|8841823
#### Create the Index
We evaluated the performance of three types of indexes: FTS, Inverted and None (a scenario with no index).
- FTS index
1234-- Ensure that when creating the FTS index, no other index exists on the text column of ms_macro.ALTER TABLE default.ms_macro DROP INDEX IF EXISTS fts_idx;ALTER TABLE default.ms_macro ADD INDEX fts_idx text TYPE fts;ALTER TABLE default.ms_macro MATERIALIZE INDEX fts_idx;
- Inverted index
1234-- Ensure that when creating the Inverted index, no other index exists on the text column of ms_macro.ALTER TABLE default.ms_macro DROP INDEX IF EXISTS inverted_idx;ALTER TABLE default.ms_macro ADD INDEX inverted_idx text TYPE inverted;ALTER TABLE default.ms_macro MATERIALIZE INDEX inverted_idx;
- None index: Ensure that the text column of the
ms_macrotable does not contain any index.
#### Running the Benchmark
Use
clickhouse-benchmark to perform stress testing. For more usage instructions, refer to the
[ClickHouse documentation](https://clickhouse.com/docs/en/operations/utilities/clickhouse-benchmark).
|
1
|
clickhouse-benchmark -c 8 --timelimit=60 --randomize --log_queries=0 --delay=0 < ms_macro_count_hastoken_100_100k.sql -h 127.0.0.1 --port 9000
### Evaluation Results
When the frequency of the searched word is high (100,000 to 1 million), the acceleration effect of the skipping index is quite limited (only a tenfold improvement compared to performance without establishing an index). However, when the frequency of the searched word is low (100 to 1,000), the skipping index can achieve significant acceleration (up to a hundredfold improvement compared to performance without establishing an index).
The
TextSearch function, on the other hand, consistently outperforms both the skipping index and the inverted index across all scenarios. This is because
TextSearch directly leverages Tantivy’s full-text search capabilities, bypassing the need to scan through granules and instead retrieving results directly from the index. This results in a much faster and more efficient search process.
## Conclusion
Integrating Tantivy into MyScaleDB has significantly enhanced its text search capabilities, making it a powerful tool for text data analysis and RAG with large language models (LLMs). By addressing the limitations of ClickHouse’s native text search functions and introducing advanced features like BM25 relevance scoring, configurable tokenizers and natural language queries, MyScaleDB offers a robust and efficient solution for complex text search requirements.
The implementation of a C++ wrapper for Tantivy, the creation of a new skipping index and the introduction of the
TextSearch function have all contributed to this improvement. These enhancements not only boost MyScaleDB’s performance but also expand its use cases for efficient and accurate text search in various applications.
For more information on how to use the
TextSearch function and other features, refer to our documentation on
[text search](https://myscale.com/docs/en/text-search/) and [hybrid search](https://myscale.com/docs/en/hybrid-search/). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)