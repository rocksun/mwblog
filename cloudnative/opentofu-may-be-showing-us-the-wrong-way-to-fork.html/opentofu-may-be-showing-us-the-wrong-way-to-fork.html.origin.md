*Update: Since this article was published, HashiCorp sent OpenTofu a cease-and-desist letter on April 3, 2024, expressing in greater detail the concerns raised in this post. On April 11, 2024, the OpenTofu maintainers responded with a detailed analysis of the claims made about the removed block. Based on these documents, it appears that the OpenTofu community did not misappropriate HashiCorp’s intellectual property. *
OpenTofu’s founders had a mission. Upset by
[HashiCorp licensing changes](https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license) in August 2023 to its popular Terraform infrastructure-as-code tool, [OpenTofu set out](https://www.linuxfoundation.org/press/announcing-opentofu) to be the “open source successor to the MPLv2-licensed Terraform,” further promising that it “will be community-driven, impartial, layered and modular, and backward-compatible.”
Hugely promising, but extraordinarily difficult to pull off. So difficult in fact, that OpenTofu may have illegally taken HashiCorp’s code to keep pace.
At least, it’s hard to avoid that conclusion, perusing OpenTofu’s GitHub repositories and comparing them to HashiCorp’s. Specifically, OpenTofu appears to have lifted Terraform code related to a new
removed block feature first implemented in Terraform V1.7, which was released under the Business Software License (BUSL) a few months after the OpenTofu fork was created. The tell? OpenTofu took this BUSL-licensed HashiCorp code, removed the headers, and tried to instead relicense it under the Mozilla Public License (MPL 2.0).
Folks, that’s not how open source works. You can disagree with a copyright holder’s choice of license, but you don’t have the right to take someone else’s code and rip-and-replace their license.
## The hubris of youth
OpenTofu launched in September 2023 to much fanfare and “formal pledges” of support from more than 140 organizations, among them Cloudflare, Harness, Oracle, and GitLab. Of course, the
[core maintainers](https://github.com/opentofu/opentofu/blob/main/MAINTAINERS) mostly came from direct HashiCorp competitors (Spacelift, env0) that had built their businesses on Terraform and were upset by HashiCorp’s license change. Fair enough.
By January, the project was
[touting OpenTofu’s general availability](https://www.linuxfoundation.org/press/opentofu-announces-general-availability), even as it called out soon-to-be-released features like client-side state encryption that Terraform didn’t have. Despite the optimistic start, however, the team soon [began to realize the difficulty](https://github.com/opentofu/opentofu/issues/874) of implementing the feature. Security is hard. (Maybe HashiCorp wasn’t dumb, after all.)
If that pace of development sounds too good to be true, coming from a hastily assembled group of relatively small companies (and
[none of the major cloud vendors](https://www.infoworld.com/article/3705094/follow-the-cloud-money.html)), perhaps it was. After all, whatever one may think about HashiCorp’s license change, the company has spent a decade building the product. The engineering muscle behind such an effort doesn’t spring to life in a few months, whatever the high-flying ideals of founders.
## Licensing magic
In Terraform V1.7,
[HashiCorp introduced](https://github.com/hashicorp/terraform/blob/v1.7/CHANGELOG.md) a major new feature:
removed block automation, which lets Terraform better manage resource deletion. Think of it as a
[config-driven approach](https://developer.hashicorp.com/terraform/language/resources/syntax#removing-resources) to
terraform state rm. However, the feature itself, while cool, isn’t the point. The timing of that feature is. Importantly, this feature was introduced in late November 2023
*after *HashiCorp switched to the BUSL. If someone wanted to use the
removed block functionality, they couldn’t get it under the MPL.
By late February, OpenTofu released similar functionality to HashiCorp’s removed block automation. Not just in terms of what it does, but also in terms of the code written to accomplish it. Take a look at these repositories and tell me if you don’t see the same thing:
- Terraform’s
[remove_statement.go](https://github.com/hashicorp/terraform/blob/main/internal/refactoring/remove_statement.go)versus OpenTofu’s [remove_statement.go](https://github.com/opentofu/opentofu/blob/main/internal/refactoring/remove_statement.go)
- Terraform’s
[removed.go](https://github.com/hashicorp/terraform/blob/main/internal/configs/removed.go)versus OpenTofu’s [removed.go](https://github.com/opentofu/opentofu/blob/main/internal/configs/removed.go)
- Terraform’s
[removed_test.go](https://github.com/hashicorp/terraform/blob/main/internal/configs/removed_test.go)versus OpenTofu’s [removed_test.go](https://github.com/opentofu/opentofu/blob/main/internal/configs/removed_test.go)
- Terraform’s
[remove_target_test.go](https://github.com/hashicorp/terraform/blob/main/internal/addrs/remove_target_test.go)versus OpenTofu’s [remove_test.go](https://github.com/opentofu/opentofu/blob/main/internal/configs/removed_test.go)
- Terraform’s
[remove_target.go](https://github.com/hashicorp/terraform/blob/main/internal/addrs/remove_target.go)versus OpenTofu’s [remove_endpoint_test.go](https://github.com/opentofu/opentofu/blob/main/internal/addrs/remove_endpoint_test.go)
Copyright law is complicated. I am a lawyer by background, but I don’t practice and so can’t be considered a very good one. Maybe it matters that OpenTofu seems to have deleted some comments in a few files. Maybe it matters that they seem to have changed a line here or there. Perhaps one could credibly argue that OpenTofu has not, in fact, created derivative works of Terraform’s BUSL-licensed code. Perhaps.
Such an argument becomes less persuasive, however, when you look at OpenTofu’s headers on the files. Here’s the header that HashiCorp used on its
removed block files:
// Copyright (c) HashiCorp, Inc.
// SPDX-License-Identifier: BUSL-1.1
Now here’s the header that OpenTofu used:
// Copyright (c) 2023 HashiCorp, Inc.
// SPDX-License-Identifier: MPL-2.0
See the problem? OpenTofu recognizes that it’s using HashiCorp’s code but pretends the code in question was licensed under the MPL. Except it wasn’t. Ever. All of the code in question was released
*after *HashiCorp moved to BUSL for Terraform. At best, the OpenTofu community has engaged in wishful thinking, desperately hoping it could retroactively make BUSL-licensed code magically become MPL-licensed code. At worst, the OpenTofu developers deceitfully misappropriated HashiCorp’s intellectual property and tried to make it their own.
Whatever OpenTofu’s developers may think, this sort of behavior is the opposite of a positive, “community-driven approach” and definitely doesn’t show “the value of open source,” as the Linux Foundation press release proclaims. It looks a lot like a violation of HashiCorp’s intellectual property. It’s completely fair for OpenTofu to disagree with HashiCorp’s license change and fork the project; it’s completely illegal for OpenTofu or anyone else to take HashiCorp’s code and apply whatever license they prefer.
This feels like a failure of governance, among other things. There’s no way that Cloudflare, Oracle, and other responsible companies signed up for that kind of community, but that seems to be what they’re getting.