
<!--
title: OpenTofu可能向我们展示了错误的fork方式
cover: ./cover.png
-->

不同意许可证？分叉项目，但不要直接拿走代码并声称它一直是公开可用的。比较 HashiCorp 代码和许可证与 OpenTofu 的版本。

> 译自 [OpenTofu may be showing us the wrong way to fork](https://www.infoworld.com/article/3714980/opentofu-may-be-showing-us-the-wrong-way-to-fork.html)，作者 Matt Asay。

**更新**：自本文发表以来，HashiCorp 于 2024 年 4 月 3 日向 OpenTofu 发送了一封停止侵权函，更详细地表达了本文中提出的担忧。2024 年 4 月 11 日，OpenTofu 维护人员对有关已删除块的声明进行了详细分析，并做出了回应。根据这些文件，OpenTofu 社区似乎并未盗用 HashiCorp 的知识产权。

OpenTofu 的创始人身负重任。[HashiCorp ](https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license)于 2023 年 8 月对其流行的 Terraform 基础设施即代码工具进行许可变更，OpenTofu 因此感到不满，[并着手](https://www.linuxfoundation.org/press/announcing-opentofu)成为“MPLv2 许可的 Terraform 的开源继任者”，并进一步承诺“它将以社区为导向、公正、分层且模块化，并向后兼容”。

前景非常光明，但实现起来却极其困难。事实上，OpenTofu 可能非法使用了 HashiCorp 的代码来跟上步伐。

至少，浏览 OpenTofu 的 GitHub 存储库并将其与 HashiCorp 的存储库进行比较，很难避免得出这样的结论。具体来说，OpenTofu 似乎提取了与 Terraform V1.7 中首次实现的新**已删除块**功能相关的 Terraform 代码，该功能是在 OpenTofu 分支创建几个月后根据商业软件许可 (BUSL) 发布的。证据是什么？OpenTofu 采用了此 BUSL 许可的 HashiCorp 代码，删除了标题，并尝试将其重新许可为 Mozilla 公共许可 (MPL 2.0)。

各位，这不是开源的工作方式。你可以不同意版权持有者的许可选择，但你无权拿走他人的代码并撕毁和替换他们的许可。

## 年轻人的傲慢

OpenTofu 于 2023 年 9 月推出，备受瞩目，并获得了 140 多个组织的“正式承诺”支持，其中包括 Cloudflare、Harness、Oracle 和 GitLab。当然，[核心维护人员](https://github.com/opentofu/opentofu/blob/main/MAINTAINERS)主要来自 HashiCorp 的直接竞争对手（Spacelift、env0），他们基于 Terraform 构建了自己的业务，并对 HashiCorp 的许可变更感到不满。这很公平。

到 1 月份，该项目[宣扬 OpenTofu 的普遍可用性](https://www.linuxfoundation.org/press/opentofu-announces-general-availability)，即使它提到了 Terraform 所没有的即将发布的功能，例如客户端状态加密。然而，尽管开局乐观，但团队很快开始意识到实施该功能的难度（[https://github.com/opentofu/opentofu/issues/874](https://github.com/opentofu/opentofu/issues/874)）。安全性很难。（也许 HashiCorp 毕竟不傻。）

如果这种开发速度听起来好得令人难以置信，来自一群仓促组建的相对较小的公司（以及[没有一家主要云供应商](https://www.infoworld.com/article/3705094/follow-the-cloud-money.html)），也许它就是如此。毕竟，无论人们如何看待 HashiCorp 的许可变更，该公司已经花了十年时间来构建产品。这种努力背后的工程实力不会在几个月内产生，无论创始人的远大理想如何。

## 许可魔术

在 Terraform V1.7 中，[HashiCorp 引入了](https://github.com/hashicorp/terraform/blob/v1.7/CHANGELOG.md)一项主要新功能：**已删除块**自动化，它使 Terraform 能够更好地管理资源删除。可以将其视为[配置驱动的途径](https://developer.hashicorp.com/terraform/language/resources/syntax#removing-resources)来terraform state rm。然而，该功能本身虽然很酷，但并不是重点。该功能的时机才是重点。重要的是，此功能是在 2023 年 11 月下旬*在*HashiCorp 切换到 BUSL 之后引入的。如果有人想使用**已删除块**功能，他们无法在 MPL 下获得它。

到 2 月下旬，OpenTofu 发布了类似于 HashiCorp 已删除块自动化的功能。不仅在功能方面，还在完成该功能的代码方面。看看这些存储库，告诉我你是否没有看到相同的内容：

- Terraform 的 [remove_statement.go](https://github.com/hashicorp/terraform/blob/main/internal/refactoring/remove_statement.go)与 OpenTofu 的 [remove_statement.go](https://github.com/opentofu/opentofu/blob/main/internal/refactoring/remove_statement.go)
- Terraform 的 [removed.go](https://github.com/hashicorp/terraform/blob/main/internal/configs/removed.go)与 OpenTofu 的 [removed.go](https://github.com/opentofu/opentofu/blob/main/internal/configs/removed.go)
- Terraform 的 [removed_test.go](https://github.com/hashicorp/terraform/blob/main/internal/configs/removed_test.go)与 OpenTofu 的 [removed_test.go](https://github.com/opentofu/opentofu/blob/main/internal/configs/removed_test.go)
 [remove_target_test.go](https://github.com/hashicorp/terraform/blob/main/internal/addrs/remove_target_test.go) 与 OpenTofu 的 [remove_test.go](https://github.com/opentofu/opentofu/blob/main/internal/configs/removed_test.go)

- Terraform 的 [remove_target.go](https://github.com/hashicorp/terraform/blob/main/internal/addrs/remove_target.go) 与 OpenTofu 的 [remove_endpoint_test.go](https://github.com/opentofu/opentofu/blob/main/internal/addrs/remove_endpoint_test.go)

版权法很复杂。我受过律师培训，但我没有执业，所以不能算是一个好律师。也许 OpenTofu 似乎删除了一些文件中的部分注释很重要。也许他们似乎在这里或那里更改了一行很重要。也许有人可以合理地认为，OpenTofu 实际上并没有创建 Terraform 的 BUSL 许可代码的衍生作品。也许。

然而，当你查看 OpenTofu 文件中的标题时，这样的论点就不那么有说服力了。以下是 HashiCorp 在其 removed 块文件中使用的标题：

```
// Copyright (c) HashiCorp, Inc.
// SPDX-License-Identifier: BUSL-1.1
```

以下是 OpenTofu 使用的标题：

```
// Copyright (c) 2023 HashiCorp, Inc.
// SPDX-License-Identifier: MPL-2.0
```

看出问题了吗？OpenTofu 承认它正在使用 HashiCorp 的代码，但假装有问题的代码是在 MPL 下获得许可的。但事实并非如此。永远不会。所有有问题的代码都是在 *HashiCorp 将 Terraform 迁移到 BUSL *之后发布的。充其量，OpenTofu 社区一直抱有幻想，迫切希望它能追溯性地使 BUSL 许可代码神奇地变成 MPL 许可代码。最糟糕的是，OpenTofu 开发人员欺诈性地盗用了 HashiCorp 的知识产权，并试图将其据为己有。

无论 OpenTofu 的开发人员怎么想，这种行为都与积极的“社区驱动方法”背道而驰，而且肯定没有像 Linux 基金会新闻稿宣称的那样展示“开源的价值”。它看起来很像侵犯了 HashiCorp 的知识产权。OpenTofu 完全有权不同意 HashiCorp 的许可证变更并分叉该项目；OpenTofu 或任何其他人获取 HashiCorp 的代码并应用他们喜欢的任何许可证都是完全非法的。

这感觉像是治理失败，还有其他问题。Cloudflare、Oracle 和其他负责任的公司绝不会加入那种社区，但这似乎就是他们正在得到的。