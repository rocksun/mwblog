Although [AI coding assistants](https://thenewstack.io/what-are-ai-code-assistants-and-how-should-you-use-them/) can churn out thousands of lines of code in minutes, writing code is the easy part. The real pain comes afterward — testing it, securing it, deploying it and keeping it running.

To address this, [Harness](https://harness.io/products/continuous-integration?utm_content=inline+mention) has launched Harness AI, a platform that automates everything that happens after you hit “commit.” And based on early customer results, they may be onto something.

## Where Things Actually Break

Most developers spend only a fraction of their time actually writing code. The rest gets eaten up by what Harness CEO [Jyoti Bansal](https://www.linkedin.com/in/jyotibansal/) calls “toil” — managing [CI/CD pipelines](https://thenewstack.io/introduction-to-ci-cd/), babysitting [test suites](https://thenewstack.io/a-better-developer-experience-requires-better-testing-tools/), chasing down [security vulnerabilities](https://thenewstack.io/top-9-api-security-vulnerabilities-how-to-defend-against-them/) and figuring out why the [cloud bill keeps increasing](https://thenewstack.io/your-engineering-organization-is-too-expensive/).

“You could spend 35 to 45 hours a week just managing and maintaining a CI/CD pipeline,” Bansal told me during a recent interview. “Your build failed? That’s another hour. Cloud costs spiking? There goes your afternoon.”

The numbers back this up. Harness found that nearly 80% of software failures happen after coding, with CI/CD pipelines being the biggest culprit. According to the [2024 DORA report](https://dora.dev/research/2024/dora-report/), despite the glut of fancy AI tools, software delivery is actually getting less stable and slower.

Now throw [AI-generated code](https://thenewstack.io/ai-generated-code-needs-refactoring-say-76-of-developers/) into the mix, and the problem gets worse. A developer can generate 20,000 lines of code in 20 minutes, but nobody’s reading through all that before shipping it.

“The downstream systems better be strong enough to catch the problems, because they’re coming,” Bansal told The New Stack.

In a blog post, Bansal said Harness AI is “the foundation for the next generation of software delivery — a generation that delivers software not just for today’s applications but also for AI-powered applications with the same speed, reliability and security.”

## Beyond Point Solutions

Most companies trying to solve this problem throw more tools at it — an [AI assistant](https://thenewstack.io/ai-coding-assistants-12-dos-and-donts/) for testing here, a [security scanner](https://thenewstack.io/how-to-implement-a-security-scanner-for-docker-images/) there, maybe some cloud cost monitoring over there. That can lead to tool sprawl without any real intelligence connecting the dots.

Bansal said Harness has taken a different, unique approach. Instead of building another point solution, it created what it calls a “Software Delivery Knowledge Graph” — essentially a brain that understands your entire development process, from code repos to production infrastructure.

[![](https://cdn.thenewstack.io/media/2025/08/53bd7f9c-unnamed-1-1.png)](https://cdn.thenewstack.io/media/2025/08/53bd7f9c-unnamed-1-1.png)

The platform looks simple enough on the surface — just a chat interface where you can ask it to “set up a pipeline for our mobile app” or “why did our deployment fail last night?” But underneath, specialized [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) are handling the heavy lifting, each focused on different aspects like [security, testing or cost optimization](https://thenewstack.io/ai-is-testing-ai-generated-code-should-you-trust-it), Bansal said.

“The Harness AI seamlessly connects a suite of intelligent agents, such as [DevOps](https://thenewstack.io/introduction-to-devops/), [SRE](https://thenewstack.io/ai-reliability-engineering-welcome-to-the-third-age-of-sre/), Release, AppSec and Test Agents,” Bansal wrote in the post. “You don’t see the agents, but you feel their impact in every workflow: faster, safer, and smarter delivery.”

What makes it interesting is the context. The system knows your company’s security policies, understands your infrastructure setup, and remembers what happened the last time you tried to deploy on a Friday afternoon. It’s not generating generic pipelines — it’s building stuff that actually fits your organization.

## Real World Results

Early numbers indicate that enterprise customers are seeing test cycle times drop by 80%, downtime cut in half, and test maintenance effort reduced by 70%. Bansal said one customer told him that it cut pipeline debugging time in half just by having an AI that actually understood its setup.

“The feedback has been tremendous,” Bansal said, recalling recent user events in Columbus, Ohio and Chicago. “People are saying nothing like this exists. Everyone’s struggling with DevOps and security and all these things that eat up 70% of engineering time, and there’s no good AI solution for it.”

## The Bigger Picture

Harness has been building automation tools for seven years, but the AI layer is relatively new — about 30 months in development, Bansal said. They are working with the usual suspects — Anthropic, OpenAI, Google — but also integrating with developer tools like Cursor and [Windsurf](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/) to meet developers where they actually work, he added.

As AI makes it easier to generate code, the bottleneck shifts to everything else. Companies that figure out how to automate software delivery might have a real competitive advantage, Bansal said.

Moreover, Bansal said that in a world where everybody is focused on making coding faster, somebody needs to make sure the rest of the pipeline can keep up.

Harness AI is available now for existing Harness customers, with a broader showcase planned for the company’s [Unscripted conference](https://www.unscriptedconf.io/) in September.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)