<!--
title: Runpod报告：Qwen力压Meta Llama，登顶最受欢迎自托管大模型
cover: https://cdn.thenewstack.io/media/2026/03/bfdbbc98-getty-images-2e66tpvgzn8-unsplash-scaled.jpg
summary: Runpod报告显示，Qwen已超越Llama成为部署最多的自托管LLM，Llama 4采用率极低。AI视频更侧重优化而非生成。ComfyUI主导图像生成。AI实际应用重视性能、效率和工作流控制。
-->

Runpod报告显示，Qwen已超越Llama成为部署最多的自托管LLM，Llama 4采用率极低。AI视频更侧重优化而非生成。ComfyUI主导图像生成。AI实际应用重视性能、效率和工作流控制。

> 译自：[Runpod report: Qwen has overtaken Meta's Llama as the most-deployed self-hosted LLM](https://thenewstack.io/runpod-ai-infrastructure-reality/)
> 
> 作者：Adrian Bridgwater

代理式AI服务的兴起，使得企业技术市场焕发活力，涌现出一套全新、完全成熟的自动化和加速工具，几乎可应用于所有行业垂直领域的所有用例。这是目前行业领导者、AI布道者乃至政治家们宣扬的，略显俗套的口号。

基础设施专家[Runpod](https://www.runpod.io/)看到了一个略有不同的现实，其形态可能有助于开发者专注于哪些AI工具和服务正在获得最实际、最功能性的部署。

它之所以能做到这一点，是因为它能够作为一个专为AI构建的GPU实例平台。该公司提供按需Pod、自动扩缩的无服务器端点以及即时集群服务，以运行分布式训练工作负载。

因此，Runpod负责监管其所谓的AI工作负载背后的“原始基础设施消耗量”，这使其能够独特的视角，洞察哪些模型实际部署了。它还可以评估模型是用于推理、微调还是训练，并识别选择了哪些GPU以及工作负载的来源。

## 匿名无服务器部署日志

Runpod的《AI现状报告》并非基于基准测试、调查或人工评估的排行榜。相反，这项分析是基于Runpod平台上的匿名无服务器部署日志，该公司称该平台目前为全球超过50万开发者提供服务。

“我们建立了内部管道来大规模分类模型使用情况，对生产日志进行了基于LLM的分析，将工作负载映射到GPU选择模式，并利用IP情报了解地理分布。结果并非传闻。它是行为驱动的，”Runpod数据主管[Charlotte Daniels](https://www.linkedin.com/in/danielscharlotte/)在[一篇博文](https://www.runpod.io/blog)中写道。

## 驳斥公众论调

AI工作负载实际投入生产的这份记录，与一些大品牌背后的宣传机器所宣扬的截然不同。Runpod表示，这在实际层面上“驳斥了大部分公众论调”。

这里提供的现实检验之一是，Qwen — *而非*Llama — 现在是部署最多的自托管LLM。Qwen由阿里云创建和开发，是一个[开放权重LLM系列](https://www.alibabacloud.com/en/solutions/generative-ai/qwen?_p_lc=1)，以其在文本、音频和视觉应用模式中同时工作的复杂推理能力而闻名。

> “引人注目的是，Llama 4的采用率接近于零。生态系统尚未发生有意义的迁移……开发者们正在优化每美元的性能、延迟、兼容性和微调。”

尽管其功能强大（以及对多模态应用的明显吸引力），Runpod指出Qwen在声量方面明显低于Meta在[基准测试](https://virtualizationreview.com/articles/2024/04/19/llama-3-ranking.aspx)、[X（前身为Twitter）帖子](https://x.com/AIatMeta/status/1908598456144531660)和[会议幻灯片](https://www.ibm.com/think/news/meta-llamacon-2025)中推广Llama的强大能力。

“更令人惊讶的是：Llama 4的采用率几乎为零。尽管有发布报道和关注，但生态系统并未发生有意义的迁移。AI软件工程市场是务实的。它优化每美元的性能、延迟、兼容性以及微调生态系统的存在，”Daniels写道。

## 渲染扼杀了视频明星

在整个AI领域中，另一个新兴领域是视频。旨在为模型发布和产品演示等用例制作文本到视频电影演示的服务受到了广泛关注。Synthesia、Runway和[CraftStory](https://www.computerweekly.com/blog/CW-Developer-Network/CraftStory-developers-expand-extend-AI-video-generation-services)等供应商已进入这一领域，承诺在几分钟内创建电影级AI视频。

如果这一概念能够像专注于这些技术的组织所承诺的那样全面运作，那么原始的基础设施消耗将表明大规模的升级。

这意味着，AI视频测试案例将被原型化，开发者会欣喜若狂并订购更多披萨，部署将升级以容纳更多空间……团队将比Martin Scorsese与Robert de Niro进行一场醉醺醺的重聚午餐更快地转向项目的长篇版本。

“生产行为讲述了一个不同的故事：升级工作负载的数量大约是生成工作负载的两倍。团队并没有将所有赌注押在一次昂贵的渲染上；相反，他们会快速生成低分辨率草稿，选择优秀方案，然后分配计算资源进行增强。先尝试，再精炼，”Daniels解释道。

所有这些都揭示了AI数据中心资源资本分配的一个真相。简而言之，优化正在消耗比原始创建更多的GPU时间。

## ComfyUI成为主流

对于图像任务，Runpod表示ComfyUI已成为“事实上的图像生成标准”，以其基于节点的方法支持了超过三分之二的图像端点。该公司关于此主题的完整报告指出，这种主导地位“反映了向模块化、可定制管道的更广泛转变”，而非简单的文本到图像调用。

Runpod给开发者的建议是，如果你正在构建图像生成工作流，那么投资ComfyUI专业知识变得越来越重要，因为生态系统已在此汇聚。

从大局来看，这项分析指出，使用Runpod AI基础设施的组织中，近三分之二位于纯AI服务之外的行业。或许不足为奇的是，健康科技（HealthTech）和金融科技（FinTech）在企业垂直领域中处于领先地位。

最终结果似乎远不如那些承诺易于部署、一键式AI服务的警报信息那样光鲜亮丽。相反，原始的基础设施消耗表明，生产级AI的使用模式正在围绕性能、效率和工作流控制进行整合。