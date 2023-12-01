<!--
title: WebAssembly助力控制平面可扩展
cover: https://cdn.thenewstack.io/media/2023/11/63c8e7ca-control-plane-1-1024x576.jpg
-->

软件架构面临着高度固有观念系统与更灵活方案选择之间的不断博弈，WebAssembly或可缓解此矛盾。

> 译自 [Why WebAssembly Is a Good Fit for Extensible Control Planes](https://thenewstack.io/why-web-assembly-is-a-good-fit-for-extensible-control-planes/)，作者 Charles Humble 是一位前软件工程师、架构师和CTO，曾担任技术和内容组的高级领导和管理人员。他于2014-2020年担任InfoQ的主编，并于2020-2023年担任ContainerSolutions的首席编辑。


在设计我们[构建应用程序](https://thenewstack.io/software-development/)的库和平台时，最终的使用情况可能与我们最初设想的非常不同。因此，在软件架构原则上采用前向兼容性和可扩展性通常是明智的。

然而，在软件架构中，研究出让应用程序对用户更加友好、能适应意外使用情况的最佳方式，这是一个长期存在的问题。因此，高度固执己见的系统与更灵活、更可定制的选择之间，存在着不断的拉锯战。

我们多次见证了这种模式。一个例子是[Cloud Foundry与Kubernetes的比较](https://thenewstack.io/when-to-choose-cloud-foundry-over-kubernetes/)。[Cloud Foundry](https://thenewstack.io/open-source-platform-engineering-a-decade-of-cloud-foundry/)高度固执己见，使用体验友好。但是[Kubernetes](https://thenewstack.io/kubernetes/)，尽管复杂度更高、对开发者不太友好，由于灵活性更强，在过去十年中主导了大部分编排工作。

[NGINX](https://www.nginx.com/?utm_content=inline-mention)现在属于F5的架构师[Matthew Yacobucci](https://www.linkedin.com/in/matthew-yacobucci-323b4b2/)对The New Stack表示：“我们不断重演这些模式。就我们的领域而言，以及F5和NGINX创建的产品，它们像瑞士军刀，可以做几乎所有事情。特别是[BIG-IP](https://docs.nginx.com/nginx-controller/platform/integrations/big-ip-self-service/)，可以管理从第2层到第7层的所有内容。”

“它可能难以配置，但是我们觉得可扩展性最终为客户带来的优点大于非常固执己见的系统。”

一个反例是我们的[控制平面](https://thenewstack.io/data-control-management-three-planes-different-altitudes/)，这是有充分理由的。例如，我们通常不愿意允许我们的开发人员直接向路由器插入共享对象，因为安全隐患令人担忧。

但是，如果有一种方法可以安全地完成此操作，会发生什么情况？Yacobucci渴望看到控制平面被扩展。而且，他认为[WebAssembly(Wasm)](https://thenewstack.io/webassembly/)可能提供了实现这一目标的方法。

## Kubernetes控制器和网关API

Kubernetes为您提供了[一组内置的控制器](https://kubernetes.io/docs/concepts/architecture/controller/)——服务控制器、Pod控制器、Deployment控制器、ReplicaSet控制器——以及一组核心API。当然，您可以扩展核心API，但您必须构建某种自定义控制器才能实现这一点。

[Kubernetes网关API](https://thenewstack.io/kubernetes-api-gateway-1-0-goes-live-as-maintainers-plan-for-the-future/)也允许扩展其核心资源，但与CRD的自定义控制器一样，网关实现也将需要一个逻辑部分——例如用于监视新资源的类型化客户端。而且，对于某些配置来说，必须对各自的数据平面配置进行进一步的转换，才能对Envoy、NGINX和HAProxy有效。

为了理解我们是如何走到这里的，值得回顾一下Kubernetes网关API的先驱[Ingress API](https://thenewstack.io/ingress-controllers-the-swiss-army-knife-of-kubernetes/)所发生的事情。它被设计来完成一项任务，并且完成得非常出色，但我们立即看到公司构建自定义资源(CRD)以各种方式尝试扩展其功能。

其中其他例子包括，Heptio创建了Contour，它增加了HTTPProxy来克服Ingress的局限性，NGINX创建了[VirtualServer和VirtualServerRoute](https://docs.nginx.com/nginx-ingress-controller/configuration/virtualserver-and-virtualserverroute-resources/)。“它们都在独立地试图规避Ingress的限制，”Yacobucci告诉我们。

最近达到正式发布状态的Kubernetes[网关API](https://gateway-api.sigs.k8s.io/)的开发人员想出了一个极具创造性且有些实验性的解决方案。网关API定义了一种Kubernetes对象，它以标准方式增强了另一个对象的行为，作为元资源(Metaresource)。(ReferenceGrant就是这种一般类型元资源的一个例子。)

网关API还定义了一种称为策略附加(PolicyAttachment)的模式，它通过添加原始规范中无法描述的设置来增强对象的行为。

那么API的实现者呢？“我们有元资源和策略附加，并且有一种强大的配置语言，您可以将其传输到数据平面，”Yacobucci说。“但在许多情况下，我们认为需要向系统中注入逻辑来遵守其意图。”

“随着网关API的出现，我们不仅要考虑ingress控制器，还要考虑更大的平台。这是我们希望保持的一种理念，方法是支持NGINX和F5在可扩展性方面的传承，并将其扩展到网关API控制平面的工作，正如我们正在开发符合网关API的[NGINX Gateway Fabric](https://github.com/nginxinc/nginx-gateway-fabric)项目。”

## 平行创新

NGINX正在架构的不仅是一个例子。例如，[Envoy网关扩展](https://gateway.envoyproxy.io/latest/design/extending-envoy-gateway/)允许通过扩展服务器来扩展Envoy网关。这利用了Envoy网关内部的一个或多个gRPC预/后挂钩来修改底层代理的xDS资源。这是一种类似的想法，尽管它首先集中在路由过滤器上，而不是策略附加上。

采用这种方法停留在Envoy和网关API生态系统中的现有系统内。但它确实需要时间成本。另外，Envoy每个部署只支持一个扩展服务器。

这与[Crossplane](https://www.crossplane.io/)等工具也有一些相似之处，可能还有[Kratix](https://kratix.io/)，尽管两者范围都更广。网关API专注于Kubernetes应用程序和API连接性——主要是集群内外的通信，[The GAMMA initiative](https://gateway-api.sigs.k8s.io/concepts/gamma/)下有一些有趣但相当初级的工作，旨在覆盖集群内的通信。

Yacobucci承认，仍有一些差距。他的目标是网关API只需要一次性安装，随后就是自助服务。

“我在这里考虑自助服务，是从客户和用户的角度来看的，”他说。“管理员添加一个入口控制器，应用程序开发人员可以通过添加元资源和元资源耦合逻辑来自定义，以处理合并、转换或任何定制配置案例。”

## 使可编程控制平面成为现实

正如我们之前所指出的，允许在控制平面层编程逻辑存在安全风险，而Yacobucci本人也承认了这些风险。“当我在一家XMPP公司工作时，我构建了类似的东西，”他告诉我们。“但这非常危险，因为您与同一内存空间中存在风险，并且语段在通过系统时发生变异。”

然而，他提出，[WebAssembly的优势](https://thenewstack.io/why-webassembly-will-disrupt-the-operating-system/)使我们能够维持常见模式(例如责任链)，并克服部分安全风险。

“如果当时我们有WebAssembly，我们无疑会使用它，”他说。

正如“[2023年WebAssembly状况](https://blog.scottlogic.com/2023/10/18/the-state-of-webassembly-2023.html)”报告所示，当您开始考虑注入性、插件和可扩展系统时，这项技术非常合适。工具和周围的生态系统继续改进，安全性很强，而且Wasm字节码很紧凑，便于传递和共享。

“我们现在认为用户体验是创建元资源和策略附加，但如果需要逻辑，我们可以简单地创建一个WebAssembly二进制文件，”Yacobucci说。“这样，您不需要重新启动入口控制器或重新部署任何内容——尽管如果您想保持容器不变性，可以选择重新部署。”

“您可以在系统内部注入功能和逻辑，或者在无需与管理员和安全团队进行任何交互的情况下动态删除它们。您的安全团队应该会感到很安全，因为WebAssembly以非常严格的方式建立壁垒。”

Yacobucci不会评论工具链的样子，但他指出F5最近收购了[Suborbital](https://suborbital.dev/opensource)，后者拥有非常成熟的WebAssembly工具链。

WebAssembly的另一吸引人质量是它提供了广泛的编程语言选择。“为Kubernetes写Go代码很有意义，”Yacobucci说。“然而，Go是一种静态编译语言，这使其更难获得动态插件式体系结构。”

[Digrid](https://www.diagrid.io/)的首席产品经理兼《[Kubernetes模式](https://k8spatterns.io/)》的合著者[Bilgin Ibryam](https://www.linkedin.com/in/bibryam?originalSubdomain=uk)同意WebAssembly是一个自然的选择，并指出服务网格和[Dapr](https://dapr.io/)都使用了该技术。

然而，他确实警告说，将太多内容放入网关的风险。“附加到网关的逻辑应该尽量简单，这样它就不会成为[ThoughtWorks所说的过于雄心勃勃的东西](https://www.thoughtworks.com/en-gb/radar/platforms/overambitious-api-gateways)，”他告诉我们。

Yacobucci的最终目标是达到一个地步，用户围绕核心控制平面组织整个系统。“我们有可扩展的数据平面和可扩展的未来证明API，”他说。“让我们确保拥有可扩展的控制平面，以利用所有这些力量。”
