# Spacelift Scales Legacy Automation: Terraform First, Ansible Next
![Featued image for: Spacelift Scales Legacy Automation: Terraform First, Ansible Next](https://cdn.thenewstack.io/media/2025/01/028448f7-spacelift-dimitri_vlachos-1024x768.jpg)
Last week saw the [1.9 release](https://thenewstack.io/opentofu-turns-one-with-opentofu-1-9-0/) of [OpenTofu](https://opentofu.org/), a fork of HashiCorp Terraform brought about [due to licensing restrictions](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/), making it a full year since the first full 1.0 release of the [Infrastructure as Code](https://thenewstack.io/introduction-to-infrastructure-as-code/) (IaC) software.

“We’re very pleasantly surprised by the traction,” said [Dimitri Vlachos](https://www.linkedin.com/in/dvlachos/), chief marketing officer for Spacelift, in an interview with TNS. “The adoption rate and the community involvement and the growth of the community is probably more than people expected.”

Spacelift was one of a coalition of companies that felt the squeeze in August 2023 when HashiCorp [relicensed its infrastructure software stack](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/), including the widely used Terraform, into a BSL ([Business Source License](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/)) that [basically prohibited](https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license) other companies from offering [competitive products around Terraform](https://thenewstack.io/terraform-gets-ai-boost-in-new-cloud-management-platform/), software that allows administrators to manage infrastructure in a code-driven way.

“There were a number of companies in the space that felt that that was a violation of the spirit of the open source,” Vlachos said.

These companies — which, in addition to Spacelift, also included [Scalr](https://www.scalr.com/), [env0](https://www.env0.com/), [Gruntwork](https://gruntwork.io/), [Digger](https://digger.dev/), and [Cloud Posse](https://cloudposse.com/) — were among the parties that [started the fork](https://thenewstack.io/opentf-disgruntled-hashicorp-rivals-threaten-to-fork-terraform/),

They “felt this type of technology should be open source underneath because it’s the fabric that runs a lot of infrastructure underneath,” Vlachos said.

Agreeing with this sentiment was the [Linux Foundation, which soon backed](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/) the project as well.

Over the past year, [the project](https://thenewstack.io/getting-started-with-opentofu-alpha/) was able to include new features, such as encryption, that have [long been requested by users](https://thenewstack.io/opentofu-registry-gets-a-user-interface-and-an-api/) while still remaining backward compatible with the last open source version of Terraform, v 1.55.

“I think OpenTofu is different than a lot of open source projects in that a lot of open source projects have a single entity sponsoring it. We have a number of sponsors. It’s called ‘Open’ for a reason,” Vlachos said.

## Spacelift Is Not an OpenTofu Reseller
Spacelift is no mere OpenTofu redistributor.

The company’s mission has always been to provide a platform to manage [multiple IaC tools](https://thenewstack.io/infrastructure-as-code-in-2024-why-its-still-so-terrible/), such as [HashiCorp’s Terraform](https://thenewstack.io/experts-share-best-practices-for-building-terraform-modules/) and [Pulumi](https://www.pulumi.com?utm_content=inline+mention), outfitting them with additional observability and governance tools for large-scale usage.

“We allow customers to manage infrastructure pipelines in a uniform way,” Vlachos said.

Here is how the [Spacelift platform works](https://spacelift.io/how-it-works): You describe your system with your favorite IaC tool — currently, the company supports Terraform, OpenTofu, [AWS CloudFormation](https://aws.amazon.com/?utm_content=inline+mention), Ansible, [Kubernetes](https://thenewstack.io/Kubernetes/), and [Terragrunt](https://terragrunt.gruntwork.io/)).

Then push your code to a code repository ([GitLab](https://about.gitlab.com/?utm_content=inline+mention), GitHub, AzureDevOps, BitBucket), and then create a stack for your repo.

So, whenever there are changes to this stack, runs will be triggered in Spacelift. You can choose whether you want to apply your code automatically or by manual intervention. If the latter, infrastructure changes are applied.

With Spacelift, primarily services can work on AWS, [Google Cloud](https://cloud.google.com/?utm_content=inline+mention) and Microsoft Azure clouds, as well as for on-prem deployments.

“Enterprises struggle with how to move at speed,” Vlachos explained. “Application developers and engineers want to move quickly. They want to release code. They need the infrastructure underneath to deliver that. But they also have to have all the controls in place to make sure it’s secure, it’s performant, it’s cost effective.”

Baseline automation tools won’t offer features such as visualizing or which individuals have control over which parts of the pipeline, to take two examples.

“Using a tool like OpenTofu or Terraform will help you with the bare bones of deploying more quickly, but it’s not going to give you all the infrastructure. You run into problems as more and more people try to manage these pipelines. You don’t have the policy engine to understand who can do what,” Vlachos added.

In this sense, OpenTofu isn’t competing with Terraform itself, but rather HashiCorp’s [Terraform Enterprise](https://developer.hashicorp.com/terraform/enterprise), or its premium cloud offering [HCP Terraform](https://developer.hashicorp.com/terraform/cloud-docs), either of which offers similar functionality. HasiCorp is in the [process of being acquired](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/) by IBM.

Financial services, retail, and health care companies have all used Spacelift’s service.

## First Terraform, Next Ansible
Another tool that is used a lot in configuration management is [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)‘s [Ansible](https://thenewstack.io/ansible-vs-salt-which-is-best-for-configuration-management/), a widely-used IT automation tool used both on-premises and in the cloud. Red Hat is a [subsidiary of IBM](https://thenewstack.io/red-hat-ibm-acquisition-clash-of-cultures-or-best-of-both-worlds/).

“There’s a lot of challenges running Ansible at scale,” Vlachos explained, pointing to how its difficult to get visibility into workflows created by the technology.

An organization running a large number of Ansible Playbooks over many nodes might find that configuration operations run very slowly. Also, according to Vlachos, Ansible itself provides very little feedback as to the reconfigurations were successful.

The same workflows used for OpenTofu and Terraform will now cover Ansible.

The new features include, in Spacelift’s words:

**Playbook Automation**: Manage Ansible playbooks from a central location.**Inventory Observability**: View all Ansible-managed hosts and playbooks, with visual success or failure indicators for recent runs.**Playbook Run Insights**: Ansible playbook run results with detailed insights to pinpoint problems and simplify troubleshooting.**Integrated IaC and Ansible Workflows**: Combine IaC (Terraform, OpenTofu, CloudFormation) and Ansible into single workbooks.**Developer Self-Service**: A portal for developers to commission workflows.
Red Hat has also been equipping Ansible for cloud usage. In December, [it launched](https://thenewstack.io/red-hat-brings-ansible-automation-to-amazon-web-services/) an Ansible-based hosted service for AWS users, allowing users to manage their AWS-based processes with Ansible.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)