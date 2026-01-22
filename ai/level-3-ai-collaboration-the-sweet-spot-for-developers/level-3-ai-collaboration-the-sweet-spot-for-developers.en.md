*This is an excerpt from Chapter 5 of [“AI for the Enterprise: The Playbook for Developing and Scaling Your AI Strategy,”](https://thenewstack.io/ebooks/generative-ai/ai-for-the-enterprise-the-playbook-for-developing-and-scaling-your-ai-strategy/) a new ebook by acclaimed tech journalist [Jennifer Riggins](https://www.linkedin.com/in/jkriggins) and sponsored by [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) and [Intel](https://www.intel.com/content/www/us/en/now/data-centric/overview.html?utm_content=inline+mention).*

*From the advantages of using the “two-speed” AI investment model to measuring the real impact of AI, this free book, [now available for download](https://thenewstack.io/ebooks/generative-ai/ai-for-the-enterprise-the-playbook-for-developing-and-scaling-your-ai-strategy/), helps enterprise leaders create an AI strategy to unlock productivity gains, solve previously impossible problems and gain a true competitive edge.*

---

## How Much Should AI Really Be in Charge?

This may change dramatically in the next year or two, but for now, your enterprise must decide — at the organization level, at the use case level and at the team level — how much autonomy you want to give AI. Generative AI (GenAI) still leaves a lot of control with the user — except maybe in public-facing chatbots — but, as you move into coding agents or even swarms of agentic AI, this changes.

“The two extremes are: Let everything be done by AI, [or] let everything be done by hand,” software engineer and technical lead [Peter Szel](https://www.linkedin.com/in/peterszel/) said. “But there are multiple levels where, in the middle, for example, I define the architecture, I define the patterns and practices I want to follow, and I create the plan,” while AI acts on these things.

Szel has identified [five levels of AI delegation](https://agentcommander.academy/blog/5-levels-of-ai-delegation?utm_source=ebook&utm_medium=referral&utm_campaign=Series13Book2) that aim to help enterprises get past the binary of “AI versus no AI”:

* **Level 1 – Manual coding:** Especially for critical systems or when an engineer is learning something new.
* **Level 2 – Target assistance:** Ask AI for single functions or classes.
* **Level 3 – Step-by-step collaboration:** An engineer creates the plan, AI reviews and iterates on it, and then asks for approval for each task.
* **Level 4 – Plan then execute:** The engineer defines the problem, then AI creates a plan. The engineer then refines it and the AI executes it autonomously.
* **Level 5 – Vibe coding:** The engineer writes prompts in natural language, and the AI writes and executes the code without review. This works best for brainstorming and rapid prototyping.

The first two levels aren’t as fast, he remarked, but your team retains architectural oversight. The last two levels definitely move faster, but even the engineer is unlikely to know the implementation details, which makes it much harder to find issues.

Szel contends that Level 3 is the “sweet spot,” where the developer retains architectural oversight but delegates the grunt work.

Everything also depends on the engineer’s experience. A junior to mid-level developer, who must optimize for learning, should avoid Level 5 and focus on Levels 1 and 2. It’s more important to get in the habit of “harshly critiquing” the AI-generated code:

1. Try to come up with why it would fail.
2. Think about similar or alternative approaches.
3. Consider how this code fits into the overall application architecture.

Level 4 is different from [specification-driven AI development](https://thenewstack.io/what-is-an-ai-native-developer/?utm_source=ebook&utm_medium=referral&utm_campaign=Series13Book2), where the spec is the single source of truth and the AI agent executes. Szel argues that spec-driven development takes away the creative work of engineering.

“The idea of working just on specification and letting the agent generate the code sounds horrible to me,” he said. “Even though it might work, I don’t really want to work on specifications eight hours a day.”

Additionally, spec-driven development, he argues, will require developers to maintain not just more code, but more specifications, too.

Be sure that your engineers and data scientists curate the context window for your developers. This includes the codebase or code files you are working with, along with the coding and architectural guidelines — anything you need the large language model (LLM) to be aware of when you assign it a task, Szel said.

If engineers leave the context window empty, he warned, the LLM will surely hallucinate. But if the context window is too cluttered, the LLM will have difficulty figuring out what to do.

Then, he continued, ask the coding agent to test its results by trying to run the code itself.

Szel “asks the agent to start with creating the automated tests first, and that’s something I review before they even get started.”

This offers several advantages, he said, because “if they can write a correct test, it means that they at least understand the problem they are solving, and then they can go ahead and implement. Then, after they’ve implemented the new feature or they fix the bug, they can run the test themselves and check whether they actually fixed the bug or implemented the feature.”

---

*To continue reading, download [“AI for the Enterprise: The Playbook for Developing and Scaling Your AI Strategy”](https://thenewstack.io/ebooks/generative-ai/ai-for-the-enterprise-the-playbook-for-developing-and-scaling-your-ai-strategy/) today!*

[!["AI for the Enterprise" ebook cover](https://cdn.thenewstack.io/media/2025/11/d43d23b4-redhat-ebook-heroimage.png)](https://cdn.thenewstack.io/media/2025/11/d43d23b4-redhat-ebook-heroimage.png)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)