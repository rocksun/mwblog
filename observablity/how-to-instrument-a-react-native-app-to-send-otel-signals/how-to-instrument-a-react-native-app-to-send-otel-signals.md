
<!--
title: 如何为React Native应用插桩以发送OTel信号
cover: https://cdn.thenewstack.io/media/2025/02/0dfa64e6-embrace-opentelemetry-react-native-featured-image.png
-->

> 译自：[How To Instrument a React Native App To Send OTel Signals](https://thenewstack.io/how-to-instrument-a-react-native-app-to-send-otel-signals/)
> 作者：Jonathan Munz; Florencia Acosta

为 React Native 应用添加监控功能，以便通过 OTLP-HTTP 将数据发送到任何 OpenTelemetry 后端，包括自动监控、自定义追踪和导航流程追踪。

在这篇文章中，我们将逐步讲解如何为 React Native 应用添加监控，以便通过 OTLP-HTTP 将数据发送到任何 OpenTelemetry (OTel) 后端。[在之前的教程](https://www.cncf.io/blog/2024/08/05/how-to-add-otel-instrumentation-to-a-react-native-app/)中，我们针对[CNCF](https://cncf.io/?utm_content=inline+mention)展示了如何使用 OTel [JavaScript](https://thenewstack.io/javascript/) (JS) 包来实现这一点。但是，在本教程中，我们将使用[开源 Embrace React Native SDK](https://github.com/embrace-io/embrace-react-native-sdk)，原因如下：

- 官方 OTel 包在集成时需要一些技巧，因为[React Native](https://roadmap.sh/react-native)不被 OpenTelemetry JS 包直接支持为平台。Embrace 软件开发工具包 (SDK) 是专门为支持 React Native 而构建的，这使我们能够无需变通方法即可集成 SDK。
- Embrace React Native SDK 建立在 Embrace 的 Android 和 iOS 原生移动 SDK 之上。这使其能够发出关于在移动应用中运行的原生代码中发生的崩溃、内存问题等的遥测数据。换句话说，您可以通过访问来自原生层和 JS 层的上下文来更好地了解移动应用问题。
- 与 OTel SDK 一样，Embrace React Native SDK 允许将数据导出到任何 OTLP-HTTP 端点。但是，通过也将数据发送到 Embrace，您可以利用 Embrace 仪表板的功能来获得更多见解，我们将在本教程的最后深入探讨。

为简便起见，在本教程中我们将重点关注[iOS](https://thenewstack.io/how-to-make-sense-of-ios-user-activity-with-opentelemetry/)。同样的流程也适用于 Android，只需对设置进行一些小的更改。（有关更多详细信息，请参阅[添加 React Native Embrace SDK](https://embrace.io/docs/react-native/integration/add-embrace-sdk/)和[Embrace 仪表板入门](https://embrace.io/docs/react-native/integration/login-embrace-dashboard/#android)。）

## 安装包

本教程将利用，这是一套帮助您构建 React Native 应用的命令行工具。特别是，我们将使用它的`[@react-native-community/cli](https://www.npmjs.com/package/@react-native-community/cli)` `init` 命令快速启动一个空白应用：

```
npx @react-native-community/cli init Walkthrough
cd Walkthrough/ios
bundle install 
bundle exec pod install 
cd .. 
npx react-native run-ios
```

此时，您应该已经在 iOS 上运行了社区的 Hello World 示例应用。接下来，添加核心 Embrace SDK 包以及`@embrace-io/react-native-otlp` 包以允许导出到 OTLP-HTTP 端点：

```
npm install @embrace-io/react-native @embrace-io/react-native-otlp
```

## 初始化 SDK

要初始化 SDK 并对其进行配置以使其指向您选择的后台（在本例中为[Grafana Cloud OTLP 端点](https://grafana.com/docs/grafana-cloud/send-data/otlp/send-data-otlp/#send-data-to-the-grafana-cloud-otlp-endpoint)），请打开`App.tsx`并在`App`函数组件中添加以下内容：

```js
import {useEmbrace} from '@embrace-io/react-native';

// ...

function App(): React.JSX.Element {
  const {isPending, isStarted} = useEmbrace({
    ios: {
      disabledUrlPatterns: ['grafana.net'],
    },
    exporters: {
      logExporter: {
        endpoint: 'https://otlp-gateway-prod-us-central-0.grafana.net/otlp/v1/logs',
        headers: [{'key': 'Authorization', 'token': 'Basic __TOKEN__'}],
        timeout: 30000,
      },
      traceExporter: {
        endpoint: 'https://otlp-gateway-prod-us-central-0.grafana.net/otlp/v1/traces',
        headers: [{'key': 'Authorization', 'token': 'Basic __TOKEN__'}],
        timeout: 30000,
      },
    },
  });
  
  // ... rest of App()
}
```

上面的代码片段中发生了一些事情，让我们逐一看看：

- 在 JavaScript 中初始化 Embrace SDK：
  - 我们使用 钩子来启动和配置 Embrace SDK。这是从 React Native 层启动 Embrace SDK 的最简单方法。请注意，因为我们正在处理移动应用，所以在启动 JS 层之前可能有一些有趣的遥测数据需要捕获，而使用这种方法我们会错过这些数据。Embrace SDK 也可以在原生代码中启动以解决这种情况，但我们不会在本教程中详细介绍。如果您感兴趣，可以在[useEmbrace](https://embrace.io/docs/react-native/integration/session-reporting/#with-hooks)[文档](https://embrace.io/docs/react-native/integration/add-embrace-sdk/#native-setup)中找到更多信息。
- 配置日志和跟踪导出器：
  - 日志和跟踪是两个基本的 [OTel 信号](https://opentelemetry.io/docs/concepts/signals/)。在这里，我们将两者都设置为导出到同一个后端。请注意，这两个导出器是独立配置的。如果需要，您可以选择只设置一个，或者您可以将遥测数据发送到不同的可观测性后端位置。
  - 任何支持以 OTLP-HTTP 接收数据的后端都可以使用。在本例中，我们选择使用 Grafana。如果您还没有设置合适的后台，您可以通过 [注册 Grafana Cloud](https://grafana.com/docs/grafana-cloud/get-started/)并创建一个帐户来快速入门。您可能需要配置数据源，例如[Tempo](https://grafana.com/docs/tempo/latest/)用于跟踪或[Loki](https://grafana.com/docs/loki/latest/)用于日志。
  - 我们还在设置
  在 iOS 配置中，排除任何匹配模式 `disabledUrlPatterns` [`grafana.net`](https://embrace.io/docs/react-native/features/otlp/#disable-tracing-for-the-otlp-export-network-requests) 的 URL 捕获。Embrace 的检测会自动为任何 [网络请求](https://embrace.io/docs/features/network-monitoring/) 创建跨度。但是，由于 OTLP 导出器会发出网络请求来发送追踪数据，这将产生一个循环：导出的网络请求创建一个跨度，该跨度被导出并创建另一个跨度，以此类推。忽略“grafana.net”
- 获取 `isPending` 和 `isStarted` 来自使用钩子的结果：
  - 我们将本教程的后面使用这些值。它们使我们能够知道 Embrace SDK 何时成功启动，以便我们能够在其之上构建进一步的检测。

## 查看自动检测

您尚未添加任何检测。但是，您仍然应该能够在您的可观测性系统中看到来自 Embrace SDK 自动设置的检测的一些有用的遥测数据，例如捕获 [网络请求](https://thenewstack.io/best-practices-for-monitoring-network-conditions-in-mobile/) 的跨度和未处理异常的日志。要查看这些数据，请重新启动应用程序并在您的可观测性工具中搜索新的跨度。

如果您使用的是 Grafana，您可以登录您的组织，选择您的 Grafana Cloud 堆栈，并在“探索”部分查看一些遥测数据。让我们深入了解您此时将看到的内容：

![](https://cdn.thenewstack.io/media/2025/02/d5035246-embrace-grafana-cloud-traces-image-1024x560.jpeg)

上面的屏幕截图显示了应用程序创建和导出的第一个 [跨度](https://thenewstack.io/spans-what-are-they-and-why-should-mobile-engineers-care/)。如果您单击其中一个追踪 ID 值，右侧面板将显示并显示跨度的详细信息。

![](https://cdn.thenewstack.io/media/2025/02/8d457045-embrace-emb-session-trace-details-further-1024x559.jpeg)

上面的屏幕截图显示了 `emb-session` 追踪，其中包含许多关于我们所说的“会话”的有趣信息。在 OTel 语义约定中，会话 [定义为](https://opentelemetry.io/docs/specs/semconv/general/session/)“包含应用程序执行的所有活动以及最终用户执行的操作的时间段”。

![](https://cdn.thenewstack.io/media/2025/02/7ff53fff-embrace-emb-session-trace-details-1024x559.jpeg)

通过向下滚动右侧侧面板，您可以看到默认情况下为每个应用程序会话收集的更多信息。

## 添加手动追踪

您也可以添加您自己的自定义追踪。在 OpenTelemetry 中，这是通过 [追踪提供程序](https://opentelemetry.io/docs/concepts/signals/traces/#tracer-provider) 完成的，因此首先添加 Embrace 的追踪提供程序包，该包实现了此接口。设置可能如下所示：

```js
import {useEmbraceNativeTracerProvider} from "@embrace-io/react-native-tracer-provider";

// ...

function App(): React.JSX.Element {
  const {isPending, isStarted} = useEmbrace({
    // ... Embrace config
  });
  
  const {tracerProvider: embraceTracerProvider} = useEmbraceNativeTracerProvider({}, isStarted);

  const tracer = useMemo<Tracer | undefined>(() => {
    if (embraceTracerProvider) {
      return embraceTracerProvider.getTracer("walkthrough-span-test", "1.0.0");
    }
    
    if (isPending) {
      console.log("Loading the Embrace SDK...");
    } else {
	console.log("The Embrace SDK has loaded");
	
	if (!isStarted) {
	  console.log(
	    "An error occurred during Embrace SDK initialization, ",
	    "the Tracer Provider won't be initialized"
	  );
	}
    }
  }, [embraceTracerProvider, isPending, isStarted]);	

  const createSpan = useCallback(() => {
    const span = tracer?.startSpan("Span created manually");
	
    span?.setAttribute("custom-attribute", "walkthrough");
    span?.addEvent("custom-event", {custom: "walkthrough-event"});
		
    setTimeout(() => {
	span?.end();
    }, 3000);
  }, [tracer]);
	
  // ... rest of App()
}
```

在此代码段中，Embrace 追踪提供程序被初始化并用于使用 `createSpan` 调用创建一个新的自定义跨度。追踪器用于手动启动跨度，然后在业务逻辑的某个点，跨度应该结束。

出于测试目的，我们在这里使用超时来结束跨度，但是更有趣的情况是 [包装一些扩展操作](https://thenewstack.io/5-user-flows-to-trace-in-your-mobile-app/) 并在其测量的操作完成后结束跨度。请注意，我们还为此实例设置了自定义属性和事件，以便将更多上下文附加到跨度。

您现在可以将该回调分配给按钮并进行测试，该按钮可以简单地呈现为：

```html
<Button onPress={createSpan} title="Test Span" />
```

触发此操作后，您可以查看 Grafana 仪表板。您应该会看到如下内容：

![](https://cdn.thenewstack.io/media/2025/02/00e2e1ca-embrace-manually-created-span-1024x558.jpeg)

名为 `Span created manually` 的跨度显示在列表中。

如果您深入研究此追踪，您将看到附加到它的自定义属性和事件：

![](https://cdn.thenewstack.io/media/2025/02/860da905-embrace-custom-attribute-on-span-1024x554.jpg)

## 添加导航检测

更真实的应用程序将支持在屏幕之间导航，这很可能也是您想要记录遥测数据的内容。Embrace 有一个 [包](https://www.npmjs.com/package/@embrace-io/react-native-navigation) 提供了此常见用例的检测。此包接收您在上一步中设置的相同追踪提供程序，并包装您的组件，以便在用户导航到新屏幕时创建遥测数据：

```js
import {
  NavigationContainer,
  useNavigationContainerRef,
} from "@react-navigation/native";
import {createBottomTabNavigator} from "@react-navigation/bottom-tabs";
import {EmbraceNavigationTracker} from "@embrace-io/react-native-navigation";

// ...

const Tab = createBottomTabNavigator();

function App(): React.JSX.Element {
  // ... Embrace already started and the tracerProvider is loaded

  const navigationContainer = useNavigationContainerRef();
  const navigationContainerRef = React.useRef(navigationContainer);

  return (
    // `NavigationContainer` is waiting for what `useNavigationContainerRef` is returning (both exported from `@react-navigation/native`)
    <NavigationContainer ref={navigationContainer}>
      <EmbraceNavigationTracker
        ref={navigationContainerRef}
        tracerProvider={embraceTracerProvider}
        screenAttributes={{
          "test.attr": 654321,
          package: "@react-navigation/native",
        }}>
        <Tab.Navigator>
          <Tab.Screen
            name="home"
            component={HomePage}
          />
          <Tab.Screen
            name="details"
            component={DetailsPage}
          />
        </Tab.Navigator>
      </EmbraceNavigationTracker>
    </NavigationContainer>
  );
};
```

您的应用程序现在应该启动一个带有两个项目的标签栏，屏幕如下所示：

![](https://cdn.thenewstack.io/media/2025/02/01690115-embrace-side-by-side-phones-1024x546.png)

此示例使用该包显示了一个非常简单的导航流程，该流程在主页和详细信息屏幕之间进行，但也支持包 `@react-navigation/native` (https://www.npmjs.com/package/@react-navigation/native) 和 `expo-router` (https://www.npmjs.com/package/expo-router)。`react-native-navigation` (https://www.npmjs.com/package/react-native-navigation)
所有配置完成后，您可以再次构建应用程序并在视图之间导航。每次视图显示然后消失（因为另一个视图出现）时，它都会创建一个跨度，表示第一个视图显示给用户的期间。

![](https://cdn.thenewstack.io/media/2025/02/c3eaa276-embrace-home-details-spans-1024x558.jpeg)

此列表中现在有两个新名称——`home`和`details`。这两个跨度是由Embrace包创建的，一旦配置了该包，它就会捕获应用程序中的每个导航操作。

仔细查看这些新跨度之一，您可以看到该包不仅添加了一些默认属性，例如`view.name`或`view.state.end`，还包括您之前通过`EmbraceNavigationTracker`组件的`screenAttributes`属性配置的属性：

![](https://cdn.thenewstack.io/media/2025/02/372051ae-embrace-navigation-attributes-1024x556.jpeg)

`NavigationContainer`组件来自`@embrace-io/react-native-navigation`，我们称之为“检测库”。它是一个独立的包，它生成关于导航流的遥测数据，并且它会在正确的时间自动启动和结束跨度，并带有相应的上下文。您可以深入了解[我们如何构建它](https://embrace.io/blog/creating-opentelemetry-instrumentation-library-react-native/)。

此检测库由Embrace公开，但它并不局限于我们的产品。相同的组件可用于使用任何追踪器提供程序跟踪遥测数据。

同样，任何与追踪器提供程序一起工作并生成有效信号的检测库都可以连接到Embrace以开始捕获其他遥测数据。

## 利用Embrace仪表盘获得有价值的见解

Embrace React Native SDK是一个很好的选择，可以快速收集有价值的数据，以分析用户旅程并[监控应用程序的运行状况](https://thenewstack.io/why-your-mobile-app-needs-client-side-network-monitoring/)跨越不同的设备。Embrace不仅为您收集这些数据，还提供一套全面的工具，通过处理SDK收集的所有信号来帮助您获得有意义的见解。

这些包括一个强大的[用户时间线](https://embrace.io/docs/features/user-session-insights)，显示导致问题或糟糕客户体验的确切事件序列：[视频](https://youtu.be/_Phnn85r6qg)。

用户时间线允许开发人员从用户的角度（例如，点击和导航）、从业务逻辑（例如，网络和检测到的跨度）以及从应用程序和设备层（例如，内存警告和崩溃）查看代码中发生的情况。将所有这些信息按顺序排列，允许开发人员深入研究影响性能的技术细节，并关联应用程序堆栈中的问题。

此外，您可以轻松地将Embrace[与您现有的可观测性解决方案集成](https://embrace.io/docs/data-destinations/)，以支持[移动SLO](https://get.embrace.io/mobile-slos-guide)（服务级别目标）并在DevOps/站点可靠性工程师（SRE）和移动团队之间创建更具凝聚力的工作流程。一个这样的例子是[网络跨度转发](https://embrace.io/docs/product/network-spans-forwarding/)，它可以追踪用户时间线和您的后端监控服务中的相同请求。

## 总结
在本演练中，我们介绍了如何检测React Native应用程序以通过OTLP-HTTP将数据发送到任何OTel后端。我们使用Embrace React Native SDK，因为它专为React Native而构建，并且比OpenTelemetry JS包大大简化了集成过程。我们还简要介绍了将OpenTelemetry信号发送到Embrace仪表盘的一些好处。

[Embrace](https://embrace.io/)正在帮助使OpenTelemetry适用于移动开发人员。我们在OTel上构建了我们的[iOS](https://github.com/embrace-io/embrace-apple-sdk)、[Android](https://github.com/embrace-io/embrace-android-sdk)和[React Native](https://github.com/embrace-io/embrace-react-native-sdk) SDK，同时与社区合作改进规范。如果您想了解有关如何利用基于OpenTelemetry构建的移动可观测性的更多信息，请查看我们的[开源存储库](https://github.com/embrace-io)或[加入我们的Slack社区](https://embraceio-community.slack.com/)。
