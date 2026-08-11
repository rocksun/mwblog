**Meta this week announced [Muse Code](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2)**, its first coding agent designed to tackle complex software engineering tasks, like planning changes, writing code, and validating the results. The terminal coding agent is powered by Muse Spark 1.2, an update to [Muse Spark 1.1](https://thenewstack.io/meta-muse-spark-api/), also released this week, that Meta says comes with improvements for code generation, debugging, codebase understanding, and end-to-end developer workflows.

Perhaps most notable is Muse Code’s expected price tag, which Meta is positioning below that of Anthropic’s Claude Code or OpenAI’s Codex. Still, software leaders aren’t exactly queuing up to test it out, saying the coding agent is likely a better fit for pet projects and open source work.

That’s because getting the lowest pricing for Muse Code requires opting in to improve Meta’s model, according to [Alexandr Wang](https://www.linkedin.com/in/alexandrwang/), chief AI officer, Meta. For many engineering leaders, trading coding data for a lower price is a no-go.

As [Ken Ringdahl](https://www.linkedin.com/in/kenringdahl/), CTO, [Emburse](https://www.emburse.com/) and advisor to [Snyk](https://snyk.io/platform), tells *The New Stack,* “Security, data privacy, [and] data security is paramount, and it’s not something we will trade off for a lower-cost option,” he says. “I’d be surprised if there’s many of my peers that would be willing to trade that off for saving a little bit of cost.”

Zuckerberg’s behemoth is kicking it into high gear in an attempt to close the gap with OpenAI and Anthropic. In early July, Meta released Muse Image, an image-generation model. Later that month, it also [debuted Muse Spark 1.1](https://thenewstack.io/meta-muse-spark-api), its first paid AI model, signalling a step away from open source to proprietary AI models with aggressive pricing to undercut OpenAI and Anthropic.

Now, it looks like Meta is applying a similar pricing strategy to Muse Code. Its pay-as-you-go pricing is similar to that for Muse Spark 1.1 at $1.25 per million input tokens and $4.25 per million output tokens, indicating the tech company wants to differentiate Muse Code as a cheaper alternative to Anthropic’s Claude Code or OpenAI’s Codex.

Most interesting is the agent’s contributor tier, which Wang told [CNBC](https://www.cnbc.com/2026/08/05/meta-debuts-muse-code-to-take-on-anthropic-and-openai-.html) gives users “a significantly lower cost,” making it “more than 10 times cheaper than even the pay-as-you-go tier.” But there’s a catch to that pricing drop: your data. To use Muse Code via the contributor tier, developers must “opt-in to help improve the model,” Wang said.

> “There isn’t IP that’s more important than your source code itself,” says Ringdahl. “I won’t gamble with my IP.”

The move is reminiscent of earlier reports that Meta is already [using its own engineers’ code fixes as training data](https://thenewstack.io/meta-metacode-engineer-training/) for its internal AI coding agent, MetaCode, even using a colored badge system to incentivize more code-fix submissions.

Thus the disinterest. When asked if they would be willing to accept the data trade-off for cheaper pricing, few seem willing. “There isn’t IP that’s more important than your source code itself,” says Ringdahl. “I won’t gamble with my IP.”

[Yunhao Jiao](https://www.linkedin.com/in/yunhaojiao/), co-founder and CEO, [TestSprite](https://testsprite.com/) echoes much of the same, telling *The New Stack* he thinks Meta’s Muse Code opt-in could expose more than just companies’ code: “Actually, Meta [takes] more than just your code, because for each of the coding sessions, there is more than just code there,” he explains, pointing to developer prompts, agent responses, and developers’ corrections.

The risk for Jiao isn’t so much what Meta may do with that information but that it may slip into competitors’ hands somewhere down the line: “Maybe Meta’s model will remember all these details, and in the future, when other companies — maybe our competitors, maybe other people when they’re doing similar features — the model will remember all those details and easily help them to replicate our work.”

Though there’s no evidence to back Jiao’s concern, for now, it’s enough to keep him away from Muse Code.

## So who should use Muse Code’s contributor tier?

In recent months, multiple companies have reportedly scaled back AI coding tool use or introduced new controls after token costs rose faster than expected, reported [*TechCrunch*](https://techcrunch.com/2026/06/05/the-token-bill-comes-due-inside-the-industry-scramble-to-manage-ais-runaway-costs/). But when asked if he thinks companies might be tempted to expand coding agent use given Meta’s cheaper agent, Jiao says his team doesn’t actually consider coding agents a big expense — certainly not enough to opt in to the data-sharing requirements of Muse Code’s contributor tier.

For those that do want to shop for the cheapest coding agent, comparing coding agents by token price may not actually be the best measure. As [Michał Piszczek](https://www.linkedin.com/in/michalpiszczek/), CTO, [Archdesk](https://archdesk.com/), tells *The New Stack*, “The useful metric is cost per accepted change after review and repair.”

Like Ringdahl and Jiao, Piszczek agrees that opting into Meta’s model improvement makes Muse Code a non-starter for product code, but he says it can have a place for open source work, personal projects, and “throwaway prototypes.”

Looking ahead, he envisions a setup where coding agent use gets split into two tiers, with lower-risk work eligible for cheaper, data-sharing options and proprietary code reserved for those with zero-data retention: “A startup can use contributor pricing on public work and require zero-data retention for its core product.”

Wang told *CNBC* that Meta is “also starting to accept requests for zero-data retention,” meaning the company wouldn’t retain developer data to improve its models, but Meta has yet to confirm if or when zero-data retention is coming.

Muse Code is available now in beta.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)