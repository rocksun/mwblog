[Anthropic](https://www.anthropic.com/) today launched automated security reviews for [Claude Code](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/), its command line [AI coding assistant](https://thenewstack.io/what-are-ai-code-assistants-and-how-should-you-use-them/), addressing growing concerns about maintaining code security as AI dramatically accelerates software development.

The new capabilities include a terminal-based security scanning command and automated GitHub pull request reviews, representing what [Logan Graham](https://www.linkedin.com/in/logangraham/), head of Anthropic’s frontier red team, calls “the starting point of helping developers make their code really, really secure without basically even trying.”

## **Security Reviews at Terminal Speed**

The centerpiece of the update is a new `/security-review` command that developers can run directly from their terminal before committing code. The feature scans for common vulnerabilities, including SQL injection, [cross-site scripting (XSS)](https://thenewstack.io/xss-vulnerability-discovered-in-backstage-software-catalog/), authentication flaws, insecure data handling and dependency vulnerabilities, Anthropic said in a blog post.

“It’s literally like 10 keystrokes and you get basically a senior security engineer over your shoulder,” Graham told The New Stack. “It should be basically effortless for somebody to make code that they are writing, or code that they’re writing with Claude extremely secure, or it should just automatically happen for them,” he added.

After identifying issues, developers can ask Claude Code to automatically implement fixes, keeping security reviews within what Graham calls the “inner development loop,” where problems are easiest and cheapest to address.

## Automated Pull Request Security

The second major feature is a [GitHub Action](https://thenewstack.io/how-to-use-github-actions-and-apis-to-surface-important-data/) that automatically reviews every pull request for security vulnerabilities. Once configured by security teams, the system automatically triggers on new pull requests, reviews code changes for security vulnerabilities, applies customizable rules to filter false positives and posts comments inline on the pull requests with specific concerns and recommended fixes.

“This creates a consistent security review process across your entire team, ensuring no code reaches production without a baseline security review,” Anthropic said in the blog post. “The action integrates with your existing [CI/CD pipeline](https://thenewstack.io/how-to-build-scalable-and-reliable-ci-cd-pipelines-with-kubernetes/) and can be customized to match your team’s security policies.”

## Real-World Results

Anthropic has been testing these features internally. Graham said the company has caught several production vulnerabilities before they shipped, including a remote code execution vulnerability exploitable through DNS rebinding in a local HTTP server, and an SSRF attack vulnerability in an internal credential management system.

“Since setting up the GitHub Action, this has already caught security vulnerabilities in our own code and prevented them from being shipped and reaching our users,” the blog post states.

## The Scale Challenge

The security features address what Graham sees as an emerging crisis in software security. As AI tools become more prevalent, the volume of code being produced is exploding.

“Models are now writing extreme amount of code,” Graham said. “I think it’s really possible over the next, like, year or two years, you end up 10x-ing or 100x-ing or 1,000x-ing the amount of code that exists in the world. The only way to keep up with that is through models.”

This dramatic increase in code volume makes traditional human-led security reviews impractical at scale, Graham said. “Right now, it requires humans to review everything to make sure it’s secure, and if we really want models to be working on the highest value things in the world, we need to figure out a way to make all the code that comes out just as secure and ideally much more,” he told The New Stack.

## Democratizing Security

Beyond addressing scale, the features aim to democratize access to security expertise. Graham explained that the tools could benefit smaller development teams that lack dedicated security engineers or budgets for expensive security software.

“We’re [democratizing security review](https://thenewstack.io/coderabbits-ai-code-reviews-now-live-free-in-vs-code-cursor/) to, you know, the one-person shop that is building something exciting and doesn’t have a [security engineer](https://thenewstack.io/aptori-is-building-an-agentic-ai-security-engineer/), can’t pay for the license for the software,” he said. “They will probably get bigger, faster and more reliably if they start using these tools.”

## From Hackathon to Production

The security features originated as an internal hackathon project at Anthropic, where the security team was building tools to maintain what Graham describes as “frontier-class security” for the AI company. When the tool began finding issues in Anthropic’s own code before release, the team decided to make it available to all Claude Code users.

“This started as a [hackathon](https://thenewstack.io/hackathon-tips-to-boost-devops-innovation/) project. It already started finding like issues or flaws in our code before we were releasing it to ourselves,” Graham explained. “And we thought, this is super, super useful. This really aligned with the mission. Why don’t we just make it available to everybody in Claude Code?”

## Enterprise Focus

The security announcement continues Anthropic’s recent push to make Claude Code more enterprise-ready. In the past month alone, the company has shipped subagents, analytics dashboards for administrators, native Windows support, Hooks and multidirectory support, Graham said.

This pace of innovation indicates that Anthropic’s broader ambition is to position Claude Code as essential infrastructure for development teams, moving beyond simple code generation to comprehensive development workflow integration.

The company is able to deliver technology at this velocity because: “Anthropic is insanely talent dense, and the stuff that we pull off for the size that we are is, like, honestly, very, very amazing today,” Graham told The New Stack.

## Looking Ahead

Graham said the security features are just the beginning of a larger transformation in how software development and security intersect with AI.

“The broad belief that we have is models, over time, will basically do everything in a very agentic way,” he said, suggesting that AI agents will increasingly handle complex, multistep development tasks autonomously.

Both the `/security-review` command and GitHub Action are available immediately to all Claude Code users. The terminal command requires updating to the latest version of Claude Code, while the GitHub Action requires manual setup following Anthropic’s documentation.

For developers and organizations grappling with the security implications of AI-accelerated development, these tools represent an early attempt to ensure that the benefits of AI coding assistance don’t come at the cost of application security, Graham said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)