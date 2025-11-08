The stakes are higher than ever for enterprises to prove that their AI agent investments are truly providing return on investment (ROI). With [studies](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/) suggesting that most [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) are failing to drive measurable business value or accelerate revenue growth, enterprise leaders are under pressure to ensure their agentic AI initiatives are worthwhile.

With these investments already in place, executive teams are now asking a [different set of questions](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/): Are these agents truly [driving impact](https://thenewstack.io/five-steps-to-build-ai-agents-that-actually-deliver-business-results/), and can they be trusted to handle critical, enterprise-grade workflows? This is where evaluation methods come into play.

The primary obstacle to trust is knowing the agent’s path to the answer. An agent’s answer may appear successful, but the path it took to get there might not be. Without visibility into these steps, enterprises risk deploying agents that may appear reliable but create hidden costs in production. Inaccuracies can waste compute, inflate latency and lead to the wrong business decisions — all of which erode trust at scale.

Unfortunately, current [evaluation practices often fall short](https://thenewstack.io/where-ai-benchmarks-fall-short-and-how-to-evaluate-models-instead/), frequently judging only the final answer, missing the agent’s decision-making process. This narrow focus overlooks the agent’s true end-to-end performance, leading companies to accept a satisfactory answer without fully understanding or being able to fix the underlying failure points in the workflow.

## **The Agent GPA Framework**

To address the lack of agent trust, enterprises should adopt a systematic evaluation framework based on three dimensions that ensure [agents are traceable and prevent hallucinations](https://thenewstack.io/agentic-ai-is-key-to-preventing-costly-ai-hallucinations/): goal, plan and action (GPA).

This three-part model is designed to break down an agent’s operation into three phases across teams, while also surfacing internal errors such as hallucinations, poor tool use or missed plan steps. This allows enterprises to [evaluate performance across every step of the agent’s reasoning process](https://thenewstack.io/ai-agentic-evaluation-tools-help-devs-fight-hallucinations/), reflecting not only the final outcome, but also the exact path taken to reach it:

* **Goal:** Did the agent’s final outcome successfully meet the objective? This measures the result for accuracy, user relevance and verifiability against source data.
* **Plan:** Did the agent design and follow a sound strategy, selecting appropriate resources for each step? This assesses the agent’s strategic intent.
* **Action:** Were the external tools or services the agent interacted with executed effectively and efficiently? This measures the agent’s hands-on execution with outside functionalities, such as data, web search, text retrieval and more.

By applying these guidelines across all three of these stages, enterprises can build trustworthy and enterprise-ready AI agents. This allows teams to not just catch failures, but to pinpoint the exact moment an error occurred for rapid corrections.

## **Goal: The Business Outcome**

The goal phase addresses the most critical question for business leaders and end users: Did the agent succeed, and is the result trustworthy? In this phase, these groups should consider:

* **Answer correctness and relevance:** Is the final answer aligned with the user’s need and the established truth?
* **Groundedness:** Is the agent’s final answer substantiated by evidence from previously retrieved context?

For example, a calendar agent could be responsible for scheduling a meeting for an executive on Friday. The agent checks the executive’s calendar and proposes a 7 a.m. Friday meeting because it sees no other open times, even though the executive has emails and a documented company policy that no meetings are scheduled before 9 a.m. When that supervising team or executive sees that the agent is not connecting the external source (email history and company policy) with the task, they can gather that the agent’s logic is incorrect. This confirms the [agent must ground its logic in all verifiable data](https://thenewstack.io/how-industries-are-using-ai-agents-to-turn-data-into-decisions/) to ensure its outcome is practical and correct, not just technically possible.

In situations like these, where the agent’s output is not grounded or if its reasoning contradicts itself, the user should immediately flag it to the managing technical teams to confirm whether the agent is producing verifiable, relevant business results that the business can actually trust.

## **Plan: The Strategic Intent**

The plan phase is where technical groups that deploy agents, like AI engineering or product teams, check their strategy and internal design before beginning work. Instead of judging the agent’s final result, these teams focus on the efficiency and logic of the algorithms. This phase is essential for mitigating future deployment risk and involves technical teams assessing:

* **Plan quality:** Did the agent design an effective, optimized roadmap to reach the goal?
* **Resource selection:** Did the agent choose the correct internal tools or functions for each subtask?
* **Logical consistency:** Are the agent’s steps coherent and grounded in prior context?

For a complex job, like analyzing market trends, the agent should first identify geographic markets and time zones, then it should choose appropriate internal sources and analytical models for data retrieval and projection. Finally, it should structure the output into a clear, comparative report format. During the plan phase, technical teams monitor whether the agent breaks the task down correctly into smaller problems and matches the right internal data to each step. These teams also make sure the agent follows the plan by executing steps in the correct order.

A solid plan means the agent has the best strategy, leading to fewer errors from bad preparation.

## **Action: The Execution Efficiency**

The action phase evaluates the agent’s actual work and resource use, connecting the initial strategy to specific, measurable performance data. This data is key for DevOps teams and controlling platform costs. Technical teams that deployed the agent should use this phase to get a detailed look at where performance slows down and how much computing power is being used. Items to consider should include:

* **Plan adherence:** Did the agent follow through on its plan? Skipped, reordered or repeated steps often signal reasoning or execution errors.
* **Tool calling:** Are the agent’s internal function calls valid, complete and parameter-correct?
* **Execution efficiency:** Did the agent reach the goal without wasted steps? This captures redundancies and superfluous resource calls, and ensures optimal resource management.

For example, teams that deployed a sales agent can observe if an agent retrieved and searched through a prospect list three times for the same market segment, unnecessarily doubling the database query cost and processing time, rather than using a simple filter by revenue tool to produce the same answer more efficiently. Deployment teams should observe the action the agent chose and make corrections to prioritize efficiency and cost savings.

By monitoring the action phase, technical teams can pinpoint where performance slows down. This keeps the agent running at its best while managing computing costs and speed, which is vital for enterprise AI.

## **From Speculative Investment to Auditable ROI**

By using this structured, three-part approach, enterprise teams across the business can better manage their AI — shifting the focus from simply accepting an answer that an AI agent gives you, to validating the entire process. By making the agent’s reasoning transparent at the goal, plan and action levels, organizations can stop guessing where failures occur and pinpoint the exact source of an error.

This degree of traceability is not just about catching hallucinations; it’s a foundational philosophy for scaling enterprise AI from siloed experiments to mission-critical, revenue-generating systems.

Embracing this framework transforms AI from speculative investment into a confident, auditable engine of exponential return on investment.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/11/04f4feb9-cropped-d21b55de-anupam-datta-600x600.jpg)

Anupam Datta is a principal research scientist and Snowflake AI Research Team Lead. He joined Snowflake as part of the acquisition of TruEra where he served as cofounder, president and chief scientist from 2019-2024. Datta was on the faculty at...

Read more from Anupam Datta](https://thenewstack.io/author/anupam-datta/)