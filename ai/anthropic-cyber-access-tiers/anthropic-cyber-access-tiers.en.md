**This week, Anthropic announced an expansion** of its Cyber Verification Program (CVP), breaking access into three use case–based tiers and folding Project Glasswing into the least restricted tier.

The frontier lab [states](https://www.anthropic.com/news/cyber-verification-program) the change will “extend the impact of our Project Glasswing to a much larger number of cyber defenders.”

But that number may be smaller than you think. Anthropic’s own tests show that the Defense Access tier — where it expects many organizations conducting defensive cyber work to land — blocked Claude Opus 5.5 in 46 out of 50 offensive-security benchmark trials.

## Many defenders will still face significant restrictions

Per Anthropic, the revamped CVP is intended to let security teams access model capabilities that best fit their scope of cyber work, with each tier tied to different verification requirements and security controls.

But it seems the AI company still considers many security teams ineligible for its most powerful cyber capabilities.

Per Anthropic, many security teams — particularly those defending self-owned or -maintained systems — will This week, Anthropic [announced](https://www.anthropic.com/news/cyber-verification-program) an expansion to its Cyber Verification Program (CVP), breaking up access into three use case–based tiers and folding in [Project Glasswing](https://thenewstack.io/anthropic-claude-mythos-cybersecurity) to the least restricted.

Per the AI company, the change-up is a move to “extend the impact of Project Glasswing to a much larger number of cyber defenders.”

But that number may be smaller than you think. Anthropic’s own tests show that the Defense Access tier — where it expects many organizations conducting defensive cyber work to land — blocked Claude Opus 5.5 in 46 out of 50 offensive-security benchmark trials.

## Most defenders will still face significant restrictions

Per Anthropic, the revamped CVP is intended to let security teams access model capabilities that best fit their scope of cyber work, with each tier tied to different verification requirements and security controls.

But it seems the AI company still considers many security teams ineligible for its most powerful cyber capabilities.

Per Anthropic, many security teams — particularly those defending self-owned or -maintained systems — will likely qualify for the “Defense Access” tier. That’s the most restricted CVP tier, designed for defensive work like incident response and vulnerability analysis. It is also the broadest in who can apply, including smaller security firms, open-source maintainers, and individual researchers with a track record of reported vulnerabilities.

In other words, many qualifying security teams can still expect strict safeguards blocking higher-risk cyber activity.

> But without a comparable defensive-focused benchmark, developers and security teams can’t yet know how these safeguards will interfere with defensive work.

When Anthropic tested the new three CVP tiers against CyScenario Bench, its evaluation for planning and executing multi-stage cyber operations, Claude Opus 5.5 with Defense Access safeguards blocked 46 of 50 trials, letting only four succeed. That’s not far off from what happened when Claude Opus 5.5 ran without CVP access; there, every task was blocked on the first prompt.

Still, Anthropic says these evaluations involve “complex, interactive offensive scenarios,” so it expected the Defense Access tier to face significant blocks.

To be clear, these results don’t mean that Defense Access blocks 92% of the defensive work the tier is designed for. But without a comparable defensive-focused benchmark, developers and security teams can’t yet know how these safeguards will interfere with defensive work.

## The fewest restrictions require government review

The other two tiers give security teams much more room to operate — but they also require more intense review.

CVP’s new mid tier, aptly named “Red Team Access,” Anthropic says is best suited for red teams and penetration-testing firms. Individual researchers are, by default, barred from access. This tier covers all Defense Access use cases, plus authorized penetration testing and red-teaming.

The difference between Defense Access and Red Team Access is stark: Red Team Access’s 34 of 50 is effectively equivalent to the model’s 67.6% success rate with no safeguards applied. No trials were blocked for Opus 5.5 under Red Team Access safeguards, and the model successfully completed 34 out of 50 tasks.

> No trials were blocked for Opus 5.5 under Red Team Access safeguards, and the model successfully completed 34 out of 50 tasks.

Only a select few will be granted “Specialized Access,” the least restricted tier that Anthropic says “is reserved for a limited set of verified organizations” authorized to test safety-critical systems, e.g., power grids or telecom networks. All members of Project Glasswing are grandfathered into the Specialized Access tier, but any new security teams hoping to join will have to pass a review jointly conducted by Anthropic and the U.S. government.

Regardless of the tier, Anthropic says all teams get access to its most capable models (e.g., Claude Opus 5.5, Sonnet 5.5, and [Mythos 5.1](https://thenewstack.io/anthropic-mythos-claude-security/)), plus new models coming later.

## And there’s a data trade-off

No matter the tier, Anthropic says all organizations enrolled in CVP must accept data retention. But there are a few workarounds.

[Enterprise Frontier Safeguards (EFS)](https://www.anthropic.com/news/enterprise-frontier-safeguards), Anthropic says, is coming later this fall and will allow eligible organizations to store data in self-controlled cloud infrastructure. Until then, organizations with access to Claude Fable 5.1 or Claude Mythos 5.1 with zero data retention are exempt from CVP’s data-retention requirement.

Also, Anthropic says it is continuing “efforts to help secure open-source software and critical infrastructure.” It’s mum on any more details, but developers and security teams can expect more information in the coming weeks.  pushed to the “Defense Access” tier. That’s the most restricted CVP tier, designed for defensive work like incident response and vulnerability analysis.

In other words, many qualifying security teams can still expect strict safeguards blocking higher-risk cyber activity.

> But without a comparable defensive-focused benchmark, developers and security teams can’t yet know how these safeguards will interfere with defensive work.

When Anthropic tested the new CVP tiers against CyScenarioBench, its evaluation for planning and executing multi-stage cyber operations, Claude Opus 5.5 with Defense Access safeguards blocked 46 of 50 trials, letting only four succeed. That’s not far off from what happened when Claude Opus 5.5 ran without CVP access; there, every task was blocked on the first prompt, whereas the Defense Access count includes any trial blocked at some point.

Still, these evaluations involve “complex, interactive offensive scenarios,” so it’s expected that the Defense Access tier would face significant blocks.

To be clear, these results don’t mean that Defense Access blocks 92% of the defensive work the tier is designed for. But without a comparable defensive-focused benchmark, developers and security teams can’t yet know how these safeguards will interfere with defensive work.

## The fewest restrictions require government review

The other two tiers give security teams much more room to operate — but they also require more intense review.

CVP’s new mid tier, aptly named “Red Team Access,” Anthropic says is best suited for red teams and penetration-testing firms. Individual researchers are, for now, barred from access. This tier covers all Defense Access use cases, plus authorized penetration testing and red-teaming.

The difference between Defense Access and Red Team Access is stark. No trials were blocked for Opus 5.5 under Red Team Access safeguards, and the model completed 34 out of 50 tasks.

> No trials were blocked for Opus 5.5 under Red Team Access safeguards, and the model successfully completed 34 out of 50 tasks.

Only a special few will be granted “Specialized Access,” the least restricted tier that Anthropic says “is reserved for a limited set of verified organizations that are authorized to test safety systems that could impact people’s lives or disrupt markets,” e.g., power grids or telecom networks. All members of Project Glasswing are grandfathered into the Specialized Access tier for current models, but new security teams will currently have to pass a review jointly conducted by Anthropic and the U.S. government.

Regardless of the tier, Anthropic says all teams get access to its most capable models (e.g., Claude Opus 5.5, Sonnet 5.5, and [Mythos 5.1](https://thenewstack.io/anthropic-mythos-claude-security/)), plus new models coming later.

## And there’s a data trade-off

No matter the tier, Anthropic says all organizations enrolled in CVP must accept data retention. But there are a few workarounds.

[Enterprise Frontier Safeguards (EFS)](https://www.anthropic.com/news/enterprise-frontier-safeguards), Anthropic says, is coming later in the fall, allowing eligible organizations to store data in self-controlled cloud infrastructure. Until then, organizations with access to Claude Fable 5.1 or Claude Mythos 5.1 with zero data retention are exempt from CVP’s data-retention requirement.

Also down the pike, Anthropic teases “efforts to help secure open-source software and critical infrastructure.” It’s mum on any more details, but developers and security teams can expect more information in the coming weeks.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)