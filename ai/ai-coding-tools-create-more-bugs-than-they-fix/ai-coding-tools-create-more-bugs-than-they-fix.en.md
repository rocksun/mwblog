[Mobb](https://www.mobb.ai/), a provider of automatic security vulnerability remediation technology, has launched new tools to secure [AI-generated code](https://thenewstack.io/ai-generated-code-needs-refactoring-say-76-of-developers/) without slowing down development.

[AI-powered coding tools](https://thenewstack.io/ai-powered-coding-developer-tool-trends-to-monitor-in-2025/) and the so-called “[vibe coding](https://thenewstack.io/vibe-coding-and-you/)” craze have [enabled developers to build more code more swiftly than ever before](https://thenewstack.io/ai-coding-human-engineers-are-more-important-than-ever/), but lurking underneath all that productivity lie [unrecognized security risks](https://thenewstack.io/after-vibe-coding-comes-vibe-testing-almost/).

Platforms like [Lovable](https://lovable.dev/), [Bolt](https://bolt.new/) and [Cursor](https://thenewstack.io/5-ways-cursor-ai-sets-the-standard-for-ai-coding-assistance/) are enabling anyone to build functional applications in minutes, while professional developers are leveraging AI assistants to code faster.

However, recent research reveals that more than 40% of AI-generated applications are inadvertently exposing sensitive user data to the public internet. Even more alarming is that AI coding assistants are consistently introducing vulnerabilities into professional codebases, [Tomer Cohen](https://www.linkedin.com/in/tomer-van-cohen/), vice president of product at Mobb, told The New Stack.

## A Two-Pronged Solution

The Boston-based startup is taking a dual approach to tackle both sides of the AI coding spectrum: casual builders using no-code platforms and professional developers using AI assistants to augment their efforts.

Thus, Mobb this week is launching two complementary solutions to address [AI coding security risks](https://thenewstack.io/ai-security-agents-combat-ai-generated-code-risks/): [SafeVibe.Codes](https://safevibe.codes/) and [Mobb Vibe Shield](https://vibe.mobb.ai/).

**SafeVibe.Codes** targets the no-code security crisis with a free web-based scanner at SafeVibe.Codes. Users simply paste their application URL to receive an instant security analysis showing exposed databases, leaked personal information and misconfigured permissions. The tool provides actionable guidance for fixing identified issues without requiring technical expertise.

“Security shouldn’t be a luxury available only to those with extensive technical knowledge or large budgets,” Cohen explained in a blog post. “By making SafeVibe.Codes completely free and accessible, we’re democratizing security testing just as AI platforms have democratized app development.”

“SafeVibe.Codes is an application we launched as a free service for the industry to quickly identify certain types of vulnerabilities in apps they built with some of the leading vibe coding platforms,” [Eitan Worcel](https://www.linkedin.com/in/worcel/), co-founder and CEO of Mobb, told The New Stack. “We are great supporters of vibe coding and see immense potential in it. In fact, the [SafeVibe.Codes] site itself was built with Bolt, which is one of those platforms.”

The platform scans for:

* Database exposure and unauthorized access
* Sensitive data leakage
* Permission misconfigurations
* Hidden pages (e.g., /admin)
* Common API security vulnerabilities (coming soon)
* Data validation issues (coming soon)

Future testing coverage will include:

* **Real-time monitoring:** Continuous security monitoring to alert you when new vulnerabilities are introduced.
* **Page exposure scanning:** Detection of unintentionally public pages and sensitive information exposed in HTML, JavaScript or API endpoints.
* **AI prompt exposure detection:** Many apps’ core intellectual property lies in their AI prompts and system instructions. Nevertheless, it is common that vibe-coding platforms expose those prompts to everyone. SafeVibe.Codes identifies when these valuable prompts are inadvertently exposed in client-side code or API responses, allowing competitors to copy your app’s unique AI behaviors.
* **Full code security analysis:** Comprehensive source code scanning to identify vulnerabilities like injection flaws, insecure dependencies and logic errors.
* **Compliance checking:** Automated verification against security standards and data protection regulations.
* **Security education hub:** Interactive tutorials and best practices specifically tailored for AI-generated applications,

## Addressing the Enterprise

Meanwhile, **Mobb Vibe Shield** addresses the professional developer side through IDE integration – it works with VS Code, GitHub Copilot, Cursor, Windsurf, JetBrains IDEs and Cline (with others to come). The tool continuously scans code as it is written, automatically detecting vulnerabilities introduced by AI assistants and applying verified security fixes in real time. Using the [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/), it integrates easily with existing AI coding workflows.

The system does not rely on AI to fix security issues it detects. Instead, it applies pre-verified security patches developed by Mobb’s security experts, ensuring that fixes resolve vulnerabilities rather than creating new ones, Cohen said.

Worcel noted that companies are already adopting vibe-coding tools at an unprecedented pace as they look to benefit from all the productivity boosts.

“We see it happening in companies of all sizes and across all industries. Neither the developers nor the security teams are equipped to handle the huge amount of new code and code vulnerabilities generated, and existing code scanning tools being slow and noisy weren’t designed to handle it either,” he told The New Stack. “Mobb Vibe Shield was built from the ground up as a solution for companies that are looking to safely adopt vibe coding. It works alongside the developer within their AI tool of choice, inspects the AI-generated code and immediately applies fixes for detected vulnerabilities before they ever become a problem.”

## The Hidden Crisis in No-Code Platforms

Mobb’s research team conducted an extensive security analysis across five major AI development platforms: Lovable, Bolt, [Base44](https://base44.com/), [Replit](https://replit.com/) and [v0](https://v0.dev/), Cohen said. The results paint a troubling picture of the current state of AI app security.

“More than 40% of applications we tested across all platforms contained some level of sensitive data exposure,” he said. “This means that nearly half of all AI-generated apps we examined were unintentionally sharing private information with the public internet.”

The types of exposed data include personal information like names, emails and phone numbers, as well as financial records, private communications and authentication credentials. In addition, in roughly 20% of cases, anonymous users could not only view this data but also modify or delete it entirely.

## It Gets Even Worse

During an interview, Cohen demonstrated the process of using Base44 to build a gym booking system. The AI created a functional application complete with class schedules and member registration. But by default, it also created publicly accessible databases containing every member’s personal information – with no warnings about the security implications.

“At no point does the platform warn you about these security implications,” Cohen wrote in the blog. “There’s no indication that sensitive personal information is being collected and stored in a publicly accessible database.”

Yet, perhaps even more troubling is what happens when users try to fix these issues. When developers attempt to enable proper security controls, the applications often break. When they ask the AI to fix the broken functionality, the platforms frequently respond by removing the security measures entirely – without explaining the trade-offs being made.

“Here’s where the problem gets even worse,” Cohen said in the blog post. “When attempting to fix the security issue by enabling Row Level Security (RLS) settings to restrict database access, in many cases the application immediately breaks. The AI-generated code is not designed to work with proper security controls.

“When asking the AI agent to fix the broken functionality, the platform’s response is alarming: in many cases it simply removed my RLS restrictions and reopened the data to the world – without any warning that this was dangerous or explaining the security implications. The AI prioritized making the app ‘work’ over keeping the data secure, effectively undoing my security improvements.”

## Introducing Vulnerabilities

Moreover, in testing, Mobb researchers found that asking AI assistants to implement common development tasks – like creating an endpoint for code commits – resulted in command injection vulnerabilities with a 100% reproduction rate, Cohen said. These flaws could allow attackers to execute arbitrary commands on production servers.

Additionally, the AI tools often claim to have implemented security measures. “It actually tells me that it did something to prevent command injection,” Cohen said. “So, developers, even experienced, responsible developers, could be tricked by this, because it looks very convincing.”

This creates a false sense of security where developers believe their AI assistant has properly secured their code, when in reality, it has introduced vulnerabilities while appearing to address security concerns.

“This isn’t meant to discourage the use of AI development tools – they’re powerful and democratizing technologies,” Cohen wrote. “Instead, it’s a call to action for both platform providers and developers to prioritize security alongside functionality.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)