
<!--
title: Meta开源针对超大规模工作负载的基准测试工具DCPerf
cover: https://cdn.thenewstack.io/media/2024/08/d66decf8-andreas-weilguny-jbsy1gkgfma-unsplash.jpg
-->

一家社交媒体巨头通过五项测试扩展了标准 SPEC 基准测试，以更准确地预测工作负载性能。

> 译自 [Meta Open Sources DCPerf, a Benchmark for Hyperscale Workloads](https://thenewstack.io/meta-open-sources-dcperf-a-benchmark-for-hyperscale-workloads/)，作者 Joab Jackson。

由于受到标准数据中心基准测试的限制，社交媒体巨头 [Meta](https://about.meta.com/?utm_content=inline+mention)（前身为 Facebook）开发了自己的性能测试集，称为 DCPerf，用于衡量其 [超大规模应用程序](https://thenewstack.io/how-meta-patches-linux-at-hyperscale/) 的性能需求，这些应用程序需要数百甚至数千台服务器才能运行。

该公司现在已经根据 [MIT 开源许可证](https://opensource.org/license/mit) 发布了这个基准测试套件（在 [GitHub](https://github.com/facebookresearch/DCPerf) 上），希望它能被学术界、硬件行业和其他互联网公司采用。

“作为一个开源基准测试套件，DCPerf 有可能成为一种行业标准方法，用于捕获在超大规模数据中心部署中运行的计算工作负载的重要工作负载特征，”Meta 工程师 Abhishek Dhanotia、Wei Su、Carlos Torres、Shobhit Kanaujia、Maxim Naumov 在 8 月 5 日发表的一篇 [博客文章](https://engineering.fb.com/2024/08/05/data-center-engineering/dcperf-open-source-benchmark-suite-for-hyperscale-compute-applications/) 中写道。

与传统的企业计算，甚至是基于超级计算机的 [高性能计算](https://thenewstack.io/top500-chinas-supercomputing-silence-aggravates-tech-cold-war-with-u-s/) (HPC) 相比，超大规模计算是一个不同的领域。Meta 的工程师们认为，鉴于数据中心驱动的超大规模计算占据了全球服务器部署的最大市场份额，它需要自己的一套测试。

因此，超大规模计算需要自己的一套评估方法是有道理的。

DCPerf 旨在匹配不同类型的超大规模工作负载，五个基准测试中的每一个都以 Meta 目前正在使用的大型应用程序为模型。

![不同 DCPerf 测试及其构建来源的应用程序表。](https://cdn.thenewstack.io/media/2024/08/ace51ceb-meta-dcperf.png)

*不同的 DCPerf 基准测试基于不同的 Meta 工作负载，每个工作负载都使用不同的技术组合。(来源：Meta)*

这些基准测试支持 [ARM](https://www.arm.com/campaigns/multi-arch-cloud-infrastructure?utm_content=inline+mention) 和 [Intel](https://www.intel.com/content/www/us/en/now/data-centric/overview.html?utm_content=inline+mention) 平台，并且可以支持多租户，以防应用程序跨多个数据中心运行。该测试软件可以在 [CentOS Stream 8/9](https://thenewstack.io/red-hat-deprecates-linux-centos-in-favor-of-a-streaming-edition/) 或 [Ubuntu 22.04 Linux](https://thenewstack.io/how-to-install-ubuntu-pro-on-your-servers/) 上运行。

## 但是 SPEC 呢？

迄今为止，数据中心基准测试的行业标准来自 [Standard Performance Evaluation Corporation](https://www.spec.org/) ([SPEC](https://thenewstack.io/nvidia-h200-gpus-crush-mlperfs-llm-inferencing-benchmark/))。Meta 自己使用 [SPEC 的 CPU 基准测试](https://www.spec.org/benchmarks.html#cpu) 套件进行处理器评估。

DCPerf 扩展了 SPEC CPU，使公司能够确定最佳配置选择，并做出更准确的性能预测。它甚至可以识别硬件和系统软件中的性能错误。

“与 SPEC CPU 等现有基准测试相比，DCPerf 提供了更丰富的应用程序软件多样性，并有助于在平台性能方面获得更好的覆盖信号，”工程师们写道。“由于这些优势，我们也开始使用 DCPerf 来协助我们决定在数据中心部署哪些平台。”

在这篇博文中，工程师们展示了 DCPerf 如何在片上系统微体系结构如何支持 Meta 的应用程序方面提供更细致的结果。

![比较 SpecCPU 和 DCPerf 准确性的图表。](https://cdn.thenewstack.io/media/2024/08/3bf78adb-meta-dcperf-compare.png)

*以下是生产应用程序消耗的平均内核频率 (1.94) 的两种估计值；SpecCPU 2006 年估计的数字为 2.10，而 DCPerf 估计的数字为 1.92。对于像 Meta 这样的大型运营，更准确的预测意味着可以更好地估计要购买多少硬件。(来源：Meta)*

在过去的两年中，Meta 一直与 CPU 供应商合作，对该规范进行外部验证。

## 谷歌也有一个基准测试工具

Meta 并不是唯一拥有自己内部测试套件的超大规模公司。

[Google](https://cloud.google.com/?utm_content=inline+mention) 拥有 [Fleetbench](https://github.com/google/fleetbench)，这是一套七个“微基准测试”，旨在帮助 CPU 和系统软件构建者更好地理解 Google 的超大规模工作负载。

“传统的基准测试通常无法捕捉到”超大规模工作负载的细微差别，Google 研究人员 [在一篇论文中](https://ieeexplore.ieee.org/document/10590038) 详细介绍了 Fleetbench。“创建一套能够代表实际仓库规模计算机所使用工作负载的公共基准测试套件具有挑战性，因为它们通常运行专有的、非公开的软件，并在机密数据上运行。”
