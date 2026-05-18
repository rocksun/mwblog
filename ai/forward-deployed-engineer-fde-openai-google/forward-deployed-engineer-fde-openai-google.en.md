*I’m Matt Burns, Chief Content Officer at Insight Media Group. Each week, I round up the most important AI developments, explaining what they mean for people and organizations putting this technology to work. The thesis is simple: workers who learn to use AI will define the next era of their industries, and this newsletter is here to help you be one of them.*

---

OpenAI launched the [Deployment Company](https://openai.com/index/openai-launches-the-deployment-company) this week, a $4 billion push built around staffing corporations and enterprises with forward deployed engineers. The next day, Google Cloud CEO Thomas Kurian [went on LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7460023647102078976) to recruit for the role, while Google Cloud [had 59 related roles open](https://www.channeldive.com/news/google-cloud-forward-deployed-engineering-jobs/820176/) and reported that the company plans to hire hundreds. Anthropic embedded its FDEs inside FIS to co-build an anti-money-laundering agent. ServiceNow and Accenture also launched a joint FDE program.

This all happened within the last 10 days.

If you’ve been wondering which AI job is durable, pays well, and isn’t a hype role like prompt engineer in 2023, the answer is becoming obvious. The forward deployed engineer is the bridge between an AI model and a working production outcome inside a company. And the path to becoming an FDE seems doable: Learn the AI engineering stack, build with real workflows, and train the customer-facing judgment most engineers avoid. Want to get started down this path? I’d highly recommend starting with [Roadmap’s AI Engineering learning path](https://roadmap.sh/ai-engineer). It has everything you need to get started.

## What a forward deployed engineer actually does

The definitive read on FDEs is on our site. In January, Jennifer Riggins published “[Why the forward deployed engineer is tech’s hottest job](https://thenewstack.io/why-the-forward-deployed-engineer-is-techs-hottest-job/)” on *The New Stack* — it’s a clear, well-sourced explainer of the role’s origin, demand, and why AI accelerated it.

**The short version:** An FDE sits between a back-office software engineer and a customer-facing software architect. The role was coined at Palantir, modeled on a forward deployed soldier “stationed overseas, ready for rapid response,” and built on a simple insight: Enterprise data is messy, and shipping a working system requires engineers embedded inside the customer’s environment. AWS principal solutions architect Prasad Rao [described the job](https://thenewstack.io/why-the-forward-deployed-engineer-is-techs-hottest-job/) to Riggins as “hands-on throughout the customer life cycle” — designing, delivering, then staying to fix problems and adjust systems based on what actually happens in the field. The role is having its moment in part because MIT NANDA’s State of AI in Business 2025 report [[PDF](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf)] found that 95% of enterprise generative AI pilots show no measurable business impact — not because the models are bad, but because models don’t deploy themselves.

NetBox Labs co-founder [Mark Coleman](https://www.linkedin.com/in/markrobertcoleman/) put the soft-skill angle to Riggins more bluntly: “People don’t know what they want until they see something they don’t want.” That sentence is the FDE’s job description. The model can generate ten plausible answers. The FDE determines which one the customer actually needs, ships it, and adjusts as the customer’s reaction changes the brief.

> I see the gap between what the models can do in solution and what our team can actually ship. The gap is human work. It’s the FDE’s job.

I’m not a developer. I’m an editor who runs Claude Cowork and OpenAI Codex sessions every day. I see the gap between what the models can do in solution and what our team can actually ship. The gap is human work. It’s the FDE’s job — at industrial scale, with senior compensation, and in OpenAI’s case, with $4 billion of capital pushing it forward.

## The role just went mainstream inside ten days

OpenAI is the headline. The [OpenAI Deployment Company launched Monday](https://openai.com/business/the-openai-deployment-company/) as a majority-controlled venture led by TPG, with Advent, Bain Capital, and Brookfield as co-leads and [Bain & Company, Capgemini, and McKinsey & Company](https://www.pymnts.com/news/artificial-intelligence/2026/openai-launches-4-billion-dollar-company-accelerate-enterprise-ai-adoption/) as founding partners. OpenAI also acquired [Tomoro](https://tomoro.ai/insights/tomoro-acquired-by-openai-deployment-company), a London applied-AI consulting firm, bringing roughly 150 AI engineers and deployment specialists in on day one. Initial backing: more than $4 billion.

This is a serious group of business consultants, each with a full Rolodex and an experienced sales team.

Google’s move is the bigger structural signal. Just a couple of weeks back, at Google Cloud Next 2026, Kurian declared, “The era of the pilot is over. The era of the agent is here,” and laid out plans to expand Google’s field organization, core technology engineering, and forward deployed engineering across industries. His [LinkedIn post on May 12](https://www.linkedin.com/feed/update/urn:li:activity:7460023647102078976/) put numbers behind it: 59 new FDE postings in week one spanning the U.S., India, Brazil, Australia, Mexico, Singapore, South Korea, and Canada, with a career ladder from FDE II to FDE IV.

[Published listings](https://www.google.com/about/careers/applications/jobs/results/101918593561567942-forward-deployed-engineer-applied-ai-google-cloud) show U.S. base salary bands from $127,000-$183,000 for Applied FDE roles up to $183,000-$265,000 for FDE IV roles, before bonus, equity, and benefits. These are not sales engineers — Google describes them as builders expected to “code, debug, and jointly ship bespoke agentic solutions directly within the customer’s environments. *The Information* reports that the broader target — hundreds of engineers — and [the *First Squawk* post](https://x.com/FirstSquawk/status/2054265532728438990) that surfaced the report hit 1.3 million views on X. Demand for the job is now its own news cycle.

Anthropic got in on the FDE fun too, shipping a deployment. FIS [announced an agentic anti-money-laundering platform](https://www.cio.com/article/4167981/anthropics-financial-agents-expose-forward-deployed-engineers-as-new-ai-limiting-factor.html) co-built with embedded Anthropic FDEs, with Bank of Montreal and Amalgamated Bank among the first institutions slated to deploy it. The press release language speaks to the signal: Anthropic engineers embed with FIS, co-design the Financial Crimes Agent, and “transfer knowledge so FIS can build and scale additional agents independently over time.” Simply, an FDE embeds, builds, and transfers.

Industry giants ServiceNow and Accenture got there first. The week prior, the two launched a joint FDE program embedding their engineers together inside customer environments to build agentic workflows on the ServiceNow AI Platform. Accenture’s own Pulse of Change research frames why: only 32% of enterprise leaders report sustained, enterprise-wide AI impact. The other 68% have pilots, decks, and a delivery gap. IBM’s Varun Bijlani [pointed to the same problem this week](https://www.ibm.com/think/insights/conversation-forward-deployed-engineers-incomplete), saying “speed of execution” is now the third-highest strategic priority among 2,000 senior executives.

> “Forward deployed engineers, or equivalent, are about to become one of the most in-demand jobs in tech. Deploying agents is far more technical a task than most people realize, often far more involved than deploying software.”

Box CEO Aaron Levie [summarized the moment](https://x.com/levie/status/2054398342852194386) on May 12: “Forward deployed engineers, or equivalent, are about to become one of the most in-demand jobs in tech. Deploying agents is far more technical a task than most people realize, often far more involved than deploying software.” Levie’s right. With agents, you’re not deploying software — you’re deploying a work output inside the enterprise, and the customer expects you to take them from current to end state in one motion. That’s a big job, even for an experienced (and high-paid) FDE.

## How to train for a forward deployed engineer role

[Jaya Gupta](https://www.linkedin.com/in/jayagupta10/) of Foundation Capital and formerly McKinsey, [reacting to Google’s announcement](https://x.com/JayaGup10/status/2054596613075763623), reframed the role better than anyone else has so far: “The FDE model is about TALENT, not just deployment. McKinsey made ‘client service’ prestigious for business generalists. Palantir made ’embedded deployment’ prestigious for technical generalists. The open question of the AI era is who makes AI implementation feel like cutting-edge work[?] The question right now that you see so many undergrads senior year asking is ‘which of these places is going to be sexy to do this forward deployed work at.'”

> “The open question of the AI era is who makes AI implementation feel like cutting-edge work[?]”

The FDE is to the AI era what McKinsey’s client-service generalist was to consulting and what Palantir’s embedded deployment role was to defense and intel – the high prestige early-career magnet for technical talent. The undergrads have figured it out. The question is which lab becomes the prestige employer for these folks.

If you’re already past undergrad, the path is just as solid. The day after his first tweet, Aaron Levie [wrote a follow-up](https://x.com/levie/status/205472996663044100) that reads like a syllabus. It’s worth quoting in full:

*“If I were a college career counselor or in career services, I’d quickly be figuring out how to get students to understand these forward deployed engineer jobs exist and how to get them. The requirements are a mix of deep technical skills, often CS majors or minors. You must be great at understanding problem solving, how to have systems thinking, and have a strong business acumen. The kicker, of course, is to make sure you’re very deep in AI agents; you need to have fluency in coding agents, MCP, CLIs, Skills, and so on. Hundreds (thousands?) of technology companies will be hiring for these roles, same with any consulting and IT services company, and the vast majority of mid-size and large enterprises will be hiring for this talent internally as well.”*

Levie is giving you the stack. CS foundations. Systems thinking. Business acumen. Deep AI agent fluency – coding agents (Claude Code, Cursor, Codex), the Model Context Protocol, agentic CLIs, and the Skills layer that sits on top. If you’re a developer, this is an additive curriculum on top of what you already know. If you’re adjacent to engineering — a PM, an analyst, an operator, an editor like me — this is the closest map to the highest-leverage role you can pivot towards.

**The most direct training path is already public.** Our team at IMG runs [Roadmap.sh](http://roadmap.sh), and the [AI Engineer roadmap](https://roadmap.sh/ai-engineer) is the closest one-page match to Levie’s stack — LLM fundamentals, RAG, agents, MCP, eval, prompt engineering, and deployment patterns. Pair it with Google’s own published FDE requirements as your readiness checklist: hands-on experience with RAG architectures, vector databases, foundation models fine-tuning, and production-grade AI deployment on cloud platforms.

That is the bar a Google or Anthropic recruiter will hold a candidate to right now. Work the roadmap as a curriculum, pair it with daily hands-on practice in Claude Code, Cursor, or Codex, and build something that ships. The thing that separates an AI engineer from a forward deployed engineer is customer context, and the only way to get customer context is to ship something to a customer — internal counts, too.

If you’re coming at this from the data side, the same shift to reshaping the job. On *Towards Data Science* last week, Sara A. Metwalli made the case in “[From Data Scientist to AI Architect](https://towardsdatascience.com/from-data-scientist-to-ai-architect/)” that the modern data scientist’s day-to-day has flipped: “Only 10 to 20 percent is spent using a model (API calls, inference), while 80 to 90 percent is spent on orchestration — handling data flow, integration, and infrastructure.” That is the same job description Google posted, written from the data perspective.

The non-technical half of the job matters at least as much. Riggin’s piece quotes Coleman on the underrated skill: “Being good at writing is a more important skill than ever now because, even though AI is able to throw out all sorts of stuff, it is still a garbage-in, garbage-out approach.” [Sundeep Teki](https://www.linkedin.com/in/sundeepteki/), an AI career coach Riggins interviews in the piece, describes the AI FDE workday as living in “ambiguity by default.” The model can do almost anything. The FDE figures out what it should do, from whom, on what timeline, and at what cost. FDEs must have judgment, communication skills, and domain expertise.

While forward deployed engineers are hot today, I question the role’s longevity. Eventually, enterprises will bring this role in-house as more engineers, PMs, and tech leaders become AI-fluent. Yet whether you’re aiming to be the embedded engineer or the internal counterpart, the skill stack is the same, and I’d urge you to start on the AI Engineering Roadmap today.

---

## Past Editions


[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/976a6c81-1706717710759.jpeg)

Matt Burns is Director of Editorial at Insight Media Group, where he oversees The New Stack, Roadmap.sh, and Towards Data Science — three platforms that collectively help millions of developers figure out what to learn next. Previously, he spent 16...

Read more from Matthew Burns](https://thenewstack.io/author/matthew-burns/)