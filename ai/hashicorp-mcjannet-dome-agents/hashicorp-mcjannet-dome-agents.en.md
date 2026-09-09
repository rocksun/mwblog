Ask a traditional enterprise application for a customer address or today’s revenue figures and, broadly speaking, it follows a predictable route its developers have already mapped out: authenticate the user, query the right system, return the result. Given the same underlying data, you’ll get the same answer each time.

Ask an AI agent the same question, and the journey is much harder to forecast. It might consult one system, decide it needs more context from another, make a dozen tool calls, pass information through a language model and only *then* produce an answer. Run the same request again, and it may take a different route altogether.

And in an enterprise, what happens along that route can matter just as much as the answer: which systems the agent accesses, what data it sees, what actions it takes and how much it spends.

That distinction — between predetermined software, and applications that make probabilistic decisions on the fly — sits at the heart of a new company from a founder who knows a thing or two about bringing order to a new generation of infrastructure.

## AI agents are hard to govern

![Dome Systems co-founder David McJannet left HashiCop in August 2025](https://cdn.thenewstack.io/media/2026/09/af2f352f-davemcj.png)

*Dome Systems co-founder David McJannet left HashiCop in August 2025*

[Dome Systems](https://www.domesystems.ai/) was co-founded at the turn of the year by [David McJannet](https://www.linkedin.com/in/davemcj/), who spent close to a decade leading [Terraform](https://thenewstack.io/terraform-state-infrastructure-drift/)-creator HashiCorp [through the cloud era](https://thenewstack.io/hashicorp-is-standardizing-and-industrializing-the-cloud/), culminating in its [blockbuster 2021 IPO](https://www.cnbc.com/2021/12/09/cloud-software-maker-hashicorp-hcp-starts-trading-on-nasdaq.html) and [subsequent](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/) $6.4 billion [sale to IBM in 2025](https://techcrunch.com/2025/02/27/ibm-closes-6-4b-hashicorp-acquisition/). McJannet is joined at the helm by [Marc Holmes](https://www.linkedin.com/in/marcholmes/), who spent more than six years at HashiCorp as chief marketing officer.

In an interview with *The New Stack*, McJannet lays out his company’s thesis on AI agent governance, arguing that enterprises are now running into the same kind of problem that they did with cloud infrastructure: adoption comes first, then the real spadework begins of putting the right controls in place across security, operations and finance.

> “It’s actually a very different architecture, and that is what unlocks the power of these new [agentic] applications.”

Part of the challenge, he says, is that agents are built very differently from the enterprise applications of yore, which companies spent years learning how to control.

“It’s actually a very different architecture, and that is what unlocks the power of these new [agentic] applications,” McJannet explains.

He points to self-driving cars as an example: a model takes in live inputs and interacts with the vehicle’s systems as conditions change, because no developer can reasonably pre-program every possible situation a car might encounter on the road.

“It’s making judgments along the way, as opposed to trying to look up the historical maps of the world and make a real-time decision,” McJannet continues.

An enterprise agent can behave in much the same way: call one tool, assess the result, decide it needs another, and keep going until the task is complete. That flexibility lets agents tackle work that would be difficult to script exhaustively in advance — but it also makes their behaviour harder for enterprises to govern.

And this gets to the heart of what McJannet is striving for with Dome.

## Table stakes for the agent era

The company [launched out of stealth](https://www.linkedin.com/posts/were-thrilled-to-be-co-leading-dome-systems-share-7450591862123298817-BdIT/) back in April with $14 million in seed funding, with McJannet having [departed HashiCorp the previous August](https://www.linkedin.com/posts/davemcj_after-9-years-as-ceo-today-marks-the-end-ugcPost-7366453413066244097-Rtzy/) after the IBM transition concluded.

Dome’s starting point is that an agent combines three things: code, a model, and the backend systems or tools it interacts with. Bringing those pieces together under one platform, McJannet says, is “table stakes” for applying meaningful constraints to what the agent can do.

“If you don’t have an integrated platform, you can’t enforce controls across everything that the agent is doing,” McJannet says.

> “If you don’t have an integrated platform, you can’t enforce controls across everything that the agent is doing.”

And so Dome’s platform is built around those three elements. An [agent registry](https://www.domesystems.ai/platform/registry) keeps track of the agents themselves; an [MCP gateway](https://www.domesystems.ai/mcp-gateway) controls the tools they can call; and a [model broker/router](https://www.domesystems.ai/model-router) governs which models they can use and how requests are routed.

The setup starts by registering the agent and giving it an identity, establishing who is allowed to call it, and connecting the backend tools it can reach — Zendesk, in this example.

![Dome registers an agent, verifies its caller and connects the tools it can use.](https://cdn.thenewstack.io/media/2026/09/ba436e43-gif2.gif)

*Dome registers an agent, verifies its caller and connects the tools it can use.*

Next, Dome connects a model provider, groups available models into a pool with routing and failover rules, then combines the agent, its tools and its models behind a single gateway. That gateway becomes the point through which Dome can apply the policies governing what the agent is allowed to do.

![Dome connects a model provider, creates a model pool and brings the agent behind a gateway.](https://cdn.thenewstack.io/media/2026/09/3061c5f1-gif3.gif)

*Dome connects a model provider, creates a model pool and brings the agent behind a gateway.*

Once those pieces are connected, teams can set permissions on each call, use guards to inspect responses, apply quotas to cap spending, and keep a common audit trail across the agent’s activity.

Today, McJannet says, enterprises are often piecing all of this together themselves. A standalone model broker might be brought in to control spending, while a separate tool gateway handles security and operational concerns. Some are then building their own agent registry to tie those systems together.

Moreover, buying those capabilities separately leaves enterprises with another integration problem to solve. A model router might govern one part of an agent’s activity and a tool gateway another, while the agent itself continues moving between them.

“If you just provide the tool gateway or just the model router, it doesn’t allow you to have this kind of system of control,” he says.

That is also where Dome’s latest move enters the fray. After spending its first months in early access, the company is now opening the platform to self-service users for the first time, allowing teams to sign up with little more than a credit card, bypassing the typically arduous enterprise sales process.

## Dome goes self-serve

Self-serve is relatively unusual route for this kind of enterprise infrastructure product. Dome is [publishing its prices](https://www.domesystems.ai/pricing), offering a free tier and letting practitioners get started without first going through a sales process, while keeping the traditional enterprise route open for larger customers.

The thinking is partly about who McJannet expects to use the product. Rather than limiting access to buyers who are already deep into a procurement process, for example, self-serve enables individual practitioners to be able to discover, try and use the platform themselves.

“”We want to make the barrier as low as possible to have people come on board,” McJannet says, adding that Dome had already seen a number of self-service sign-ups ahead of the launch.

Separately, its pricing reflects a belief about where value will ultimately sit in this market. McJannet regards [model routing](https://thenewstack.io/cursor-ramp-meta-model-router/) and tool connectivity as baseline capabilities, with the more valuable piece being the *controls* that sit across the agent as a whole — think permissions, data redaction and spending quotas.

It’s also worth noting that while Dome’s main target user will be platform engineering teams inside large enterprises, typically working alongside operations and security, self-serve also creates an opening for another kind of user: the small company, perhaps even only one or two people, building an agent and trying to sell into an enterprise. The sort of scenario that aligns with the fabled [one-person unicorn](https://techcrunch.com/2025/02/01/ai-agents-could-birth-the-first-one-person-unicorn-but-at-what-societal-cost/) promised by many in [the AI realm](https://x.com/alexisohanian/status/1752753792058294725).

Indeed, McJannet says developers can get far building the application itself, only to hit a wall when a prospective enterprise customer begins its security and operations review. How is identity enforced? Who can see the data the agent reaches? What happens when it calls other agents? Can its activity be reconstructed afterwards?

Some builders, he says, have asked whether they can “certify” their agents on Dome because “*my agent won’t get deployed until I can satisfy these infrastructure elements*.” McJannet is careful to add that Dome doesn’t currently run such a certification program, but it’s clearly one route the company could venture down.

“If you register that agent on Dome, all the infrastructure elements are taken care of,” McJannet says.

## ‘Unblocking AI agents’: Lessons from the cloud era

That division between developers eager to ship, and enterprise teams worried about what happens after, is also where McJannet sees the strongest parallel with his years at HashiCorp.

During McJannet’s tenure, HashiCorp increasingly positioned itself around helping large organizations standardize how cloud infrastructure was provisioned, secured and connected. That included the [2020 launch](https://www.globenewswire.com/news-release/2020/06/22/2051130/0/en/hashicorp-launches-multi-cloud-infrastructure-automation-as-a-service-with-hashicorp-cloud-platform.html) of HashiCorp Cloud Platform (HCP), which offered its infrastructure tools as managed cloud services.

More broadly, McJannet’s account of early cloud adoption begins with developers swiping a credit card and deploying directly to Amazon because cloud infrastructure allowed them to build applications that had previously been impractical. The applications were compelling enough that enterprises adopted cloud despite resistance from operations and security teams, and what followed was a second phase: companies needed common services for provisioning, credentials, networking and other controls before cloud could become routine across the organization.

Platform engineering teams became the people responsible for reconciling those two demands: allowing developers to build while giving security, operations and finance enough control to permit those applications into production. McJannet believes agents are now creating the same tension.

> “You’ve got this queue of cool apps that developers build that the ops and security teams are just not comfortable letting flourish in their environments.”

“You’ve got this queue of cool apps that developers build that the ops and security teams are just not comfortable letting flourish in their environments,” he says. “And so, inevitably, it has to go that same direction where the platform engineering team has to figure out [a way] to get to say ‘yes’.”

Dome’s bet is that enterprises will eventually prefer one system spanning the entire agent to a patchwork of gateways, routers and security products. In McJannet’s telling, that common control layer is what gives enterprises a way to limit how far an agent can roam while still letting it act autonomously.

“You have to have this control layer that provides this corridor where we can constrain the behavior of that new type of application architecture,” he says. “Because without that, you cannot unblock the deployment of AI applications.”

> “That’s the part that we’re trying to answer — how do we unblock agents at scale?”

There is still plenty for Dome to prove. The company isn’t naming customers at this stage; McJannet says none of the enterprises it has worked with are yet willing to be identified publicly, though he says Dome has spent the past eight months talking to dozens of them.

Ultimately, McJannet believes the cloud era showed that new applications only become commonplace once enterprises have the controls to let them through. Dome is his attempt to solve that problem for agents.

“I think that’s the part that we’re trying to answer — how do we unblock agents at scale?”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)