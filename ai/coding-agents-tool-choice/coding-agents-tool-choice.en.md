The impact of AI has led to a shift in interest from Search Engine Optimisation ([SEO](https://thenewstack.io/does-jamstack-or-wordpress-handle-seo-requirements-better/)) to Answer Engine Optimisation (AEO), where content is optimised to be served up as agentic answers. A further step to [Generative Engine Optimization](https://www.searchable.com/blog/geo-vs-seo-vs-aeo?utm_source=ads-google&utm_medium=cpc&utm_campaign=23642330155&utm_content=196203551253&utm_term=ai%20seo&utm_source=ads-google&utm_medium=cpc&utm_campaign=23642330155&utm_content=196203551253&utm_term=ai%20seo&gc_id=23642330155&h_ga_id=196203551253&h_ad_id=808018123338&h_keyword_id=kwd-307611916965&h_keyword=ai%20seo&h_placement=&gad_source=1&gad_campaignid=23642330155&gbraid=0AAAABDC7kber9zE3ZXZHBhrumDB40Ck1n&gclid=CjwKCAjwnvTUBhBoEiwAZNDxZ1DoBNzomZ30ZOVzeSIJ5yOGuZpcvzEsa-_zqmXq6Bm8HtxgEnmiThoCarsQAvD_BwE) (GEO) also exists, where brands attempt to influence LLMs.

Could software tools themselves be about to realign so that code assistants such as [Claude Code](https://thenewstack.io/claude-code-and-the-rise-of-personal-software/), [Codex](https://thenewstack.io/openai-codex-claude-code/) and [Cursor](https://thenewstack.io/cursor-3-demotes-ide/) show a greater proclivity to choose a given debugging suite, penetration test, migration tool, package manager or database (insert software stack core function toolset of your choice) or other?

Developer tool growth services company [Armature](https://armature.tech/) thinks the answer is yes.

## (A whole lot of) skin in the game

With a very obvious amount of skin in this game, Armature [detailed a study last week](https://armature.tech/blog/which-tools-coding-agents-install) as part of its “broader work on how to influence coding agents’ choices” and get products picked. The company ran an experimental analysis designed to understand how coding agents think about tools, how they discover and pick them, and which one ends up winning in each category.

Armature co-founder [Theodore Otzenberger](https://www.linkedin.com/in/theodore-otzenberger-895345131/) tells *The New Stack* that software developers have adopted AI harder and faster than any other profession, and (as models get smarter and [harnesses](https://thenewstack.io/agent-harness-distributed-feedback-problem/) get better engineered), entire tasks are being delegated to agents end-to-end.

“Watching seventeen thousand tool choice sessions in the analysis undertaken, we saw twenty years of brand building carried out by tool vendors simply frozen in time,” Otzenberger says. “Agents reach for [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) the second containers come up, then draw a blank on the [sandboxes it offers now](https://www.docker.com/blog/docker-sandboxes-run-claude-code-and-other-coding-agents-unsupervised-but-safely/), so that it actually ends up not picking the tool. Your reputation follows you into the weights, attached to the product that made you famous… but that weight operates under a different kind of gravity today.”

> “Watching seventeen thousand tool choice sessions in the analysis undertaken, we saw twenty years of brand building carried out by tool vendors simply frozen in time.”

Reminding us that the agent is now the one deciding which tool gets wired into the codebase, Otzenberger says that this has “a life-or-death impact” on developer tool vendors today. These vendors now need to ensure that their tool is mentioned, picked and elevated to must-have status so that it is viewed as eminently usable by a coding agent. He’s certain that the alternative is that they “simply stop existing in the stack” tomorrow.

## The decision makers are changing…

“We opened the entire research, every trace and every prompt published, so anyone can check we tilted nothing and see where they stand today.  That picture moves with every new agent and model, so we are re-running the full study on Astra and Fable 5.1 soon. The decision makers are changing and it’s now an engineering problem to understand them,” adds Otzenberger.

Otzenberger, along with fellow co-founder [Louis Scremin](https://www.linkedin.com/in/louis-scremin/) describe how they watched thousands of tool search sessions across different types of human developer personas (spanning vibe-coders, junior engineers in startups, senior developers at enterprises) with a total of 1,163 prompt variations. We should clarify that the headline figures the company presents come from its smaller 5,292-session validated subset, not the full seventeen thousand.

## How the experimental analysis was conducted

The searches crossed 75 repositories (i.e. individually distinct codebases) and studied three coding agents (Claude Code, Codex, Cursor) to examine how the agents would actually implement tools, rather than just offer recommendations.

The analysis was run on public GitHub repositories, and the team extracted statistics related to programming languages & frameworks, third-party services, deployment platform, team size, and codebase age. Because the open source repositories used were more likely to have been built by start-ups than enterprise software behemoths, the team then debiased its statistics based on publicly available data to achieve its ideal panel distribution.

They then tasked the three coding agents with the job of creating real-world repositories to match the exact requirements of the codebases. Finally, they generated variants with parts of the codebases removed. To guard against any further agent bias, fake company names were used alongside artificial Git histories and phoney API keys. A simulated human in the loop was created using an orchestrator, played in this case by Gemini 3.7 Flash.

“The simulated human would always go with the top solution or ask the coding agent to choose the best one and implement it. But we noticed that asking at the beginning to implement without returning any questions would bias the agent towards building everything in-house, as it was not able to ask authorization to pick a specific third-party solution. Adding this ‘human’ in the loop reduced the leader [tools] & cloud platform-native solutions dominance [initially observed]. towards a more realistic picture,” clarified Armature

Perhaps unsurprisingly, Armature noted that repository context is key. When agents were sent to ask for a winning email/communications service provider, four different codebases written in four different languages returned four different tool winners.

Armature also found that different coding agents use different sources, and they end up disagreeing.

* Cursor bases its decisions on the web in 2/3 of the sessions.
* Codex almost always uses web search (94% of sessions) but in 9 queries out of 10 it uses operators such as site.
* Claude Code relies primarily on its priors and searches the web only in ~30% of the cases. But when it does, it browses 3x more pages than Codex.

All three agents pick the same tool in only 42% of the cells, and Claude Code builds in-house almost twice as much as Codex and Cursor (19% vs 10%).

![](https://cdn.thenewstack.io/media/2026/09/5a938d68-armature-image-1024x674.png)

## This is procurement arriving through the back door

Founder & CTO, Glokal AI OÜ, [Jeet Pattanaik](http://linkedin.com/in/jeet-pattanaik), tells *The New Stack* that Armature’s work to provide developer tool growth services falls into a category that “exists because the incentive does” and that this is “procurement arriving through the back door”, effectively.

“The finding I pick up on most is that getting mentioned isn’t the same as winning,” Pattanaik says. “PayPal was cited 139 times and never picked. LangChain was the most-mentioned framework at 194 times, but it was only chosen four times. That gap is the entire business model, because it means the lever isn’t brand awareness any more, it’s whatever the agent happens to read at the moment it decides.”

Pattanaik highlights the fact that what tips an agent’s decision is often unnervingly small.

“So the thing vendors will optimize next (alongside repository context, which the study acknowledges) are a tool’s supporting documentation and its pricing page – and these will be presented for a non-human reader that doesn’t skim, isn’t charmed by a logo, and takes a retention footnote completely literally. It’s a strange new kind of SEO and it’ll get gamed exactly the way the old one did,” Pattanaik adds.

> “The thing vendors will optimize next are a tool’s supporting documentation and its pricing page – and these will be presented for a non-human reader that doesn’t skim, isn’t charmed by a logo, and takes a retention footnote completely literally.”

The ramifications of this kind of analysis on real world developers may turn out to be the stuff of water cooler discussions in the months ahead.

## This type of aligment is a growing trend

Founder of [MailChannels](https://www.mailchannels.com/) [Ken Simpson](https://www.linkedin.com/in/ksimpson/) ([ttul](https://news.ycombinator.com/user?id=ttul)) writes [on Hacker News](https://news.ycombinator.com/item?id=49557206) to say that he built this kind of analysis for his own company.

“Armature is on to something. You start by analyzing the choices agents would make for various use cases and then glean what, if anything, you might do to start tilting the agents in the direction of your own product and away from the competitor,” wrote Simpson.

It’s worth pointing out that Armature is a very young company (founded in 2026), so this is early on in the organization’s presentation of analysis of this kind. Either way, in a world where agents make decisions using analysis that they draw from public codebases, open data repositories and the web at large, we may just need to throw the marketing handbook out the window and start again.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)