Going forward, when you run [IBM](https://ad.doubleclick.net/ddm/trackclk/N1114924.4097665THENEWSTACK/B33037161.434371219;dc_trk_aid=627496700;dc_trk_cid=227599223;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=$%7BGDPR%7D;gdpr_consent=$%7BGDPR_CONSENT_755%7D;ltd=;dc_tdv=1?utm_content=inline+mention)‘s Terraform Infrastructure as Code (IaC) software, you will have one language to write your configurations: the HashiCorp Configuration Language (HCL).

On Monday, HashiCorp, an IBM company, announced that it will no longer support the Terraform Cloud Development Kit (CDK or CDKTF). Although the existing code will remain available in a [GitHub archive](https://github.com/hashicorp/terraform-cdk), HashiCorp will no longer maintain or update the code, leaving it all but unusable for enterprises.

“Unfortunately, Terraform CDK did not find product-market fit at scale. HashiCorp, an IBM Company, has chosen to focus its investments on Terraform core and its broader ecosystem,” a note on the site read.

The CDK itself is licensed under the [Mozilla Public License](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/) (MPL), so users are free to fork the software itself, IBM suggested.

The company, however, is encouraging users to use [HCL](https://github.com/hashicorp/hcl), which was developed by HashiCorp and licensed under the Mozilla Public License (MPL), originally designed for the software.

## Terraform’s Rocky History

Originally released in 2014 by HashiCorp, Terraform is software that allows administrators to automate the deployment of IT infrastructure, either in the cloud or on premises, through the use of scripts and a set of Terraform commands such as `terraform init`, `terraform plan` and `terraform apply`. The output is rendered as [JSON](https://thenewstack.io/an-introduction-to-json/).

Over time, Terraform [has become](https://thenewstack.io/is-terraform-dead-revive-your-infrastructure-as-code-strategy/) the most popular software for automated IT deployment, especially in the [cloud native community](https://thenewstack.io/cloud-native/).

In 2023, HashiCorp [switched](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/) the Terraform license from open source to a Business Source License, which spurred a user-based open source fork of the software, called [OpenTofu](https://thenewstack.io/how-opentofu-happened-and-whats-next/), that was adopted by the [Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention) and, later, by the [Cloud Native Computing Foundation](https://thenewstack.io/opentofu-joins-cncf-new-home-for-open-source-iac-project/) [(CNCF)](https://cncf.io/?utm_content=inline+mention).

In 2024, IBM [announced](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/) it was acquiring HashiCorp and finalized the purchase earlier this year.

## Terraform CDK Migration Plans

Despite a call to open source the CDK, IBM is encouraging current users to adopt the HCL if they are not already doing so.

“If you are not using AWS CDK, we highly recommend migrating to standard Terraform and HCL for long-term support and ecosystem alignment,” the company asserted.

Terraform users with .tf files created under the CDK can convert them to HCL with the following command:

```
cdktf synth --hcl
```

Those using CDTF on [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) infrastructure can also use [AWS’ own CDK](https://aws.amazon.com/cdk/).

## The Limits of IaC

Overall, the Infrastructure as Code user base appears [to be chafing](https://thenewstack.io/infrastructure-from-code-what-went-wrong/) from [the limits of IaC](https://thenewstack.io/infrastructure-as-code-in-2024-why-its-still-so-terrible/).

As a result, many alternative approaches to Terraform have popped up in the last few years, including [Adam Jacob’s System Initiative](https://thenewstack.io/chef-creator-unveils-ai-platform-to-fix-flaws-with-infrastructure-automation/) and [Formae from Platform Engineering Labs](https://thenewstack.io/kubecon-a-terraform-killer-built-on-apples-pkl/).

They point to how HCL has its limits, especially for highly scalable environments. A declarative configuration language, HCL is limited in offering advanced programming constructs, and many resulting workarounds have resulted in obtuse code. Tooling is limited as well.

The advantage that the CDKTF brought to users was that it allowed them to detail deployment instructions through their own favorite programming language rather than HCL. CDKTF supported [TypeScript](https://thenewstack.io/what-is-typescript/), [Python](https://thenewstack.io/what-is-python/), C# and the [Go programming language](https://thenewstack.io/introduction-to-go-programming-language/).

This is also the approach that Terraform competitor [Pulumi](https://www.pulumi.com?utm_content=inline+mention) has [staked out](https://thenewstack.io/qa-pulumis-joe-duffy-on-the-renaissance-of-infrastructure-as-code/), namely the ability to provision infrastructure in [any one of a number of programming languages](https://thenewstack.io/pulumi-program-the-infrastructure-with-an-actual-programming-language/).

Yet, there has also been considerable debate around whether a general-purpose programming language is better than a domain-specific language. Terraform’s users are administrators, not programmers, as critics have pointed out.

## Community Reaction

Nonetheless, many of those in the IaC community [took the news hard](https://bsky.app/profile/rawkode.dev/post/3m7ojjj35uc26). Kubernetes expert [David Flanagan](https://www.linkedin.com/in/rawkode/) noted that the development kit has gotten over 140,000 downloads per week for TypeScript alone, with similar numbers in other language communities.

So clearly, the CDKTF is still highly used by the community, he argued.

“You don’t kill a project with [an estimated] million users every single month because nobody likes it or it doesn’t have a ‘market fit.’ You kill it because it is not increasing your profit margin, it is not selling enterprise licenses,” Flanagan said in a short video.

To be fair, IBM has a long history of buying open source-based companies, and keeping the open source licensing intact, [including](https://thenewstack.io/red-hat-ibm-acquisition-clash-of-cultures-or-best-of-both-worlds/) the Linux-based [Red Hat](https://www.openshift.com/try?utm_content=inline+mention), the Cassandra-focused [Datastax](https://thenewstack.io/ibm-to-acquire-datastax-to-boost-watsonx-ai-development/) and, most recently, the [Kafka-based Confluent](https://thenewstack.io/ibms-confluent-acquisition-is-about-event-driven-ai/). (There’s been no word, however, on whether IBM would [revert the Terraform license](https://thenewstack.io/with-ibms-open-source-roots-terraform-could-be-free-again/) back to open source.)

Flanagan went on to note that people are probably using the CDKTF because they require the additional programming capabilities. “It’s called Infrastructure as Code, not Infrastructure as JSON,” he quipped.

Site reliability engineer [Liz Fong-Jones](https://www.lizthegrey.com/) offered a more measured response.

“To be more gentle about this, HashiCorp has decided to stop trying to compete with Pulumi with language-native APIs; they’re all in on HCL as the only way to work with Terraform,” Fong-Jones [wrote on BlueSky](https://bsky.app/profile/lizthegrey.com/post/3m7ojmtbtoc23).

## Do We Need a Programming Language for IaC?

In fact, others think this may not be a bad idea.

Platform Engineering Labs’ Co-Founder and CEO [Pavlo Baron](https://platformengineering.com/author/pavlo-baron/) thought the IBM move made sense.

“IBM is historically good at optimizing for the target buyer. This is rather a sign that nobody on the right side of the cycle wants to do full-blown programming. CDKs, and this includes the approach Pulumi takes, are exclusively for developers. Developers usually don’t operate infrastructure,” he wrote by email.

“Serious operations happen on the right side of the cycle, though. Thus, the CDK is missing their target user and addresses the wrong one. So I understand and support the logic behind this move.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)