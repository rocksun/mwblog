
<!--
title: 构建符合人体工学的JavaScript OpenTelemetry
cover: https://cdn.thenewstack.io/media/2025/08/dbb809c5-code.jpg
summary: OpenTelemetry在前端使用笨拙，源于多语言API的通用性与JavaScript的特殊性不匹配。核心在于分离上下文管理、数据检测和控制流。关键概念是“无结构的注释”和“不要让我思考”，通过简化事件结构，将状态管理移至SDK或收集器，提升JavaScript中OpenTelemetry的人体工程学特性。
-->

OpenTelemetry在前端使用笨拙，源于多语言API的通用性与JavaScript的特殊性不匹配。核心在于分离上下文管理、数据检测和控制流。关键概念是“无结构的注释”和“不要让我思考”，通过简化事件结构，将状态管理移至SDK或收集器，提升JavaScript中OpenTelemetry的人体工程学特性。

> 译自：[Building an Ergonomic OpenTelemetry for JavaScript](https://thenewstack.io/building-an-ergonomic-opentelemetry-for-javascript/)
> 
> 作者：Hazel Weakly

*这是分为两部分的系列文章的第一篇。*

在我看来，OpenTelemetry 是过去几年软件社区中最吸引人的发展之一。它已被证明对于检测分布式系统、微服务和复杂架构非常有价值。正因为如此，团队能够以越来越高的效率理解他们的系统，并在整个组织内分享这种理解。

随着它的迅速普及，[OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/) 在前端也变得越来越普遍。然而，我们遇到了一个问题：使用起来感觉很笨拙，[尤其是在浏览器中](https://thenewstack.io/setting-up-opentelemetry-on-the-frontend-because-i-hate-myself/)。

这不一定是任何人的错。这是如此多不同的语言使用单一 API 的自然结果；总会有一些感觉不对劲。OpenTelemetry 规范*确实*声明 [API 应该感觉符合语言习惯](https://opentelemetry.io/docs/specs/otel/specification-principles/#be-general)，但设计上的笨拙仍然存在。我不太确定为什么，但我想当你把每个社区的需求以及语言功能的共同点放在一起时，你最终不可避免地会得到一些在任何给定的语言中都感觉不太自然的东西。

也就是说，在这个基础上构建并提供一些前端开发人员会觉得更符合人体工程学的东西，存在着巨大的机会。几种语言已经做了类似的工作：例如，Ruby、[Go](https://thenewstack.io/opentelemetry-for-go-is-almost-a-go/) 和 [Java](https://thenewstack.io/getting-started-with-opentelemetry-for-java/) 都有相当符合人体工程学的 OpenTelemetry 集成。

这些符合人体工程学的实现具有共同的因素：特定于语言的功能用于在通用 API 之上创建便利，并且常见的控制流模式自然地融入到 OpenTelemetry 期望的状态机中。

有时，该语言没有特别常见的控制流模式（如 Haskell 或 Ruby），但这两种语言都具有灵活性，可以以允许检测库保持符合人体工程学的方式来塑造控制流，尽管存在潜在的摩擦。

> 我们将极大地受益于在我们的系统中分离上下文管理、数据检测和控制流。

事实上，我要大胆声明：OpenTelemetry 的核心是上下文管理，这是一个有意与规范的其余部分分离的概念，*专门*为了可以以对运行时环境最合理的方式实现上下文。尽管有这种意图，但我们似乎并没有真正获得这种关注点分离的好处。

如果我们要获得这些好处并释放真正符合人体工程学的遥测检测，那么开发将 OpenTelemetry 期望的控制流与在你的程序中合理的控制流分离的能力至关重要。如果我希望人们从本文中记住一件事，那就是我们将极大地受益于在我们的系统中分离上下文管理、数据检测和控制流。

这里有一个权衡，而且可能很难驾驭。如果你采用 OpenTelemetry 期望的控制流的状态机并将其推送到库本身中，它们可能会变得非常繁琐。另一方面，如果你依赖于隐式传播该控制流，那么当 OpenTelemetry 所需的控制流与你的程序的自然控制流不同时，你就会遇到问题。

## OpenTelemetry 中的 API 摩擦

当控制流与你注释和检测代码的方式相关联时，你必须更改代码结构以匹配 OpenTelemetry 期望的内容。对于 JavaScript 来说，这根本不是它擅长的事情，尤其是在前端。

JavaScript 还有一个独特的限制，即需要在浏览器以及 Node.js 中提供“相同”的语言。在前端，你有一个事件驱动的浏览器运行时，旨在为你完成繁重的工作。因此，它在异步代码、线程上下文和管理底层细节方面受到相当大的限制。毕竟，浏览器应该处理所有这些，并且浏览器 API 最初是在前端代码非常简单的世界中设计的。

现在我们在前端有复杂的代码，你可能会遇到你想要做的事情与浏览器容易实现的事情之间的不匹配。在后端，你有 Node.js，它迅速偏离了浏览器，以便添加某些在操作系统上运行所必需的 API，例如进程处理和线程上下文；这些偏差恰好使检测变得更加容易，但在前端（尚未）没有补充。

> 如果我们退后一步，思考一下在不更改语言的情况下我们可以做什么，我喜欢围绕两个概念来构建它：“无结构的注释”和“不要让我思考”。

即使 Node.js 可能具有更好的工具来启用符合人体工程学的 OpenTelemetry 实现，但 JavaScript 在设计上仍然是深度事件循环驱动的。OpenTelemetry 的 Span 和 Trace 模型与该模式不太匹配。因此，在 JavaScript 中有效地设置 OpenTelemetry 很困难。

最大的改进可能需要[语言更改](https://github.com/tc39/proposal-async-context)。但是，如果我们退后一步，思考一下在不更改语言的情况下我们可以做什么，我喜欢围绕两个概念来构建它：“无结构的注释”和“不要让我思考”。

OpenTelemetry 最自然的 API 之一是启动一个 span，在该 span 内执行工作，并让整个 span 干净利落地封装在父函数中。如果你有非常干净的同步代码，你的生活将会非常美好。但是，JavaScript 最初被设计为在某个事件上执行，由浏览器运行时调用，然后退出。因此，JavaScript 最自然的检测 API 是 `console.log`。每次你偏离 `console.log` 的人体工程学特性越远，你的生活就会变得越艰难，并且与该语言的自然模式作斗争。

相比之下，Go 有一个 `defer` 关键字，允许你以半显式的方式创建隐式作用域，而不会破坏你的语言的控制流。它还提供了一个上下文对象，让你可以在你的应用程序中传递上下文，而无需手动传播。这非常适合 OpenTelemetry（以及一般的检测）。Java 支持线程本地状态、装饰器和元编程，这允许人们在 OpenTelemetry 的基本 API 之上构建符合人体工程学的 API。

你可以看到以下（有些尖锐地选择的）示例之间人体工程学的明显差异：

```go
// https://github.com/open-telemetry/opentelemetry-go-contrib/blob/main/examples/dice/instrumented/rolldice.go#L38-L40
var (
    tracer  = otel.Tracer(name)
)
func rolldice(w http.ResponseWriter, r *http.Request) {
    ctx, span := tracer.Start(r.Context(), "roll")
    defer span.End()
    // rest of function
}
```

vs

```go
// https://github.com/open-telemetry/opentelemetry-js/blob/main/examples/opentelemetry-web/examples/fetch/index.js#L60-L65
const webTracerWithZone = providerWithZone.getTracer('example-tracer-web');

const singleSpan = webTracerWithZone.startSpan('files-series-info');
context.with(trace.setSpan(context.active(), singleSpan), () => {
  getData(url).then((_data) => {
    trace.getSpan(context.active()).addEvent('fetching-single-span-completed');
    singleSpan.end();
  });
  // rest of function
});
```

虽然选择此示例是为了展示痛点，但我们可以看到当语言的功能集和 API 的规范之间发生摩擦时会发生什么。理想情况下，我们希望 Go 示例和 JavaScript 示例的代码在人体工程学方面几乎相同。

## 无结构的注释

那么，我们如何促进 JavaScript 中最简单的检测应该感觉像 `console.log` 这样的想法，尤其是在你没有一个很好的方法来传递上下文时？JavaScript 中的异步上下文在后端有些缺乏，而在前端则完全没有。你也没有线程本地原语或在语言中隐式共享状态的能力。那么，你能做什么？

我认为关键是查看 OpenTelemetry 的底层规范和协议。事实证明，跟踪、span、span 事件和日志都建立在底层原语之上……也就是说，它们基本上都只是事件。事实上，OpenTelemetry 中的几乎所有东西都是自下而上的事件。

* 例如，日志是缺少 EventName 的事件。（*学究式地*说，在规范中，事件是具有非空 EventName 的 LogRecords）。
* Span 是具有关于你应该如何组合和构建它们的某些类型的元数据和语义的事件。
* Trace 是一系列 span，它们再次只是事件。

换句话说，关于你必须如何编写事件、发送它们的顺序以及将什么信息放入事件中的语义本质上是导致 OpenTelemetry API 中这种摩擦的唯一原因。如果你删除关于如何构建事件的一些限制，并使 OpenTelemetry SDK 能够将一些元数据负担推送到收集器上，你可以通过将状态机管理从你的代码控制流移动到 SDK，甚至可能是语言运行时本身来解决许多复杂性。你甚至可以以一种将 span 和 trace 拼接在一起的负担放在可以设计为有状态的东西上的方式来做到这一点；虽然 OpenTelemetry 收集器目前是无状态的，但它将是处理该状态的自然场所。

我在这里的大胆想法（听起来可能有些争议）是：如果我们抛弃 span 和 trace 必须具有与代码结构相对应的某种开始和结束结构的想法，那会怎么样？相反，如果我们以允许在收集器中处理开始和结束 span 的状态机的方式注释所有内容，那会怎么样？

假设如果这篇文章是一个 span，我会担心 [OpenTelemetry 处理它的能力](https://thenewstack.io/opentelemetry-challenges-handling-long-running-spans/)。由于我还有很多内容要介绍，因此我将其分为两部分。在下一篇文章中，我将分享我使 JavaScript 的 OpenTelemetry 更符合人体工程学的第二个概念：“不要让我思考”。然后，我将介绍一些关于遥测未来状态的想法，以及我们今天可以做些什么来为浏览器中的 OpenTelemetry 创建更好的支持。

同时，如果你想了解更多关于浏览器特别兴趣小组 (SIG) 正在积极研究的内容，请查看此 [按需网络研讨会](https://get.embrace.io/web-otel-panel-typ?utm_source=the-new-stack&utm_medium=paid&utm_campaign=ergonomic-js)。与往常一样，OpenTelemetry 对我来说的魔力在于它的社区，尤其是这个社区愿意团结起来，为每个人建设更美好的未来。[快来加入派对吧！](https://github.com/open-telemetry/community?tab=readme-ov-file#get-involved)