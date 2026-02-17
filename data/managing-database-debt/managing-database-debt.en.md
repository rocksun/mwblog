Technical debt is an inevitable byproduct of software development as complexity grows. However, unlike stateless application code, the stateful nature of databases makes this debt far easier to accumulate and significantly harder to pay off, sometimes taking weeks and even months of planning and execution.

Existing data creates massive inertia against change, and having different sets of data in different environments, from development to production, makes problems hard to predict. Add in the painful but unavoidable layers of compliance and safety restrictions in the path to production, and the slope becomes an even steeper climb.

Managing data for complex problems is tough, and there is no magical solution. But by investing in specific skills and reflecting on engineering practices, we can prevent our databases from becoming “debt-abases”.

The strategies below are based on my personal experience and opinions. You might nod along with some and disagree with others — and that is okay. Ultimately, you should make the most pragmatic choice based on your circumstances, not by norms.

## Know databases beyond the surface

Have you ever learned a concept and wished you had applied it sooner? In application code, mistakes or inefficiencies can often be fixed relatively easily. The same cannot be said for data or schema changes — or worse, the decision to swap out the entire database.

Knowing the internals of our chosen database helps us make good design choices regarding schemas, indexes, and queries early on. Understanding how our database handles concurrency, caching, indexing, and query execution eliminates the need for time-consuming digging, costly investigations, and disruptive changes later on.

On top of that, adding a new data store to our stack is REALLY costly. Beyond the obvious burden of maintenance and monitoring, developers face increased cognitive load and technical blind spots, which are breeding grounds for bugs.

