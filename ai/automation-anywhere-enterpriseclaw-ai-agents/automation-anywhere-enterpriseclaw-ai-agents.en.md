The press release version of [Automation Anywhere](https://www.automationanywhere.com/)‘s [EnterpriseClaw](https://www.automationanywhere.com/products/enterprise-claw) announcement is straightforward enough: a new capability for deploying what the company calls “claw-style” AI agents.

These are [autonomous agents](https://thenewstack.io/why-apis-are-the-missing-link-for-truly-autonomous-ai-agents/) that can access device file systems, create tools at runtime, and interact directly with applications across enterprise infrastructure, backed by partnerships with [Cisco](https://thenewstack.io/cisco-is-using-ebpf-to-rethink-firewalls-vulnerability-mitigation/), [Nvidia](https://thenewstack.io/nvidia-nemoclaw-launch/), [Okta](https://thenewstack.io/okta-expands-free-identity-management-services-cloud-native-deployment-options/), and [OpenAI](https://thenewstack.io/openai-launches-gpt-5-5-calling-it-a-new-class-of-intelligence/). It offers better security, Nvidia is contributing [OpenShell](https://thenewstack.io/nvidia-openshell-agent-runtime/), Okta will offer identity management, and OpenAI will allow companies to use the all-new GPT 5.5 within EnterpriseClaw

The more interesting story is what EnterpriseClaw, introduced last week at the company’s [Imagine 2026](https://imagine.automationanywhere.com/) event, reveals about the gap between how AI agents are being built and how enterprises operate.

## **A “claw-style” agent**

[Adi Kuruganti](https://www.linkedin.com/in/adikuruganti27/), Automation Anywhere’s Chief AI and Development Officer, is candid about where the idea came from. Nvidia’s OpenShell — an open source runtime for autonomous, self-evolving agents that could essentially allow agents to replicate anything a human operator could do at a keyboard. That combination of capabilities is what Automation Anywhere is calling a “claw-style” agent, a term the company coined.

EnterpriseClaw is essentially OpenShell’s capability wrapped in centralized governance, he says. A “claw-style” agent differs from a traditional agent in three ways: Device-level access (local or shared), dynamic tool creation at runtime, and interaction with the computer screen.

The problem, Kuruganti says, is that OpenShell “could access pretty much everything, which is not a good thing in enterprise settings.”

For individual users or isolated cloud environments, broad system access is a feature. For a healthcare system, a bank, or a manufacturer running processes in air-gapped data centers, it could lead to a governance failure.

EnterpriseClaw is Automation Anywhere’s answer. It takes the autonomy model, adds centralized governance, credential controls, observability, and the ability to run agents close to where data lives. That includes environments behind firewalls and those that will never touch a public cloud.

## **An industry-wide identity crisis**

Of the four partner integrations, the most telling may be Okta’s. Kuruganti tells *The New Stack* that agent identity, which involves how an autonomous agent authenticates to enterprise systems, what access it gets, and how its actions are audited separately from the humans it works on behalf of, is still a work in progress across the industry.

The current state is awkward, he says. Most enterprises are still handing agents human credentials to access systems like Salesforce or SAP. That means when an agent executes a process autonomously, the audit trail shows a human did it.

“There’s no clear record of what the agent did versus the human,” Kuruganti says.

Okta’s “first-class identity” model — where each agent has its own identity, access scope, and audit trail — is the proposed fix, and the company is working to establish it as a cross-vendor standard, not just an Automation Anywhere integration. That work is ongoing.

## **The hybrid reality**

Kuruganti notes that almost everyone is building for the cloud, but enterprise data is not there yet.

“Most of the agent platforms out there are really thinking all in on cloud only,” he says. “The reality is most of the data doesn’t live in the cloud.”

For large enterprises in healthcare, financial services, and manufacturing — which Kuruganti identifies as Automation Anywhere’s three core customer industries — data lives on-premises, in private cloud VPCs, and in some cases in air-gapped environments where cloud connectivity is not an option.

That’s the architectural bet EnterpriseClaw is making: that the customers who matter most for enterprise automation aren’t the ones who have moved everything to the cloud, but the ones who haven’t and won’t anytime soon, Kuruganti says.

Nvidia’s role in the partnership reflects this directly — [Nemotron](https://thenewstack.io/nvidia-launches-nemotron-3-super-a-120b-open-model-for-large-scale-ai-systems/) models running on-premises via OpenShell exist for the customer whose bare-metal data center has no path to a cloud inference endpoint, he adds.

## **The orchestration play**

How Automation Anywhere positions EnterpriseClaw and the company’s orchestration capabilities against ServiceNow, Microsoft, and others is also worth examining. Kuruganti’s positioning of the company as “the Switzerland of business process orchestration” is a jab at platform-centric competitors.

His argument is that ServiceNow automates within ServiceNow’s ecosystem; Microsoft automates within Microsoft’s. Automation Anywhere’s Mozart Orchestrator, by contrast, is designed to manage agents built on any platform, including competitors’, under a single governance layer.

That is the company’s value proposition. Whether customers experience it that way is a separate issue. But the proliferation of agentic platforms is creating a new orchestration problem and requires a multi-platform agent governance solution.

## **Where it stands**

EnterpriseClaw is in preview, available to Automation Anywhere customers now under existing consumption pricing. A formal GA with dedicated packaging is expected later this year. The company says the preview designation isn’t a technical limitation — production deployments are happening — but a commercial one: they haven’t finalized how they want to price it.

At Imagine, Automation Anywhere also announced Autonomous IT and Autonomous Finance — prebuilt solutions that combine AI agents, process intelligence, and governance controls for the CIO and CFO’s offices. Both are available now.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)