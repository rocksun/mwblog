On Friday evening, Anthropic suddenly [disabled](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/) its new flagship models, Fable 5 and Mythos 5, after the U.S. government became aware of a way to perform a specific jailbreak on Fable 5 and put it under an export control order. Since this order applies to all foreigners, including those in the U.S., Anthropic had no other choice but to disable these models for everybody.

As of now, it is unclear what this jailbreak entailed, and Anthropic argues that what the government showed were “minor vulnerabilities” that “all appear relatively simple,” and that don’t go beyond the capabilities of other publicly available models.

When Anthropic announced Fable 5 and Mythos 5, it noted that Fable 5 had undergone extensive red-teaming security exercises with the help of the UK’s AI Security Institute and other external testers. Anthropic’s own internal testing showed that the model would complete about 5% of adversarial cyber tasks.

The Fable 5 [model card](https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf) also specifically notes that, “in the event that a public universal jailbreak is found, we will move quickly to update our defenses to ensure that they remain robust to all known attacks.” But according to the current information, this current issue isn’t about a universal jailbreak but applies to a very specific problem.

As of Saturday morning, Anthropic hasn’t updated its previous statement, which concluded that all of this “is a misunderstanding.”

## More than a misunderstanding?

Given that this is 2026, the story gets more complicated, though. David Sacks, the co-chair of the [President’s Council of Advisors on Science and Technology](https://en.wikipedia.org/wiki/President%27s_Council_of_Advisors_on_Science_and_Technology) and the White House’s former AI and crypto czar, on Saturday [tweeted](https://x.com/davidsacks/status/2065853007619588171) the U.S. government’s version of events.

Sacks argues that “a highly credible trusted partner of both Anthropic and [the U.S. government]” reported the jailbreak and that the administration asked Anthropic CEO Dario Amodei to improve the guadrails to fix the jailbreak or take the model down. “Dario refused,” Sacks writes.

## Amazon’s role

According to independent reports from the [Wall Street Journal](https://www.wsj.com/tech/ai/amazon-ceos-talks-with-u-s-officials-triggered-crackdown-on-anthropic-models-dcc90578) and [The Information](https://www.theinformation.com/articles/amazons-jassy-raised-concerns-anthropic-model-trump-crackdown), it was Amazon CEO Andy Jassy who reported a jailbreak that Amazon researchers found to, according to the Wall Street Journal, “U.S. officials, including Treasury Secretary Scott Bessent.”

Those Amazon researchers, the report says, found ways to get Fable 5, the version of Mythos 5 with security guardrails, to aid in cyberattacks. Anthropic, when it released Fable 5, noted that it had put guardrails in place to prevent Fable 5 from aiding users in starting cyberattacks or creating bioweapons, for example.

Indeed, many users quickly complained that the model [refused to answer innocuous questions](https://thenewstack.io/fable-5-developer-reactions/). Often, when the system detected potentially unsafe prompts, Claude would also quietly move to using the former flagship model, Opus 4.8.

Since this jailbreak was reported by Amazon, chances are those researchers tested Fable 5 on [Amazon Bedrock](https://aws.amazon.com/blogs/aws/anthropic-claude-fable-5-on-aws-mythos-class-capabilities-with-built-in-safeguards-now-available/), which Amazon says has the same safety mechanisms in place as using Claude through Anthropic directly.

Sacks argues that Anthropic defended its position not to take the model down “by saying the jailbreak isn’t serious” and pulls a rhetorical move that puts Anthropic into a corner of its own making.

“That is not what the trusted partner and the USG believe; nor is that kind of minimizing language consistent with Anthropic’s brand as the AI safety company,” he writes. “It’s difficult to fathom how they could claim a jailbreak allowing operability of a cyber weapon could be defined as not ‘serious.’”

As many a pundit has pointed out since this story broke, it was Anthropic that argued that Mythos 5 was too dangerous to release to the public. It’s also Anthropic that has built a brand on being the frontier lab that takes AI safety seriously.

Now Sacks can turn this against the company and writes, “In the past, Anthropic has always said that safety must be top priority and taken super seriously. In this case, Anthropic prioritized the continued offering of the consumer model over safety.”

## What’s next?

The most obvious solution here is for Anthropic to put new guardrails in place that would make this specific jailbreak impossible — though given the nature of these non-deterministic models, some other jailbreak may just be around the corner.

Chances are, though, that we’ll see a fix relatively soon and that the export control will be lifted and the model becomes available again.

This does, however, set a new precedent for how the U.S. government could handle AI safety and the other U.S.-based frontier labs are surely watching this very closely. The way AI has progressed has been a constant back-and-forth between these labs, after all, one besting the other on a regular basis — and Fable 5/Mythos 5 isn’t likely to be the pinnacle of AI model development.

What this means for the next tranche of models from OpenAI and Google remains to be seen. The U.S. government has, after all, proposed voluntary safety tests before a new model could be released and this affair will likely put this idea to the forefront again.

Anthropic, it is worth noting, has been the company that has [advocated](https://darioamodei.com/post/policy-on-the-ai-exponential) for AI regulations more than anybody.

## “The ball is in Anthropic’s court”

All of this, of course, is complicated by the contentious relationship between Anthropic and the Trump White House.

Sacks, in his tweets, argues that this is not the case here and that “the Admin values Anthropic’s technical capabilities and feels that this issue, while serious, should be easily resolved. The ball is in Anthropic’s court.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)