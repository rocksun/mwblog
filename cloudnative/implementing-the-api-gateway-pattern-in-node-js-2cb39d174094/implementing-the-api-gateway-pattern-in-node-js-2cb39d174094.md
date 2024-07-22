
<!--
title: 在基于Node.js的微服务应用程序中实现API网关模式
cover: ./cover.png
-->

使用 Node.js 在 5 分钟内构建自己的 API 网关

> 译自 [Implementing the API Gateway Pattern in a Microservices Based Application with Node.js](https://blog.bitsrc.io/implementing-the-api-gateway-pattern-in-node-js-2cb39d174094)，作者 Ruvani Jayaweera。

微服务提供增强的可扩展性、灵活性和敏捷性。

随着组织采用基于微服务的应用程序，管理这些服务的多种和分布式性质变得越来越具有挑战性。

因此，API 网关模式成为一项关键解决方案，它充当微服务生态系统中客户端交互的中心入口点。

这种模式充当流量协调器，简化客户端体验并简化微服务通信的复杂性。让我们进一步探讨这种模式。

## 了解 API 网关模式

API 网关模式是微服务架构中的一个关键组件，充当客户端交互的集中式入口点。这种模式通过智能地将请求路由到相应的微服务并聚合响应来协调流量，从而提供无缝的客户端体验。

除了简化通信之外，API 网关还实施安全措施，包括身份验证和授权。它还处理路由、协议转换、负载均衡和缓存，优化性能和可扩展性。

这种全面的理解突出了 API 网关在简化微服务通信和提高整体系统效率方面的关键作用。

## API 网关模式如何工作？

微服务 API 网关模式充当微服务架构中客户端交互的中心枢纽。

客户端仅与 API 网关通信，API 网关根据预定义规则智能地将请求路由到相应的微服务。

API 网关协调流量流，聚合来自多个微服务的响应，并处理协议转换以实现标准化通信。它实施安全措施，包括身份验证和授权，并包含负载均衡、缓存和日志记录等功能。

> API 网关简化了客户端实现，增强了安全性，并优化了基于微服务的系统中的通信。

## API 网关模式有哪些优势？

使用 API 网关模式为应用程序提供了许多好处。它的一些主要优势包括：

- **简化的客户端交互**：客户端与单个入口点（API 网关）交互，简化了客户端实现。
- **智能路由**：API 网关根据预定义规则将请求智能地路由到相应的微服务，减轻了客户端浏览微服务网络复杂性的负担。
- **流量协调器**：API 网关充当流量协调器，有效地引导传入请求，确保客户端和微服务之间的无缝通信。
- **响应聚合**：API 网关可以将来自多个微服务的响应聚合到一个连贯且统一的响应中。这减少了客户端发出的请求数量，并提高了整体系统性能。
- **协议转换**：它处理协议转换，允许客户端使用标准化通信协议，同时在内部将这些请求转换为特定于微服务的协议。
- **安全集中化**：在集中位置实施安全措施，包括身份验证和授权。这确保了整个微服务生态系统中一致且安全的方法。
- **负载均衡**：包含负载均衡，以将传入请求均匀地分布在微服务的多个实例之间。这促进了最佳资源利用，并防止单个服务成为性能瓶颈。
- **缓存机制**：实施缓存机制以存储和检索经常请求的数据。缓存减少了微服务的负载，提高了响应时间，并优化了资源使用。
- **日志记录和监控**：集中日志记录和监控功能，提供对整个微服务架构的运行状况、性能和使用模式的洞察。

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*at9K8lQiSl-JihBb.png)

## 如何在 Node.js 中实现 API 网关模式？

现在我们已经对 API 网关模式是什么以及它是如何工作的有了基本的了解，让我们看一下如何在 Node.js 中实现一个。

重要的是要了解，没有“一种”方法可以做到这一点。实际上，有几种方法可以实现 API 网关模式，每种方法都适合不同的环境和用例。

因此，让我们看一下两种最常见的方法。

## 方法 01：基于容器的实现（使用 Kubernetes 或 Docker）

