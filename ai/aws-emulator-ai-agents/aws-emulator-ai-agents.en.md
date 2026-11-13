![AWS logo](https://cdn.thenewstack.io/media/2026/11/ad6fe451-img_5814-1024x768.jpg)

AWS on Wednesday launched an emulator for AWS called AWS Emulator.

That, by itself, is interesting and may raise some questions about the [future of LocalStack](https://www.localstack.cloud). But what’s maybe most interesting is that the emulator was entirely built by a team of agents and will also be maintained by them going forward.

Since AWS wasn’t sure it could actually copyright the work of these agents — and didn’t want to assert copyright where none may exist — the emulator is available under the [Creative Commons Zero license](https://creativecommons.org/publicdomain/zero/1.0/deed.en), which puts the code into the public domain.

Tom ‘Spot’ Callaway, a principal open source software strategist at AWS, told The New Stack that there have obviously been other emulators in the past — and AWS itself has built some, too.

“The challenge is that they get out of date very quickly,” he explains. “They don’t always reflect reality on the ground, and because of that, they’re often not trusted. And we didn’t even trust them internally.”

With the rise of [agentic coding tools](https://thenewstack.io/claude-code-vs-cursor-vs-codex-vs-antigravity-2026/), the team also saw a need for a better emulator that could help agents [test code against AWS services](https://thenewstack.io/runtime-verification-coding-agents/) without having to hand over AWS credentials to the agents.

![](https://cdn.thenewstack.io/media/2026/11/e05101e5-screenshot-2026-11-11-084900-1024x556.png)

The agent system building AWS Emulator. Credit: AWS.

Meanwhile, the team was also looking at a test case for building a full project with agents, and the emulator proved to be a good testing ground, in large part because it provided a bounded problem with clear goals and the ability to test the results.

Since AWS already publishes a full set of API models as Smithy models and generates all its SDKs from those files, “there’s no reason that we can’t also generate mock emulation around that same logic,” Callaway says.

### A weekend Kiro experiment

The project goes back to an experiment by Matt Goldberg, a senior principal engineer on the AWS Developer Tools team. Callaway says the team was “heavily inspired by the Anthropic work where they instantiated a compiler,” referring to the C compiler that Anthropic researchers had [a team of agents](https://thenewstack.io/anthropics-opus-4-6-is-a-step-change-for-the-enterprise/) build earlier this year.

Goldberg writes in a [blog post](https://aboutamazon.com/news/aws/how-autonomous-ai-agents-built-aws-emulator) that he first asked [Kiro](https://thenewstack.io/kiro-is-awss-specs-centric-answer-to-windsurf-and-cursor/), AWS’s agentic coding tool, to build an emulator for Amazon Simple Queue Service (SQS). It came back with a first version 15 minutes later. He then had Kiro build out the rest of AWS over a weekend. That version unsurprisingly had gaps, he notes, but his team started testing its own software against it the following Monday.

“I got to admit, the first time I heard about this, I was like, ‘Are we sure this is a good idea?’” Callaway says.

The more the team iterated on it, he adds, the more comfortable he became that this was a good problem for agents to take on.

In its current version, AWS Emulator supports 438 public AWS API models covering more than 200 services. As AWS updates them and releases new services, the agents will quickly update the emulator, too.

Callaway expects the gap between a new AWS service launching and the emulator supporting it to be “days, not weeks, not months,” though he notes the team hasn’t yet seen how that plays out with the project in public.

The emulator itself is written in Rust and runs locally on Linux, macOS, and Windows, without a network connection or an AWS account.

“There’s no AI inside of AWS Emulator,” Callaway says. “It does not do an LLM callout at all.”

### Three teams of agents

AWS says it divides the work among three teams of agents. The first develops test scenarios from the public Smithy models and runs them against real AWS services to establish how the emulator should behave.

These scenarios can involve several services working together, rather than just individual API calls. As Callaway explains, “if the docs don’t tell the truth, then the cloud becomes the source of truth.”

The second team runs those scenarios against the emulator and investigates where its behavior differs from AWS. It groups failures that appear to have a common cause and files issues in the code repository.

Finally, the third team picks up those issues and changes the code to address them. Before those changes can merge, they have to pass build and test checks, as well as reviews by other agents for security problems, coding standards, and regressions in the emulator’s behavior.

The human engineers, meanwhile, focus on improving the system that directs the agents.

“We don’t edit it. We don’t modify it,” Callaway says of the emulator’s code. “If we find that the code has issues, we try and trace those issues back to the agent and fix the agent so that it doesn’t make bad code.”

So when there is a problem in the code those agents generated, the team will change how the agents work, rather than patch the code by hand.

Goldberg writes that an earlier version of the agents at one point decided to write their own Python interpreter so the emulator could support Lambda functions. The team has since instructed them to reuse existing libraries.

“I think we’ve learned a lot about sandboxing,” Callaway says, “haven’t we all in the last few months?”

The first iterations of the system “did not have as aggressive a [sandbox](https://thenewstack.io/cloud-agent-code-sandboxes/) as they needed to,” he says, and there was some early concern about the agents looking at the source code of AWS’s internal services to figure out how to implement something like Aurora. The team also spent a lot of time reassuring Amazon executives that the framework building the emulator wasn’t going to “go rogue.”

### No pull requests accepted

That hands-off approach goes for outside contributors, too.

“We’re not going to take pull requests on the project at all,” Callaway says. “The agents will be doing that. We will take issues from customers.”

He describes the agents as “their own little pull request army.” If they keep getting a particular API wrong, “that’s a bug in the agent,” he says, and he expects customers to mostly contribute scenarios the emulator doesn’t handle well yet.

AWS is also publishing the benchmark it uses to test the emulator “so that you can not trust us,” Callaway says. “You can run that benchmark.” Others could also use it to benchmark their own work, he notes.

### What the emulator can’t do

Users shouldn’t expect the emulator to do the things the actual services do, though.

“I run this SQL query, and I don’t get the right results,” Callaway says. “Well, guess what? There’s no database.” The emulator, he says, “really was built for the purposes of testing coverage.”

AWS says it will share more about the project at its re:Invent conference, which starts Nov. 30. The New Stack will be there — and [we’re even throwing a party](https://thenewstack.io/event/aws-reinvent-reception-with-sourcegraph-and-opslevel/).

The post [AWS had its agents build a free and open emulator for AWS. They now maintain it, too.](https://thenewstack.io/aws-emulator-ai-agents/) appeared first on [The New Stack](https://thenewstack.io).