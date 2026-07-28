The [current maelstrom of discussion](https://thenewstack.io/microsoft-nvidia-meta-and-open-weights/) surrounding the use of [open-source software](https://thenewstack.io/open-source/) and [open-weight AI models](https://thenewstack.io/chinese-frontier-models-quantization/) appears to be splitting opinion on what constitutes legitimate openness versus actions that might constitute theft and create new [cybersecurity](https://thenewstack.io/ai-is-changing-cybersecurity-fast-and-most-analysts-arent-ready/) vulnerabilities.

In a direct move to address these industry-wide concerns, 33 partners announced on Monday the formation of the new [Open Secure AI Alliance](https://www.opensecureaialliance.org/) and how the newly created body will develop techniques and tools to safeguard software by rapidly identifying and patching vulnerabilities.

## Open Secure AI Alliance inaugural partners

The inaugural partners of the Open Secure AI Alliance are [Nvidia](https://thenewstack.io/microsoft-nvidia-meta-and-open-weights/), Adobe, Cadence, [Capital One](https://thenewstack.io/capital-one-developer-enablement/), [Cisco](https://thenewstack.io/cisco-is-using-ebpf-to-rethink-firewalls-vulnerability-mitigation/), Cloudera, [Cloudflare](https://thenewstack.io/cloudflare-ai-web-economics/), [Cognition](https://thenewstack.io/coding-agents-team-infrastructure/), CrowdStrike, [Databricks](https://thenewstack.io/databricks-is-rebuilding-the-data-stack-for-ai-agents/), Dell Technologies, [DoorDash](https://thenewstack.io/doordash-cli-agents-order/), [Elastic](https://thenewstack.io/agentic-ai-observability-operations/), [HPE](https://thenewstack.io/hpe-agentic-ai-ops-burnout/), Hugging Face, [IBM](https://thenewstack.io/ibm-bob-agentic-development/), LangChain, the [Linux Foundation](https://thenewstack.io/agentic-ai-foundation-launch/), [Microsoft](https://thenewstack.io/microsoft-scout-openclaw-runtime/), [NetApp](https://thenewstack.io/apache-cassandra-6-features/), Nous Research, [OpenClaw](https://thenewstack.io/persistent-ai-agents-compared/), [Palantir](https://thenewstack.io/palantir-nvidia-sovereign-ai/), [Palo Alto Networks](https://thenewstack.io/palo-alto-portkey-ai-gateway/), [Salesforce](https://thenewstack.io/context-is-everything-sales-force-data-360/), [ServiceNow](https://thenewstack.io/servicenow-ai-governance-agents/), [Snowflake](https://thenewstack.io/snowflake-coco-coding-agent/), Synopsys, Thinking Machines Lab, TrendAI, [Red Hat](https://thenewstack.io/red-hat-introduces-its-first-out-and-out-ai-platform/), Reflection AI, and [SpaceXAI](https://thenewstack.io/musk-spacexai-grok-open-source/).

It’s a grouping of some of the most influential names in technology, but also includes two notable exceptions: OpenAI and Anthropic, two closed, proprietary AI labs. Their absence is understandable, as they operate closed labs and open-weight AI models are effectively the competition.

[Nvidia](https://thenewstack.io/nvidia-open-weight-letter/) VP of enterprise platforms, [Justin Boitano](https://www.linkedin.com/in/justinboitano/), released a statement to say that open-weight models are foundational to American AI leadership and cybersecurity.

“To maintain U.S. leadership in the AI industrial revolution, the infrastructure that runs our economy needs safe, secure access to both closed and open models,” Boitano writes. “For cybersecurity, open models and open harnesses are essential because they broaden defensive capability, increase transparency for defenders, and complement frontier closed models with customizable, localized controls.”

As regulators grapple with AI safety, Boitano predicts it will be important to “recognize open models and open tooling as defensive assets” — thus enabling transparency, independent evaluation and shared remediation.

## Nobody can subpoena a downloaded weights file

[Mark Vigoroso](https://www.linkedin.com/in/markvigoroso/), founder & CEO of technology consultancy firm [The Enterprise Edge](https://www.tee5.ai/about), tells *The New Stack* that AI regulators have traditionally “built their entire AI safety apparatus” around auditing a handful of closed labs. And now, that approach is out of date.

“Open weight models blew past that closed model approach months ago,” Vigoroso says. “This alliance is an admission that the actual safety work now has to happen in the infrastructure layer: patch cycles, provenance, identity around who’s deploying what, because nobody can subpoena a downloaded weights file.”

> “This alliance is an admission that the actual safety work now has to happen in the infrastructure layer: patch cycles, provenance, identity around who’s deploying what, because nobody can subpoena a downloaded weights file.”

Vigoroso argues that the AI safety debate is “stuck on model-level controls”, while the real regulatory gap is provenance of infrastructure and identity, i.e., knowing where a model came from, who deployed a model and what it touched, not just whether the model itself is safe.

“Groups like the [EU AI Office](https://digital-strategy.ec.europa.eu/en/policies/ai-office), NIST’s Center for AI Standards and Innovation ([CAISI](https://www.nist.gov/caisi)), and the UK’s AI Security Institute ([AISI](https://www.aisi.gov.uk/)) focus almost *entirely* on frontier closed models. Open weight models ([Mistral](https://thenewstack.io/mistral-vibe-cloud-agents/), DeepSeek, and others) fall into a regulatory blind spot: Once weights are released, there’s no way to enforce downstream safety obligations.

Current regulatory frameworks for AI models assume a single accountable deployer; open source has none. That’s the real story: Regulators are writing rules for a centralized world while the ecosystem is decentralizing, Vigoroso says.

While detailed operational information explaining the intended actions of this alliance is currently scant, Nvidia has highlighted that it is contributing solid research to the Open Secure AI Alliance to speed the development of new cybersecurity tools and techniques.

## Harnesses integrate with models, making agents easier to test

The open source Nvidia Labs Object-Oriented Agent (NOOA) project is now available on GitHub to make advanced AI safety capabilities more accessible for agent harnesses. This research framework enables harnesses to integrate with models to make agent behavior easier to test, trace, audit, and govern.

[Aparna Rayasam](https://www.linkedin.com/in/aparna-rayasam/), CEO of verified identity and end-to-end encryption company [Atsign](https://atsign.com/), tells *The New Stack* that the “AI blitzkrieg conversation has reached a critical inflection point.” This moment is one where we cannot build the next era of open cognitive innovation on top of what Rayasam calls “legacy, Swiss-cheese infrastructure.”

> …the “AI blitzkrieg conversation has reached a critical inflection point.”

“The formation of the Open Secure AI Alliance proves that AI safety isn’t just an algorithmic math problem — it is a foundational networking problem,” Rayasam says. “The massive, distributed pipelines required to train and run modern AI demand an entirely new paradigm of trust. True safety means ensuring that the data pipelines feeding these models are inherently invisible, un-attackable, and completely stripped of open network perimeters.”

The key notion here is that we are moving from a world of protecting data at rest to a world where the connective tissue of AI must be secure by design.

## One AI vendor to secure them all? No thanks.

Founder and CPO of agentic identity and permissions security company [Reco](https://www.reco.ai/), [Gal Nakash](https://www.linkedin.com/in/naksec/), tells *The New Stack* that the launch of the Open Secure AI Alliance is an “important signal” which underlines why AI security can’t be solved by one vendor or one closed framework.

“Jensen Huang’s point that [every SaaS company will become a GaaS company](https://www.youtube.com/shorts/XsUvLCQeu1k) captures why this matters now: Software is shifting from passive tools people log into, to AI agents that access data, take actions, and execute workflows,” says Nakash. “Open source tools and shared standards can help the industry move faster, but they need to be grounded in real enterprise context across identity, permissions, data access and behavior.”

[Chris Boehm](https://www.linkedin.com/in/chrisboehmii/), Field CTO at automated, identity-driven microsegmentation company [Zero Networks](https://zeronetworks.com/resource-center/webinars/cyber-security-and-resilience-regulation-uk?cid=701Uc000012QSS2IAO&utm_term=Zero_NetworksZero_Networks&utm_campaign=brand-search-tofu-uki&utm_source=google&utm_medium=cpc&utm_id=23984533379&utm_content=practioner&hsa_acc=1154373649&hsa_cam=23984533379&hsa_grp=199586129484&hsa_ad=814699429847&hsa_src=g&hsa_tgt=kwd-2304959397113&hsa_kw=zero%20networks&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gad_campaignid=23984533379&gbraid=0AAAAACkyBiw_MB53L1xqCfSbKA96Sadtp&gclid=Cj0KCQjw4JbTBhCoARIsALWUaBvEF-62etHZVtfKXihNJWwN2jEzDN9C6CIUfRW9Yj3FRjnbeTLN17IaAmk_EALw_wcB), tells *The New Stack* that news of the Open Secure AI Alliance makes him feel like he’s seen this before somewhere.

“This looks like the Trusted Platform Module ([TPM](https://support.microsoft.com/en-us/windows/security/devicesecurity/enable-tpm-2-0-on-your-pc)) at Microsoft story all over again,” Boehm says. “It’s a case of an industry group defining what trusted hardware means, the platform vendors adopt it, and within a few years it’s a procurement requirement rather than a suggestion.”

He explains that “Windows 11 did exactly that with TPM 2.0 and Secure Boot”, and both Linux and Apple adapted. “I’d expect the same for AI infrastructure, where attested silicon becomes the floor for regulated workloads, and the vendor list narrows to whoever can meet it,” predicts Boehm.

> “This looks like a case of an industry group defining what trusted hardware means, the platform vendors adopt it, and within a few years it’s a procurement requirement rather than a suggestion.”

## A more global and geographically-inclusive approach is needed

[Amanda Brock](https://www.linkedin.com/in/amandabrocktech/), CEO of open technology body [OpenUK](https://openuk.uk/), tells *The New Stack* that the Open AI Alliance is undoubtedly a great starting point, particularly with [OpenAI’s security woes](https://thenewstack.io/openai-huggingface-sandbox-breach/) it divulged last week.

“But, like the [open letter on US Leadership in open weights](https://www.microsoft.com/en-us/corporate-responsibility/topics/open-weight/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform), this is a US response to a US challenge,” Brock says. “[Rumors of a forthcoming Presidential Executive Order](https://www.axios.com/2026/07/20/ai-us-china-open-source-kimi) to [close down open models](https://www.semafor.com/article/07/15/2026/white-house-not-ruling-out-action-on-open-source-ai-models) have been circulating for weeks — and worsened by the administration being thrown into turmoil over China’s [Kimi K3](https://thenewstack.io/kimi-k3-open-weight-coding/).”

For this alliance to succeed, Brock insists that it will need to take a more “global and geographically-inclusive approach”, beyond the US-centric founding members.

“It must also engage the open source ecosystem of individuals and innovators who are building the infrastructure, agentic harness functions and developer tools for AI. It’s important to realize that open AI infrastructure development shifts the innovation into the hands of the many, in direct opposition to the small number of corporate creators of frontier models,” Brock adds.

Nvidia’s Boitano echoes Brock’s view. In a blog post reviewed in draft by *The New Stack*, he writes that “open models turn more AI users into AI builders,” expanding opportunity, accelerating innovation, and keeping progress from being concentrated in only a few organizations or regions.

Boitano concludes by saying that open models also enable independent scientific research into how AI systems behave, allowing researchers to understand, evaluate, and improve them. It’s all about what he has called making broad, continuous defense possible.

Looking ahead, it feels like the next wave of AI safety bodies, movements, or alliances won’t just be model auditors—they’ll be trust-infrastructure standards bodies (encompassing identity verification, content provenance, credence, etc.) using borrowed approaches to governance and compliance. Ultimately, this may be the only enforcement layer that survives open weight proliferation.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)