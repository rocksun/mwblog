
<!--
title: 导致SimKube 2.0出现的Bug
cover: https://substackcdn.com/image/fetch/w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25f23ea4-e63c-4842-ae3e-ab4b34a80ce0_1024x1024.jpeg
-->

> 译自：[The bug that led to SimKube 2.0](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20)
> 
> 作者：Drmorr

你们中的一些人可能已经注意到（在我的新设计的网站上！）SimKube 现在是 2.0 版本了——实际上，已经有几个月了。大约一个月前，我在 lobste.rs 上发表了一条评论，说我希望更多的人谈论他们的调试过程，而 SimKube 2.0 的出现是由于一个有点令人尴尬的 bug，所以我想在这篇文章中“以身作则”，谈谈我为 SimKube 经历的调试过程。

你们中的一些人可能已经注意到（在我的[新设计的网站](https://simkube.dev/)上！）SimKube 现在是 2.0 版本了——实际上，这种情况已经持续几个月了。 大约一个月前，我曾在 [lobste.rs 上发表过评论](https://lobste.rs/s/usawel/debugging_memory_corruption_who_wrote_2#c_6huyba)，希望更多的人谈论他们的调试过程，而 SimKube 2.0 的出现是由于一个有点令人尴尬的 bug，所以我想在这篇文章中“以身作则”，谈谈我为 SimKube 经历的调试过程。

附：您还可以在 [GitHub 上](https://github.com/acrlabs/simkube)找到“完整”的 SimKube 代码，以及我们今天讨论的[更改差异](https://github.com/acrlabs/simkube/commit/7678afca8ecf43d944977cebc8c9861835ed5048)。

## 首先，来自我们赞助商的关于版本控制的消息

如果您在互联网上花费过任何时间，您就会知道版本编号方案是一个备受争议的话题；[SemVer](https://semver.org/) 可能是“大多数”人熟悉的方案，但也有 [CalVer](https://calver.org/)，被 Ubuntu 等项目使用，还有“有一个数字并使其有时增加”（又名，Google Chrome 版本控制方案），还有“使用你的 Git SHA 作为版本号”的人群，然后是 Google Cloud Platform 正在做的任何事情：

```
> gcloud version
Google Cloud SDK 511.0.0
alpha 2025.02.18
beta 2025.02.18
bq 2.1.13
bundled-python3-unix 3.12.8
core 2025.02.18
gcloud-crc32c 1.0.0
gke-gcloud-auth-plugin 0.5.9
gsutil 5.33
```

部分问题在于，版本号被用于不同的受众来传达不同的信息。营销人员想要一个与大型新功能集或产品发布相对应的版本号，而技术人员想要一个传达有关他们需要做多少工作才能升级的信息的版本号（即，您是否进行了任何重大更改，您是否修复了一些错误，您是否引入了新错误等）。

无论如何，我不是来引发关于版本控制方案的争论的，我只是想说明 SimKube 2.0 实际上意味着什么。SimKube 项目遵循“尽力而为”的 semver 方案，这意味着“当大数字上升时，存在一个我在发布时知道的重大更改，如果其中一个较小的数字上升，可能仍然存在重大更改，我只是当时不知道。” 换句话说——SimKube 2.0 与 SimKube 1.x 不兼容，但它们仍然是同一个项目。 没有发生一些大的重写或其他事情。 而且，既然我们已经度过了“2.0”的难关，未来的重大更改（希望）看起来不会那么重要了。 我想我们会看到这在实践中如何发挥作用，但现在，让我们谈谈启发这一切的 bug。

## 为什么这些对象没有被创建？

好的，快速回顾一下：SimKube 分为多个组件；`sk-tracer` 收集 Kubernetes 集群中发生的事件的“跟踪”，`sk-driver` 在模拟环境中重放来自这些跟踪的事件。 当用户报告说并非他们跟踪中的所有事件都在他们的模拟中被重放时，我首先发现了有问题的 bug。 我完成了所有标准的调试步骤：

1. 我尝试在自己的设置上运行，它似乎工作正常。
2. 我从用户的集群中获取了日志，然后说“嗯？这没有任何意义，也没有足够的信息来实际了解发生了什么。”
3. 与用户设置了一个 Zoom 通话来观看它崩溃，我观察到它确实崩溃了。 即使在实时调试会话中，仍然无法弄清楚发生了什么。
4. 最后将其缩小到“Google Cloud 上发生了一些奇怪的事情”，所以去年我在 KubeCon 时，我启动了 ACRL 的第一个 Google Cloud 环境来尝试重现它。

在这一点上，我实际上能够重现这个问题，并且在这一点上我意识到 Google Cloud 与这个问题完全无关，而且我也可以在本地很好地重现这个问题——我只是没有*意识到*我正在本地重现它。

那么我们实际遇到的问题是什么呢？简而言之，用户报告说并非他们跟踪的所有对象都在其模拟环境中被创建。具体来说，用户试图跟踪 Kubernetes Deployments 和 ServiceAccounts，而且因为我在创建跟踪文件格式时具有一定的前瞻性，所以我可以从他们生成的跟踪文件中看到这不是用户错误：

```
{
    "trackedObjects": {
        "v1.ServiceAccount": {
            "podSpecTemplatePath": null
        },
        "apps/v1.Deployment": {
            "podSpecTemplatePath": "/spec/template"
        }
    }
}
```

我还看到跟踪文件没有存储任何实际的 ServiceAccount 资源，这意味着 bug 出在 `sk-tracer` 的某个地方。查看用户的 `sk-tracer` 日志，我在其初始化的最开始看到了如下模式：

```
2024-11-12T16:59:08.711589Z INFO sk-store/src/trace_store.rs:171: microservices-demo/adservice - ObjectApplied @ 1731430748
2024-11-12T16:59:08.711867Z INFO sk-store/src/trace_store.rs:171: microservices-demo/cartservice - ObjectApplied @ 1731430748
2024-11-12T16:59:08.712140Z INFO sk-store/src/trace_store.rs:171: microservices-demo/checkoutservice - ObjectApplied @ 1731430748
...
2024-11-12T16:59:08.715746Z INFO sk-store/src/trace_store.rs:171: microservices-demo/frontend-external - ObjectDeleted @ 1731430748
2024-11-12T16:59:08.715841Z INFO sk-store/src/trace_store.rs:171: gmp-system/alertmanager - ObjectDeleted @ 1731430748
2024-11-12T16:59:08.715912Z INFO sk-store/src/trace_store.rs:171: default/kubernetes - ObjectDeleted @ 1731430748
```

这些日志记录了 `sk-tracer` 正在观测的一系列事件：正如预期的那样，我们看到一大堆对象在日志的第一部分被创建，然后（出乎意料地）一大堆对象被删除。

顺便说一句，这就是为什么我认为我无法在第一步重现这个问题的原因——在我的环境中，我每次都从头开始创建，我没有看到所有的 `ObjectDeleted` 日志行。我*确实*看到了一些看起来有点像这样的日志行：

```
2024-11-12T16:59:08.715912Z INFO sk-store/src/trace_store.rs:171: - ObjectDeleted @ 1731430748
```

正如你所看到的，*一些*对象正在被删除，但是没有名称，所以我无法分辨是哪些对象。我认为这很奇怪，但是这些事件有点虚假（不像我从用户那里得到的日志），我认为这是一个不相关的 bug。

但无论如何，既然我知道问题发生在我自己的环境中，并且我*大致*知道该在哪里查找，我的下一个想法是启动调试器并单步执行代码。为什么它决定在 `sk-tracer` 启动时从跟踪中删除一些对象？如果我能设置一个断点并四处查看，也许我就能弄清楚发生了什么。不幸的是，Rust 中的调试状态是，我尽可能客气地说，*糟糕透顶*。Rust 代码有两种不同的调试后端，分别基于 [gdb](https://sourceware.org/gdb/) 和 [lldb](https://lldb.llvm.org/)。它们的工作方式略有不同，但没有一个工作*良好*。简而言之，这些调试器是为 C 和 C++ 代码编写和设计的，几乎不了解 Rust。像“如何检查这个 `Option` 的内容？”这样的简单事情需要你手动取消引用一堆地址（当然喜欢一直输入 `/x *(int*)0x12345678`），甚至更糟糕的是，它们对 [traits](https://doc.rust-lang.org/book/ch10-02-traits.html) 没有任何了解，这意味着你可以对对象执行的操作类型受到了*严重*限制[9](https://blog.appliedcomputing.io/p/the-bug-that-led-to-simkube-20#footnote-9-157665317)。

所以相反，我又回到了基于打印行的调试。好吧，根据用户问题的上下文，有一件事很清楚：我的日志行需要打印被删除对象的*类型*，而不仅仅是名称。所以我做了一个 [quick fix](https://github.com/acrlabs/simkube/commit/951eb7ecfd1c20eca9b5ea3ce63ec5bca306f91d) 来更新它，现在我得到了如下所示的日志行：

```
2024-11-12T16:59:08.711589Z INFO sk-store/src/trace_store.rs:171: ObjectApplied @ 1739899948: apps/v1.Deployment microservices-demo/adservice
```

一旦我有了这些日志行，事情就变得……稍微清楚了一些：也就是说，一种类型的所有对象都被创建，然后另一种类型的所有对象都被创建，然后第一种类型的所有对象都被删除。现在我们有进展了！问题出在这段代码中（为了清晰起见，略有简化）：

```
let mut apis = vec![];
for gvk in tracked_objects.keys() {
    let stream = build_stream_for_tracked_obj(apiset, gvk).await?;
    apis.push(stream);
}

let obj_stream = select_all(apis);

while let Some(res) = obj_stream.next().await {
    let ts = clock.now_ts();

    match res {
        Ok(evt) => handle_obj_event(evt, ts),
        Err(err) => {
            skerr!(err, "watcher received error on stream");
        },
    }
}
```

因为 `sk-tracer` 可以被配置为监视任意 Kubernetes 资源类型，所以我们在这段代码中使用了动态 API；对于用户配置的每种资源类型（Deployments、ServiceAccounts 等），我们都会创建一个单独的 watcher 流，该流接收与该对象对应的 [GVK](https://book.kubebuilder.io/cronjob-tutorial/gvks.html) 的“事件”。什么是事件呢？它是一组已从集群应用或删除的 Kubernetes 对象；这些对象从 [kube-rs 运行时](https://github.com/kube-rs/kube) 传入。事件本身不带时间戳，因此我们改为收集*接收*事件的时间戳，并将（时间戳，事件）对传递给 `handle_obj_event`。该函数是做什么的？

```
fn handle_obj_event(&mut self, evt: Event<DynamicObject>, ts: i64) {
    let mut store = self.store.lock().unwrap();
    match evt {
        Event::Applied(obj) => store.create_or_update_obj(&obj, ts),
        Event::Deleted(obj) => store.delete_obj(&obj, ts),
        Event::Restarted(objs) => store.update_all_objs(&objs, ts);
    }
}
```

看起来很简单：如果创建或修改了对象，我们会收到一个 `Applied` 事件；如果删除了对象，我们会收到一个 `Deleted` 事件。那么……这个 `Restarted` 事件是什么？嗯，有可能监视集群中更改的程序重新启动（或者 `sk-tracer` *本身* 重新启动），在这种情况下，我们会收到集群中当前所有对象的列表。但是，如果在中间期间删除了某些内容会发生什么？我们无法知道它，因此 SimKube 所做的是跟踪我们见过的所有对象，然后将我们在最新更新中未获得的对象标记为“已删除”。这是难题的一部分。

第二部分需要了解如何处理这些流：我们为每种对象类型创建一个流，然后使用 `select_all` 异步处理*每个对象类型*的更新。这意味着，当 `sk-tracer` 首次启动时，我们*首先*获得一个更新*所有* ServiceAccount 对象（例如）的事件，*然后*我们获得一个更新*所有* Deployment 对象的事件。但是，至关重要的是，没有 ServiceAccount 对象出现在第二个事件中，这意味着跟踪/删除逻辑启动并删除刚刚记录的所有 ServiceAccount。哎呀！

达到这一点只需要大量盯着代码，并试图在我脑海中推理事情，直到灵光一闪——异步处理可能会有一些令人惊讶的行为！

## 那么为什么要发布新的主要版本？

好的，现在我们了解了问题是什么，我们该如何解决？解决方案是让 `sk-tracer` 在跟踪对象名称的同时，还跟踪对象*类型*（即其 GVK）；这样，当它收到 `Restarted` 事件时，它只能将协调逻辑应用于*该类型*的对象，而不是它见过的所有对象。

进行此更改需要在跟踪中存储对象的 GVK 以及对象的名称。现在，我*可以*在仍然支持旧版本的跟踪文件格式的同时做到这一点，但是在自从我首次开发跟踪格式以来，我意识到它在很多方面都不是很可扩展，因此我选择利用此错误来改善格式的可扩展性。而且由于我现在用户很少，因此我实际上并不担心破坏向后兼容性，因此我选择直接这样做。而且，由于无论如何我都要发布一个新的主要版本，因此我借此机会更新了所有依赖项，并进行了一些其他小的重大更改。

所以无论如何，这就是我的 SimKube 调试故事！不知道是否有人觉得有趣，但我总是喜欢阅读人们如何解决问题，所以希望你也喜欢！下次我将讨论新版本中我真正兴奋的一些新功能。

与往常一样，感谢您的阅读，

~drmorr
