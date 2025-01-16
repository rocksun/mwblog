
<!--
title: 如何为低代码和无代码集成准备API产品
cover: https://cdn.thenewstack.io/media/2025/01/952a154a-jantine-doornbos-xt9tb6oa42o-unsplash-scaled.jpg
-->

API产品不再仅仅是开发者工具。它们是日益壮大的低代码和无代码解决方案生态系统中不可或缺的一部分。

> 译自 [How To Prepare API Products for Low-Code and No-Code Integrations](https://thenewstack.io/how-to-prepare-api-products-for-low-code-and-no-code-integrations/)，作者 Milos Dekic。

现在是2025年，我们正在见证公民开发者的空前兴起。生成式AI的最新进展使非开发人员能够快速轻松地创建复杂的流程和解决方案。Zapier、Make和UIPath等低代码和无代码平台已经成为企业的重要工具，因为它们能够让更多的人参与到[无需深入技术](https://thenewstack.io/a-software-developers-guide-to-technical-writing/)的[软件开发](https://thenewstack.io/a-software-developers-guide-to-technical-writing/)中。这对[API产品开发人员](https://thenewstack.io/bring-purpose-to-api-product-development-with-apiops-cycles/)来说既是挑战也是机遇：为传统开发人员设计强大的API，同时也要让越来越多的非技术用户能够访问这些API。

不幸的是，许多API无法满足低代码和无代码开发人员的需求。复杂的身份验证、繁琐的文件处理以及缺乏对自动化平台和市场集成的显式优化等问题，造成了重大的采用障碍。

本文通过一个真实的例子，探讨了为在低代码和无代码生态系统中蓬勃发展而准备API的一些关键考虑因素，特别关注文件处理API。通过解决这些差距，开发人员可以将他们的API定位为对越来越多的用户有吸引力的用户友好型解决方案。

## 我们在API产品中忽略了低代码/无代码的准备工作

我们最近将我们的DWS API产品与Zapier集成。在Nutrient公司，试用我们自己的技术至关重要，因为它能保持我们产品的高质量。这次集成是一段学习之旅，我们很快就被提醒，API开发人员倾向于专注于为以开发人员为中心的开发环境创建资源，并优化其产品以直接与代码集成。然而，低代码/无代码平台的工作方式不同，未针对这些环境优化的API可能会面临重大挑战。

对于处理文件的API来说，这些问题尤其突出，因为许多低代码/无代码平台需要URL，或者无法处理文件流。许多处理文件的API产品不会持久化它们。它们不提供文件存储这一事实是出于设计考虑，目的是最大限度地降低数据泄露风险并限制攻击面，以及简化合规性并提供更高的可扩展性。

例如，在无代码和低代码工作流自动化的世界中，事务性存储等问题很重要，而没有准备好集成会导致：

- 难以将API集成到工作流中的沮丧的[公民开发者](https://thenewstack.io/digital-workflows-low-code-and-the-rise-of-citizen-developers/)；
- 与Zapier和Make等流行平台的兼容性问题；
- 潜在用户无法采用API产品而导致的收入损失机会；
- 与为无缝集成而设计的API相比的竞争劣势。

在将我们的API产品与Zapier集成时，我们遇到了这些挑战。尽管在传统的开发人员环境中非常强大，但我们端点的设计方式给低代码工作流带来了障碍，突出了我们需要根据新的现实调整API设计实践的必要性。

## 为什么准备好低代码/无代码集成很重要

忽略API产品的低代码/无代码准备工作带来的后果不仅仅是用户沮丧。未能与这些平台对齐的API可能会失去重要的市场机会。低代码/无代码工具越来越受到希望降低开发开销并使非技术用户能够自动化流程的企业的青睐。无法无缝集成到这些生态系统的API：

- **限制其用户范围**: 许多用户仅依靠低代码平台访问API；
- **错过经常性收入**: 低代码集成通常会带来长期订阅；
- **落后于竞争对手**: 为低代码准备而设计的API会更快获得关注并提高市场知名度。

处理文件的API产品——许多行业的日常用例——尤其面临风险。如果没有优化的文件处理机制，此类API将难以满足低代码工具的事务性、安全性和用户友好性要求。

## 将我们的API产品与Zapier集成时我们学到了什么

为方便与低代码/无代码平台无缝集成，开发者应采用特定的设计原则和功能。以下是根据我们 DWS API 与 Zapier 集成的经验推断出的几种方法：

**1. 身份验证不仅仅是每次请求都传递 API 密钥**

API 产品往往依赖 API 密钥进行身份验证。这些主要是事务性 API，不需要文件存储和复杂的权限，因此不需要 OAuth 或 JWT。当开发者注册帐户时，他们会获得一个 API 密钥，他们可以在请求头或有效负载中传递此密钥。

虽然这对于低代码和无代码集成看起来足够简单，但我们需要思考[超越代码中身份验证的使用方式，并转向](https://thenewstack.io/ai-code-assistants-are-moving-beyond-auto-complete-heres-whats-next/)我们的产品如何在工作流自动化平台上的“连接器”应用程序中使用。以[Zapier 的连接标签](https://docs.zapier.com/platform/build/connection-label)为例：Zapier 用户可以为单个应用程序使用多个帐户。连接标签提供了一种超越简单枚举来区分帐户的方法。很简单：您的 API 产品应该能够根据用于身份验证的 API 密钥来识别自身。

例如，为了实现 DWS API 与 Zapier 的身份验证，我们没有专门用于验证或识别连接的端点，我们必须首先从无代码“表单模式”切换到低代码“代码模式”，因为我们唯一可以实现它的方法是对 API 调用进行“试运行”，否则会消耗 API 积分，如果 API 密钥无效则会失败。

我们最终得到类似这样的结果：

```js
const formData = {
    instructions: JSON.stringify({
      parts: [
        {
          html: 'index.html',
        },
      ],
    }),
    'index.html': {
      content: "<!DOCTYPE html><html><head><title>Hello World</title></head><body><h1>Hello World!</h1><p>This is a PDF now.</p></body></html>",
      filename: 'index.html',
      contentType: 'text/html', 
    },
  };
 
const options = {
  url: 'https://api.nutrient.io/analyze_build',
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${bundle.authData.api_key}`
  },
  body: formData
}
 
return z.request(options)
  .then((response) => {
    const results = response.json;
    return results;
  });
```

我们对 HTML 到 PDF 的转换进行了试运行，成功的响应意味着 API 密钥有效。不幸的是，我们无法识别连接，当我们想在他们的市场上发布我们的 Zapier 连接器时，这带来了挑战。

为了使您的 API 能够自我识别，您可以实现一个类似 **/account/info** 的端点，该端点将以 JSON 格式返回有关帐户的信息。像 Zapier 这样的平台可以从该 JSON 中推断连接标识符。有两种设计方法需要考虑：

1. **单个 API 密钥**: 这是默认设置，也可能是您的 API 产品最初使用的设置。如果您的用户只有一个密钥，您可以使用用户的电子邮件地址或其他联系信息作为标识符，并让您的端点返回类似“John Appleseed <john@appleseed.com>”的内容。
2. **多个 API 密钥**: 您可以允许您的用户生成、命名和管理多个 API 密钥。根据您产品的复杂性，这些密钥也可以具有特定的范围。这种方法有很多好处，因为您的用户可以监控和管理每个 API 密钥的成本，并在其团队内分配功能。在与低代码/无代码平台集成的上下文中，用户可以将其密钥命名为“Zapier 集成”，这将是您的 API 端点返回的标识符。

无论您采用哪种方法，您的 API 产品都应该准备好用于低代码或无代码平台。这意味着您应该有一个旨在验证和识别 API 密钥的端点。

**2. 文件处理应具有选项**

如果您的 API 产品处理文件，则与无代码/低代码平台的集成可能会变得更具挑战性，因为他们的用户不一定考虑文件是否以及在哪里持久化，也不考虑它们如何在不同的应用程序之间交换。但您必须考虑。

在设计处理文件的 API 产品时，使用 API 端点接受和输出文件的方法数量有限。RESTful API 最常用的一种方法是使用多部分表单数据。它很方便，开发人员可以同时发送元数据和文件。但是，多部分表单请求不一定受开箱即用的无代码工具支持，低代码方法也可能具有挑战性。

例如，为了使用 DWS API 的 **/sign** 端点与 Zapier 集成，我们不得不再次从“表单模式”切换到“代码模式”，因为我们的 API 流式传输生成的 文件，所以我们必须[对其进行填充](https://docs.zapier.com/platform/build/hydration-cli)才能在 Zaps 中使用。然后，我们必须弄清楚如何使用他们有限的平台 CLI 来实现多部分表单请求。

我们最终学会了如何包含必要的依赖项：

```javascript
const MultipartFormData = z.require('form-data');
```

这帮助我们准备了请求签署 PDF 的表单数据：

```javascript
// previously defined: inputPdfBuffer, updatedFileName, bundle
 
const formData = new MultipartFormData();
 
formData.append("data", JSON.stringify({
  signatureType: "cades",
  cadesLevel: "b-lt",
}));
 
formData.append("file", inputPdfBuffer, {
  filename: updatedFileName,
  contentType: 'application/pdf',
});
 
const formDataHeaders = formData.getHeaders();
const headers = {
  Authorization: `Bearer ${bundle.authData.api_key}`,
  'Content-Type': formDataHeaders['content-type'],
};
```

这花费了时间，因为它需要理解他们的“z”对象。大型语言模型难以处理这个问题，坚持使用不受支持的 `await` 并错误地推断可以导入哪些依赖项以及如何导入。

我们的 API 产品尚未准备好面向无代码开发者，低代码方法带来的挑战主要是因为 Zapier 的平台 CLI 是沙盒化的。

文件处理 API 可以使用 URL 引用而不是文件流和多部分表单数据。当然，这需要文件存储，但是许多在 Zapier 和其他市场上提供连接器的应用程序都会从其存储中公开文件，并提供下载永久链接以方便集成。

以我们的 DWS API 为例，**/build** 端点可以接受文件 URL 而不是流作为 `FilePart` 参数。尽管如此，为了使其对无代码/低代码友好，我们需要超越多部分表单请求，并创建一个可以接受有效负载中文件 URL 的端点，而无需增加复杂性。这使得无代码集成更容易实现，而现在这并非易事。

输出方面的情况非常相似。如果 API 产品提供文件存储，则当有文件输出时，API 端点可以返回永久链接而不是流式传输文件。这带来了自身的业务影响，因为引入文件存储往往会使产品变得复杂。至少，为欧盟客户服务的企业会对用户文件存储的地理区域有所表示。

**3. API 端点应独立且可预测**

低代码/无代码平台通常基于用户将离散的任务或“操作”链接在一起以创建工作流的模型。例如，在 Zapier 中，用户可以定义一个触发器（“上传文件时”）和一个操作（“转换文件”）。它也捕捉了无代码和低代码开发者的思维方式。具有明确定义的操作且直接映射到此工作流模型的 API 将使用户更容易地将其集成到此类平台中，而无需自定义编码或复杂的配置。

作为一名工程师，我喜欢 DWS API 团队对 **/build** 端点的处理方式。它非常强大，您可以发送多个文档并捆绑不同的操作，按顺序运行它们。例如，您可以使用单个 API 调用来接受各种格式的一堆文件（例如，几个 MS Office 文件、几个图像和一个 PDF），将它们全部转换为 PDF，将它们合并到单个 PDF 文件中，然后压缩生成的 文件。太棒了，对吧？但是，对于只想将单个 MS Office 文件转换为 PDF 的开发者来说，这往往过于复杂。为了使我们的 API 产品更适合无代码和低代码集成，更好的方法是围绕特定操作创建端点，例如 **/convert** 和 **/compress**。

离散操作允许更大的 API 调用灵活性，这对于像 Zapier 这样链接“操作”的平台尤其重要。它们也更直观，使潜在错误更容易隔离和调试。最终，围绕可预测的、基于任务的操作设计的 API 促进了更好的可用性。我们的目标是设计在技术上强大，同时又高度易于访问且足够直观的 API，以满足不断增长的公民开发者和非技术用户的需求。

**4. 文档应适合低代码和无代码开发者**

如果您有 API 产品，则应使用它来构建与流行的工作流自动化无代码和低代码平台的集成。这将是一个学习和改进的绝佳机会。在 Nutrient 进行此操作后发现，我们的 API 产品并非完全能够应对这一挑战。我们没有针对低代码集成的具体指南，没有关于使用无代码平台设置我们产品的说明，也没有用户可以直接使用的预构建操作或工作流，而无需学习使用我们的 API 端点进行编码。

另一个建议是继续试用你的API产品，特别是将其与无代码平台集成。这将使你能够定期测试API与这些平台的兼容性，主动解决问题，并持续改进你的文档。

## 充分发挥API产品的潜力

API产品不再仅仅是开发者工具。它们是日益壮大的低代码和无代码解决方案生态系统不可或缺的一部分。除此之外，“开发者”这个术语也随着每一个问世的LLM代码生成产品的出现而不断发展。通过采用良好的实践来验证和识别身份验证，提供文件处理选项和平台友好的设计，并确保文档是最新的，你可以确保你的API能够满足这个不断变化的市场的需求。

对于API产品而言，低代码/无代码的准备工作不仅仅是为了避免挫折——它还关乎解锁新的收入来源，扩大用户群，并在快速变化的API领域保持竞争力。我们已经在改进[DWS API](https://www.nutrient.io/api/)，你也应该这样做。现在是行动的时候了。
