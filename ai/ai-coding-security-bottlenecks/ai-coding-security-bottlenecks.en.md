Code assistants have fallen short of the “10x engineers” we expected. A recent GitLab survey of DevOps practitioners found that while more than [one-third of code is now written by AI](https://about.gitlab.com/resources/developer-survey/), practitioners ranked quality control and security vulnerabilities introduced by AI as the top adoption challenges. As organizations deploy AI coding tools at scale, these problems are overwhelming their security teams. AI promised to accelerate development, but we are creating security review bottlenecks faster than AI can improve coding efficiency.

Security engineers who previously reviewed 100 lines of code per hour can now face 100,000 lines of code because AI contributed to that code. Meanwhile, attackers are already using autonomous agents to rapidly detect flaws in existing systems. As risks proliferate and security backlogs grow, engineers’ capacity to defend remains constrained.

> “AI promised to accelerate development, but we are creating security review bottlenecks faster than AI can improve coding efficiency.”

This challenge has always existed in some form. Security processes dependent on human toil could be easily overlooked when code volumes were manageable. However, AI’s complexity is making product security work exponentially harder. If we don’t address these scaling challenges quickly, the window to secure AI-scale development will become trickier to close.

Here are the two compounding failures driving these bottlenecks — and how to avoid them.

## 1. Deploying AI tools without expanding security reviews

The “[shift left](https://thenewstack.io/shift-left-hangover-steve-corndell/)” movement aimed to address security bottlenecks by shifting security responsibility to developers earlier in the software development lifecycle. Adding security testing to development workflows sounds good in theory, but forcing developers to address security checks that often flag false positives is suboptimal. We can [unintentionally add hours](https://thenewstack.io/shift-left-hangover-steve-corndell/) to their workday without considering incentives. Developers will find workarounds because they need to ship features on a deadline.

With the shift left approach, teams failed to account for the entire software development lifecycle, leading to unintended downstream effects. We’re making the same mistake with AI code assistants. These assistants optimize for code generation while leaving the review process unchanged. The solution isn’t adding more people or more tools in isolation. Teams need to think holistically about the entire pipeline.

The organizations that avoid this trap map their value streams before adding more AI tools. This is in addition to documenting processes that rely on tacit, institutional knowledge, which complicates how teams define and measure the value AI delivers. When AI improves an undocumented process, teams cannot measure or prove that value.

> “The solution isn’t adding more people or more tools in isolation. Teams need to think holistically about the entire pipeline.”

Leaders should also implement scalable review methodologies that combine AI with practical human oversight, establishing prioritization frameworks based on measurable risk. For instance, code that touches sensitive customer data or production databases requires a much more intensive review than a feature to customize an application’s theme.

## 2. Traditional security frameworks won’t work for AI agents

Traditional security frameworks assume predictable human behavior. AI agents don’t follow those rules, and the result is an entirely new class of risk.

The complexity multiplies when agents interact with other agents across organizational boundaries. When an internal agent receives instructions from a third-party agent that itself received instructions from another external system, the security model must account for this complexity. As more agents are added to a chain, the higher the chance that malicious requests exist outside direct observation.

Avoiding these issues requires developing security controls to limit permissions and monitor agent behavior. Emerging approaches, such as establishing composite identities for AI systems, can help link AI activity to human accountability by tracking which [agents performed specific actions](https://thenewstack.io/how-to-add-tool-support-to-ai-agents-for-performing-actions/) and who authorized them.

Many security engineers today struggle to articulate how the backend of an LLM actually works, but understanding how an AI system is designed is fundamental to understanding AI security risks. This doesn’t require deep engineering expertise for every component, but rather a basic understanding of how the pieces fit together to achieve outcomes, much like security professionals understand how web applications work.

### What’s next

Most organizations will spend the next two years building AI capabilities on systems they know are flawed, because development cannot wait for every fix to arrive. It’s the right choice. No single solution will work for every organization to secure AI-driven development. The key is to acknowledge risk, manage it strategically, and work toward doing things the right way.

Security teams also can’t solve these failures alone. [Recent research from DX](https://getdx.com/report/ai-assisted-engineering-q4-impact-report/) shows that while 91% of developers now use AI tools and report saving 3-4 hours per week, organizational dysfunction, including meetings, interruptions, slow code reviews, and CI wait times, is costing teams more time than AI saves. Quality outcomes also vary among organizations, with some seeing improved change failure rates and faster delivery, while others are drowning in technical debt.

> “AI is an amplifier. If your delivery system is healthy, AI makes it better. If it’s broken, AI makes it worse.” – Bryan Finster, continuous delivery expert

The true differentiator isn’t the AI tools themselves, but the underlying engineering practices and culture. As continuous delivery expert [Bryan Finster observes](https://bdfinst.medium.com/5-minute-devops-ai-is-taking-our-jobs-pt-3-9aa721cdec46), “AI is an amplifier. If your delivery system is healthy, AI makes it better. If it’s broken, AI makes it worse.” The failures are rooted in upstream problems that AI now exposes at scale. Security reviews sit at the end of this chain, inheriting every weakness that came before.

Security teams must become advocates for the engineering practices that enable secure AI-driven development, including documented processes, a strong testing culture, and continuous delivery principles that embed security throughout software delivery. The quality of what reaches security teams in the first place remains the real constraint.

The organizations that will succeed are those that confront these problems now, before the volume of AI-generated code makes them impossible to fix.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/07/bb9e0e83-cropped-2a5de734-julie-davila--600x600.jpg)

Julie Davila is VP of Product Security at GitLab, where she enables critical infrastructure software factories to develop secure software faster. Her career has spanned from U.S. Army service to NASA, where she helped implement the first federal AWS migration....

Read more from Julie Davila](https://thenewstack.io/author/julie-davila/)