[IBM](https://thenewstack.io/ibm-tackles-shadow-ai-an-enterprise-blind-spot/) is betting that the next competitive frontier in [AI-assisted development](https://thenewstack.io/three-ai-assisted-development-skills-you-can-start-using-today/) isn’t raw [code-generation](https://thenewstack.io/ai-code-generation-trust-and-verify-always/) speed — it’s governance, auditability, and the operational discipline to deploy AI within enterprises that can’t afford to get it wrong.

That’s the pitch behind [IBM Bob,](https://bob.ibm.com/) the company’s new [agentic development](https://thenewstack.io/agentic-ai-is-quickly-revolutionizing-ides-and-developer-productivity/) platform released this week. Bob has been running internally at IBM since June 2025, scaling from 100 developers to more than 80,000 users across IBM’s global workforce.

Surveyed users report an average 45% increase in productivity. On specific teams, the numbers go higher. For instance, the [IBM Instana](https://www.ibm.com/products/instana) team reported an average 70% reduction in time on selected tasks, while the [Maximo](https://www.ibm.com/products/maximo) developer team estimated 69% time savings on code generation and refactoring work that normally takes days.

IBM notes that these are self-reported figures. That caveat matters. But the internal deployment itself is the more interesting data point.

[Neel Sundaresan](https://www.linkedin.com/in/neel-sundaresan-a964a2/), GM of Automation and AI at IBM Software, was part of the team that built the original [Microsoft GitHub Copilot](https://thenewstack.io/github-copilot-interaction-data/) before joining IBM. Sundaresan tells *The New Stack*, “We have all these enterprise workloads we are familiar with. Before we even go knock on the doors of a client, we have a story to tell.”

That story runs from [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) app modernization to [COBOL](https://thenewstack.io/cobol-everywhere-will-maintain/) maintenance to [FedRAMP](https://thenewstack.io/ship-fast-break-nothing-launchdarklys-winning-formula/) compliance work — the kind of legacy-heavy, risk-sensitive development that most AI coding tools aren’t really built for, Sundaresan says. It’s a deliberate positioning move. IBM isn’t chasing Cursor or GitHub Copilot on its own terms.

Bob is structured around the full software development lifecycle — planning, coding, testing, deployment, and modernization — coordinating what IBM calls role-based specialized agents across each stage. The product ships with [Bob Shell](https://bob.ibm.com/docs/shell), a [CLI](https://thenewstack.io/user-interfaces-in-agentic-cli-tools-what-developers-need/) that creates self-documenting audit trails in real time, so every agent action is traceable. Security controls — prompt normalization, sensitive data scanning, real-time policy enforcement, and AI red-teaming — are baked into the workflow rather than bolted on afterward.

IBM says that the last point is a direct response to a known problem: the company cites industry figures suggesting 45% of AI-generated code reaches production without sufficient review.

The multi-model orchestration layer is where Bob’s technical architecture gets interesting. Rather than asking developers to select a model, Bob routes tasks automatically — drawing on [Anthropic Claude](https://thenewstack.io/anthropic-doubles-claude-usage-outside-peak-hours/), [Mistral](https://thenewstack.io/mistral-vibe-cloud-agents/) open-source models, [IBM Granite](https://www.ibm.com/granite), and a set of proprietary, fine-tuned models built specifically for the Bob environment. Lighter completions go to smaller, cheaper models. Complex reasoning tasks go to larger frontier models. Granite, which Sundaresan described as a small model suited primarily to code completion, plays a narrow role. “I would say 90-plus percent of it is all like bigger tasks,” he said.

> “We’re not going to be cost-constrained, but we are going to be cost-informed”

The cost-awareness framing is intentional. “We’re not going to be cost-constrained, but we are going to be cost-informed,” Sundaresan says. He compared letting developers self-select the latest frontier model for simple prompts to “taking your Ferrari to go buy milk” — technically functional, but expensive and unnecessary. IBM doesn’t expose the underlying model to users. The routing is managed automatically.

That’s a meaningful philosophical difference from tools that surface model selection as a feature, IBM says.

## Bob 2.0?

“If you look at the popular coding assistants today, many are forks of VS Code, or forks of something that’s like VS Code, and that gives us the minimal functionality that’s required of an IDE. And then all of the AI goes on top, and you can build amazing experiences,” Sundaresan says. Then, in 2025, “people started saying, ‘Why do I even need an IDE? Why do I even need an IDE? Why can’t I do it in a shell?’ So that’s why Claude Code came along. And that’s why we have Bob Shell…,” he notes.

> “You don’t need an interface. The best interface is no interface… as we go forward to Bob, 2.0 Bob is going to be an agent.”

Sundaresan argues, “You don’t need an interface. The best interface is no interface, right? So, as we go forward to Bob, 2.0 Bob is going to be an agent. You can embed Bob pretty much anywhere you want to, and it’s an AI engine that makes your experience different.”

He explains that Bob could be on your phone or in your application. It could be targeted at consultants, he says.

“We have thousands of consultants,” Sundaresan says. “You could have a bunch of Bob consultants buried in there along with them, because a lot of the consulting workloads are very different from engineering work.”

## Proven at scale — with caveats

Meanwhile, the early customer results are a showcase of the type of work IBM typically does for customers. [Ernst & Young](https://www.ey.com/en_us) is using Bob to accelerate refactoring, test generation, and documentation on its global tax platform. [Blue Pearl](https://www.bluepearl.co.za/#about), a cloud solutions firm, said Bob compressed a typical 30-day Java upgrade into three days, saving more than 160 engineering hours with zero post-deployment defects. [APIS IT](https://www.apis-it.hr/web/naslovnica), working on government modernization with [mainframe](https://thenewstack.io/broadcom-investing-in-mainframe-success-beyond-code/) and [.NET](https://thenewstack.io/net-modernization-github-copilot-upgrade-eases-migrations/) systems, reported 10x faster architecture analysis and 100% accuracy documenting legacy JCL/PL/I code.

“Developing enterprise platforms isn’t just about speed. It’s about understanding deeply embedded logic, maintaining architectural standards, and evolving systems responsibly,” says [Christopher Aiken](https://www.ey.com/en_us/people/christopher-d-aiken), Tax Platforms Leader and Chief Product Officer, Ernst & Young, LLP, in a statement. “EY teams leveraged IBM Bob to apply AI to better interpret complex logic and streamline how changes are introduced, helping create a stronger foundation for scalable transformation.”

The consistent thread across these cases is that all three involve the kind of deeply legacy-entangled enterprise environments that other tools tend to sidestep and that IBM specializes in.

## Where Bob fits

The agentic coding market now has serious entries from AWS (Kiro), JetBrains (Central), GitHub (Copilot Workspace), and a bunch of other players. Sundaresan acknowledged the crowded field directly.

“I don’t think I’m there to take down one of those things,” he says. “There are leaderboards and stuff like that, but if you look under the cover, all of us have similar models. If you don’t have the right models, you don’t even have a play. So really, what value you add on top of these models, how you orchestrate these models, how you maintain costs — that’s the question.”

IBM’s answer is enterprise specificity: decades of Java, [zSystems](https://www.ibm.com/history/eserver-zseries), COBOL, and security compliance experience embedded into the tool’s workflows, not just its marketing. Whether that’s a genuine moat or a repositioning of capabilities the competition is also building toward is a question worth revisiting as the market matures.

Bob is available now as a SaaS offering with a 30-day free trial. On-premises deployment — which would address data residency requirements for regulated industries — is described as a future target with no firm timeline.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)