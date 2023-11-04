<!--
# 少代码替代低代码
https://cdn.thenewstack.io/media/2023/11/5be2b166-pencil-1024x683.jpg
Image from New Africa on Shutterstock.
 -->

目标是用尽可能少的代码实现尽可能多的价值。让我们来看看实现用更少代码做更多事的技术、工具和框架。

译自 [Less Code Alternatives to Low Code](https://thenewstack.io/less-code-alternatives-to-low-code/) 。

在我们系列文章的[第一部分](https://yylives.cc/2023/08/14/broken-promises-of-the-low-code-approach/)，我们分析了“低代码”和“少代码”在思想上的区别。我们明确了虽然[低代码解决方案](https://thenewstack.io/is-low-code-and-no-code-adoption-too-good-to-be-true/)让更多人可参与软件开发，但它存在局限性，特别是在开发复杂系统时。

增加的每一行代码都会提高系统的复杂度和维护负担。因此，目标是让团队用尽可能少的代码实现尽可能多的价值。在本文中，我们将探讨实现用更少代码做更多事的技术、工具和框架。

## 改变思维方式

拥抱“[最小化编程](https://thenewstack.io/low-code-vs-no-code/)”理念非常重要。这种理念本质上倾向追求代码的清晰性，激励你识别代码中不可或缺的元素，然后抛弃其他部分。是否存在更简洁的解决方案？工具能否用更少的代码实现相同的结果？我正在构建独特且具有价值的东西，还是在重复解决已被解决的问题？

每一行代码都必须从它所提供的潜在价值和代表的未来负担进行审视。通过避免或删除不必要的代码，利用他人的工作来减少这种负担。

## 调整过程

这种对“少码”的倾向不仅仅局限于个别开发者，而应该渗透到整个软件开发生命周期。代码评审不应仅视为批评环节，而应作为精简、明晰和简化代码的团队协作工作。同样，重构应被视为利用新知识改进旧代码的常规练习。一个更简洁、流畅的代码库就像一个组织良好的工作空间: 它能提高工作效率。自动化测试与此相辅相成，起着安全网的作用。它允许你修剪代码库并替换组件，同时确保新版本的表现如预期。

## 从低代码向少代码迈进的框架和工具

现代框架通过减少执行常见任务所需编写的代码量，极大地提高了开发效率。框架的底层代码由社区进行了测试和维护，减轻了周边维护负担。代码生成器不仅避免了重复性的击键，还确保生成的代码本身具有一致性和高效性。此外，我们开始看到AI和自动化技术为开发者提供新的支持，使其工作更具生产力。

在本节中，我们首先查看一些辅助前端开发的工具。之后，我们再深入研究几个真正体现“少代码”方法优势的工具。

## 前端开发中低代码的替代工具

前端开发有许多选择，虽然几种工具广为人知，但这个领域发展迅速，新的工具层出不穷。这种工具的不断变化可能会让人觉得这块领域善变，好像团队只是追随潮流，但实际情况通常不是这样。这些新进入者往往解决新的问题，以新方式解决现有问题，或针对特定利基进行优化。它们借鉴现有工具的经验教训而构建，通常将它们作为增强或互操作性的基础以帮助采用。

例如，Next.js 在 React 的基础上增加了意见和功能，这些功能帮助创建 Web 应用程序。它可以帮助解决混合静态和服务器端渲染内容、基于页面的路由、数据获取、中间件等常见挑战。

Next.js 利用文件系统提供自动路由，消除了单独的路由配置的需要。这大大简化了代码，使其更易于理解和维护。

```bash
app/
├─ page.js
└─ about/
   └─ page.js
```

在这个结构中，`app/page.js` 和 `app/about/page.js` 文件自动成为应用程序中的页面路由(`/` 和 `/about`)。

Next.js 还通过允许开发人员为 API 创建自定义路由处理程序来方便后端开发;这些文件约定命名为 `[route].js`。

```js
// app/api/route.js
export async function GET() {
  const res = await fetch('<https://mydata.example.com/latest>', {
    headers: { 'Content-Type': 'application/json' },
  });
  const data = await res.json();
 
  return Response.json(data);
}
```

相比之下，Astro更注重内容，具有确保博客、作品集、电子商务或营销网站等页面加载时间的功能。Astro的部分水合特性在减少发送到浏览器的代码量方面是一个突破。与传统的完全水合整个应用程序的框架不同，Astro仅向浏览器发送必要的JavaScript，从而极大地减少了加载时间。

```jsx
// This component won't send any JavaScript to the client
// Great for static sites or server-rendered pages
 
<html>
  <body>
    <h1>Hello, world!</h1>
  </body>
</html>
 
// This component sends a tiny amount of JavaScript to the client
// Astro will automatically only hydrate the <Counter /> component, nothing else
 
<html>
  <body>
    <Counter client:load />
  </body>
</html>
```

虽然Astro提供了自己的组件框架，但它也与React、Svelte和Vue等多种其他框架互操作。

其他工具关注构建时间改进、托管和预览、无障碍性、自动化测试、类型安全等围绕开发网站和应用程序的许多其他任务。

探索和选择适合您情况的工具，而不是最熟悉的工具，可以在很少投入的情况下极大地影响您的应用程序。

## 后端开发的低代码替代工具

后端工具的变化节奏一度非常缓慢。然而，最近这个领域变得更加活跃，以至于很容易错过新工具的全貌。与前端开发一样，这些新选择通常解决新的问题，或在现有选项基础上进一步提高生产力和稳定性。

不去探索这些新选项，会导致团队从事低价值、没有差异化的工作，或认为过去的挑战至今仍未解决。

例如，[Supabase在PostgreSQL基础上](https://thenewstack.io/supabase-takes-aim-at-firebase-with-a-scalable-postgres-service/)，结合其他一些开源工具，提供了一整套后端开发工具，用于构建和托管API、数据持久化、函数和认证等，所有这些都增强了PostgreSQL数据库。

Supabase可以以极少的代码实现用户认证:

```js
import { createClient } from '@supabase/supabase-js'
 
const supabase = createClient('<https://your-supabase-url>', 'your-public-api-key')
 
async function signUp(email, password) {
  const { user, error } = await supabase.auth.signUp({
    email: email,
    password: password,
  })
 
  if (error) console.error(error)
  else console.log(user)
}
```

另一个进步领域是基础设施即代码，也称为自我配置运行时。这些是工具、框架或平台，尽可能减少构建应用程序的重复工作，让团队只关注特定产品的代码。这类新兴选项包括Nitric、Encore、Shuttle、Ampt和Wing等，每种方法针对这个问题及其适用场景各有不同。

以下是一个使用Nitric构建的API示例，它消除了使用传统IaC工具构建部署项目的需要。相反，要部署必要的基础设施，Nitric CLI会自动创建资源规范，然后配置和设置运行应用代码所需的API网关和文档存储。

```js 
import { api, collection } from '@nitric/sdk'
import { v4 as uuid } from 'uuid'
 
const profileApi = api('public')
const profiles = collection('profiles').for('writing', 'reading')
 
profileApi.post('/profiles', async (ctx) => {
  const id = uuid()
 
  // Store the new profile in the profiles collection
  await profiles.doc(id).set({
    name: ctx.req.json().name,
    age: ctx.req.json().age,
    homeTown: ctx.req.json().homeTown,
  })
 
  // Set a JSON HTTP response
  ctx.res.json({
    msg: `Profile with id $[id] created.`,
  })
})
```

## 适应变化

在敏捷和效率至关重要的时代，“少代码”不仅是编写更少的代码，而是利用最好的工具、实践和思维方式，以更少的努力交付更多价值。随着技术格局不断发展，开发者和团队保持好奇心和适应变化至关重要。

工具和产品格局的变化并非简单追随潮流，而是关乎抽象、效率和提供构建更好系统的新方法。
