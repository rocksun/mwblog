# React 服务器组件简介

![React 服务器组件简介的特色图片](https://cdn.thenewstack.io/media/2024/04/de6cd4b4-react-server-components-in-a-nutshell-featured-image-1024x538.jpg)

哇，最近关于 [React 服务器组件](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023) (RSC) 的讨论很多，而且在很大程度上，在阅读了 [互联网上最聪明的人](https://thenewstack.io/react-panel-frontend-should-embrace-react-server-components/) 的所有非常聪明的解释之后，我并没有真正理解任何内容。但从那时起，我花时间试验了 [Waku](https://waku.gg/)，现在我认为 RSC 比我最初想象的要简单得多。

## 什么是 Waku？

Waku（wah-ku）或わく在日语中意为“框架”。作为 [一个极简的 React 框架](https://thenewstack.io/new-framework-lets-devs-explore-react-server-components/)，它旨在加速初创公司和机构的开发人员构建中小型 React 项目的工作。根据 Waku 网站，这些项目包括营销网站、轻量级电子商务和 Web 应用程序。

然而，该网站的介绍中遗漏的是 Waku 支持 React 服务器组件——因此，如果你想自己试用它们，你不需要使用 Next.js（我对此表示感谢）。值得一提的是，Waku 目前正在快速开发中，只应在非生产项目中使用。

## React 服务器组件简介

所以我的看法是：RSC 使 React 开发人员能够在组件级别访问异步服务器端请求和结果数据。

在 RSC 之前，Next.js、Gatsby、Remix 和 Astro 等框架要求你在路由级别进行服务器端请求。

以下是一些示例，说明你如何在上述每个框架中实现此目的。

## Next.js 路由（应用程序路由器）

```
import { useRouter } from 'next/router';

export default function App() {
  const router = useRouter();

  const getData = async () => {
    const res = await fetch('https://api.github.com/repos/vercel/next.js');
    return res.json();
  };

  return (
    <div>
      <button onClick={async () => {
        const data = await getData();
        router.push({
          pathname: '/about',
          query: { data },
        });
      }}>
        Go to About Page
      </button>
    </div>
  );
}
```

在此路由中，有一个名为 `getData` 的函数，它向 GitHub API 发出异步请求并返回响应，然后可以使用 `getData` 函数提取该响应并将其提供给路由或页面。

## Next.js 路由（页面路由器）

```
import { getServerSideProps } from 'next';

export async function getServerSideProps() {
  const res = await fetch('https://api.github.com/repos/vercel/next.js');
  const data = await res.json();

  return {
    props: { data },
  };
}

export default function About({ data }) {
  return (
    <div>
      <h1>About Page</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
```

在此路由中，有一个名为 `getServerSideProps` 的函数，它向 GitHub API 发出异步请求，并通过 `data` prop 将响应返回给路由或页面。

## Gatsby 路由

```
import { graphql } from 'gatsby';

export const query = graphql`
  query {
    github {
      repository(owner: "vercel", name: "next.js") {
        name
        description
        stargazers {
          totalCount
        }
      }
    }
  }
`;

export default function About({ data }) {
  return (
    <div>
      <h1>About Page</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
```

在此路由中，有一个名为 `getServerData` 的函数，它向 GitHub API 发出异步请求，并通过 `data` prop 将响应返回给路由或页面。

## Remix 路由

```
import { useLoaderData } from 'remix';

export default function About() {
  const data = useLoaderData();

  return (
    <div>
      <h1>About Page</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export async function loader() {
  const res = await fetch('https://api.github.com/repos/vercel/next.js');
  const data = await res.json();

  return data;
}
```

在此路由中，有一个名为 `loader` 的函数，它向 GitHub API 发出异步请求并返回响应，然后可以使用 `useLoaderData` hook 提取该响应并将其提供给页面。

## Astro 路由

```
---
data:
  github:
    repository:
      owner: vercel
      name: next.js
---

<h1>About Page</h1>
<pre>{{ github.repository.name }}</pre>
<pre>{{ github.repository.description }}</pre>
<pre>{{ github.repository.stargazers.totalCount }}</pre>
```

在此路由中，从 [Astro 的特殊“frontmatter”围栏](https://thenewstack.io/how-to-use-astro-with-a-sprinkling-of-react/) 中向 GitHub API 发出异步请求。然后，路由或页面可以直接访问 `data`。

## Prop 钻取

你会注意到，在所有这些示例中，数据都通过名为 `data` 的 prop 传递给名为 `ParentComponent` 的组件。

### ParentComponent

```
import { ChildComponent } from './ChildComponent';

export default function ParentComponent({ data }) {
  return (
    <div>
      <ChildComponent data={data} />
    </div>
  );
}
```

`ParentComponent` 可能看起来像这样，其中数据再次传递给另一个名为 `ChildComponent` 的组件。

### ChildComponent

```
export default function ChildComponent({ data }) {
  return (
    <div>
      <h1>Child Component</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
```

最后，在 `ChildComponent` 中，你可能希望使用此数据；正如你所看到的，数据在到达目的地之前必须进行一段旅程。

## 组件级数据获取

正如你可能知道的那样，如果你重构此应用程序或移动 `Parent` 或 `Child` 组件，你还需要重新连接数据旅程。

在应用程序的生命周期中，这种情况并不少见，并且根据应用程序的复杂程度，将决定在数据到达预期目的地之前你需要深入到什么程度。

这是 RSC 真正可以提供帮助的地方。以下是我使用 Waku 采用的方法。

## Waku 路由

```
import { useRouter } from 'waku';

export default function App() {
  const router = useRouter();

  return (
    <div>
      <button onClick={() => router.push('/about')}>
        Go to About Page
      </button>
    </div>
  );
}
```

使用 Waku，我仍然有一个路由，但在此级别不会进行数据获取。

### Waku ParentComponent

```
import { ChildComponent } from './ChildComponent';

export default function ParentComponent() {
  return (
    <div>
      <ChildComponent />
    </div>
  );
}
```

`ParentComponet` 仍然导入并返回 `ChildComponent`，但没有 prop，也没有任何内容传递给 `ChildComponent`。

### Waku ChildComponent

```
import { useServerData } from 'waku';

export default function ChildComponent() {
  const data = useServerData();

  return (
    <div>
      <h1>Child Component</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
```

这是 `ChildComponent`；同样，没有数据通过 prop 传递。相反，所有数据获取都在组件中进行，服务器端。

## 对某些人来说很熟悉

在组件级别访问数据的方法可能对某些人来说很熟悉。对我来说是这样，因为我是一个狂热的 Gatsby 用户。

### Gatsby 的 `useStaticQuery` hook

在 [2019 年 2 月，Gatsby 引入了 `useStaticQuery` hook](https://www.gatsbyjs.com/blog/2019-02-20-introducing-use-static-query/)，虽然获取数据的方法截然不同（我并不是试图将此与 RSC 进行比较），但理论有点相似，原因如下。

- `use
**在 Gatsby 中，你从未使用 GraphQL（一个常见的误解）获取数据；相反，你正在查询它。数据获取发生在构建时，但使用 `useStaticQuery` 钩子，你能够从任何组件、任何级别访问数据，而无需通过道具传递它。**

**使用 RSC，数据获取发生在运行时，因此虽然 RSC 和 Gatsby 的 `useStaticQuery` 钩子之间的数据获取方法不同，但当你能够从任何组件中访问数据时，你所做的架构选择是有道理的。**

## 数据获取需要思考

然而，使用 RSC，你仍然需要考虑在哪些场景中执行组件级数据获取有意义，而不是路由级数据获取。

一方面，在需要数据的组件中获取和访问数据很方便；但另一方面，如果你有几个组件都在同一路由上独立获取数据，这会对性能产生负面影响吗？

在某些情况下，进行单个路由级请求并将结果数据通过道具传递给需要它的组件可能仍然有意义，而不是进行多个组件级数据请求。值得一提的是，采用明智的缓存策略可能会限制多个组件级数据请求的影响。

## 最后的想法

在我看来，RSC 只是在构建数据密集型 React 应用程序时可用的另一种选择。我认为它们不会解决每个用例，它们也不是为了解决每个用例而设计的。在许多情况下，它们可能不是正确的选择，但这没关系。

正如每个开发人员在其职业生涯中多次对任何给定方法所说的那样，这取决于具体情况。

我从使用 Gatsby 的经验中知道，从组件中轻松访问数据是有好处的。它可以真正帮助理解应用程序正在做什么，因为逻辑、数据和结果用户界面元素整齐地位于同一文件中，并且与追逐道具并尝试遵循数据旅程相比，开发人员体验通常更好。

总之，我真的很喜欢 RSC，我认为随着时间的推移，我们都会发现最佳实践和在开发时需要注意的事项。但就目前而言，我认为它们是向前迈出的非常酷的一步，我期待进一步尝试。如果你有兴趣自己尝试 RSC，请尝试一下 Waku。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。