<!--
title: 别再怪React了，你的状态管理“宿醉”该醒了！
cover: https://cdn.thenewstack.io/media/2025/12/c9b7f69f-pablo-merchan-montes-1kan9yrcqdc-unsplashb.jpg
summary: React 应用故障源于糟糕的状态架构，而非框架。盲目追求新状态库、滥用Context/Hooks，掩盖了数据流不清晰的问题。需理解数据流，有目的地设计状态，才能扩展应用。
-->

React 应用故障源于糟糕的状态架构，而非框架。盲目追求新状态库、滥用Context/Hooks，掩盖了数据流不清晰的问题。需理解数据流，有目的地设计状态，才能扩展应用。

> 译自：[Stop Blaming React for Your State Management Hangover](https://thenewstack.io/stop-blaming-react-for-your-state-management-hangover/)
> 
> 作者：Alexander T. Williams

每次 React 应用出现故障时，第一条推文总是各种“React 太烂了”。不，它不是（好吧，谁信啊，也许确实有一点），但真正出问题的是你对状态的心智模型。

开发者们不断地寻求新的状态管理库，就像宿醉的人寻求油腻食物一样：希望它能修复根本上是自作自受的问题。Zustand、Jotai、Recoil、Valtio——它们都是很棒的工具。

但如果你不理解数据如何在你的应用中流动，它们都无法将你从混乱中拯救出来。React 不是你的替罪羊：你的[状态架构](https://medium.com/@skylernelson_64801/state-architecture-patterns-in-react-part-2-the-top-heavy-architecture-flux-and-performance-a388b928ce89)才是罪魁祸首。

## 对“闪亮”状态管理解决方案的沉迷

React 生态系统[滋生新状态管理库](https://thenewstack.io/frontends-next-evolution-ai-powered-state-management/)和方法的速度，比 npm 警告你漏洞的速度还要快。每隔几个月，就会有一个新的库在 X 上流行起来，承诺带来简洁性、高性能并终结样板代码。开发者们争相安装，深信这次他们找到了“真命天子”。蜜月期持续到第一次 prop 逐层传递冲突或同步 bug 出现。然后，又回到了指责 React——再一次。

但这些库没有解决根本问题：**不清晰的数据流**。开发者们在没有问过数据“为什么”存在于某个位置的情况下，就一层一层地堆叠全局 store、context 和 hook。他们是在框架上修修补补地粘合逻辑，而不是设计一个架构。当所有东西都在更新其他所有东西时，你构建的是一个雷区，而不是一个 UI。

> 你无法通过将思考外包给最新的库来设计出清晰的架构。

React 赋予你的是可组合性。你如何利用它决定了你的应用是优雅还是脆弱。你无法通过将思考外包给最新的库来设计出清晰的架构。你需要通过理解单向数据流——React 的核心原则——并坚持它来做到这一点。

## 理解 Context 过载和 Provider 金字塔

如果你的组件树看起来像一个俄罗斯套娃的内部，你并不孤单。“Provider 金字塔”，即你应用的一半代码都生活在相互重叠的 context 中，是新的回调地狱。每个人都在追求全局状态的便利性，但 context 并非万能药。它是一把手术刀：精准使用时威力强大，滥用时则灾难重重。

开发者们经常[将所有东西都包裹在 context 中](https://stackoverflow.com/questions/75060633/react-context-performance-and-suggestions)，因为它感觉像是共享状态的涅槃。但每个 provider 都引入了复杂性。调试嵌套的 context 变成了对 `useContext` 调用的考古发掘。性能也会受到影响，因为重新渲染会层层级联。

> 事实是，大多数数据不需要是全局的。

不，[切换到 Zustand](https://tkdodo.eu/blog/working-with-zustand) 并不能神奇地解决这个问题。你仍然在错误的粒度上同步状态。更不用说，如果你正在运行实例，那么[容器安全](https://checkmarx.com/product/container-security/)又是另一个你需要担心并认真对待的事情。可以肯定地说，这不是我遇到过的最简单的一团糟。

事实是，大多数数据不需要是全局的。购物车？当然可以。主题偏好？也许吧。但那个“当前选中的标签页”或“临时筛选器”状态呢？让它保持局部。一旦你将所有东西都全局化，你就失去了对心智模型的控制。React 鼓励局部推理——尊重这个边界。

## 为什么 Redux 并非你想象中的恶棍

[Redux](https://thenewstack.io/top-10-javascript-libraries-to-use-in-2024/) 曾是[React 疲劳症的受气包](https://thenewstack.io/why-react-is-no-longer-the-undisputed-champion-of-javascript/)；但事后看来，它并非恶棍。它只是让你的架构变得诚实。Redux 迫使开发者思考数据流、action 语义和不可变性。这种纪律是痛苦的，但它暴露了逻辑的实际位置。真正的问题不是 Redux；而是团队如何滥用它。

许多人将 Redux 视为所有变量的垃圾场——从身份验证到模态框是否打开。结果是一个全局意大利面条式的 action 和 reducer 大杂烩，没有人能理解。然后，便出现了一波“Redux 太复杂”的思考文章，却刻意忽略了这种复杂性源于将 Redux 视为数据库而非协调层。

> 现代工具抽象掉了样板代码，但它们并没有消除对思维纪律的需求。

现代工具抽象掉了样板代码，但它们并没有消除对思维纪律的需求。无论你使用 Zustand、MobX 还是 React Query，同样的原则都适用：[状态属于它最有意义的地方](https://thenewstack.io/the-pros-and-cons-of-using-react-today/)。全局状态应该是一个例外，而不是默认选项。你不需要更少的库；你需要更少的借口。

## React Hooks 带来的简单性假象

React Hooks 本应简化事情。相反，它们却成了架构罪过的新藏身之处。自定义 Hook 非常适合抽象，但当你开始像俄罗斯套娃一样嵌套它们时，你就在创建隐式耦合。每个 `use` 都隐藏了[依赖关系和时序问题](https://react.dev/reference/react/use)，这些问题只会在生产环境中浮出水面——当你的组件树开始表现得像被附身一样时。

Hook 的诱人之处在于它们*感觉*可组合。但没有纪律的组合只是一层层的混乱。理解状态变化源头的心智成本迅速增加。你最终会得到十几个 Hook 以稍微不同的方式共享状态——每次重新渲染都会像多米诺骨牌一样触发其他 Hook。

简单性不是关于更少的代码行；而是关于可预测性。因果之间的心智跳跃越少，你的应用就会越健康。在你编写另一个 `useGlobalStore` 之前，请问你的 Hook 真的需要存在吗？大多数时候，你可以通过 props 和清晰的层级结构来解决它。

## 如何在不失去理智的情况下扩展你的 React 应用

每个 React 项目都始于整洁。然后现实降临：更多的功能、更多的组件、更多的开发者。突然间，状态就像一条不受管制的河流一样流动。这时团队就会恐慌并引入一个新的库。但扩展不是关于工具——而是关于模式。

将状态与使用它的组件并置。有意识地向下传递数据，而不是本能地传递。使用派生状态而不是重复真实来源。按领域而非便利性拆分 context provider。这些原则不是潮流；它们是永恒的。如果你将[架构视为一个活的系统](https://alexkondov.com/full-stack-tao-clean-architecture-react/)，而不是一个拼凑物，你就可以在不将其变成依赖迷宫的情况下扩展 React 应用。

> 即使在规模化应用中，大多数 React 混乱也源于忽视基本原理。

即使在规模化应用中，大多数 React 混乱也源于忽视基本原理。当清晰就能解决问题时，不要追求复杂性。框架会演变，语法会改变，但整洁架构的法则永远不会过时。React 不需要完美——只需要一致性。

## 框架不是问题，你的架构才是

因为状态头痛而责怪 React，就像因为糟糕的驾驶而责怪你的车一样：[为什么不直接换辆车，而不是抱怨呢](https://thenewstack.io/why-devs-are-ditching-react-for-preacts-simplicity-and-speed/)？框架完全按照你告诉它的去做。如果你的组件疲于奔命，你的 context 层过度膨胀，或者你的 Hook 与黑魔法无异，那都是你的问题。

React 在一件事上是有主见的：数据向下流动。其他一切——副作用、同步和缓存——都是你的责任。这不是一个 bug；这是一个特性。它迫使你有意图地构建。当你将这种责任推卸给 GitHub 上流行的任何东西时，你是在用理解换取暂时的解脱。

> 框架不会制造混乱；开发者才会。

你不需要用 Solid、Svelte 或 Vue 重写你的应用。你需要停止将抽象层修修补补地粘到你从未完全设计的架构上。框架不会制造混乱；开发者才会。一旦你接受了这一点，React 就不再是一种痛苦，而会成为一个伙伴。

## 结论

React 没有坏。是你的架构坏了。无休止地更换库、重塑模式和责怪框架，只会掩盖真相：状态管理很难，因为清晰思考很难。

解决方案不是另一个 Hook 或全局 store；而是谦逊和纪律。理解你的数据如何流动，有目的地设计你的状态，React 就会停止感觉像一个对手。别再为你的宿醉责怪 React 了。是你倒的酒。