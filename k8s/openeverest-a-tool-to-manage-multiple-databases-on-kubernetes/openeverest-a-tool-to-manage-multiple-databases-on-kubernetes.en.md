Database support provider [Percona](https://www.percona.com/?utm_content=inline+mention) is donating a database management tool for [Kubernetes](https://thenewstack.io/kubernetes/) environments to the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention).

For Kubernetes environs, the newly named [OpenEverest](https://github.com/openeverest) (formerly called Percona Everest) provides a unified interface for managing different types of databases, including provisioning and management. Thus far, it supports PostgreSQL, MySQL and [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention).

The company’s [strategy](https://www.percona.com/blog/blog-post-good-bye-percona-everest-hello-openeverest/) is to make [OpenEverest](https://openeverest.io/) a multivendor project managed by open governance, via the CNCF. It will retain the same Apache 2.0 open source license and be donated to the organization. Current users of the commercial [Percona Everest](https://www.percona.com/software/percona-everest) will see no major changes, according to the company.

“As Percona Everest matured, it became clear that the project would be better served as a community-led open source initiative rather than something led solely by Percona,” said [Blair Rampling](https://www.linkedin.com/in/blairrampling), vice president of product management at Percona, in an email statement. “As OpenEverest, the project is well positioned to serve as a fully vendor-agnostic Kubernetes data platform, so even more databases can be provisioned and managed, and eventually enable integrations beyond databases.”

Everest maintainer [Sergey Pronin](https://www.linkedin.com/in/sergeypronin/) and Percona founder [Peter Zaitsev](https://www.percona.com/blog/author/pz/) have also formed a new company, [Solanica](https://solanica.io/), to provide enterprise support services for the software.

[![OpenEverest Workflow](https://cdn.thenewstack.io/media/2026/01/d904b114-openeverest-workflow.png)](https://cdn.thenewstack.io/media/2026/01/d904b114-openeverest-workflow.png)

OpenEverest workflow (OpenEverest).

## Private Database as a Service

Percona created Everest as a way to manage multiple databases in a cloud environment with the same ease enjoyed by cloud database providers, explained [Piotr Szczepaniak](https://www.linkedin.com/in/petersgd/?originalSubdomain=pl), senior product manager at Percona, in a [2023 post for The New Stack](https://thenewstack.io/building-an-open-source-private-dbaas/).

Cloud databases (Database as a Service, or DBaaS) are often preconfigured, reducing the time developers need to set them up. High availability, disaster recovery and autoscaling features are usually built in, relieving the burden to set them up.

Running a private database service — perhaps as part of a [platform engineering initiative](https://thenewstack.io/platform-engineering/) — comes with additional advantages, such as greater control of security settings and control over the data itself, Szczepaniak elaborated. Lower operational costs may be another benefit.

Setting up and maintaining a private database service, however, can be a challenge for many shops. This is the targeted user user base for OpenEverest.

## How Everest Works

To [create a database](https://openeverest.io/blog/how-openeverest-works/) in Everest, the user submits a request with the desired configuration through a web interface. Then they use the interface to requisition the needed Kubernetes resources.

One of the benefits of Everest is that admins do not need to know specific setup routines for each type of database.

OpenEverest server, via a RESTful API, uses a set of custom resource definitions (*DatabaseCluster*, *DatabaseClusterBackup* and *DatabaseClusterRestore*) that are database independent, sparing the admin from having to understand the quirks of each individual database operator. It then relies on a set of operators that are written for specific database systems.

Thus, the software works identically for MySQL, MongoDB or PostgreSQL.

[![](https://cdn.thenewstack.io/media/2026/01/10376322-openeverest-crds-scaled.png)](https://cdn.thenewstack.io/media/2026/01/10376322-openeverest-crds-scaled.png)

Administrating OpenEverest itself, including installation, is done through a command line interface (CLI), which handles tasks around account management, role-based access control (RBAC), namespaces, provisioning and upgrading.

## CNCF’s Criteria for New Projects

With an active user base, Everest is in a good position to become a [CNCF incubating project](https://www.cncf.io/projects/). CNCF’s criteria for a technology include at least some users who are deploying the technology in production, a healthy contributor base and a [clear roadmap](https://github.com/openeverest/roadmap) for future development.

Managing stateful database loads was one of the original challenges for Kubernetes, and so there has been a lot of work around the challenge, leading to the launch of the [Data on Kubernetes](https://dok.community/) community.

Other multidatabase solutions in development include [KubeBlocks](https://kubeblocks.io/docs/preview/user_docs/overview/introduction) and [KubeDB](https://kubedb.com/features/). With over [150 volunteer-written extensions](https://operatorhub.io/operator/stackgres), [StackGres](https://stackgres.io/doc/1.14/intro/about/) is a popular implementation focusing on PostgreSQL, and the CNCF sandbox project CozyStack is a cloud management platform with database support. Almost all databases have their own dedicated Kubernetes operators as well.

Percona provides premium support services for a range of open source database systems, including [MySQL](https://thenewstack.io/facebook-makes-a-big-leap-to-mysql-8/), [PostgreSQL](https://thenewstack.io/percona-brings-transparent-data-encryption-to-postgres/), MongoDB and [Valkey](https://thenewstack.io/percona-backs-valkey-with-enterprise-grade-support/).

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)
[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)