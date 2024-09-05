
<!--
title: Elastic意外回归开源背后的原因是什么？
cover: https://cdn.thenewstack.io/media/2024/09/936b67b8-https-thenewstack.io-whats-behind-elastics-unexpected-return-to-open-source.jpg
-->

随着 Elastic 改变 Elasticsearch 和 Kibana 的许可证，其转变似乎更像是一种商业策略，而不是拥抱公共资源。

> 译自 [What's Behind Elastic's Unexpected Return to Open Source?](https://thenewstack.io/whats-behind-elastics-unexpected-return-to-open-source/)，作者 Steven J Vaughan-Nichols。

你说什么？在 Elastic 将 Elasticsearch 的开源 Apache 许可证改为半专有的 Server Side Public License 三年后，[Elastic](https://www.elastic.co/) 正在回归开源。

我承认我的错误。我密切关注开源公司政策，但我没有预料到这一点。在令人惊讶的事件中，Elastic，这家提供流行的搜索和分析引擎 [Elasticsearch](https://www.elastic.co/elasticsearch) 及其可视化仪表板 [Kibana](https://www.elastic.co/kibana) 的公司，宣布其核心产品将回归 [开源许可](https://ir.elastic.co/news/news-details/2024/Elastic-Announces-Open-Source-License-for-Elasticsearch-and-Kibana-Source-Code/default.aspx)。这一决定是在该公司 [从 Apache 2.0 许可证转向争议性举措](https://www.zdnet.com/article/elastic-changes-open-source-license-to-monetize-cloud-service-use/) 三年后做出的。

当时，[Shay Banon](https://www.linkedin.com/in/kimchy/)，Elastic 的创始人兼 CTO，在其公司博客的一篇文章中宣称，[Amazon Web Services (AWS)](https://aws.amazon.com/?utm_content=inline+mention) 和 Amazon Elasticsearch Service 正在 [损害 Elastic 的业务](https://www.elastic.co/blog/why-license-change-aws)，因为他们“拿走了我们的 Elasticsearch 和 Kibana 产品，并直接将其作为服务提供，而没有与我们合作”。

结果，正如任何关注 [开源](https://thenewstack.io/open-source/) 的人所预料的那样，AWS 等公司对 Elasticsearch 进行了分叉。事实上，Banon 在周四发布的一篇公司博客文章中写道，当 Elastic 更改许可证时，他知道“这会导致 Elasticsearch 的分叉，它将拥有不同的名称和不同的发展轨迹”。

好吧，他猜对了。此外，AWS 的分叉，OpenSearch，[已经取得了成功](https://www.infoworld.com/article/2338432/somehow-opensearch-has-succeeded.html)。

情况已经发生了变化。现在，Banon 在新的博客文章中写道，Elastic 将为 Elasticsearch 和 Kibana 添加 [GNU Affero 通用公共许可证 (AGPL)](https://www.gnu.org/licenses/agpl-3.0.en.html) 作为第三种许可选项，与 [Elastic 许可证 (ELv2)](https://www.elastic.co/licensing/elastic-license) 和 [Server Side Public License (SSPL)](https://www.mongodb.com/legal/licensing/server-side-public-license) 并列。与其他两种许可证不同，AGPL 长期以来一直被 [开源倡议 (OSI)](https://opensource.org/) 认可为真正的开源许可证。

OSI 则很高兴 Elastic 回归。在给 The New Stack 的一封电子邮件中，OSI 执行董事 [Stefano Maffulli](https://www.linkedin.com/in/maffulli/) 写道：“我们很高兴欢迎 Elastic 回归开源生态系统”。

他补充说：“他们选择强大的 copyleft 许可证表明了这种许可证模式及其双重效应的持续重要性：一是它旨在保护用户下游的自由，二是它也赋予单一供应商开发人员对项目的强大控制权”。

## ‘兴奋地跳来跳去’

因此，Elasticsearch 和 Kibana 再次成为开源软件。具有讽刺意味的是，这仅仅是在 Cockroach Labs，另一家从开源转向半专有许可证的公司，[转向专有许可证](https://thenewstack.io/cockroach-rescinds-open-core-for-a-free-enterprise-version/) 几天后发生的。（它正在消除其精简的开源版本数据库；一个更强大的免费版本，没有企业支持，将提供给年收入低于 1000 万美元的组织）。

Elastic 为什么会做出这种重大的许可策略转变？Banon 在他的博客文章中宣称：“我们与 AWS 的合作关系比以往任何时候都更加牢固”。事实上，“我们甚至被评为 AWS 年度合作伙伴”。此外，“市场混乱（大部分）已经解决”。

混乱？Banon 似乎指的是 AWS 使用“Amazon Elasticsearch Service”来指代其 Elasticsearch 产品。但是，[该商标争议已于 2022 年解决](https://www.elastic.co/blog/elastic-and-amazon-reach-agreement-on-trademark-infringement-lawsuit)。尽管如此，正如 [Simon Willison](https://thenewstack.io/pyconus-simon-willison-on-hacking-llms-for-fun-and-profit/)，开源开发者和 Django 框架的共同创建者，在他的博客中写道，“我不完全相信这种解释，但如果它能引发 [其他不再是开源公司的公司回归的趋势](https://simonwillison.net/2024/Aug/29/elasticsearch-is-open-source-again/)，我完全支持！”

我也是！

Banon 一再声称，Elastic 对重回开源感到非常高兴。“Elasticsearch 和 Kibana 现在可以再次被称为开源软件，”他在最新博客文章的开头写道。“很难用语言表达这个声明让我有多高兴。我简直要兴奋得跳起来了。我们 Elastic 的所有人都是这样。开源在我的 DNA 里。它也在 Elastic 的 DNA 里。能够再次称 Elasticsearch 为开源软件，真是无比的喜悦。”

作为一名从一开始就支持开源的人，我对此感到有些过分。然而，如果 AGPL 许可证能促进 Elasticsearch 和 Kibana 的更广泛采用，这对 Elastic 来说将是一件好事。

然而，开源社区中的一些人仍然对 Elastic 对开源原则的长期承诺持怀疑态度。[Peter Zaitsev](https://thenewstack.io/author/peter-zaitsev/)，[Percona](https://www.percona.com/?utm_content=inline+mention) 的创始人，在推特上表示这是一个“好消息”，但想知道“社区的信任是否能像这样轻易地恢复”。

> 好消息 - Elastic 现在可以在 Open Source AGPLv3 许可证下使用。我想知道社区的信任是否能像这样轻易地恢复
>
> [https://t.co/L24NpJrClt][#opensource]— Peter Zaitsev (@PeterZaitsev)
>
> [2024 年 8 月 30 日]

## 市场力量

在商业方面，Elastic 宣布重回开源的同时，也发布了其[最新季度的收益报告](https://www.businesswire.com/news/home/20240828810610/en/Elastic-Reports-First-Quarter-Fiscal-2025-Financial-Results)。

总体结果相当不错。该公司总收入为 3.47 亿美元，同比增长 18%，Elastic Cloud 收入为 1.57 亿美元，同比增长 30%。这超过了收入和盈利能力的预期上限。

也就是说，股市并不喜欢 Elastic 首席执行官 [Ash Kulkarni](https://www.linkedin.com/in/kulkarniashutosh/) 在收益报告中的声明：“我们在今年开局较慢，客户承诺量受到年初我们进行的细分调整的影响，这些调整的完成时间比预期要长。我们一直在采取措施解决这个问题，但这将影响我们今年的收入。”

当我说市场不喜欢这个消息时，我的意思是市场 *真的* 不喜欢。[Elastic 的股价下跌了 26%，至 79.96 美元](https://www.barrons.com/articles/elastics-stock-earnings-3de2fb5a)；在过去一年中，该股下跌了 32%，而[标准普尔 500 指数上涨了](https://www.barrons.com/market-data/indexes/spx?mod=article_chiclet) 18%。

我怀疑股市专家会关注开源开发者和许可证。也就是说，看看这种令人惊讶的许可证变更将如何影响 Elastic 的产品和股价将会很有趣。
