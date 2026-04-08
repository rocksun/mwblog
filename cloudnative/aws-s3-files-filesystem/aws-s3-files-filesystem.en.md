Amazon S3 can now be a file system. On Monday, AWS launched a new S3 feature called S3 Files that makes S3 buckets accessible as native file systems, supporting NFS v4.1+ operations such as creating, reading, updating, and deleting files. In today’s announcement, AWS’s Sébastien Stormacq calls it “the first and only cloud object store that offers fully-featured, high-performance file system access to your data.

S3 Files connects any AWS compute resource, including EC2 instances, ECS and EKS containers, Fargate tasks, and Lambda functions, directly with data already stored in S3. The data stays in S3 and is also accessible through S3’s usual APIs.

It’s worth noting that this does not, however, turn S3 into a file system you can mount locally from your desktop or another cloud provider. It won’t let you mount your S3 bucket as a Finder folder, for example.

A file system on top of S3, Stormacq writes, is “ideal for workloads where multiple compute resources — whether production applications, agentic AI agents using Python libraries and CLI tools, or machine learning (ML) training pipelines — need to read, write, and mutate data collaboratively.”

## The gap S3 never closed

AWS has enough file storage services to keep “cloud architects entertained during their architecture review meetings,” Stormacq acknowledges. He notes that S3 Files is specifically meant for interactive, shared access to data that already lives in S3.

According to AWS, S3 now stores more than 500 trillion objects across hundreds of exabytes. From the outset, the service was built as an object storage platform, but developers quickly realized the potential of using its almost unlimited scale as the basis for a filesystem for their applications.

Open-source projects like s3fs-fuse and Goofys use FUSE to translate standard file operations into S3 API calls. Those tools, however, tend to be slower and, given S3’s limitations, couldn’t support file locking and treat renames as copy-and-delete operations. Other options like [ObjectiveFS](https://objectivefs.com/) and [JuiceFS](https://juicefs.com/en/) offer full POSIX semantics but require separate metadata infrastructure.

AWS saw the potential here, too. S3 File Gateway, part of the Storage Gateway family, has offered NFS and SMB access to S3 for years — but it’s a hybrid-cloud tool, designed for on-premises environments connecting to S3.

In 2023, the company also launched the open-source Mountpoint for S3, a high-performance FUSE client it optimized for cloud-native, read-heavy workloads. It was faster than s3fs, but still couldn’t do in-place edits, directory renames, or file locking.

## Built on EFS, not the S3 API

With S3 Files, AWS is taking a different approach. Rather than building a file system emulation on top of the S3 API, S3 Files uses Amazon Elastic File System (EFS), the company’s managed NFS service that has long been AWS’s answer for workloads that need shared file access across multiple compute instances.

Instead of trying to make the S3 API behave like a file system, AWS is layering a production-grade file system directly onto S3 storage. EFS already provides support for NFS v4.1, with sub-millisecond read latency, and concurrent access from thousands of clients. According to AWS, S3 Files delivers similar ~1ms latencies for actively used data.

One interesting aspect of S3 Files — and one that developers may not love — is that the caching architecture has two tiers. Files that benefit from low-latency access are automatically placed in the file system’s high-performance storage. For files where low-latency access isn’t the priority — for large sequential reads, for example — S3 Files serves them directly from S3 to maximize throughput.

The system also supports intelligent pre-fetching, and users can control whether to load full file data or metadata only, allowing optimization for specific access patterns.  
S3 Files will work with any existing general-purpose S3 bucket. There’s no need for any migrations.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)