让我们看看如何在 Docker 环境中实现和部署 API 网关模式。

首先，我为我的应用程序创建了以下文件夹和文件结构。

**步骤 1 - 创建 service-a 微服务**

```javascript
const express = require('express');

const app = express();
const port = 3001;

app.get('/api/data', (req, res) => {
console.log(Received request to /api/data: ${req.method} ${req.url} );
res.status(200).send('Response from Service A');
});

app.listen(port, () => {
console.log(Service A listening on port ${port} );
});
```

这仅仅定义了一个简单的 Express API，它一个 GET 方法来返回一些示例数据。

**步骤 2 - 创建 service-a Dockerfile**


```dockerfile
FROM node:14
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3001
CMD ["node", "service-a.js"]
```

这将创建一个 Dockerfile，该文件负责创建步骤 01 中定义的微服务的包可执行文件。它定义了如何启动环境并启动服务器的指令。


**步骤 3 - 创建 service-b 微服务**

```javascript
const express = require('express');
const app = express();
const port = 3002;
app.get('/api/info', (req, res) => {
  console.log(`Received request to /api/info: ${req.method} ${req.url}`);
  res.status(200).send('Response from Service B');
});
app.listen(port, () => {
  console.log(`Service B listening on port ${port}`);
});
```

这声明了第二个 API，它将通过一个简单的 GET 端点向客户端返回一些信息。

**步骤 4 - 创建 service-b Dockerfile**

```dockerfile
FROM node:14
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3002
CMD ["node", "service-b.js"]
```

这将再次创建一个指令文件，说明如何启动此微服务。 

**步骤 5 - 创建 API 网关**


```javascript
const express = require('express');
const httpProxy = require('http-proxy');
const app = express();
const proxy = httpProxy.createProxyServer();
const serviceAUrl = 'http://service-A:3001';
const serviceBUrl = 'http://service-B:3002';
app.use('/api/data', (req, res) => {
  console.log(`Incoming request to /api/data: ${req.method} ${req.url}`);
  proxy.web(req, res, { target: serviceAUrl }, (err) => {
    console.error(`Error forwarding request to service A: ${err.message}`);
    res.status(500).send('Internal Server Error');
  });
});
app.use('/api/info', (req, res) => {
  console.log(`Incoming request to /api/info: ${req.method} ${req.url}`);
  proxy.web(req, res, { target: serviceBUrl }, (err) => {
    console.error(`Error forwarding request to service B: ${err.message}`);
    res.status(500).send('Internal Server Error');
  });
});
// Add this middleware to log the request received by the proxy
proxy.on('proxyReq', function (proxyReq, req, res, options) {
  console.log(`Received request to ${options.target.href}: ${req.method} ${req.url}`);
});
const port = 3000;
app.listen(port, () => {
  console.log(`API Gateway listening on port ${port}`);
});
```

现在，这个是实际的 API 网关实现。它使用 http-proxy 创建一个代理服务器。

此服务器负责根据请求路径将 API 网关的请求转发到实际的微服务（serviceA 和 serviceB）。接下来，在网关中声明路由，并在调用端点时将其代理到内部微服务。

**步骤 6 - 配置 Docker Compose**

```yaml
version: '3'
services:
  service-a:
    build:
      context: ./service-A
      dockerfile: Dockerfile
    ports:
      - 3001:3001
  service-b:
    build:
      context: ./service-B # Correct the path if necessary
      dockerfile: Dockerfile
    ports:
      - 3002:3002
  api-gateway:
    build:
      context: ./api-gateway
      dockerfile: Dockerfile
    ports:
      - 3000:3000
    depends_on:
      - service-a
      - service-b
```

接下来，你需要创建一个 Docker-Compose 文件，负责管理这三个 docker 容器。这有助于通过一个命令启动、管理和终止这三个容器，并将其作为一个单一实体进行处理。

**步骤 7 - 构建并运行应用程序。**

最后，运行 docker-compose up --build 命令以构建两个服务和 API 网关的镜像，并以容器形式启动它们。

