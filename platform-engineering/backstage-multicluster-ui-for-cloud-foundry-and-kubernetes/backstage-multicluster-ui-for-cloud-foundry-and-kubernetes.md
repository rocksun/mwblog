
<!--
title: 云原生多集群用户界面，适用于Cloud Foundry和Kubernetes
cover: https://cdn.thenewstack.io/media/2024/11/2790ae20-andrew-_ibhdwv6pgi-unsplash-scaled.jpg
-->

将Stratos（一个多集群UI）添加到Backstage开发者门户框架的实践指南

> 译自 [Backstage Multicluster UI for Cloud Foundry and Kubernetes](https://thenewstack.io/backstage-multicluster-ui-for-cloud-foundry-and-kubernetes/)，作者 Sylvain Kalache。

开源项目且CNCF孵化项目[Backstage](https://backstage.io/)已成为许多公司平台工程工具包的核心部分。这是有充分理由的。该框架专为构建开发者门户而设计，通过其应用商店提供大量的插件目录，并易于创建您自己的插件。

在本文中，我将展示如何将[Stratos](https://stratos.app/)——一个支持Cloud Foundry、Kubernetes、EKS、AKS、GKE等的开源多集群UI——集成到Backstage中。虽然该项目已经存在7年了，但由于多云增长和[平台工程需要将基础设施的每个部分](https://thenewstack.io/the-pillars-of-platform-engineering-part-5-orchestration/)整合在一个屋檐下，它最近受到了广泛关注。

## Backstage自建插件

虽然Backstage社区已经拥有[超过200个插件](https://backstage.io/plugins)，但该工具的优势还在于它提供了一种简单的方法，可以通过您自己的插件来构建和集成任何基础设施或软件开发工具。虽然有很多Backstage插件，但它们可以分为两大类：前端插件在Backstage应用程序上显示UI，后端插件[管理服务器端操作](https://thenewstack.io/what-can-incident-teams-learn-from-crisis-management/)。您可以通过在Backstage应用程序文件夹中键入`yarn new`来查看Backstage提供的所有不同的插件模板。

## 创建我们的Backstage插件

首先，您需要安装Backstage应用程序（请按照[此处](https://backstage.io/docs/getting-started/)的安装说明进行操作）。使用`yarn start`和`yarn start-backend`命令启动您的应用程序前端和后端。接下来，您将通过在Backstage项目的根目录下键入以下命令来创建前端插件：

```bash
yarn new
```

系统将提示您输入插件ID。它可以是任何字符串。在我的例子中，我将它命名为`stratos`。

```
? Enter the ID of the plugin [required] stratos
Creating frontend plugin @internal/backstage-plugin-stratos
Checking Prerequisites: availability plugins/stratos ✔
creating temp dir ✔
Executing Template: templating .eslintrc.js.hbs ✔
[...]
🎉 Successfully created plugin
```

您可以通过调用`curl -I http://localhost:3000/stratos/`或将URL粘贴到浏览器中来检查您的插件是否运行良好。每个Backstage插件都被视为一个独立的Web应用程序，这使其非常强大，但也存在学习曲线。为简单起见，我将使用Backstage提供的现有示例模板来构建我的插件。如果您将其用于生产环境，则此处是[正确构建插件的文档](https://backstage.io/docs/plugins/plugin-development)。

我们将编辑现有的Stratos[组件文件以集成我们的iframe以嵌入](https://thenewstack.io/how-to-build-embed-components-with-astro-qwik-and-stackblitz/)Stratos界面。为此，我们将编辑文件`plugins/stratos/src/components/ExampleComponent/ExampleComponent.tsx`并在其中粘贴以下内容。

```tsx
import React from 'react';
import { Typography, Grid } from '@material-ui/core';
import { Header, Page, Content,} from '@backstage/core-components';
import { ExampleFetchComponent } from '../ExampleFetchComponent';

export const ExampleComponent = () => (
  <Page themeId="tool">
    <Header title="Backstage + Stratos = ❤️" />
    <Content>
      <iframe src="http://localhost:8080/" width="100%" height="100%" style={{ border: 0 }} />
    </Content>
  </Page>
);
```

我不会详细介绍配置文件，但需要注意的是，我们使用`src="http://localhost:8080/"`提供iframe服务，这会将Stratos界面显示到Backstage中。
我们与Backstage的工作完成了；现在，让我们开始使用Stratos。

## 部署Stratos

有三种方法可以部署Stratos：Cloud Foundry、Kubernetes或[Docker](https://stratos.app/docs/deploy/all-in-one)。我将使用Docker方式，您可以通过运行以下命令来启动Stratos：`docker run -p 5443:5443 splatform/stratos:stable`。

根据您部署和配置Stratos的方式，您可能能够直接将其提供到Backstage iframe中。在我们的例子中，Docker容器中的证书已过期，并且没有简单的[解决方法](https://thenewstack.io/your-authorization-system-is-broken-here-are-5-ways-to-fix-it/)；我们需要在Stratos前面放置一个代理。Backstage提供了一个内置的代理可以完成这项工作，但是根据您部署Stratos的方式，您可能无法获得有效的解决方案。我不会在本文中详细介绍，但在[这段视频中](https://youtu.be/VgbK4rceFSc?si=roojGEYRGkSL6zIB)，我演示了如何使用Backstage代理流量，并介绍了您可能面临的挑战。

我们将使用Nginx进行代理，以创建一个易于构建的解决方案。以下是我们Nginx配置所需的内容：

```nginx
server {
    listen 8080 default_server;
    listen [::]:8080 default_server;

    location / {
        proxy_pass https://localhost:5443/;
        proxy_set_header Host $host;
        proxy_hide_header X-Frame-Options;
    }

    location ~* \.(js|css|png|jpg|jpeg|svg|woff|woff2|ico)$ {
        proxy_pass https://localhost:5443;
        proxy_set_header Host $host;
        proxy_hide_header X-Frame-Options;
    }
}
```

此Nginx配置文件分为两个主要部分：第一部分用于服务[动态内容和静态](https://thenewstack.io/how-to-secure-web-applications-in-a-static-and-dynamic-world/)资源。如前所述，代理使我能够通过iframe提供Stratos服务；以下是一些要点：

1. `listen 8080 default_server;` — Stratos 通过HTTPS提供服务，并且当使用当前Docker镜像时，它没有有效的SSL证书，这对iframe来说是个问题。我使用Nginx通过HTTP提供流量来解决这个问题。
2. `proxy_hide_header X-Frame-Options;` — Stratos在其响应头中包含同源策略，阻止浏览器在iframe中显示页面。此Nginx指令删除包含该安全策略的头。

启动Nginx，刷新插件页面后，您应该会看到以下内容。

![](https://cdn.thenewstack.io/media/2024/10/3c97ddc7-screen-shot-2024-10-23-at-1.34.25-pm-1024x673.png)

将Stratos集成到Backstage中，可以提供多集群Cloud Foundry和Kubernetes环境的简化、集中视图，从而简化基础设施管理。Stratos被Comcast和TwentyFive等知名最终用户使用。虽然此设置旨在用于演示——而不是生产——但它突出了Backstage强大的插件生态系统如何为可扩展和协作的[平台工程](https://thenewstack.io/how-to-build-an-internal-developer-platform-like-a-product/)奠定基础。
