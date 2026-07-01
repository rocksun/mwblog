After the U.S. government [lifted its export controls for Fable 5](https://thenewstack.io/anthropic-fable-ban-lifted/) on Tuesday, Anthropic announced that it would bring the model back on Wednesday, July 1. Now, the company has [clarified what this process will look like](https://www.anthropic.com/news/redeploying-fable-5), as well as a few more details on the ‘jailbreak’ — or bypass, as Anthropic prefers to call it — that led to the Commerce Department applying export controls to both Claude Fable 5 and Claude Mythos 5.

On July 1, Fable 5 will return to the Claude Platform, Claude.ai, Claude Code, and Claude Cowork for all users globally on the Pro, Max, Team, and Enterprise plans. But there is some bad news, too: until July 7, users on subscription plans will be able to use Fable 5 for up to 50% of their weekly usage limits. After that, it will only be available via usage credits, which are billed at the same rates as access to [Anthropic’s API plans](https://platform.claude.com/docs/en/about-claude/pricing).

For standard Enterprise users, Fable 5 will *not* be part of their regular allowance, not even until July 7. Access for them will be billed through usage credits immediately. There’s a short grace period until July 7 for premium Enterprise seats, though, and those users will get Fable 5 access through the subscription plan until then.

Originally, Fable 5 was supposed to be available for free from June 9 to June 22.

Access for developers who accessed Fable 5 through AWS, Google Cloud, and Microsoft Foundry will be re-enabled soon, too.

Before pulling Fable 5, Anthropic charged $10 per million input tokens and $50 per million output tokens. It doesn’t look like this pricing will change.

## What happened, according to Anthropic

With this update, Anthropic also released a few more details on what led to all of this. Anthropic confirms that Amazon researchers “had found a method of bypassing Fable 5’s safeguards: prompting it so that it identified a number of software vulnerabilities.” In one case — and this seems to have been the only case — they got the model to demonstrate how the vulnerability could be exploited.

Anthropic says it worked with the government and partners, including Amazon, to review the report and found that other models, including Claude Opus 4.8, GPT-5.5, and Kimi K2.7, were able to find the same vulnerabilities that were part of the Fable 5 report, and that every model the team tested, including basic models like Claude Haiku 4.5, was able to figure out how to exploit this vulnerability.

The company stresses that “the reported technique did not expose any unique Mythos-level cyber capabilities” and instead was just below the borderline for Fable 5’s safeguards to kick in.

> “The new classifier means that the specific technique described in the Amazon report is blocked in over 99% of cases.” — Anthropic.

After Fable 5 was taken offline, Anthropic worked with the government to train an improved safety classifier — a system that can detect when somebody requests the model to produce harmful outputs — that now also blocks these kinds of requests. The company essentially increased the number of benign requests that the model will block.

## The price for bringing Fable 5 back: larger safety margins

One has to wonder what this means for all of the other models that exhibited the same behavior, but as of now, this only applies to Fable 5, and the U.S. government is apparently just fine with that.

“The new classifier means that the specific technique described in the Amazon report is blocked in over 99% of cases,” Anthropic writes and notes that while the model will still not block all low-risk cyberdefense capabilities, it should block the majority of those that are harmful. The company says it “deliberately set the safety classifiers to trigger on a set of requests that we know are likely benign” to increase the safety margin.

![](https://cdn.thenewstack.io/media/2026/06/a660a765-0cf1fc27ba70725d56c623b27dc1f05228a303c2-3840x1732-1-1024x462.webp)

When Fable 5 launched, there was already some feedback from users that the model would block even the most harmless of requests, so it remains to be seen how this will now play out with these enhanced guardrails. Anthropic already hints at this in its announcement.

“The new classifier also comes at the cost of flagging benign requests more often during routine coding and debugging tasks,” the company writes. “As with all our safeguards, we’ll continue to refine this to better distinguish genuine misuse from legitimate requests and reduce false positives.”

This, it seems, is the price Anthropic had to pay to bring Fable back.

Like before, Fable 5 will route any problematic requests to Opus 4.8 — a model that Anthropic itself says could also replicate Fable 5’s behavior. Feel free to make sense out of this, but don’t tell the U.S. government about it.

## What’s a jailbreak, anyway?

Since all of this started because of what seems to have been a relatively minor issue, Anthropic is also using this announcement to propose a way to score jailbreaks based on what they provide to the attackers. These include what capability gain the jailbreak unlocks and for how many distinct offensive cybersecurity tasks that capability gain would work, as well as the ease of weaponizing the jailbreak and how easy it is to discover and obtain the technique.

The company admits that this is a work in progress and it’s unclear how exactly these criteria should be scored and weighed against each other.

To monitor its own models, Anthropic is creating a team that will monitor its jailbreak submission channels 24/7. It’s also launching a new program [on HackerOne](https://hackerone.com/anthropic-cyber-jailbreak/?type=team) where researchers can submit potential vulnerabilities.

## Playing nice with Washington

As for the U.S. government, Anthropic says it will continue its collaboration with agencies like the Office of the National Cyber Director, the Office of Science and Technology Policy, the Department of the Treasury, and the Department of Commerce, with a focus on the framework the White House established as part of the [Promoting Advanced Artificial Intelligence Innovation and Security](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/) executive order.

“Our hope is that this collaboration, along with our proposed consensus industry framework, will serve as the basis for systematic rules for the whole industry—and even offer the beginnings of a template for effective global coordination on the risks and benefits of AI,” Anthropic writes and notes that it hopes these rules will be “codified in strong regulation and applied equally across frontier model developers.”

Anthropic has, of course, long been a proponent of AI safety regulations, so there’s no surprise there. It’s no coincidence, though, that the company calls for these rules to be applied to its competitors, too.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)