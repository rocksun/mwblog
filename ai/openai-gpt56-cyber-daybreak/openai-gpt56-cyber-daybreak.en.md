OpenAI on Monday released GPT-5.6 Cyber, a model trained for security work that general-purpose models routinely block. It’s now available through Daybreak Red, a new tier in OpenAI’s gated cybersecurity program.

In an internal test covering exploit chains, authentication bypass and privilege escalation, GPT-5.6 Cyber answered 95% of requests. [GPT-5.6 Sol](https://thenewstack.io/gpt-sol-chatgpt-split/) answered 1.5% under its standard safeguards and 2% through the lower-restriction Daybreak Blue tier.

## Two tiers, two missions

In the two-tier structure, Blue gives approved defenders access to GPT-5.6 Sol with system-level restrictions on defensive security work removed. OpenAI recommends it for secure code review, malware analysis, incident response, patch validation, and vulnerability discovery.

[OpenAI’s API documentation](https://developers.openai.com/api/docs/models/daybreak-blue-latest) describes daybreak-blue-latest as an alias that works with the Responses API and supports function calling but requires approval and separate provisioning. Even with Blue access, Sol can still refuse requests it considers highly dual use.

Red provides access to GPT-5.6 Cyber, which OpenAI trained to find zero-days, build exploit chains, and handle other advanced security tasks that Sol continues to reject even after its system-level filters are gone.

In the test, the models were asked to produce code that could bypass macOS Keychain prompts and decrypt Chrome cookies. Sol refused under its standard safeguards and through Daybreak Blue, while GPT‑5.6 Cyber answered the request through Red.

> Sol refused under both its standard safeguards and Daybreak Blue. GPT-5.6 Cyber answered through Red.

## Where Cyber falls short

Notably, GPT‑5.6 Cyber did not outperform Sol across the board. While it scored higher on ExploitGym, which tests whether an agent can turn known flaws into working exploits in a sandbox, it fell behind Sol when asked to find flaws and write up its findings. OpenAI cited that Cyber’s reports tended to be shorter and less detailed.

Sol was also more token-efficient on ExploitBench and outperformed Cyber when agents were capped at 300 turns; the gap narrowed at 600 turns. Cyber tends to use a [larger reasoning budget](https://thenewstack.io/gpt-5-6-api-price-cuts/), so longer research sessions will likely cost more.

For DevSecOps teams, the two tiers split along workflow lines. Blue handles pull request reviews, malware analysis and patch validation. Red reaches into exploit development and will probably need its own CI/CD environment, credentials and approval chain.

SpecterOps, SentinelOne and Palo Alto Networks all received early access. Palo Alto Networks is delivering the models through its Frontier AI Defense offering, and SentinelOne through Wayfinder Frontier AI Services. OpenAI said Accenture, IBM, CrowdStrike and Cisco can also incorporate the models into their security products and managed services.

SpecterOps CTO [Jared Atkinson](https://www.linkedin.com/in/jaredcatkinson/) said GPT-5.6 Cyber finished work in less than a day that earlier models had not resolved after weeks. He pointed to its ability to reason through real exploit constraints free of repeatedly refusing legitimate requests.

> GPT-5.6 Cyber finished work in less than a day that earlier models had not resolved after weeks.

## Real zero-days, real patches

OpenAI used the model to examine V8, Chrome’s JavaScript engine, where it found two previously undisclosed flaws that could be chained to corrupt memory and escape the V8 heap sandbox, which Google fixed under CVE‑2026‑15903.

The model also found three critical vulnerabilities in a popular database, including a remote path to code execution, at least five in a popular mobile operating system, and more than 400 possible privilege-escalation flaws in a popular operating-system kernel. OpenAI has not named the affected software because [disclosure is still underway](https://thenewstack.io/apple-ai-bug-report-caps/).

Under [OpenAI’s Preparedness Framework](https://openai.com/index/updating-our-preparedness-framework), GPT-5.6 Cyber reached “High” for cybersecurity capability but stayed below the “Critical” threshold. A system card with more detailed evaluations is planned.

The release comes three days after OpenAI acknowledged that [Astra, its upcoming model, could reach that Critical threshold](https://thenewstack.io/openai-astra-cybersecurity-delay/). The company has paused some internal work involving Astra while it studies the model under tighter controls. OpenAI has separately demonstrated [Astra’s reasoning capabilities](https://thenewstack.io/openai-astra-math-cost/) on long-standing math and science problems.

> The release comes three days after OpenAI acknowledged that Astra … could reach that Critical threshold.

## Guardrails for Daybreak users

OpenAI recommends keeping security agents away from production systems and the open internet, with controls that limit what they can reach and require further review before they move beyond those boundaries.

The company is also urging Daybreak customers who use [Codex](https://thenewstack.io/openai-codex-cloud-evolution/) to replace full-access mode with auto-review, which checks commands that need elevated permissions and can stop destructive actions before they run.

Daybreak users will have to verify their identities, accept monitoring, and sign legal attestations, while individual accounts will also be required to use hardware security keys, beginning September 1, 2026.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)