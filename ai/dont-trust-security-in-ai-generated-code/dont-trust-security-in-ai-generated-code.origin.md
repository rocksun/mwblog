# Don’t Trust Security in AI-Generated Code
Speaking from more than 20 years of experience in development and cybersecurity, developers need to use all the cutting-edge, time-saving, and productivity-boosting tools. It’s meticulous, time-consuming work to ensure you commit to high-quality, functional code, and the software development life cycle always demands more.

As such, nowadays, almost all developers use some form of AI-generated code — and they absolutely should. AI tools make developers’ lives easier by leveraging the knowledge cultivated by the development community over time and across the globe to overcome obstacles that, while potentially new and challenging to them, have long been addressed. They can reasonably trust that code to perform the function they want to achieve — and can test it to be sure.

But can they [trust that code to be secure](https://thenewstack.io/zero-trust-security-for-distributed-applications-with-dapr-open-source/)? Absolutely not. With all that time and work spent committing functional code, just as much, if not more, is spent navigating the security backlog afterward.

**What’s Wrong With AI-Generated Code?**
GenAI platforms, such as Copilot, learns from code posted to sites like GitHub and has the potential to pick up some bad habits along the way. It searches for and returns code that, first and foremost, actually works, but security is a secondary objective (if at all). As you’ll see further down in this article, this leads to substantial potential for vulnerabilities.

A pair of studies recently explored the effect of AI on code security. The first was a Stanford University study, “[Do Users Write More Insecure Code with AI Assistants?](https://arxiv.org/pdf/2211.03622)” and the other was a Wuhan University study, “[Exploring Security Weaknesses of Copilot Generated Code in Github](https://arxiv.org/pdf/2310.02059v2).”

The Stanford study found the following.

- Participants who had access to an AI assistant wrote significantly less secure code than those without access to an assistant.
- Participants with access to an AI assistant were also more likely to believe they wrote secure code, suggesting that such tools may lead users to be overconfident about security flaws in their code.
- Participants who invested more in creating their queries for the AI assistant, such as providing helper functions or adjusting the parameters, were more likely to eventually offer secure solutions.
The Wuhan study found that almost 30% of Copilot-generated code snippets have security weaknesses. Focusing specifically on Python, 91 of 277 snippets, or 33%, contained security weaknesses; of those 91 snippets, there were 277 instances of security weakness. In other words, the insecure code was VERY insecure.

**How Do I Secure My Code?**
At this point, it should go without saying that when it comes to using GenAI like Copilot to help with your code, you should never assume that what you’re getting is perfectly secure. You should approach AI-generated code like you approach code written by humans with a keen, skeptical eye and through standard security protocols. However, with the volume and prevalence of potentially vulnerable AI [code making its way into software development](https://thenewstack.io/augment-ai-code-assistant-targets-large-development-teams/) lifecycles, traditional reactive approaches may not be enough.

Organizations should create and maintain a culture of [security that integrates](https://thenewstack.io/llm-integration-pitfalls-protecting-sensitive-data-in-the-ai-age/) security at every stage of the SDLC and seeks to identify vulnerabilities as proactively as possible. Ideally, vulnerabilities should be identified as [developers write the code](https://thenewstack.io/idps-give-developers-more-freedom-to-write-code/), ensuring they commit quality, secure code, eliminating backlogs for security operations teams, and making the entire lifecycle more efficient. Addressing vulnerabilities within the IDE during coding is the natural end-point of shift-left and secure-by-design philosophies and the most effective and efficient way to integrate security into the software development lifecycle.

**Conclusion**
Whether code is manually written or AI-generated, detecting and fixing vulnerabilities as code is written saves time and preserves focus. This also reduces the back-and-forth in peer reviews, making the entire process smoother and more efficient. By embedding security more deeply into the development workflow, we can address security issues without disrupting productivity.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)