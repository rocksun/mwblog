Although forking is fairly routine in code platforms like GitHub and different file systems, it’s not been a feature in [object storage](https://thenewstack.io/why-ai-loves-object-storage/). Aiming to change that, [Tigris Data](https://www.tigrisdata.com/?utm_content=inline+mention) has introduced bucket forking, which allows organizations to fork their data — without unwieldy copies, time-consuming delays, escalating costs, data governance issues, or security and regulatory woes — with the same ease with which you can fork code in GitHub.

## What Is Bucket Forking?

Bucket forking is underpinned by snapshots of the data, which effectively freeze the data’s state at a particular point in time so that it can be forked.

Once data is forked, there’s a *metadata-only* copy of the bucket that users can work on (allowing them to modify, add or delete data from any point) without affecting the original bucket. As is the case with code [forked in git](https://thenewstack.io/need-to-know-git-start-here/), the forked bucket and the source bucket are isolated from each other; changes in one don’t appear in the other.

Access to forked data is as instantaneous for petabytes of data as it is for gigabytes. This provides a scalable means of fueling innovation for data science sandboxes, testing and deploying intelligent agents in production, and implementing swift backups to speed disaster recovery.

Bucket forking uses an immutable, append-only architecture and the open source [FoundationDB](https://thenewstack.io/foundationdb-a-distributed-database-that-cant-be-killed/) as a key-value-based metadata store for the underlying data objects. This architecture helps make Tigris Data’s [AWS](https://aws.amazon.com/?utm_content=inline+mention) S3-compatible object storage applicable across a broad range of verticals and use cases.

## The Role of a Log-Based Architecture

The bucket-forking features in Tigris Data’s object storage are directly attributed to its immutable architecture, which was designed like a log-based system.

“As new object storage and new files are created, or new versions of files are updated, they’re just appended to the log,” [Ovais Tariq](https://www.linkedin.com/in/ovaistariq/), Tigris Data CEO, explained.

> “Because you know the data’s not going to get mutated or changed, you don’t need to copy the entire data set.”  
> **—Ovais Tariq, CEO, Tigris Data**

This append-only architecture means that no matter how many times objects are updated, there is a complete history of the changes, which can be used to support time travel. It also helps maintain the state of the storage system.

“When you’re mutating state, there are a lot of edge cases involved that you need to think about,” Tariq said. “You need to think about concurrency and conflicts. Several of those complexities go away when choosing an append-only, immutable design.”

## Understanding Snapshots in Object Storage

Snapshots are a frozen point in time of the storage “log.” They are created by placing a marker at a specific temporal state of the stored data. In addition to revealing everything that’s happened to the state of the data up until that point, snapshots help organizations recover from a cybersecurity attack or implement disaster recovery.

Another potential benefit for organizations is that “because you know the data’s not going to get mutated or changed, you don’t need to copy the entire data set,” Tariq commented.

This approach potentially creates substantial cost benefits. Because there are no copies, organizations can make snapshots of data of any scale without paying more for larger storage quantities. They can also implement as many snapshots as they need, be that hourly, daily, weekly or every half hour, to accommodate their applications.

Most of all, snapshots enable bucket forking, which involves “creating parallel timelines of the data without doing any copying,” Tariq said.

## How Bucket Forking Supports Machine Learning

For multiagent machine learning (ML) experiments, instantaneous, scalable bucket forking helps data scientists experiment with different versions of data and models. Versioning built directly into storage eliminates the need for external version management tooling, encouraging earlier and faster experimentation.

“When you have a shared data set and want to run multiple experiments with it, with Tigris, it’s straightforward to run them in an isolated manner,” Tariq said. “You just fork it.”

This approach may be even more beneficial for deploying agents, particularly in terms of successfully monitoring, governing and auditing them. “If you have a coding agent and the agent makes mistakes, you can do snapshots every time agents make a change,” Tariq said.

Afterward, organizations can simply roll back the data to before the mistake occurred and update the agent’s functionality accordingly.

Many agentic systems employ agents working in parallel, presenting challenges not only with collisions but also with managing their environments. “When multiple agents share the same development environment, forking provides safety and isolation,” Tariq continued.

By using a fork per agent, organizations can help ensure safety, isolation and point-in-time control.

## The Technology Behind Forking: FoundationDB

Versioning, a critical enabler of bucket forking and snapshots, is attributed to the metadata stored in FoundationDB, a distributed, ordered key-value store in which “the key range is ordered,” Tariq said.

The keys are the metadata — primarily consisting of information about the buckets and their objects, the key to the object and the version of the data. The versioning supports bucket forking and snapshots by providing multiplicities of the metadata of the same object.

As Tariq explained: “When I write an object once, it starts at version zero. Then, when I write the next copy, it starts at the next version, and so on and so forth.”

Although FoundationDB stores the keys or metadata “pointers” about the objects, the underlying data is kept on disk in a file store. That data isn’t actually copied, which is what enables organizations to fork data and begin working on it like it was a copy — without doubling the amount of storage they’re paying for.

This approach is primed for regulatory compliance and data governance use cases since “you automatically get this verifiable audit trail of all the changes that were performed on storage,” Tariq explained.

## Broad Applicability Across Industries

The underlying value of Tigris Data’s bucket forking isn’t the ease, simplicity or cost-saving measures it provides for working with test data sets or backups.

The most important factor is that these benefits, including disaster recovery, auditability, data science experimentation, multiagent deployments and more, are horizontally applicable across industries and use cases. They fuel development in any facet of the data landscape while providing immutable records of everything that was done to the data — without copying it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/07/ee3e39b7-cropped-52925a32-jelani-harper-110x110-1.jpg)

Jelani Harper has worked as a research analyst, research lead, information technology editorial consultant, and journalist for over 10 years. During that time he has helped myriad vendors and publications in the data management space strategize, develop, compose, and place...

Read more from Jelani Harper](https://thenewstack.io/author/jelani-harper/)