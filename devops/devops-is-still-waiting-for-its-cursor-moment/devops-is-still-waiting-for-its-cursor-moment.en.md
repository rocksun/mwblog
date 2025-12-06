It’s 2:47 am. Your phone is buzzing. Production alerts. The checkout service is throwing 5xx errors and customers are abandoning carts and the on-call engineer is flipping between Datadog, Argo CD, kubectl and logs. She’s just trying to figure out what changed. Latency spiked 20 minutes ago. A deployment went out at 2:31 am.

Two pods are in CrashLoopBackOff. Memory limits were changed. She rolls back, updates the ticket, writes the postmortem and… tries to go back to sleep. Yet she knows she’s gonna go through some version of this again next week.

Meanwhile, her colleague refactored an entire module in [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) in minutes, because of AI. The AI understood the codebase, proposed the change and handled the tedious parts. And it did it all automatically.

What happened?

AI has transformed the way we write code. But it has not transformed the way we operate the infrastructure to run that code.

## **The Gap Continues to Grow Wider**

In the past two years, AI has reshaped the way developers work:

* Cursor and Copilot write and refactor code.
* Tools like Lovable, v0 and Bolt generate frontends.
* Replit agents scaffold and deploy full applications.

But DevOps work remains manual. Engineers still have to resolve incidents by:

Incidents still stall releases. Backlogs still grow.

AI has supercharged development, while operations remained stuck. This isn’t a market oversight. This problem is much, much harder.

## Why Operating Infrastructure Is So Much Different

### 1. There’s No Buffer for Mistakes

A bad code suggestion fails in a branch.  
A bad infrastructure change will immediately affect live traffic.

Every action in DevOps has a blast radius: Pods die, security groups break connectivity and pipelines cause a cascade of failures.

### **2. The Context Surface Is Huge**

An AI for DevOps has to synthesize:

* Production vs. Dev
* The state of [Kubernetes](https://thenewstack.io/kubernetes/)
* [Code](https://thenewstack.io/infrastructure-as-code-or-cloud-platforms-you-decide/) repos for Terraform / Infrastructure as Code.
* CI/CD runs
* Observability signals
* Cloud provider configuration
* Cost data
* Compliance constraints

So your code assistants will only need the file and its neighbors. With DevOps, you’ve got to have whole-stack awareness.

### **3. Every Environment Is Unique**

There’s no universal model that defines the shape of your infrastructure. Every company has custom terraform modules, custom pipelines, deployment strategies, alert rules and dashboard logic. A generic AI just can’t operate safely.

### **4. Governance Is Mandatory**

Real infrastructure demands:

* Role-based access control (RBAC)
* Approvals
* Audit logs
* Compliance evidence

No AI can bypass these processes. It has to be able to integrate with them.

## **Why Existing Tools Fall Short**

It’s tough. Plenty of products address slices of the problem:

* Runbook automation executes predefined scripts.
* AIOps platforms group alerts.
* Observability tools diagnose anomalies.
* Incident management tools route and escalate responders.
* Coding copilots help make changes to IaC

Sure. These are all useful. But none operate in the same way as Cursor does for application code.

## **What a ‘Cursor for DevOps’ Has To Have**

To make a Cursor for DevOps work, you’ve got to have a few things:

### It Has To Run Inside Your Cloud

Infrastructure and data are sensitive. A viable system has to sit in the customer’s virtual private cloud, , use identity and access management, and rely on cloud native large language models (LLMs) like Amazon Bedrock.

### It Needs a Unified Orchestration Layer

IaC, Kubernetes, CI/CD, observability, cost and compliance are all separate domains, right? The AI needs a coordinator who can handle:

* Identity
* Context sharing
* Tool integration
* Multistep workflows
* Infrastructure as Code

### You’ll Need a Well-Designed Human-in-the-Loop System

Here’s the step-by-step process:

1. AI observes and proposes.
2. Humans approve code and infrastructure changes
3. AI executes.
4. Everything is logged.

This is the only way production can work well.

### **Native RBAC Is Essential**

Agents have to be able to inherit the exact permissions of the people they represent. And the elevation has to arrive just in time.

### Domain-Specific Agents With Deep Expertise Are the Key to Success

You don’t want one giant model. You want specialized agents, like:

* Kubernetes agent
* CI/CD agent
* Observability agent
* Compliance agent
* Cost optimization agent
* Code IDE integrated agents

Each one has deep knowledge of its domain. And it’s a single orchestration layer that ties them together. Infrastructure has many separate problems, and you need agents that specialize in Kubernetes, CI/CD, observability, compliance and cost management. These agents make smarter decisions and stay closer to real DevOps work. They can also work together: One agent can flag an issue, another can fix it by either making a config or code change, and a third can verify it, so complex workflows get handled correctly.

## **Early Results Show the Path Forward**

We’ve witnessed teams piloting these architectures. They’re already seeing:

* MTTR reductions of 40 to 70 percent
* Ticket volumes are dropping dramatically
* Provisioning cycles are shrinking from weeks to hours
* Automatic evidence and continuous control checks

These gains come from allowing AI to handle the predictable work. So you don’t have exhausted DevOps teams anymore. AI can now analyze signals, recognize known patterns, execute approved remediations, provision environments and capture audit data behind the scenes. The goal isn’t to replace engineers. The goal is to give them leverage.

## **The Cursor Moment Is Coming**

No, the complexity of [infrastructure hasn’t changed](https://thenewstack.io/how-autonomous-agents-are-changing-infrastructure-management/). But AI capabilities have. The architectural patterns now exist to apply AI on both development and operations safely.

Over the next 18 months, we’re sure to see:

* Better cross-agent orchestration
* Deeper tool integrations
* Richer contextual reasoning
* Smoother alignment with existing workflows
* Beautiful IaC coding experiences.

DevOps has waited for its Cursor moment, and the ingredients are finally in place.

We’re building the AI DevOps Engineer at DuploCloud so you’ll get AI agents that: Run inside your cloud, understand your infrastructure, execute real DevOps tasks with built-in governance and compliance and help write and run your IaC. [Learn more](https://duplocloud.com/) about the DuploCloud AI DevOps Engineer.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/12/347160f9-cropped-957e9965-image2.png)

Zafar Abbas is the CTO at DuploCloud and previously served as vice president of engineering at Juul Labs and Zenefits, directing teams across e-commerce, payroll, platform and infrastructure. He’s passionate about developing great products and empowering high-performing teams.

Read more from Zafar Abbas](https://thenewstack.io/author/zafar-abbas/)