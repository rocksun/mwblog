The hullabaloo over moves away from open source licensing — [HashiCorp/OpenTofu](https://thenewstack.io/how-opentofu-happened-and-whats-next/) anyone? — seems to have settled a bit, but continues in the database sphere.

One vendor bucking that trend is distributed Postgres vendor [pgEdge](https://www.pgedge.com/?utm_content=inline+mention). It recently announced it has gone totally open source and changed licensing on its [Spock](https://github.com/pgEdge/spock) multimaster logical replication extension, [large object logical replication](https://github.com/pgEdge/lolor) (lolor) extension and [Snowflake sequences](https://github.com/pgEdge/snowflake) from its proprietary pgEdge Community License to the Open Source Initiative (OSI)-approved [PostgreSQL License](https://opensource.org/license/postgresql).

The move came at the behest of potential customers, [Phillip Merrick](https://www.linkedin.com/in/phillipmerrick/), cofounder and CEO, explained in an interview.

“We found we were excluded from a lot of the conversations in the Postgres community around our type of technology because the Postgres community, quite rightly, doesn’t want to get on board with anything that’s not open source, and they didn’t consider our community license … to be true open source. So, it just made sense to rip the Band-Aid off and go fully open source.”

Vice President of Engineering [Dave Page explained](https://www.pgedge.com/blog/pgedge-goes-open-source) in a blog post that the previous “source available” license placed some restrictions on the way the components could be used.

Merrick said the previous license allowed users to copy the code, modify it and use it as they wished. The only real prohibition was using the code to compete directly with pgEdge.

“We always saw ourselves as a company committed to open source and the Postgres community. With our distributed Postgres work, we had actually made that open source, but I guess that was open source with a lowercase ‘o’ and lowercase ‘s,’ because we didn’t have it on one of the OSI-approved licenses,” he explained.

Under a source-available license, software source code is made available and can be freely modified and redistributed, though it often restricts commercial or competitive use.

The [Amazon/Elastic tussle](https://thenewstack.io/amazon-elastic-and-the-fight-for-open-source-freedom-in-the-enterprise/) and other instances of cloud providers and other companies taking open source code and using it to compete directly with its creators made pgEdge leery.

“We had some trepidation about that. It turns out, our fears were maybe a little bit unfounded, not entirely unfounded, but a little unfounded. And meanwhile, we knew that there were some customers who really didn’t want to look at our technology unless it was open source, capital ‘O,’ capital ‘S,’ with an OSI-approved license,” Merrick said.

## Interest in Enterprise-Grade Postgres

He said the Postgres market seems to be contracting a bit, while some customers are insisting on products with an [OSI](https://opensource.org/osd)-approved license.

The OSI has rejected both the Business Source License (BSL) and [Server Side Public License (SSPL)](https://opensource.org/blog/the-sspl-is-not-an-open-source-license) as not truly open source. The OpenLogic “[2025 State of Open Source Report](https://www.openlogic.com/system/files/2025-05/report-openlogic-2025-state-of-open-source-support.pdf)” states that after license changes, the OSI no longer lists [MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline+mention), Elasticsearch and CockroachDB as meeting its criteria for open source offerings, though they have been relicensing some components under the OSI-approved [AGPL (GNU Affero General Public License)](https://opensource.org/license/agpl-v3).

IDC analyst [Devin Pratt](https://my.idc.com/getdoc.jsp?containerId=PRF005946) told FastForward that two recently acquired Postgres startups — Neon and Crunchy Data — reflect [market interest in enterprise-grade Postgres](https://fastforward.boldstart.vc/snowflake-snags-crunchy-data-to-get-enterprise-grade-postgres-database/) as well as AI.

[Neon was acquired by](https://www.wsj.com/articles/databricks-to-buy-startup-neon-for-1-billion-fdded971) Databricks as a foundation for its [hosted Lakebase offering](https://thenewstack.io/lakebase-is-databricks-fully-managed-postgres-database-for-the-ai-era/) and to make developing AI agents easier. And Crunchy Data now is part of [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) to be integrated into its [AI Data Cloud](https://thenewstack.io/how-snowflake-redefined-its-data-stack-with-an-ai-first-strategy/).

The interest in enterprise-grade Postgres has prompted pgEdge to diversify as well.

In its enterprise offering, pgEdge has focused on a distributed [multimaster](https://www.pgedge.com/solutions/benefit/multi-master) architecture to [maintain high availability](https://thenewstack.io/how-distributed-postgres-solves-clouds-high-availability-problem/) for critical workloads. It has expanded support for nondistributed as well as distributed Postgres applications.

## Shift Back Toward Open Source Licenses

“After several years of vendors, typically database vendors, moving away from open source licenses to source available alternatives (e.g., BSL, SSPL, etc.), there has been a shift back towards open source licenses — often the AGPL,” [Stephen O’Grady](https://www.linkedin.com/in/sogrady/), Redmonk principal analyst and cofounder, said in email.

Using an admittedly small sample in her study, Redmonk’s [Rachel Stephens](https://www.linkedin.com/in/rachelstephens/) found that companies yielded [minimal business value](https://redmonk.com/rstephens/2024/08/26/software-licensing-changes-and-their-impact-on-financial-outcomes/) or growth in adoption from changing from an open source license to a proprietary one.

“In general, source available licenses can introduce friction to adoption for both developers and enterprises, so some projects have moved back to approved [open source licenses](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/ "open source licenses") offering maximal protection,” O’Grady said.

Redis recently declared itself [open source again](https://thenewstack.io/redis-is-open-source-again/) under the [AGPL v3 license](https://opensource.org/license/agpl-v3). Redis CEO [Rowan Trollope](https://www.linkedin.com/in/rowant) told TNS’s [Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/) the change grew from cloud providers offering hosted Redis on their platforms. The license switch means those vendors now also have to license Redis.

“We believe that the AGPL license provides protection from the [cloud service providers] in that, if they want to offer us as an open source version, which they can do, they have to publish all the code as open source. They have internal policies that say they won’t do that. So we think it’s an effective model,” Trollope told Lardinois.

“If anything, things [software licensing changes] have slowed down here over the last year,” said open source advocate [Dan Lorenc](https://thenewstack.io/author/dan-lorenc/), CEO and co-founder of Chainguard, adding that these changes come in bursts.

He pointed to the [Fair Source project](https://fair.io/about/), an initiative begun in 2024 to address the need for clearer software licensing in open source.

“The Fair Source project has tried to catalyze a shift here by providing a new standard license for software companies to use, but their website shows just how slow this movement is going: seven announcements in 2024, only five so far in 2025,” he said. “Meanwhile, open source continues to grow. [GitHub’s ‘Octoverse’ report](https://github.blog/news-insights/octoverse/octoverse-2024/) most recently showed 25% year-over-year growth in open source projects. If these license changes can’t outpace this growth, they’ll continue to remain a rounding error.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/01/cabe83e0-susan-mug.jpg)

Susan Hall is the Sponsor Editor for The New Stack. Her job is to help sponsors attain the widest readership possible for their contributed content. She has written for The New Stack since its early days, as well as sites...

Read more from Susan Hall](https://thenewstack.io/author/susanhall/)