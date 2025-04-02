# 如何通过 OpenTelemetry 理解 iOS 用户行为

![Featued image for: How To Make Sense of iOS User Activity With OpenTelemetry](https://cdn.thenewstack.io/media/2025/02/bbf19b42-image3-1024x576.jpg)

软件工程师构建软件系统并将其发布到世界。在构建期间和之后，[工程师希望获得关于系统如何运行、执行和崩溃的实时反馈](https://thenewstack.io/how-time-plays-a-crucial-role-in-aggregating-mobile-data/)。

这种实践被称为[可观测性](https://thenewstack.io/observability/)，它是指从应用程序运行时收集信号或遥测数据，并使用这些信号来[提出关于应用程序的问题](https://hazelweakly.me/blog/redefining-observability/)。可观测性的价值来自于所有开发人员最终都会学到的一个真理：当你发布应用程序时，总会发生一些事情，而处理这种情况的最佳方法是收集尽可能多的关于应用程序的信息，以便对原因进行假设。

[OpenTelemetry](http://opentelemetry.io) 是一套非常流行的工具，用于提出这些问题。[OpenTelemetry，或简称 OTel](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/)，为开发人员提供了一种标准化的方式来传输应用程序信息，目前包括[指标 (metrics)](https://opentelemetry.io/docs/concepts/signals/metrics/)、[日志 (logs)](https://opentelemetry.io/docs/concepts/signals/logs/) 和[追踪 (traces)](https://opentelemetry.io/docs/concepts/signals/traces/)，几乎支持任何流行的编程语言。任何环境中的应用程序都可以将相同类型的数据发送到其可观测性后端，从而创建一个[标准](https://jeremymorrell.dev/blog/opentelemetry-and-the-value-of-standards/)，该标准对于任何了解 OTel 的人都具有可识别性、可理解性和可用性。
OpenTelemetry 和可观测性总体上仍在构建共识的一个领域是[观察移动应用程序](https://dzone.com/articles/the-future-of-mobile-observability-is-opentelemetr)。移动可观测性必须[考虑到许多因素](https://www.cncf.io/blog/2024/11/29/why-does-opentelemetry-work-differently-on-mobile-versus-backend-apps/)，这些因素对于 Web 服务或数据库来说并不存在，例如电池寿命或用户体验。让我们探讨一下 OTel 如何使用现有工具解决[移动可观测性](https://embrace.io/guides/mobile-observability-glossary/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=ios-otel-instrumentation)特有的问题。

## OpenTelemetry Instrumentation
OpenTelemetry 允许开发人员使用十几个强大支持的[语言 API 和 SDK](https://opentelemetry.io/docs/languages/) 将遥测数据添加到他们的应用程序中。这些工具包中的每一个都是根据 OTel 生态系统中存在的规范创建的，并且每一个都为在应用程序中收集 OTel 信号提供了简单的检测。

例如，以下是使用 [OTel-Swift](https://github.com/open-telemetry/opentelemetry-swift) instrumentation 的追踪示例：

```swift
// Set up the tracer
let tracer = OpenTelemetry.instance.tracerProvider
    .get(
        instrumentationName: "instrumentation-library-name",
        instrumentationVersion: "1.0.0"
    )

// Start a span to trace an activity in the app
let span = tracer.spanBuilder(spanName: "start-activity")
    .startSpan()

// End the span after all the activity is completed
span.end()
```

可观测性工具的一个关键方面是代码应该在编写时进行检测。让应用程序代码直接告知其遥测数据比从外部猜测发生了什么更容易：

```swift
// Situation 1: Telemetry isn’t tied directly to functionality
func myFunction() {
    action.start()
    while.action.state != .ended {
        if action.result == .interrupted {
            action.start()
        } else {
            continue
        }
    }
}

// When calling myFunction, we can only guess at when the functionality began and ended
// We also know nothing about what happened in the function
let span = tracer.spanBuilder(spanName: "myFunction")
    .startSpan()
myFunction()
span.end()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

// Situation 2: Telemetry is tied to functionality
func myFunction() {
    action.start()
    // We can begin tracing the action right when it starts
    let span = tracer.spanBuilder(spanName: "myFunction")
        .startSpan()
    while.action.state != .ended {
        if action.result == .interrupted {
            // We can note information about the execution of our function
            span.addEvent(
                name: “action interrupted”,
                timestamp: Date.now
            )
            action.start()
        } else {
            continue
        }
    }
    // We can end the span right when the action completes
    span.end()
}

// Calling the function will include the instrumentation
myFunction()
```
以这种方式添加检测允许开发人员将操作的整个上下文封装在操作生成的遥测数据中，而无需任何解释或遗漏。这种工具能够胜任移动开发人员想要做的大部分事情。然而，OTel规范起源于Kubernetes集群和[后端系统](https://dzone.com/articles/8-ways-mobile-observability-is-the-opposite)的可观测性用例，这有时会导致移动端上出现[未考虑到的情况](https://thenewstack.io/opentelemetry-challenges-handling-long-running-spans/)。OTel收集的信息主要集中在[资源](https://opentelemetry.io/docs/concepts/resources/)等项目上，这些项目在很大程度上不影响移动端，而像[应用程序崩溃](https://thenewstack.io/developing-a-mobile-crash-model-for-opentelemetry/)这样的关键移动活动目前在OTel中没有概念模型。更根本的是，移动应用程序是生产中单个编译的软件，而不是一组微服务，因此它们的[工具方法必须不同](https://get.embrace.io/mobile-observability-guide/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=ios-otel-instrumentation)。

## 移动应用程序的结构

对于OTel工具来说，移动应用程序的结构提出了一个复杂的情况。iOS和[Android应用程序](https://www.cncf.io/blog/2024/12/30/solving-android-app-issues-with-opentelemetry-beyond-local-profiling/)必须通过传输单个可下载文件发布到各自的应用商店。这意味着所有应用程序活动，以及关于该应用程序的信息，都是在编译时从单个代码库生成的。

想象一下一个代码库，其中包含UI元素、网络、用户身份验证详细信息和设备上的SQLite存储的具体信息，仅举几例。这些功能都必须存在，才能使实时移动应用程序正常运行，但对于开发人员来说，这是一个需要维护的相互关联的文件夹的混乱集合：

![](https://cdn.thenewstack.io/media/2025/02/4767d999-image1-300x145.png)

图1

更复杂的是，这些功能中的每一个都可能依赖于其他功能才能使应用程序运行。

例如，用户令牌管理器可能需要从本地存储检索其令牌，然后使用网络库与身份验证服务再次检查令牌是否仍然有效，然后触发已验证用户的导航更新，以将其进一步带入应用程序体验。在一个项目中编写所有这些内容，然后使用OTel跟踪该单个过程，可能会造成重叠的责任和黑盒子的混乱：

```
123456789101112131415161718192021222324 |
// Workflow rootlet authRootSpan = tracer.spanBuilder(spanName: "auth-root") .startSpan()// Retrieve the auth tokenlet token = TokenManager.retrieveToken()// Add to the Auth root a span for retrieving the auth token// Issue: we don’t know any of the internals of the .retrieveToken() call, or even when it will completelet retrieveAuthTokenSpan = tracer.spanBuilder(spanName: "retrieve-auth-token") .setParent(authRootSpan) .startSpan()// Send auth token to web service for verificationlet response = NetworkingManager.verify(authToken: token)// Add to the Auth root a span for this request// Issue: we don’t know any of the internals of the .verify call, or when it will complete. // This is especially egregious for networking, as we’d like to know the full details of ~what happened~ during a requestlet verifyAuthTokenRequestSpan = tracer.spanBuilder(spanName: "verify-auth-token") .setParent(authRootSpan) .startSpan()// ...There will continue to be a similar pattern of issues for this approach |
```

这项工作不应该在一个地方完成！

## 构建基于接口的OTel方法

为了管理这种复杂性，移动开发人员通常将他们的单体应用程序组织成具有有限依赖关系的独立模块。这些模块各自管理其自身功能的职责，并尝试仅公开其他模块可以使用的接口：

![](https://cdn.thenewstack.io/media/2025/02/a0704340-image2-300x96.png)

图2

将应用程序功能拆分为其自己的模块具有[访问控制](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/accesscontrol/)的内置优势：模块仅公开开发人员允许其公开的功能。例如，在以下代码中，只有`makeRequest` 函数可以在其他地方访问：

```
12345678910111213141516171819202122232425262728293031323334353637383940414243444546 |
```
```markdown
```swift
// in RunningApp-Networking
public struct RequestHelper {
    // Inaccessible to others
    private setupRequest() {}
    private teardownRequest() {}

    // Accessible to others
    public makeRequest() -> Result {
        setupRequest()
        defer {
            teardownRequest()
        }
        // do request logic
        return Result.success
    }
}
```

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

```swift
// In other modules, we can get the Result object
import RunningApp_Networking

let networkingResult = RequestHelper.makeRequest()
```

这里重要的步骤是：使用 `RequestHelper.makeRequest` 将会返回一个 `Result` 对象到应用程序中的其他模块。我们可以使用类似的模式为模块之间的 OTel instrumentation 返回对象，并且只返回另一个模块可能需要的信息：

```swift
// in RunningApp-Networking
public struct RequestHelper {
    private setupRequest() {}
    private teardownRequest() {}

    public makeRequest() -> (result: Result, processStartTime: Date) {
        let startTime = Date.now
        setupRequest()
        defer {
            teardownRequest()
        }
        // do request logic
        return (result: Result.success, processStartTime: startTime)
    }
}
```

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

```swift
// In other modules
import RunningApp_Networking

let (networkingResult, networkingStartTime) = RequestHelper.makeRequest()
let networkingRequestSpan = tracer.spanBuilder(spanName: "networking")
    .setStartTime(time: networkingStartTime)
    .startSpan()
```

我们可以进一步迭代共享的特定信息，但为什么不使用共享的数据格式和语言呢？如果有一套工具可以让我们标准化在不同应用程序边界之间收集和传输的遥测数据，而无需每次都自定义传输信息的格式，那该多好。

**我们可以让我们的模块使用 OpenTelemetry 在它们之间进行通信**！通过在接口中传递 span 作为返回类型，模块可以传递它们自己的遥测数据，并将它们与来自应用程序其他部分的遥测数据组合起来，然后再将它们传输到设备之外。我们还可以使用我们想要附加的任何其他属性和事件来装饰遥测数据，而无需更改共享数据模型。将这种丰富的上下文添加到遥测数据是[理解和重现](https://thenewstack.io/why-your-mobile-app-needs-client-side-network-monitoring/)影响用户的问题的关键：

```swift
// in RunningApp-Networking
public struct RequestHelper {
    private setupRequest() {}
    private teardownRequest() {}

    public makeRequest() -> (result: Result, span: Span) {
        var span = tracer.spanBuilder(spanName: "networking")
            .setStartTime(time:Date.now)
        setupRequest()
        defer {
            teardownRequest()
        }
        // do request logic
        // we can decorate the span with any pertinent information
        // maybe being in low power mode is affecting the outcome
        span.setAttribute(key: ”is-low-power-mode”, value: true)
        // maybe certain operating systems experience worse networking outcomes
        span.setAttribute(
            key: “operating-system”,
            value: UIDevice.current.systemVersion
        )
        return (result: Result.success, span: span)
    }
}
```

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

```swift
// In other modules
import RunningApp_Networking

let largerProcessSpan = tracer.spanBuilder(spanName: "larger-process")
    .startSpan()

let (networkingResult, networkingSpan) = RequestHelper.makeRequest()
networkingSpan.setParent(largerProcessSpan)
    .startSpan()
```

这种方法允许我们在模块之间共享完全形成的遥测数据，而无需让其他模块负责该遥测数据的细节或目的。毕竟，这就是遥测数据的目标：报告影响我们系统所有部分的因素，同时系统还在运行。 [开发人员可以将应用程序的不同部分建模](https://thenewstack.io/observability-is-a-multicluster-app-developers-best-friend/)为单独的服务，并在之后创建一个完整的画面。

## 使用 OTel Context

在总结之前，我们应该提到 [context](https://opentelemetry.io/docs/concepts/context-propagation/#context) 的概念，它直接构建到所有 OTel SDK 中。Context “包含发送和接收服务或执行单元的信息，以便将一个信号与另一个信号相关联。” 换句话说，它与它通信的其他服务共享有关给定服务的信息，以便它们的遥测数据可以以任何数量的方式组合在一起。
对于移动可观测性而言，这是一个令人兴奋的机会，因为应用程序开发人员可以受益于了解在给定时间点收集的遥测数据，而不管它在应用程序中的位置如何。在 iOS 应用程序中，您可以检查 OpenTelemetry SDK 中 [span](https://thenewstack.io/spans-what-are-they-and-why-should-mobile-engineers-care/) 在该时间处于活动状态：

```swift
let currentSpan = OpenTelemetry.instance.contextProvider.activeSpan
```

但是，以这种方式使用 OTel 接口会给许多场景带来偶然性。移动设备是多核计算机，可以同时运行多个进程。如果网络请求在后台运行并且屏幕正在滚动，那么正在测量的“活动 span”将是什么？“活动 span”如何解释异步操作，这些操作尤其关系到网络和本地存储中的数据完整性？这些是移动开发中 [单例](https://developer.apple.com/documentation/swift/managing-a-shared-resource-using-a-singleton) 的标准问题，但在处理应用程序遥测的上下文时仍然值得考虑。

## 总结

OpenTelemetry 的标准化概念和工具包允许开发人员以可预测的方式跨系统边界共享信息。在移动开发中，使用 OTel 进行强大的检测可以告诉开发人员代码的每一层发生了什么。此外，将 OTel 视为信息共享抽象允许 [移动开发人员标准化其应用程序发送信息的结构](https://thenewstack.io/5-user-flows-to-trace-in-your-mobile-app/)。

在 [Embrace](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=ios-otel-instrumentation)，我们希望增强在移动设备上捕获的信息的功能，以便轻松了解哪些因素会影响用户体验。加入我们的 [community Slack](http://community.embrace.io) 提出问题，并详细了解我们对 OTel 的方法和我们的旅程。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)