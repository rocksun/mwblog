<!--
title: SolidJS创始人：细粒度响应式，前端未来新战场
cover: https://cdn.thenewstack.io/media/2025/11/bcda7b35-solidjsryancarniato.jpg
summary: SolidJS将引入新原语Projections，优化响应式架构。Ryan Carniato强调Signals并非总能提升性能，细粒度渲染是关键。框架还利用Async Signals和Transitions处理异步数据。
-->

SolidJS将引入新原语Projections，优化响应式架构。Ryan Carniato强调Signals并非总能提升性能，细粒度渲染是关键。框架还利用Async Signals和Transitions处理异步数据。

> 译自：[SolidJS Creator on Fine-Grained Reactivity as Next Frontier](https://thenewstack.io/solidjs-creator-on-fine-grained-reactivity-as-next-frontier/)
> 
> 作者：Loraine Lawson

Solid 计划在其响应式架构中引入一个新的原语，SolidJS 的创建者 [Ryan Carniato](https://github.com/ryansolid) 在上周的 JSNation 大会上透露。

这之所以重要，有两个原因：首先，作为框架领域的领导者，Carniato 正在展示他所预见的未来所有 JavaScript 框架在扩展其能力方面的方向；其次，Solid 的发展有时会引发其他框架的效仿，正如我们在 [Angular](https://thenewstack.io/angular-v21-adds-signal-forms-new-mcp-server/) 和 [Preact](https://thenewstack.io/why-devs-are-ditching-react-for-preacts-simplicity-and-speed/) 中看到的 [Signals 采用](https://thenewstack.io/javascript-in-2023-signals-reacts-rsc-and-full-stack-js/)。

Carniato 将 Signals 解释为“像电子表格”，其中普通的赋值代表一个时间点。

“这意味着在完成时，变量 A 反映当前的和，但如果 B 或 C 发生变化，你必须再次执行赋值。”他说道。

他补充说，Signals 只是一组帮助表示同步的原语。当他在 2018 年开源 Solid.js 时，Signals 已经存在了近十年，但由于 React 组件模型，Signals 已经失宠，他说道。

“当几乎所有除 React 以外的框架都将 Signals 作为一等公民采用时，其影响是难以忽视的。所以很棒，对吗？故事结束了，”他说。“不，我认为：我们只是处于一个更大变化的开始，我不是唯一有这种想法的人。”

他也不是在谈论人工智能，而是关于如何最大限度地利用应用程序的底层架构问题。

“仅仅拥有 Signals 是不够的。Signals 是一种改变机制，但你如何使用它们才是关键，”他说道。

他表示，使 Signals 强大的共同点在于对驱动应用程序的数据图的了解。他补充说，这使开发人员能够做“我们本来不容易做到的不可思议的事情”。

他在演讲中探讨了 Signals 所赋予的能力，介绍了引用 Solid 即将推出的功能（可能目前尚未发布）的代码示例。其中包括一项针对该框架的新原语提案。

## Signals 不等同于更快的性能

Carniato 首先审视了性能，因为这是最容易谈论的，并且“可以说是最不重要的”，他说道。

“这始于揭穿一个常见的误解：我正在使用 Signals，所以我的应用程序框架一定更快，”他说。“不幸的是，它并非如此，正如 React 团队的 [Joe Savona](https://conf.react.dev/speaker/90f2d599-df38-40b7-9878-ff82d16ce353) 所发现的——如果你看了他在 React Conf 2025 的演讲，他展示了添加任何状态管理实际上都会降低框架的性能上限。”

Carniato 补充说，虽然 React 编译器可能允许开发人员编写更优化的代码，但它对绝对性能没有显著影响。

他解释说，将 [MobX](https://mobx.js.org/README.html)、[Zustand](https://zustand.docs.pmnd.rs/) 或 [Signals 添加到 React](https://thenewstack.io/did-signals-just-land-in-react/)，甚至将 Signals 添加到 Preact，并不能保证在所有情况下都能提高性能。事实上，平均而言，它们会使性能变慢。这是因为框架是围绕虚拟 DOM (VDOM) 构建的，每次状态更新时，框架都必须重新运行组件函数并对 VDOM 树进行差异比较，即比较旧的虚拟树和新的虚拟树以查找更改。

他表示，Signals 和更佳性能的答案在于细粒度渲染。为此，SolidJS 消除了 VDOM，并使用响应式图谱仅更新依赖于已更改数据的精确、细粒度 DOM 节点。Solid 以及 Svelte 和 Vue 都加入了 Solid 的行列，拥有细粒度渲染树。

“想象一个应用程序，你需要将状态拉高，以便在多个点可用，比如标题中的购物车和页面深处的购买按钮，”他说道。“你更新状态，会触发整个树的重新渲染，但实际上只需要更新购物车，我们却做了所有这些额外的工作。”

> “这始于揭穿一个常见的误解：我正在使用 Signals，所以我的应用程序框架一定更快。”
> 
> **– SolidJS 的创建者 Ryan Carniato**

通常，开发人员被告知要使用 memoize，即缓存函数调用的结果，当再次出现相同的输入时返回缓存的结果，而不是重新计算结果。

SolidJS、Vue 和 Svelte 使用诸如 Signals 之类的响应式原语，它们本质上是 memoize 的。但 memoization 在速度和内存之间创建了一种权衡。

“你可以意识到发送到购买按钮的数据没有变化，只运行那一条路径。通常，这就是 React 编译器所做的。这也是 Svelte 3 所做的，”他说。“如果购物车发生了变化，这是无法避免的：从状态的所有者到该变化，所有组件都需要重新运行。我们可以修剪沿途未变化的分支，但变化必须到达它在 UI 中的位置。”

他表示，你使用 Signals 的点进入树并成为一个新的路径。

“然而，通过细粒度渲染，所有 props 都以这种方式工作，”他说。“默认情况下，你可以在应用程序的顶部或底部声明此数据，将其通过 10 个组件传递，以获得完全相同的结果。它不需要重新运行整个组件或其任何父级，只需更改部分。”

他表示，这导致“我的组件是否会重新运行”这一整个类别消失，并且性能组合不再是问题。

他表示，Svelte 和 Vue 也加入了 Solid 的细粒度渲染行列。

## Solid 的新原语

Store 是代理，其中每个属性都有可能成为自己的 Signal。在使用 Store 的过程中，Carniato 意识到存在一些问题，这些问题需要驱动细粒度数据，以及从单一来源开始但又希望分叉或拆分响应性的情况。

“在更改表格上的选中类时检查每一行是一种浪费，但将‘是否选中’包含在每一行中并不总是实用，特别是当数据在多个地方共享时，”他说。“有时我们只需要将响应式数据投射到其他数据上，而无需修改源。有时，我们需要能够创建该数据的临时扩展，例如合并和乐观更改，而无需提交它们。”

他解释了 SolidJS 响应性模型中的两个高级概念，两者都旨在消除对复杂副作用（如 React 中的 useEffect）的需求来管理状态同步。

第一个是 **Projections**（投影），这将是 [Solid](https://github.com/solidjs/solid) 的一个新[原语](https://primitives.solidjs.community/)。它仍在开发中。Carniato 解释说，Projections 将响应性解释并拆分为多个不同的源。它们就像你放在主数据上的专业过滤器或镜头。它们是细粒度、派生的且非变异的。他还解释说，它们还允许开发人员创建临时更改，例如乐观 UI 更新（在服务器实际确认之前立即向用户显示其更改），而无需更改核心应用程序数据。

“虽然你可能不经常使用它们，但它们代表了一个我们以前在前端框架中从未真正找到良好解决方案的领域——一个既细粒度又派生的原语，”他说道。

第二个是 **Async Signals**（异步信号），它已作为 SolidJs 的一部分，通过 createResource 实现。异步信号是一种将慢速数据直接集成到基于读取的快速、同步 UI 流程中的解决方案。

> “虽然你可能不经常使用它们，但它们代表了一个我们以前在前端框架中从未真正找到良好解决方案的领域——一个既细粒度又派生的原语。”
> 
> **– Carniato**

传统模型以写入为中心，这意味着你必须在慢速数据到达后手动告知框架进行更新，这通常会导致 useEffect 或生命周期方法中出现复杂的逻辑。但 Solid 的方法以读取为中心，因此它只应在没有数据可渲染时暂停（一个“读取”问题）。

“对你来说可能有趣的是，因为我们是细粒度的，并且因为我们可以将响应性推到读取发生的地方，”他说。“基本上，在这个模型中，子节点会自动变为兄弟节点。”

他随后演示了细粒度响应性方法的加载速度：他指出，整个页面加载了两秒钟，因为它们都并行运行。

他还讨论了如何利用这一点来创建“自愈响应性”，其中响应式图谱了解所有依赖关系，允许框架在单击“重置”按钮时自动将错误追溯到异步源并重试获取——而无需重新运行组件函数。

虽然细粒度响应性保证了速度，但在处理非紧急、异步更新时，应用程序仍然面临着一个被称为“撕裂”的一致性问题。Carniato 指出，SolidJS 在初始加载后默认会发生撕裂——例如，计数器数字可能会立即更新，但伴随的慢速获取的短语会短暂显示旧数据。

为了解决这个问题，SolidJS 使用了 [**Transitions**（过渡）](https://www.solidjs.com/tutorial/async_transitions)，它允许开发人员将更新标记为非紧急。这个原语对于实现异步数据的平滑、并发渲染至关重要。Carniato 解释说，Transitions 还可以“将突变和异步获取联系起来，以消除围绕数据和待定状态的奇怪竞态条件”。Transitions 可以用于确保应用程序在慢速数据更改期间不会出现视觉“撕裂”。

他指出，Solid 自 2020 年左右就有了这些功能，这使其在原语方面积累了经验。Transitions 是构建功能齐全的乐观 UI 的关键机制。

但随着框架倾向于细粒度响应性，最好的还在后头。

“我认为我们正处于下一件大事的悬崖边上，”Carniato 告诉听众。