Having in-depth knowledge allows us to squeeze the most out of our primary database before introducing another. Depending on our performance needs, a properly configured database might even [eliminate the need for an external sidecar cache](https://medium.com/mongodb/when-should-you-use-a-cache-with-mongodb-db0040d9c12c). Remember: modern databases have their own internal caches too.

## Design your data model (but do not over-engineer)

The data model is the foundation for how our queries are executed. Databases like [MongoDB](https://www.mongodb.com/docs/manual/data-modeling/), [Neo4j](https://neo4j.com/docs/getting-started/data-modeling/), and [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/data-modeling.html) all advocate for specific modeling principles tailored to their underlying engines. A good design must be driven by access patterns and specific internal database mechanics. Getting this right can [improve performance by an order of magnitude](https://www.mongodb.com/company/blog/mongodb-design-reviews-help-customers-achieve-transformative-results), preventing the need for desperate, reactive patches later on.

Data modeling isn’t just for NoSQL. If you are wondering, [YugaByteDB](https://docs.yugabyte.com/stable/develop/best-practices-develop/data-modeling-perf/) and [TigerDB](https://www.tigerdata.com/learn/data-modeling-on-postgresql) (both based on PostgreSQL) have also published their own sets of practices. With growing support for less-structured data and the increasing flexibility of RDBMS systems, schema design becomes even more relevant.

That being said, optimization sometimes comes with a significant overhead. Adhering to the Pareto Principle, in most applications, 20% of queries account for 80% of the database workload. We should prioritize and optimize those specific queries, and opt for the simplest design for the rest—as long as they meet basic performance needs.

## Rethinking testing strategies

We absolutely need automated tests to refactor queries with confidence. However, maintaining 100% unit test coverage for database interactions creates a massive overhead. It often requires seeding different datasets for every possible scenario, and reading the test setup code can be more difficult than reading the query itself.

In my opinion, most straightforward CRUD queries do not need isolated unit tests. They should be verified during development, but maintaining a suite of unit tests just to check if a SELECT \* works is a poor return on investment. Any unintended changes to these simple queries should be caught during code reviews. Instead, rely on higher-level overarching tests — Integration, API, or End-to-End (E2E) tests — to provide the necessary safety net.

**What *should* be unit tested?** We should focus on complex queries and edge cases that aren’t obvious to a team member reading our code. For large, complex queries, we can break them down into smaller logical pieces and test them independently.

* **MongoDB:** [Aggregation pipelines](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/) are naturally broken down by stages. This makes it easy to isolate specific transformations and test them independently without running the entire pipeline.
* **RDBMS:** Massive queries often become “black boxes.” Refactoring them into [Common Table Expressions (CTEs)](https://www.geeksforgeeks.org/sql/cte-in-sql/) or views allows us to decompose the logic into smaller, verifiable units.

Food for thought: Foreign key constraints are major setbacks for unit testing. You may intend to test a query on a single table, but strict foreign keys may require you to seed data across several other tables, irrelevant to your test. Do we really need hard database constraints for all relationships, or can we afford to have application-level checks or asynchronous updates to maintain the data integrity?

## Centrally manage “invisible functions”

Stored procedures and triggers are often “invisible” because they don’t live in the application source code. This makes them easy to miss, forget, or break.

Imagine this scenario: Developer A deploys a trigger to update a timestamp. Months later, Developer B writes a schema migration that inadvertently breaks the logic Developer A implemented. This breaking change might go undetected for weeks, leaving developers scouring the application logs for a “magical bug” without realizing the issue lies elsewhere.

I am not strictly against stored procedures and triggers. In my opinion, they should be centrally-managed by someone(s) if used. Someone with expertise and good oversight on the database must own the “database sanity” role to oversee these invisible functions during code reviews.

## Leverage on database schema validations

By “schema validation,” I mean enforcing both data structure and business logic. Having checks run by the database acts as a central control, critical for databases accessed by multiple services owned by different teams, where misalignment on requirements and release schedules can easily lead to dirty data.

In addition to basic structural validations, SQL databases support [CHECK CONSTRAINTS](https://www.w3schools.com/sql/sql_check.asp), which enable us to enforce regular expressions or value ranges directly on columns. MongoDB [JSON schema validation](https://www.mongodb.com/docs/manual/core/schema-validation/) allows us to enforce similar rules even on [polymorphic collections](https://www.mongodb.com/docs/manual/core/schema-validation/specify-validation-polymorphic-collections/) (collections that contain documents with different structures).

## Using ORMs and ODMs: A double-edged sword

Object-Relational Mappers (ORMs) and Object-Document Mappers (ODMs) add a layer of abstraction that allows developers to write queries in the language they are comfortable with. They also handle basic sanitization and validation.

However, abstractions come with “gotchas” when misconfigured or misunderstood. Unexpected behaviour can lead to unexpected results or performance (e.g., [the N+1 problem](https://www.pingcap.com/article/how-to-efficiently-solve-the-n1-query-problem)). Very often, these are harder to detect or fix because the actual query is hidden behind a method call, requiring you to dig deeper to analyze the exact statements or commands the underlying driver sent.

Furthermore, these abstracted mappers are rarely great at performing advanced queries or complex aggregations. For the sake of code consistency, we might be compelled to use the mapper’s idiomatic way of query, twisting the code into incomprehensible knots to produce a query that works. Often, it is simpler to write them as raw queries, and we need not shy away from bypassing the ORM or ODM.

## What’s next

Technical debt caused by databases is unforgiving. There is no silver bullet, but we can make conscious decisions to stop digging the hole deeper. By investing in database knowledge and adopting pragmatic strategies, we can keep this debt in check. Whether you are using a relational database or otherwise, the goal is to have a robust, well-oiled engine adaptable to change rather than a “debt-abase” that everyone is too terrified to touch.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/dd657c5c-cropped-b7246e45-screenshot-2026-02-10-at-14.21.34.png)

Wen Jie Teo serves as a Senior Developer Advocate at MongoDB, where he designs and delivers technical workshops both onsite and virtually, empowering developers to maximize the platform's capabilities. He regularly speaks at industry conferences, sharing best practices and challenging...

Read more from Wen Jie Teo](https://thenewstack.io/author/wen-jie-teo/)