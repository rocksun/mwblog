<!-- 
title: 2024年4大最便宜的托管Kubernetes提供商排名
cover: ./cover.png
 -->

价格和比较更新至2024年2月10日。

译自 [Top 4 cheapest managed Kubernetes providers in 2024](https://medium.com/@emilmatyjaszewski/cpde-fa2776906266) 。

## 介绍

独自运行Kubernetes可能会非常麻烦，特别是在没有托管控制平面服务的情况下。对于本地测试或开发，Minikube或k3s等轻量级工具可能非常完美，但是在某些场景下，需要一个托管的公共集群。

在本文中，我们将比较来自4个不同云提供商的最负担得起的托管Kubernetes集群。我们将详细说明价格和基本功能。

## 考量因素

通常，在使用云提供商运行托管集群时，其所有底层资源的费用都需要支付。为了找到最具成本效益的解决方案，这些资源的数量显然需要限制并保持尽可能低，以避免不必要的费用。 

运行一个基本的(且最便宜!)Kubernetes集群时，所需的最少云资源是:

1. 计算资源
2. 块存储
3. 负载均衡器

一些云提供商还对控制平面管理收取额外费用，但是这通常会将其排除在最便宜的选择之外，因此在这种情况下我们可以跳过这一点。

## 集群规模

记住我们的唯一目的是找到运行非生产集群的最便宜方式，我们将资源保持在尽可能低的水平，在节点故障的情况下还维持合理的资源余量。

此比较的核心假设是:

- 2个工作节点(静态的，非抢占式的，非竞价实例)
- 每个工作节点至少0.5 GB内存和1个共享vCPU
- 每个工作节点至少20 GB磁盘存储
- 欧洲位置，最好是德国
- 能够向互联网公开应用程序

由于某些云提供商没有完全匹配这些规格的实例，因此选择了最接近的匹配。 

请记住，这些真的是最低可能的规格，因此集群将无法处理诸如以下负载:

- 内存耗尽的应用程序，即Spring应用程序 
- 使用繁重的容器镜像的应用程序，即包含Node.js的node_modules

为了完全适应这些，某些集群规格需要相应地增加，但这超出了本文的范围。

## 云提供商比较

1. Civo — 每月$20

作为2021年推出的托管Kubernetes市场上的最新竞争者之一，它在此比较中是最便宜的。

- 控制平面: 免费
- 节点: 2个 1 GB内存 / 1 vCPU / 30 GB NVMe存储 — 每个$5/月
- 负载均衡器: $10/月
- 总计: $20/月

2. Vultr — 每月$30   

按最低价格计算，下一个提供商是Vultr — 一个不太流行的托管Kubernetes提供商，于2014年推出。考虑到其价格，此选项提供了最多的资源。

- 控制平面: 免费
- 节点: 2个 2 GB内存 / 1 vCPU / 55 GB SSD存储 — 每个$10/月
- 负载均衡器: $10/月
- 总计: $30/月

3. Linode/Akamai — 每月$34

另一个竞争对手是Linode，最近被Akamai收购。他们的定价与之前和下一个选项非常可比。

- 控制平面: 免费
- 节点: 2个 2 GB内存 / 1 vCPU / 50 GB存储 — 每个$12/月
- 负载均衡器: $10/月
- 总计: $34/月

4. DigitalOcean — 每月$36

最后但同样重要的是，DigitalOcean的DOKS服务，结果证明它是与所比较的选项中最昂贵的。 

- 控制平面: 免费
- 节点: 2个 2 GB内存 / 1 vCPU / 50 GB SSD存储 — 每个$12/月
- 负载均衡器: $12/月
- 总计: $36/月

## 结论

大多数调查的云提供商都没有提供低端节点，其中大多数的最小机器甚至有2 GB内存和1 vCPU。

这是一场激烈的竞争，但是在各个类别中有几个赢家:

- 最低价格:Civo($20/月)  
- 最佳性价比:Vultr($30/月)

在选择完美的提供商时，还有一些其他因素需要考虑，例如防火墙产品、包括数据库在内的其他服务、网络流量定价等，但是这两者被证明是用于最小规模Kubernetes集群设置的最佳选择。
