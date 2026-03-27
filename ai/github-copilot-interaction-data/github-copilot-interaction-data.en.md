Yet another platform will use your data to train its AI models. This time, it’s GitHub.

[GitHub](https://github.com/) announced this week that it will use interaction data (e.g., inputs, outputs, code snippets, and associated context) from users of GitHub CoPilot to train and improve its AI models, per a [blog post](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/) from [Mario Rodriguez](https://www.linkedin.com/in/mariorodriguez3/), GitHub’s chief product officer.

The update begins April 24 and applies to all Copilot Free, Pro, and Pro+ users, but you can opt out. As GitHub explained in an email sent on Wednesday to [its Copilot users](http://github-launches-its-coding-agent/), to opt out: “Go to GitHub Account Settings; select Copilot; choose whether to allow your data to be used for AI model training.”

If you’ve previously opted out of letting GitHub collect your interaction data for product improvements (i.e., by disabling the setting called “Enabling or disabling prompt and suggestion collection”), those preferences will be carried forward, so you can skip this step.

Copilot Business and Copilot Enterprise users need not concern themselves; they won’t be affected by this update.

## What you’re giving, to whom

Importantly, if you don’t opt out, it’s not only GitHub that will get access to your interaction data but its affiliates, too.

As GitHub notes, this includes “companies in our corporate family, including Microsoft.” Per GitHub’s [updates to its privacy statement and terms of conditions](https://github.blog/changelog/2026-03-25-updates-to-our-privacy-statement-and-terms-of-service-how-we-use-your-data/) (also released on Wednesday), these affiliates “may now use shared data for additional purposes, including developing and improving artificial intelligence and machine learning technologies, subject to applicable law and their own privacy commitments.”

The platform says these permissions do not extend to third-party AI model providers or other independent service providers, though, as it clarifies in its [FAQs and related discussion](https://github.com/orgs/community/discussions/188488), “We may also engage service providers to assist with model training on our behalf, subject to contractual obligations to use the data only for providing services to GitHub.”

What, exactly, do you hand over to GitHub and its affiliates if you *don’t* opt out?

The list in GitHub’s announcement covers seven types of interaction data, including: “Outputs accepted or modified by you”; “inputs sent to GitHub Copilot”; “code context surrounding your cursor position”; “comments and documentation you write”; “file names, repository structure, and navigation patterns”; and “interactions with Copilot features (chat, inline suggestions, etc.).”

What will not be included in model training is interaction data from Copilot Business, Copilot Enterprise, or enterprise-owned repositories, nor “content from your issues, discussions, or private repositories at rest.”

In its announcement, GitHub draws attention to this “at rest” specification, noting that the update “does process code from private repositories when you are actively using Copilot.”

When asked how long interaction data is retained and whether users can view or delete it, GitHub says retention varies by use case, noting it may retain inputs, outputs, code snippets, and associated context for up to five years, though that period is often shorter.

## Not all developers are on board

In his announcement blog post, Rodriguez reminds readers that GitHub built its original models using both publicly available data and code samples. In the last year, the platform says it has incorporated interaction data from Microsoft employees to “meaningful improvements, including increased acceptance rates in multiple languages.”

Now, GitHub aims to see similar gains by incorporating user interaction data into its training, hoping to help its models better understand development workflows, deliver more accurate, secure code pattern suggestions, and catch bugs early.

But judging by the initial reactions from developer communities on [Reddit](https://www.reddit.com/r/GithubCopilot/comments/1s3ky4h/on_april_24_well_start_using_github_copilot/) and [Hacker News](https://news.ycombinator.com/item?id=47521799), not everyone is convinced that the update benefits all users equally.

A common complaint is that users have to opt out, not opt in; others say GitHub provides conflicting instructions for how to opt out, making it unnecessarily difficult.

Still others criticize GitHub’s move to use individual users’ data but not that of businesses or enterprises, as one commenter on Hacker News writes:

> “The individual/corporate asymmetry you’re describing is standard across B2B SaaS. Slack, Notion, and Figma all include ML training carve-outs in enterprise DPAs [Data Processing Agreement] that free users don’t get. GitHub isn’t doing anything unusual here — they’re just doing it with code, which feels more sensitive than documents or messages because it might literally be your employer’s IP you’re working on from a personal account.”

In its FAQ and related discussion, GitHub explains the difference by acknowledging that it has agreements with Business and Enterprise customers that prohibit Copilot interaction data from model training, and stresses again that individual users can opt out at any time.

Other developers are less vocally critical, giving GitHub points for being more transparent where other companies are sly: “tbh [to be honest], I appreciate them adding a notification banner for this. Most companies would have done it as silently as possible,” writes one redditor.

GitHub defends its decision to pull individual users’ interaction data into model training, calling it in line with established industry practices and a move that “will improve model performance for all users,” a number now exceeding 26 million, it says. With so many developers using GitHub Copilot, the sheer volume of data now available for AI model training could lead to faster model improvements.

“We believe the future of AI-assisted development depends on real-world interaction data from developers,” Rodriguez affirms in the company’s announcement post.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)