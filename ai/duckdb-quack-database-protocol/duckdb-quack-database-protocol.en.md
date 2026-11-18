![In this episode of The New Stack Podcast, Guillermo Sánchez Dionis, product lead at DuckLabs, explains how Quack addresses the limitations of traditional database protocols, which often introduce unnecessary overhead and inefficient data serialization.](https://cdn.thenewstack.io/media/2026/11/dcee749a-for-thumbnail-26-1024x576.png)

**Older database protocols were built before big data.** Some still send results row by row, repeating details like column names and types with every row. The result, says [DuckLabs](https://ducklabs.com/) product team lead [Guillermo Sánchez Dionis](https://www.linkedin.com/in/guillermo-s%C3%A1nchez-dionis/), is “quite a bloated message.” That overhead adds up when you’re moving large query results.

DuckDB’s answer is [Quack](https://duckdb.org/quack/), an HTTP-based protocol that streams query results in batches of column data as DuckDB produces them. It was previewed in May and was released in October as part of DuckDB 2.0.0 LTS.

VIDEO

On this latest episode of *The New Stack* podcast, recorded at DuckLabs headquarters in Amsterdam, Sánchez Dionis explains how that design lets developers start working with results while a query is still running.

A database protocol is a formal set of rules and message formats that dictates how a client application communicates with a database server. It acts as a specialized language that lets a software application securely send SQL queries, receive structured data tables, and manage transactions over a network. It handles connection and authentication, query packaging, data serialization, and error management.

But according to Sánchez Dionis, most protocols were designed pre-big data for other types of systems, with serialized rows rather than columns. They also add a lot of unnecessary data, he says, like column types and column names per row.

“It becomes quite a bloated message. That already makes the protocol not only not good for analytical systems, but it’s also quite heavy,” he contends. As protocols evolved for analytical systems, they did start using columns, but “they were still doing things like serializing one value at a time and other things that are really not efficient. Modern systems are trying to converge on using vectorized execution to be able to serialize more values at a time and trying to use more efficient representations of columnar data formats to send over the wire.”

All while the Quack protocol, he says, is aiming for a different, highly efficient approach.

Quack is DuckDB’s HTTP-based client/server protocol, with its first production release shipping in DuckDB 2.0.0 on Oct. 21. Not only does this signal Quack moving out of the preview stage, but the protocol now offers certain developer-friendly features:

* The CONNECT statement allows developers to attach to and query a remote Quack server via standard SQL commands.
* The new -serve CLI argument instantly starts a Quack server instance from the command line, and -connect connects to one.
* Multiple clients can write to the same database concurrently, with transactions handled under DuckDB’s multi-version concurrency control (MVCC) isolation.

“Quack uses DuckDB’s data chunks — which is our columnar representation of data. We also serialize in a very efficient manner because we are a vectorized engine. We also make sure that we send the results in a streaming fashion,” Sánchez Dionis explains.

“One of the most important things is tightly coupling the engine. Once you start producing results, instead of waiting for the query execution to end and then serializing all of the results at once, you serialize and send results as they are emitted by the engine. Therefore, the client can keep consuming results without having to stop the engine.”

For developers, he says, that means they don’t have to do anything.

> “I think the biggest advantage that you will see is you will have a very small memory footprint”

“You run a query from the comfort of your laptop, and you just get streaming results back. I think the biggest advantage that you will see is you will have a very small memory footprint,” he says. “What’s cool about Quack is that you install and load it wherever you are. You can also create another client on the [same] laptop with the Quack extension, and they will communicate with each other.”

Then, the scale of how many DuckDB servers is up to you and your team. And the overhead of running it on that server is next to none, Sánchez Dionis continues, as it’s Quack’s biggest efficiency gain yet.

More Quack improvements are expected in upcoming DuckDB 2.0 patch releases, as the DuckLabs team looks to build stability on the server side.

The post [DuckDB has an answer to “bloated” database messages](https://thenewstack.io/duckdb-quack-database-protocol/) appeared first on [The New Stack](https://thenewstack.io).