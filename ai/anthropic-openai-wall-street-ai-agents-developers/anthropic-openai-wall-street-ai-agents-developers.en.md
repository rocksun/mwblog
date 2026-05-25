**Within 72 hours this month**, [Anthropic](https://thenewstack.io/anthropic-agents-managed-aws-claude/) and [OpenAI](https://thenewstack.io/openai-launches-a-no-code-agent-builder/) each launched enterprise deployment arms, announced major [financial services partnerships](https://thenewstack.io/fintech-partnership-streamlines-banking-data-integrations/), and shipped agent tooling targeting Wall Street workflows. The message was the same — the next phase of frontier AI is not about models. It’s about deployment.

For developers, the implications are still unsettled.

## The services land grab

Anthropic’s new services firm — backed by Blackstone and Hellman & Friedman alongside General Atlantic, Apollo, Goldman Sachs, and Sequoia Capital — targets mid-sized enterprises that the large consulting and systems integration firms don’t prioritize. These include community banks, regional health systems, and mid-market manufacturers. Applied AI engineers from Anthropic embed directly with clients alongside the new firm’s own engineering staff, doing workflow discovery, building custom Claude-powered solutions, and supporting clients long-term.

OpenAI’s Deployment Company — “DeployCo” — operates one market segment up, targeting large enterprises with the same forward-deployed engineering model. Its [acquisition of applied AI consulting firm Tomoro](https://www.linkedin.com/posts/tomoro-ai_today-were-announcing-that-tomoro-will-become-activity-7459592053048586240-Mu3o/) brings roughly 150 experienced [Forward Deployed Engineers](https://thenewstack.io/forward-deployed-engineer-fde-openai-google/) (FDEs) from day one, backed by more than $4 billion in initial investment and a partner roster that includes McKinsey, Bain & Company, and Capgemini.

Both companies are betting on the same thesis: that the deployment gap — the widening distance between what frontier AI can do and what enterprises have actually shipped — is the next major revenue opportunity. And both moved on it in the same week.

“I would say there is a tremendous, somewhat surprising opportunity here,” [Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst with the Futurum Group, tells *The New Stack*. “Even within highly regulated industries, where inaccuracies are not tolerated, generative and agentic AI promises to reinvent the way both consumers and financial professionals work with data.”

[Jason Cutler](https://www.linkedin.com/in/jasonrcutler/), SVP of Anthropic Consulting and Engineering at [Caylent](https://caylent.com/), an AWS Premier Partner that recently launched a dedicated Anthropic practice, put it plainly. “A year ago, there was a lot of concern — is Claude going to take the work of services partners like us?” he tells *The New Stack*. “And just in the last week, we’ve seen Anthropic investing in a services company, OpenAI investing in a services company, Google hiring FDEs. We know there’s a need.”

Cutler lists three phases of enterprise AI maturity he sees in the field: training and enablement, operating model and governance, and transformation. Most customers, he says, are still stuck in phase one.

“You can bring AI into an existing process, but you’re not getting the full advantage of AI yet. You really have to recreate the process alongside AI and your employees to really benefit,” he says.

## Finance is the proving ground

The financial services sector has emerged as the one where both labs are concentrating their enterprise push. On May 4, PwC and OpenAI announced a collaboration to build AI agents around the core operating functions of the CFO’s office — planning, forecasting, reporting, procurement, payments, treasury, tax, and accounting close. OpenAI is serving as “customer zero,” building a procurement agent inside its own finance organization before exporting those patterns to enterprise clients. Early results include processing 5x as many contracts with the same headcount using Codex and managing more than 200 investor interactions during a recent fundraise using an IR-GPT tool, the company says.

The next day, Anthropic released 10 ready-to-run agent templates targeting the most labor-intensive workflows in finance: pitch building, KYC screening, month-end close, GL reconciliation, earnings review, and underwriting. The templates ship as plugins in [Claude Cowork](https://thenewstack.io/anthropic-takes-claude-cowork-out-of-preview-and-straight-into-the-enterprise/) and [Claude Code](https://thenewstack.io/anthropics-claude-code-gets-support-for-remote-mcp-servers/), and as cookbooks for Claude Managed Agents. New data connectors — Dun & Bradstreet, Verisk, SS&C Intralinks, Third Bridge, Moody’s — give the agents access to the live data financial professionals use. Claude Opus 4.7, Anthropic says, leads Vals AI’s Finance Agent benchmark at 64.37%.

[Sanjay Subramanian](https://www.linkedin.com/in/sanjaysubramanian/), PwC Partner, US & Global Anthropic Alliance Lead, Global AI Analyst Relations Lead, and a 27-year firm veteran, described the calculus for regulated industries in a briefing with *The New Stack*.

“Financial services companies are looking at documents,” he says. “Intelligent document processing with both structured and unstructured data — that’s been one of the great use cases.”

Subramanian cited an insurance engagement in which an underwriting cycle was compressed from 10 weeks to 10 days through a three-phase deployment: backtesting against historical outcomes, co-delivery with human oversight, and agents providing first-pass deliverables, with underwriters reviewing at checkpoints.

Liability, he was careful to note, has not changed. “The human still has to review it before it goes to the next level. We’re not changing that process. I think it’s too early to change that process.”

## What breaks

Not every use case has worked, however. Subramanian identified a pattern in what fails: high-variance, unpredictable input.

“A supply chain company where they’ve got lots of parts that need to get fixed — if those parts are so diverse, the questions are so diverse, there’s less precision around that outcome,” he says. The cases that work are deterministic and back-testable: ticketing systems, underwriting, and document review against known policy. The cases that struggle are open-ended customer service scenarios where the question space is effectively unbounded, he says.

> “The quality of these models is going up and up… The ability for companies to deploy them is not keeping up. That gap is increasing.” — Sanjay Subramanian, PwC

The harder lesson, he notes, is organizational. “If we look at the models that have come out the last two years — the AI revolution — the quality of these models is going up and up,” Subramanian tells *The New Stack*. “The ability for companies to deploy them is not keeping up. That gap is increasing.”

CIOs conditioned to cost containment resist the temporary increase in spending required to rebuild legacy infrastructure. “That’s probably one of the toughest things to get people comfortable with — that reinvention.”

Cutler echoes the point from a developer angle. The governance conversation is now the first conversation. “When we see things like PHI and credit card authorizations and sensitive information, we need to make sure we’re setting that up correctly on the foundational layer, so that customers feel safe that by leveraging AI, they’re not out of bounds from what they have to do from a compliance standard,” he says.

## The junior developer question

Both Cutler and the Subramanian were asked directly whether junior developers benefit from Claude Code or get squeezed out by it. Both pushed back on the displacement narrative, though with different positioning.

“In some cases, junior developers seem to be catching on even faster,” Cutler says. “In the age of AI, some people are catching up very, very fast, and their own curiosity is lending itself to leveraging the tools effectively.” Caylent has built what it calls a “Playbook Catalyst” — an engagement designed to harvest how developers are actually using Claude Code across an organization, surface what good looks like, and use that to drive enablement for the rest of the team.

Subramanian frames it in terms of baseline shift. “What it’s going to do is re-baseline what normative is — what quality is, what the expectation of time to value is. But it also means that if you’re a new developer, you’re able to learn quicker, you’re able to test things out quicker. We can create automated packages to review your code, to coach you.”

He described AI as effectively substituting for the senior developer mentorship that junior developers often can’t access. “Things that would have taken a long time, you can learn a lot quicker.”

On the [COBOL](https://thenewstack.io/how-cobol-code-can-benefit-from-machine-learning-insight/) modernization front — a significant concern for financial institutions running decades-old core systems — Subramanian described a dynamic that mirrors what developers are seeing elsewhere. Senior developers who were initially skeptical of Claude Code are finding they have more capacity, not less.

“They’re not spending time in meetings where developers working under them need to ask questions,” he says. “They’re actually able to reduce time to value in their deployment capabilities, and allow senior developers to spend time really building new capabilities as they transform from an old code base to a new code base.”

## The fox in the henhouse

Not everyone reads the partnerships as cleanly beneficial. Venture capitalist [Chamath Palihapitiya](https://www.linkedin.com/in/chamath/) issued a [blunt warning on X](https://x.com/chamath/status/2056074605228605580) after the DeployCo announcement: “If you are running a consulting business and you are deploying Anthropic or OpenAI directly into your organization (I’m looking at you, PwC and Accenture) you are letting the fox into the henhouse.”

> “If you are running a consulting business and you are deploying Anthropic or OpenAI directly into your organization… you are letting the fox into the henhouse.”  
> — Chamath Palihapitiya

His argument: “OpenAI and Anthropic are openly funding and starting competitors to you while also using your usage to drive more success for them. This is not a failure on their part but a failure on your part.”

PwC now holds formal partnerships with both Anthropic and OpenAI. It sits in the Claude Partner Network alongside Accenture and Deloitte, and simultaneously co-develops finance agents with OpenAI’s own finance organization. Anthropic’s unnamed services firm targets a market segment just below PwC’s. DeployCo, with McKinsey and Bain & Company as investors, targets the same large enterprises PwC serves.

However, Caylent’s Cutler did not share Palihapitiya’s concern. He says he sees DeployCo’s launch as a validation, not a threat.

“It shows that private equity companies know that this work is going to need to get done. I think it actually validates Caylent going out and creating this practice, because the business is out there today,” Cutler tells *The New Stack*.

Whether that optimism is well-founded, or whether Palihapitiya’s warning proves prescient, could depend on how quickly the labs’ own deployment arms can scale.

For developers building AI in financial services right now, the answer may matter less than the immediate reality, because the infrastructure is being built, the agent templates are shipping, and the certifications are being written. The work is there.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)