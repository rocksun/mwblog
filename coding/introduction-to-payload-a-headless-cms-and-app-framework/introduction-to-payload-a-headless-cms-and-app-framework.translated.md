# Payload 简介：一款 Headless CMS 和应用程序框架

![介绍 Payload 的专题图片：一款 Headless CMS 和应用程序框架](https://cdn.thenewstack.io/media/2024/09/cda64814-getty-images-0udnq131w5g-unsplash-1024x724.jpg)

Web 开发有趣的一点在于，它始终试图将视觉设计与数据设计融合在一起。虽然它们需要在网站和 Web 应用程序中结合使用，但它们是截然不同的学科。像 [Ruby on Rails](https://thenewstack.io/return-to-the-rails-way-installing-ruby-on-rails-in-2024/) 这样的框架一直在努力将它们融合在一起。

[Payload CMS](https://payloadcms.com/) 大胆地将自己描述为“Headless CMS 和应用程序框架”。虽然我们不会将用户界面称为“Head”，但 [Headless](https://thenewstack.io/headless-cms-vs-no-code-website-builders/) 仅指没有专属前端的框架。内容管理系统 (CMS) 只是一个操作结构化数据的框架。例如，如果数据是一个博客，那么被管理的内容就是帖子。

[什么是 Payload](https://payloadcms.com/docs/getting-started/what-is-payload) 页面很好地阐述了这一困境，并试图解释其自身的角度。它认识到 CMS 往往会“将内容的呈现与其存储绑定在一起”，从而切中要害。因此，Payload 的目标是与您想使用的任何前端一起工作。

截至目前，Payload 正在进行一些重大更改，并将发布版本 3，因此旧文档可能已过时。按照说明操作后，我得到了一个旧版本。毫无疑问，这将会得到解决。请查看其 [Discord 频道](https://discord.com/invite/r6sCXqVk3v) 了解最新信息。

## 安装

到目前为止，[安装](https://payloadcms.com/docs/getting-started/installation) 的先决条件选项对于数据库来说有点窄，但可以选择一个关系型数据库和一个基于文档的数据库示例：

在我的 MacBook 上，我通过 Homebrew 安装了一个社区版 [MongoDB](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/)：

```bash
brew tap mongodb/brew
brew install mongodb-community@6.0
```

然后，我通过将其添加为服务来启动 Mongo：

```bash
brew services start mongodb-community@6.0
```

我们可以将连接字符串视为 URL，因此我们应该能够设置 Payload。

在另一个浏览器选项卡中，我安装了 Payload 应用程序：

```bash
npm create payload@latest my-payload-app
```

我设置了一个演示项目，很快就准备好了启动：

```bash
cd my-payload-app
```

其中一个示例项目失败了，因为它需要 Discord！正如我所说，由于即将进行的更改，一些文档和视频还没有完全匹配。这当然是一件好事，因为该项目非常活跃。我选择了 `payload-demo` 模板，效果很好。

然后 `yarn dev` 运行项目：

```bash
yarn dev
```

连接到 MongoDB 后，它会同时启动 Payload 管理员（位于 `localhost:3000/admin`）和演示应用程序（标记为 Next.js 应用程序，这是用于该模板的 React 框架）。

## Payload 应用程序

直接进入应用程序，我们会看到：

![Payload 应用程序的屏幕截图](https://cdn.thenewstack.io/media/2024/09/01-payload-app.png)

此时，还没有任何内容，因此您会被引导至管理仪表板以开始创建一些内容。管理仪表板允许我创建具有电子邮件地址的管理员角色或用户角色。

仪表板本身有助于解释 Payload 的实际用途：

![Payload 仪表板的屏幕截图](https://cdn.thenewstack.io/media/2024/09/02-payload-dashboard.png)

Payload 将所有内容组织成集合中的类型集。这包括页面和用户。我们可以创建新类型并立即开始使用它们，就像我们将要做的那样。

这里有一个小小的困惑：首先，您按下“Seed the database”链接，您将获得许多演示内容。这将清除所有已存在的内容。您还需要创建一个“主页”，否则您将只看到上面显示的默认模板页面，这可能会让您认为您没有内容，而实际上您有。

一旦我理解了该系统，我就创建了一些简单但没有灵感的页面类型内容：

![页面类型内容的屏幕截图](https://cdn.thenewstack.io/media/2024/09/03-page-type-content.png)

使用管理界面添加到集合后，您可以发布任何更改（提交它们）。这将自动更新您的网站。

## 使用代码完成所有操作

在现阶段，我所做的并不比您使用 [Publii](https://thenewstack.io/jamstack-style-build-a-website-with-netlify-and-publii/) 等工具所能做的更多，后者也像一个经典的 CMS。但是，Payload 有两点很突出。您不仅可以使用 REST 与之通信，还可以重用 Payload 的部分内容，从而模糊谁拥有什么的界限。而且您可以使用代码完成所有操作，这就是我们现在要做的。

例如，您可以看到用户是一种集合类型，可供我们使用：

![用户集合类型的屏幕截图](https://cdn.thenewstack.io/media/2024/09/04-users-collection-type.png)

这些注册在哪里？都在 `payload.config.ts` 文件中。首先导入它们，然后（如下所示）将它们添加到已知集合中：

```typescript
// payload.config.ts
import { buildConfig } from 'payload/config';
import path from 'path';
// ... other imports
import Users from './collections/Users';

export default buildConfig({
  // ...
  collections: [
    Users,
    // Your other collections
  ],
});
```

在 `Users` 文件夹中，我们有一个基本的 `index.ts` 文件，它定义了 `Users` 类型。虽然这包含了很多 Typescript，但其中大部分只是描述了管理员访问权限。Payload 允许相当精细的访问控制：

```typescript
// ./collections/Users/index.ts
import { CollectionConfig } from 'payload/types';

const Users: CollectionConfig = {
  // ...
  access: {
    // ... granular access control settings
  },
};

export default Users;
```
```
| 1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859 |
|-------------------------------------------------------------------------------------------------------------------|
| import type { CollectionConfig } from 'payload/types' import { admins } from '../../access/admins' import { anyone } from '../../access/anyone' import adminsAndUser from './access/adminsAndUser' import { checkRole } from './checkRole' import { ensureFirstUserIsAdmin } from './hooks/ensureFirstUserIsAdmin' import { loginAfterCreate } from './hooks/loginAfterCreate' const Users: CollectionConfig = { slug: 'users', admin: { useAsTitle: 'name', defaultColumns: ['name', 'email'], }, access: { read: adminsAndUser, create: anyone, update: adminsAndUser, delete: admins, admin: ({ req: { user } }) => checkRole(['admin'], user), }, hooks: { afterChange: [loginAfterCreate], }, auth: true, fields: [ { name: 'name', type: 'text', }, { name: 'roles', type: 'select', hasMany: true, defaultValue: ['user'], options: [ { label: 'admin', value: 'admin', }, { label: 'user', value: 'user', }, ], hooks: { beforeChange: [ensureFirstUserIsAdmin], }, access: { read: admins, create: admins, update: admins, }, }, ], timestamps: true, } export default Users |

然而，我们将对此进行精简，并创建我们自己的集合类型，不带管理员或钩子。
假设我们只需要一个名为 Members 的类型。我将创建相应的文件夹并创建一个精简的 index.ts：

```

```
| 123456789101112131415161718 |
|-----------------------------------|
| import type { CollectionConfig } from 'payload/types' const Members: CollectionConfig = { slug: 'members', fields: [ { name: 'name', type: 'text', }, { name: 'membership', type: 'number', }, ], timestamps: true, } export default Members |
```

这只是描述了一个具有名称和数字成员资格字段的类型。Payload 通过不同的字段完成了大量工作。
服务器检测到更改：

并且集合会立即在管理面板中识别新类型：

我们可以像操作任何其他集合类型一样操作成员：

最后一件事。让我们通过 REST 访问我们的新成员：

所以我们被拒之门外了。但是等等……还记得我们为了简化 Member 集合而删除的粒度访问权限吗？让我们尝试稍微恢复一下：

```
| 12345678910111213141516171819202122 |
|----------------------------------------------------|
| import type { CollectionConfig } from 'payload/types'import { anyone } from '../../access/anyone'const Members: CollectionConfig = { slug: 'members', access: { read: anyone, }, fields: [ { name: 'name', type: 'text', }, { name: 'memebership', type: 'number', }, ], timestamps: true,}export default Members |
```

我所做的只是添加了“anyone”的导入并添加了该访问权限。现在让我们试试：
很好。我们创建了一个新集合，在管理控制台中看到了它，为其创建了一个条目，甚至通过 REST 请求了它。所以这个内容现在可以用于我的网站了。

## 结论
正如我之前所说，Payload 目前正在过渡到版本 3，因此在您研究它之前，等待一段时间可能是有意义的。也就是说，如果您不坚持您的前端和后端必须进行“强制联姻”，那么这个想法已经相当不错了。

[
YOUTUBE.COM/THENEWSTACK
技术发展日新月异，请不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、采访、演示等内容。
](https://youtube.com/thenewstack?sub_confirmation=1)
```