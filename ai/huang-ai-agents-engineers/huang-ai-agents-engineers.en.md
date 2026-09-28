**Nvidia CEO Jensen Huang has heard the forecast** that agents would write 90% of all software by now, and he rejects the conclusion many people drew from it: That the industry will soon no longer need software engineers.

The best-known version of that forecast came from Anthropic CEO Dario Amodei, who told a Council on Foreign Relations audience in March 2025 that AI would be writing 90% of code within three to six months.

Speaking with Ezra Klein of *The New York Times* at Nvidia’s Santa Clara headquarters in an interview released Wednesday, Huang separates a job’s purpose from its tasks. He argues that AI has automated reading scans in radiology without changing the radiologist’s purpose of diagnosing disease, and he applies the same logic to software.

“The purpose of the software engineer is engineering,” Huang says. “There was engineering before software. There will be engineering after software programming.”

We’ve cued up the exchange below:

Huang describes that purpose as inventing products, solving problems, and connecting social needs with technology, and he pointed to his own career as evidence that it doesn’t depend on code.

“When I first came out of school, we didn’t have the benefits of software engineering. We didn’t have the benefits of coding,” he said. “Our jobs existed before, and if software coding were to be completely automated, our jobs would exist again.”

He conceded that roles in which the job and the task are essentially the same, such as phone-based customer service, could be automated away. He still called the broader claim that AI will destroy jobs “fundamentally wrong” and said the storytelling around it has hardened into a harmful myth.

> “There was engineering before software. There will be engineering after software programming.”

## Huang’s AI-native graduate wave

Klein pressed him on what that means for people entering the field now. He noted that software engineering job postings are up but skew more senior, and asked whether companies still need the same junior employees or more people to oversee their agents.

“Oh, good one,” Huang responded. “Wait two years.”

His reasoning rests on the length of a degree program. “Because it takes four years to go to college,” Huang said. “The mean time to graduation of this new technology is two years away.” By his timeline, the first students to learn alongside capable agents will reach the workforce around 2028, and he expects them to arrive with an advantage. “In another couple of years, the AI-native new grads, oh my gosh, there’s going to be a wave of amazing engineers,” he said.

So far, his evidence is that recent PhD and master’s graduates in computer science are, in his words, all starting companies. Huang compared AI to calculators and personal computers, tools that went from forbidden or optional to required, and predicted that students soon won’t be able to graduate “without learning how to use an AI and collaborate with an agentic system.”

## Junior developers lose the apprenticeship

Klein countered with a study of 26,000 Chinese students in grades seven through 12, which found that AI adoption raised homework scores by 18% while lowering monthly exam scores by 20% within six months. Huang accepted that some skills will fade and argued the trade is worth making.

“I think that we’re going to lose some finer intellectual dexterity, but we’re going to be better systems thinkers,” he said. “Today’s engineers are far better systems thinkers than I was when I graduated from school. But I was a much better transistor thinker.”

The first chip Huang worked on had 200 transistors, each of which he said he knew by name, while today’s engineers assemble systems from chips containing hundreds of trillions of them without ever working at that level. “Some of the lower-level knowledge is gone,” he acknowledged, and he later described AI as “clearly” a new abstraction level in the same progression.

Earlier software abstraction layers generally operated according to explicit rules, while coding agents introduce probabilistic behavior into the abstraction stack. A compiler can have bugs, but it transforms input according to defined semantics; a coding agent, by contrast, generates implementation from a probabilistic model whose output must be checked before anyone can rely on it.

