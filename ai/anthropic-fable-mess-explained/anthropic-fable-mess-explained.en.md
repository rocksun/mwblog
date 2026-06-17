The [Anthropic-Mythos-Fable story](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/) has been The Topic since Friday, and it moved fast enough to lose anyone who blinked. Here’s my opinionated tick-tock of what happened, who’s calling Anthropic the good guy, and who’s calling it the bad guy.

Where I land: Anthropic mostly got this one right, and it’s one hell of an ad for Fable.

## **The Timeline**

**February/March:** Anthropic and the Department of Defense [get into a spat](https://www.anthropic.com/news/statement-department-of-war) over the use of the company’s AI models; Anthropic [wants certain limits on how its technology is used](https://www.anthropic.com/news/statement-comments-secretary-war). The ensuing fight leads to Anthropic being [dubbed a supply-chain risk](https://www.anthropic.com/news/where-stand-department-war), theoretically restricting government use of the company’s models and, in the same stroke, limiting government contractors’ access to the same.

**April 7:**Anthropic introduces Mythos, a new model family. After discovering that Mythos is adept at finding and exploiting novel cybersecurity flaws, Anthropic launches ‘[Project Glasswing](https://www.anthropic.com/glasswing)‘ to provide critical technology companies with access to tools to harden their own software before a broader release.

**April 16:** The White House [was reportedly working](https://www.bloomberg.com/news/articles/2026-04-16/white-house-moves-to-give-us-agencies-anthropic-mythos-access?embedded-checkout=true) to make a version of Mythos available for agency use.

**April 30:**Anthropic wants to expand the number of groups that can access Mythos; the White House reportedly [opposes the move](https://www.wsj.com/tech/ai/white-house-opposes-anthropics-plan-to-expand-access-to-mythos-model-dc281ab5), concerned that adding more partners would make Anthropic compute-constrained, thereby limiting USG access to the model.

![](https://www.cautiousoptimism.news/wp-content/uploads/sites/3/2026/06/image-22-1024x409.png)

**June 2:** Anthropic [announces](https://www.anthropic.com/news/expanding-project-glasswing)that Project Glasswing’s initial 50 partners found more than 10,000 serious software flaws by using Mythos. The company expands Project Glasswing to 150 new organizations in 15 countries. Anthropic also promises that it is working to “safely release Mythos-level capabilities in general access,” but that the “highly robust safeguards that prevent the model’s cyber capabilities from being misused–safeguards that we (and, to our knowledge, all other AI developers) have yet to develop.”

**June 9:**Anthropic [announces and releases Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5), a ‘Mythos-class’ model built to reduce cybersecurity and biology-related risks. The company said in its release notes that it had built safeguards for Mythos (Fable) sufficient “for a general release.” At the time, Anthropic said that it had “prioritized safety” by making the guardrails on Fable 5 “stricter than would be ideal.”

* Some users found Fable 5 *so*restricted in certain use cases (mostly biology-related queries) that it was nigh useless.
* Fable 5 also featured distillation protections and a strict 30-day data retention policy that Anthropic claimed would help “defend against complex and novel attacks (including new jailbreaks and attacks that operate across many requests) as well as help [it] identify and reduce false positives.”
* At this juncture, the core complaint levied against Anthropic was that it was *too* cautious; that by keeping Mythos private and releasing only a security-minded version of the model (Fable), it was creating a [two-tier AI market](https://www.cautiousoptimism.news/anthropic-just-added-a-velvet-rope-to-the-ai-club/). People didn’t like that!

Anthropic had “[previously notified the government multiple times](https://www.axios.com/2026/06/13/anthropic-amazon-white-house)” about its June 9th release date for Fable before the launch.

**June 10:** Anthropic [releases two frameworks](https://www.anthropic.com/policy-on-the-ai-exponential) to address advanced AI development and its economic impacts. The papers called for “government action and for regulation—regulations that are carefully designed to prevent government overreach and protect innovation,” including, when “a model poses risks of this kind,” allowing the government to “have the legal authority to block or deter its deployment.”

**June 11:** Amazon’s Andy Jassy reportedly [told the government](https://www.wsj.com/tech/ai/amazon-ceos-talks-with-u-s-officials-triggered-crackdown-on-anthropic-models-dcc90578) that its researchers had found a way to get Fable 5 to “provide [it] with information that could be used to aid cyberattacks and was supposed to be off-limits.” (At least five other companies [chimed in, too](https://www.axios.com/2026/06/13/anthropic-amazon-white-house), making this less an Amazon-specific point, even if it was a key actor.)

**June 12:** Senior White House staff and administration leaders met to discuss the situation, then brought Anthropic CEO Dario Amodei into the conversation via phone. (This took 1.25 hours [per Politico](https://www.politico.com/news/2026/06/13/inside-the-whirlwind-24-hours-that-led-the-white-house-to-slap-export-controls-on-anthropic-00961519), with the company saying that it offered other senior execs in the interim; there’s beef about why it took so long to get Amodei on the horn. We can skip the drama and focus on what matters.)

**June 12, continued:** Amodei [viewed the issue](https://www.politico.com/news/2026/06/13/inside-the-whirlwind-24-hours-that-led-the-white-house-to-slap-export-controls-on-anthropic-00961519) as a misunderstanding and argued that the reported “bypass” did not “pose the same risk as a broader ‘jailbreak.’” The White House “urged” Anthropic “to voluntarily remove the model and coordinate with the government to address the vulnerabilities.” Amodei asked for more “time and information, but he made no commitments to pull the model.”

* Politico reports that Treasury Secretary Scott Bessent “told Amodei directly that he was making a ‘bad decision,’ according to the senior White House official.”

**June 12, even more:** After failing to reach a deal with Anthropic, the Trump administration imposed export controls on both Fable 5 and Mythos 5 (the two available versions of Mythos-class models, with differing safety limits).

* Anthropic [responds](https://www.anthropic.com/news/fable-mythos-access) by saying that the “export control directive to suspend all access to Fable 5 and Mythos 5 by any foreign national, whether inside or outside the United States, including foreign national Anthropic employees” meant it must “abruptly disable Fable 5 and Mythos 5 for **all** our customers to ensure compliance.” (Emphasis original.)

## Good Guy Anthropic, the argument

Anthropic built a new, more powerful AI model that it believed had unique, novel cyber-related capabilities. It wanted to get ahead of the model’s cybersecurity risks, so it quickly assembled a group of leading technology companies and provided them with subsidized early access; governments red-teamed Fable’s safeguards before launch…

***This is an excerpt from*Cautious Optimism*, a ***modestly upbeat*** publication focused on technology, business, and power.*** ***Read the cases for and against Anthropic, plus where Alex Wilhelm lands, on [Cautious Optimism](https://www.cautiousoptimism.news/the-anthropic-fable-mess-explained?utm_source=The+New+Stack&utm_medium=referral&utm_campaign=Article+Excerpt).***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/04/03000ee4-cropped-4cd6e98e-image.png)

Alex Wilhelm is a journalist focused on technology and finance. He co-hosts the This Week in Startups podcast, and writes the Cautious Optimism newsletter. He was previously Editor in Chief of TechCrunch+.

Read more from Alex Wilhelm](https://thenewstack.io/author/alex-wilhelm/)