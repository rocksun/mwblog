
<!--
title: YAMLScript助YAML成为了适当的编程语言
cover: https://cdn.thenewstack.io/media/2024/03/0d72fe48-restaurant-149039_1920-1024x644.png
-->

Ingy döt Net 正在酝酿一种脚本语言，可为 YAML 带去许多人以为它早已拥有的所有编程功能。


> 译自 [With YAMLScript， YAML Becomes a Proper Programming Language](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/)，作者 Joab Jackson。

[YAML](https://www.yaml.org/) 数据是否需要编程？包括 YAML 本身的创建者之一在内，许多人都认为需要。

[Ingy döt Net](https://github.com/ingydotnet) 已经启动了一个项目，旨在为数据序列化语言 YAML 带来脚本功能，该项目名为 [YAMLScript](https://github.com/yaml/yamlscript)。Ingy döt Net 还在致力于另一种编程语言 Lingy。

SUSE 工程师 [Tina Müller](https://github.com/perlpunk) 在上个月的年度 [FOSDEM 演讲](https://ftp.heanet.ie/mirrors/fosdem-video/2024/h2215/fosdem-2024-2046-do-you-know-yaml-.av1.webm)中透露了这一消息。

使用 YAMLScript，所有有效的 YAML 代码都是有效的 YAMLScript 代码。此外，所有 YAMLScript 函数代码(因为它本身就使用 YAML 语法)都可以直接嵌入到 YAML 文件中，或者从其他文件加载。

新的可编程功能将包括"出色的插值特性"，例如合并、过滤和连接。而且人们可以创建自己的"生成器"来动态操作数据，döt Net 承诺。

这项工作仍处于初期阶段，编译器的最新版本是本周早些时候发布的 [0.1.41](https://github.com/yaml/yamlscript/releases/tag/0.1.41) 版。但其思想是，它将通过 Müller 的会议形式解决"人们想要使用 YAML 进行的大多数编程事物"，döt Net 说。

## YAML 本身不是一种编程语言

[YAML](https://www.yaml.info/) 最初设计时并非用于编程，尽管许多人[希望它是如此](https://thenewstack.io/yall-against-my-lingo-why-everyone-hates-on-yaml/)。

这种语言自 2004 年问世以来一直存在理解上的误区，YAML 是 döt Net、[Oren Ben-Kiki](https://github.com/orenbenkiki) 和 [Clark Evans](https://clarkevans.com/) 的杰作。

根据其名称，[YAML](https://github.com/yaml/yamlscript)(现在表示为"YAML Ain't Markup Language")实际上不是一种标记语言(如用于网络的 [HTML](https://thenewstack.io/html-5-1-replaces-html-5-w3c-standard/))，而是一种数据序列化语言，事实上它是 [JSON](https://thenewstack.io/an-introduction-to-json/) 的超集。

YAML([当前版本为 1.2.2](https://yaml.org/spec/1.2.2/))提供了多种将数据串联起来的方式。

一个[流序列](https://yaml.org/spec/1.2.2/#flow-sequences)可以写成[方括号](https://yaml.org/spec/1.2.2/#flow-sequences)内用[逗号](https://yaml.org/spec/1.2.2/#flow-collection-styles)分隔的列表:

```
- [ Bob Marley， Peter Tosh， Bunny Wailer ]
```

或者！数据可以使用缩进来写作块集合:

```
- Gene Clark
- Roger McGuinn
- David Crosby  
```

然而，在这种简单的格式背后，隐藏着[令人困惑的](https://www.yaml.info/learn/index.html)一系列选项和规则，关于数据如何进一步标记，以及它[如何被解释](https://play.yaml.io/main/parser?input=IyBFZGl0IE1lIQoKJVlBTUwgMS4yCi0tLQpmb286IEhlbGxvLCBZQU1MIQpiYXI6IFsxMjMsIHRydWVdCmJhejoKLSBvbmUKLSB0d28KLSBudWxsCg==)。

但是，到目前为止，它还没有被用作一种编程语言。YAML 本身不了解"变量"或"函数"是什么。

## ${{ … }} Is Not YAML

但即使是经常使用的人也可以被原谅，他们会认为 YAML 是一种编程语言。

在基础设施管理软件中，YAML 数据经常被模板软件覆盖的执行代码所修饰。[VMware](https://broadcom-software.security.com/blogs/division/broadcom-software?utm_content=inline-mention) 的 [Saltstack](https://thenewstack.io/how-saltstack-reinvented-itself-for-a-cloud-dominated-world/) 以这种方式将 YAML 嵌入到其 [Salt State 文件](https://devopslibrary.com/lessons/salt-states/)中，人们会认为编码就是在 YAML 中进行的，Müller 说，并用代码片段进行了演示。

[Red Hat](https://www.openshift.com/try?utm_content=inline-mention) 的 [Ansible](https://thenewstack.io/red-hat-ansible-gets-event-triggered-automation-ai-assist-on-playbooks/) 做了类似的事情，将 YAML 作为字符串嵌入到其配置代码中，Müller 观察到。

这两个自动化工具都使用 [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) 模板来添加编码。很多人认为覆盖层实际上就是 YAML，她说。他们不断涌入 YAML 频道(#chat:yaml.io on matrix; libera.chat#yaml on irc)，询问他们的代码为何出错。

[GitHub Actions Workflow](https://docs.github.com/en/actions/using-workflows) 也将 YAML 嵌入到 `${{ … }}` 字符串的中心。

同样，这不是 YAML。

VMware、Red Hat 和 GitHub 并非是唯一超越 YAML 的公司。YAML 的静态限制在 Kubernetes 中尤为突出，因为它在 Kubernetes 中被[用作配置格式](https://thenewstack.io/googles-cloud-code-plug-ins-take-the-yaml-out-of-kubernetes/)。

在 2020 年，[亚马逊网络服务](https://aws.amazon.com/?utm_content=inline-mention)发布了 [cdk8s](https://thenewstack.io/aws-cdk8s-a-dev-friendly-alternative-to-yaml-for-managing-kubernetes-clusters/)，这是一个框架，用于捕获 Kubernetes 配置数据，以便它可以被共享用于不同的用途。

而 [Pulumi](https://www.pulumi.com/?utm_content=inline-mention) 已经围绕[管理配置数据](https://thenewstack.io/pulumi-program-the-infrastructure-with-an-actual-programming-language/)的能力(即使是 [Kubernetes 的配置数据](https://thenewstack.io/pulumi-releases-a-kubernetes-operator/))构建了其[核心价值主张](https://thenewstack.io/qa-pulumis-joe-duffy-on-the-renaissance-of-infrastructure-as-code/)，不是使用笨拙的 YAML 文件，而是[使用编程代码本身](https://thenewstack.io/pulumi-using-languages-to-program-across-clouds/)。

## YAML 现在是一种(函数式)编程语言

可以使用 [curl](https://thenewstack.io/you-too-could-have-made-curl-daniel-stenberg-at-fosdem/) 下载 döt Net 的 YAMLScript 编译器/解释器("ys")，并[在命令行中](https://thenewstack.io/fosdem-24-can-the-unix-shell-be-improved-hell-yes/)解压缩。或者它可以作为库[导入](https://thenewstack.io/vendoring-why-you-still-have-overlooked-security-holes/)到许多语言中的任何一种，例如 [Python](https://thenewstack.io/what-is-python/)。

ys 解释器将任何[有效的 YAML](https://yaml.org/spec/1.2.2/#103-core-schema) 代码作为 YAMLScript 进行摄取。用户只需在 YAML 函数代码前面加上: !yamlscript/v0。

[Rosetta Code](https://rosettacode.org/wiki/Rosetta_Code) 展示了你可以用 YAMLScript 说"[Hello World](https://rosettacode.org/wiki/Hello_world/Text#YAMLScript)"的所有方式:

```yaml
!yamlscript/v0

say: "Hello， world!"

=>: (say "Hello， world!") 

=>: say("Hello， world!")

say:
=>: "Hello， world!"

say: ("Hello， " + "world!") 

say: ."Hello，" "world!"

say "Hello，": "world!"

say "Hello，" "world!":
```

在底层，YAMLScript 被编译为 [Clojure 代码](https://thenewstack.io/stack-overflow-rust-remains-most-favored-but-clojure-pays-the-most/)，由 [Small Clojure 解释器 (SCI) ](https://github.com/babashka/sci)运行。

由于 Clojure 是一种函数式编程语言，基于 [Lisp 语法](https://borretti.me/article/why-lisp-syntax-works) - "尽管它在语法上通常看起来不像是 Lisp"，文档中指出 - 因此，从技术上讲，YAML 就是一种[函数式编程语言](http://joabj.com/Writing/Tech/Dev/0306-Functional_Programming.html)(立即使其成为继 [Microsoft Excel](https://thenewstack.io/excel-the-functional-programming-tool-you-didnt-know-you-had/) 之后使用最广泛的函数式语言之一)。

Tina Müller 在 FOSDEM 大会上演示了 YAMLScript。