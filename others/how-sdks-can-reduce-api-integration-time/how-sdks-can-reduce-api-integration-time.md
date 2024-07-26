
<!--
title: SDK如何缩短API集成时间
cover: https://cdn.thenewstack.io/media/2024/07/8d89af6f-platformteamswinoverdevsquickwins.jpg
-->

免费 SDK 中心提供针对各种流行 API 的软件开发工具包，使将服务集成到应用程序中变得更加轻松快捷。

> 译自 [How SDKs Can Reduce API Integration Time](https://thenewstack.io/how-sdks-can-reduce-api-integration-time/)，作者 Deirdre Corley; Adam Kane。

API 无处不在。它们是公司向世界展示其产品和服务的关键方式，72% 的组织认为 API 采用是其业务战略和未来增长的 [关键组成部分](https://www.axway.com/en/company/media/2022/press-release-axway-study-shows-apis-can-be-major-revenue-driver-organizations)。

随着 [API 集成](https://thenewstack.io/api-management/) 成为业务运营的核心，最大限度地减少 API 集成所需的时间对于开发人员至关重要。使用软件开发工具包 (SDK) 是 [缩短 API 集成时间](https://thenewstack.io/how-sdks-benefit-api-management/) 的关键因素。

## 缩短 API 集成时间以提高收入

无论 API 集成是推动新产品发布、建立新的合作伙伴关系还是连接内部服务，最大限度地减少开发人员在这些集成上花费的时间都可以显着提高收入增长。以下是我们听到的关于缩短 API 集成时间如何帮助提高收入的主要驱动因素：

### 加速销售周期

对于许多 B2B 公司来说，在他们和客户的产品之间建立 API 集成是销售的必要条件。缩短 API 集成时间通过促进更快的集成和合同签署来加速销售周期。这使企业能够更快地抓住销售机会，推动更多销售并增加收入。

### 加快上市时间

快速集成可以更快地进行产品开发，使企业能够在竞争对手之前抢占市场份额。率先推出新功能或产品可以吸引更多客户，并在竞争对手之前抢占市场份额，直接促进收入增长。

### 提高开发人员效率

减少复杂集成的时间使开发人员能够专注于核心功能，从而增强产品并吸引更多客户。根据 [麦肯锡的一份报告](https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/choosing-to-grow-the-leaders-blueprint)，缩短开发周期并投资于工程扩展机会的企业是那些在收入增长方面获得回报的企业。更高的生产力意味着更多功能和改进，从而带来更好的产品，可以吸引和留住更多客户。

### 改善客户体验

快速集成 API 并推出新功能可以增强客户体验。更可靠、功能更丰富的产品可以提高客户满意度、留存率和推荐率，所有这些都会促进收入增长。

## 实现使用 SDK 的优势

鉴于 API 在当今商业环境中的关键作用，公司正在为开发人员提供各种工具来帮助缩短 API 学习曲线。这些工具包括公开 API 规范文档、将文档与最新的 API 更改保持同步、提供 API 端点的测试和验证工具以及与开发人员社区互动以获取 API 反馈。

但是，减少整体 API 集成时间的最有效工具是使用 SDK，它允许开发人员使用预构建的库来简化 API 调用和数据处理。SDK 可以通过简化集成并减少所需的自定义开发量，将软件开发时间缩短多达 50%。

使用 SDK 缩短 API 集成时间的一些主要优势包括：

### 更快的开发周期

假设您正在将支付网关集成到您的电子商务应用程序中。如果没有 SDK，您需要手动处理 API 集成的各个方面，从身份验证到错误处理。这可能很耗时且容易出错。SDK 提供现成的功能和工具，可以抽象化 API 复杂性，使您能够专注于构建功能，而不是处理低级 API 细节。

### 语言原生

SDK 是为语言原生而设计的，提供符合语言习惯的接口，可以无缝集成到您现有的代码库中。这最大限度地减少了学习曲线，增强了直观的集成并扩大了您的开发人员范围。此外，SDK 通常包括 IntelliSense 支持和类型安全，通过提供智能代码建议和防止请求中的错误来提高代码准确性和生产力。

如果没有 SDK，您必须手动构建请求并根据 API 文档进行验证。使用 SDK，所有初始设置、猜测和手动验证都将消除，因为类型和身份验证模式包含在库中。

**示例：**

```js
//Without SDK

async () => {
  const url = 'https://api.petstore.com/v1/pets';

  const params = new URLSearchParams({
    yourQueryParameter: 'your-query-parameter',
  }).toString();

  const response = await fetch(`${url}${params ? '?' : ''}${params}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer YOUR_API_TOKEN`,
      'your-header-parameter': 'your-header-parameter',
    },
    body: JSON.stringify({
      id: 10,
      name: 'doggie',
      category: {
        id: 1,
        name: 'dogs',
      },
      photoUrls: ['photoUrls'],
      tags: [
        {
          id: 8,
          name: 'dog-tag',
        },
      ],
      status: status,
    }),
  });

  const data = await response.json();

  console.log(data);
};

//With liblab SDK

import { Category, Pet, Petstore, Tag, Status } from 'petstore';

(async () => {
  const petstore = new Petstore({ token: 'YOUR_API_TOKEN' });

  const category: Category = {
    id: 1,
    name: 'dogs',
  };

  const tag: Tag = {
    id: 8,
    name: 'dog-tag',
  };

  const status = Status.AVAILABLE;

  const pet: Pet = {
    id: 10,
    name: 'doggie',
    category: category,
    photoUrls: ['photoUrls'],
    tags: [tag],
    status: status,
  };

  const { data } = await petstore.pet.addPet(pet, {
    yourQueryParameter: 'your-query-parameter',
    yourHeaderParameter: 'your-header-parameter',
  });

  console.log(data);
})();
```

### 综合文档

高质量的 SDK 将包含广泛的文档和代码示例，使开发人员能够快速开始使用其母语的 API 调用。

### 增强安全性

API 通常需要安全处理敏感数据，SDK 默认情况下确保 [安全最佳实践](https://roadmap.sh/best-practices/api-security)。它们帮助您的集成符合最新标准，并降低安全漏洞的风险。如果没有 SDK，您需要为每个请求手动实现身份验证模式。但是，使用 SDK，您可以进行一次身份验证，SDK 将安全地将这些凭据重新用于每个后续请求。

**示例：**

```java
// Without SDK
String username = "YOUR_USERNAME";
String password = "YOUR_PASSWORD";

String basicToken = Base64.getEncoder().encodeToString((username + ":" + password).getBytes());

int id = 1;

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://api.petstore.com/v1/pet/" + id))
    .header("Accept", "application/json")
    .header("Authorization", "Basic " + basicToken)
    .method("GET", HttpRequest.BodyPublishers.noBody())
    .build();
    
HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
System.out.println(response.body());


// With liblab SDK
PetstoreConfig config = PetstoreConfig.builder()
  .basicAuthConfig(
    BasicAuthConfig.builder()
      .username("YOUR_USERNAME")
      .password("YOUR_PASSWORD")
      .build()
  )
  .build();
Petstore petstore = new Petstore(config);

Pet response = petstore.petService.getPetById(1);
System.out.println(response);
```

### 提高代码质量

一致性在软件开发中至关重要。当不同的团队成员以不同的方式实现 API 调用时，会导致代码库碎片化，难以维护。SDK 推广统一的方法，从而产生更干净、[更易于维护的代码](https://thenewstack.io/quick-tips-to-make-your-sdk-more-maintainable-in-typescript)。

## 使用免费 SDK 简化集成

SDK 是简化 API 集成、提高生产力和确保健壮、安全实现的宝贵工具。通过利用 SDK，开发人员可以专注于他们最擅长的工作——构建出色的应用程序。

为了支持开发人员利用 SDK 的优势，[liblab](https://liblab.com/) 创建了 [liblab hub](https://hub.liblab.com/)。liblab hub 是一个平台，提供针对各种流行 API 的免费、易于使用的 SDK，使将这些服务集成到您的应用程序中比以往更容易。

无论您是使用体育、AI、DevTools 还是客户关系管理 (CRM) 应用程序，liblab hub 都提供高质量的 SDK，以减少您行业中流行 API 的集成时间。探索 [liblab hub](https://hub.liblab.com/) 的免费 SDK 集合，并了解 SDK 如何减少您的 API 集成时间并提高收入。

*Guilherme Bassa 也为本文做出了贡献。*