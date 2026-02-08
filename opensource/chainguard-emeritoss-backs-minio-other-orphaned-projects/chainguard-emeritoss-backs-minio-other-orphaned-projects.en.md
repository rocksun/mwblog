Open source has a problem. There are many under-supported, or even abandoned, open source programs that are still in wide use, but there’s no one at the driver’s wheel.

To address this issue, [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention) recently launched [Chainguard EmeritOSS](https://c67dcd9a.streak-link.com/Csf3OJpyshg0bW_ibgbecPa5/https%3A%2F%2Fgithub.com%2Fchainguard-forks%2F), a project to support these vital, but unloved, programs. After putting its support behind [three different programs](https://thenewstack.io/chainguard-takes-over-maintenance-of-aging-oss-projects/), the infrastructure security company is coming to the rescue of 10 more programs.

Perhaps the chief one is [MinIO](https://github.com/minio/minio), a lightweight, high-performance, [open source object storage system](https://thenewstack.io/add-object-storage-to-rocky-linux-with-minio/) that’s fully Amazon S3 API-compatible.

In December, the maintainers [put the software](https://medium.com/@heinancabouly/minios-maintenance-mode-a-wake-up-call-for-the-cncf-ecosystem-38add3bc6c4f) under [maintenance-only mode](https://github.com/minio/minio), much to the consternation of the community that still used the community edition. The namesake company, previously in charge of the project, recommends [the free edition](https://www.min.io/download) (though not open source) or the commercial edition of its Alstor platform instead.

Chainguard ramped up support and even offers a [secure MinIO image](https://www.chainguard.dev/unchained/secure-and-free-minio-chainguard-containers).

## Other newly supported programs

Other [newly supported zombie programs](https://www.chainguard.dev/unchained/fork-yeah-were-adding-ten-new-open-source-projects-to-emeritoss) include:

[Prometheus PushProx](https://github.com/prometheus-community/PushProx), a proxy and client solution that enables [Prometheus](https://prometheus.io/) to scrape targets even if they’re hidden behind NATs or firewalls. While PushProx still “pulls” the data in, behind the scenes, it runs a tunneling proxy that “pushes” data requests to retrieve the data.

[Cassandra Exporter](https://github.com/criteo/cassandra_exporter) is a standalone metrics exporter for [Apache Cassandra](https://thenewstack.io/why-apache-cassandra-5-0-is-a-game-changer-for-developers/). This Java Virtual Machine (JVM) program retrieves Cassandra performance and usage metrics without overburdening the Cassandra NoSQL DBMS.

[Prometheus exporter](https://github.com/prometheus-community/json_exporter) scrapes JavaScript Object Notation (JSON) APIs and turns them into metrics using the [JSONPath](https://jsonpath.com/) configuration. With this useful tool you can pull in data from almost any API that understands JSON.

[Prometheus exporter for RabbitMQ](https://github.com/kbudde/rabbitmq_exporter) exposes broker, queue, connection, and exchange stats via the Management API. This exporter works with legacy [RabbitMQ 3.x](https://www.rabbitmq.com/release-information) versions. It provides extensive filtering and configuration capabilities for monitoring RabbitMQ infrastructure. It’s often used for message-queue monitoring and alerting.

The [Prometheus exporter for Python RQ (Redis Queue](https://github.com/mdawar/rq-exporter)) exposes job-queue metrics, including processing time and counts. This enables managers to monitor background workloads more effectively via an HTTP endpoint, typically “/metrics,” that Prometheus can then scrape for data.

When I was a young [Unix developer](https://thenewstack.io/learning-linux-start-here/), I’d just use grep, awk, and sed, but the Logstash [filter range plugin](https://github.com/logstash-plugins/logstash-filter-range) lets you define numeric or string ranges and check whether a given field’s value falls within them without writing shell scripts by hand. Armed with this data, you tag events, drop unwanted data, apply conditional processing, and you get the idea.

[PgCat](https://github.com/postgresml/pgcat) is a PostgreSQL connection pooler and proxy that supports sharding, load balancing, failover, and mirroring. It can multiplex client connections to PostgreSQL DBMSs to cut down connection overhead and reduce network latency.

The [OpenStack](https://www.openstack.org/) [Velero plugin](https://github.com/Lirt/velero-plugin-for-openstack) adds backup and restore operations to [Velero](https://velero.io/) for OpenStack Cinder volumes, Swift containers, and Manila shares. It provides volume snapshotting and object storage capabilities for OpenStack environments. Without it, Velero is used to back up and restore Kubernetes clusters running on OpenStack.

Finally, the [k8s-node-collector](https://github.com/aquasecurity/k8s-node-collector) is a small utility that provides a Kubernetes node information collector to gather file system, process, and system data. It produces structured JSON output for auditing, compliance checks, or custom integrations.

## No more support

Of course, what all these programs have in common is that their creators no longer support them. As [Kim Lewandowski](https://www.linkedin.com/in/kimsterv/), Chainguard’s CSO and co-founder, wrote in the blog post announcing this news, “When a project no longer requires continuous upkeep or the maintainers need to step away, Chainguard EmeritOSS [steps] in.”

This is a very useful service. There are far too many mission-critical [open source programs](https://thenewstack.io/open-source/ "open source programs") that no longer have a home, and Chainguard is giving them one. As Lewandowski put it, “EmeritOSS exists for the projects that have earned their stripes. They’ve shipped, scaled, and supported real systems, and while their maintainers may be ready to step back, the software itself still has plenty of life left.”

## Hand off unsupported projects

Indeed, they do. As Chainguard co-founder and CEO, [Dan Lorenc](https://www.linkedin.com/in/danlorenc) explained in an earlier The New Stack column: “We need a way for open source maintainers to gracefully [hand off ‘done’ projects](https://chainguard.dev/unchained/introducing-chainguard-emeritoss) even when they no longer have a significant feature roadmap. We need to offer them a place where:

That place is EmeritOSS.

Do you need these programs? [Chainguard’s forked, stability-focused EmeritOSS](https://github.com/chainguard-forks/) versions will remain freely available on [GitHub](https://github.com/chainguard-forks/) in source code. Don’t want to fuss with the code? Chainguard also offers secure, continuously maintained container images and [APK packages](https://edu.chainguard.dev/open-source/wolfi/apk-package-manager/) through its commercial distributions. Are you depending on another open source program and need help? You can [submit it for consideration](https://get.chainguard.dev/emeritoss-submission?__hstc=1638499.72def09cf1055c99e814f503d1822919.1768770970725.1768770970725.1768776191368.2&__hssc=1638499.1.1768776191368&__hsfp=4354069f6051f96c2c74e52210cf4c11&_gl=1*o0up4c*_gcl_au*OTQ2MzcwNDk5LjE3Njg3NzA5NzA.), and Chainguard might support it via EmeritOSS.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)