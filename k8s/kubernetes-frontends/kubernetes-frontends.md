<!--
title: 软件工程师视角的Kubernetes管理前端的内部机制 
cover: ./cover.png
 -->

在这篇博文中，我们回顾了Kubernetes管理前端，并讨论了这些工具是如何被构建的。

> 译自 [The Inner Workings of Kubernetes Management Frontends — A Software Engineer’s Perspective](https://glasskube.dev/blog/kubernetes-frontends/)，作者是 Christoph Enne 。

近年来Kubernetes的兴起导致了大量开源的Kubernetes管理工具貌似凭空出现。这篇文章背后的研究的目的仅仅是要理解这些工具的架构，并且随后为试图开始自己的Kubernetes前端开发的开发者提供一个简要的概述和选择。我们不会深入探讨这些工具本身以及它们试图解决的问题，而是将重点放在软件工程方面。我们还仅探索开源和自托管工具，不讨论云提供商的PaaS/IaaS平台——这将是一篇完全不同的文章。

搭建和与第一个集群进行交互可能会令人不知所措。就像我一样，你可能遇到了臭名昭著的`kubernetes/dashboard`，按照安装说明进行了安装，并问自己："我刚才做了什么，为什么它的工作方式是这样的?" 在对集群进行一些调整之后，你可能还安装了更多的外部工具来帮助你管理集群的某些具体方面，为你提供CLI或Web UI。

作为最近几年主要从事Web开发的软件工程师，我对这些工具是如何构建和部署的感到好奇。

我们首先澄清一下接下来探索不同Kubernetes UI所需的一些基本知识。之后，我们将看到它们有什么共同之处，以及是什么使这种软件如此特别，最后形成一个建议，说明如何自己构建Kubernetes Web UI。

## Kubernetes基础知识

官方文档在任何情况下都非常有帮助;只需要记住一件重要的事情:无论在何时何地与集群进行交互，都是通过Kubernetes API进行的 - 至少就本文的范围而言是如此，尽管可能还有其他用例。 

作为该API的消费者，需要知道它托管在哪里以及如何对其进行身份验证。Kubernetes API可以从集群内部(即从运行在pod上的应用程序)和集群外部(例如从命令行)进行访问。但是，在某些情况下，API仅可从VPN内访问。

由于我们正在查看具有Web UI的工具，因此需要暴露该UI及其后端，以便用户可以访问它。选项是:

- 使用`kubectl proxy`打开从本地机器到集群的代理(参见 访问集群)，
- 使用`kubectl port-forward`将本地端口转发到集群的特定pod(参见 使用端口转发访问集群中的应用程序)，  
- 使用类型为`LoadBalancer`的Kubernetes服务来访问集群的应用程序(参见 使用服务访问集群中的应用程序)。

另外，Web服务器也可以在用户的本地机器上运行，在这种情况下就不需要担心这些选项。但是，对于这些方法的任何一种方法都需要在用户的机器上有一个有效的kube配置。

## 管理前端

现在，让我们看一下一些常用的前端以及它们是如何构建的。

### kubernetes-dashboard

Kubernetes Dashboard是一个流行的Web UI，用于查看和管理集群中的各种Kubernetes资源。在最新稳定版本2.7中，后端和前端都是同一个容器的一部分。 Go后端同时为API和Angular UI资产提供服务。这种部署策略要求用户使用`kubectl proxy`来访问Web应用程序。


在新的3.0版本中，它仍处于alpha阶段，部署策略已更改: 后端和前端每个都在专用的容器中运行。因此，通过kubectl proxy访问它不再起作用，因为UI需要访问在不同pod和端口上运行的后端。应改用此处描述的端口转发方法。

### ArgoCD

ArgoCD是一个Kubernetes的GitOps持续交付工具。它包含几个组件，包括自己的API服务器和Web UI。所有后端组件都是用Go编写的，UI是一个React应用程序。

与Kubernetes Dashboard一样，服务器(包括UI资产)部署在集群内部，这使得用户需要执行端口转发或使用LoadBalancer。这在他们的文档中有描述。

### Lens

Lens是一个桌面UI，但对我们的探索仍很有趣。它使用Electron、React和Typescript开发。Lens App使用Typescript Kubernetes客户端连接到集群，由于桌面应用程序显然在集群外运行，它使用本地提供的kubeconfig与其连接。

### glasskube

是的，一个相当厚颜无耻的插播广告(我在那里工作)，但它也是一个有趣的替代方案。对于Glasskube软件包管理器的UI，我们通过CLI命令在本地启动Web服务器，并从那里提供UI资产。我们决定采用这种方式，因为在我们的使用案例中，这更有意义。每当用户需要Glasskube UI时，他们会根据需要托管它，可以长期或者短期 - 不需要24/7在集群内运行它。

## 发现

许多开源Kubernetes管理UI的编码方式类似 —— 使用强大的Kubernetes-go客户端的Go后端，以及JavaScript中的单页面应用程序作为前端。在大多数情况下，Web资源(例如JS文件)与后端一起提供服务，这意味着一个容器同时为后端和前端提供服务。实际上很难找到不是这样构建的东西。 

### 集群内与集群外

当涉及到部署这样一个Web工具时，只有两种选择:

- Web服务器部署在集群内的pod上，并且可以通过代理、端口转发或ingress访问。
- Web服务器部署在集群外部，直接(本地)部署在用户的机器上。

Kubernetes客户端(例如Go客户端)支持开发人员这两种方法来连接集群，正如我们在下面的例子中看到的。

**它所依赖的代码段:**

这些简化的示例在很大程度上基于这里和这里看到的官方示例。

让我们看一下在集群内部运行应用程序时如何连接到Kubernetes API:

```go
import (
	"context"

	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/rest"
)

func main() {
	// retreive the config for the cluster we are currently in:
	config, err := rest.InClusterConfig()
	if err != nil {
		panic(err.Error())
	}

	// create the clientset for this config:
	clientset, err := kubernetes.NewForConfig(config)
	if err != nil {
		panic(err.Error())
	}

	// do something with the clientset, e.g. getting all pods in the cluster:
	// pods, err := clientset.CoreV1().Pods("").List(context.TODO(), metav1.ListOptions{})
}
```

Go客户端实现使用pod的服务帐户以及环境变量`KUBERNETES_SERVICE_HOST`和`KUBERNETES_SERVICE_PORT`来识别它所在的集群。随后，它创建REST配置对象，客户端集可以通过该对象获得。

同样，在集群外部运行时，需要创建配置对象，但此配置是从本地kube配置中读取的:

```go
import (
	"context"
	"flag"
	"path/filepath"

	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/clientcmd"
	"k8s.io/client-go/util/homedir"
)

func main() {
	// get the passed (or default) kube config file path
	var kubeconfig *string
	if home := homedir.HomeDir(); home != "" {
		kubeconfig = flag.String("kubeconfig", filepath.Join(home, ".kube", "config"), "(optional) absolute path to the kubeconfig file")
	} else {
		kubeconfig = flag.String("kubeconfig", "", "absolute path to the kubeconfig file")
	}
	flag.Parse()

	config, err := clientcmd.BuildConfigFromFlags("", *kubeconfig)
	if err != nil {
		panic(err.Error())
	}

	clientset, err := kubernetes.NewForConfig(config)
	if err != nil {
		panic(err.Error())
	}

	// do something with the clientset, e.g. getting all pods in the cluster:
	// pods, err := clientset.CoreV1().Pods("").List(context.TODO(), metav1.ListOptions{})
}
```

同样，Kubernetes Go客户端为我们提供了一个简单的函数来解析kubeconfig文件以获取配置，然后可以用该配置创建一个clientset。

尝试运行这些简单的示例时，您还会遇到这两种方法之间的一个区别: 运行本地工具更容易，因为您不需要构建映像、将其推送到注册表，然后将其拉入集群。

**选择哪一个?**

假设您要以类似的方式构建自己的Kubernetes UI。当涉及到您的工具的Web服务器应该在哪里运行的决定时，有几件事需要考虑:

- **分发**: 在集群内部运行您的工具意味着您必须构建和分发docker镜像。相反，如果您希望用户在其机器上安装它，则必须分发本机二进制文件。对于这两种情况，网上都有大量的工具和资源。
- **可用性**: 当您的集群由于某种原因关闭时，用户可能无法访问托管在集群内部的工具。这带我们来到下一个要点:
- **用户入门体验**: 这可能是一个边缘用例，但本地托管的web工具可以在其所有组件安装在集群之前使用。这意味着您可以为新用户实现某种UI入门流程，使该工具更易于安装和设置。
- **兼容性**: 同一集群的多个用户可能安装了不同版本的您的(本地托管)工具。如果集群内只运行一个web服务器，则无法发生这种情况。
- **持久性**: 当需要存储工具特定的数据(即非Kubernetes资源)时，您可以将其存储在集群内(例如在ConfigMap中)。对于本地部署的变量，您还可以在用户的机器上存储用户特定的数据，如设置。这个决定在很大程度上取决于用例。
- **开发人员体验**: 似乎没有明显的区别，但值得注意的是，在开发集群内web服务器时，在开发期间，这个服务器仍然需要以某种方式支持集群外配置方法。否则，每次更改后都必须构建和部署镜像到集群中。

最终，工具是部署在集群内部还是外部完全取决于您，但始终要考虑用例并意识到使用它的上下文非常重要。您也可以选择为用户提供这两种选项。

对于我们在Glasskube，很明显我们希望为新用户(特别是那些刚接触Kubernetes世界的用户)提供一个易于使用的界面，他们可能还没有设置所有Glasskube集群组件。通过提供托管本地Web服务器的CLI命令和支持性Web UI，可以支持这些用户。

## 总结  

在本文中，我们探索了一些提供Web UI的Kubernetes工具，并从软件工程师的角度分析了这些工具的Web方面。显然没有一刀切的解决方案来设计和开发这样的工具，但以上列表希望能给出正确方向的提示。像软件工程中的任何事情一样:这取决于。

最后一个插播: 我在Glasskube工作，我们正在构建缺失的Kubernetes包管理器。如果您对我们的工作感兴趣，请务必给我们加星:`glasskube/glasskube`。我们也在研究一篇文章，关于不同CLI框架的比较，如果您更偏向命令行。如果这还不够，我们可能很快会写关于使用htmx的文章，因为它正在流行，我们需要您的关注。我已经能看到标题了:"我们如何通过使用看似老派的技术来减少95%的代码库" —— 我认为这以前没有做过;)