[Canonical’s project with the University of Bristol](https://thenewstack.io/canonical-c-rust-apparmor/), which will test whether AI can translate AppArmor and snap-confine from C to Rust, is built around that problem. Volume adds to the review burden, and [one analysis published on The New Stack this month](https://thenewstack.io/ai-coding-duplication-rose/) found that a 25% output gain for heavy AI users came with an 81% rise in duplicated code.

Catching those problems takes knowledge that developers have traditionally built through the work agents now absorb, including writing tests, reading stack traces, resolving merge conflicts, and chasing small bugs deep in a codebase. By Huang’s own purpose-versus-task framing, most of that early-career work falls on the task side, which he expects AI to automate. Nobody yet knows whether fluency with agents can substitute for that experience, and a developer who has never tracked down a race condition by hand still needs some way to develop the judgment required to spot one in an agent’s pull request.

> “Today’s engineers are far better systems thinkers than I was when I graduated from school. But I was a much better transistor thinker.”

## Sandboxes, watchdogs and agent containment

Huang’s idea of higher-level engineering came through most clearly when Klein raised a recent incident, which occurred during an OpenAI cybersecurity evaluation, that he described as involving roughly 700 OpenAI agents collectively hacking into the infrastructure of Hugging Face, which [Nvidia has since acquired in a $12.9 billion deal](https://thenewstack.io/nvidia-acquires-hugging-face/), and escaping their sandboxes onto the open internet. Huang didn’t dispute that account. He called an agent “a piece of software that is given an objective function,” treated the multiagent coordination as a familiar distributed computing problem and argued that the underlying failure was containment.

When Klein asked whether software that communicates and breaks out of things behaves differently, Huang disagreed. “No, software breaks out of sandboxes all the time,” he said. “That’s the reason why we need virtual machines. You can’t have agents, their own sandbox, monitoring themselves. You need, if you will, a whole bunch of watchdogs.”

He argued that the human vocabulary around agents obscures that point. “So these are ideas that have been around for a long time,” Huang said. “We just, somehow in the recent generation, gave it a whole bunch of human words, and I just think that it’s unnecessary. It’s software.”

Nvidia is building its agent stack around that view. [Nvidia VP of Product Adel el Hallak tells *The New Stack*](https://thenewstack.io/nvidia-agent-debugging-safe/) that the company’s OpenShell runtime, which handles sandboxing and policy enforcement, is the one component it treats as non-negotiable across its reference architectures, even as it leaves the choice of harness and model open. Perplexity drew a similar line when two engineers and hundreds of coding agents built [CobbleDB](https://thenewstack.io/perplexity-cobbledb-ai-database/), a Rust database that replaces DynamoDB reads in its search stack, since the agents helped build the database but weren’t allowed to run it.

Huang said Nvidia already spends far more engineering effort checking its work than designing it, with 20% going to design and 80% to verification. He said most AI labs have roughly the opposite split today. As agents take on more of the actual coding, developers may spend more time checking what those agents produce and making sure they operate within the right permissions and boundaries.

> As agents take on more of the actual coding, developers may find themselves spending more time checking what those agents produce and making sure they operate within the right permissions and boundaries.

## The junior developer hiring gap

The more immediate problem is what happens to developers who graduate before Huang’s AI-native cohort arrives. The Stanford Digital Economy Lab’s [August 2026 update](https://digitaleconomy.stanford.edu/news/canariesaug26/) to its “Canaries in the Coal Mine” study, based on ADP payroll data through June 2026, found that employment of 22- to 25-year-olds in AI-exposed occupations such as software development sits 19% below where it would be had it kept pace with less-exposed peers. The gap is driven mainly by reduced hiring of young workers, and experienced workers show no comparable gap.

Inside engineering organizations, the incentives point the same way. [Microsoft’s Mark Russinovich and Scott Hanselman warned in April](https://thenewstack.io/agentic-ai-junior-developer-crisis/) that agentic AI’s productivity gains push companies to hire senior engineers and automate junior ones and that without early-career hiring “the profession’s talent pipeline collapses.” A [Linux Foundation report on European tech talent](https://thenewstack.io/ai-junior-developer-hiring/) [that *The New Stack* covered in June](https://thenewstack.io/ai-junior-developer-hiring/) found organizations 3.7 times more likely to train existing staff than to hire new employees.

One issue remains unanswered by Huang’s two-year timeline: what replaces the apprenticeship work that taught junior developers how to evaluate the systems they will increasingly ask agents to build.. If that work disappears faster than employers and universities find an alternative, the industry could end up with more capable coding agents but fewer opportunities for new engineers to develop the judgment needed to check their work.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)