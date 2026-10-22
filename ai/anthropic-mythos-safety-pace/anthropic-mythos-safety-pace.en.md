**Anthropic first released Mythos-class models in February 2026**, but CEO Dario Amodei said it delayed broader access until June to build stronger cybersecurity safeguards.

Amodei laid out that reasoning Tuesday in a lengthy post on X, written in response to criticism from Nathan Calvin and defending the company’s approach to AI safety. He conceded the decision may have cost Anthropic a competitive edge. Releasing the models sooner, he argues, would have given organizations less time to prepare their infrastructure for increasingly capable AI-powered cyberattacks.

“We likely sacrificed a significant chunk of a several-month model lead,” Amodei writes.

Anthropic tells *The New Stack* that the delay follows a commitment in its [Responsible Scaling Policy](https://www-cdn.anthropic.com/e670587677525f28df69b59e5fb4c22cc5461a17.pdf) to require a strong argument that catastrophic risk is contained and to delay development and deployment as far as needed until it no longer believes it holds a significant lead.

## Sparring over a strategy under scrutiny

In his [criticism posted Monday](https://twitter.com/_NathanCalvin/status/2112295219765137570), Calvin argues that Anthropic increasingly resembles a company racing to build superintelligence while weakening its commitments to preventing dangerous AI outcomes.

He points to the company’s more than $500 billion in computing deals, its growing use of AI to develop new models, and changes to its [Responsible Scaling Policy](https://www.anthropic.com/responsible-scaling-policy), which establishes safeguards as models become more powerful.

> “When Anthropic strays and makes mistakes, why do the mistakes systematically tend to guard and favor Anthropic’s interests?”

“When Anthropic strays and makes mistakes, why do the mistakes systematically tend to guard and favor Anthropic’s interests?” Calvin asks.

Anthropic’s February policy revision, version 3.0, replaces earlier requirements, which Amodei now calls too rigid, with an approach that emphasizes transparency, risk reporting, and independent evaluation. The current version is 3.4, effective July 8.

In its Frontier Safety Roadmap, Anthropic says it will “strive to avoid situations where we revise the goals in a less ambitious direction because we simply can’t execute.”

## Why Anthropic removed its safety pledge

The February revision also removes a 2023 commitment never to train an AI system unless Anthropic could guarantee in advance that its safety measures were adequate. Calvin argues that the change weakens Anthropic’s unilateral commitment to slow or stop development.

Anthropic says the updated policy is its strongest yet on public accountability and transparency.

Anthropic’s chief science officer, [Jared Kaplan](https://www.linkedin.com/in/jared-kaplan-645843213/), told *[Time](https://time.com/7380854/exclusive-anthropic-drops-flagship-safety-pledge/)* magazine for a story published in February that the reasoning is practical.

“We felt that it wouldn’t actually help anyone for us to stop training AI models,” Kaplan says, adding that unilateral commitments didn’t make sense “if competitors are blazing ahead.”

> “Our strategy has always been what I’ve called the ‘race to the top,’”

Amodei offers a similar defense in his Tuesday X post.

“Our strategy has always been what I’ve called the ‘race to the top,'” he writes, arguing that Anthropic can shape industry safety standards more effectively by staying at the technological frontier.

He concedes Anthropic could have handled three of Calvin’s points better, including its handling of the draft bill, and calls the Responsible Scaling Policy critique “the most substantive item,” but argues that the company has repeatedly sacrificed commercial advantages for safety. Beyond the Mythos delay, he points to restrictive biological safeguards, support for AI regulation, and export controls on advanced chips and chipmaking equipment.

Amodei argues these decisions show a willingness to put safety ahead of short-term profits, even when they carry substantial costs, and that Anthropic’s strategy has remained consistent.

## April–June: Anthropic expands access to Mythos

Anthropic first released Claude Mythos Preview in April through [Project Glasswing](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/), giving selected partners, including Amazon, Apple, Microsoft, CrowdStrike, and the Linux Foundation, access to the model’s vulnerability-discovery capabilities for defensive work while keeping it out of reach of ordinary developers.

On June 2, Anthropic [expanded the program](https://www.anthropic.com/news/expanding-project-glasswing) to approximately 150 additional organizations in more than 15 countries. Anthropic warns that, for most partners, a major attack could affect more than 100 million people, by Anthropic’s estimate. It also says “hundreds of thousands of organizations, researchers, and maintainers” will likely need access to advanced cybersecurity capabilities before Anthropic can release Mythos-level models more broadly.

## June: Fable is released and then pulled back

Anthropic released [Claude Fable 5 on June 9](https://thenewstack.io/anthropic-claude-mythos-fable-5/), a Mythos-class model with additional cybersecurity and biological and chemical safeguards that the company says make it suitable for general use. Its sibling, Mythos 5, shared the same underlying model but carried fewer cybersecurity restrictions and remained limited to trusted partners. Anthropic outlined the distinction in its [launch announcement](https://www.anthropic.com/news/claude-fable-5-mythos-5).

Three days later, on June 12, a U.S. government export-control directive [forced Anthropic to suspend both models](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/). The order barred access by foreign nationals, including the company’s own employees. Because the order covered foreign nationals everywhere, Anthropic said the only way to comply was to [disable the models for all customers](https://www.anthropic.com/news/fable-mythos-access), though it publicly disagreed with the directive.

The Commerce Department [lifted the controls on June 30](https://thenewstack.io/how-anthropic-is-bringing-fable-5-back/). In its [announcement confirming the decision](https://www.anthropic.com/news/redeploying-fable-5), Anthropic outlined plans for closer government cooperation on pre-release testing, information sharing, and cybersecurity standards for future models. Fable 5 returned worldwide on Anthropic’s own platforms on July 1, while Mythos 5 had already regained access for select U.S. organizations on June 26.

Access rules now shape what developers can use. Anthropic’s [expanded Cyber Verification Program](https://www.anthropic.com/news/cyber-verification-program) gives security professionals access to its most capable models, including Claude Mythos 5.1, through three tiers based on the scope of their cybersecurity work. Existing Glasswing members receive access to [the least restricted tier](https://thenewstack.io/anthropic-cyber-access-tiers/), while new organizations applying for that tier undergo a review involving Anthropic and the U.S. government.

In Anthropic’s own tests, Defense Access, the most restricted of the three tiers, blocked Claude Opus 5.5 at some point in 46 of 50 trials on CyScenarioBench, a multi-stage offensive-security benchmark, while Red Team Access blocked none.

The announcement includes no comparable defensive benchmark, making it hard to determine how often the restrictions might interfere with legitimate security work. Anthropic acknowledges its safeguards produce false positives on secure coding and offers a form for users to report wrongful blocks.

## Pacing the frontier and the policy playbook

Amodei acknowledges that AI development could soon move faster than the safeguards built to govern it. “We are nearing that point,” he writes in the X post.

Anthropic’s own research illustrates why the company is concerned. In its June report, “[When AI builds itself](https://www.anthropic.com/institute/recursive-self-improvement),” Anthropic states that as of May, Claude authored more than 80% of the code merged into Anthropic’s codebase.

That figure measures lines of production code attributed to Claude, not autonomous control over the company’s engineering decisions. Anthropic calls the figure conservative, and leadership has separately estimated that Claude writes 90% or more of code when scripts and experimental code are included.

> “We are not there yet, and recursive self-improvement is not inevitable.”

“We are not there yet, and recursive self-improvement is not inevitable,” the authors write.

In his June essay, “[Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential),” Amodei argues for stronger government oversight of frontier AI development. The proposal calls for independent evaluations, public risk reporting, and giving governments the legal authority to block or deter deployments that pose catastrophic risks. Anthropic’s October draft bill would allow a block only when a model is judged to imminently risk killing or injuring more than 50 people or causing more than $1 billion in damages.

Amodei outlined a three-stage plan in September in an essay titled “[We Must Pace the Frontier](https://darioamodei.com/post/we-must-pace-the-frontier)” that begins with independent evaluators working inside AI companies, expands to coordination among democratic countries, and ultimately calls for agreements involving both democratic and authoritarian governments. Anthropic argues that pacing the frontier requires industry-wide and global coordination alongside steps individual labs can take on their own.

The company’s [Frontier Safety Roadmap](https://www.anthropic.com/responsible-scaling-policy/roadmap), whose most recent entries are dated October 19, sets December 15, 2026, as the target for a policy proposal on how governments can support deeper access for embedded evaluators.

By January 15, 2027, Anthropic plans to either publish a policy framework to shape the pace of AI development or explain why it decided not to. The roadmap warns that automated AI research “could accelerate progress faster than governance or safety measures can keep up.”

The company acknowledges that its roadmaps may change, saying it will publish updates on whether it meets its goals.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)