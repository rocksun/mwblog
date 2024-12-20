
<!--
title: 运通的FaaS使用WebAssembly而非容器
cover: https://cdn.thenewstack.io/media/2024/12/9972fe22-getty-images-mpzj4fpslq0-unsplash.jpg
-->

Amex采用WebAssembly的一个关键原因是，WebAssembly展现出比容器更好的性能指标。

> 译自 [Amex's FaaS Uses WebAssembly Instead of Containers](https://thenewstack.io/amexs-faas-uses-webassembly-instead-of-containers/)，作者 B Cameron Gain。


# 美国运通的FaaS使用WebAssembly而非容器

![Amexs FaaS使用WebAssembly而非容器的特色图片](https://cdn.thenewstack.io/media/2024/12/9972fe22-getty-images-mpzj4fpslq0-unsplash-1024x562.jpg)

[美国运通](https://card.americanexpress.com/d/american-express/)已选择在其内部[函数即服务(FaaS)](https://thenewstack.io/boost-azures-faas-capabilities-with-durable-functions/)平台上使用[WebAssembly](https://thenewstack.io/webassembly/)。这代表了迄今为止WebAssembly在商业应用中最大规模的采用和使用。选择的开源WebAssembly工具是[wasmCloud](https://thenewstack.io/cncf-welcomes-webassembly-based-wasmcloud-as-a-sandbox-project/)，它最近获得了孵化器地位，正如最近在盐湖城举行的[KubeCon + CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/)活动上宣布的那样。

美国运通采用WasmCloud作为其FaaS以及wasmCloud获得[云原生计算基金会(CNCF)](https://cncf.io/?utm_content=inline+mention)孵化器地位，都代表了显著的工程和人才投入，有助于说明WebAssembly的设计目标。

美国运通采用这项技术的主要原因之一是，WebAssembly展现出比[容器](https://thenewstack.io/containers/)更优越的性能指标。这验证了多年来WebAssembly的开发以及对其潜力的期待。此前，WebAssembly主要被视为容器的理论替代方案，填补了容器并非总是理想解决方案的空白。

在本例中，美国运通优先考虑安全性，旨在实现一个沙箱式环境，提供轻量级、低延迟的功能。在KubeCon的Wasm Day现场演示中，美国运通的高级架构师展示了WebAssembly的优势，尤其突出了其速度和沙盒功能——由平台工程师构建在底层运行，以便开发人员通过FaaS完成工作，并具有最小的学习曲线。

“我们作为FaaS平台的目标是减轻开发人员的所有责任，”美国运通公司的一名员工工程师在与KubeCon+CloudNativeCon北美大会同期举行的WasmCon活动上的演讲中说道。“公司里的开发人员只需要负责编写包含业务逻辑的函数代码，其他一切应该由我们的平台负责。”

美国运通采用Wasm作为其FaaS平台的主要原因之一是，简单地将任何代码编译并高效运行“在所有场景中都不可行，”在与美国运通工程副总裁共同发表的WasmCon演讲“[使用Wasm组件提升无服务器平台](https://events.linuxfoundation.org/wasmcon/program/schedule/)”中说道。

当代码需要与[关系数据库](https://thenewstack.io/dont-let-time-series-data-break-your-relational-database/)交互并有效管理连接池时，将其编写为原生二进制文件更合适。WasmCloud使这种方法成为可能。“数据库特定的代码可以编写为原生二进制文件，而计算密集型函数代码仍然可以使用WebAssembly编译，”他说。“Wasm允许函数代码与原生二进制组件无缝交互。这种灵活性使得一旦生态系统达到可以进行这种转换的水平，就可以用WebAssembly组件替换原生二进制组件。”

## 平台工程加码

从平台工程的角度来看，描述了现代环境如何涵盖多个不同的数据源，包括施加某些限制（例如连接约束）的遗留数据源。平台工程师能够独立扩展数据源IO等组件，将这些责任与功能代码开发人员创建的代码分开。正如所描述的那样，这减少了函数的大小，通过卸载数据源连接等任务，从而增加了函数的密度和实例数量。

“鉴于这些好处，我们决定在wasmCloud之上构建一个FaaS运行时。这种方法能够维护单个运行时并提高密度，同时确保函数完全沙盒化和隔离，”他说。“wasmCloud提供了诸如组合和模块化等附加功能，使wasmCloud成为平台的自然选择。”

## 打造企业级就绪运行时
[@AmericanExpress]的FaaS具有开源[#Wasm]和[#WebAssembly]组件：“使用Wasm组件提升无服务器平台”——美国运通公司 的Ritesh Rai和Vamsi Sangavarapu在[#WasmCon]上的发言。[pic.twitter.com/C0sZ1Jb1qW]— BC Gain (@bcamerongain) [2024年11月12日]

Rai表示，在开发自定义FaaS运行时期间，对针对WebAssembly量身定制的核心生态系统功能的需求变得显而易见。在探索各种选项时，考虑了开源项目以加快开发速度。Rai表示，与其内部构建所有内容，不如利用wasmCloud作为平台的基础。

对于美国运通正在开发的FaaS，代码被编写并推送到存储库中，正如Rai描述的过程一样。部署管道将代码编译成一个WebAssembly组件，称为函数。一个安全装饰器被添加到组件中，其中包含安全过滤器和凭据。Rai表示，这个安全组件进一步封装在一个平台组件中，该组件允许使用多个接口来调用业务逻辑。

在开发自定义FaaS运行时期间，对针对WebAssembly量身定制的核心生态系统功能的需求变得显而易见。在探索各种选项时，考虑了开源项目以加快开发速度。与其内部构建所有内容，不如利用wasmCloud（一个优秀的开源CNCF项目）作为平台的基础。

在这个系统中，函数代码被编写并推送到存储库中。部署管道将此代码编译成一个WebAssembly组件，称为函数。一个安全装饰器被添加到组件中，其中包含安全过滤器和凭据。这个安全组件进一步封装在一个平台组件中，该组件允许使用多个接口来调用业务逻辑。

## 基于wasmCloud的平台功能

平台组件部署在wasmCloud上，将标准业务逻辑转换为企业级的WebAssembly平台。wasmCloud提供密钥管理、项目管理和多接口访问等关键功能，允许无缝调用函数。此外，该平台还为函数开发者提供开发SDK，使其能够与其他函数或WebAssembly组件交互，就像使用库一样。

自定义wasmCloud组件扩展了平台功能。已经对开源生态系统做出了大量贡献，增强了现有的能力提供者，并创建了针对特定需求的新能力提供者。


Cosmonic首席执行官兼创始人  和  ——之前担任Cosmonic首席技术官——在他们于美国前十大银行工作期间，CNCF在一份声明中表示。该项目目前由Cosmonic首席技术官兼字节码联盟技术指导委员会成员  领导。WasmCloud旨在解决应用程序团队在编写软件时在每个企业中面临的摩擦，并且自从被接受进入CNCF沙箱以来，它的普及率不断提高；它现在正在由在包括Adobe、Orange、MachineMetrics、TM Forum成员CSP和Akamai在内的一系列组织工作的工程师部署和维护。

[Adobe](https://thenewstack.io/adobe-developers-use-webassembly-to-improve-users-lives/)也依靠wasmCloud来使用WebAssembly。正如Adobe高级软件工程师  在其演讲“[在超分布式云上释放开源WASM的强大功能](https://wasmcon24.sched.com/event/1iTbK/unleash-the-power-of-open-source-wasm-on-a-hyper-distributed-cloud-colin-murphy-adobe-douglas-rodrigues-akamai?iframe=yes&w=100%&sidebar=yes&bg=no)”中所描述的那样，他和Akamai Technologies高级架构师  在KubeCon+CloudNativeCon之前的WasmCon期间，Wasm不仅有效，而且正在使用中，涵盖了Kubernetes环境。在谈到WebAssembly时，  在他的演讲中说：“关键在于，我们以前做不到的事情，现在可以做了。”

虽然意义重大，但美国运通和wasmCloud项目应该会带来更大的Wasm发展，因为美国运通的工程师将继续为该项目做出贡献。随着Wasm对无服务器的特别前景，正如[Fermyon](https://www.fermyon.com/?utm_content=inline+mention)通过其SpinKube项目所展示的那样，Wasm作为容器的替代品——至少对于无服务器应用程序而言——应该会继续成形。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)