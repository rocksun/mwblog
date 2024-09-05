# What’s Behind Elastic’s Unexpected Return to Open Source?
![Featued image for: What’s Behind Elastic’s Unexpected Return to Open Source?](https://cdn.thenewstack.io/media/2024/09/936b67b8-https-thenewstack.io-whats-behind-elastics-unexpected-return-to-open-source-1024x576.jpg)
Excuse me? Three years after [Elastic dumped Elasticsearch’s open source Apache license](https://thenewstack.io/amazon-elastic-and-the-fight-for-open-source-freedom-in-the-enterprise/) for a semi-proprietary Server Side Public License, [Elastic](https://www.elastic.co/) is returning to open source.

Mea culpa. I follow open source corporate policies closely, and I didn’t see this coming. In a surprising turn of events, Elastic, the company behind the popular search and analytics engine [Elasticsearch](https://www.elastic.co/elasticsearch) and its visualization dashboard [Kibana](https://www.elastic.co/kibana), has announced a return to [open source licensing for its core products](https://ir.elastic.co/news/news-details/2024/Elastic-Announces-Open-Source-License-for-Elasticsearch-and-Kibana-Source-Code/default.aspx). This decision comes three years after the [company’s controversial move away from the Apache 2.0 license](https://www.zdnet.com/article/elastic-changes-open-source-license-to-monetize-cloud-service-use/).

Then, [Shay Banon](https://www.linkedin.com/in/kimchy/), Elastic’s founder and CTO, declared in a post on his company’s blog that [Amazon Web Services (AWS)](https://aws.amazon.com/?utm_content=inline+mention) and Amazon Elasticsearch Service was [hurting Elastic’s business](https://www.elastic.co/blog/why-license-change-aws) by “taking our Elasticsearch and Kibana products and providing them directly as a service without collaborating with us.”

The result, as could have been predicted by anyone who follows [open source](https://thenewstack.io/open-source/), was that AWS, among others, forked Elasticsearch. Indeed, Banon wrote in a company blog published Thursday that when Elastic changed the license, he knew “it would result in a fork of Elasticsearch with a different name and a different trajectory.”

Well, he got that right. Moreover, AWS’s fork, OpenSearch, [has proved successful.](https://www.infoworld.com/article/2338432/somehow-opensearch-has-succeeded.html)

Things have changed. Now, Banon wrote in the new blog post that Elastic would be adding the [GNU Affero General Public License (AGPL)](https://www.gnu.org/licenses/agpl-3.0.en.html) as a third licensing option for Elasticsearch and Kibana, alongside its [Elastic License (ELv2)](https://www.elastic.co/licensing/elastic-license) and [Server Side Public License (SSPL)](https://www.mongodb.com/legal/licensing/server-side-public-license). Unlike the other two, the AGPL has long been recognized by the [Open Source Initiative (OSI)](https://opensource.org/) as a true open source license.

The OSI, in return, is happy to have Elastic back. In an email to The New Stack, [Stefano Maffulli](https://www.linkedin.com/in/maffulli/), the OSI’s executive director, wrote, “We are delighted to welcome Elastic back into the open source ecosystem.”

He added, “Their choice of a strong copyleft license signals the continuing importance of that license model and its dual effect: one, it’s designed to preserve the user’s freedoms downstream, and two, it also grants strong control over the project by the single-vendor developers.”

## ‘Jumping Up and Down With Excitement’
So, once more, Elasticsearch and Kibana are open source. Ironically, this came only days after Cockroach Labs, another company that scuttled from open source to a semi-proprietary license, [shifted to a proprietary license](https://thenewstack.io/cockroach-rescinds-open-core-for-a-free-enterprise-version/). (It is eliminating its stripped-down, open-core version of its database; a more robust free version, without enterprise support, will be available to organizations with less than $10 million in annual revenue.)

Why is Elastic making this significant shift in licensing strategy? In his blog post, Banon proclaimed, “Our partnership with AWS is stronger than ever.” In fact, “We were even named AWS partner of the year.” Besides, “the market confusion has been (mostly) resolved”

Confusion? Banon appears to be referring to AWS’s use of “Amazon Elasticsearch Service” to refer to its Elasticsearch offering. But, that [trademark dispute was resolved in 2022](https://www.elastic.co/blog/elastic-and-amazon-reach-agreement-on-trademark-infringement-lawsuit). Still, as [Simon Willison,](https://thenewstack.io/pyconus-simon-willison-on-hacking-llms-for-fun-and-profit/) noted open source developer and co-creator of the Django framework, wrote on his blog, “I’m not entirely convinced by this explanation, but if it kicks off a [trend of other no-longer-open-source companies returning to the fold](https://simonwillison.net/2024/Aug/29/elasticsearch-is-open-source-again/) I’m all for it!

Me too!

Banon also claimed, over and over again, that Elastic is pleased as punch to be open source once more. “Elasticsearch and Kibana can be called Open Source again,” he wrote in the opening of his latest blog post. “It is hard to express how happy this statement makes me. Literally jumping up and down with excitement here. All of us at Elastic are. Open source is in my DNA. It is in Elastic DNA. Being able to call Elasticsearch Open Source again is pure joy.”

This strikes me, as an open source supporter since day one, as a bit much. However, if the AGPL license encourages the wider adoption of Elasticsearch and Kibana, it will work out well for Elastic.

However, some in the open source community remain skeptical about Elastic’s long-term commitment to open source principles. [Peter Zaitsev](https://thenewstack.io/author/peter-zaitsev/), founder of [Percona](https://www.percona.com/?utm_content=inline+mention), tweeted that it was “Great News” but wondered “if community trust can be reclaimed as easily as well.”

Great News – Elastic is now available under Open Source AGPLv3 license. I wonder if community trust can be reclaimed as easily as well

[https://t.co/L24NpJrClt][#opensource]— Peter Zaitsev (@PeterZaitsev)

[August 30, 2024]
## Market Forces
On the business side, as Elastic announced its return to open source, the company also released its [latest quarter’s earning report](https://www.businesswire.com/news/home/20240828810610/en/Elastic-Reports-First-Quarter-Fiscal-2025-Financial-Results).

The overall results were quite good. The company’s total revenue was $347 million, an increase of 18% year-over-year, and its Elastic Cloud revenue was $157 million, an increase of 30% year-over-year. This outperformed the high end of guidance for both revenue and profitability.

That said, the stock market didn’t like Elastic CEO [Ash Kulkarni’s](https://www.linkedin.com/in/kulkarniashutosh/) statement in the earnings report: “We had a slower start to the year with the volume of customer commitments impacted by segmentation changes that we made at the beginning of the year, which are taking longer than expected to settle. We have been taking steps to address this, but it will impact our revenue this year.”

When I say the market didn’t like this, I mean the market *really* didn’t like it. [Elastic’s shares dropped 26%, to $79.96](https://www.barrons.com/articles/elastics-stock-earnings-3de2fb5a); over the year, the stock fell 32%, as the [S&P 500 gained](https://www.barrons.com/market-data/indexes/spx?mod=article_chiclet) 18%.

I doubt that stock market mavens pay much attention to open source developers and licenses. That said, it will be interesting to see how this surprising license shift affects Elastic’s products and stock price.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)