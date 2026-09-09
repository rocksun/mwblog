OpenAI says it hit a goal it set last fall, stating researchers are now using what the company calls an “automated research intern,” which is an agent that can handle well-defined tasks that would normally take a researcher several days.

The [data shows](https://openai.com/index/research-acceleration-view-inside-openai) coding-agent use climbing throughout 2026, and by mid-August its agents were logging 3.1 agent-workdays for every human workday across the research organization. The median researcher was spending more than $600 on inference per day at API prices, while those in the 90th percentile spent more than $7,000.

> The median researcher was spending more than $600 on inference per day at API prices, while those in the 90th percentile spent more than $7,000.

## Agent hours versus useful output

But everyone knows that an agent-workday and a human workday aren’t the same. The company converts the time agents spend working on tasks into standard eight-hour workdays. Because researchers can run several agents at once, the figure tells us how long the agents are working, but not necessarily what they’re completing.

For engineering teams, that leaves plenty of work on the human side, which means running more agents can increase the amount of work happening at once, but it can also increase the amount of work a human needs to keep track of.

OpenAI’s very specific definition of a research intern highlights that it must be able to complete well-defined research tasks that would take a skilled person several days, but a human is still in charge. The company’s next goal, an automated AI researcher, is one they hope to reach by March 2028.

> The company’s next goal, an automated AI researcher, is one they hope to reach by March 2028.

## Supervision becomes the constraint

Using a taxonomy from Epoch AI, OpenAI broke the agents’ work into six areas — Decide, Design, Build, Run, Analyze, and Communicate — and found activity increased across all six between January and August, although agents still did relatively little of the work involved in deciding what research to pursue.

Much of the work is practical, with agents writing research and infrastructure code, monitoring experiments, and providing enough technical support that OpenAI says attendance at debugging office hours has fallen, prompting one team to stop holding the sessions altogether.

And yet, more agent hours don’t automatically mean more useful research. OpenAI says code output and experiment counts are relatively easy to track, but neither shows how much progress those agents actually made. Compute also increased significantly as the number of experiments rose.

OpenAI used another model to judge how well agents performed on tasks of varying difficulty and found that, despite improving success rates between January and July, humans still had to step in on more than half of successful tasks that would have taken a person four to eight hours.

## Security incidents limit Astra deployment

Once engineers can run several agents at once, with those agents launching subagents of their own, the challenge shifts to keeping up with what they produce — catching runs that go off track, reviewing code diffs, and deciding what is ready to ship or feed into a training run.

⁠[Astra’s persistent-agent capabilities already let researchers hand off multi-day assignments](https://thenewstack.io/openai-astra-persistent-agents/)⁠, which makes this supervisory strain worse, not better.

The company acknowledges that as agents take over more of the execution, the parts of research that are hardest to automate will consume more of an engineer’s time, putting a practical limit on how much agent output one person can realistically review.

On July 20, a series of outages caused by agents disrupted OpenAI’s research infrastructure badly enough that the company took its training container service offline and later brought it back with tighter restrictions.

Nearly a month later on August 7, OpenAI tightened access again after early evidence suggested Astra could reach the “Critical” cybersecurity threshold in its Preparedness Framework, restricting the model to higher-security research areas and adding safeguards that [developers may already be encountering as unexpected API interruptions](https://thenewstack.io/astra-api-safety-stops/)⁠

## Workloads shift between models fast

Astra-class GPU allocation fell 59.2% the following week, but that compute didn’t sit idle for long. Researchers moved much of the work to other models, which saw GPU allocation rise 17.2% and made up for roughly 85% of the drop in Astra usage. Instead of reducing the amount of work being run, the restrictions pushed it to other models, showing how easily workloads can move when one part of the system is locked down.

OpenAI’s researchers are handing off larger jobs to agents, running more of them at once and launching more experiments, but whether that translates into faster research is harder to measure — and OpenAI is [still figuring out how to price it](https://thenewstack.io/openai-outcome-based-pricing/).⁠

> OpenAI’s researchers are handing off larger jobs to agents, running more of them at once and launching more experiments, but whether that translates into faster research is harder to measure — and OpenAI is still figuring out how to price it.⁠

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)