# Charles Schwab Adopts PostgreSQL (With VMware Tanzu)
![Featued image for: Charles Schwab Adopts PostgreSQL (With VMware Tanzu)](https://cdn.thenewstack.io/media/2024/09/8b061920-hegde-1024x768.jpg)
Brokerage firm [Charles Schwab](https://www.schwab.com/) has found value in [PostgreSQL](https://thenewstack.io/qa-how-enterprisedb-brings-five-nines-to-postgresql/): The company has begun the process of replacing some of its proprietary database management systems with this open source system.

The thinking goes: When it comes to relational databases, they are all pretty much the same these days.

After five decades in refinement, relational databases are pretty much all mature. Gartner doesn’t even bother doing a Magic Quadrant for them any longer, [focusing its analysis on cloud databases](https://www.gartner.com/reviews/market/cloud-database-management-systems) instead.

So, in terms of cost-effectiveness — which, obvs, would be a prime concern for a financial services company — getting the most out of databases comes down to Total Cost of Ownership (TCO).

Schwab found that the open source PostgreSQL database system had a lower TCO than proprietary models, noted [Nataraj Hegde](https://www.linkedin.com/in/nataraj-hegde-12767417/), Charles Schwab database engineering director, at [Broadcom](https://broadcom-software.security.com/blogs/division/broadcom-software?utm_content=inline+mention)‘s[ VMWare Explore 2024](https://www.vmware.com/explore/us?utm_source=the+new+stack&utm_medium=referral&utm_campaign=event&utm_content=inline-mention) last week, in a talk that detailed the process Schwab used to vet the software.

![](https://cdn.thenewstack.io/media/2024/08/bda5a30f-novick-hegde-300x225.jpg)
VMware’s Ivan Novick (L) and Schwab’s Nataraj Hegde, VMWare Explore. (Photo: TNS)

This is not to say the PostgreSQL, developed in part by [Michael Stonebreaker](https://thenewstack.io/dr-michael-stonebraker-a-short-history-of-database-systems/) in the early 1990s, could easily be dropped into the regulatorily complex environs of Charles Schwab, without some enterprise support.

This is where Broadcom comes in. As part of the company’s [VMware Tanzu platform Data Solutions](https://tanzu.vmware.com/data), the company maintains its own enterprise-hardened version of PostgreSQL, according to [Ivan Novick](https://www.linkedin.com/in/ivannovick/), product management for Tanzu Data Services, Broadcom, who joined the talk.

## PostgreSQL as a Service
“You must be wondering, why is Schwab running Postgres?” Hegde asked the audience. Hegde himself is a certified Master in Oracle, and has experience with many other NoSQL and SQL database systems.

At Schwab, Hegde is in charge of the roadmaps of various data applications. The company has set up a centrally managed architecture where databases can be offered to internal users “as a platform service.” The user requests the database and gets a connection.

The database team takes care of all the underlying configuration bits, such as the architecture, the backup options and so on.

## Why Choose PostgreSQL
PostgreSQL is exploding in popularity, with the [potential to eclipse](https://db-engines.com/en/ranking) the most popular open source database, Oracle’s MySQL, in time, given their current trajectories.

“Postgres has gathered a lot of traction in the industry, with more and more enterprise customers like us,” Hegde said. “One big reason is the cloud. On the cloud, Postgres is becoming the de facto SQL database.

The database market [is expected](https://www.einpresswire.com/article/638376992/operational-database-management-market-size-worth-usd-80-26-billion-in-2028-at-a-cagr-of-5-2) to grow to about $80 billion by 2028. And in terms of open source databases, PostgreSQL is [gobbling up the market](https://medium.com/@fengruohang/postgres-is-eating-the-database-world-157c204dcfc4).

But database technology in general is maturing.

“There is no real strategic advantage of one relational database over the other,” Hegde said. PostgreSQL has achieved parity with many commercial offerings, including optimizations, indexing strategies and support for the latest data types such as [JSON](https://thenewstack.io/an-introduction-to-json/) and [vector](https://thenewstack.io/onehouse-automates-vector-embedding-for-its-data-lakehouse/).

Without any differentiators worth worrying about, the next aspect to consider, from Schwab’s viewpoint, is TCO.

PostgreSQL is open source, so it has no vendor lock-in (or pesky licensing audits).

“Not having to pay the license for database definitely lowers the TCO, but it is the lower TCO is not just licensing,” Hegde said,

PostgreSQL is also very easy to install and maintain. And the compute and storage operational costs are also lower. “Because it is simple, you have less operational cost,” he said.

So for these reasons, Schwab made PostgreSQL a preferred database.

## PostgreSQL and High Availability
Once PostgreSQL was vetted, Schwab still had some hurdles to get onboarded, a set of issues that took about six months to work through.

Overall, Schwab runs about 20,000 applications in-house. Any other of these projects could use PostgreSQL if they chose, so it has to be able to support a wide range of workloads.

The onboarding team looked at how Schwab used its current databases in order to identify any gaps that might have been missing with PostgreSQL. PostgreSQL would be able to handle more than 90% of the bank’s current workload, they found.

High availability (HA) was a major requirement, and Schwab found that PostgreSQL could offer the same HA as Oracle and [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) SQL Server, with a bit of additional software, also open sourc\e.

Most database vendors have some sort of backup and recovery strategy, but more is needed than simply replicating copies of the database, Hegde said. But more is needed than a full backup. Schwab requires point-in-time backups, which can restore a database to the state where it was at a particular time.

At Schwab, every PostgreSQL database actually has four backup copies, spread across three distinct regions. They are managed by the [Patroni HA](https://patroni.readthedocs.io/en/latest/) software for PostgreSQL.

![Schwab's High Availability architecture.](https://cdn.thenewstack.io/media/2024/09/4fcf1b1f-schwab-postgres-04.jpg)
Schwab’s High Availability architecture.


## Vendor Support for PostgreSQL
Vendor support was another requirement for adopting any open source software at the financial institution.

“When it comes to databases, we were not comfortable running in open source with no vendor support,” Hegde said.

When the company runs into a big problem it still requires calling a vendor for expedited resolution.

Bringing PostgreSQL to Schwab involves more than just downloading and installing a copy of the database management system. It had to be offered to all employees as a service — this is where the need came in for security, backup and other advanced features.

Despite being open source, PostgreSQL has a number of options for commercial support, including packages from [EDB](https://www.enterprisedb.com/) and [Percona](https://www.percona.com/?utm_content=inline+mention).

Schwab consulted with VMware, which provided a reference architecture, which was used as a starting point. The company has a centralized governance plan for applications, so the deployment had to hit those milestones.

One problematic point with PostgreSQL was that Schwab would be downloading the software from [PostgreSQL](https://www.postgresql.org/) on the Internet. The banking form wanted a more substantial source for downloading, just to ensure the source [doesn’t get corrupted](https://thenewstack.io/linux-xz-backdoor-damage-could-be-greater-than-feared/) by malicious actors.

“When we’re dealing with banks and government agencies, you need to have more protections and insurances about the source domain of the code,” Novick explained.

This version came from [VMware Tanzu](https://tanzu.vmware.com?utm_content=inline+mention), a platform designed to simplify the enterprise development process, and includes [Tanzu Data Solutions](https://tanzu.vmware.com/data), which provides PaaS-ready versions of about 20 open source data-centric applications, including PostgreSQL.

VMware got into the business of supporting PostgreSQL through [Greenplum parallel database](https://thenewstack.io/pivotal-readies-the-greenplum-parallel-processing-database-for-kubernetes/), which was part of [Pivotal when VMware](https://thenewstack.io/vmware-acquires-pivotal-software-for-more-kubernetes-prowess/) acquired in 2020 (Broadcom [acquired](https://thenewstack.io/vmware-to-be-acquired-by-broadcom-in-a-61-billion-deal/) VMware in 2023, and Greenplum was renamed [VMware Tanzu Greenplum](https://tanzu.vmware.com/greenplum)). Greenplum was originally built from PostgreSQL and so Pivotal/VMware built up a deep expertise in PostgreSQL, and so it was a natural fit to start offering customers a “pristine” version of PostgreSQL as well, Novick explained.

VMware takes the source code of these applications, and compiles it on its own “build farm,” along with its own additional open source co. In effect, these open source applications have been vetted by VMware.

## Summary
The banking company then tried out the software to replace the test environment, stressing the software against a long list of probable test cases. A few early adopters then tested the software in a production environment, which helped identify any operational gaps.

At present, Schwab runs several applications of PostgreSQL, but it will soon ramp up an effort to migrate more apps from proprietary databases they are running, such as Oracle.

This means when starting a new project, a team will be given an instance of PostgreSQL to start working with. And the company is generating documentation for helping the managers of other internal apps — those that don’t require some proprietary extensions of some commercial database system — migrate to PostgreSQL.

You can view the whole presentation [here](https://www.vmware.com/explore/video-library/video/6360759651112).

*Disclosure: Broadcom paid travel/lodging for the reporter to attend this conference. *
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)