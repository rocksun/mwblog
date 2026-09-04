Connecting an AI agent to a tool is relatively straightforward. Things get more complicated once an organization has hundreds or thousands of resources spread across different clouds and platforms. Agentic Resource Discovery, or ARD, is meant to help agents find their way through all of that.

AWS highlighted the open specification in its August 31 [Weekly Roundup](https://aws.amazon.com/blogs/aws/aws-weekly-roundup-welcome-ducklabs-to-the-team-agentic-resource-discovery-ard-and-more-august-31-2026/) after taking a deeper technical look at it a week earlier, describing the idea as “DNS, but for agents.” Instead of telling an agent where to find everything ahead of time, ARD lets it search across different registries for what it needs.

And despite AWS highlighting the project, ARD isn’t an AWS technology. It was authored by [Junjie Bu](https://www.linkedin.com/in/junjiebu/) of Google, [R.V. Guha](https://www.linkedin.com/in/r-v-guha-59b19412/) of Microsoft and [Shaun Smith](https://www.linkedin.com/in/smithshaun/) of Hugging Face, and released under the Apache 2.0 license. Engineers from several other companies have helped shape the project, including Cisco, Databricks, GitHub, GoDaddy, [Nvidia](https://thenewstack.io/nvidia-hugging-face-acquisition-neutrality/), Salesforce, ServiceNow, and Snowflake.

AWS’s role, at least so far, has been to provide feedback on the specification and explore how it could work with its own Agent Registry. The goal is to make the registries that already exist work together.

> Instead of telling an agent where to find everything ahead of time, ARD lets it search across different registries for what it needs.

## MCP skips the discovery step

The [Model Context Protocol](https://thenewstack.io/mistral-mcp-connector-migration/) has become a common way for AI applications to connect to external tools and data, but it assumes the client already knows which server it wants to use. That becomes a problem as companies [spread their infrastructure across clouds](https://thenewstack.io/enterprise-ai-agent-governance/), SaaS platforms and internal systems.

ARD helps an agent find a resource before it tries to use it. The specification uses the term “agentic resource” for anything an AI client can connect to, from an MCP server to other outside capabilities. An ARD-compatible service keeps track of what’s available instead of requiring developers to set up every connection in advance.

> The Model Context Protocol has become a common way for AI applications to connect to external tools and data, but it assumes the client already knows which server it wants to use.

## Federation without forced migration

Companies can keep their own catalogs and policies while routing searches to other ARD-compatible services. An enterprise, for example, could keep internal resources private while searching approved external catalogs when needed. AWS calls this “describe once, discover everywhere.”

The current v0.91 proposal, dated August 26, uses JSON-LD and a REST interface. Its required POST /search endpoint searches by task, while optional endpoints allow clients to browse available resources.

Each discovery service can set its own rules for what it returns and which sources it trusts. This is also where AWS’s DNS comparison falls short. A domain name points to a specific location, while an ARD search could turn up several options that all appear capable of doing the job.

## Route 53 engineers shaped ARD

The DNS comparison has some history behind it. Two of the three authors of AWS’s August 24 ARD post work closely with Route 53. Principal software engineer [Jeffrey Damick](https://www.linkedin.com/in/jeffreydamick/) focuses on DNS and networking technologies, while [Bhargav Talluri](https://www.linkedin.com/in/bhargavt/) leads product management for Route 53, as well as for agent identity and discovery in AWS Agent Registry.

Agent Registry already gives AWS customers a central view of their resources. Adding ARD could bring resources running elsewhere into that view without requiring companies to register everything with AWS.

> Adding ARD could bring resources running elsewhere into that view without requiring companies to register everything with AWS.

ARD’s governance is still being worked out, with board terms and membership among the details yet to be settled. The group has also discussed eventually moving the project to a neutral organization such as the W3C or an AI foundation.

AWS is already exploring how it could connect with Agent Registry and [find resources outside its own catalog](https://thenewstack.io/cloudflare-ai-web-economics/).

There may not be much time to settle on a common approach, since connecting all these directories will only get harder once companies have built their own discovery systems.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)