# Want Real Time? Run Scripts Inside the Database
![Featued image for: Want Real Time? Run Scripts Inside the Database](https://cdn.thenewstack.io/media/2024/09/ec2ce051-database-1024x576.jpg)
The decision about where to run your scripts can significantly affect system performance, efficiency and overall architecture. Traditionally, enterprises have relied on separate application servers, but many also choose to execute scripts directly [inside the database](https://thenewstack.io/data/). This approach can streamline your data operations and decrease latency.

By leveraging the power of the database engine itself, these scripts can efficiently perform complex multistep operations that would be difficult to accomplish with single queries. Scripts can be called by transactions to ensure data consistency or apply business rules. Scripts can contain loops and conditions that can’t be added to a SQL query. Performance can also improve because, unlike an external application, internal scripts do not incur network overhead; they can be compiled, and execution plans can be cached for better performance.

## Comparison With Traditional Approaches
Traditionally, many applications separated the data layer (database) from the application logic layer (application server) — scripts run on the application server, which then communicates with the database to fetch or manipulate data. While this architecture has its merits, it also introduces potential inefficiencies, especially when dealing with [large volumes of data](https://thenewstack.io/processing-large-data-sets-in-fine-grained-parallel-streams-with-sql/) or complex operations.

Transferring large data sets between the database and application server can be network-intensive and time-consuming, while multiple round trips between the database and the application server can become bottlenecks.

## The Power of Proximity: Impact on Performance and Efficiency
One of the primary advantages of running scripts inside the database is the proximity to the data itself, which translates into significant performance benefits and improved efficiency.

### Example: Data Transformation On the Fly
Let’s consider a scenario where we need to query, sort and transform data on the fly. We’re going to query for customers, order customer records by the total amount purchased, then assign each to a loyalty tier. Naturally, we want this to happen as fast as possible.

#### Without Internal Scripting:
- The application server sends a query to the database to retrieve the raw data.
- The database returns the result set to the application server.
- The application server processes the data (sorting, transforming, etc.)
- If updates are needed, the application server sends update queries back to the database.
This approach involves multiple round trips between the application server and the database, potentially introducing network latency and increasing overall processing time.

#### With Internal Scripting:
In this case:

- The entire operation is performed within the database.
- No data needs to be transferred to an external server.
- The database’s internal optimizations can be leveraged for better performance.
The simplicity, performance and operational ease of the internal scripting approach are evident. Everything happens in one place, reducing complexity and potential points of failure.

## Performance Benefits in Detail
As mentioned, running scripts inside a database engine offers significant performance advantages by eliminating the need for data to travel back and forth across the network between the database cluster and the application server. This reduces latency and alleviates potential issues that unpredictable delays can cause in distributed systems.

Internal scripts also can take advantage of database-specific features and optimizations that may not be available for access externally. This includes low-level access to indexing structures, statistics and other internal mechanisms that make efficient use of CPU, memory, and I/O to significantly boost performance. In addition, modern databases employ sophisticated query planning and optimization techniques. Internal scripts benefit from these optimizations automatically, leading to better performance without requiring manual tuning or optimization by developers.

## Improved Resource Utilization
Direct access to the database engine enables it to optimize resource utilization based on the tasks the script completes and the current system load. For instance, the database can [efficiently manage memory allocation](https://aerospike.com/blog/hybrid-memory-architecture-optimization/?utm_source=byline&utm_medium=pr&utm_campaign=thenewstack) for large datasets, use parallel processing capabilities for complex calculations and optimize I/O operations for data retrieval and storage.

## Development and Maintenance Efficiency
A centralized approach to scripting simplifies maintenance and updates to business logic, as changes can be made in one location rather than across multiple application layers running on separate servers. A simple n-tier architecture might have separate servers for UI/presentation/web tier, business logic tier, data access tier and a database. By consolidating data processing logic within the database, organizations can simplify the overall system architecture, reducing the number of components that need to be managed and maintained down to the UI tier and database tier. A simpler system architecture leads to easier troubleshooting and maintenance.

One of the key advantages of this approach is the ease of debugging and troubleshooting. When scripts run inside the database, debugging can often be done directly within the database environment, simplifying the process of identifying and fixing issues. This integrated debugging capability allows developers to trace script execution, examine [data states and resolve problems more efficiently](https://thenewstack.io/aws-aerospike-team-up-for-more-efficient-data-streaming/) than in many distributed systems where issues may span multiple layers or components.

The development process itself becomes more streamlined when scripts run inside the database — [developers no longer need](https://thenewstack.io/what-ai-developer-skills-do-you-need-in-2024/) to build to push data between multiple environments and toolsets. This reduction in data movement minimizes synchronization issues and potential data discrepancies between environments.

## Potential Drawbacks and Considerations
There are several potential concerns about running scripts inside the database engine, none of which are insurmountable:

- How will scripts affect overall database performance? If scripts consume significant resources on database nodes, they may compete with regular database operations for CPU, memory and I/O. This resource contention can lead to slower query response times for other database users or applications, particularly during periods of peak use. Database administrators must carefully monitor and manage resource allocation to ensure that script execution doesn’t negatively affect critical database functions.
- The syntax of stored procedures is specific to a database, thus heavy reliance on stored procedures increases vendor lock-in. Writing “normal” code with database calls in ANSI SQL is more portable. Make sure your organization allows scripts before writing them.
- Will your DevOps team be able to preserve the separation of concerns, a development best practice? Consolidating logic in the database can simplify development, but it can also blur the lines between data storage and business logic, potentially complicating the long-term maintenance and evolution of the system.
## Mitigating Challenges With the Right Database
To address these potential obstacles, it’s crucial to choose a [database system](https://aerospike.com/products/database/?utm_source=byline&utm_medium=pr&utm_campaign=thenewstack) that is designed for efficient resource management and scalability. Look for databases that offer:

- Advanced resource (CPU, memory, storage, network) management capabilities
- Built-in support for distributed processing
- Robust scripting languages with good developer tools
- Efficient handling of concurrent operations
Running scripts inside the database offers compelling advantages in terms of performance, data consistency and development efficiency. By bringing processing closer to the data, organizations can achieve faster operations, better resource utilization and simplified architectures. In today’s real-time world where microseconds count, organizations must do everything they can to optimize performance

Organizations that embrace this approach position themselves to address data demands, today and tomorrow, with greater agility, performance and resource efficiency.

*Visit our website to learn more about* *Aerospike Database**.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)