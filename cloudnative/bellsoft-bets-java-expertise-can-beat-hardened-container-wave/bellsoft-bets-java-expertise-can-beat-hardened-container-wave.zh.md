加固容器市场随着风险投资和初创企业的涌入而日益火爆，但[Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/)平台提供商[BellSoft](https://bell-sw.com/)认为，其八年来构建Java运行时积累的经验，赋予了它他人所不具备的优势：即对这些安全容器内部实际运行的内容的专业知识。

该公司于去年11月在亚特兰大举行的[KubeCon大会](https://thenewstack.io/kubecon-vclusters-k8s-platform-to-manage-gpus-as-a-service/)上推出了其[BellSoft加固镜像](https://bell-sw.com/bellsoft-hardened-images/)，寄望能在这个由[Chainguard](https://www.chainguard.dev/?utm_content=inline+mention)开创先河、众多初创企业纷纷涌入的领域中脱颖而出。BellSoft的切入点在于，它不仅仅是为容器增加安全性——它还在优化Java工作负载本身。

“容器市场正在兴起，”BellSoft联合创始人兼首席执行官Alexander Belokrylov在接受*The New Stack*采访时表示。“我看到风险投资者投入了大量资金，看起来他们认为这个市场有潜力。”

Belokrylov表示，BellSoft正在解决的问题是真实的。根据负责安全研究的Forrester Research分析师Janet Costello Worthington的说法，当开发团队使用基础镜像时，他们通常会继承一个巨大的攻击面，包括不必要的软件包、shell、编译器、包管理器以及可能包含已知但尚未解决漏洞的未使用库。

“这可能导致补丁混乱、紧急重建，甚至生产故障，”她说。“加固容器剥离了这些不必要的组件，降低了漏洞利用的风险，并简化了容器管理。”

与此同时，Java正面临一个特殊的漏洞问题：[44%的Java服务包含已知的被利用漏洞](https://www.datadoghq.com/state-of-devsecops/)，相比之下，[Go](https://thenewstack.io/introduction-to-go-programming-language/)的这一比例为5%，其他语言仅为2%。典型的容器镜像携带[600个已知漏洞](https://www.netrise.io/resources-whitepaper-brief/supply-chain-visibility-risk-study-edition-2)，其中近一半已存在多年。过去一年中，三分之二的组织曾发生容器安全事件。

## BellSoft的独特之处

BellSoft认为其差异化优势不仅在于构建安全的容器——更在于理解容器内部的内容。该公司是[OpenJDK](https://thenewstack.io/microsoft-releases-its-own-distro-of-java-21/)排名前五的贡献者之一。

“我们的差异化优势在于对我们提供的技术拥有深厚的技术专长，”Belokrylov说。“我们不仅仅是软件构建专家；我们是这类项目的专家。”

这种专业知识始于三年前的[Alpaquita Linux](https://bell-sw.com/alpaquita-linux/)，这是一个类似Alpine的操作系统，最初是一个Java优化项目。“最初，我们的想法是优化[Linux](https://thenewstack.io/introduction-to-linux-operating-system/)以运行Java工作负载，”Belokrylov说。“然而，事实证明，为Java工作负载优化的Linux，几乎可以优化一切。”

现在，BellSoft为.NET、C/C++、[JavaScript](https://thenewstack.io/introduction-to-javascript/)、[Python](https://thenewstack.io/how-python-grew-from-a-language-to-a-community/)和Go提供加固镜像——所有这些都具有接近零的常见漏洞和暴露（CVEs）并提供技术支持。该公司声称，其[Liberica JDK Lite](https://bell-sw.com/libericajdk/)比标准Java镜像的漏洞少95%，并可节省高达30%的资源。

根据Costello Worthington的说法，提供加固容器镜像的供应商通过解决关键的安全和操作挑战来提供价值。

“这些镜像具有更小的臃肿度、更少的继承漏洞、安全的默认配置以及更小的攻击面，”她说。“加固镜像还通过来源、证明和详细说明内部内容的软件物料清单提供必要的透明度。”

## 竞争激烈的领域

Belokrylov表示，在KubeCon大会上他看到了许多竞争对手。Chainguard在开创加固容器方面做得“非常好”，但新的参与者正在涌现。“有许多初创公司或多或少地在做同样的事情，但它们都是从零开始的，”他说。

Chainguard首席执行官Dan Lorenc承认了市场突然涌入的现象。“从某种程度上看，这个领域在过去一年里变得如此拥挤，令人有些费解，”他在接受*The New Stack*采访时表示。“我们三年前就开始做了，因为当时显然有这个需求。”

但Lorenc认为加固容器产品的大量出现是一个更深层次问题的症状。

“软件供应链已破裂，近期加固容器产品的大量涌现是行业的反应，”他在*The New Stack*的[一篇文章](https://thenewstack.io/hardened-containers-dont-fix-a-broken-software-supply-chain/)中写道。“行业的回应是在生产线末端加强检查（更多的检查、更多的扫描器），却在很大程度上忽视了组件如何从上游采购、组装和验证。”

在这篇文章中，Lorenc还写道：“真正的问题在于信任软件的来源，以及为什么直接从源代码构建开源软件是保护整个软件供应链的唯一途径。”

目前，加固容器市场除了BellSoft之外，还包括Chainguard、Docker、[Red Hat](https://www.openshift.com/try?utm_content=inline+mention)、[VMware](https://www.vmware.com/?utm_content=inline+mention)等老牌厂商；[AWS](https://aws.amazon.com/?utm_content=inline+mention)、Azure和[Google Cloud Platform](https://cloud.google.com/?utm_content=inline+mention)等云服务提供商；以及[RapidFort](https://www.rapidfort.com/)、[Wiz](https://www.wiz.io/)、[Edera](https://edera.dev/)、[Lineaje](https://www.lineaje.com/)、[Minimus](https://www.minimus.io/)等初创公司，以及其他参与者。

这个机会之所以存在，是因为企业现在对所有东西都运行安全扫描器。“他们在接受软件时不再是盲目的了，”Belokrylov说。“他们要求供应商提供具有有限数量常见漏洞和暴露（CVEs）的软件。”

BellSoft希望处理这个基础层。

“这里的想法是，像BellSoft这样的供应商，实际上负责了软件交付包的很大一部分，例如基础镜像，并保持它们是最新且零常见漏洞和暴露（CVEs）的，”Belokrylov说。“开发人员可以专注于他们的应用程序，而BellSoft则维护基础，”他说。

对于企业而言，Costello Worthington指出，利用加固容器镜像的客户通常会发现更容易满足合规性要求，并简化获取[FedRamp授权](https://www.fedramp.gov/)的过程。

“为开发团队提供精选的基础镜像，可以确保开发工作专注于业务的路线图特性和功能，同时更容易满足合规性要求，减少漏洞，并加速开发速度，”她说。

## 技术方法

加固镜像剥离了包管理器和非必要组件，其配置是锁定的，无法在运行时更改。Alpaquita Linux支持musl和glibc，允许团队在不重写代码的情况下进行迁移。

与等待上游补丁的竞争对手不同，BellSoft在需要时会编写自己的补丁——这一能力源于其对OpenJDK和[GraalVM](https://thenewstack.io/graalvm-finally-gets-java-for-webassembly/)的积极贡献。

该公司还销售Liberica JDK性能版，它将Java 25的现代JVM反向移植到旧版本中。

“专门针对JDK 8 API编写的应用程序，其性能表现就如同它们已经迁移到最现代的Java版本一样，无需更改任何一行代码，”Belokrylov说。“对于那些仍然运行Java 8应用程序，特别是在云端运行的公司来说，这是一个杀手级功能。”

## 可用套餐

BellSoft提供一个免费的社区版，包含适用于JDK 21和25+的加固容器。标准版涵盖所有JDK版本以及GraalVM、Go、Python、C和Alpaquita基础版，并提供7天常见漏洞和暴露（CVEs）修复服务水平协议（SLA）。高级版则增加了支持和性能咨询。