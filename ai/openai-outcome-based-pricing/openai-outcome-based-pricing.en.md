**AI companies have always charged customers** for the tokens they use, whether the model gives them exactly what they need or completely misses the mark. Now, OpenAI is experimenting with a different approach by allowing customers to pay only when the AI gets the job done right.

First reported by [*The Information*](https://www.theinformation.com/briefings/openai-starts-letting-customers-pay-ai-works), the company has already started testing that approach with some enterprise customers, billing them based on successful outcomes rather than simply the amount of compute consumed along the way.  
  
OpenAI has not publicly disclosed pricing or exactly how it determines when a particular task counts as a success. Still, the approach presents an interesting technical challenge for developers building AI agents. If a customer only pays when an agent completes a task, someone needs to determine exactly when that task is complete. As we know, determining if an AI agent succeeded is more complicated than counting tokens.

## Counting tokens, not success

Some outcomes are easy for software to verify, such as a support ticket closing without human involvement, but other jobs leave room for interpretation. For example, take a coding agent asking to fix an authentication bug. It might rewrite the code and pass every test, only for the patch to cause another problem once it reaches production. In that case, the agent technically completed the task, but the customer probably wouldn’t consider it a successful outcome.

> With outcome pricing, getting through 90% of a task may not be enough for the run to count as billable.

The same issue arises with longer-running agents that interact with browsers, databases, APIs, and other systems. An agent may carry out nine of the ten steps before failing at the last one. With token pricing, all of that activity can still be charged for. With outcome pricing, completing 90% of a task may not be enough for the run to be billable.

## Evals become billing infrastructure

Developers already use evals to catch problems with models and agents. OpenAI’s hosted tools, for example, can check responses against expected results and grade a model’s performance on a given task.

Braintrust adds visibility into what happens during an agent run. It records model calls, retrievals, and tool calls in a trace, then scores the run on factors such as task completion, factual accuracy, and correct tool use. Developers can also turn those traces into datasets for future testing.

Some results are easy: a unit test either passed or it didn’t, an API returned the expected response, or a database contains the record it was supposed to create. There isn’t much room for debate.

> It records model calls, retrievals, and tool calls within a trace, then scores the run for things like task completion, factual accuracy, and correct tool use.

Semantic evals are different because they require a judgment rather than a pass/fail. An [LLM-as-a-judge](https://thenewstack.io/bionic-shell-command-safety/) can help developers compare two versions of an agent, but using that judgment to trigger a charge is another matter. A false positive could leave a customer paying for unfinished work, while a false negative could leave the vendor covering the cost of a successful run.

## Grading your own work

When an AI company runs the agent and sets the criteria for success, it is effectively [grading its own work](https://thenewstack.io/google-double-blind-evaluation/) and then billing the customer for the result.

That gets trickier with more subjective work. Asking an agent to generate a monthly sales report gives you something you can check. But asking it to generate a good one is different because someone still has to decide whether the result is actually any good. And if the goal is to improve conversion rates, figuring out how much of that improvement is attributable to the agent is even harder.

There’s also the question of who gets blamed when something outside the agent fails. An agent might handle a support request correctly only to hit a timeout in the customer’s CRM. A coding agent could finish its work but fail because a separate service is unavailable. If those runs don’t count as successful, the vendor could end up paying for failures it didn’t cause.

## Failed agents shrink margins

Outcome pricing changes who pays when an agent fails. Under token pricing, an agent can burn through tokens and retry failed steps without ever finishing the job. The customer still pays for that usage.

> If it never finishes, the provider has spent money on compute without anything to bill.

If the customer pays only for successful outcomes, failed runs become the provider’s expense. An agent that completes a task on its first attempt is more profitable than one that requires 20 model calls and several retries. If it never finishes, the provider has spent money on compute resources without anything to bill for.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)