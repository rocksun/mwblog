# Meet Embabel: A Framework for Building AI Agents With Java
![Featued image for: Meet Embabel: A Framework for Building AI Agents With Java](https://cdn.thenewstack.io/media/2025/06/e6fe4da0-java-embabbel-1024x576.jpg)
AI agents are becoming true collaborators in the workplace, [with more developers every day beginning to build them](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/). To reach their potential for your team, AI agents need to be able to pursue specific goals and execute workflow tasks, make decisions and take actions without constant human supervision. They need to learn from their interactions and adapt their behavior over time. And they need to do all this while being aware and focused on your context and your goals.

To be useful, an agent needs to balance a multitude of safe — secure and reliable — integrations. This is the battleground that dedicated tools and frameworks are beginning to wade into.

In May, Microsoft launched its [Azure AI Foundry](https://thenewstack.io/microsoft-brings-mcp-local-ai-models-and-post-quantum-security-to-windows/) to help you build, amongst other things, context-aware agents and their workflows. Postman has its [AI Agent Builder](https://www.postman.com/product/ai-agent-builder/), Open AI has its [Playground](https://openai.com/index/new-tools-for-building-agents/), the [Python ecosystem](https://thenewstack.io/building-autonomous-systems-in-python-with-agentic-workflows/) already has a rich set of agent-building libraries and tools, and dedicated [agent-building tools](https://thenewstack.io/ai-agents/) are arriving and maturing all the time.

But that still leaves us with one small gap …

Java and the JVM.

## What’s Java Doing About AI Agents?
Java is still a huge player in enterprise software development. It’s only natural that building enterprise Java applications and services that leverage AI has seen increasing investment in line with every other development ecosystem.

The [Spring AI](https://spring.io/projects/spring-ai) project has been rapidly gaining traction as a strong set of abstractions over the low-level details of LLM interactions, providing a ready set of tools to integrate AI into your Java applications and services.

But dedicated and focused support for building JVM-based AI agents has been a little thin on the ground until recently. That looks about to change with the first of what is likely to be a new set of AI agent-focused frameworks for the JVM: [Embabel](https://github.com/embabel/embabel-agent).

## What’s Embabel?
Embabel is a new open source project that looks to simplify how to create safe AI agent workflows inside, while taking full advantage of the rich Java ecosystem.

As the project’s founder, [Rod Johnson](https://www.linkedin.com/in/johnsonroda/), pointed out [in a Medium blog post](https://medium.com/@springrod/embabel-a-new-agent-platform-for-the-jvm-1c83402e0014): AI agent development requires a “new programming model” and a “higher level orchestration technology” to safely integrate with existing context, better or cheaper AI models, inject crucial guardrails, manage flow execution and give just enough deterministic control of how the agent makes its choices when completing the task you have given it.

In this way, an agent has many of the same characteristics of any enterprise codebase, i.e. multiple integrations, multiple integration styles and orchestrations across multiple sources of data of varying volume, velocity, variety, veracity and value.

Johnson originally created the [Spring Framework](https://spring.io/projects/spring-framework) to deliver a better programming model for enterprise Java. With Embabel, it is the turn of programming for AI agents.

Similarly to how Spring changed enterprise Java using a new programming model based on [dependency injection](https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-collaborators.html) and [inversion of control](https://docs.spring.io/spring-framework/reference/core/beans/introduction.html), Embabel looks to create a programming model that helps developers build agents using the same best practices that production code is usually held to, while at the same time still allowing your agents to pursue specific goals, execute workflow tasks and make their own dynamic, runtime decisions.

## Agents, Trust and Determinism
Determinism and AI models have a difficult history. When we build applications, we’re used to the application behavior being deterministic — i.e., our code, given the same input and initial state, will always produce the same output and behavior.

This is not how LLMs work. LLMs hallucinate — some would argue, so do humans — on one extreme, and on the other can respond with surprising but remarkably useful results when given free rein over their creative options.

For simple, prompt-based interactions with humans in the loop, this indeterminism can be an annoyance but not much more. But with agents, who are also closing the OODA loop (observe, orient, decide and act) completely by taking action without human interaction, determinacy of outcome becomes essential.

Building trust in your agent’s workflow requires a means of exploring the determinacy of how your agent navigates its workflow. You want to leave the door open to incredible results from an agent’s work while making sure you retain some control over how that work is navigated. To do this, Embabel turns to GOAP.

## What Is GOAP, and How Does Embabel Use It?
Embabel agents use [goal-oriented action planning (GOAP)](https://www.reddit.com/r/godot/comments/xgrk0g/goap_goaloriented_action_planning_is_absolutely/) out of the box to be able to navigate possible steps on the way to a defined goal. In Embabel’s implementation of GOAP, a goal is a step — some executable code — with a set of preconditions that have to be met before the goal can be executed.

Then there are accompanying possible steps, called actions, that have pre- and post-step conditions that are hints as to whether they should be involved in a planned path to the goal. One of Embabel’s innovations here is to declare those conditions in type-safe Java code.

Embabel assesses the goal and steps within your agent, planning a path that should meet the goal, but if at any point in the execution of the path a set of conditions are not met then Embabel will change its path.

One example of this might be a set of post-conditions to a step that worked with an indeterministic LLM might be unsatisfactory and so an alternative step might be selected, perhaps using a different LLM, to see if better results, as judged by the post-step conditions, can be obtained.

![The components of Embabel, which aims to make it easier to build AI agents in Java.](https://cdn.thenewstack.io/media/2025/06/f397190f-embabel-components-1024x690.png)
The components of Embabel.

The Embabel programming model comprises:

**Actions:**Steps an agent takes, often methods or functions, indicated by the`@Action`
attribute.**Goals:**What an agent is trying to achieve, indicated by the`@AchievesGoal`
attribute.**Conditions:**Factors to assess before executing an action or determining that a goal has been achieved. Conditions are reassessed after each action is executed.**Plan:**A sequence of actions to achieve a goal. Plans are dynamically formulated by Embabel. Embabel replans after the completion of each action, allowing it to adapt to new information as well as observe the effects of the previous action.
The Embabel programming model allows an agent’s workflow to be composed of many possible steps, demarcated with the `@Action`
attribute, along with one or more `@AchievesGoal`
annotated actions to indicate a goal.

The collection of possible steps can be deterministically navigated by the Embabel runtime based on your indicated pre and post conditions toward the defined goal, leaving the option to replan if results from steps/actions don’t go the way you need.

From a [second Medium blog post](https://medium.com/@springrod/ai-for-your-gen-ai-how-and-why-embabel-plans-3930244218f6) describing how Embabel plans, using the Embabel programming model you can “enjoy the benefit of a system that can make plans [you] never explicitly coded, but without paying the price of surrendering flow control to an opaque model. Your agents can strike a balance between determinism and the potential for new, better, even cheaper routes to the goal through the myriad of different steps that your agent could take.

If you’re coming from a JVM background, Embabel ships with some examples and instructions to kick its tires and begin to explore building your own agents for the JVM. Embabel is 100% written in Kotlin but fully embraces Java for developing your agents.

## The Future Is Bright for AI Agents
Building AI agents is in its infancy and Embabel is very early in its life. The good news is that there’s a proven track record of fast innovation in open source and Embabel is open and licensed with the enterprise-friendly Apache Software License.

You can expect things to develop in the public domain quite quickly and here on The NewStack we’ve predicted that “a lot of software engineers will become agentic process authors”. In specialty insurance and public sectors alone, [Prasad Prabhakatan](https://www.linkedin.com/in/prasadprabhakaran), head of artificial intelligence at eSynergy, told me that “we’re seeing a 30-50% shift in AI engineering work evolving towards building, orchestrating and governing AI agents.”

He added, “Our current focus with customers is on abstracting the complexity of LLMs and orchestration, making agent development accessible to mainstream developers — especially Java/Spring and .NET engineers. We’re building reusable patterns, SDKs and reference architectures that allow these teams to plug into agents without needing to be AI experts.”

## Got An Agent Story To Tell?
Building your own agents and have a story to tell? Please [reach out to me](https://www.linkedin.com/in/russmiles/) if you’re interested in sharing your stories, good and bad, of the impacts and pitfalls of this new AI engineering approach.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)