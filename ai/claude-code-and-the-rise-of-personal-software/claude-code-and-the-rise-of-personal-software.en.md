It’s not news to say [Claude Code](https://thenewstack.io/claude-code-desktop-redesign/) is actively changing how software is built. But what is news is who’s building it. [Software development](https://thenewstack.io/innovating-software-development-with-ai-and-ml-pros-and-cons/) is shifting from software developers to everyone else. Anthropic’s agentic coding tool, Claude Code, makes software development as simple as describing what you want. And its ease of use is no secret. After launching in May 2025, Claude Code hit [$1 billion in annualized revenue](https://aibusinessweekly.net/p/claude-ai-statistics) by November. By February 2026, that number more than [doubled to $2.5 billion](https://aibusinessweekly.net/p/claude-ai-statistics).

Claude Code is drastically changing how enterprise engineering teams operate. What’s even more interesting is how it democratizes software development and brings those same capabilities to teams that used to rely on SaaS and engineering teams. Now, people in areas like marketing, finance, and sales can build software. An entire ecosystem is emerging around the novel idea that anyone can create the software they need.

Claude Code isn’t an anomaly. Other non-technical app-building platforms are growing rapidly alongside it. [Lovable grew 2,800%](https://getmocha.com/blog/ai-app-builder-statistics) in a single year. [Replit grew 15x](https://getmocha.com/blog/ai-app-builder-statistics). The appetite for building software has expanded well beyond professional developers.

Welcome to the rise of personal software. But don’t be fooled by the term “personal software”. Personal software is any software developed to fit a need unique to a person, system, or team. This includes software that benefits the individual and the enterprise. A recent Retool survey found that 35% of companies have already replaced at least one SaaS tool with one they built themselves, and 78% expect to build more in 2026. Retool CEO David Hsu summed it up simply: The default question in boardrooms is shifting from “what should we buy?” to “can we just build this?”

## So what does personal software written with Claude Code look like?

It looks like what [Taylor Houck](https://www.linkedin.com/in/twhouck/), Head of Cloud and AI Efficiency at PointFive, tells *The New Stack* thathe built in less than a week using Claude Code. It was a solution to a problem he dealt with every day that no existing software solved, and wasn’t big enough to justify the cost of hiring a team of engineers to build something custom.

Houck’s team ran a content workflow that was dependent on humans. Someone would fill out a form. A team member would take those details, validate them, and draft content. That draft would get pasted into a shared Google Doc and emailed to the contributor for review. The contributor would respond with feedback. The team would rework it. Once approved, someone would manually upload it to a CMS. Straightforward and simple, but every step was a bottleneck and a possible point of failure. The workflow worked, but not at the same time.

The workflow would have stayed that way had Houck not automated the process using Claude Code. But he did, and now it’s fully automated. Once someone fills out the form, a webhook triggers an agentic system hosted on AWS Lambda, backed by a DynamoDB database. The system validates the submission, drafts the content, generates a review URL, and automatically emails it to the contributor. The contributor reviews it, suggests edits, or approves it directly. Every action automatically triggers the next step in the workflow. No one is waiting on anyone. Once it’s fully approved, a single click pushes it live on the website via a direct CMS integration.

The entire solution took less than a week to build and includes 130 files and 85,000 lines of code. 100% built by Claude Code.

This software is simple, even boring. But, at the same time, it never would have existed before now. Not because the idea was too complex. But because it was never economically viable to build something this customized, for just one team. Traditional software development requires months of engineering time, salaries, and infrastructure costs. The math didn’t work for a problem this niche. “It just never would’ve been economically viable before,” Houck says. “It would’ve taken a team of engineers a lot of time to build this. Now it costs less than $5 a month to run, and I built it within a $200 a month Claude subscription.”

Houck isn’t a developer. He describes himself as someone who “knows enough to be dangerous” with a background in [cloud infrastructure](https://thenewstack.io/ai-cloud-taxonomy-2026/) rather than software engineering. He didn’t have the know-how to write the code, but with Claude Code’s help, he directed the application. Before a single line was written, he spent hours with Claude in planning mode, defining requirements, workshopping the architecture, and stress-testing decisions. Claude even deployed the application. Of the experience, Houck says, “I gave Claude the AWS credentials, and it did all the deployment for me. I didn’t have to do any click ops. I didn’t have to do anything in AWS manually.”

Even after building so much already, Claude Code will bring more benefit to Houck and his team. The application relies on two third-party SaaS tools, Typeform for the form and Webflow for the website. He has already rebuilt both himself using Claude Code and is preparing to push them to production. He’s now rebuilding the SaaS stack around his personal software.

When speaking to others about getting started with Claude Code, Houck says, “There are use cases that I’ll never think of. Each of us has our own experience and skill set. Use your unique perspective and lean into these tools as a force multiplier.”

And the implications go beyond individual productivity. Houck sees Claude Code as a leveling up of the entire workforce. “Individual contributors who use these tools are now managers, and managers who have teams are now directors. Pretty much everyone has access to all these tools.”

## An emerging pattern in personal software

Houck isn’t alone. [Ondrej Machart](https://www.linkedin.com/in/ondrejmachart/), Head of Product at Livesport, used Claude Code to build 13 projects over six months. In his Medium article, [Lessons From 13 Claude Code Projects That Changed My Product Manager Role](https://medium.com/@ondrej.machart/13-claude-code-projects-that-changed-my-product-manager-role-over-the-last-6-months-7057b9045d51), he writes about building a native iOS app, a tool that helped his company’s C-suite make a major product consolidation decision, all using Claude Code, and a personal task tracker.

Machart’s app didn’t start with Claude Code. He had tried Replit, Lovable, and other vibe coding tools, but none offered what he needed. After a colleague’s suggestion, he began using Claude Code in the terminal. He spent two months learning the ropes over evenings and nights, motivated not by getting rich overnight but by building something people might actually use.

His first project, a native iOS app for parents to find nearby playgrounds, made it all the way to the App Store with a subscription model and third-party API integrations. “I didn’t become an engineer, and I don’t plan to become one,” he wrote. “I did become more T-shaped in terms of understanding other areas and domains. That’s valuable because it brings empathy.”

Like Houck, Machart isn’t a software engineer. Neither of these people set out to build the unicorn (yet). They both required software that wasn’t available, and so they used Claude Code to solve the problem. And Claude Code succeeded. The problems that didn’t make sense to solve before are now solvable. Claude Code didn’t just make software development faster. It made it personal.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)