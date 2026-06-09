Microsoft used its [Build 2026](https://news.microsoft.com/build-2026/) conference last week to announce a series of updates to its flagship [Visual Studio IDE](https://thenewstack.io/developers-test-visual-studio-2026s-ai-native-claims/) centered on a theme the company is calling agents that participate in development rather than sit next to it — along with a long-awaited move to let developers bring their own AI models and keys to the IDE.

The announcements span debugging, profiling, testing, merge conflict resolution, .NET modernization, and a new model flexibility option that Microsoft says will open the door to teams whose environments have made the current AI integration a non-starter.

“Historically, AI integration in Visual Studio has been limited to a small set of sanctioned endpoints,” writes [Mads Kristensen](https://www.linkedin.com/in/madskvistkristensen/), principal product manager for Visual Studio, in a [blog post](https://devblogs.microsoft.com/visualstudio/whats-coming-next-in-visual-studio-our-microsoft-build-2026-announcements/) accompanying the announcements. “That works for a lot of developers, but it has left real customers behind, including teams whose environments call for different choices.”

## BYOK: The enterprise unlock

The bring-your-own-key (BYOK) announcement may be the most significant for enterprise shops. Microsoft is moving toward a model that lets developers use different AI models — whether running locally or in the cloud — rather than being locked to the handful of endpoints Visual Studio has historically supported.

> Microsoft is willing to compete on flexibility rather than assuming developers will simply work within whatever AI stack Redmond has blessed.

That matters for teams with compliance requirements, cost constraints, or data sovereignty concerns that have prevented them from using Visual Studio’s AI features in their current form. The move also signals that Microsoft is willing to compete on flexibility rather than assuming developers will simply work within whatever AI stack Redmond has blessed.

Beyond BYOK, Microsoft’s bigger architectural push is embedding agents directly into the IDE’s existing toolchain — the debugger, profiler, and test runner — rather than treating AI as a parallel chat interface.

“This is not about replacing the tools you already rely on,” Kristensen writes. “It is about connecting them more effectively.”

The practical pitch is aimed at enterprise [C#](https://thenewstack.io/c-compiler-lead-jared-parsons-on-20-years-at-microsoft/) and [C++](https://thenewstack.io/introduction-to-c-programming-language/) developers working in large codebases where, as Kristensen puts it, the hard problems are not “write this function” but “figure out why this thing is slow under load.” The agents are meant to help identify issues faster, explain what is happening, suggest fixes, and help validate results — all within the context of the existing debugger and profiler rather than requiring developers to context-switch to a chat window.

A dedicated Build session — “[GitHub Copilot in Visual Studio: Agents That Debug, Profile, and Test” (BRK207)](https://build.microsoft.com/en-US/sessions/BRK207), featuring Kristensen and [Nik Karpinsky](https://www.linkedin.com/in/karpinsn/), Principal Software Engineer Lead at Microsoft, provides additional information on this topic.

## Modernization gets more ambitious

Microsoft is also expanding what it calls [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) modernization, the agent experience built into Visual Studio for upgrading applications to the latest .NET stack.

New this summer: the ability to migrate [Web Forms](https://learn.microsoft.com/en-us/aspnet/web-forms/what-is-web-forms) applications to [Blazor](https://thenewstack.io/no-more-javascript-how-microsoft-blazor-uses-webassembly/) and add[Aspire](https://thenewstack.io/microsofts-net-aspire-the-spring-boot-of-net-development/) to existing apps for cloud-ready [observability](https://thenewstack.io/introduction-to-observability/) and orchestration. The modernization agent is designed to assess a project, build a migration plan, and execute upgrades step by step.

The pitch is aimed at teams that have been sitting on aging Web Forms codebases because the economics of a full rewrite never made sense. Whether the agent-assisted approach actually changes that calculus remains to be seen, but it is a more concrete use case than general-purpose code generation.

## Smaller changes worth noting

Microsoft is also shipping a quality-of-life fix that addresses a scenario most Visual Studio developers have encountered: builds that run even when the Error List already shows obvious problems, only to fail on something that was visible up front. Going forward, Visual Studio will check errors and warnings before the build starts, Kristensen writes.

> Going forward, Visual Studio will check errors and warnings before the build starts, Kristensen writes.

On the collaboration side, Microsoft is working on AI-assisted merge conflict resolution — not auto-merging, but helping to understand the conflict and make a decision. Also coming: Microsoft-authored skills that apply automatically based on project type and context, reducing the need for developers to know what to prompt for.

## Under the hood

Underneath it all, Visual Studio is moving to the GitHub Copilot SDK as the foundation for its AI integration. The change will not be visible in any menu, but Microsoft says it will allow the company to move faster and stay aligned with the broader Copilot ecosystem.

The full set of announcements is available at the [Visual Studio blog](https://devblogs.microsoft.com/visualstudio/). Also, the Build sessions are streaming online for free at [build.microsoft.com](https://build.microsoft.com/en-US/home).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)