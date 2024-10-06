# MongoDB 8 Goes Hard on Time-Series Data, Horizontal Scaling
![Featued image for: MongoDB 8 Goes Hard on Time-Series Data, Horizontal Scaling](https://cdn.thenewstack.io/media/2024/10/5d6d4528-mongodb-1024x683.png)
[MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention) has [released version 8](https://www.mongodb.com/try) of its namesake document database and has geared this version for high-end, performance-oriented workloads.
Optimizations have made the database system 32% more performant. The speed of time-series aggregations has been boosted by 200%, Scalability has been improved by 50%, and the database’s unique feature, [queryable encryption](https://thenewstack.io/mongodb-6-0-brings-encrypted-queries-time-series-data-collection/), has been expanded for more types of queries.

In the month prior to this release, the company also discontinued a number of lesser-used features and products.

[MongoDB](https://thenewstack.io/benchmarking-postgresql-vs-mongodb-for-genai/) has over 50,000 customers of its commercially-supported [MongoDB Enterprise platform](https://www.mongodb.com/atlas), and the base [open source database](https://github.com/mongodb/mongo) is used in millions of deployments.
For its commercial clients, the company has been working to make the software [more robust](https://thenewstack.io/mongodb-builds-out-its-full-platform-play/).

“Customers across industries tell us how critical it is for their core operational database to perform well, no matter the scale involved,” said [Jim Scharf](https://www.mongodb.com/company/newsroom/press-releases/mongo-db-announces-jim-scharf-as-chief-technology-officer), chief technology officer at MongoDB, in a statement. “MongoDB 8.0 was built to exceed the most stringent security, durability, availability, and performance requirements of our customers.”

## Time Series Data Processing
The improvements aimed at improving overall performance across a wide variety of use cases, where even minor sub-optimal performance can lead to user disgruntlement.

Various optimizations in the architecture have squeezed an additional 32% performance improvement from the software through smarter memory usage and more efficient queries.

Time series processing has improved by a remarkable 200%. A fresh way of batch processing of INSERTs, UPDATEs and DELETEs speed bulk writes by 56% and data replication concurrent writes by 20%.

This means the company claims that MongoDB can handle higher volumes of time series data while performing complex aggregations.

## Horizontal Scaling
The company and the project’s contributors have also worked harder to improve horizontal scaling or the ability the software has to move from, say, thousands of users to millions of users.

This is usually done by splitting the data into “shards” across multiple servers or shards. Starting with version 8.0, MongoDB can now distribute data across multiple shards 50% faster without any additional configuration or setup.

The software can also better handle unexpected spikes in workload demand. It now includes the ability to set a default maximum time limit for running queries, to reject recurring types of problematic queries, and to set query settings to persist through events like database restarts to help ensure high performance for applications experiencing high demand.

Further enhancing resilience for [Kubernetes users](https://thenewstack.io/5-reasons-to-run-mongodb-on-kubernetes/) is the new multicluster support for the MongoDB Enterprise Kubernetes Operator, for deploying MongoDB across local and geographically-distributed multiple clusters.

This can allow users to spread their deployment across geographically separated clusters for greater resilience.

## What Else Is in the Box?
Other improvements that come with MongoDB 8 include:

**MongoDB Queryable Encryption**for range functions. This follows up on earlier work to encrypt the data during networking and storage, and even remain encrypted when it is queried. This extension now covers a new type of query, range functions. These queries remain encrypted until the end user, with the appropriate decryption key, views it.**The MongoDB for IntelliJ Plugin**will help Java Developers write and test Java queries for the database more efficiently.**MongoDB CoPilot Participant for VS Code Public Preview**brings a chat interface to developers writing for the database system, offering developers queries, and explanations of schemas from directly within VS Code.
## Other Changes
MongoDB has also been busy trimming its product line, mostly around its Atlas cloud data service. Last month, the company announced it [would be discontinuing](https://medium.com/@stevdza-san/this-is-bad-mongodb-is-shutting-down-their-services-c2c6048d667b) the [Atlas Data API and Custom HTTP endpoints](https://www.mongodb.com/community/forums/t/mongodb-atlas-data-api-and-custom-https-endpoints-end-of-life-and-deprecation/296686), [Atlas Device Sync and Atlas Device SDKs](https://www.mongodb.com/blog/post/realm-now-part-atlas-platform), [Atlas Data Lake](https://www.metarouter.io/post/the-power-of-mongodb-atlas-data-lake) and [Atlas Edge Server](https://www.mongodb.com/products/updates/product-support-deprecation). Customers [can use](https://medium.com/@stevdza-san/this-is-bad-mongodb-is-shutting-down-their-services-c2c6048d667b) these features until Sept. 30, 2025.

MongoDB sets its roadmap to customer needs, and not all of the features it introduces find its audience, explained [Andrew Davidson](https://www.linkedin.com/in/andrewad/), senior vice president of product, MongoDB, in an e-mail statement.

“MongoDB invests in areas based on customer feedback, and we develop our roadmap to meet their needs,” he stated.

The company has a wide ecosystem of partners who should be able to provide these capabilities, however.

“We are committed to helping affected customers successfully move to one of these alternative solutions within our extensive partner network,” he noted.

MongoDB 8.0 is now available on the [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), Google Cloud, and Microsoft Azure through [MongoDB Atlas.](https://www.mongodb.com/atlas) MongoDB Enterprise Advanced [now runs](http://mongodb.com/try) on 8.0 as well.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)