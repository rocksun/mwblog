# Architect’s Guide to Apache Iceberg
![Featued image for: Architect’s Guide to Apache Iceberg](https://cdn.thenewstack.io/media/2025/05/01095a00-iceberg-1024x576.jpg)
[Apache Iceberg](https://iceberg.apache.org/) 1.9.0, released April 28, delivers a set of updates that do more than just extend its feature set. They signal something bigger: the gap between [Delta Lake](https://blog.min.io/delta-lake-minio-multi-cloud/?utm_medium=pr&utm_source=na&utm_content=blog&utm_campaign=2025_5_pr_na_ww_3rd-party-sites_data_Architects-Guide-to-Converging-Formats_blog) and [Iceberg](https://blog.min.io/the-definitive-guide-to-lakehouse-architecture-with-iceberg-and-aistor/?utm_medium=pr&utm_source=na&utm_content=blog&utm_campaign=2025_5_pr_na_ww_3rd-party-sites_data_Architects-Guide-to-Converging-Formats_blog) is closing. Features once exclusive to Delta Lake, like row-level operations with lineage, fast semi-structured data handling, are now available in Iceberg. And [Iceberg](https://thenewstack.io/snowflake-databricks-and-the-fight-for-apache-iceberg-tables/) is now supporting easier migration off Delta Lake, a sure sign that they are no longer competitors, but a victor inheriting the spoils.
Let’s explore what’s new in Iceberg 1.9.0, how it reflects Delta Lake’s historical advantages and what this convergence means for the future of the Lake house.

## Original Differences Between Iceberg and Delta
Originally, Iceberg and Delta Lake made [different architectural bets](https://thenewstack.io/architects-guide-to-a-reference-architecture-for-an-ai-ml-data-lake/).

Delta Lake prioritized performance early, optimizing tightly around Parquet and Spark with a transaction log model. Iceberg, on the other hand, focused on long-term data organization — things like building a format-agnostic table spec, introducing snapshot-based versioning and defining a layered metadata hierarchy. Delta used flat transaction logs; Iceberg used manifest trees. Delta required Parquet; Iceberg supported multiple formats like Avro, Orc and of course Parquet. These distinctions gave each project a unique edge.

With Iceberg 1.9.0, however, the story shifts. [Iceberg is closing performance gaps](https://thenewstack.io/snowflake-databricks-and-the-fight-for-apache-iceberg-tables/) while preserving architectural clarity. Delta is adding compatibility layers. What once were differentiators are now shared capabilities.

## Iceberg 1.9.0: What’s New?
### Enhanced Row-Level Operations
Iceberg 1.9.0 allows the coexistence of equality deletes and row-lineage tracking. This advancement enables precise deletion of rows based on specified conditions and assignment of unique row IDs to inserted or updated rows, facilitating accurate data versioning and auditing.

Delta Lake has long supported this kind of row-level mutation and lineage tracking. Iceberg now matches that capability, closing one of the functional gaps between the two.

### Delta Lake to Iceberg Migration
Iceberg offers a structured approach to migrating from Delta Lake through the `iceberg-delta-lake`
module. This module provides the `snapshotDeltaLakeTable`
action, enabling the creation of an Iceberg table that references the data files of an existing Delta Lake table without data duplication. It also supports maintaining the transactional history during migration, ensuring continuity in data operations.

The result is a more direct and efficient way to move from Delta to Iceberg and a clear sign that Iceberg is becoming the dominant open table format.

### Variant Data Type Support
Iceberg 1.9.0 introduces a `variant`
logical type for storing semi-structured data (like JSON) in a binary format. This avoids the performance overhead of parsing and storing JSON as strings.

The idea comes directly from Delta Lake, which introduced the same feature to improve query performance by up to [eight times in benchmarked scenarios](https://www.databricks.com/blog/introducing-open-variant-data-type-delta-lake-and-apache-spark). Iceberg adopting this capability makes it a viable option for low-latency workloads with semi-structured data like involving logs and events.

### Native Geospatial Support
Iceberg 1.9.0 adds a new `geometry`
logical type, enabling efficient storage and querying of spatial data sets. Key features include:

- Support for Well-Known Binary (WKB) encoding.
- Default Coordinate Reference System (CRS) set to OGC:CRS84.
- Multidimensional support for XY, XYZ, XYM and XYZM coordinate formats.
- Optional spatial statistics like bounding boxes to enhance query performance and spatial indexing.
This geospatial model aligns with the GeoParquet specification, ensuring compatibility with open data standards. It’s an example of Iceberg — and by extension the data community — circling around a common standard.

### REST Catalog: More Enterprise-Ready
Improvements to REST catalog authentication include:

- Support for pluggable authentication handlers.
- Clearer separation between auth and request logic.
- Expanded testing for enterprise identity systems.
This is a foundational update for production-grade deployments that use the Iceberg REST catalogs for multiengine or multi-tenant environments, a very [common use case](https://blog.min.io/the_way_of_the_cloud/?utm_medium=pr&utm_source=na&utm_content=blog&utm_campaign=2025_5_pr_na_ww_3rd-party-sites_data_Architects-Guide-to-Converging-Formats_blog) in enterprise data lakehouse deployments.

### Deprecating the Past: Hadoop 2 and Spark 3.3 Dropped
Support for Hadoop 2 and Spark 3.3 has been removed. This isn’t just house cleaning: it’s a signal. If you’re still tied to legacy Hadoop infrastructure, it’s time to plan your [exit](https://min.io/solutions/hdfs-migration?utm_medium=pr&utm_source=na&utm_content=blog&utm_campaign=2025_5_pr_na_ww_3rd-party-sites_data_Architects-Guide-to-Converging-Formats_blog). Iceberg is moving forward with modern runtimes, cloud native storage and scale-out compute.

### Other Notables
**Partition statistics APIs:**Exposes partition-level metadata for better planning and pruning.**Nanosecond timestamp support:**Extended precision for Parquet backends.**InternalData API:**Improved integration paths for engines like Spark, Flink and Trino.
You can find the full release notes [here](https://github.com/apache/iceberg/releases/tag/apache-iceberg-1.9.0).

## Convergence Is Good for Everybody
Delta Lake has long been the default choice for Databricks users. But since [Databricks acquired Tabular](https://blog.min.io/modern-data-architectures-with-iceberg-and-tabular/?utm_medium=pr&utm_source=na&utm_content=blog&utm_campaign=2025_5_pr_na_ww_3rd-party-sites_data_Architects-Guide-to-Converging-Formats_blog), the catalog company founded by Iceberg’s creators, the future of open-table formats looks a lot more unified.

Iceberg is gaining the performance and usability features that made Delta Lake popular while staying true to its [architectural clarity](https://thenewstack.io/the-architects-guide-a-modern-data-lake-reference-architecture/): independent catalog support, spec-driven evolution and openness. Delta Lake is starting to expose REST interfaces and compatibility layers like [UniForm](https://docs.databricks.com/aws/en/delta/uniform).

This is convergence. And it’s good for everyone building on top of lakehouses. Organizing around standards lowers the cognitive and operational overhead for teams adopting or migrating lakehouses. Which [means that data engineers](https://thenewstack.io/what-does-the-modern-data-stack-actually-mean/), architects, analysts and AI engineers don’t have to relearn tools, platforms or functionality. When things work the way you expect them to, everything is easier.

## Why Storage Matters
If the storage can’t keep up, nothing else matters.

Iceberg depends on fast scans, fast metadata operations and high throughput.

Modern object-storage is designed for that. It runs on commodity hardware and deploys to private clouds, data centers, colos or edge locations, all while delivering the best performance on the least amount of hardware. The economics of a private cloud Iceberg deployment is unbeatable: no egress fees or cost for GETS and PUTs means you can scale up as far and fast as you need without worrying about a sky-high cloud bill. Not to mention that the most secure deployments are still those in airgapped deployments.

Storage isn’t the exciting part of the stack, but if it’s too slow, too expensive or not safe enough, everything else falls through.

## The Path Forward
The convergence of Delta Lake and Iceberg isn’t about one winning over the other. It’s about the ecosystem maturing. As both projects evolve to adopt each other’s strengths, the real winner is the user. Teams can now choose tools based on architectural fit and operational goals, not just feature checklists or vendor alignment.

This shift pushes the industry toward greater interoperability, more open standards and simpler decisions. It lowers switching costs, encourages best practices and frees teams to focus on building reliable, high-performance data systems rather than navigating format silos.

This is progress.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)