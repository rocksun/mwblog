# OpenTofu vs. HashiCorp Takes Center Stage at Open Source Summit
![Featued image for: OpenTofu vs. HashiCorp Takes Center Stage at Open Source Summit](https://cdn.thenewstack.io/media/2024/04/361be1a9-zemlin-oss-na-2-1024x576.png)
SEATTLE — The
[InfoWorld](https://www.infoworld.com/article/3714980/opentofu-may-be-showing-us-the-wrong-way-to-fork.html) story by [Matt Asay](https://www.linkedin.com/in/mjasay/) about [OpenTofu](https://thenewstack.io/opentofu-1-6-general-availability-open-source-infrastructure-as-code/) and a cease and desist letter from HashiCorp took center stage Tuesday morning at [Open Source Summit North America](https://events.linuxfoundation.org/open-source-summit-north-america/).
On April 3, InfoWorld published a post by Asay, MongoDB’s vice president of developer relations, in which he claimed OpenTofu, the group that forked Terraform, the widely used Infrastructure as Code product, “lifted Terraform code related to a new removed block feature first implemented in Terraform V1.7, which was released under the
[Business Software License (BUSL)](https://fossa.com/blog/business-source-license-requirements-provisions-history/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform) a few months after the OpenTofu fork was created.”
Hashicorp runs the Terraform project. The company
[changed Terraform’s license](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/) from the [Mozilla Open Source Public License](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/) about seven months ago. What a ride it has been ever since.
So, Asay writes this post, saying, “It looks a lot like a violation of HashiCorp’s intellectual property.”
The OpenTofu project
[has denied HashiCorp’s allegations of code theft](https://thenewstack.io/opentofu-project-denies-hashicorps-allegations-of-code-theft/).
What makes Asay’s post odd, in this case, is how it all looks. His employer, MongoDB, turned to a closed-source license in
[2018](https://techcrunch.com/2018/10/16/mongodb-switches-up-its-open-source-license/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform). And here’s Asay writing this post that simultaneously publishes at about the same time when OpenTofu gets its [cease and desist letter](https://opentofu.github.io/legal-documents/2024-04-03%20HashiCorp%20C%26D/OpenTofu%20C&D%20-%20Redacted.pdf) from Hashicorp.
“Not only did that happen publicly, but simultaneously the OpenTofu maintainers got a cease and desist letter from a Silicon Valley law firm telling them to take that code out,” said
[Jim Zemlin](https://www.linkedin.com/in/zemlin/), executive director of The Linux Foundation, in the opening keynote at the Open Source Summit.
## Investigating ‘Code Theft’ Allegations
I so agree with
[Runtime’s Tom Krazit analysis of the Asay episode:](https://www.runtime.news/hashicorps-threats-to-a-terraform-fork-fell-flat-and-might-have-made-it-stronger/)
That seemed to be enough for Infoworld, which inserted an editor’s note at the top of Asay’s piece saying, “based on these documents, it appears that the OpenTofu community did not misappropriate HashiCorp’s intellectual property” (emphasis theirs) but otherwise left the headline and copy of the article intact.
(Why a venerable enterprise tech publication continues to give a vendor marketing executive the space to write basically anything he wants, especially about a subject where he has an enormous conflict of interest given the similarities between MongoDB and HashiCorp’s open source licensing strategies, remains inexplicable.)
As for OpenTofu? Zemlin said the project leaders analyzed and refuted every facet of the Hashicorp allegation.
“We have tools that allow us to process tens of thousands of contribution agreements in an automated and accurate way,” Zemlin said. We take this stuff seriously, and the OpenTofu project fortunately does, too.
“When they heard these accusations, they immediately went and did a source code origination analysis. They knew where all the code was, how it came in, and what license it was under. And it turns out that this analysis refuted every single aspect of HashiCorp’s allegation.”
What does this mean? We’re looking at a new era — more closed-source licensing and forks, followed by more lawyers and more developers getting caught in the middle.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)