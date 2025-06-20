![](https://cdn.thenewstack.io/media/2025/06/34d563f2-russell_spitzer-150x150.jpg)

Russell Spitzer

Version 3 of Apache Iceberg has been released. A number of features have been added that expand the flexibility of the data table format, including a few much-requested data types, faster deletes, row lineage and default values for NULL types.

This new version —  as well the v4 version the core development team is about to start on — will better equip Iceberg for new types of use cases, explained [Russell Spitzer](https://www.russellspitzer.com/about/index.html), a program manager for [Apache Iceberg](https://iceberg.apache.org/terms/).

As an open data format, Apache Iceberg has been instrumental in the creation of [data lakehouses](https://thenewstack.io/showdown-at-the-lakehouse-databricks-muscles-up-with-tabular/), which combine multiple sources of structured and unstructured data for large-scale analysis. It uses a sophisticated set of metadata to keep track of the tracks of the changes in the different files it indexes.

Iceberg, along with a good metadata store, keeps track of a schema as it evolves, which gives users more flexibility in updating the schema while maintaining the ability to query older data. It can do time travel and rollbacks. It can also scale without users worrying about partitions.

Apache Iceberg is both a set of specifications as well as a number of reference implementations. There is a view specification, a REST specification for how to communicate with the server. It also includes a specification for [Puffin file format](https://iceberg.apache.org/puffin-spec/) for storing indexes, statistics and other data bits that can’t be stored within an Iceberg manifest. There is also a range of implementations written in different languages (Java, Python, Rust, Go, C++), and based on different platforms such as [Apache Spark](https://thenewstack.io/architects-guide-to-apache-iceberg/) and [Apache Flink](https://thenewstack.io/a-developers-guide-to-getting-started-with-apache-flink/).

![](https://cdn.thenewstack.io/media/2025/06/fb5ec95c-iceberg-diagram.jpg)

![](https://cdn.thenewstack.io/media/2025/06/72d8f51e-iceberg-01-300x225.jpg)

Spitzer

Spritzer, along with [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) Senior Manager of Developer Relations [Danica Fine](https://www.linkedin.com/in/danica-fine/), held an explanatory session about [Iceberg version 3 specification](https://iceberg.apache.org/spec/#version-3-extended-types-and-capabilities) at the annual [Snowflake Summit](https://thenewstack.io/snowflake-streamlines-data-analysis-for-enterprise-ai/) held earlier this month in San Francisco. The new features they covered included:

* Deletion vectors
* Variant type
* Geometric type
* Row lineage
* NULL default values

## Deletion Vectors

Fine explained that when it comes to deleting data, Iceberg has two avenues: copy-on-write and merge-on-read. **Copy-on-write** simply makes a copy of whatever file is being changed minus whatever row(s) that needed to be deleted; **merge-on-read** keeps the original but then makes a deletion file, noting the contents to be removed. Deletes can be all instances of a value (equality delete) or just one in a specific location (position delete).

Position delete can pose a quandary though. You can have one file capture all deletes in a partition, or have a file of deletes for each file. And so the admin was confronted with understanding and making the appropriate trade-offs to optimize speed of access.

![](https://cdn.thenewstack.io/media/2025/06/b99469c5-iceberg-delete-1024x768.jpg)

For v3, position delete files will be replaced with highly performant Puffin files. Puffin has been repurposed for storing deletion files as well. Each file will get its deletion vector.

“You’re going to see a lot less maintenance tasks on your end. You don’t have to actually go through and consolidate your data,” Fine said.

## New Data Types

New data types abound in v3.0.

First up is the [Variant type](https://github.com/apache/iceberg/issues/10392), which provides a binary support format for storing semi-structured data, such as [JSON](https://thenewstack.io/an-introduction-to-json/). It allows you to change the type of data you’re ingesting without changing the schema. Variants can be extended with multiple values.

Snowflake itself already supported variant types, so it made sense to extend that to Iceberg, said Spitzer.

![](https://cdn.thenewstack.io/media/2025/06/3e0c2a4b-iceberg-variant-1024x768.jpg)

“Variants are really great for a lot of different things,” he said. You get “all the benefits of having a structured type while still having the flexibility of being able to store just about anything you want in every single cell.”

As an example, he pointed to using variant types to capture data from [Internet of Things deployments](https://thenewstack.io/enterprise-challenges-for-the-internet-of-things/). Think of a sensor that provides latitude and longitude values, but also error codes.

The end user will need to write the variant type into the engine (and/or apps) writing data to the Iceberg columns. Soon, you will also be able to [shred variant types](https://github.com/apache/parquet-format/blob/master/VariantEncoding.md) into proper [Parquet columns](https://thenewstack.io/an-introduction-to-apache-parquet/) for faster analysis, though that is not supported quite yet.

The release also offers a couple of new geometric data types as well. The geotype options unlock a lot of functionality: Geometry captures two-dimensional surfaces, and Geography can be used for three-dimensional and spherical objects (this type will be available later this summer).

The geotypes will only be available to new columns — you can’t backport the data type to existing columns, Fine warned. User code will also have to be revamped to enjoy the new data types.

## Row Lineage

Row lineage is another feature that came from Snowflake, and is actually used in many of Snowflake’s functions, Spitzer said.

Row lineage provides a way to check each row of a table for changes: when the data was changed, and what it was changed from (“[Change Data Capture](https://thenewstack.io/change-data-capture-for-real-time-access-to-backend-databases/)“). Basically, row lineage allows you to audit your data changes.

“This is something that you simply could not do before in Iceberg tables,” Spitzer said. “We built a bunch of code to try to approximate this with CDC views, but you really just couldn’t ever know for sure what happened to a single row and where it came from.”

Two new metadata columns capture this activity: one for the row updated, and the other for the last snapshot that row was updated.

Row lineage is turned on automatically for Iceberg v3.

![](https://cdn.thenewstack.io/media/2025/06/811349ff-iceberg-row-1024x768.jpg)

## Null Default Values

NULL, NULL, NULL. Devs hate Nulls. Nulls are all over Iceberg tables. The problem was that there was no default value for nulls in Iceberg. When it comes to calculation time, how do you math?

Now the Iceberg provides a way to change all the missing values into a set value, before calculations are made.

So the Null gets two new parameters. One is `initial-default`. This will be the value that will replace NULL After the upgrade, the first time the engine scans the table, it will replace NULLs with the `initial-default`. The idea is that you set the `initial-default` once and forget about it.

There is also a `write-default`, which adds in the specified value when a NULL is written to the table. This can be changed at any time.

“The reason that there’s two different defaults is that the moment you’ve done that and a row is compacted or moved to a different file, the value that used to be null is now written as a real value, so you can’t change it a second time,” Spitzer explained.

## Beyond v3: Streaming and Low-Latency

Those who upgrade to a Apache Iceberg v3 table will need a v3-compliant engine, and some of the updates will require changes to the code that operates on Iceberg.

The working groups are already starting up on Iceberg version 4, Spitzer said. Proposals for new features are being circulated on the mailing list.

“We’re looking at a whole bunch of things to try to make Iceberg a better table format for use cases that currently it’s not great at,” Spitzer said in a follow-up interview with TNS.

These include small tables and tables with lots of updates. They are looking a ways to better accommodate streaming applications, and they want to lower latency in general. This would involve reducing the number of writes to the metadata layer.

## Apache Polaris Nears a Big Release Too

Although originally developed at Netflix and subsequently maintained by [Dremio](https://www.dremio.com/resources/guides/apache-iceberg/), Iceberg has received quite a bit of open source help from Snowflake — in terms of engineering time and even certain features that Snowflake originally developed in-house for its own data formats.

Last year, Snowflake [released as open source](https://thenewstack.io/the-open-format-movement-heats-up-snowflake-embraces-apache-iceberg/) its own REST catalog it had developed for Iceberg, [called Polaris](https://thenewstack.io/snowflake-polaris-aims-for-multiquery-engine-interoperability/). Iceberg requires a metadata catalog to centralize metadata management, governance and access control for Iceberg tables.

The idea was to “abstract away commit logic from the client and have them in a central server location,” Spitzer said. The catalog often relies on a database for the actual persistence layer. Snowflake’s own commercial Polaris implementation, [Open Catalog](https://www.snowflake.com/en/product/features/open-catalog/), uses [FoundationDB](https://thenewstack.io/foundationdb-a-reliable-key-value-store-with-acid-compliance/). 

The version one release of Polaris will happen “soon,” Spitzer said. Last minute adjustments are being made for production and security assurances. The software had a lot of Snowflake-specifics that needed to be changed out.

And, of course, the software must be scalable.

“There’s folks who want to use it for their own internal organizations, where 20 transactions-a-second on the catalog is more than enough. But we have some people who want to run it as a service, or run it for a huge organization, where you need to handle thousands of transactions a second. It’s probably very rare, but we want to make sure that it scales up to that,” he said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 25 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)