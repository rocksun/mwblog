**When Nvidia announced [NOOA (Object-Oriented Agents)](https://developer.nvidia.com/blog/six-agent-harness-capabilities-for-higher-model-performance/) last week**, it signaled a broader shift in agent development: The harness around a model may matter as much as the model itself.

Nvidia is contributing NOOA to the [Open Secure AI Alliance](https://thenewstack.io/open-secure-ai-alliance/), the [much-written-about industry group](https://www.google.com/search?q=%22open+secure+ai+alliance%22&sca_esv=fc15e49dbd266fb4&tbm=nws&sxsrf=APpeQnsnb-qNSpvEszrXHberS6Qb9HFlVA:1785851699526&tbas=0&source=lnt&sa=X&ved=2ahUKEwjiwq-BkIeWAxUEODQIHTWWMusQpwV6BAgFEBE&biw=1178&bih=860&dpr=2) Nvidia formed last week to build and share open-source and open-weight tools for AI development.

NOOA is founded on one idea: An agent is a single Python class. Here is how Nvidia describes it in its announcement blog post:

*“Its methods are its capabilities. Its fields are its state. Its docstrings are its prompts. Its type annotations are enforced contracts. A standard Python method whose body is an ellipsis (…) is completed at runtime by an LLM-driven loop. Method with a normal body run as ordinary, deterministic Python.”*

By bringing an agent’s capabilities, state, and prompts together in one Python class, Nvidia is working to solve the thorny problem that is fragmentation in agent development.

It’s an issue that [Adnan Masood](https://www.linkedin.com/in/adnano/), Ph.D., chief AI architect, [UST](https://www.ust.com/), sees regularly.

“The harness is everything wrapped around the model,” Masood tells *The New Stack*. “Today it is scattered by design. A team building on LangGraph or AutoGen typically has prompts in Jinja templates, tool definitions in JSON schemas, callbacks in Python, and the workflow drawn as a graph in yet another abstraction.”

## Can one Python class make agents easier to test?

Nvidia’s idea is to make agent development more like traditional software development so both humans and AI coding agents can inspect and manage an agent with familiar coding tools, thereby making it simpler to test and trace agent behavior.

Masood believes that Nvidia is taking a meaningful step by wrapping capabilities, state, and prompts into a single Python class with NOOA. But other experts are more skeptical.

[Karthik Karunanithi](https://www.linkedin.com/in/karthikkarunanithi/), solution architect, [IBM](https://www.ibm.com/us-en), agrees that corralling workflow graphs, prompt templates, schemas, and callbacks into one Python class is a real improvement, but he also tells *The New Stack* that he wonders if doing so will introduce a new review problem because “inside that class, one method with `...` is completed by a model at runtime, while the next method is just ordinary Python.”

Since both have the same signature, indentation, and docstring, Karunanithi questions whether it may be harder to distinguish between deterministic code and probabilistic behavior.

When asked how NOOA could help with testing and tracing agent behavior, [Siddhartha Saxena](https://www.linkedin.com/in/siddsax/), co-founder of [Thine](https://www.thine.com/) and [Merlin AI](https://www.getmerlin.in/), gives Nvidia points for using typed input/output within the single Python class to bring structure to agent calls.

Saxena tells *The New Stack* the challenge comes when activity scales to millions of tool calls. For this reason, he considers testing agent traces largely an observability problem and not something a framework like NOOA can solve on its own.

## More inspectable agents, but new execution risks

Bringing an agent’s capabilities, state, and prompts into one Python class may make it easier to inspect its behavior. But centralizing logic in one place also raises new questions about security.

> “An agent whose state is readable and whose runs leave one inspectable trace is far easier to audit than logic smeared across prompt files and scattered scripts.”

Big picture, Saxena sees centralization as a net benefit, saying it makes agent code more readable and maintainable. Still, he points out that that readability may come with a tradeoff: “Obviously, if something is readable for humans, it means it’s readable for aliens, as well.”

When asked whether centralizing agent logic improves security or creates new risks, Masood seems to agree with Saxena’s take, telling *The New Stack* both things can be true:

“An agent whose state is readable and whose runs leave one inspectable trace is far easier to audit than logic smeared across prompt files and scattered scripts.”

But a separate risk that may come with NOOA, Masood adds, is the framework’s use of code as action, which allows the model to act by writing and running Python. “That is powerful,” he explains, “and it widens the blast radius of a prompt injection, where malicious text in a document or webpage steers the model.”

Karunanithi echoes that tradeoff, acknowledging that centralization makes agent logic easier to understand but also concentrates risk. Like Masood, he highlights the need for sandboxing, along with scoped credentials and separate identities for each agent.

It’s worth noting that for production deployment, Nvidia pairs NOOA with the [Nvidia OpenShell](https://developer.nvidia.com/blog/run-autonomous-self-evolving-agents-more-safely-with-nvidia-openshell/) secure runtime.

## Nvidia claims “double-digit” benchmark swings

Nvidia explains its NOOA release by arguing that harness design has a major role in agent performance, stating: “Harness design alone can account for double-digit swings in benchmark results and significant differences in token cost, with the same underlying model.”

It backs up that claim with results from three benchmarks. On SWE-bench Verified, NOOA reaches 82.2% with GPT-5.5 using 29 LLM calls and roughly 1.1M tokens per task. The comparison harnesses, Nvidia says, need 66 calls and 2.2M tokens to reach 78.2% and 29 calls at 1.3M tokens to reach 78.6%. The technology company describes this result as “parity or better, at roughly half the cost.”

> “Harness design alone can account for double-digit swings in benchmark results and significant differences in token cost, with the same underlying model.”

On the vulnerability-rediscovery benchmark, CyberGym L1, NOOA solves 86.8% of tasks with GPT-5.5. It reaches 50.2% mean RHAE on ARC-AGI-3, a benchmark for general reasoning.

When asked what the framework’s benchmark results might mean for developers, Karunanithi cautions against overgeneralizing. He says SWE-bench Verified, CyberGym L1, and ARC-AGI-3 all serve as useful benchmarks because they have a programmatic oracle but notes that they differ greatly from most regulated production systems, “where nobody can tell you at runtime whether an insurance claim, access decision, or compliance judgment was actually correct.”

But it seems Nvidia is after more than better benchmark scores. As [Paul Furgale](https://www.linkedin.com/in/paulfurgale/), distinguished research scientist, Nvidia, posted to [LinkedIn](https://www.linkedin.com/posts/paulfurgale_ai-llms-agents-activity-7487524360161755136-7kvZ/):

“We did this because we believe the future of open AI depends on more than open models. It also depends on open research into how those models interact with computers.”

While Furgale says the technology company doesn’t expect everyone to adopt NOOA, it encourages the developer community to adopt, challenge, and improve its techniques.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)