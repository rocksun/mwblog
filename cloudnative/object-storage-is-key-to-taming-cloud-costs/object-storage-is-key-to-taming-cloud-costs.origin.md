# Object Storage Is Key To Taming Cloud Costs
![Featued image for: Object Storage Is Key To Taming Cloud Costs](https://cdn.thenewstack.io/media/2024/06/8b8c9da1-mountain-8079469_1280-1024x678.jpg)
[Rising cloud costs](https://thenewstack.io/cloud-native-observability-fighting-rising-costs-incidents/) have been a recurring theme in recent years. We saw enterprise cloud use skyrocket [during 2020](https://thenewstack.io/cloud-dominated-decade-will-2020/); in late 2022 into early 2023, cloud providers reported declining and flat revenues as CXOs got sticker shock from bloated cloud bills. Yet the [tide has turned again](https://thenewstack.io/answers-to-the-5-most-common-cloud-cost-optimization-questions/), even though cloud repatriation is still a trend. Nearly a third of companies are spending more than $12 million a year in public cloud, up 24% from 2023, according to [ Flexera State of the Cloud 2024](https://info.flexera.com/CM-REPORT-State-of-the-Cloud?lead_source=Organic%2520Search).
IT leaders must keep investing in public cloud infrastructure because it offers scalability and flexibility, presents opportunities for cost savings, and perhaps most importantly, the major cloud providers now host a ready-made suite of seravices for launching AI projects.
## The Data Challenge of Cloud
Getting
[data to the cloud](https://thenewstack.io/cloud-data-migration-or-cloud-data-tiering/), however, can be a barrier. IT leaders must spend more time than ever researching cloud services, migration, and tiering tools and methodologies while understanding their unique data environments. The cloud offers various storage services and tiers at very different price points. For unstructured data, cloud file storage such as Azure Files or AWS FSX and cloud object storage such as Amazon S3 or Glacier are popular options. You can cut cloud costs by at least 70% — but it requires a combination of migrating and tiering data to the appropriate storage class at the appropriate time. In a [ prior article](https://thenewstack.io/cloud-data-migration-or-cloud-data-tiering/), I discussed the differences between migrating and archiving (aka tiering) files to the cloud and when to use each approach.
Briefly, cloud data migration is the process of moving files from data centers to cloud file storage. Users must then access the migrated data directly from the cloud. Cloud data migration makes sense when you plan to use the cloud as your file storage to run applications from the cloud or when you want to use the cloud for long-term archives or data lakes for AI. This is a “detached archive” that requires changes to users and applications.
Cloud tiering is the process of transparently extending on-premises file systems with cloud object storage. Ideally, the tiering solution should allow users to access tiered files from the on-premises file system so there is no change to users or applications. This makes sense when you need a live or “attached archive” or extension to your existing infrastructure.
Whether tiering or migrating to the cloud, object storage is an essential factor to consider. In this article, I’ll focus on cost-effective object storage as a migration and tiering target for enterprise data.
## The Benefits of Cloud Object Storage for Unstructured Data
Unlike cloud file storage, which delivers high performance for active data with scalability and pay-per-use pricing benefits, cloud object storage is a superb way to save dramatically on rarely used or “cold” data. Object storage was designed to be highly scalable and less costly to store large amounts of data. Unlike file storage, object storage is better for data that is read many times and written or modified rarely, thus making it ideal for use as an archive. Another benefit of migrating data to object storage is using new services, such as cloud AI and ML tools, which are mostly designed to work with objects. The point here is that your data is natively available to these services. Finally, if you move data into
[ immutable storage](https://www.komprise.com/glossary_terms/immutable-storage/) such as AWS S3 Object Lock, no one can modify or delete it—thus creating an affordable ransomware defense tactic.
## Cost Savings from Object Storage
On average, cloud object storage is 2x to 10x less than cloud file storage. In addition, if you are actively reading and writing the files (get/put operations), the cost for these operations adds up for a file server.
|Service
|Storage Type Price
|(GB/month)
|AWS Object Store
|S3 Standard
|.023
|S3 Infrequent Access
|.0125
|S3 Glacier Instant Retrieval
|.004
|Amazon EFS File Server
|Standard
|.30
|Infrequent Access
|.016
|Archive
|.008
Leveraging cloud object storage is an essential element of your cloud migration and tiering strategy, especially for file data, as it can
[ save 70% of annual storage and backup costs](https://techcommunity.microsoft.com/t5/azure-storage-blog/how-to-save-70-on-file-data-costs/ba-p/3799616) on average.
## File-to-Object Tiering Tactics
Object stores are ideal for archives because cold data is typically not written to or modified. Furthermore, object stores are inexpensive, yet unlike tape, the data can be retrieved in milliseconds. Most
[ data tiering](https://www.komprise.com/glossary_terms/data-tiering/) solutions are policy-driven and run continuously, which makes them ideal for moving cold data from fast, expensive file systems to much less costly object storage systems. Because they can run without intervention, it guarantees that your tiering project will provide ongoing data storage savings. However, many tiering solutions break the file into proprietary blocks on object storage, rendering the data useless in the cloud.
The key aspects to consider when tiering files to cloud object storage are:
- Does the solution provide transparency so that users can see, search, and access the file from the original source as if it had never been tiered?
- Can the files be accessed natively from the object store? In essence, is the full file preserved in the cloud as a native object so you can leverage cloud services and applications that use an object interface to access content?
- Can you execute policy-driven automation to reduce overheads and ensure continual cost optimization?
- Is file metadata preserved so there is file-object duality and the data can be retrieved as either files or objects? This is an essential element to consider if your use case requires file-based access.
- Can you rehydrate the files back to the source file system with full fidelity concerning the content, metadata, permissions and access control lists (ACL)? This ensures data is appropriately protected once it has returned to the file server.
## File-to-Object and Object-to-Object Cloud Migration Tactics
When migrating files to cloud object stores, if retrieving the data as files is important, ensure that the solution preserves file metadata. Also, ensure that native object access is available.
Migrating on-premises objects is more straightforward than migrating files to cloud objects because this is a “like-to-like” migration. If you are migrating objects for cloud applications, you’ll need to migrate all the required data stored on-premises.
Since cloud migrations are across a WAN, look for solutions specifically designed to transfer data at high speeds. This can reduce large migration timelines from several months to just a few weeks; long, complicated migration cycles are a notable barrier to cloud journeys for many enterprises.
If you are migrating objects for archival purposes, you’ll need to analyze data to identify buckets with “cold” objects and determine what to migrate.
Object storage is highly scalable and less expensive than file storage. Nowadays, many solutions are available that translate files into objects with high fidelity, allowing you to leverage the lower cost of cloud storage for files while still providing the ability to rehydrate the data back to a file system with full fidelity.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)