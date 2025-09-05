For years, APIs were built with a clear consumer in mind: a human developer on another team who could interpret documentation, handle inconsistencies, and ask questions in a shared Slack channel. But AI agents are now emerging as primary API consumers, and they lack the intuition or “tribal knowledge” to fill in the gaps of a poorly designed contract.

And this creates an urgent, strategic problem for technology leaders. The internet is full of [tutorials that explain the technical steps to generate](https://thenewstack.io/prompt-engineering-get-llms-to-generate-the-content-you-want/) a Model Context Protocol (MCP) server from an OpenAPI specification, but simply running a tool isn’t a strategy. The distinction between a merely functional API and one that is truly effective for AI interaction lies within the quality and semantic richness of its underlying specification.

“An effective MCP server, the kind that allows an AI to reason and act reliably, is born from a spec that is far more than just functional,” comments [Steve Rodda](https://www.linkedin.com/in/steverodda), CEO of [Ambassador](https://www.getambassador.io/), an API development platform helping developers to develop, test, mock, and deploy API services.

“The real question is whether your APIs are truly ready for this new, autonomous world,” Rodda reasons, adding that organizations must critically evaluate the readiness of their existing APIs — and the code that underpins them — for this new era of autonomous consumption.

To gain a comprehensive understanding, we consulted with prominent technology leaders across the industry, seeking their insights into overlooked details, entrenched habits that require change, and the cultural shifts necessary to transition from a human-first to a machine-centric API strategy. Their collective insights provide a practical roadmap for what comes after you generate the spec.

## Why Context Is Crucial for Your API Specification

The push for effective [MCP in agentic AI](https://optimizing.cloud/model-context-protocol-mcp-application-agentic-ai-development/) is gaining traction because it solves critical and expensive business problems, particularly around the time and complexity of customer onboarding. [Mayank Bhola](https://in.linkedin.com/in/mayankbhola), co-founder and Head of Product at [LambdaTest](https://www.lambdatest.com/), an AI-native testing platform, shares a direct example of this.

For one of their products, the manual back-and-forth to configure a new customer’s setup could take anywhere from hours to two weeks. By developing an MCP that intelligently scans the customer’s project and automatically generates the necessary configuration, he says, “that entire two-week onboarding process is now reduced to less than an hour.”

This proves that well-designed, context-aware interactions through MCP are far beyond the capabilities of traditional REST APIs — elevating business efficiency and customer satisfaction.

So what separates a specification that an AI can merely parse from one it can truly understand? The consensus from most engineering leaders is that context is everything. Because an AI agent can’t infer intent or ask for clarification, the spec itself must do all the work, shifting from a simple technical contract to a rich, descriptive guide.

And that starts with treating the AI like the newest member of your team, one who has immense talent but zero institutional knowledge. It requires a level of descriptive clarity that many teams overlook, as an AI can’t fill in the blanks.

[Rohan Gupta](https://www.linkedin.com/in/swarnendurohan-gupta/), principal product manager at [Harness](https://www.harness.io/), drives this point home, stating that “AI agents need clear and consistent parameters like precise descriptions, schema examples, and well-defined error codes. Unlike humans, AI agents can’t infer or fill in the blanks. Context is everything.” This means teams must get into the habit of mandating that every single API parameter, field, and error code includes a detailed, human-readable description and a concrete example, as if they were explaining it to a developer seeing your system for the very first time.

This need for semantic clarity extends beyond mere descriptions and applies directly to the data being transmitted. For example, while a “check-the-box” MCP server can technically serve API calls, that is not enough for an AI agent. An API field called status with values of 1, 2, or 3 is meaningless unless explicitly documented with what those values represent. The most effective way to enforce this is to implement a linting rule in your [CI/CD pipeline that flags any API](https://thenewstack.io/solving-api-integration-and-aggregation-with-supergraph/) parameter using numeric or abbreviated codes unless it has a corresponding, exhaustive list of all possible values and their explicit meanings.

But it’s not just about describing the data; it’s about giving your API endpoints purpose. You might need to think of your specification less like a raw interface contract and more like a well-organized catalog of capabilities. Developers might find it helpful to give each operation a unique, verb-based name (e.g., listAllTodos rather than just list) and a clear description of its purpose. A good first step here is to establish an API governance policy that requires all endpoint operations to be verb-based and highly specific, clearly stating the action they perform and the resource they act upon.

This points to a fundamental shift in the design philosophy behind APIs. [Aron Semle](https://www.linkedin.com/in/aron-semle-9a837910/), chief technology officer at [HighByte](https://www.highbyte.com/), uses a powerful analogy, commenting that low-level CRUD APIs are like “giving AI access to Legos and asking it to build a house: It might pull it off, but it will have a lot of latitude and room to hallucinate.” And such poorly structured APIs don’t just confuse agents; they directly increase the risk of incorrect actions or hallucinated API sequences. This should push organizations to prioritize the creation of higher-level, composite API endpoints that align with common user goals, even if they orchestrate multiple granular, internal CRUD operations behind the scenes.

For APIs in high-stakes environments, this context must also extend to operational rules. As [Giorgio Regni](https://www.linkedin.com/in/giorgioregni/), chief technology officer of [Scality](https://www.scality.com/), points out, many specs lack “built-in atomic operations for transaction-like interactions” and “context-based dynamic permissions to protect sensitive data.” To solve this, organizations should involve their security and platform engineering teams directly in the API design review process, ensuring that specifications include explicit definitions for transactional integrity and implement the principle of least privilege.

All these points ladder up to a single, critical question. The core challenge is not just adding a few more descriptive fields, but fundamentally rethinking what it means to design an API in the first place. Rodda underscores that the focus must shift from simply documenting an endpoint to designing a rich, context-aware contract that provides the AI with all the instructions it needs to act effectively and safely. This makes it imperative for leadership to establish “AI-readiness” as a formal sign-off criterion in the API design and review process, complete with a checklist covering semantic clarity, task orientation, and operational safety.

## Legacy Habits and Practices That Confuse AI Agents

Building a high-quality specification is only part of the solution; organizations must also actively unlearn legacy design habits that, while suitable for human developers, create significant issues for autonomous agents. Practices that were once acceptable shortcuts or minor inconveniences for developers are now significant roadblocks for AI agents who take every detail literally.

First is the habit of building overly generic, “kitchen sink” endpoints. Developers often create a single, flexible endpoint for updating a large object, assuming the calling developer will know which fields are safe to update in combination. But for an AI, this flexibility is a trap, forcing it to guess at valid operations and potentially break things.

[Nandita Giri](https://www.linkedin.com/in/nandita-giri-14225025), a Senior software engineer at [Microsoft](https://www.microsoft.com/), points this out with the example of an updateCustomer endpoint that “allows arbitrary partial updates on a large object.” She explains that this is bad because “agents must guess what is safe and valid to update.” Instead, her advice is to break operations into targeted, explicit endpoints like updateCustomerEmail or updateCustomerAddress so the agent’s task is unambiguous.

There’s also the related habit of exposing too much, creating a noisy and overwhelming surface for the AI. In a rush to provide transparency, teams might map every internal function to an AI tool, but this can be counterproductive.

According to [Ravi Teja Thutari](https://www.linkedin.com/in/ravitejathutari/), lead software engineer at [Hopper](https://hopper.com/), this “naïve, one-to-one mapping of each REST endpoint into an AI tool can overwhelm an LLM,” making it difficult for the model to choose the right action from a sea of low-level options. The better approach is to curate and abstract where possible, grouping related functions or exposing only higher-level workflows that are relevant to the agent’s goals.

And there is a very practical, economic reason to be concise. Every piece of context returned by the MCP server is added to the LLM’s context window, which has real performance and cost implications. “All the context returned with the MCP is added to the LLM context, that means it needs to be short and sweet, returning long descriptions is both costly in terms of tokens and can cause the LLM to overflow,” cautions [Tal Lev-Ami](https://www.linkedin.com/in/tallevami), CTO and co-founder of [Cloudinary](https://cloudinary.com/). This forces teams to be ruthless in their editing, ensuring every description and every tool exposed serves a direct purpose for the task at hand.

Another bad habit is writing lightweight specs with the assumption that a human will manually build the bridge between systems. For years, teams have relied on other developers to write adapters or “glue code” to handle undocumented fields or inconsistent behaviors. But AI agents can’t do this. Gupta explains that this leads to “lightweight specs and brittle adapters that AI agents can’t meaningfully reason about.” To break this habit, teams must shift their mindset and start designing APIs as if they are the complete, final interface, with the spec serving as the single, unassailable source of truth.

A frequent symptom of this incompleteness is the lack of proper data handling for large result sets. Regni of Scality notes that a “lack of pagination can result in long wait times and unnecessary load on both servers and agents while potentially causing timeouts and memory issues.” For any API that might return more than a handful of results, building robust, well-documented pagination is no longer an optional [feature but a core requirement for creating](https://thenewstack.io/challenges-of-creating-a-decentralized-open-source-twitter/) a stable and reliable AI-ready service.

While it’s important to consider what AI can’t do, it’s far more dangerous to overlook the new security vulnerabilities that arise from using it. As the adoption of MCP servers grows, security is exceedingly important because LLM vulnerabilities—such as [prompt injection attacks](https://thenewstack.io/when-prompt-injections-attack-bing-and-ai-vulnerabilities/), data poisoning, and supply chain issues—are a growing concern for organizations.

At [LambdaTest](https://www.lambdatest.com/), the engineering teams take a proactive approach to this challenge. Bhola shares that they run their MCP servers remotely, a strategy that ensures customer data is moved to more secure protocols and never leaves the local system. This calls for a “security-first” mindset in API design, where teams must actively scan for and mitigate new risks like tool poisoning or privilege management issues.

These issues are often symptoms of a deeper cultural problem in how software has been developed. These bad habits persist because the specification is often treated as an artifact generated after the real work of coding is done, rather than a primary design document.

When people fail to create or use good OpenAPI specs from the start, “the resulting MCP server is not good,” Rodda points out. The only way to truly fix these habits is to treat the design and maintenance of the API specification with the same rigor and importance as the application code itself.

## Closing the Gap From Existing Code to an Effective Spec

Avoiding bad habits in new APIs is one thing. But what about the decade or more of existing, mission-critical APIs that were written as code first, with documentation as a distant afterthought? For most established organizations, this is the most significant hurdle they face, and it’s a problem that can’t be solved by simply pointing a tool at a Git repository.

And this is because the foundational element — a high-quality, up-to-date specification — often doesn’t exist at all. This is the central challenge that Rodda identifies for most enterprises. He asks the critical questions: “What about all the stuff that you don’t have specs for? So many APIs are just code. If you can’t get it from code to spec, then you’re not going to be able to use one of those tools anyway.”

This highlights the urgent need for a new class of tooling that can bridge this gap. And it’s why, with solutions like the [Blackbird](https://www.getambassador.io/products/blackbird/api-development), the approach at Ambassador is to enable teams to go directly “from code to an MCP server,” generating the necessary specification as a core part of the modern API workflow.

But even after that initial spec is generated, the real challenge is keeping that spec perfectly synchronized with code that is constantly evolving. Giri, speaking from her experience working on AI agent frameworks and enterprise API integration at Microsoft, highlights the “maintenance gap,” where undocumented changes create a divergence between the spec and the API’s actual behavior.

For a human developer, this is an inconvenience; but for an agent that trusts the spec literally, she says, “it’s fatal,” warning that this drift also damages faith in the agent’s performance, because “once an agent fails due to spec-code drift, it’s very difficult to regain user trust.” And this makes it essential for teams to add automated CI pipelines that perform contract testing, verifying that live API behavior always matches what’s in the spec before changes ever reach production.

The hurdle is also one of translation, because legacy [code rarely contains](https://thenewstack.io/terraform-beta-supports-multicloud-complex-environments/) the semantic business logic that an AI needs to understand intent. You can generate a spec from code, but that spec will be just as cryptic as the code was.

The hardest part is “retrofitting semantic transparency and intent-exposing controls across every endpoint,” says [Nic Adams](https://www.linkedin.com/in/nxadams/), co-founder and CEO at [0rcus](https://0rcus.com/). The process cannot be fully automated; it requires a dedicated effort from product managers and domain experts to manually enrich the generated spec with the business context and purpose that the code alone cannot provide.

Closing the AI-readiness gap means creating a living, breathing connection between the three key elements of your system. According to Gupta of Harness, the real work is “tightening the feedback loop between the spec, the code, and the actual runtime behavior of the API.” To actualize this, organizations must invest in tools that can monitor live API traffic to surface inconsistencies and establish automated standardization processes. This reduces developer toil while ensuring the API behaves predictably for its new AI consumers.

## Rewiring Your Company Culture for an Agentic World

Solving the technical hurdles of legacy code is a critical first step. But to truly capitalize on this new paradigm, organizations must look beyond the code and address the single most important factor: their culture. The rise of AI agents requires a fundamental change in how teams think about, build, and value their APIs.

And it starts with a profound shift in mindset. For years, APIs were built for other programs, but now they are being built for collaborators that can reason and operate autonomously. Gupta argues that to gain the most benefit, organizations need to start “recognizing AI agents as operators and collaborators, not just backend automation tools.” This requires treating AI as a primary user from day one by involving AI/ML specialists in the API design phase and defining success metrics based on agent performance, not just API uptime.

If the AI agent is the new core user, then the [API specification for AI](https://optimizing.cloud/your-ai-needs-machine-readable-api-specifications/) effectively becomes its user interface. This elevates the spec from a simple piece of documentation to a central product that requires dedicated investment.

Thutari of Hopper emphasizes that in an AI-driven world, engineering teams must “treat the OpenAPI spec as the true source of intent,” because for an agent, it is the product. To make this a reality, teams must give spec maintenance the same priority as feature development, with dedicated ownership, rigorous peer reviews, and versioning managed like production code.

This process shift naturally requires breaking down old organizational structures. Code-first development often creates silos, but an AI-centric model demands constant, high-velocity communication between teams. Adams of 0rcus argues for “disposing of code-first silos” and instead restructuring engineering around “continuous spec validation, cross-discipline design reviews, [and] adversarial model-in-the-loop testing.” This means forming cross-functional pods that include platform, API, and AI agent teams, and mandating rapid feedback loops between them to convert APIs into living, self-adapting contracts.

Even the very definition of quality assurance must evolve. Because large language models are non-deterministic, you can’t test an AI-driven system with the same pass/fail logic used for traditional software. “When an application uses a large language model, you can’t ‘test’ it in the traditional, deterministic sense… The term testing no longer holds good; this is where the term ‘evaluation’ comes into play,” Bhola explains. This cultural change requires both engineering and QA teams to move beyond simple test cases and instead build robust evaluation frameworks that can assess the quality and safety of non-deterministic AI outputs at scale.

But this shift shouldn’t be viewed as a burden; it’s an opportunity to democratize development. By making tools and systems accessible to AI, you also make them more accessible to a wider range of people. Lev-Ami of Cloudinary sees this as a chance to move “beyond dev-only or dev-first,” creating a more inclusive set of tools where “the creator ecosystem has broadened” to include both agents and a wider set of human users. Leadership can champion this by creating internal platforms and educational resources that empower roles outside of core engineering to participate in building AI-driven workflows.

This cultural shift from treating APIs as a technical implementation to a core business product is the key to unlocking value. This is precisely “why AI makes APIs and specifications so much more important,” says Rodda, arguing that in this new world, embracing a culture of “specification-based development is critical,” as the quality of the spec directly determines the effectiveness and potential of any AI that consumes it.

## How AI Is Breaking Traditional API Versioning

This new, collaborative relationship with AI agents doesn’t just change how APIs are designed; it fundamentally breaks the traditional models we’ve used for managing their entire lifecycle. The familiar v1, v2, v3 progression feels slow and rigid in a world where AI-driven workflows need to adapt in real time.

And this requires a new mental model for managing change. It’s no longer just about avoiding a breaking change that will crash an app; it’s about providing a stable and predictable experience for an AI collaborator that is constantly learning and reasoning. Teams will need to “treat changes to APIs like changes to UX,” says Lev-Ami. He notes that making unpredictable changes “won’t just break an app, they will confuse the agent.” This means API changelogs and update announcements must be written with this new audience in mind, clearly explaining not just what changed, but why, and how it might impact an agent’s decision-making process.

The stakes are higher because agents often operate across multiple APIs from different providers to complete a single task. A change in one place can cause a domino effect. According to Gupta, this means versioning can no longer focus solely on backward compatibility within a single service; it must also “preserve contextual continuity across different toolchains.” Your API governance strategy must therefore expand to include cross-system impact analysis, ensuring a version change in one API doesn’t lead to unexpected failures in an agent’s complex, multitool workflow.

This complexity is pushing the industry towards a more fluid, granular approach. The monolithic version is simply too coarse-grained for agents that may want to mix and match features. Giri says the future is “capability-based versioning,” where [APIs advertise granular features](https://thenewstack.io/using-apis-with-low-code-tools-9-best-practices/) like supportsSegmenting=true. This allows for “fine-grained deprecation” of individual fields instead of killing an entire version. Teams can start experimenting with this today by using feature flags and metadata tags in their API responses, which allows agents to query for specific capabilities at runtime rather than being locked into a static version.

This future requires a renewed focus on process and stability. Enterprises [must refine their API governance](https://thenewstack.io/api-governance-a-must-for-well-regulated-industries/) and focus on “implementing gradual deprecations rather than abrupt breaking changes,” Regni advises. This means lifecycle management must now include a formal, [data-driven deprecation policy where API usage is carefully monitored](https://thenewstack.io/agentic-ai-is-coming-but-can-your-data-infrastructure-keep-up/), and teams provide long-term support with clear timelines to give developers of AI agents ample time to adapt.

So, where does this all lead? In the most forward-looking vision, the entire concept of versioning could become obsolete. Semle imagines a future where a sufficiently intelligent AI makes versioning irrelevant, as it can “work with a new or updated tool set like it did before to accomplish a task.” But he tempers this with a dose of reality, noting that hallucinations are still a challenge. While we may not be there yet, this vision should encourage architects to design for maximum flexibility, knowing that the ultimate goal is an intelligent system that can adapt to change without human intervention.

## Preparing Your Organization for the New API Economy

The journey to AI-readiness is clearly about more than just technology. It’s a fundamental shift in philosophy. The insights from these leaders point to APIs evolving from simple contracts to becoming rich, contextual guides for AI collaborators. It’s a move away from a code-first culture where specs are an afterthought, and toward a design-centric culture where the spec is the product.

And so, before your organization can capitalize on this future, it must take an honest look at its present. For any established enterprise, the path begins by answering the foundational questions that Rodda of Ambassador insists leaders must ask. The most important first step is a frank assessment of your assets to determine, “Is your spec what it needs to be to get to an MCP server? And what if you have code and not a spec?” The answers to these questions will dictate your strategy and reveal the critical importance of having a strong bridge from your existing code to the AI-driven future.

The effort invested in this transition will be a defining factor in the next tide of competition. The companies that thrive will be those that embrace this new reality and build their services accordingly. As Giri of Microsoft so aptly concludes, “As AI agents become the primary API consumers, clarity, consistency, and machine-readability will define the winners.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/11/f50df1b2-headshot-600x600.png)

Saqib Jan is a technology analyst with experience in application development, FinOps, and cloud technologies.](https://thenewstack.io/author/saqib-jan/)