API 网关将在 localhost:3000 上提供服务。

当需要访问服务 A 或服务 B 时，可以改为调用 API 网关。API 网关会将请求正确路由到相关服务。可以使用 postman 或浏览器调用 HTTP 方法来测试此操作。这样可以在控制台中看到类似于以下内容的输出。

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*hzGEsvWGUEfZfiJC.png)

你可以在这里找到 GitHub 仓库，了解其完整实现。

## 方法 02：服务网格实现

还可以将服务网格与 Node.js 一起用于实现 API 网关。为此，可以使用 Express.js 等工具来构建 API 网关服务，并使用 Istio 作为服务网格。

为此，需要具备以下先决条件。

- Node.js 
- Docker已安装 
- Kubernetes 集群并安装了 Istio

**步骤 1：创建 Express.js API 网关**

创建一个新的目录作为 API 网关项目并导航至该目录。

```bash
mkdir api-gateway
cd api-gateway
```

初始化新的 Node.js 项目。

```bash
npm init -y
```

安装需要的依赖项。

```bash
npm install express axios
```

为 API Gateway 创建一个 index.js 文件。

```javascript
const express = require('express');
const axios = require('axios');
const app = express();
```
```javascript
const port = 3000;
app.get('/service1', async (req, res) => {
  try {
    const response = await axios.get('http://service1.default.svc.cluster.local');
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});
app.get('/service2', async (req, res) => {
  try {
    const response = await axios.get('http://service2.default.svc.cluster.local');
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: 'Internal Server Error' });
  }
});
app.listen(port, () => {
  console.log(`API Gateway listening at http://localhost:${port}`);
});
```

**步骤 2：部署 Express.js API 网关**

通过在项目根目录中创建 Dockerfile 来将 Node.js 应用程序容器化。

```dockerfile
FROM node:14
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "index.js"]
```

构建并推送 Docker 镜像。

```bash
docker build -t your-registry/api-gateway:latest .
docker push your-registry/api-gateway:latest
```

为 API 网关创建 Kubernetes 部署（api-gateway-deployment.yaml）。

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-gateway
spec:
  replicas: 1
  selector:
    matchLabels:
      app: api-gateway
  template:
    metadata:
      labels:
        app: api-gateway
    spec:
      containers:
      - name: api-gateway
        image: your-registry/api-gateway:latest
        ports:
        - containerPort: 3000
```

应用部署。

```bash
kubectl apply -f api-gateway-deployment.yaml
```

**步骤 3：为 API 网关配置 Istio**

创建 Istio 网关（gateway.yaml）。

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: api-gateway
spec:
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "your-api-gateway-host"
```

创建 Istio 虚拟服务（virtualservice.yaml）。

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: api-gateway
spec:
  hosts:
  - "your-api-gateway-host"
  gateways:
  - api-gateway
  http:
  - route:
    - destination:
        host: api-gateway.default.svc.cluster.local
        port:
          number: 3000
```

应用 Istio 网关和虚拟服务。

```bash
kubectl apply -f gateway.yaml
kubectl apply -f virtualservice.yaml
```

**步骤 4：测试 API 网关**

使用指定的宿主访问您的 API 网关。

```bash
curl http://your-api-gateway-host/service1
curl http://your-api-gateway-host/service2
```

此示例演示了使用 Express.js 和 Istio 的 API 网关的基本设置。根据您的具体需求和服务网格偏好调整代码和配置。此外，请考虑根据需要增强安全性、添加更多功能和实现服务发现。

您可以在 [此处](https://github.com/ruvani/api-gateway-pattern-service-mesh) 找到 GitHub 存储库。

## 结论

总之，在现代软件架构中，采用 API 网关模式来实现微服务，成为提高可扩展性、灵活性以及整体效率的关键策略。通过将微服务的管理集中到一个专用网关，组织可以简化通信、实施安全措施并简化不同服务的集成。

这种模式不仅优化了开发和维护流程，而且还促进了更敏捷和响应更快的系统。

感谢您的阅读！
