The general consensus emerging across the AI and industrial spheres is that the models themselves [are no longer the bottleneck](https://thenewstack.io/ai-agent-infrastructure-bottleneck/) — they are more than good enough to power deep conversations, produce vast swathes of production-grade code, and resolve all manner of customer support requests.

The harder problem is everything wrapped around the models: the policies that decide what an agent can do on its own, the escalation path for when it can’t, and the record showing what happened when something goes wrong.

## Making agents reliable

Ultimately, it boils down to trust: As a head of customer operations or a chief information officer, do you want a system handling live customer calls and taking actions on someone’s account without a clear boundary on what it’s allowed to handle unsupervised, and who’s accountable if it fails?

OpenAI thinks it has an answer in the form of Presence, a product unveiled on Wednesday that puts AI agents — the same ones OpenAI has been running on its own support line — on enterprise phone and chat channels.

In a [blog post](https://openai.com/index/introducing-openai-presence/) announcing the product, OpenAI notes that the real test for enterprise AI agents has moved beyond proving they can do the job — now it’s whether they can stay reliable as the products, policies, and people around them keep changing.

“The challenge for enterprises is no longer proving that AI agents can work; it’s making them reliable enough to do high-value work in production,” the company writes. “Agent behavior must also adapt as products, policies, and user behavior change.”

> “The challenge for enterprises is no longer proving that AI agents can work, it’s making them reliable enough to do high-value work in production.”

## Presence of mind

Presence is the agent and everything needed to run it in production, bundled into one product — OpenAI builds and deploys the agent itself for each customer, and packages it with the policies, testing tools, and monitoring needed to keep it running once it’s live.

At the center of it is the agent itself, which can handle live conversations in real time: verifying who it’s talking to, looking up an account or an order, and resolving the issue directly, whether that’s a duplicate charge or a delivery update, without needing a person on the line.

![AI agent verifies a customer, resolves duplicate charge](https://cdn.thenewstack.io/media/2026/07/bc1fd68f-openai-presence-still-1-1024x576.webp)

*AI agent verifies a customer, resolves duplicate charge*

Before any of that goes live, teams can run a policy change through simulation, testing it against a batch of past cases and scoring how it holds up across categories like refunds, cancellations, and account verification before approving the rollout.

![Simulation testing a new refund policy change](https://cdn.thenewstack.io/media/2026/07/a61162d0-openai-presence-still-2-1024x576.webp)

*Simulation testing a new refund policy change*

Once an agent is in production, a live dashboard tracks its ongoing performance — response accuracy, call volume, and how it’s handling specific tasks like refunds or cancellations — giving teams a way to catch problems as they emerge.

![Live dashboard tracking agent performance and volume](https://cdn.thenewstack.io/media/2026/07/12e9003b-openai-presence-still-3-1024x576.webp)

*Live dashboard tracking agent performance and volume*

With Presence, a company picks a single, specific job for the agent to handle, such as an insurance claim, an IT request, or a billing dispute, and the agent only gets the systems and information tied to that job, nothing more. It’s the company, not OpenAI, that sets the rules: what the agent can do without checking in, what needs a person’s sign-off first, and the point at which it stops and hands over to a human.

Getting to that point, however, isn’t a matter of flipping a switch on an API. OpenAI’s own engineers sit with each customer to figure out the job, wire up the systems, decide the permissions, run it through testing, and get it live, then hand ongoing support to outside integration partners as the deployment grows.

Notably, OpenAI says this has actually been part of its own internal support operation for some time, where it claims the agent now resolves 75% of inbound issues on its English-language phone line without a person stepping in. And that’s obviously a big part of its pitch: if it’s good enough for OpenAI, one of the most valuable private companies in the world, whose reputation depends entirely on people trusting what it builds, then it surely must be good enough for anyone else?

Whether it is, or isn’t, remains to be seen. But the company has a handful of early design partners on board, including [BBVA](https://en.wikipedia.org/wiki/Banco_Bilbao_Vizcaya_Argentaria), [SoftBank](https://en.wikipedia.org/wiki/SoftBank_Group), and [IAG](https://en.wikipedia.org/wiki/Insurance_Australia_Group). And it’s clear this is still far from a full rollout — it’s not yet available as a self-serve product, which is one such signal. Access, for now, is limited to eligible enterprise customers through a restricted rollout, with deployments handled directly by OpenAI’s own “forward deployed engineers” and a small number of global systems integrators.

Presence isn’t OpenAI’s only move on this front. The launch lands a month after the ChatGPT-maker, alongside tech titans including Google and Microsoft, [founded the Appia Foundation](https://thenewstack.io/google-microsoft-and-openai-join-forces-to-help-create-ais-missing-trust-layer/), a Linux Foundation effort to give companies a standardized way to demonstrate their AI systems meet safety and compliance obligations, as opposed to relying on self-declared claims.

Where Appia is building industry-wide paperwork for proving an AI system can be trusted, Presence is OpenAI trying to prove it one customer at a time.

## The forward deployed engineer: AI’s trust layer

Zooming out, Presence’s dependence on OpenAI’s own engineers is itself part of a broader trend, with tech companies embedding technical staff directly with a customer to design, build, and support an AI system on-site rather than handing over an API and walking away.

As *The New Stack* has [previously reported](https://thenewstack.io/forward-deployed-engineer-fde-openai-google/), the “forward deployed engineer” (FDE) exploded into one of the industry’s most sought-after jobs within the space of about ten days in May, with OpenAI [launching](https://openai.com/index/openai-launches-the-deployment-company/) its own $4 billion company built entirely around staffing enterprises with these engineers, and Google posting dozens of openings with salaries reaching into the mid-six-figures. AWS, meanwhile, [announced in June](https://thenewstack.io/aws-forward-deployed-engineering/) that it was putting $1 billion behind a similar team of its own, embedding engineers directly with customers to help build and run AI systems using the customer’s own data and infrastructure.

> “It’s easy to make an AI agent. The hard part is making an AI agent which can be trusted to speak directly with customers today and which will adapt as needs change.”

[Colin Jarvis](https://www.linkedin.com/in/colin-jarvis-50019658/), OpenAI’s global head of forward deployed engineering, took to LinkedIn on Wednesday to explain that Presence grew out of OpenAI’s FDE team working directly with its own product team to solve a recurring problem in customer deployments.

“A lot of our most challenging customer work begins with external-facing use cases where agents need to be robust to changing customer behavior, business policy shifts and external compromise,” Jarvis writes.

What that points to is trust: a company handing an agent its phone lines wants to know a person who understands both the system and the business is standing behind it, not just a model running unsupervised.

[Zach Parent](https://www.linkedin.com/in/zachary-parent/), a forward deployed engineer at OpenAI, [explains](https://www.linkedin.com/feed/update/urn:li:activity:7485690824257712128/) on LinkedIn that the difficulty has now shifted from building an agent at all, to building one a company will actually let near its customers as its needs keep changing.

“These days, it’s easy to make an AI agent,” Parent writes. “The hard part is making an AI agent which can be trusted to speak directly with customers today and which will adapt as needs change.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)