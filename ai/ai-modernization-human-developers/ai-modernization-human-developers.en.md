Modernization has traditionally been a choice between two hard options: keep patching a legacy system until it collapses under its own technical debt, or attempt a risky rewrite that trades known problems for unknown ones. Now, with AI tools readily available, the way teams approach application modernization is rapidly changing: code is scanned, summarized, and updated at a pace no human-only team can match.

For many organizations buried in technical debt, this can feel like getting thrown a life preserver, and they are eager to implement AI modernization tools into their workflows. We saw proof of this recently, with IBM’s stock sharply dropping after [Anthropic announced that its Claude Code AI tool can be used to modernize COBOL](https://www.reuters.com/business/ibm-posts-steepest-daily-drop-since-2000-after-anthropic-says-ai-can-modernize-2026-02-24/).

But speed is not the same thing as success, and while [AI tools can shorten modernization timelines](https://thenewstack.io/how-ai-can-speed-up-modernization-of-your-legacy-it-systems/), you still need domain expertise to ensure accuracy.

## Where AI shines in modernization work

Much of application modernization is made of repetitive, mechanical tasks, with legacy systems containing outdated patterns, deprecated functions, and copy-pasted code. This is where AI modernization tools outpace most alternatives: [scanning large codebases](https://thenewstack.io/open-source-coding-agents-like-opencode-cline-and-aider-are-solving-a-huge-headache-for-developers/), spotting common issues, and suggesting updates.

AI summarizes unfamiliar code, highlights risky dependencies, and drafts first-pass refactors, making modernization faster and more accessible. The offloading of these tasks is why agent-based modernization platforms (such as the [new MongoDB AMP](https://thenewstack.io/agent-infused-mongodb-tackles-application-modernization/)) have become so popular.

AI is also useful in helping your team get unstuck. As the Principal Product Manager at [Perforce Zend](http://www.zend.com/) and [Perforce OpenLogic](http://www.openlogic.com/), I have seen many modernization efforts stall at the starting line, all because the code feels too large or too complex to understand. AI lowers that barrier, helping teams explore the current state of their applications and plan highly effective [web application migrations](https://www.zend.com/resources/events/webinars/managing-php-application-migrations).

I cannot overstate the importance of this momentum. AI tools give your team a faster way into your code, answering basic questions quickly and reducing the fear that comes with working on older systems. Of course, that’s assuming that AI tools are paired with domain expertise, as using [AI without oversight](https://thenewstack.io/shadow-ai-the-growing-risk-it-leaders-must-address/) can lead to expensive consequences.

Despite their many benefits, AI modernization tools have a critical limitation: they cannot understand your entire system. The larger your application is, the truer that becomes. AI can update code, but it cannot fully know or anticipate how that code behaves in production. It doesn’t know why certain workarounds exist, how customers rely on edge cases, or which failures will create real business risk.

After all, legacy systems are rarely clean, and AI works from patterns and not lived experience. Business rules are often hidden in unexpected places, and a small code change can affect billing, compliance, and customer trust.

> “Legacy systems are rarely clean, and AI works from patterns and not lived experience.”

This is where expert-led oversight comes in.

Domain knowledge is critical for navigating legacy complexity, hidden dependencies, and more. Experienced developers, engineers, and architects know which parts of the system are fragile, which changes are safe, and where extra testing will be required — and that kind of judgement cannot be automated.

After all, the [domain and subject matter experts](https://thenewstack.io/future-ai-driven-devsecops/) in your organization understand why certain application behaviors exist and what problem they solve. These are the individuals who can identify the truly critical parts of your application and fully capture requirements. Without this expertise, AI agents and processes will struggle to succeed.

## Use AI as a partner, not a replacement

The best way forward is to treat AI as a member of your team and to design the context in which it operates precisely. Through context engineering, you give your AI tools the right boundaries, system knowledge, and goals so they can do what they do best: scan code, recognize patterns, suggest updates, and accelerate routine work. Then developers handle what AI can’t: setting direction, managing risk, and ensuring all changes align with your business needs.

> “The best way forward is to treat AI as a member of your team and to design the context in which it operates precisely.”

Approaching AI as a partnership changes the scope of your modernization project. Instead of a risky “big bang” rewrite, your team can move in safer, smaller steps. AI proposes changes, and experts decide which changes to accept, adjust, delay, or decline.

Take, for instance, the [Professional Services](http://www.zend.com/services) team at [Perforce Zend](http://www.zend.com/), where we use AI tools to help teams modernize critical PHP applications. In one case, we assisted a customer looking to [modernize from CodeIgniter to Symfony](https://www.zend.com/services/migration/codeigniter-migration). We applied AI tools to perform fact-checking, automate brainstorming, and significantly reduce time requirements. However, that speed was achieved without compromising stability. Our PHP engineers reviewed all outputs and results, ensuring that our customer could reach their goals sooner and with complete confidence — all thanks to expert-led AI modernization tactics.

Another example comes from MongoDB, which recently found that [using LLMs and AI tools can help fully modernize legacy applications](https://thenewstack.io/mongodb-finds-ai-can-help-with-legacy-system-migration/) and aid migration. By applying AI, organizations using or migrating to MongoDB can now automate much of the manual work that usually delays cloud and platform transitions. This dramatically reduces migration time and costs, with [Swiss bank Lombard Odier able to migrate code](https://www.mongodb.com/press/mongodb-collaborates-with-lombard-odier-to-modernize-core-banking-technology) 50 to 60 times faster.

The takeaway is clear: When AI is paired with human knowledge, modernization becomes predictable. Teams can repeat the process across systems, versions, and projects, turning modernization from a one-time event into an ongoing practice.

## How to get started with expert-led AI modernization

If you’re looking for ways to get started with effectively implementing an expert-led AI strategy, use this checklist for practical steps to move forward:

1. **Define the target state first** — Set clear goals, constraints, and “must not fail” areas before applying AI.
2. **Use AI for speed, not authority** — Let AI accelerate analysis and drafts while experts own final decisions.
3. **Anchor decisions in domain expertise** — Apply business, regulatory, and operational context to every change.
4. **Standardize what works** — Turn proven modernization into repeatable, low-risk playbooks.
5. **Prove changes before production** — Validate functionality, performance, security, and operational impact, with experts writing tests for critical sections and ensuring that AI-written code does not introduce new risk.
6. **Make modernization continuous** — Use AI to keep systems current, not just to fix crises.
7. **Evaluate in**–**house developer abilities honestly** — AI tools do not replace expertise, so partner with third-party support to fill knowledge or skills gaps.

Remember: AI tools bring speed to modernization, and domain expertise brings accuracy. The two together are a powerful combination and can fundamentally change how we approach legacy modernization efforts — delivering the best possible results without sacrificing stability or trust.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/03/f42cab1a-cropped-d0a7b10e-img_0342.jpeg)

Matthew Weier O’Phinney is Principal Product Manager at Perforce OpenLogic and Zend, focused on providing the tools and support developers need to build and deploy applications. An open-source contributor for more than 20 years, he led the Zend Framework from...

Read more from Matthew Weier O’Phinney](https://thenewstack.io/author/matthew-weier-ophinney/)