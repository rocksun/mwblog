# Deep Dive into Columnar Databases: What Makes Them Shine
![Featued image for: Deep Dive into Columnar Databases: What Makes Them Shine](https://cdn.thenewstack.io/media/2025/02/c6ba388a-tom-podmore-70ru5lg28me-unsplash-1024x674.jpg)
[Tom Podmore](https://unsplash.com/@tompodmore86?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/white-concrete-building-with-glass-windows-70rU5lg28ME?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
Columnar storage has emerged as a game-changer in the data engineering and analytical landscape. It offers significant performance advantages over traditional row-oriented databases.

The idea of storing data in columns is not new. It was first introduced comprehensively in 1985 by GP Copeland and SN Khoshafian. Their paper, *“*[A Decomposition Storage Model (DSM)](https://dl.acm.org/doi/10.1145/971699.318923),” proposed storing data in binary relations, pairing each attribute value with the record’s identifier. This approach organized data by columns rather than rows, offering simplicity and retrieval performance advantages for queries involving a subset of attributes. However, it required more storage space overall.

Researchers started developing [MonetDB in 1999](http://sites.computer.org/debull/A12mar/monetdb.pdf) and released it as an open-source project in 2004. It became one of the first systems to embrace columnar architecture for analytical workloads and showcase its effectiveness. [C-Store](https://dl.acm.org/doi/10.5555/1083592.1083658), developed in the mid-2000s, marked another crucial milestone. It introduced advanced concepts that are now standards in modern columnar storage systems.

Developments in this area accelerated in the late 2000s and early 2010s, with projects like [Apache Parquet](https://parquet.apache.org/) (influenced by [Google’s Dremel paper](https://research.google/pubs/dremel-interactive-analysis-of-web-scale-datasets-2/)) bringing columnar storage to the Hadoop ecosystem.

**The Core Concept: Columnar vs. Row-Oriented Storage**
Traditional row-oriented [databases store all data for a single row together](https://thenewstack.io/how-open-source-and-time-series-data-fit-together/). A row signifies an entity you want to model. From that perspective, and for this post, consider a document-oriented [database like MongoDB](https://thenewstack.io/how-to-plan-your-mongodb-upgrade/) row-oriented since it stores the entire document (entity) together, similar to row-oriented databases. In contrast, columnar data stores organize data in columns, each containing values for a single attribute across all rows. This seemingly simple change has profound implications for performance.

**Predicates and Projections in Query Processing**
There are two key concepts to understand when discussing transactional and analytical systems:

**Predicates**are the conditions by which you filter the entities (rows) you want (think of them as a`WHERE`
clause in an SQL query).**Projections**are the fields (columns) you want in the response (think of them as the names you define in a`SELECT`
statement).
If you think of your [data as a list of rows vertically stacked](https://thenewstack.io/the-architects-guide-to-the-modern-data-stack/), predicates slice it horizontally, and projections slice it vertically.

Transactional queries often rely on predicates to filter rows, with projections spanning the entire row (e.g., `SELECT * FROM orders WHERE user_id = 1234`
). In contrast, projections in analytical queries involve a small subset of fields from the entity being queried (e.g., `SELECT user_id, name, num_orders FROM user_aggregates WHERE user_id = 1234`
).

Consider a table with 50 columns and millions of rows. In a row-oriented system, if you need only three columns, the database would still have to read all 50 columns for each row. With columnar storage, only the three relevant columns are accessed, massively reducing the I/O overhead, i.e., the amount of [data processed in analytical](https://thenewstack.io/clickhouse-optimizing-real-time-data-analysis-with-online-analytical-processing/) queries.

**Key Techniques Powering Columnar Stores**
Storing data in columns [enables various optimizations that significantly improve query performance](https://thenewstack.io/enhancing-the-flexibility-of-sparks-physical-plan-to-enable-execution-on-various-native-engines/). Here’s a mental model: Think of query execution as a [pipeline that passes data](https://thenewstack.io/leaky-data-pipelines-uncovering-the-hidden-security-risks/) through various stages, transforming it at each step. The smaller the data, the lower the cost and the faster the pipeline.

[Reducing the data](https://thenewstack.io/nvme-of-substantially-reduces-data-access-latency/) you work with can be done in several ways:
**Efficient data representation**(data compression, column-specific compression)**Filtering data early**(column pruning, predicate pushdown)**Expanding data as late as possible**(direct operations on compressed data, late materialization)**Faster data processing**(vectorized execution, optimized joins)
These techniques are interconnected and rely on each other for maximum performance gains.

**Data Compression and Column-Specific Compression**
Columnar [storage enables high compression ratios because data](https://thenewstack.io/getting-started-with-python-and-influxdb/) within a single column is of the same type and exhibits similar patterns. Techniques such as **dictionary encoding, run-length encoding (RLE), bit packing, and delta encoding** are commonly used in modern columnar stores.

For example, in a web analytics [database tracking the source](https://thenewstack.io/cockroach-rescinds-open-core-for-a-free-enterprise-version/) of user traffic, the

*source*column typically has a small set of unique values. This allows:
**Dictionary encoding**: Assign integer values to string values (e.g., email = 1, Twitter = 2).**Run-length encoding (RLE)**: If consecutive entries have the same value, store them as (value, count).**Bit packing**: If only a few unique values exist, use fewer bits per value instead of a full integer.
**Column Pruning**
Column pruning eliminates unnecessary columns from query execution. Consider the query:

`SELECT first_name, last_name, email, phone FROM users WHERE num_orders > 10`
If the table has 100 columns but the query needs only five, column pruning reduces the I/O overhead by 95%.

**Predicate Pushdown**
Predicate pushdown filters data as early as possible in the query execution pipeline. By using **zone maps** (metadata that tracks min/max values within storage blocks), databases can skip entire blocks that don’t match the filter criteria.

For example, in the query:

`SELECT name FROM users WHERE age > 30 AND city = 'New York'`
A columnar database can first filter blocks based on metadata before scanning individual rows, reducing unnecessary processing.

**Direct Operation on Compressed Data**
Columnar databases can perform operations directly on compressed data, minimizing I/O costs. Consider the query:

`SELECT sum(salary) FROM employees WHERE department = 1002`
Using dictionary encoding and RLE, only relevant [data is read and expanded](https://thenewstack.io/snowflake-consolidates-platform-expands-ai/) at the final step, significantly improving performance.

**Late Materialization**
Late materialization defers loading unnecessary columns until needed. In the query:

`SELECT name FROM users WHERE age > 30 AND city = 'New York'`
Only age and city are processed initially, and the name column is loaded at the final stage.

**Vectorized Processing**
SIMD (Single Instruction, Multiple Data) allows processors to execute operations on multiple values in parallel. Consider:

`SELECT sum(price) FROM sales WHERE user_id = 1234`
Instead of evaluating user_id row-by-row, SIMD compares 256 values at a time, leading to significant speedups.

**Efficient Join Implementations**
Columnar [databases implement advanced join techniques like semi-joins using bloom filters](https://thenewstack.io/why-jiocinema-skipped-redis-for-recommendation-bloom-filters/). These structures allow databases to efficiently check whether a value exists in a dataset, reducing unnecessary comparisons.

For example, in the join:

123 |
SELECT * FROM orders o JOIN customers c ON o.customer_id = c.idWHERE c.region = 'EMEA' |
A bloom filter is built for valid customers, allowing the database to quickly discard irrelevant orders.
**Conclusion**
Columnar data stores provide:

**Storage efficiency**through compression**Reduced I/O**via column pruning and predicate pushdown**Faster execution**using vectorized processing and optimized joins
They are widely used in web analytics, business intelligence, machine learning infrastructure, and real-time analytics.

If you’re a data practitioner, understanding these internals can help you optimize performance. If you’re an engineering leader, these techniques will help you evaluate trade-offs and make strategic decisions for your organization.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)