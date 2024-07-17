# 优雅地终止：优雅关闭指南

**阅读 packagemain.tech 上的原文**

您是否曾经因沮丧而拔掉电脑的电源线？虽然这似乎是一个快速解决方案，但它会导致数据丢失和系统不稳定。在软件世界中，存在类似的概念：硬关闭。这种突然的终止会导致与物理对应物相同的问题。值得庆幸的是，有一种更好的方法：优雅关闭。

通过集成优雅关闭，我们向服务提供提前通知。这使它能够完成正在进行的请求，可能将状态信息保存到磁盘，并最终避免在关闭期间发生数据损坏。

本指南将深入探讨优雅关闭的世界，特别关注它们在 Kubernetes 上运行的 Go 应用程序中的实现。

# Unix 系统中的信号

在基于 Unix 的系统中实现优雅关闭的关键工具之一是信号的概念，简单来说，信号是一种简单的方式，用于从另一个进程向一个进程传达一个特定的事情。通过了解信号的工作原理，我们可以利用它们在应用程序中实现受控的终止过程，确保平稳且数据安全的关闭过程。

有很多信号，您可以在 [此处](https://en.wikipedia.org/wiki/Signal_(IPC)) 找到它们，但我们只关心关闭信号：

* **SIGTERM**— 发送到进程以请求其终止。最常用，我们将在后面重点介绍。
* **SIGKILL**— “立即退出”，无法干预。
* **SIGINT**— 中断信号（例如 Ctrl+C）
* **SIGQUIT**— 退出信号（例如 Ctrl+D）

这些信号可以从用户（Ctrl+C / Ctrl+D）、从另一个程序/进程或从系统本身（内核/操作系统）发送，例如 **SIGSEGV** 又名段错误是由操作系统发送的。

# 我们的实验服务

为了在实际环境中探索优雅关闭的世界，让我们创建一个简单的服务，我们可以用它来进行实验。这个“实验”服务将有一个单一的端点，它通过调用 Redis 的 [INCR](https://redis.io/docs/latest/commands/incr/) 命令来模拟一些现实世界的工作（我们将添加一个轻微的延迟）。我们还将提供一个基本的 Kubernetes 配置来测试平台如何处理终止信号。

最终目标：确保我们的服务优雅地处理关闭，而不会丢失任何请求/数据。通过比较并行发送的请求数量与 Redis 中的最终计数器值，我们将能够验证我们的优雅关闭实现是否成功。

我们不会详细介绍设置 Kubernetes 集群和 Redis 的过程，但您可以在我们的 [Github 存储库](https://github.com/plutov/packagemain/tree/master/graceful-shutdown) 中找到完整的设置。

验证过程如下：

- 将 Redis 和 Go 应用程序部署到 Kubernetes。
- 使用 `vegeta` 发送 1000 个请求（25/秒，持续 40 秒）。
- 在 vegeta 运行时，通过更新镜像标签来初始化 Kubernetes **滚动更新**。
- 连接到 Redis 以验证“计数器”，它应该为 1000。

让我们从我们的基本 Go HTTP 服务器开始。

```go
package main

import (
	"net/http"
	"os"
	"time"

	"github.com/go-redis/redis"
)

func main() {
	redisdb := redis.NewClient(&redis.Options{
		Addr: os.Getenv("REDIS_ADDR"),
	})
	server := http.Server{
		Addr: ":8080",
	}
	http.HandleFunc("/incr", func(w http.ResponseWriter, r *http.Request) {
		go processRequest(redisdb)
		w.WriteHeader(http.StatusOK)
	})
	server.ListenAndServe()
}

func processRequest(redisdb *redis.Client) {
	// 在这里模拟一些业务逻辑
	time.Sleep(time.Second * 5)
	redisdb.Incr("counter")
}
```

当我们使用此代码运行验证过程时，我们会看到一些请求失败，并且 **计数器小于 1000**（每次运行的数字可能会有所不同）。

这清楚地表明我们在滚动更新期间丢失了一些数据。😢

# 在 Go 中处理信号

Go 提供了一个 [signal](https://pkg.go.dev/os/signal) 包，允许您处理 Unix 信号。需要注意的是，默认情况下，SIGINT 和 SIGTERM 信号会导致 Go 程序退出。为了使我们的 Go 应用程序不会如此突然地退出，我们需要处理传入的信号。

有两种方法可以做到这一点。

使用通道：

```go
c := make(chan os.Signal, 1)
signal.Notify(c, syscall.SIGTERM)
```

使用上下文（现在首选方法）：

```go
ctx, stop := signal.NotifyContext(context.Background(), syscall.SIGTERM)
defer stop()
```

**NotifyContext** 返回父上下文的副本，当收到列出的信号之一时，当返回的 **stop()** 函数被调用时，或者当父上下文的 Done 通道被关闭时，该副本被标记为已完成（其 Done 通道被关闭），以先发生者为准。

我们当前的 HTTP 服务器实现存在一些问题：
- 我们有一个运行缓慢的 `processRequest` 协程，并且由于我们没有处理终止信号，程序会自动退出，这意味着所有正在运行的协程也会被终止。
- 程序没有关闭任何连接。
让我们重写它。

graceful-shutdown/main.go
```go
package main

import (
	"context"
	"log"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/go-redis/redis/v8"
	"golang.org/x/sync/errgroup"
	"sync"
)

// 导入
var wg sync.WaitGroup

func main() {
	ctx, stop := signal.NotifyContext(context.Background(), syscall.SIGTERM)
	defer stop()
	// redisdb, server
	http.HandleFunc("/incr", func(w http.ResponseWriter, r *http.Request) {
		wg.Add(1)
		go processRequest(redisdb)
		w.WriteHeader(http.StatusOK)
	})
	// 将其设为协程
	go server.ListenAndServe()
	// 监听中断信号
	<-ctx.Done()
	// 停止服务器
	if err := server.Shutdown(context.Background()); err != nil {
		log.Fatalf("无法关闭：%v\n", err)
	}
	// 等待所有协程完成
	wg.Wait()
	// 关闭 Redis 连接
	redisdb.Close()
	os.Exit(0)
}

func processRequest(redisdb *redis.Client) {
	defer wg.Done()
	// 在这里模拟一些业务逻辑
	time.Sleep(time.Second * 5)
	redisdb.Incr("counter")
}

以下是更新摘要：

- 添加了 **signal.NotifyContext** 来监听 SIGTERM 终止信号。
- 引入了一个 **sync.WaitGroup** 来跟踪正在进行的请求（`processRequest` 协程）。
- 将服务器包装在一个协程中，并使用 **server.Shutdown** 与上下文一起优雅地停止接受新连接。
- 使用 **wg.Wait()** 确保所有正在进行的请求（`processRequest` 协程）在继续之前完成。
- 资源清理：添加了 **redisdb.Close()** 在退出之前正确关闭 Redis 连接。
- 清洁退出：使用 **os.Exit(0)** 表示成功终止。

现在，如果我们重复验证过程，我们将看到所有 1000 个请求都已正确处理。🎉

# Web 框架/HTTP 库
像 Echo、Gin、Fiber 等框架会为每个传入请求生成一个协程，为其提供上下文，然后根据您决定的路由调用您的函数/处理程序。在我们的例子中，它将是为“/incr”路径提供的 `HandleFunc` 的匿名函数。

当您拦截 **SIGTERM** 信号并要求您的框架优雅地关闭时，会发生两件重要的事情（为了简化）：

- 您的框架停止接受传入请求
- 它等待任何现有的传入请求完成（隐式等待协程结束）。
*注意：一旦 Kubernetes 将您的 Pod 标记为“Terminating”，它也会停止将来自负载均衡器的传入流量定向到您的 Pod。*

# 可选：关闭超时
终止进程可能很复杂，尤其是在关闭连接等许多步骤涉及的情况下。为了确保一切顺利运行，您可以设置超时。此超时充当安全网，如果进程花费的时间超过预期，则会优雅地退出进程。

```go
shutdownCtx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
```
defer cancel()
go func() {
	if err := server.Shutdown(shutdownCtx); err != nil {
		log.Fatalf("无法关闭：%v\n", err)
	}
}()
select {
case <-shutdownCtx.Done():
	if shutdownCtx.Err() == context.DeadlineExceeded {
		log.Fatalln("超时，强制关闭")
	}
	os.Exit(0)
}

# Kubernetes 终止生命周期
由于我们使用 Kubernetes 部署了我们的服务，让我们深入了解它如何终止 Pod。一旦 Kubernetes 决定终止 Pod，以下事件将发生：

- Pod 被设置为“Terminating”状态，并从所有服务的端点列表中删除。
- **preStop** 钩子如果定义则执行。
- **SIGTERM** 信号被发送到 Pod。但是，现在我们的应用程序知道该怎么做！
- Kubernetes 等待一个宽限期（**terminationGracePeriodSeconds**），默认情况下为 30 秒。
- **SIGKILL** 信号被发送到 Pod，并且 Pod 被删除。

如您所见，如果您有一个长时间运行的终止过程，则可能需要增加 **terminationGracePeriodSeconds** 设置，**允许您的应用程序有足够的时间优雅地关闭。

# 结论
优雅关闭可以保护数据完整性，保持无缝的用户体验，并优化资源管理。凭借其丰富的标准库和对并发的重视，Go 使开发人员能够轻松地集成优雅关闭实践——这是在 Kubernetes 等容器化或编排环境中部署的应用程序的必要条件。

您可以在 [我们的 Github 存储库](https://github.com/plutov/packagemain/tree/master/graceful-shutdown) 中找到 Go 代码和 Kubernetes 清单。