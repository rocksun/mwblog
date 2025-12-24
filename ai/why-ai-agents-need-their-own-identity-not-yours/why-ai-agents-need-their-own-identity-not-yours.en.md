AI native startups definitely serve the non-human crowd.

An AI agent can’t really have a human identity, according to [Jake Moshenko](https://www.linkedin.com/in/jake-moshenko/), CEO of [AuthZed](https://authzed.com/). That premise comes to bear when considering how AuthZed works with OpenAI and the production-scale [retrieval augmentation generation (RAG)](https://thenewstack.io/how-rag-architecture-overcomes-llm-limitations/) authorization model OpenAI has deployed.

“It’s a common misconception that you’re going to want to deploy an agent as ‘me,’” Moshenko said. “A lot of the value that people are going to try to capture out of agents are autonomous processes that run as part of your company.”

## The Problem With Tying AI Agents to Human Identities

Remember back in the day, the havoc that occurred when services shared the identity of someone who had left the company?

“If the user leaves the company or changes roles, you’re not going to want that to automatically restrict every agent they’ve ever deployed,” Moshenko said. “It’s like making a hiring decision — if I change the manager, that doesn’t mean I want all the employees that worked for that manager to just go away.”

Let’s say, though, the agents do get bound to a person.

“Just because I deployed an agent to help code review some things doesn’t mean I want that agent to be able to do Jake-like things from [a human resources] or fundraising perspective,” Moshenko said.

AuthZed’s permission model treats agents as subject types. It allows organizations to federate access for agents the same way they do for humans. Still, there are gaps.

“Just because you can see that it’s reading sensitive financial data and maybe writing some numbers back, that isn’t, in and of itself, a verification model for saying the agent is doing the correct thing,” he said. “If I bring on an accountant, I’ll open the books to them — they have to, to get their job done. But that doesn’t mean they aren’t doing something incorrect or nefarious with the books.”

Moshenko said cloud native tooling provides authorization, controlling what agents can access through permission boundaries. Cloud native tooling also provides observability, tracking what actions agents take. But verification? You can’t automatically determine if it made the correct decision.

## The Limits of Automated AI Agent Verification

But even using deterministic tools can’t necessarily make it easy. There are always human and non-human factors. Automated agent testing, using security scanning, linting, and other tools, can be foiled.

“Sufficiently clever humans can make things look totally benign that are actually quite nefarious,” Moshenko said. “Sufficiently nefarious people and/or AIs could definitely pass all of your linting tests and unit tests and integration tests, but still be doing something they’re not supposed to do.”

He cited “[Reflections on Trusting Trust](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf),” by [Ken Thompson](https://thenewstack.io/ken-thompson-recalls-unixs-rowdy-lock-picking-origins/), a Turing Award winner. The paper detailed how you can’t trust it if a compiler has already been compromised. Compilers may inject vulnerabilities that re-inject themselves when compiling the compiler itself — making them effectively undetectable through conventional testing.

“Really, it’s like hiring a human: Everything becomes ‘trust but verify,’” Moshenko said. “We do code review with people in the loop, because that reduces our exposure to nefarious activity when it has to make it through two humans instead of just one.”

## Production at Scale: The OpenAI and AuthZed Case Study

AuthZed points to its capability in [providing OpenAI](https://authzed.com/customers/openai) with the RAG authorization capability the leading large language model (LLM) provider is using. AuthZed worked wth OpenAI on its ChatGPT Enterprise Connector, which demonstrates a use case for its authorization technology, based on the Google [paper about its global authorization system, Zanzibar.](https://authzed.com/zanzibar)

“They make sure that whoever is asking about Q4 earnings actually has access to the source document that existed on Google Drive,” Moshenko said. “They’re not injecting any context that that user wouldn’t have been able to go and dredge up themselves.”

AuthZed allows OpenAI to ingest enterprise data. What happens next is key. The authorization data gets associated with the documents. At that point, before feeding the document fragments into an LLM’s context window, they verify permissions with AuthZed. Better, there is no need to check with the sources upstream. And the numbers are significant. AuthZed has processed 37 billion documents as of this fall.

And the difference with cloud native tooling is striking. Traditional systems authorize APIs. AuthZed post-filters which document enters the LLM context based on user permissions.

AuthZed provides authentication, but verifying that the agents’ behavior still does not get fully resolved without a deeper approach to validation.

[Jentic](https://jentic.com/) works on the premise that infrastructure for AI workloads is a bit like being in 1996. They connect disparate systems, working with enterprise architects who are untangling and filling gaps in their technical debt.

“I think if all LLM development stopped tomorrow, it’s going to be another five or 10 years before we figure out exactly what to do, what the best practices are, all sorts of processes and methodologies and ways of working with it,” said [Michael Cordner](https://www.linkedin.com/in/michaelcordner/), Jentic’s CTO and co-founder, in an interview with The New Stackat [AWS re:Invent](https://reinvent.awsevents.com/on-demand).

[Dorothy Creavan,](https://www.linkedin.com/in/dorothycreaven/) Jentic’s co-founder and COO, also said in an interview with The New Stack that  it’s a bit like older times when new technologies started getting adopted, but now there is no landscape for connecting the world of APIs with the work of AI. You have to have machine-readable documentation for APIs to become useful. Then you’re able to create these deterministic workflows that you can really rely on.

Said Cordner, “Part of our platform centralizes all authentication in one place … Centralized authentication and being able to observe what agents are doing.” In a lot of cases, agents are “being developed, kind of like a shadow IT organization.”

## How Intuit’s GenOS Platform Accelerates AI Adoption

At [KubeCon + CloudNativeCon North America,](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) in Atlanta, [Intuit’s service mesh team showed its proprietary GenOS,](https://medium.com/intuit-engineering/intuits-custom-llm-leaderboard-optimizing-model-selection-for-financial-use-cases-ac08d467f8f3) to accelerate AI adoption in its products. It’s an internal platform with an agent and tools registry, tracing, memory management and evaluation built in.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Intuit demonstrated how on-call debugging agents access logs, metrics, change logs, and Envoy response flags, then use RAG to match against internal documentation, root cause analyses, and architecture reviews.

Intuit has more than 350 Kubernetes clusters, 2,000 rollouts and deployments, 16 million daily transactions, and 292,000 peak transactions per second. Debugging is challenging on such a scale, to say the least.

“Working with such scale means that you are generating a huge amount of data through all the interconnected services that you have through logs, metrics and traces,” said [Kartikeya Pharasi](https://www.linkedin.com/in/kartikeyapharasi/), ​​a staff software engineer from Intuit. “In cases of an incident, you might spend a lot of time coming up with complex queries or going through documentation on the fly in a high-pressure situation.”

Pharasi said the right tool choice becomes critical. It’s almost more important than the tools themselves, “because what’s even more dangerous than not being able to do this kind of debugging is if you pick the wrong tool and the wrong kind of step is executed.”

## Why AI Agents Require Machine-Specific Interfaces

Evident? The machines need different interfaces than humans do. We see this again and again, in the interviews I conducted at AWS re:Invent with companies participating in the [AWS](https://aws.amazon.com/?utm_content=inline+mention) Generative AI startup program.

Cordner said Jentic sees agents as the future of software that runs on APIs. The problem: a mismatch between AI workloads, unsuitable infrastructure and APIs not structured for machines.

“Imagine a world where all your API layer is so well documented that AI has an easy time turning your business processes into deterministic workflows,” Creavan said. “That’s where it is.”

You see the landscape changing when considering the language barrier with deterministic systems and how it breaks down, and in some respects, makes for descriptions that better define their purpose in the organization.

“If you think about something like writing a function to undo a payment transaction, you might name that function something like `reverse_transaction` or `revert_record`,” said [Ryan Tay](https://www.linkedin.com/in/ryan-tay-8578991a9/), a software engineer at Intuit. “But a user and similarly, an LLM is not going to think of that as reversing a transaction, right? They’re going to call that something like a refund.”

It’s more about the readability that the machine needs. For instance, [LlamaIndex](https://www.llamaindex.ai/), another startup, along with Jentic, in the AWS Generative AI program, said it turns documents into tokens using RAG, deepening the context for the agents.

“The general reasoning capabilities are always improving, but the core is just better specialized context,” Liu says. “If agents understand all this stuff in a very accurate manner, all of a sudden they can actually make decisions.”

Intuit is also looking to the [Model Context Protocol (MCP)](https://thenewstack.io/why-the-model-context-protocol-won/) to share across teams.

“We’re currently looking at other teams trying to build like a full-on incident response agent that can call our tool and any other platform-specific tools,” Tay said. “The Model Context Protocol … allows the agents to talk to tools that you define, and also the tools that other teams and maybe other organizations are defining.”

The missing piece: agent-specific authorization —something AuthZed addresses but Intuit hasn’t yet implemented.

## The Future of AI Agent Management and Security

In 2025, the confusion about infrastructure for AI workloads surfaced more as companies raced to adopt AI in the enterprise. The technical debt remains in the form of human-centric APIs. That will change in the next year as teams build out evaluation frameworks, agent identity models and develop sandbox environments, among other initiatives.

Agent management will take different forms. [Adam Draper](https://www.linkedin.com/in/adamwdraper/), product design lead at Weights & Biases, talked about managing agents by breaking them down into smaller agents, while his colleague, [Ayush Thakur](http://Ayush%20Thakur), a machine learning engineer at W&B, said some companies may take different approaches.

“Some of the big labs want to have one agent which has basic tools like code execution, file system tools, etc … LLMs are really powerful to write code,” Thakur said. “A one-agent approach allows agents to have access to all the databases and systems, and to write pieces of code that execute themselves in a sandbox.

Clarity matters. “The more clear and concise you can make those prompts, the more predictable you are going to create an agent that’s functioning the way you want,” Draper said.

Sandbox isolation becomes critical. Thakur said he has never seen agents given root access. He said some companies containerize all the sandboxes so the agent can do stuff in that sandbox, and then kill it when no longer required.

Moshenko, though, said verification has fundamental limits regardless of approach.

“Sufficiently clever humans can make things look totally benign that are actually quite nefarious,” he said. “Sufficiently nefarious people and/or AIs could definitely pass all of your linting tests and unit tests and integration tests, but still be doing something they’re not supposed to do.”

Again, it all points to the need for human oversight.

“Really, it’s like hiring a human: everything becomes ‘trust but verify,’ ” said Moshenko. “We do code review with people in the loop, because that reduces our exposure to nefarious activity when it has to make it through two humans instead of just one.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/13c3d9d6-cropped-0fe18b69-ef774ac85213a6506cf973dc6380cd57.jpeg)

Alex Williams is founder and publisher of The New Stack. He's a longtime technology journalist who did stints at TechCrunch, SiliconAngle and what is now known as ReadWrite. Alex has been a journalist since the late 1980s, starting at the...

Read more from Alex Williams](https://thenewstack.io/author/alex/)