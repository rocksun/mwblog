Cognition built its newest coding model on a foundation that anyone can download, yet the company is keeping its own finished version locked away.

Released Wednesday, [SWE-2 Flash](https://cognition.com/blog/swe-2-flash) costs one-fifth as much as Cognition’s larger SWE-2 model and generates tokens roughly three times faster, according to the company. Built on Thinking Machines Lab’s open weight Inkling-Small, the new model comes with a catch: Cognition is keeping its weights private, citing cybersecurity concerns.

Inkling-Small is a 276-billion-parameter mixture-of-experts model with 12 billion active parameters that Thinking Machines Lab, the startup led by co-founder and CEO [Mira Murati](https://www.linkedin.com/in/mira-murati-4b39a066/), released on July 30 under an Apache 2.0 license, which means anyone can pull the weights from Hugging Face and build on them.

> “a practical way to turn a weak open base into a usable agent model,”

Cognition says the bulk of its performance gains came from adding a mid-training stage before reinforcement learning, and the numbers it published are striking — on Terminal-Bench 4.0, Flash scored 20% against Inkling-Small’s 0.9%, and its FrontierCode 2.0 score climbed from the base model’s 3.2% to 24%, narrowly edging out SWE-2’s 23.8%.

CultOfAI, an AI commentary [account on X](https://x.com/TheCultOfAI/status/2118664755514876078), calls mid-training “a practical way to turn a weak open base into a usable agent model,” though the same account cautions that the figures are Cognition’s own rather than independently verified.

## Cheaper, faster, still trailing

Flash doesn’t keep pace with the larger model on every test, coming within a hair on SWE-Bench Pro v2 Hard at 89.9% to SWE-2’s 90.6% but trailing on DeepSWE 1.1 and Terminal-Bench 4.0, while competitors including Claude Haiku 5.5 and DeepSeek V4.1 Flash outscore it on several benchmarks.

## Open base, private weights

Building on a model released under Apache 2.0, one of the more permissive [open source licenses](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/ "open source licenses"), doesn’t obligate Cognition to open its own work, since the license lets developers modify and commercialize derivatives without sharing their changes — so keeping SWE-2 Flash’s weights private sits well within the company’s rights even as it cuts against the spirit of the base it borrowed.

The decision caught the attention of [David Hendrickson](https://www.linkedin.com/in/david-hendrickson-667971102/), CEO of GenerAIte Solutions, who praised Cognition for turning Inkling-Small into a “coding beast” but [pointed out on X](https://x.com/TeksEdge/status/2118100981309190355) that “the improved weights aren’t public.”

His observation comes as open-weight models close the performance gap with proprietary alternatives and become [serious contenders for coding platforms](https://thenewstack.io/kimi-k3-open-weight-coding/). Cognition’s decision to keep its improved model private contrasts with that trend.

Cognition says it’s building a program to share the weights with select industry partners and research labs that could inspect, fine-tune, and run the model on their own infrastructure, an arrangement likely to appeal to enterprises and governments wary of sensitive code leaving their systems.

More details are coming in the next few weeks, the company says, and for now it remains unclear who will qualify, what restrictions they’ll face, or whether they’ll be allowed to share models built on SWE-2 Flash.

## Cybersecurity drives the lockdown

Cybersecurity is central to Cognition’s decision to restrict the weights. The company included cybersecurity tasks in Flash’s training, raising its ExploitBench score from Inkling-Small’s 11.3% to 34.8%. That’s a significant improvement, although the benchmark doesn’t establish how the model would perform in real-world attacks or whether releasing its weights would increase the risk of misuse.

> Cognition points to a rise in AI-enabled cyberattacks as justification for limiting access.

The concern is that capabilities used to find and investigate vulnerabilities could just as easily help attackers. Cognition points to a rise in AI-enabled cyberattacks as justification for limiting access. Similar challenges are trending across the industry; AI tools can now [identify tens of thousands of potential vulnerabilities in open-source projects](https://thenewstack.io/anthropic-oss-scanner-vulnerabilities/) faster than maintainers can investigate and fix them.

## American model, limited access

Cognition describes SWE-2 Flash as a fully American coding model and claims it beats every American open-weight model on leading evaluations, including models three times its size, a qualification that carries weight because the company’s own benchmark table shows models built outside the United States, DeepSeek V4.1 Flash among them, outscoring Flash on several tests.

Developers can try SWE-2 Flash through Devin Desktop and CLI, and the model is free through November 30.

> Cognition describes SWE-2 Flash as a fully American coding model and claims it beats every American open-weight model on leading evaluations

[Cyber Security Expert
Step by step guide to becoming a Cyber Security Expert in 2026

Fundamental IT Skills
CTFs (Capture the Flag)
Operating Systems
Networking Knowledge
Certifications
Security Skills and Knowledge
Cloud Skills and Knowledge
Programming Skills](https://roadmap.sh/cyber-security?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=cognition-flash-private-weights)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)