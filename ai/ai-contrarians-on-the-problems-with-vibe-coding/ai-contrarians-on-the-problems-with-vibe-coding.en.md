“What the hell is going on right now?” asked engineer [David DeGraw](https://github.com/catskull), aka Catskull, in a [blog post](https://catskull.net/what-the-hell-is-going-on-right-now.html) last week.

Vibe coding. Vibe coding is what’s going on — and it’s exhausting everyone and ruining everything, some developers say.

“Engineers are burning out,” DeGraw wrote. “Orgs expect their senior [engineering staff to be able to review](https://thenewstack.io/ai-coding-assistants-are-reshaping-engineering-not-replacing-engineers/) and contribute to ‘vibe-coded’ features that don’t work.”

He’s not alone in his criticism of AI’s impact. Like DeGraw, many contend that AI is like the emperor who wore no clothes.

## The Devin Experiment

It’s not just the frontier [large language models](https://thenewstack.io/will-llms-and-vibe-coding-fuel-a-developer-renaissance/) models that are problematic. It’s specialty AI tools as well, according to AI contrarians.

The programming team at Answer.AI spent a month using [Devin](https://devin.ai/), which claims to be a “fully autonomous software engineer.” It was first released in March, 2024.

Machine learning engineer [Hamel Husain](https://x.com/HamelHusain) and data scientists [Isaac Flath](https://www.linkedin.com/in/isaacflath/) and [John Whitaker](https://github.com/johnowhitaker) shared [their experience with the tool](https://www.answer.ai/posts/2025-01-08-devin.html) publicly in January. At first, the code was a bit verbose but it worked, they found.

“We imagined having Devin write documentation during our meetings or debug issues while we focused on design work,” they wrote. “But as we scaled up our testing, cracks appeared.”

Tasks that seemed straightforward took days rather than hours. Devin would get stuck in technical dead ends. It also created overly complex, unusable solutions, they added.

Devin would even push forward with tasks that weren’t actually possible, they noted.

“When asked to deploy multiple applications to a single Railway deployment (something that Railway doesn’t support), instead of identifying this limitation, Devin spent over a day attempting various approaches and hallucinating features that didn’t exist,” they noted.

That led to this observation: “The most frustrating aspect wasn’t the failures themselves — all tools have limitations — but rather how much time we spent trying to salvage these attempts.”

They began to document it across three categories:

1. Creating new projects from scratch;
2. Performing research tasks; and
3. Analyzing/modifying existing projects.

Out of 20 tasks, there were 14 failures, three successes — counting their initial two — and three inconclusive results, they wrote.

“Even more telling was that we couldn’t discern any pattern to predict which tasks would work,” they wrote. “Tasks that seemed similar to our early successes would fail in unexpected ways.”

## What AI Takes

[Luciano Nooijen](https://github.com/lucianonooijen/) is also [disenchanted with AI tools](https://lucianonooijen.com/blog/why-i-stopped-using-ai-code-editors/). He’s an engineer in the gaming industry who focuses on online game client development, multiplayer functionality and engine programming. He gave it a good try, from [ChatGPT](https://thenewstack.io/does-chatgpt-encourage-dangerous-delusions/) to [GitHub Copilot](https://thenewstack.io/the-top-ai-tool-for-devs-isnt-github-copilot-new-report-finds/), and he used AI tools as part of his workflow, beginning in late 2022 with the first release of ChatGPT. He continued to use AI-based tools in his development workflow through 2023.

“Initially, I was super impressed with the capabilities of these [LLMs](https://thenewstack.io/introduction-to-llms/),” Nooijen wrote. “The fact that I could just copy and paste obscure compiler errors along with the C++ source code, and be told where the error is caused, felt like magic.”

But he compared it to a Tesla car with full self-driving (FSD) capabilities.

“Being reliant on Tesla’s FSD took away my own ability to go into autopilot,” he wrote. “Working with AI-powered code editors was somewhat similar.”

Initially, Nooijen felt AI-assisted programming was faster. But when he had to do without his AI tools while working on a personal side project, he realized the AI had taken something as well.

“I felt less competent at doing what was quite basic software development than a year or so before,” he wrote. “All of a sudden, it made it very clear to me how reliant I had become on AI tools. Anytime I defined a function, I paused in my editor to wait until the AI tools would write the implementation for me. It took some effort to remember what the syntax was to write unit tests by hand.”

Nooijen also noticed that AI was becoming less useful over time. It was also draining his own confidence in his abilities.

“Not only did it take out the fun for me, but I started to feel a bit insecure about making some implementation decisions myself,” he said. “It was quite clear that because I did not practice the basics often, I was less capable with the harder parts as well.”

In 2024, Nooijen removed all LLM integrations from his code editor and went back to non-assisted coding.

“The longer you work with a language, framework or codebase, the more you develop this kind of intuition of what the correct approach is,” Nooijen wrote. “This intuition is what I was slowly losing when relying on AI tools a lot. And this is coming from a lead developer.”

He, too, can’t help but wonder how developers can hope to [“vibe code”](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/) their way to senior development.

“Where will you get the skills from to maintain and extend the vibe-coded codebase when the AI tools are down, or have become too expensive?” Nooijen questioned.

## Post-Developer Era? Not Really

Josh Comeau, a frontend developer and trainer, thinks that [predictions of AI replacing](https://www.joshwcomeau.com/blog/the-post-developer-era/) [frontend developers](https://roadmap.sh/frontend) are overblown.

“As far as I can tell, every AI success story still has skilled human developers as a necessary ingredient,” Comeau wrote in his assessment of AI software used in programming. “So, I think it’s safe to say that we’re not living in the post-developer era.”

Comeau experimented with [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) and found that it required guidance. He, too, compared it to driving a car, but with cruise control.

“It feels a bit like driving on the highway with ‘cruise control’: The car mostly goes where you point it, but you still need a hand on the steering wheel, keeping it steady,” he said. “Otherwise, the car will slowly start to drift out of its lane. If you don’t occasionally nudge it back on track, you’ll wind up in a ditch.”

It’s the same with AI, he wrote.

“If I didn’t know how to code, I wouldn’t notice the subtle-yet-critical issues with the model’s output,” he added. “I wouldn’t know how to course-correct, or even realize that course-correction was required!”

LLMs do save him time, he said. But overall, he still spends the majority of his time writing the code himself.

## Is AI Ruining a Generation of Programmers?

But the real threat from AI may be how it impacts on the next generation of developers. DeGraw contends that junior developers are over-relying on the tool. The best engineers love to help new team members contribute and learn, he wrote, but they can’t do that if everything just becomes fodder for an AI prompt.

“Instead of their comments being taken to heart, reflected on, and used as learning opportunities, hapless young coders are instead using feedback as simply the next prompt in their ‘AI’ masterpiece,” DeGraw wrote. “I personally have witnessed and heard first-hand accounts where it was incredibly obvious a junior engineer was (ab)using LLM tools.”

But right now, there’s a sort of “[groupthink](https://www.psychologytoday.com/us/basics/groupthink)” mentality around AI.

“In a recent company town-hall, I watched as a team of junior engineers demoed their latest work. I couldn’t tell you what exactly it did, or even what it was supposed to do — it didn’t seem like they themselves understood,” he said. “Championing their ‘success,’ a senior manager goaded them into bragging about their use of ‘AI’ tools to which they responded, ‘This is 4,000 lines of code written by Claude.’ Applause all around.”

But when you dig into the code, there are problems, he added. One friend DeGraw cited spent a month on a team of developers tasked with reviewing a heavily vibe-coded pull request.

“A month. Reviewing slop produced by an LLM,” he wrote. “What are the cost savings of paying ChatGPT $20 a month and then having a literal team of engineers try and review and merge the code?”

Another AI pain point that also could be detrimental to junior developers: Many companies are operating under the belief that AI will make developers obsolete. It means some companies aren’t hiring as “aggressively” as they otherwise might, Comeau wrote.

“Companies are not hiring the developers they need because they’re convinced that AGI (artificial general intelligence) is right around the corner, and when that egg hatches, we won’t need human developers at all anymore,” Comeau stated. “‘It’ll be any week now,’ they’ve been saying for years.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)