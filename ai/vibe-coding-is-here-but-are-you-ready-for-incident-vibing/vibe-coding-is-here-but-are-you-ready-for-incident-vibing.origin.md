# Vibe Coding Is Here — But Are You Ready for Incident Vibing?
Imagine coding while entirely giving in to the vibes and forgetting that the code exists. Instead of typing, tell [Cursor](https://www.cursor.com/) and [Sonnet](https://www.anthropic.com/claude/sonnet) to build everything for you. When faced with a bug, you don’t try to troubleshoot — instead, you feed the error back into the LLM and copy-paste the fix. The code grows beyond your comprehension, but it always ends up working. That’s how Andrej Karpathy — an OpenAI founding member — describes [Vibe Coding](https://x.com/karpathy/status/1886192184808149383).

And while Karpathy presents this as a fun approach for throwaway weekend projects, the reality is that a version of vibe coding — or writing code heavily using LLMs — is already happening at scale. Google reports that [AI generates 25% of its new code](https://arstechnica.com/ai/2024/10/google-ceo-says-over-25-of-new-google-code-is-generated-by-ai/), and in many parts of the industry, that number is likely even higher. Multiple people have [reported](https://www.linkedin.com/feed/update/urn:li:activity:7293680969788653569/) that software engineers at companies — including HubSpot — are no longer allowed to write software and can only prompt LLMs. Vibe coding is, in my opinion, the future of building software.

But what happens when AI-generated code fails in production and causes an outage? In this article, I explore this question and share a few ideas for getting your engineering organization ready.

## Code Vibing Is Fun and Games Until an Outage Hits
It is essential to have skilled engineers who understand the codebases they operate in. Strong engineering organizations even ensure that no engineer becomes a [single point of failure](https://thenewstack.io/james-webb-space-telescope-and-344-single-points-of-failure/) by spreading knowledge across team members.

When an incident occurs, the usual response is to bring in an [engineer who knows the affected part](https://thenewstack.io/the-6-pillars-of-platform-engineering-part-1-security/) to resolve it quickly. However, as more [code is generated](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/) by LLMs, engineers who deeply understand the codebase will become increasingly rare, making outages harder to diagnose and resolve.

Ph.D. student at UC Berkeley Shreya Shankar captures the issue perfectly in a [tweet](https://x.com/sh_reya/status/1873431565650502060) that has gathered over 300 million views: “How come nobody is talking about how much shittier eng on-calls are thanks to blind integrations of AI-generated code? LLMs are great coders but horrible engineers.” And with outages now costing [$14,000 per minute](https://www.bigpanda.io/blog/it-outage-costs-2024/), it is clear that teams can’t afford to waste time deciphering code written by an LLM.

## Vibe Coding Meets Incident Vibing
AI-generated code isn’t going away, with [61% of engineering teams embracing generative AI](https://jellyfish.co/blog/61-of-engineering-teams-are-embracing-generative-ai-heres-why-and-how-to-join-them/) — it will only increase. Here’s how to prepare for the future of incident management.

First, use AI-powered incident management tools like [Rootly](https://rootly.com/ai) or [PagerDuty Advanced](https://www.pagerduty.com/platform/generative-ai/). These tools handle the logistics of incidents — automatically spinning up communication channels, drafting updates for different stakeholders, and managing post-mortems. These tools have also started using AI to match current incidents with past ones, helping you quickly find similar cases and who fixed them, reducing the mean time to resolution.

Then, upgrade the way you fix incidents. What if you could use a tool to pinpoint the root cause and suggest a fix? That’s precisely what a new wave of LLM-driven incident resolution tools, labeled as AI SRE assistants, like [Sentry AI](https://sentry.io/changelog/sentry-ai-now-available-for-early-adopters/) and [Datadog Bits AI,](https://docs.datadoghq.com/bits_ai/) are doing.

These tools process the same [data an SRE would — error logs](https://thenewstack.io/observability-isnt-enough-its-time-to-federate-log-data/), metrics, application traces — but also ingest unstructured human-generated data like Slack discussions, cookbooks, and post-mortems. They can quickly [automate root cause analysis](https://thenewstack.io/machine-learning-for-automated-root-cause-analysis-promise-and-pain/), highlighting the commit that triggered the issue, visualizing how it affected system metrics, and tracing the chain of failures that led to an outage. So, when a human is paged and gets on a computer, a root cause analysis is already available to review.

The more advanced tools don’t just diagnose issues — they also propose solutions. You can review, discuss, and approve the fix before deploying it or let the tool handle everything automatically. Understandably, some Ops engineers are skeptical. What if the LLM hallucinates a fix that makes things worse? What if there’s no rollback available? Deploying changes gradually can help mitigate risk, but that’s one of many factors to consider. AI-driven incident resolution is promising, but it comes with its own set of challenges.

However, self-healing tools aren’t new: They’ve been around for at least over a decade. Facebook introduced [FBAR](https://engineering.fb.com/2011/09/15/data-center-engineering/making-facebook-self-healing/) in 2011 to automate rack maintenance. Dropbox presented [Naru](https://www.usenix.org/conference/srecon16europe/program/presentation/mah) 2016 to handle server failures, alerts, and remediation. However, these were deterministic systems with predefined rules, drastically reducing screw-ups’ chances.

At LinkedIn, as a senior SRE, I [co-designed a self-healing mechanism](https://patentcenter.uspto.gov/applications/14185537) for distributed infrastructure that used machine learning for root cause analysis and remediation, though it was never fully implemented. With the rise of LLMs, this approach is happening, and I am so excited to see it come to life. Companies in this space are making real progress. The competition is heating up. At least 20 players are in the market, and VC funding is [pouring in](https://techcrunch.com/2024/12/11/microsofts-m12-invests-another-22-5m-into-nuebird-months-after-its-22m-seed-round/). Enter incident vibing! Yes, I just made that up.

## If You Cannot Fight them, Join Them
With generative AI enabling developers to work up to [twice as fast](https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/unleashing-developer-productivity-with-generative-ai), this trend isn’t going anywhere. So why not embrace incident vibing? When an outage hits, sit back, sip your coffee, and let your AI-SRE assistant figure out how to fix the work of your Vibe Coding co-workers.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)