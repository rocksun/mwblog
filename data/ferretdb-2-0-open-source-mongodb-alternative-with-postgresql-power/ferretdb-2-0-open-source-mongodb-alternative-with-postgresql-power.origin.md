# FerretDB 2.0: Open Source MongoDB With PostgreSQL Power
![Featued image for: FerretDB 2.0: Open Source MongoDB With PostgreSQL Power](https://cdn.thenewstack.io/media/2025/03/5e5b11c1-ferretdb-1024x683.png)
A new project from the founders of [Percona](https://www.percona.com/?utm_content=inline+mention), [FerretDB](https://www.ferretdb.com/) has set out to offer an open source alternative to the MongoDB NoSQL documented-oriented database system.

FerretDB is not a fork, nor a rewrite of [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention). Rather, it is a proxy that converts MongoDB 5.0+ wire protocol queries to SQL. It runs on a stock version of [PostGreSQL](https://thenewstack.io/postgresql-17-gets-incremental-backup-sql-queries-for-json/).

The FerretDB system also can serve as an on-premises alternative for MongoDB-compatible cloud services, notably [Microsoft CosmosDB](https://thenewstack.io/microsoft-introduces-cosmo-db-globally-distributed-multi-mode-azure-database-service/) and [DynamoDB](https://thenewstack.io/dynamodb-when-to-move-out/) from [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) ([Google Cloud](https://cloud.google.com/?utm_content=inline+mention) itself offers [MongoDB Atlas](https://thenewstack.io/mongodb-atlas-finally-gets-a-command-line-interface/), the commercial cloud version of MongoDB).

On Tuesday, the company released version 2.0 of [the open source software](https://github.com/FerretDB/FerretDB), which comes with a considerable performance boost thanks to the inclusion of the [DocumentDB extension](https://github.com/microsoft/documentdb) for PostgreSQL — courtesy of [Microsoft ](https://news.microsoft.com/?utm_content=inline+mention) — as a database engine.

Also, the DocumentDB extension, which provides support for the [BSON (Binary JSON) data type](https://www.mongodb.com/resources/basics/json-and-bson#:~:text=BSON%20stands%20for%20%E2%80%9CBinary%20JSON,more%20quickly%20compared%20to%20JSON.), provides the ability to query document data through SQL.

In effect, FerretDB can turn any Postgres database system into a MongoDB service provider.

## Open Source Is Important
FerretDB isn’t designed to serve as a drop-in replacement for all [MongoDB instances](https://thenewstack.io/5-reasons-to-run-mongodb-on-kubernetes/) — especially not for those that utilize the[ advanced proprietary features](https://thenewstack.io/mongodb-unveils-managed-graphql-for-mongodb-atlas/) — but should work for about 80% of workloads, estimated FerretDB co-founder and CEO [Peter Farkas](https://www.linkedin.com/in/farkasp/), in an interview with TNS.

It also works with most third-party MongoDB tools and drivers.

Farkas founded FerretDB with [Peter Zaitsev](https://peterzaitsev.com/) and [Alexey Palazhchenko](https://www.linkedin.com/in/alexeypalazhchenko/). Zaitsev was one of the confounders of Percona, a company that specializes in offer [high performance support](https://thenewstack.io/percona-backs-valkey-with-enterprise-grade-support/) for databases such as [MySQL](https://thenewstack.io/upgraded-mysql-crashes-on-restart-percona/), MongoDB and ValKey. Palazhchenko and Farkas were also early employees of Percona.

Originally, MongoDB found a home with Web developers as an easy, very scalable, way to store data. Mongo used the more dev-friendly [ JSON format](https://thenewstack.io/working-with-json-data-in-python/) to store data in a document-oriented model, which is easier to work with than SQL schema-defined columns and rows, especially with complex nested data.

In 2018, MongoDB changed the license of its namesake document store to a more restrictive [SSPL license](https://www.mongodb.com/legal/licensing/server-side-public-license) ([from GPLv3](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)) largely as an effort to thwart cloud providers from offering MongoDB capabilities without giving back to the projector paying Mongo (a similar situation [Reddis](https://redis.com/?utm_content=inline+mention) found itself in several years later).

Kicking off this project in 2021, the three Percona expats had suspected that many MongoDB users required an open source licensed edition. They may work for an organization that is building its software stack on purely [open source software](https://thenewstack.io/open-source/). Or they may want an open source on-premises backup for cloud providers, Farkas explained.

## The OpenDocDB Standard
Many users may not want to run critical systems on a open source project that is controlled by a single company. Recognizing this, the company has stood up the [OpenDocDB](https://opendocdb.org/about) initiative, with the hopes of attracting a development community around FerretDB.

The idea is that just as SQL has become a vendor-neutral standard for querying structured data, so too could OpenDocDB, building from the [MongoDB API](https://www.mongodb.com/products/tools/mongodb-query-api), become a standard for querying document-oriented databases.

Following the [Percona playbook](https://www.percona.com/about), FerretDB itself plans to make money from offering tools and advanced enterprise features, a cloud service, and premium support for highly-availability mission-critical deployments.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)