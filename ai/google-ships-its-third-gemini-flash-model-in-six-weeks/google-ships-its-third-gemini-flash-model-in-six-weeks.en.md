**Google hasn’t released a Gemini Pro model in a while**, but on Wednesday, the company [launched](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) yet another set of Gemini Flash and Flash Cyber models.

Even though Gemini 3.7 Flash is only three weeks old (and this is Google’s third Flash release in six weeks), the new Flash model often outperforms it by quite a margin, especially on agentic coding tasks and agentic computer use.

Like before, Flash 3.8 will be available at $0.75/$3.75 per million input/output tokens. That’s the introductory price, though. It will expire on December 31, 2026, and go to $1.50/$7.50 then.

## Fairwind gates Flash 3.8 Cyber

Flash 3.8 looks to be a very good model, and Google is right in calling it its “workhorse model,” but Flash 3.8 Cyber is worth a mention, too. With this, Google is essentially copying the Anthropic playbook.

Google describes the Cyber model as its “most capable cybersecurity model with frontier-level performance in vulnerability detection and automated patching.” And because of this, it’s only available to a select number of “trusted defenders” through a new program Google calls [Fairwind](https://deepmind.google/fairwind-program/).

These include about 650 trusted partners like Accenture, CrowdStrike, the Center for Internet Security, Datadog, Palo Alto Networks, Snowflake, and Wiz.

“The defender’s edge comes from shrinking the time between detecting a flaw and patching it,” Four Flynn, Google’s VP for Security and Privacy, writes in the [announcement](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/). “Through Google’s Fairwind Program, government and enterprise partners gain autonomous tools to repair systems faster and at scale, keeping them one step ahead of agentic-speed threats.”

With Flash 3.5 Cyber, Google had launched a limited-access program, but that didn’t have a name and seemed a bit ad hoc at the time.

## Gemini 3.8 Flash: long-horizon coding and agents

As for Flash 3.8, Google notes that the new model often outperforms models like GPT-5.6 Sol from OpenAI and Claude Sonnet 5 and Opus 5 from Anthropic when it comes to working on complex engineering tasks. On benchmarks like DeepSWE, for example, it matches Opus 5 and beats GPT-5.6 Sol and Sonnet 5.

There’s a caveat here, though, in that Google also stresses that “3.8 Flash works harder.” But working harder means it will also use more tokens, and Google, to its credit, is open about that and notes that, “On complex tasks, it exhibits greater diligence — executing extra reasoning steps, and calling tools iteratively. At times, the model might use more tokens to maximize performance, especially at higher effort levels.”

To counteract this, developers can choose between different reasoning modes, though, just like with previous models.

![](https://cdn.thenewstack.io/media/2026/09/ce2cb6f2-hromzf5boaalg1y-836x1024.png)

Credit: Google.

Google’s benchmarks do not include [Anthropic’s Fable 5.1](https://thenewstack.io/anthropic-fable-5-1-launch/), which was only released a day earlier. That’s a much stronger model, but also far more expensive.

Nobody would call Fable 5.1 a workhorse model, but it’s worth highlighting that on general agentic benchmarks like Terminal-Bench 4.0, where Flash 3.8 scores 19.1%, Fable 5.1 hits 55.8%, and Opus 5 gets to 51.8%. Meanwhile, on Terminal-Bench 2.1, which focuses on coding, Flash 3.8 does better than its competitors.

Terminal-Bench is the outlier here, though, as the Gemini model actually does quite well on other agentic tasks, even when compared to other flagship models.

Where Google’s model still struggles, despite some impressive gains, is on computer use (59% vs. 75.4% on OSWorld-2.0 for Opus 5) and GDPVal, a benchmark that tests models on knowledge work tasks, where Google, at 1545, remains well behind Opus 5 at 1824 but is finally catching up to Sonnet 5 at 1584.

Google notes that it was able to improve the model in such a short time in part because it’s now using agentic loops to improve the models, too. “Both of today’s releases are powered by the same foundational intelligence, and further accelerated by long-running agentic loops designed to recursively evaluate and refine the underlying models,” the team writes.

## Chinese models close the gap

One thing worth noting is that Google’s comparison focuses on OpenAI and Anthropic, but it’s hard not to notice that on some benchmarks like DeepSWE 1.1, some of the Chinese models like GLM-5.3 and GLM-5.3 Flash, as well as DeepSeek v4 Pro and Kimi K3, are very much in the same league, too — and they often offer even better price/performance ratios.

![](https://cdn.thenewstack.io/media/2026/09/8b98daca-gemini-3-8-flash__evals__deepswe.width-2000.format-webp-1024x576.webp)

Credit: Google.

## Cyber benchmarks

As for Flash 3.8 Cyber, Google says it delivers “frontier-level performance in autonomous vulnerability discovery” on CyberGym, where it beats 3.5 Flash Cyber, which was released in July, and “significantly larger frontier models.”

CyberGym only covers C and C++ code, so Google also tested the model on an internal benchmark that spans 20 languages and reports a success rate above 70% there.

On Collinear’s CWE-Bench, the model scores a pass@1 of 47.2%, just behind “a leading frontier model at 47.8%” that Google doesn’t name.

Benchmarks only go so far, though. Chrome’s security team says the model produced 2.6 times more correct patches than “the best commercial models that are much larger,” while Wiz reports 7.5% to 9.7% higher recall on its internal penetration testing benchmark at 2.3 to 5.2 times lower cost.

## Safety

On the safety front, Google says that 3.8 Flash is shipping “with safeguards against misuse in the domains of Chemical, Biological, Radiological, and Nuclear (CBRN) and cyber offense, while enabling beneficial use cases, as per our [Frontier Safety Framework](https://deepmind.google/blog/strengthening-our-frontier-safety-framework/).”

Gemini Flash 3.8 Cyber has a more permissive set of safeguards, but that’s why it is only available to a select group of users, too.

Google does note that the new model is far more robust when it comes to prompt injections, too, with (almost) class-leading results in the Gray Swan IPI benchmark, for example.

![](https://cdn.thenewstack.io/media/2026/09/cce3a0e3-gemini-3.8-flash_evals_attack__l.width-2000.format-webp-1024x576.webp)

## Gemini Pro?

The release of the next Gemini Pro model will be interesting. These Flash models are improving rapidly, and while Google has fumbled the Pro launch a bit, that model may have been worth the wait. Google’s strategy to bet on its Flash models in the meantime also means that it has been able to push a price/performance narrative that has been harder to tell for other U.S.-based frontier labs.

At this rate, though, we may see a Gemini 3.9 Flash before Gemini 4 Pro arrives.

## Availability

Gemini 3.8 Flash is now available in the usual Google products like Antigravity, Google AI Studio, Android Studio, and Stitch, as well as Gemini Enterprise.

Consumers with AI Pro and Ultra subscriptions can also use it in the Gemini App, AI Mode in Google Search, and Gemini in Google Sheets.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)