
<!--
title: 区块链Python工具包AlgoKit
cover: https://cdn.thenewstack.io/media/2024/03/af607270-kelly-sikkema-377gw1wn0ic-unsplash-1.jpg
-->

Algorand 基金会已推出 AlgoKit 2.0，支持 Python 开发。

> 译自 [AlgoKit — Python Toolkit for Blockchain](https://thenewstack.io/algokit-python-toolkit-for-blockchain/)，作者 Jessica Wachtel。

为了进一步实现[区块链](https://thenewstack.io/enterprise-blockchain-is-doomed/)的民主化，开发者现在可以在 [Algorand](https://algorandtechnologies.com/) 上编写 Python 应用程序。[Algorand 基金会](http://algorand.foundation/)本周发布了 AlgoKit 2.0，The New Stack 在发布之前采访了该基金会的首席技术官 [John Woods](https://www.linkedin.com/in/johnalanwoods/)。

Woods 说：“我的期望是 [AlgoKit 2.0] 将为从未开发过应用程序的 Python 开发者，或是有常规软件工程经验但从未构建过在区块链上运行的应用程序的开发者提供一个浅显的学习曲线。”

Woods 认为，Algorand 选择 Python 作为其新的顶级开发语言的原因之一是 Python 开发者的数量众多且多样化。他表示，他相信 Python 开发者将帮助 Algorand 实现“从技术角度实现有意义且有价值的目标”。

## AlgoKit 2.0

AlgoKit 2.0 是一个命令行工具，类似于 [Rust 中的 Cargo](https://thenewstack.io/tutorial-import-libraries-of-rust-code-with-crates-io/) 和 [Swift](https://thenewstack.io/apple-highlights-swift-enhancements-at-wwdc22/) 中的 Swift Package Manager。正如在[新闻稿](https://www.prnewswire.com/news-releases/algorand-becomes-first-layer-1-blockchain-to-use-python-as-a-native-programming-language-with-algokit-2-0-launch-302101020.html?tc=eml_cleartime)中所解释的，AlgoKit 的目的是帮助开发者快速轻松地构建和启动安全、自动化、可投入生产的去中心化应用程序。1.0 版本于 2023 年 3 月发布，引入了简单的五分钟入门流程，为你提供了构建、测试和部署的强大工具。现在，仅仅一年后，2.0 版本已扩展为面向开发者的完整工具包，其中包含智能合约模板库；所有必需的应用程序基础设施在本地运行；简化的前端设计体验；以及第一个通用编程语言 Python 的原生集成。

在 AlgoKit 之前，开发者需要学习 Teal（一种类似于低级汇编的语言），才能在 Algorand 上构建任何应用程序。现在有了 AlgoKit，开发者可以使用纯 Python 在 Algorand 上编写完整的应用程序。Woods 和 AlgoKit 的工程师认为，通往 Algorand 的捷径非常重要，因此在开发该工具时，他们专注于已经让开发过程变得更简单的工具。在此过程中，团队对 VS Code 和 Xcode 等工具进行了彻底的审查，Woods 发现“所有这些平台的共同点是，它们为开发者提供了轻松构建、测试和部署其应用程序的工具”。他指出，这与当时在 Algorand 中的开发形成了鲜明的对比。

## 开发挑战

从一开始，Woods 和 AlgoKit 团队就知道他们将构建一个类似于设备的产品，其中包含一个用于构建“正常工作”的应用程序的框架。类似于微波炉或洗碗机，你只需打开它，它就拥有完全运行所需的一切。类似于设备的框架还需要可交付，并通过一行安装完成所有工具。但这并不是最严峻的挑战。对于这个团队来说，最严峻的技术挑战是构建一个让 Algorand 可以读取顶级 Python 代码的编译器。

Python 天生不适合区块链应用程序。区块链应用程序（例如[智能合约](https://thenewstack.io/do-i-need-a-smart-contract-2/)）具有传统操作系统中的 Python 应用程序所没有的限制。这给 AlgoKit 团队增加了一层复杂性，因为他们希望 Python 应用程序为网络增加价值，并且不会造成损害。为此，他们转向了最受信任的工作模型之一。AlgoKit 的编译器以 LLVM 开源代码为模型。

AlgoKit 的编译器管道分几个步骤工作。最上面是 Python 代码，编译器将 Python 代码编译并优化为中间语言。它会提取无法访问的代码和类似的任务。编译器执行的下一步是将该代码编译为略低级别的中间语言并进一步优化。编译器的最后一步将该代码转换为将在 Algorand 上运行的字节码。

## 后续步骤

AlgoKit 将在 2023 年继续进行更多升级，包括集成更多常用编程语言。开发者可以通过 [developer.algorand.org/algokit](https://developer.algorand.org/algokit/?utm_source=prnewswire&utm_medium=press_release&utm_campaign=algokit) 开始使用 AlgoKit。Algorand 团队还将在今年春季举办一系列初学者和中级开发者训练营，提供英语和西班牙语两种语言，供有兴趣开启区块链编码之旅的人士参加。访问 [developer.algorand.org/bootcamps](http://developer.algorand.org/bootcamps) 了解更多信息并注册。
