Anthropic has released an update to Claude Code and Claude Cowork that brings computer-use capabilities to macOS desktops, enabling autonomous task execution. With the new capability, announced Monday, you can now ask Claude to execute tasks in [Claude Code](http://anthropics-claude-code-comes-to-web-and-mobile/) or Claude Cowork using various apps or tools on your computer.

When executing a task, Claude opts for the most efficient method first, leaning on its [connectors](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) to services like Slack or Gmail. When no connector is available, Claude will take over your browser, mouse, keyboard, and screen to scroll, point, and click to open and navigate your desktop apps as needed to verify task completion. It’s worth noting that these screen interactions still get the job done but are slower than direct integrations.

Working with the apps, files, and tools on your computer, Claude with computer use can perform tasks like automatically checking your morning emails, compiling disparate metrics into a formatted spreadsheet, and opening a pull request, to name a few.

This comes shortly after last week’s [Dispatch launch](http://claude-dispatch-versus-openclaw/), a new feature in Claude Cowork that lets you converse with Claude across your phone and desktop. Paired with Dispatch, Claude’s new computer use capability means you can assign Claude tasks directly from your phone, step away from screens altogether, and then open up your desktop to check out the finished work later on.

There’s no setup required, but you’ll need to make sure your computer is awake and running, and the Claude Desktop app is open.

## What about security?

In its [announcement](https://claude.com/blog/dispatch-and-computer-use), Anthropic outlines what guardrails are in place to keep Claude in line.

For starters, the assistant asks for your permission before accessing each new app. Some are blocklisted by default (a list you can add to), and you reserve the right to turn off Claude at any time.

Meanwhile, safeguards are in place to minimize risks, such as prompt injection. As explained in Anthropic’s announcement: “When Claude uses your computer, our system will automatically scan activations within the model to detect for such activity.”

Plus, Claude itself was trained to avoid risky actions, such as transferring funds, entering sensitive data, modifying or deleting files, or capturing facial images. And all sensitive data (e.g., passwords, health information, etc.) is automatically excluded from [Claude’s memory](http://claudes-free-plan-can-now-remember-you/).

Still, the company concedes that risks remain — and users should take steps to protect sensitive data from Claude’s autonomous hand.

When the capability is in use, Claude takes screenshots of your computer, capturing any information visible on your screen, be it sensitive or not. Before launching this computer-use feature, Anthropic’s support documentation recommends closing any files or apps that contain confidential information, such as legal or financial documents.

It also behooves users to deny permissions to sensitive apps (e.g., banking, medical), tailor prompts carefully to avoid unintended actions, and prioritize simple tasks (such as research and organization) over complex, multi-step workflows.

“Computer use is still early compared to Claude’s ability to code or interact with text,” reminds Anthropic in its announcement, acknowledging that the capability “won’t always work perfectly” and will sometimes “need a second try.”

So why now?

Claude’s computer use capability in Claude and Cowork is in research preview, available now for Claude Pro and Claude Max subscribers (not Team or Enterprise plans), for macOS only.

Anthropic backs up the release by explaining in its announcement, “We’re sharing it early because we want to learn where it works and where it falls short.”

When asked how it will continue to improve security in step with evolving threats, Anthropic tells *The New Stack* that it aims to leverage real-world usage and feedback to further hone its security safeguards. That’s why the capability is being rolled out gradually with plans to harden it as the company learns more about how the feature is used.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)