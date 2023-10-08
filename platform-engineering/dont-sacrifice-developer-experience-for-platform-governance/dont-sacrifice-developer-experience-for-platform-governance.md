<!-- 

# 不要以平台治理牺牲开发者体验
https://cdn.thenewstack.io/media/2023/10/79f0f01f-developers-1024x576.jpg
 -->

译自 [Don’t Sacrifice Developer Experience for Platform Governance](https://thenewstack.io/dont-sacrifice-developer-experience-for-platform-governance/) 。

我们正在创建新的基础设施即代码方法，以协调运维团队和开发者的基础设施即代码工具和工作流程。

基础设施即代码(IaC)工具，如 Terraform 和 [Pulumi](https://www.pulumi.com/?utm_content=inline-mention)，无疑改变了我们管理云基础设施的方式。虽然这些工具非常有价值，但总有可能进一步增强和优化运维团队和开发者的工作流程。我来自于正在创造新的来自代码的基础设施(IfC)方法的团队之一。我们与 Nitric 和 IfC 的目标不是取代这些工具，而是与它们协调一致。

我们正在开发功能来简化整个部署过程，直接从应用程序代码本身推断出复杂的基础设施代码。我们没有重写 IaC 工具链，而是将其无缝集成到我们的流程中。这确保运维团队可以继续使用他们的首选 IaC 工具，而开发者可以从更直观的界面中受益。

## IaC 开发者体验需要重新设计

当我们谈及 IaC 与开发者体验(DX)之间的脱节时，是指许多开发者从应用开发转向基础设施供应和管理时感受到的断层。传统的 IaC 工具虽然强大，但学习曲线往往很陡峭。它们要求开发者以云资源、配置和依赖的方式思考，这与他们的核心应用逻辑有很大差异。

这很容易让人陷入每个特定云提供商的细节难题中。无论是 AWS 的身份和访问管理(IAM)角色的复杂性，GCP 的网络规则还是 Azure 的存储配置，魔鬼总是藏在细节中。这种复杂性使我们的团队无法专注于提供核心业务价值。

## 极大提升开发者体验的方法

让我们来探讨一下我们是如何通过基础设施即代码(IaC)模块制作一个平台工程工具的，它可以直接从代码中自动生成和实现资源规范。这里有一段代码，让用户可以从存储桶中获取下载 URL：

```typescript
import { api， bucket } from "@nitric/sdk";

const photoApi = api('photos');
const photos = bucket('myPhotos').for('reading');

photoApi.get("/photo/:path"， async (ctx) => {
  const { path } = ctx.req.params;
  ctx.res.body = await photos.file(path).getDownloadUrl();
});
```

[Nitric CLI](https://nitric.io/docs) 检查这段代码，自动生成一个详细的规范，其中包含资源和全局属性的列表。这个列表包括 API、存储桶和执行单元等资源，以及在云端配置它们所需的必要信息。

![](https://cdn.thenewstack.io/media/2023/10/47f8610f-image2.jpg)

该资源规范清楚地定义了应用程序的部署和运行需求，这使得我们可以生成与项目一同存在的资源图和文档。

更重要的是，它也帮助解决基础设施漂移的问题。每当我们变更应用程序代码时，无论是在部署还是本地运行时，资源规范都会自动更新，以添加/删除/修改资源，使其与应用程序的需求保持一致。

那么，我们已经自动生成了一个资源规范;下一个逻辑问题是“我们如何将这个规范转换成已部署的资源?”

## 结合基础设施即代码

这里，与 Pulumi 和 Terraform 等基础设施即代码工具的集成至关重要。它们充当完成预配请求的动力来源。我们的目标是消除每个项目团队需要与项目一起维护基础设施即代码代码版本的需求。相反，Nitric 框架会自动实现资源规范。

Nitric 的核心在于它的提供商系统。这些云提供商充当插件，分为两大类:

1. **部署提供商**：解释资源规范并将其转换为具体的云资源。例如设置 API 网关或存储桶。
2. **运行时提供商**：将抽象的 SDK 调用转换为特定的云 API 请求。例如发布主题或读/写存储桶。

### 部署提供商

使用 Pulumi 部署代码设置 S3 存储桶的代码可能如下所示。代码遍历资源规范，收集建立存储桶资源所需的必要细节。

```go
for _， res := range request.Spec.Resources {
  switch b := res.Config.(type) {
  case *deploy.Resource_Bucket:
    s3Bucket， err := s3.NewBucket(ctx， b.Bucket， &s3.BucketArgs{
      Tags: pulumi.StringMap{
        "x-nitric-project":    pulumi.String(ctx.Project())，
        "x-nitric-stack":      pulumi.String(ctx.Stack())，
        "x-nitric-name":       pulumi.String(b.Bucket)，
      }
    })
    if err != nil {
      return nil， errors.WithMessage(err， "s3 bucket "+name)
    }
  }
}
```

主要优势在于部署变得更加声明式和可重现。此外，它还鼓励模块和模板的重用，加快和标准化部署。这种模块化方法本质上具有未来适应性，允许在资源配置、预配工具选择甚至未来的云目标方面提供灵活性。

### 运行时 Provider

除了部署之外，Nitric 确保与云资源的运行时交互被抽象化。SDK 映射到适当的云 API。例如:

```typescript
const images = bucket("images").for("writing");
bucket.file('cat.png').write(data); 
```

write 命令映射到一个提供商实现，它按如下方式完成写请求:

```go
// Write - 将对象写入存储桶
func (s *S3StorageService) Write(ctx context.Context， bucket string， key string， object []byte) error {
	newErr := errors.ErrorsWithScope(
		"S3StorageService.Write"，
		map[string]interface{}{
			"bucket":     bucket，
			"key":        key，
			"object.len": len(object)，
		}，
	)

	if b， err := s.getBucketName(ctx， bucket); err == nil {
		contentType := http.DetectContentType(object)

		if _， err := s.client.PutObject(ctx， &s3.PutObjectInput{
			Bucket:      b，
			Body:        bytes.NewReader(object)，
			ContentType: &contentType，
			Key:         aws.String(key)，
		}); err != nil {
			return newErr(
				codes.Internal，
				"unable to put object"，
				err，
			)
		}
	} else {
		return newErr(
			codes.NotFound，
			"unable to locate bucket"，
			err，
		)
	}

	return nil
}
```

注意：Nitric 框架是开源的，提供商用 Go 语言编写，使用为 AWS、GCP 和 Azure 打包的 Pulumi 自动化引擎，遵循最佳实践。使用 gRPC 向提供商实现发出请求，允许使用您喜欢的任何语言编写提供商。在我们 CTO Tim Holm 写的这篇博文中可以了解更多关于 gRPC 及我们如何使用它的信息。

## 搭桥铺路，拆墙联通

Nitric 根据开发者编写的代码自动生成详细的资源规范。这个规范充当导管，使运维团队可以使用他们偏好的基础设施即代码工具来提供应用程序确切需要的资源。这是代码、规范和基础设施之间的协作互动，确保所有团队保持一致。

对运维团队来说，这种集成意味着在不需要深入了解应用程序细节的情况下进行监督和治理，同时使用他们喜欢的基础设施即代码工具不会影响规模和性能。

对开发人员来说，这意味着简化的部署流程，他们只需定义自己的需求，Nitric 与基础设施即代码工具一起使其成为现实。

Nitric 社区正在蓬勃发展，我们非常乐意与您取得联系。有多种方式可以表示您的支持。在我们的 [Discord](https://discord.gg/Webemece5C) 渠道上可以了解更多关于 [Nitric](https://nitric.io/) 的信息，并参与积极讨论。在 [GitHub 上给我们点赞](https://github.com/nitrictech/nitric)可以表示您对我们的使命的热情支持，加入我们一起重塑平台工程。