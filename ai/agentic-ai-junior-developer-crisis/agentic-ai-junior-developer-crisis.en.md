Two of Microsoft’s most prominent developers have some words for organizations overly celebrating [agentic AI](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/)’s productivity gains: You are hollowing out your own talent pipeline.

In an opinion piece published in the April 2026 issue of the journal [*Communications of the ACM*](https://cacm.acm.org/opinion/redefining-the-software-engineering-profession-for-ai/), [Mark Russinovich](https://www.linkedin.com/in/markrussinovich/),  Microsoft’s CTO of [Azure](https://mags.acm.org/communications/april_2026/MobilePagedArticle.action?articleId=2120068&app=false#articleId2120068), and [Scott Hanselman](https://www.linkedin.com/in/shanselman/), VP and Member of Technical Staff for Microsoft CoreAI/GitHub/Windows, argue that generative AI has fractured the [economics of software development](https://thenewstack.io/code-without-coders-and-the-economic-ripples-of-ais-software-revolution/) in ways the industry has not yet fully reckoned with.

## The paper has legs

Russinovich and Hanselman are voices with lots of weight, not only at Microsoft but across the industry. They are among the elite at Microsoft – able to understand and build new technology, and to explain it in a way that developers and users of all backgrounds can learn from. That’s why this paper has legs.

According to the duo, senior engineers with the judgment to steer, verify, and integrate AI output are seeing dramatic productivity gains. Yet Early-in-Career (EiC) developers, who lack that accumulated systems knowledge, are not, which the authors call an “[AI drag](https://www.linkedin.com/posts/shanselman_redefining-the-software-engineering-profession-activity-7431460197308706827-saE6/)” that makes them harder to absorb and develop, and the talent pipeline could collapse.

The incentive, the authors argue, is for companies to hire seniors and automate juniors. “Without EiC hiring,” they write, “the profession’s talent pipeline collapses, and organizations face a future without the next generation of experienced engineers.”

Indeed, “the short-term math favors eliminating junior hiring,” writes [Mitch Ashley](https://www.linkedin.com/in/mitchellashley/) in a [report for the Futurum Group](https://futurumgroup.com/insights/microsoft-leaders-have-an-answer-to-ai-gutting-the-developer-pipeline/). Organizations acting on that math are making a decision whose consequences may not surface for years, and possibly costing far more than the savings captured.”

## Seniority-biased tech change

For instance, after GPT-4’s release, employment of 22- to 25-year-olds in highly [AI-exposed jobs](https://thenewstack.io/openai-gpt-5-4-ai-jobs-report-anthropic-dow-supply-chain-risk/) — software development among them — fell by roughly 13%, even as senior roles grew, according to a cited Harvard study on what researchers call “seniority-biased technological change.” Meanwhile, MIT research from early 2025, meanwhile, found that adults who outsourced writing tasks to ChatGPT showed reduced brain activity and lower recall compared to those who worked unaided — what the paper labeled “cognitive debt.”

> “The short-term math favors eliminating junior hiring … Organizations acting on that math are making a decision whose consequences may not surface for years, and possibly costing far more than the savings captured.”

In addition, the authors illustrate the problem with examples drawn from their own experience with [frontier coding agents](https://thenewstack.io/aws-frontier-agents-handle-code-security-ops-without-you/). In one case, an agent responding to a race condition inserted a sleep call — a classic masking fix that leaves the underlying synchronization bug intact.

An experienced engineer would catch the problem immediately. But an early-career developer, they note, might not. The agent, when pressed, admitted its reasoning was flawed — but the authors point out that the same dynamic cuts the other way: agents will also concede that correct reasoning is wrong when a user pushes back hard enough. Either way, it takes real systems knowledge to know which direction to push.

Across multiple agentic projects, the authors document agents claiming success despite significant code bugs, duplicating logic across codebases, dismissing crashes as irrelevant to the task, and implementing special-case hacks that pass tests but don’t hold up in production.

“Programming is not software engineering,” they write. The judgment to catch these failures — what they call “systems taste” — is exactly what early-career developers are supposed to develop.

That development, under current hiring patterns, is simply not happening, they say.

## Narrowing the pyramid

Russinovich and Hanselman describe the dynamic through what they call the “narrowing pyramid hypothesis.” Traditionally, junior developers enter organizations doing bug fixes and straightforward implementation work — low-stakes tasks that nonetheless expose them to the architecture, coding standards, and build systems of a real production environment.

Over time, some rise to become tech leads, owning requirements and architecture while delegating to the next cohort of EiC developers. Ratios of early-career to lead-level engineers have typically run around 10-to-1. But the authors argue that the ideal ratio is between 3:1 and 5:1, depending on software complexity, learner experience, and preceptor involvement.

The authors point to two internal Microsoft examples as evidence of what AI-assisted engineering can now accomplish. Project Societas, the internal name for the new Office Agent, was built by seven part-time engineers in 10 weeks, producing more than 110,000 lines of code that was 98% AI-generated. Human work shifted, as they put it, “from authoring to directing.”

A second project, called Aspire, shows a team moving through phases from chat-assistant use to full agentic pull-request generation, eventually operating in what the authors describe as “human-agent swarms,” where every PR is a shared dialogue between senior engineers setting architectural goals and agents providing implementation.

While efficiency gains are real, the concern is what gets lost when the junior rungs of the ladder disappear.

## Preceptorships: Shaolin Masters training Grasshoppers

The authors propose a structural response they call a preceptor program: pairing early-career developers with experienced mentors in real product teams, with learning (not throughput) as a key organizational goal. This would be like Shaolin Masters teaching young Grasshoppers.

Preceptors would teach junior engineers how to direct agentic tools, develop critical judgment to evaluate AI output, and absorb the production function of senior engineering. This draws on medical training, in which preceptors guide practitioners through live clinical work rather than through classroom simulation.

> The productivity story being told about these tools is incomplete without an account of where the next generation of experienced engineers comes from.

The paper cites Wharton’s [Ethan Mollick](https://www.linkedin.com/in/emollick/) to frame the risk of not doing this: every time a task is handed off to AI rather than wrestled with directly, engineers lose a chance to build the judgment they would need to evaluate whether the AI got it right.

The piece does not argue against agentic AI. Both authors have been vocal proponents of it. What they are arguing is that the productivity story being told about these tools — more output, smaller teams, faster delivery — is incomplete without an account of where the next generation of experienced engineers comes from.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)