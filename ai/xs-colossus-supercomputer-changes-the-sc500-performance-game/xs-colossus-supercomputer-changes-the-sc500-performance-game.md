
<!--
title: X的巨型计算机改变了SC500性能游戏
cover: https://cdn.thenewstack.io/media/2024/11/06b7cb90-xai.png
-->

X.AI刚刚安装完成Colossus，这是世界上最大的AI超级计算机。微软、谷歌、Facebook、亚马逊和Oracle等超大规模云服务提供商也正在投入数十亿美元。

> 译自 [X's Colossus Supercomputer Changes the SC500 Performance Game](https://thenewstack.io/xs-colossus-supercomputer-changes-the-sc500-performance-game/)，作者 Agam Shah。

对于计算硬核玩家来说，性能是不可协商的——[AI服务](https://thenewstack.io/ai/) 的快速响应与他们家用电脑中最新GPU的速度一样重要。

像X公司的巨型计算机Colossus这样的令人难以置信的AI超级计算机正在取代传统系统，而这些系统间接地影响着用户的整体计算体验。

硬件专家们现在正在关注新的计算现实。随着新的AI超级计算机取代传统系统，旧的系统性能衡量方法正在被淘汰。

本周，Top500组织[发布了一个列表](https://top500.org/)，其中包含世界上[最快的超级计算机](https://thenewstack.io/sc500-microsoft-now-has-the-third-fastest-computer-in-the-world/)。根据该列表，美国能源部拥有三台[世界上最快的超级计算机](https://thenewstack.io/top500-chinas-supercomputing-silence-aggravates-tech-cold-war-with-u-s/)。

30多年来，Top500榜单一直是记录传统计算机速度进步的权威文件。AI超级计算机正在颠覆这一趋势，并可能使Top500榜单成为过去时代的遗物。Top500通常每年发布两次榜单。

最新的Top500榜单有一个新的领导者，劳伦斯利弗莫尔的El Capitan，其性能达到1.74 exaflops，其次是之前排名第一的ORNL的1.35-petaflop Frontier，然后是阿贡的1.01 exaflops Aurora。

## 淘汰旧的

传统计算和AI是两种根本不同的数据处理方式，它们的性能衡量方法也不同。它们不能同时包含在同一个列表中。

大型云服务提供商正在通过拆除老式数据中心和非AI服务器来为AI服务器让路。人们对用于数据库、ERP和Web服务的传统系统兴趣较小。

[X.AI](https://x.ai/about)刚刚完成了Colossus的安装，它是世界上最大的AI超级计算机。Colossus用于训练Grok 3。它拥有的GPU数量超过世界上任何已知的传统超级计算机。X尚未公布Colossus的系统性能，但如果将其作为传统计算机进行基准测试，它很容易进入前十名。

大型云服务提供商微软、谷歌、Facebook、亚马逊和Oracle正在斥资数十亿美元用于拥有数千个GPU的AI超级计算机。

## 架构变化

几十年来，CPU定义了传统计算机的性能。科学家们表示摩尔定律已经失效，随之而来的是CPU扩展也即将停滞。

GPU是提升性能的方式。GPU也是AI系统的焦点，而CPU更多地充当调度器的角色。

随着英伟达和AMD每年发布新的GPU架构，GPU性能只会不断提高。

英伟达明年将推出Blackwell GPU来取代Colossus中使用的Hopper H100 GPU。根据独立组织MLPerf发布的基准测试结果，Blackwell的性能大约是H100的两倍。

大型云服务提供商正在部署为GPU设计的新的服务器。Oracle即将推出的Colossus杀手将拥有多达131,072个Nvidia GPU，据该公司称，“这比Frontier超级计算机多三倍以上，比其他大型云服务提供商多六倍以上”。

AI超级计算机拥有更大的内存和存储空间，并优先考虑组件之间更快的通信。

## 技术差异

传统计算和AI超级计算机的计算方式不同。根本的区别在于对查询响应的精度。更高的位数通常表示计算精度更高。

传统系统计算准确并提供精确的答案。这需要同时使用最多的64位或32位计算资源来生成最佳答案。系统在64位或32位计算下运行温度更高。

Top500运行64位基准测试来衡量处理器回答查询所需的时间。高精度计算对于金融预测和科学计算至关重要，这些领域严重依赖数据准确性。

AI则不同。计算风格更类似于猜测，答案准确性会随着时间的推移而提高。这些系统优先考虑计算效率而不是数值精度。

Top500组织者现在正在努力寻找对最快的AI服务器进行排名的方法。

AI计算使用4位到16位的数据类型，这些数据类型的精度低于64位。AI超级计算机向用户提供可能的答案，GPU并行工作以根据查询和数据趋势提高准确性。随着系统学习更多内容，答案会变得更准确。

开源生成式AI模型Llama和Gemma的分支已被量化到8位和4位，以用于速度和内存容量有限的移动设备。

AI基准测试还必须考虑模型的响应质量和相关性，这使得硬件测量变得复杂。4位量化模型将更快，但精度远低于8位量化AI模型。

独立组织[MLPerf制定了规则](https://thenewstack.io/nvidia-h200-gpus-crush-mlperfs-llm-inferencing-benchmark/)，根据任务（训练或推理）、生成式AI模型、量化和其他规范来衡量AI速度。

包括英伟达、谷歌、英特尔和AMD在内的芯片制造商通过MLPerf发布AI基准测试结果。

## 新技术的加入

Top500组织者Erich Strohmaier去年推测，传统超级计算到2030年将无法达到10艾弗洛普斯。英特尔在2021年[宣布](https://www.intel.com/content/www/us/en/newsroom/news/innovation-cloud-edge-news.html#gs.0x7ak1)传统计算速度将在2027年达到泽塔弗洛普斯。

微软的561拍弗洛普斯Eagle超级计算机在Top500中排名第四，也是前十名中唯一一个商业云系统。Azure系统结合了Ubuntu Linux、英伟达的H100 GPU和英特尔的第四代至强处理器。

云提供商没有向Top500提交基准测试结果，因为这将耗费时间和金钱。这样做会使系统无法为客户访问数天或数周，而这在AI需求激增的情况下是不切实际的。

一些AI硬件无法获得，因为组件无法现货购买。谷歌正在使用其自研的TPU（无法现货购买）来运行其AI工作负载。同样，AWS的Trainium AI芯片只能通过其云服务获得。

Top500组织者现在正在努力寻找对最快的AI服务器进行排名的方法。

该组织有一个名为HPL-MxP的基准测试，涵盖混合精度测量。它考虑了4位到16位的数据类型来衡量超级计算机的AI速度。HPL-MxP将与将AI与传统工作负载合并的科学家相关。

专家们本周还在SC2024超级计算会议上聚会，寻找衡量AI速度的方法。X.AI的Colossus超级计算机将成为讨论的重要内容。

英伟达将Colossus归类为世界上最大的加速系统。

这台超级计算机的建造速度创下了纪录，“从设备交付到训练仅用了19天，并在122天内全面投产，”英伟达加速计算总监Dion Harris说。

Colossus的性能数据尚未公布，但Harris表示，“X对系统的性能感到非常满意。”

Harris说：“此次部署为大规模AI设定了新的标准。”