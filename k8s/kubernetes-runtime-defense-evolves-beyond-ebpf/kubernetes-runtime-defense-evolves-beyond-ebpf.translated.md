# Kubernetes 运行时防御超越 eBPF

![Kubernetes 运行时防御超越 eBPF 的特色图片](https://cdn.thenewstack.io/media/2024/11/b3ef9197-engin-akyurt-xcwek_bx7ys-unsplash-1-1024x683.jpg)

云计算带来了许多[安全挑战](https://thenewstack.io/upskilling-developers-to-meet-todays-security-challenges/)，攻击面远远超出了[Web 应用防火墙](https://thenewstack.io/how-attackers-bypass-commonly-used-web-application-firewalls/)、基于网络 IP 的规则和基础设施层配置的静态边界保护。

[人工智能的快速兴起](https://thenewstack.io/top-5-ai-engineering-trends-of-2023/)加剧了这些挑战，并“迫使安全措施进入运行时——这是一个难以捉摸的攻击面，每个人都知道需要保护它，但安全技术却无法跟上，”Operant AI 的联合创始人兼首席执行官说，这家成立四年的初创公司其运行时应用程序平台旨在不仅保护云应用程序，[还保护 AI 模型和 API](https://thenewstack.io/bypassing-ebpf-to-protect-runtimes-in-kubernetes-apps/)。

这家位于旧金山的公司的平台包括运行时风险扫描和分析等功能，跨 API、数据存储、遗留端点和[Kubernetes](https://thenewstack.io/kubernetes/)集群强制执行运行时安全措施，扫描 API 的漏洞以找出漏洞并生成实时洞察，以及[代码即策略](https://thenewstack.io/is-policy-as-code-the-cure-for-multicloud-config-chaos/)，用于跨多个云扩展安全策略。

在犹他州盐湖城最近举行的[KubeCon + CloudNative NA](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)展会上，Operant AI 又迈出了新的一步，推出了 3D Runtime Defense Suite，它将实时发现、检测和防御功能整合到一个包中，以确保保护云应用程序的每一层，包括 AI 模型和 API。

## 一套防御措施

增强的发现功能包括 AI 工作负载、模型和 AI API 的即时实时蓝图，识别幽灵 API 和影子 AI 数据流，以及跟踪从第三方 API 到数据存储的数据使用模式。

运行时检测针对开放式 Web 应用程序安全项目（[OWASP](https://thenewstack.io/mitigate-owasp-security-top-threats-with-an-api-gateway/)）十大[大型语言模型 (LLM) 威胁](https://thenewstack.io/pyconus-simon-willison-on-hacking-llms-for-fun-and-profit/)，包括提示注入、敏感数据泄露、模型盗窃和数据投毒。Operant 的当前平台已经涵盖了 OWASP 在 API、Kubernetes 和[LLM](https://thenewstack.io/how-llms-guide-us-to-a-happy-path-for-configuration-and-coding/) 上 80% 以上的威胁。另一个功能是检测敏感数据的泄漏，例如个人身份信息 (PII)、密钥和 API 密钥。

防御部分包括自动内联阻止和删除敏感数据流，隔离可疑的第三方容器和 AI 模型，以及对敏感 API（包括端点）强制执行速率限制和令牌使用。

## 自动删除敏感数据

敏感数据流的自动删除是一个关键功能，它解决了数据隐私问题，既从防御的角度，也从数据治理和遵守越来越多的政府法规的角度来看。Bhavsar 告诉 The New Stack，人工智能开发现在是一个混合体，一些公司因数据隐私问题而停止人工智能开发，而另一些公司则构建可能与第三方共享私人数据的人工智能产品和功能，无论是偶然还是故意。

“在当今的 GenAI [生成式 AI] 应用程序世界中，公司正在利用其模型构建各种业务关键型功能，”他说。“但为了让 AI 发挥作用，它需要真正、真正好的数据。那么，我们如何在不关闭整个 AI 应用程序流程的情况下保护数据并获得所需的功能呢？”

Operant 的内联自动删除功能会在敏感数据（例如社会安全号码、电话号码和 API 密钥）在实时应用程序中移动时检测到它们，标记它们并根据其重要性优先考虑其风险配置文件。

“该系统允许工程师选择默认关闭整个数据流，或者让它在内联自动删除保护数据的私有元素的情况下运行，”Bhavsar 说。“内联自动删除会在私有数据离开内部应用程序环境之前将其删除，这对数据隐私和数据治理来说都是一个巨大的胜利，因为它意味着核心敏感元素无法发送到任何地方，而应用程序本身可以继续运行。”
## 超越日志和eBPF

Operant并非唯一一家致力于保护运行时环境的厂商。其他公司依赖于诸如[eBPF](https://thenewstack.io/p99conf-how-ebpf-could-make-faster-database-systems/)之类的工具——它使程序能够在特权上下文中（如操作系统内核）运行——以及日志记录，后者会生成大量软件工程师需要处理的警报。虽然它们会警告开发者攻击的存在，但Operant的技术会采取措施将其关闭。

“对于人手紧张的团队来说，这些方法会导致反应性过载，同时又缺乏实际理解攻击路径所需的多维上下文，而这些攻击路径实际上是从外部第三方、通过API、通过服务一直连接到数据存储的，”Bhavsar说。“在团队构建复杂的GenAI产品和功能之前，情况就是这样，但GenAI所需的数据流和应用程序架构使这种情况更加严重，无论团队是使用AI API还是在Kubernetes上部署的第三方模型，大多数团队都是如此。”

此外，运行时攻击——包括提示注入、零日漏洞数据泄露、数据投毒和分布式拒绝服务 (DDoS)——需要在运行时被阻止，而其他运行时机制无法做到这一点。

AI应用程序安全工具也不够。AI应用程序并非孤立存在，组织只能保护云应用程序的AI元素。

“你必须保护其嵌入其中的整个云堆栈，包括Kubernetes内部发生的所有短暂而复杂的交互，Kubernetes已成为AI应用程序开发的事实上的平台，”他说。“要做到这一点，你需要在数据离开边界之前保护应用程序或模型正在使用的数据。”


## 默认安全至关重要

Operant确保应用程序边界内的所有API和Kubernetes交互在数据发送出去之前都是安全的，使AI软件和模型能够提供业务价值，而不会因为安全问题而影响其功能。默认安全模式允许团队更快、更负责任地开发AI，并在攻击者进入环境之前就部署非侵入式运行时防御控制。

Operant希望通过其3D运行时防御套件广泛撒网，不仅在功能方面，还在其对生成式AI平台（如[OpenAI的GPT模型](https://thenewstack.io/openais-chatgpt-now-formats-output-to-developer-queries/)、[谷歌的Gemini](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/)、[Cohere](https://thenewstack.io/cohere-vs-openai-in-the-enterprise-which-will-cios-choose/)和[Anthropic的Claude](https://thenewstack.io/a-nue-ux-web-framework-plus-anthropic-openai-boost-ai-apis/)）的覆盖范围方面。Bhavsar表示，鉴于AI行业的快速发展以及开发团队做出的各种选择，有效的AI防御产品需要与厂商和平台无关，以应对变化并确保弹性。

“我们希望从一开始就构建正确的即插即用架构，以便将来添加其他提供商或自定义我们在客户堆栈中支持的提供商，就像我们产品的其余实现一样简单，”他说。“这是我们做出的一个关键战略决策……这样一来，安全工程师和开发团队就可以采用经得起时间考验并能够扩展的安全实践，而无需额外成本或大量人工工作，因为他们将继续发展其开发流程和工具。”


## 基于经验的构建

Bhavsar和Operant的联合创始人兼CTO [Priyanka Tembey](https://www.linkedin.com/in/priyanka-tembey-a1947611/)都拥有超过十年的为网络安全用例构建机器学习和AI的经验，这使他们了解哪些方法是短期措施，哪些方法可以在规模上进行转型。

“业界有很多噪音，但我们正在构建持久耐用的技术，该技术默认设计为可扩展且灵活，以匹配实际工程团队所在的位置，并为他们提供轻松的未来网络弹性，即使AI不断发展，”Bhavsar说。

他们的想法得到了支持。该公司于2023年4月公开推出，9月从SineWave Ventures、Felicis、Alumni Ventures、Massive、Calm Ventures和Gaingels获得了1000万美元的风险投资资金，使其在一年多时间内总共筹集了1350万美元。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)