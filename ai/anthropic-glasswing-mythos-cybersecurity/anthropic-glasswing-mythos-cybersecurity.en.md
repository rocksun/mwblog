Anthropic laid down some sobering words on Tuesday.

“**A successful attack on their codebase could be catastrophic.** For most partners, we estimate that a major attack could affect more than 100 million people, with important ramifications for both global and national security,” reads an [announcement](https://www.anthropic.com/news/expanding-project-glasswing) from the AI giant.

The organization’s warning aligned with news of an expansion of [Project Glasswing](https://thenewstack.io/openai-daybreak-anthropic-glasswing/), a collaborative effort designed to secure global software code resources. The project provides secure, approved access to [Claude Mythos Preview](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/), which comprises Anthropic’s group of models that are more powerful than the [Opus family](https://thenewstack.io/claude-opus-48-release/) of large language models available to the general public.

> “AI models have reached a level of coding capability where they can surpass all but the most skilled humans at finding and exploiting software vulnerabilities.” —Anthropic

Anthropic [announced](https://www.anthropic.com/glasswing) Project Glasswing on April 7, stating that 50 organizations would have access to its powerful AI tools. The announcement came paired with a statement that reads in part, “AI models have reached a level of coding capability where they can surpass all but the most skilled humans at finding and exploiting software vulnerabilities.”

## Initial Project Glasswing members

Key initial member partners in Project Glasswing included Amazon Web Services, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorgan Chase, the Linux Foundation, Microsoft, Nvidia, Palo Alto Networks, and Anthropic itself.

On Tuesday, Anthropic announced that it was adding to the Glasswing project “approximately 150 new partners:

*We’re now expanding Project Glasswing. Following several weeks of close collaboration with our Project Glasswing partners, the security industry, open-source software maintainers, and the US government, we’re extending the partnership to approximately 150 new organizations. Each one will need to meet our security requirements before they gain access.*

Those groups, as well as the 50 or so that were part of Glasswing when it was announced in April, crucially have early access to Mythos Preview, its highly advanced AI model that Anthropic says has already found “thousands of high-severity vulnerabilities”, including a number in “every major operating system and web browser” today. Given the rate of AI progress, the organization has predicted that “it will not be long” before such capabilities proliferate, potentially beyond actors who are committed to deploying them safely.

Highly aware of the risks associated with model misuse by bad actors and emphasizing the use of Claude Mythos to [prevent, rather than aid, cyber risk](https://thenewstack.io/claude-mythos-preview-simulation/) from the start, Project Glasswing partners pointed the pre-release software at their codebases and found more than 10,000 high- or critical-severity security flaws.

## How is Project Glasswing being expanded?

The 150 or so new partners — Anthropic doesn’t offer a specific figure — joining Project Glasswing were not identified in Tuesday’s announcement. Originating in around 15 countries, the project seeks to further expand its geographical reach.

“The group covers several industries that weren’t well represented in our initial cohort, such as power, water, healthcare, communications, and hardware. And many of the new partners are vendors — companies or nonprofits that maintain codebases that are relied upon by lots of other organizations around the world, including governments,” the company said.

## A multiplicity of Mythos-class models

The initiative was formed in response to what Anthropic has said it has been “warning about for some time,” i.e., that within 6 to 12 months the team expects that “many other AI companies” will have Mythos-class models, which, of course, could be released without safeguards to prevent misuse.

“We see our role as twofold,” states Anthropic. “First, to help the software industry adapt by safely providing wide access to better models, tools, and common infrastructure. Second, to steadily shift the support we provide, from finding vulnerabilities to disclosing, fixing, and deploying patched software.”

Apparently, as genuinely collaborative as it was described, the first weeks of Project Glasswing saw participants sharing information and best practices with other partners while working with third parties to triage the model’s findings. Those best practices are intended to lay down methods that can be “replicated widely” by other organizations adapting to new tools of this nature.

## Claude Security scans codebases & suggests patches

To support its work in this space. Anthropic also released [Claude Security in February](https://www.anthropic.com/news/claude-code-security), a service that draws upon the company’s latest public frontier models, including Claude Opus 4.8, to scan codebases and suggest patches. “We’re also releasing – on request, to trusted security teams – [the tools](https://www.anthropic.com/research/glasswing-initial-update) we developed to help Project Glasswing’s partners find vulnerabilities more quickly,” said Anthropic.

As Anthropic has said, it views the cybersecurity bottleneck as a matter of now verifying, disclosing, and patching the large number of vulnerabilities that Mythos-class models can surface.

As the super AI model race continues, OpenAI released [GPT-5.5-Cyber](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/) as part of its Trusted Access for Cyber (TAC) program on May 7, and subsequently scaled it up on [April 14,](https://openai.com/index/scaling-trusted-access-for-cyber-defense/) promising that the company is “Fine-tuning our models specifically to enable defensive cybersecurity use cases.”

OpenAI backed up this move and said its approach of scaling cyber defense would move “in lockstep with increasing model capabilities” to guide the testing and deployment of future releases.

> “Anthropic’s Project Glasswing program runs on the opposite model [to open, peer-reviewed standards]. It chooses which findings to send for independent review, and the reviewers are contractors who have been hired in. That’s not third-party validation, that’s editing.”   
> —Justin Beals, Strike Graph

## Edited validation by Anthropic is not good enough

[Justin Beals](https://www.linkedin.com/in/jubeals/), CEO & founder of [Strike Graph](https://www.strikegraph.com/?utm_source=google&utm_medium=cpc&utm_campaign=conv_brand_core_sept&utm_content=homepage&utm_adgroup=&utm_term=strike%20graph&obility_id=162202211228&utm_source=google&utm_medium=ppc&utm_campaign=&utm_term=strike%20graph&utm_content=674373217125+g&hsa_acc=1590697097&hsa_cam=20565699356&hsa_grp=162202211228&hsa_ad=674373217125&hsa_src=g&hsa_tgt=kwd-482754174443&hsa_kw=strike%20graph&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=20565699356&gbraid=0AAAAABq3n6lbWSrnBTaWelqllKKt_Cr_K&gclid=Cj0KCQjw_vnQBhCxARIsADcZyxIlbyhi7oQTjv1tlkj4_yKU8qhuIPCNiiLVUc5OeE3KlCQ3mO03IPkaArevEALw_wcB), an AI-native GRC and compliance management platform, tells *The New Stack*that he thinks a controlled rollout of frontier AI is the right instinct. But he has stated that he has concerns over how vulnerabilities are being assessed and analyzed.

“The engineering community has spent years building open, peer-reviewed standards for how software gets evaluated and trusted,” says Beals. “Anthropic’s Project Glasswing program runs on the opposite model. It chooses which findings to send for independent review, and the reviewers are contractors who have been hired in. That’s not third-party validation; that’s editing.”

Beals wants the broader security community involved with access to independent, third-party evaluation across the full corpus.

“Developers building on top of these models need to know what they’re actually integrating, not a summary of what Anthropic decided to share. As frontier models get deeper into the stack, the technical debt of opaque safety claims compounds. The standard for any infrastructure this consequential should be verifiable transparency, not curated receipts,” Beals clarifies.

It seems like the need for approval is widespread, but a more open and even balance is, too. [Guy Currier](http://linkedin.com/in/guycurrier/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform), an analyst at the Futurum Group, tells *The New Stack* that if we thought drones were the frontier of automated warfare, we’re wrong.

“Software is an equally advanced front, and cyberthreats follow no Geneva Convention and are pervasively present in corporate, public, personal, and political spheres, not just military,” Currier says. “Mythos has had its stumbles and Project Glasswing its valid criticisms (lack of transparency, self-policing), but something broad-based has to be done, and the sooner the better. Anthropic’s leadership is welcome, helpful, and on brand.”

## What’s next for Project Glasswing in 2026?

Looking ahead (which in AI circles may be later this month), Anthropic envisages more for initiatives like Project Glasswing and any that come after it.

“We’re in discussions with third parties about how we might substantially scale up the reviewing and patching of vulnerabilities in open-source software. We’re also working on sharing ideas and best practices for disclosing vulnerabilities to open-source maintainers, with the intent of making these reports easier to triage and to act upon,” states Anthropic in its Tuesday announcement.

Mythos Preview can also be used for penetration testing (simulating a cyberattack to identify how vulnerabilities might be exploited), automating threat detection and response, and rebuilding legacy codebases in memory-safe languages, among many other defensive tasks.

The organization has said it has a “longer-term aim” to support the industry in creating new initiatives, standards, and infrastructure for the era of powerful cyber models.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)