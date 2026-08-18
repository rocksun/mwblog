After it joined Project Glasswing and gained access to experiment with Mythos Preview, security and AI company [Rubrik](https://www.rubrik.com/) learned it didn’t have the engineering capacity to keep up with [the model’s vulnerability-hunting capabilities](https://thenewstack.io/will-it-mythos-benchmark).

[Arvind Nithrakashyap](https://www.linkedin.com/in/arvind-nithrakashyap-752280/), CTO and co-founder, Rubrik, says Mythos was instantly finding complex vulnerability chains that slipped past Rubrik’s usual security tools and methodology, including identifying relationships between components across large codebases that a conventional scan or a single engineer’s review couldn’t catch. And that surge in findings created a prioritization bottleneck Rubrik’s existing engineering team wasn’t prepared to handle:

“When we first saw the readout of potential issues, our immediate instinct was to treat it as a capacity problem,” Nithrakashyap tells *The New Stack*, adding Rubrik was even considering hiring more human reviewers to accommodate the larger volume.

But the pivot away from this idea was swift. “We quickly abandoned the plan,” he continues, “as we realized there was no way human-driven remediation could keep pace with AI-speed discovery.”

## Old workflows don’t work with AI-led discovery

Only vetted partners that are invited to Project Glasswing get access to Mythos Preview. Rubrik joined that list in June when Anthropic [expanded](https://thenewstack.io/anthropic-glasswing-mythos-cybersecurity/) the project to roughly 150 organizations across 15 countries.

> “We quickly abandoned the plan…as we realized there was no way human-driven remediation could keep pace with AI-speed discovery.”

Once onboard, Rubrik assembled a multi-functional engineering and infosec team to enable high-fidelity threat discovery and elimination, leaning on automation whenever possible rather than scaling its base of human reviewers.

“The focus was to build an effective harness,” says Nithrakashyap, “that manages tool calls and checkpoints, adds business context, security context, and trust boundaries.” Specifically, he tells *The New Stack* the goal was to build a software layer around Mythos that could cut down the number of findings that ultimately make it to engineers for review and remediation.

As Nithrakashyap explains it, Rubrik’s team first uses Mythos to run a whole-repository scan, leveraging those initial findings to then inform progressively more targeted passes. These subsequent passes then weed out the noise to ensure only high-quality findings are routed to appropriate teams and prioritized accordingly.

According to Nithrakashyap, it was only after introducing those targeted passes that Rubrik’s engineering team was able to build a workflow that could relay high-priority, actionable findings from Mythos and make remediation more manageable for engineers.

## The harder question: what not to automate

With Mythos flagging vulnerabilities at rates Nithrakashyap claims aren’t feasible for human-led remediation, he says building automation that can match the rate of discovery is the only way to move forward. But doing so comes with decisions about where to let machines handle remediation and where only human judgment will do.

> “Mythos has shown us that AI actually increases the demand for engineering rigor in the systems that surround it.”

“Surprisingly, we ran into this question about what not to automate quite often,” says Nithrakashyap, calling out the inherent conflict between “trustworthy automation” and “maximum automation.” As he explains to *The New Stack*:

“To maintain trust, we chose to limit automated remediation to a deliberate, tightly-scoped subset of vulnerability classes where machine-driven fixes are highly reliable and well defined.” This way, only vulnerabilities within those predefined classes can move along the automated path. Everything else Mythos surfaces that doesn’t fall into those categories gets routed to engineering teams where human judgment can own the final fix.

## More findings, new bottlenecks

Rubrik’s learnings after one month with what Anthropic [calls](https://thenewstack.io/claude-mythos-preview-simulation/) its “most capable model” indicate that most existing engineering workflows likely aren’t ready to keep up with the model’s speed of discovery. As Nithrakashyap tells *The New Stack*, “Mythos has shown us that AI actually increases the demand for engineering rigor in the systems that surround it.”

Adapting requires integrating structural context directly within the harness and building systems to categorize and filter Mythos findings into actionable insights for remediation.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)