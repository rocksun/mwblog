<!--
title: 使用Astro、Qwik 和 Fuse.js构建网站搜索
cover: https://cdn.thenewstack.io/media/2024/02/aa3866ed-tns-astro-site-search-featured-image-1024x538.jpg
-->

利用 Astro 的内容集合、静态端点和 Qwik 的 Astro 集成以及 Fuse.js，构建网站搜索功能的方法。

> 译自 [How to Build Site Search with Astro, Qwik and Fuse.js](https://thenewstack.io/how-to-build-site-search-with-astro-qwik-and-fuse-js/)，作者 Paul Scanlon 是一名资深软件工程师、独立开发者倡导者和技术作家。更多关于 Paul 的内容可在他的网站 paulie.dev 上找到。

在这篇文章中，我将解释如何利用Astro的[内容集合](https://docs.astro.build/en/guides/content-collections/)、[静态端点](https://docs.astro.build/en/guides/endpoints/)以及Qwik与[Fuse.js](https://www.fusejs.io/)的[Astro集成](https://github.com/QwikDev/astro)来构建站点搜索。

我已经准备了一个演示站点和开源仓库，你可以在以下链接找到：

- 🚀 https://tns-astro-site-search.netlify.app
- ⚙️ https://github.com/PaulieScanlon/tns-astro-site-search

![Zoom](https://cdn.thenewstack.io/media/2024/02/f48c127a-tns-astro-site-search-search-modal-1024x640.jpg)

## 内容集合是什么？

Astro提供了一种方便的方式来“批量”查询或转换相似类型的内容。在我的演示中，这将适用于所有以[MDX](https://mdxjs.com/)格式编写的博客文章。所有博客文章都共享相同的模板或布局和[模式](https://docs.astro.build/en/guides/content-collections/#defining-a-collection-schema)。以下是博客文章的模式。

```javascript
// src/content/config.js

import { z, defineCollection } from 'astro:content';

export const collections = {
  posts: defineCollection({
    type: 'content',
    schema: z.object({
      draft: z.boolean().optional(),
      audioFeedId: z.string().optional(),
      base: z.string(),
      title: z.string(),
      tags: z.array(z.string()).optional(),
      date: z.date(),
      author: z.string(),
      featuredImage: z.string(),
    }),
  }),
};
```

你可以在这里看到存储库中的`src`：[src/content/config](https://github.com/PaulieScanlon/tns-astro-site-search/blob/main/src/content/config.js).js。

为了更加保险，这里是我一篇博客文章的前置元数据（但所有博客文章将使用相同的模式）。

```markdown
// src/content/posts/2024/02/the-qwik-astro-audiofeed-experiment.mdx

---
base: posts
title: 中 Qwik, Astro, Audiofeed 实验
tags: [Qwik, Astro, Audiofeed, AI]
date: 2024-02-06
author: Paul Scanlon
featuredImage: https://res.cloudinary.com/www-paulie-dev/image/upload/v1707261626/paulie.dev/2024/02/get-started-with-qwik-astro_qtxmyq.jpg
---
```

你可以在存储库中查看源代码：[the-qwik-astro-audiofeed-experiment.mdx](https://github.com/PaulieScanlon/tns-astro-site-search/blob/main/src/content/posts/2024/02/the-qwik-astro-audiofeed-experiment.mdx)。

## 如何查询Astro的内容集合

为了构建站点搜索功能，我首先需要查询所有的博客文章。我使用了一个[静态端点](https://docs.astro.build/en/guides/endpoints/)来实现这一点。我称之为 `all-content.json.js`，它位于 `src/pages` 目录中。例如：

```javascript
// src/pages/all-content.json.js

import { getCollection } from 'astro:content';

export const GET = async () => {
  const posts = await getCollection('posts');

  const search = posts
    .filter((item) => item.data.draft !== true)
    .map((data) => {
      const {
        slug,
        data: { base, title, date },
      } = data;

      return {
        date: date,
        title: title,
        base: base,
        path: `/${base}/${slug}`,
      };
    })
    .sort((a, b) => b.date - a.date);

  return new Response(JSON.stringify({ search }));
};
```

一旦我使用 `getCollection('posts')` 查询了所有的博客文章，我会快速过滤掉可能处于草稿模式的任何博客文章，然后仅返回对搜索有用的前置元数据字段，并按日期排序。

结果被字符串化并作为标准响应返回。

以下是结果的样式。

```javascript
[
  {
    date: 2024-02-22T00:00:00.000Z,
    title: '如何使用 KwesForms 和 Astro 构建调查',
    base: 'posts',
    path: '/posts/2024/02/how-to-build-a-survey-with-kwesforms-and-astro'
  },
  {
    date: 2024-02-06T00:00:00.000Z,
    title: 'Qwik、Astro、Audiofeed 实验',
    base: 'posts',
    path: '/posts/2024/02/the-qwik-astro-audiofeed-experiment'
  }
  ...
]
```

你可以在这里看到存储库中的源代码：[src/pages/all-content.json.js](https://github.com/PaulieScanlon/tns-astro-site-search/blob/main/src/pages/all-content.json.js)。

这些数据提供了我开始构建搜索组件所需的全部信息。

## 如何查询静态端点

为了构建搜索组件（接下来会介绍！），我首先需要从静态端点查询数据，并将其传递给搜索组件。我在布局组件中查询数据，该组件存在于演示站点的每个页面中，例如：

```astro
// src/pages/index.astro
 
---
import Layout from '../layouts/layout.astro';
---
 
<Layout>
  <h1>Lorem ipsum</h1>
  <p>...</p>
</Layout>
```

你可以在这里看到存储库中的源代码：[src/pages/index.astro](https://github.com/PaulieScanlon/tns-astro-site-search/blob/main/src/pages/index.astro)。

以下是布局组件，它向端点发出服务器端请求。

```jsx
// src/layouts/layout.astro

---
import Search from '../components/search';

const content = await fetch(`${import.meta.env.PROD ? 'https://tns-astro-site-search.netlify.app' : 'http://localhost:4321'}/all-content.json`);
const { search } = await content.json();
---

<html lang='en'>
  <head>...</head>
  <body>
    <header>
       <Search data={search} />
    </header>
      <main>
        <slot />
      </main>
  </body>
</html>
```

这里需要指出的一件事是 fetch 中使用的 URL。如果站点已部署且 PROD 为 true，则静态端点的 URL 将为 [https://tns-astro-site-search.netlify.app/all-content.json](https://tns-astro-site-search.netlify.app/all-content.json)，而在开发中则使用本地主机 URL。

只要我能够查询搜索数据，我就可以通过 `data` 属性将其传递给我的搜索组件。

你可以在这里看到存储库中的 src：[src/layouts/layout.astro](https://github.com/PaulieScanlon/tns-astro-site-search/blob/main/src/layouts/layout.astro)。

## 构建搜索组件

为了构建搜索组件，需要安装两个附加依赖项。它们如下。

```bash
npm install fuse.js @qwikdev/astro
```

**Fuse.js**

我使用 [Fuse.js](https://www.fusejs.io/) 来帮助进行“模糊搜索”。键盘输入被捕获并传递给 Fuse.js。如果任何字母或单词与标题或日期匹配，Fuse.js 将返回该项。

**Qwik**

我使用 [Qwik 的 Astro 集成](https://github.com/QwikDev/astro)来帮助管理客户端状态。[Qwik 比 React 更轻量](https://thenewstack.io/how-quiks-astro-integration-beats-both-react-and-vanilla-js/)，并且比纯 JavaScript 更简洁。

剩下的步骤将涵盖如何设置搜索和过滤。我创建了一个简单的示例，你可以在这里预览：[https://tns-astro-site-search.netlify.app/simple](https://tns-astro-site-search.netlify.app/simple)。源代码可以在这里找到：[src/components/simple-search.jsx](https://github.com/PaulieScanlon/tns-astro-site-search/blob/main/src/components/simple-search.jsx)。

注意：我的演示中使用的示例包含大量额外的 CSS 和 JavaScript 来处理模态框，这并不是创建搜索功能所必需的。

## 搜索组件：第一步

第一步是创建搜索组件并返回一个 HTML 输入框。添加一个 `onInput$` 事件处理程序，并创建一个名为 `handleInput` 的函数来捕获按键。

```javascript
// src/components/simple-search.jsx

import { component$, $ } from '@builder.io/qwik';

const Search = component$(({ data }) => {
  const handleInput = $(async (event) => {
    const {
      target: { value },
    } = event;

  });

  return (
    <div>
      <input type='text' placeholder='搜索' onInput$={handleInput} />
    </div>
  );
});

export default Search;
```

## 搜索组件：第二步

接下来，导入 useSignal，并创建两个新的常量来保存所有数据和过滤后的数据。

```jsx
// src/components/simple-search.jsx

- import { component$, $ } from '@builder.io/qwik';
+ import { component$, $, useSignal } from '@builder.io/qwik';

const Search = component$(({ data }) => {
+  const all = useSignal(data);
+  const filtered = useSignal(data);

  const handleInput = $(async (event) => {
    const {
      target: { value },
    } = event;
  });

  return (
    <div>
      <input type='text' placeholder='搜索' onInput$={handleInput} />
    </div>
  );
});

export default Search;
```

## 搜索组件：第三步

接下来，导入并初始化 Fuse.js。Fuse.js 的配置接受来自 `useSignal` 常量（`all.value`）的值，并在任何输入值与标题或日期的值匹配时应用模糊过滤阈值为 0.5。

`fuse.searc`h 可用于过滤数组中不符合配置参数的任何项，并返回一个新数组。我将这个新数组称为“results”。

```jsx
// src/components/simple-search.jsx

import { component$, $, useSignal } from '@builder.io/qwik';

const Search = component$(({ data }) => {
  const all = useSignal(data);
  const filtered = useSignal(data);

  const handleInput = $(async (event) => {
    const {
      target: { value },
    } = event;

    const FuseModule = await import('fuse.js');
    const Fuse = FuseModule.default;

    const fuse = new Fuse(all.value, {
      threshold: 0.5,
      keys: ['title', 'date'],
    });

    const results = fuse.search(value).map((data) => {
      const { item: { base, path, title, date } } = data;

      return {
        title,
        date,
        path,
        base,
      };
    });

    if (value) {
      filtered.value = results;
    } else {
      filtered.value = all.value;
    }
  });

  return (
    <div>
      <input type='text' placeholder='搜索' onInput$={handleInput} />
    </div>
  );
});

export default Search;
```

## 搜索组件：第四步

接下来是添加一个 if 语句。如果从 HTML 输入中捕获到值，那么我将 `useSignal` `filtered.value` 设置为结果，如果未从 HTML 输入中捕获到值，那么我将 `useSignal` `filtered.value` 设置为 `all.value`。

这将返回一个过滤后的列表，或者整个列表。

```jsx
// src/components/simple.search.jsx

import { component$, $, useSignal } from '@builder.io/qwik';

const Search = component$(({ data }) => {
  const all = useSignal(data);
  const filtered = useSignal(data);

  const handleInput = $(async (event) => {
    ...

    if (value) {
      filtered.value = results;
    } else {
      filtered.value = all.value;
    }

  });

  return (
    <div>
      <input type='text' placeholder='搜索' onInput$={handleInput} />
    </div>
  );
});

export default Search;
```

## 搜索组件：第五步

最后一步是遍历 `filtered.value`（如果有长度）并返回项目列表。如果没有结果，则返回 `null`。

```jsx
// src/components/simple-search.jsx

import { component$, $, useSignal } from '@builder.io/qwik';

const Search = component$(({ data }) => {
  const all = useSignal(data);
  const filtered = useSignal(data);

  const handleInput = $(async (event) => {
   ...
  });

  return (
    <div>
      <input type='text' placeholder='搜索' onInput$={handleInput} />
      <ul>
        {filtered.value.length > 0
          ? filtered.value.map((data, index) => {
              const { path, title } = data;
              return (
                <li key={index}>
                  <a href={path}>{title}</a>
                </li>
              );
            })
          : null}
      </ul>
    </div>
  );
});

export default Search;
```

## 完成

至此，我们已经掌握了如何使用 Astro 的[内容集合](https://docs.astro.build/en/guides/content-collections/)查询数据的原理，如何通过[静态端点](https://docs.astro.build/en/guides/endpoints/)使数据可用，以及如何使用 [Fuse.js](https://www.fusejs.io/) 和[ Qwik 的 Astro 集成](https://github.com/QwikDev/astro)来实现模糊搜索并管理客户端状态。

我在我的网站上也采用了同样的方法，目前效果还不错！
