# AI Agents: Why Workflows Are the LLM Use Case to Watch
![Featued image for: AI Agents: Why Workflows Are the LLM Use Case to Watch](https://cdn.thenewstack.io/media/2025/02/92fad013-ai-agents-workflows-watch-1024x576.jpg)
There’s an unsung hero of the modern enterprise: the workflow. It’s sometimes called a rules engine, a process flow, a single-state machine or a software-defined workflow. In a user interface (UI), it’s a “wizard.” Developers often call it (somewhat dismissively) “the business logic.”

I want you to take a moment to appreciate this unsung hero’s quiet dignity because we’re about to throw the white-hot light of Silicon Valley hype on its doorstep: AI agents.

There’s so much written about AI, large language models (LLMs) and agentic applications, it’s hard to believe how many of us (and yes, that includes me) are still confused about them. But there’s a good reason why we are: AI agents are an *implementation detail *of our quiet business hero, the workflow.

Agents are the *how*. The workflow is the *what*.

The distinction is critical because [AI agents can be defined](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) in a pretty straightforward way: Your business application uses a foundation model throughout a workflow. Our friends at Anthropic make a [distinction between agentic workflows and agents](https://www.anthropic.com/research/building-effective-agents), where agents can loop and branch and be somewhat autonomous. In my experience, business workflows do this too; it’s a fuzzy boundary.

## Let’s Talk About How AI Changes Workflow Apps
An agentic app uses foundation models to identify places to intervene in a workflow. For example: Foundation models can be stunningly good classifiers, replacing painstakingly encoded rulesets or supervised learning models with something more flexible and high performing out of the box.

Point a foundation model towards an email inbox or an account summary and start asking: Is the current situation something an app knows how to handle? Should this case be escalated, based on rules written by non-technical business experts? Should this item go to the specialist quality control (QC) flow, or the default QC flow? Is this email spam? Harassment? A sales opportunity? A churn risk?

The model output here is a “yes” or “no,” which presents far fewer accuracy risks than a chatbot. This is stuff you can ship, with safety and measurable outcomes, right now.

The sudden availability of effective, inexpensive natural language classifiers will accelerate many enterprise applications because the distance between *what the business wants* and the *rules that get encoded in software *are currently a major source of human suffering in Fortune 500 companies. Things get heard incorrectly. Things decay and go out of sync. Technical constraints flow upstream and get encoded into business processes.

The agentic app bridges this gap between our intention and our software because much of the business logic can be represented in natural language, inviting new stakeholders and contributors into the software development process. It is [as big a shift in power inside businesses](https://thenewstack.io/ai-is-rapidly-redefining-how-humans-develop-and-use-apps/) as the arrival of spreadsheets around 1985 and the arrival of collaborative spreadsheets around 2005.

There are small but expensive workflow glitches all over enterprises, and AI agents give app developers a powerful set of tools to throw at them.

But agents mean more to workflows than just classifiers! They can also start to evaluate outputs (is the problem really solved?), operate as a text generator (here’s a system event log turned into a status update), and sometimes even initiate action by executing a function (booking a meeting, updating an inventory, dispatching a truck).

All of this could be done by traditional business software and human labor queues, but it’s usually really expensive to get right.

## The Low-Code Moment and the High-Code Future
AI is having a consumer chatbot cultural moment and has some traction with code assistants. What we have yet to see — what might happen this year — is AI adoption spreading from software and a few other niches into other business verticals, particularly the operations layers that seem to produce the most custom apps inside enterprises.

Per its financial disclosures, the first company to see positive returns on AI investment isn’t a pure tech play. It’s an operations software as a service (SaaS) provider, [ServiceNow](https://www.servicenow.com/products/observability.html?utm_content=inline+mention). It, along with Workday and Salesforce, are offering a [low-code bridge](https://thenewstack.io/low-code-no-code/) between business intentions, as documented by non-technical subject matter experts, and software automation. AI is helping.

Cheers to these folks for moving first and making this work. I think this will follow the pattern of most low-code solutions, which promise to empower business users and trim IT spend, but with a non-trivial handcuff to a platform vendor.

I think the next wave will be a high-code replication of these workflow engines because it’s not that hard to implement. Open foundation models and [existing frameworks](https://thenewstack.io/spring-ai-transforms-java-for-genai-app-delivery) (including [Spring AI](https://spring.io/projects/spring-ai), which my team maintains) can get a team started in days. This may look like a big GUI platform for business task workflows, but a quicker and safer path will be finding small, shippable points of intervention… everywhere. And this looks a lot lighter and a lot faster today than it did a few years ago.

## A Hypothetical Agentic App: Smaller Than You Think
Imagine a customer buys an indoor bike trainer, and it ships. The software to manage the bike can’t connect. The customer asks for a return, and away we go, mailing bikes. But what if that was a known issue with a resolution available? Update some firmware, go ride.

Your human worker in the support process might identify that, but imperfectly. It’s hard to know every issue, every time.

So we build a tiny app to look for this issue and fix it. First we build a listener that flags possible incidents of this known issue. If it detects a case, it inserts a message in the support system with a link to the resolution. Safe enough to try right now, with measurable outcomes. An agent might get more assertive with a good track record. Can we email the proposed resolution directly to the customer? Can we pause the return unless the human support acknowledges the issue? Could the agent start to more closely identify the likely issue, link to specific firmware versions or otherwise improve messaging to the customer?

There are small but expensive workflow glitches all over enterprises, and AI agents give app developers a powerful set of tools to throw at them.

## You’ll Need a Platform
So how do we get closer to a world where your app developers are empowered to deploy little helpers throughout your business?

You can start by asking why they aren’t rapidly deploying small experiments without LLMs. And that usually looks like the dev experience story: self-serve provisioning, well-documented golden paths to production, robust test automation, and pre-approved lanes for [safety and legal oversight](https://thenewstack.io/kubecon-keynotes-wrestle-with-ai-governance-complexities). If app teams are empowered to ship small, continuous improvements with minimal outside dependencies, things go fast.

How do we apply this to our agentic app future? First of all, we need to wrap that self-serve pattern and developer empowerment around our new best friend, the foundation model. We are seeing a separation of competencies emerging between data science or AI working groups and full-stack app development teams. In my view, this is healthy role specialization: there are model providers, there are machine learning (ML) ops model infrastructure teams, and there are applications consuming these resources. The first two might be as-a-service external vendors; the app teams won’t be.

For this abstraction between model provider and app teams to work, you’ll need feedback, observability, versioning and other concerns to be handled; with a formal API or at least a good working agreement. What you do not want is every app team solving this in isolation; you probably need an AI framework, but you don’t need 50 competing, underresourced AI frameworks.

I also think that there’s [a role for middleware platforms like an AI gateway](https://thenewstack.io/not-my-fathers-middleware-how-to-be-productive-with-agentic-ai/), which facilitates provisioning, observability, model feedback and privacy guardrails across an organization.

## The Future: Microservice to Nano Service
If provisioning and platforming get solved, we’re running headlong into a world where we have very thin wrappers around a lot of enterprise data that used to be locked up, and we have agentic apps that can access them in clever ways. Small solutions start blooming all over.

![Code block - An example of a very lightweight tool wrapper with natural language instructions on how a foundation model can interact with it.](https://cdn.thenewstack.io/media/2025/02/e06c0499-lightweight-tool-wrapper.png)
An example of a very lightweight tool wrapper with natural language instructions on how a foundation model can interact with it.

It’s the same story we had with cloud native architectures and microservices communicating over APIs. The thing that’s new is the scale of effort; we’re moving from micro to nano. Very thin wrappers, like the [Model Context Protocol](https://spring.io/blog/2025/02/14/mcp-java-sdk-released-2), let foundation models request data and perform actions. Very lightweight workflow apps let business users explain what should happen in natural language. Platforms provide safety, security and appropriate models on demand. You ship in days, not months, and iterate until it works.

The takeaway here is that the agentic app revolution isn’t a story that will transform bleeding-edge tech companies. It’s a modernization story; a fighting chance to solve small problems across existing enterprises with the team you already have.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)