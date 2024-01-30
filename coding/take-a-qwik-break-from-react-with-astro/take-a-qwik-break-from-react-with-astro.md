<!--
title: Qwik带来简洁高效的Astro开发
cover: https://cdn.thenewstack.io/media/2024/01/28cd973c-quiw-break-from-react.jpg
-->

Paul Scanlon通过代码示例比较了React和Qwik，他认为Qwik值得作为React的替代品进行探索。

> 译自 [Take a Qwik Break from React with Astro](https://thenewstack.io/take-a-qwik-break-from-react-with-astro/)，作者 Paul Scanlon 是一名高级软件工程师、独立开发者倡导者和技术作家。可以在他的网站 paulie.dev 上找到更多关于 Paul 的信息。

在我们开始之前，有个免责声明: 我非常喜欢 React，但有时候我真的用不上它。

我最近的许多项目都是使用 [Astro](https://astro.build/) 构建的(默认情况下不会向客户端发送任何 JavaScript - 非常适合快速、轻量和高性能的内容网站)。但有时，我确实需要一点客户端 JavaScript 来实现交互。在这时，我发现自己在普通 Vanilla JavaScript 和 React 之间难以抉择。

一方面，Vanilla JavaScript 通常比 React 更轻量，但维护起来可能会变得困难。React 在一定程度上解决了这个问题，但对于最小的客户端 JavaScript 需求来说，它有点笨重。

出于这些原因(以及其他一些原因)，我开始研究 React 的替代方案。而且瞧，我发现了 [Qwik](https://qwik.builder.io/)。

## Qwik 是什么？

官方的产品营销信息如下:"Qwik 是一个全新的 Web 框架，可以为任何规模或复杂程度的 Web 应用程序提供即时加载。"

但是，对我来说，我更倾向于这样理解 Qwik: **像 React 一样编写代码，浏览器体验像 Vanilla**。

Qwik 与 React 在本质上完全不同，它是从零开始设计的，以促进框架在客户端和服务器端的工作需求的增长。

[Qwik 比 React 更轻量，比 Vanilla 更简洁](https://thenewstack.io/how-quiks-astro-integration-beats-both-react-and-vanilla-js/)，并且不需要任何额外的 `use client` 或 `client:load` 指令。它足够智能到可以在服务器端(如果必要的话)执行，并在客户端恢复。Qwik 团队比我讲述得好多了，所以可以访问文档来了解更多信息: [思考 Qwik](https://qwik.builder.io/docs/concepts/think-qwik/)。

## Qwik Astro 集成 

如我所言，我目前对 Qwik 的探索主要集中在我使用 Astro 的工作上。来自 [Jack Shelton](https://twitter.com/TheJackShelton) 的优秀 [@quikdev/astro](https://github.com/QwikDev/astro) 集成使得开始使用 Qwik 变得绝对轻松。这里有一段摘录自[文档](https://github.com/QwikDev/astro)。如你所见，开始使用只需要安装集成并将其添加到 Astro 配置中即可。

```js
// astro.config.mjs
 
import { defineConfig } from 'astro/config';
import qwikdev from '@qwikdev/astro';
 
export default defineConfig({
  integrations: [qwikdev()],
});
```

## 切换的不情愿

我可以理解切换的不情愿。我的许多“React 朋友”都表现出不愿意切换，声称他们已经掌握了 React，不想花时间学习新东西。这一点是公平的，但这两种技术真的有多大差异吗？

在下面的代码示例中，我将涵盖一些常见的 React 用例，并向您展示如何使用 Qwik 实现相同的功能。希望您同意，学习曲线并不陡峭。

随着所有这些准备就绪，我们现在可以开始了!

## 简单组件

这是一个简单的 React 组件。

### React 简单组件

```js
import React from 'react';
 
const SimpleReactComponent = () => {
  return (
    <div>
      <p>Hello, I'm a simple React component</p>
    </div>
  );
};
 
export default SimpleReactComponent;
```

导出默认 SimpleReactComponent;

这是 Qwik 版本。

### Qwik 简单组件

```js
import { component$ } from '@builder.io/qwik';
 
const SimpleQwikComponent = component$(() => {
  return (
    <div>
      <p>Hello, I'm a simple Qwik component</p>
    </div>
  );
});

export default SimpleQwikComponent;
```
 
主要区别在于使用 `component$`。完整解释可以在 Qwik 文档中找到:[component\$](https://qwik.builder.io/docs/components/overview/#component)。

## 状态与信号(State vs. Signal)

在下面的示例中，点击按钮将 `isVisible` 的值设置为 `true` 或 `false`。

这个布尔值用于确定是否返回包含 Rocket 表情符号的 `<span />`。它也用于在按钮中显示 “显示”或“隐藏”词。

你可以在下面的链接中看到这个 Qwik 组件的 `src` 代码和预览。

- 预览: https://qwik-break-from-react.netlify.app/use-signal-qwik-page/
- 仓库: https://github.com/PaulieScanlon/qwik-break-from-react/blob/main/src/components/use-signal-qwik-component.jsx

### useState React 组件

```js
import { useState } from 'react';
 
const UseStateBooleanReactComponent = () => {
  const [isVisible, setIsVisible] = useState(true);
 
  const handleVisibility = () => {
    setIsVisible(!isVisible);
  };
 
  return (
    <div>
      <p>
        <span>
          {isVisible ? (
            <span role='img' aria-label='Rocket'>
              🚀
            </span>
          ) : null}
        </span>
        Hello, I'm a useState boolean React component
      </p>
      <button onClick={handleVisibility}>{`${isVisible.value ? 'Hide' : 'Show'} Rocket`}</button>
    </div>
  );
};
 
export default UseStateBooleanReactComponent;
```
 
### useSignal Qwik 组件

```js
import { component$, useSignal, $ } from '@builder.io/qwik';
 
const UseSignalQwikComponent = component$(() => {
  const isVisible = useSignal(true);
 
  const handleVisibility = $(() => {
    isVisible.value = !isVisible.value;
  });
 
  return (
    <div>
      <p>
        <span>
          {isVisible.value ? (
            <span role='img' aria-label='Rocket'>
              🚀
            </span>
          ) : null}
        </span>
        Hello, I'm a useSignal Qwik component
      </p>
      <button onClick$={handleVisibility}>{`${isVisible.value ? 'Hide' : 'Show'} Rocket`}</button>
    </div>
  );
});
 
export default UseSignalQwikComponent;
```

这里的主要区别在于处理程序的定义方式以及状态或信号的声明方式。

函数声明用$()包装，将函数转换为[QRL](https://qwik.builder.io/docs/advanced/qrl/)。您可以在文档中阅读有关函数处理程序的更多信息: [重用事件处理程序](https://qwik.builder.io/docs/components/events/#reusing-event-handlers)。

在函数内部，事情会有点不同。使用 Qwik，您直接更新信号值。例如 isVisible.value = true。与 React 的 useState 不同，信号只包含值，不包含设置器对。

最后，注意 onClick 属性上的 trailing $。例如 onClick$。

## 状态与存储

在下面的示例中，+ 按钮将火箭添加到数组中，- 按钮删除最后添加的项。每次修改数组时，页面都会更新以反映更改。

您可以在下面的链接中查看这个 Qwik 组件的源代码和预览。

- 预览: https://qwik-break-from-react.netlify.app/use-store-qwik-page/
- 仓库: https://github.com/PaulieScanlon/qwik-break-from-react/blob/main/src/components/use-store-qwik-component.jsx

### useState React 组件

```js
import { useState } from 'react';
 
const UseStateBooleanReactComponent = () => {
  const [rockets, setRockets] = useState(['🚀']);
 
  const handleAdd = () => {
    setRockets((prevState) => [...prevState, '🚀']);
  };
 
  const handleRemove = () => {
    setRockets((prevState) => [...prevState.slice(0, -1)]);
  };
 
  return (
    <div>
      <div className='h-8'>
        {rockets.map((data, index) => {
          return (
            <span key={index} role='img' aria-label='Rocket'>
              {data}
            </span>
          );
        })}
      </div>
      <p>Hello, I'm a useState array React component</p>
      <div className='flex gap-4'>
        <button onClick={handleAdd}>+</button>
        <button onClick={handleRemove}>-</button>
      </div>
    </div>
  );
};
 
export default UseStateBooleanReactComponent;
```

### useStore Qwik 组件

```js
import { component$, useStore, $ } from '@builder.io/qwik';
 
const UseStoreQwikComponent = component$(() => {
  const rockets = useStore(['🚀']);
 
  const handleAdd = $(() => {
    rockets.push('🚀');
  });
 
  const handleRemove = $(() => {
    rockets.pop();
  });
 
  return (
    <div>
      <div className='h-8'>
        {rockets.map((data) => {
          return (
            <span role='img' aria-label='Rocket'>
              {data}
            </span>
          );
        })}
      </div>
      <p>Hello, I'm a useStore Qwik component</p>
      <div className='flex gap-4'>
        <button onClick$={handleAdd}>+</button>
        <button onClick$={handleRemove}>-</button>
      </div>
    </div>
  );
});
 
export default UseStoreQwikComponent;
```


与 `useSignal` 示例类似，函数声明被 $() 包装，但在我看来，更新数组的方法更直接。可以使用简单/标准的 JavaScript `.push` 或 `.pop`，而不是 React 的方法，必须先扩展前状态然后再修改它。

## 客户端数据获取

在 Astro 的上下文中，即使有客户端数据请求可能会感到奇怪，但你可能仍然需要进行一点客户端数据获取，下面是如何做的。

您可以在下面的链接中查看此 Qwik 组件的 `src` 代码和预览。

- 预览: https://qwik-break-from-react.netlify.app/client-fetch-qwik-page/
- 仓库: https://github.com/PaulieScanlon/qwik-break-from-react/blob/main/src/components/client-fetch-qwik-component.jsx

### useEffect React 组件

```js
import { useState, useEffect } from 'react';
 
const ClientFetchReactComponent = () => {
  const [data, setData] = useState(null);
 
  useEffect(() => {
    const getData = async () => {
      const response = await fetch('https://api.github.com/repos/BuilderIO/qwik/pulls/1', {
        method: 'GET',
      });
 
      if (!response.ok) {
        throw new Error();
      }
 
      const json = await response.json();
      setData(json);
      try {
      } catch (error) {
        console.error(error);
      }
    };
 
    getData();
  }, []);
 
  return (
    <div>
      <p>Hello, I'm a simple Client fetch React component</p>
      {data ? <pre>{JSON.stringify(data, null, 2)}</pre> : Loading...}
    </div>
  );
};
 
export default ClientFetchReactComponent;
```

### useVisibleTask Qwik 组件

```js
import { component$, useVisibleTask$, useSignal } from '@builder.io/qwik';
 
const ClientFetchQwikComponent = component$(() => {
  const data = useSignal(null);
 
  useVisibleTask$(async () => {
    try {
      const response = await fetch('https://api.github.com/repos/BuilderIO/qwik/pulls/1', {
        method: 'GET',
      });
 
      if (!response.ok) {
        throw new Error();
      }
 
      const json = await response.json();
      data.value = json;
    } catch (error) {
      console.error(error);
    }
  });
 
  return (
    <div>
      <p>Hello, I'm a simple Client fetch Qwik component</p>
      {data.value ? <pre>{JSON.stringify(data.value, null, 2)}</pre> : Loading...}
    </div>
  );
});
 
export default ClientFetchQwikComponent;
```


如您所知，React 的 `useEffect` 必须返回一个函数，而不是一个 promise。为了在页面加载时异步获取数据，带有空依赖数组的 `useEffect` 需要包含一个可以使用 `async/await` 的函数。

然而，Qwik 有 [useVisibleTask](https://qwik.builder.io/docs/components/tasks/#usevisibletask) - 它可以返回一个 promise。`useVisibleTask` 只在浏览器中执行，但如果您确实希望对服务器端数据获取使用类似的方法，Qwik 还有 [useTask](https://qwik.builder.io/docs/components/tasks/#usetask)。

## 总结

这些只是 React 和 Qwik 之间差异/相似性的几个示例，我个人真的越来越喜欢 Qwik 的思维方式。相当长的一段时间以来，我一直具有一些人所说的 “React 思维”，但从 React 中快速休息让我环顾四周，看看其他 JavaScript 巨头都在忙些什么(Qwik 由 [Angular 创造者 Miško Hevery 创建](https://thenewstack.io/angular-qwik-creator-on-how-js-frameworks-handle-reactivity/))。

考虑迁移离开 React 可能会令人生畏，但当想到 React 过去是什么(一个客户端状态管理库)以及它现在正在重新设计成什么......[在此插入您的理解]，现在可能是调查您的替代方案的好时机。

没有人知道未来会怎样，但 Qwik 至少是为现在设计的，用于现在，我目前真的很享受这种体验。前进，[Qwik](https://qwik.builder.io/) 团队!
