**OpenAI introduced [GPT-5.6 Sol](https://thenewstack.io/openai-gpt-56-live/) earlier this month** as a model built for more demanding coding tasks. But it didn’t take long for power users to complain that their ChatGPT Work and Codex usage limits were disappearing much faster than expected, even during jobs that appeared to spend much of their time waiting for tools to finish.

In response, OpenAI reset usage limits for ChatGPT Work and Codex users and rolled out backend inference improvements that it says should make typical Sol sessions last about 18% longer.

The update solves an immediate frustration, while exposing a fundamental shift for anyone building or deploying AI agents.

In a post on X, OpenAI engineering lead [Thibault Sottiaux](https://www.linkedin.com/in/thibault-sottiaux-27195366/) acknowledged that the company underestimated how expensive real-world agentic execution would become.

“GPT-5.6 Sol is much more willing to work for longer, make additional tool calls, and coordinate complex workflows across tools and subagents,” Sottiaux wrote. “That makes it better at solving hard problems, but some tasks were using far more than we intended.”

> “GPT-5.6 Sol is much more willing to work for longer, make additional tool calls, and coordinate complex workflows across tools and subagents. That makes it better at solving hard problems, but some tasks were using far more than we intended.”

## Sol’s unexpected token appetite

Sottiaux attributed much of the unexpected usage to Sol’s new programmatic tool calling, or “code mode.” By allowing the model to continue working while tools run in the background and coordinate more complex workflows, Sol ended up consuming far more tokens than OpenAI had projected. The company acknowledged that its testing hadn’t captured what power users would do once the model was released.  
  
“We should have recognized this sooner and been more upfront about it,” Sottiaux wrote.

> “We were very focused on average and median usage before launch and missed some cases where the long tail could use significantly more usage.”

## Power users expose edge cases

Most developers have run into this before. A system performs well in testing, but power users expose edge cases that never showed up under typical workloads. AI coding agents make those problems easier to miss because so much of their work happens out of sight.

“The median user actually found Sol quite token efficient,” Sottiaux noted. “While some power users working on harder tasks saw their usage drain much faster. We were very focused on average and median usage before launch and missed some cases where the long tail could use significantly more usage.”

## Agents burn tokens while waiting

Developers documenting their experiences in the openai/codex GitHub repository gave insight into what was happening. One user described a 43-minute coding session that generated nearly 300 model responses, along with 96 execution calls and 192 wait calls, consuming the remaining 42% of a five-hour usage allowance largely while waiting for tool results.

Another found that tasks which appeared independent were executed one after another instead of at the same time, extending the runtime and increasing token usage across more than 700 execution cells.

OpenAI’s initial response focused on making those workflows more efficient. The company improved how Sol behaves while waiting for tool calls, streamlined web searches, and temporarily lifted the five-hour usage cap while the changes rolled out.

## Chat limits meet agentic workloads

The fixes should make Sol more efficient, but they also highlight that subscription limits were designed around chat. Coding agents are different. They can spend 30 or 40 minutes working through a task, making tool calls and revising code before returning a result. That makes it much harder for developers to predict how much of their allowance a single job will consume.

> Subscription limits were designed around chat. Coding agents are different.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)