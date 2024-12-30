# What Happens to Relicensed Open Source Projects and Their Forks?
![Featued image for: What Happens to Relicensed Open Source Projects and Their Forks?](https://cdn.thenewstack.io/media/2024/12/62f2b75e-open-source-forks-1024x576.jpg)
Many popular [open source projects](https://thenewstack.io/open-source/) are owned and driven by a single company, and in today’s difficult economic climate, those companies are under [increasing pressure](https://redmonk.com/rstephens/2024/08/26/software-licensing-changes-and-their-impact-on-financial-outcomes/) to deliver a strong return on their investments. One response to this pressure has been relicensing popular open source projects to more restrictive licenses in the hopes of generating more revenue. In some cases, relicensing has [resulted in a hard fork](https://thenewstack.io/why-open-source-forking-is-a-hot-button-issue/) of the original project. These relicensing events and their forks can be disruptive to the organizations and individuals using and contributing to affected open source projects.

Several companies have relicensed their open source projects in the past few years, so the [CHAOSS project](https://chaoss.community/) decided to look at how an open source project’s [organizational dynamics](https://chaoss.community/practitioner-guide-organizational-participation/) evolve after relicensing, both within the original project and its fork. Our research compares and contrasts data from three case studies of projects that were forked after relicensing: Elasticsearch with fork [OpenSearch](https://thenewstack.io/opensearch-how-the-project-went-from-fork-to-foundation), Redis with fork [Valkey](https://thenewstack.io/navigating-the-path-from-redis-to-valkey), and Terraform with fork [OpenTofu](https://thenewstack.io/how-opentofu-happened-and-whats-next).

These relicensed projects and their forks represent three scenarios that shed light on this topic in slightly different ways. The following summarizes what we found when we looked at the data, and you can dive into the details about these six projects in the [paper, presentation and data](https://github.com/chaoss/wg-data-science/tree/main/publications) we shared at the recent [OpenForum Academy Symposium](https://symposium.openforumeurope.org/).

## Elasticsearch and OpenSearch
Almost all contributions to the original Elasticsearch project came from employees of the relicensing company (Elastic), and the fork was created by new contributors and owned by a single company ([Amazon](https://aws.amazon.com/?utm_content=inline+mention)).

### Elasticsearch
Elasticsearch was an open source project under the Apache 2.0 license until Feb. 3, 2021, when the [project was relicensed](https://www.elastic.co/blog/licensing-change) under the Server Side Public License (SSPL) and the Elastic License. On Aug. 29, 2024, it again became an open source project when Elastic announced it was adding the GNU Affero General Public License (AGPLv3) as an additional licensing option, but there isn’t yet enough data to include this in the analysis.

Both before and after the relicense, contributors to the [Elasticsearch repository](https://github.com/elastic/elasticsearch) were mostly Elastic employees; they consistently made over 95% of the lines added to and deleted from Elasticsearch, with almost no participation from contributors outside of Elastic. As a result, the 2021 relicense had little to no impact on contributors, but there was a bigger impact on the users or consumers of Elasticsearch who were forced to decide whether to continue using it, and if so, under which of the two available licenses.

### OpenSearch
OpenSearch was forked from Elasticsearch on April 12, 2021, under the Apache 2.0 license, by the Amazon Web Services (AWS) team so that it could continue to offer this service to its customers. OpenSearch was owned by Amazon until September 16, 2024, when it [transferred the project](https://thenewstack.io/aws-transfers-opensearch-to-the-linux-foundation/) to the Linux Foundation.

As with Elasticsearch, most contributions to the [OpenSearch repository](https://github.com/opensearch-project/OpenSearch) came from Amazon employees, however, to a lesser extent and with increases in organizational diversity over time. In the first year of the fork, a small number of Amazon employees made 80% of total additions and 91% of total deletions to the code. Only two people who didn’t work for Amazon made 10 or more commits, making up 7% of additions and 4% of deletions.

In the final year of the fork under Amazon’s ownership (before the project was moved under the Linux Foundation), its organizational diversity improved, with 63% of additions and 64% of deletions coming from Amazon employees who made 10 or more commits. Six people who didn’t work for Amazon made 10 or more commits, making up 11% of additions and 13% of deletions. In summary, the contributors are mostly from Amazon, but organizational diversity is gradually improving.

## Terraform and OpenTofu
Almost all contributions to the relicensed Terraform project came from employees of the company (HashiCorp), and the fork (OpenTofu) was created by new contributors as a foundation project.

### Terraform
Terraform was under the open source Mozilla Public License v2.0 (MPL 2.0) until Aug. 10, 2023, when it was relicensed along with HashiCorp’s other open source projects (e.g., Vagrant, Vault) to the Business Source License (BSL). Similar to Elasticsearch, the [Terraform repository](https://github.com/hashicorp/terraform) had very few contributors who weren’t HashiCorp employees. In the year before and the year after relicensing, there were only two contributors to Terraform who were not affiliated with HashiCorp, and they both made a very small number of contributions.

Since there were so few contributions from outside of the company, there was no substantial impact on the contributor community from the relicensing event, so the only people affected would likely have been Terraform users.

### OpenTofu
OpenTofu was forked from Terraform on Aug. 25, 2023, by a group of users as a Linux Foundation project under the MPL 2.0. These users were starting from scratch with the codebase since no contributors to the [OpenTofu repository](https://github.com/opentofu/opentofu) had previously contributed to Terraform.

Contributions came from 31 people at 11 organizations who made five or more contributions to the OpenTofu repository in the first year. The most substantial contributions came from Spacelift, whose employees made over half of the additions and deletions. Employees from Env0 and Scalr have also made a few contributions, so there is some organizational diversity across the project.

## Redis and Valkey
The relicensed project (Redis) had significant numbers of contributors who were not employed by the company, and the fork (Valkey) was created by those existing contributors as a foundation project.

### Redis
The Redis project was an open source project under the Berkeley Software Distribution 3-clause (BSD-3) until March 20, 2024, when the project was relicensed under the Redis Source Available License (RSALv2) and the SSPLv1. This was contrary to the [2018 Redis blog post](https://redis.io/blog/redis-license-bsd-will-remain-bsd/) stating that the Redis open source project would always remain under the BSD license.

The Redis project differs from Elasticsearch and Terraform in the number of contributions to the [Redis repository](https://github.com/redis/redis) from people who were not employees of Redis. In the year leading up to the relicense, when Redis was still open source, there were substantial contributions from employees of other companies: Twice as many non-Redis employees made five or more commits, and about a dozen employees of other companies made almost twice as many commits as Redis employees made.

In the six months after the relicense, all of the external contributors from companies (including Amazon, Alibaba, Tencent, Huawei and Ericsson) who contributed over five commits to the Redis project in the year prior to the relicense stopped contributing. In sum, Redis had strong organizational diversity before the relicense, but only Redis employees made significant contributions afterward.

### Valkey
[Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/) was forked from Redis 7.2.4 on March 28, 2024, as a Linux Foundation project under the BSD-3 license. The fork was driven by a group of people who previously contributed to Redis with public support from their employers. Within its first six months, the [Valkey repository](https://github.com/valkey-io/valkey) had 29 contributors employed at 10 companies, and 18 of those people previously contributed to Redis. Valkey has a diverse set of contributors from various companies, with Amazon having the most contributors.
## Next Steps
This is the first step in a much larger research project underway within the [CHAOSS Data Science Working Group](https://github.com/chaoss/wg-data-science/tree/main/dataset/license-changes/fork-case-study). To date, we’ve only looked at the primary repository and organizational affiliation data for each project, so we’re working toward including more repositories and additional metrics to better understand the project health dynamics within these projects. We also might expand to look at other projects that were forked after being relicensed.

Looking at all of these projects together, we see that the forks from relicensed projects tend to have more organizational diversity than the original projects. This is especially true when the forks are created under a neutral foundation, like the Linux Foundation, rather than forked by a single company.

It is still too early to understand the ultimate success or failure of these projects — both the original and the fork. The new forks have more organizational diversity, and projects with greater organizational diversity tend to be more sustainable. However, we don’t yet know if this will be true for these projects, especially for companies that continue struggling to meet their investors’ expectations.

*CHAOSS will take part in State of Open Con, a conference covering open source software, open hardware, open data, open standards and AI openness on Feb. 4 and 5 in London. Alex Williams, founder and publisher of The New Stack, will moderate a track on the future of open source.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)