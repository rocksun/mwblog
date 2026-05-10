Late last month, [OpenAI shipped a new product](https://thenewstack.io/openai-workspace-agents-gpt-5-5/) they dubbed “Codex for (almost) everything.” Its goal was to shift [Codex](https://thenewstack.io/openais-codex-is-now-on-windows/) from a code editing product to a general-purpose tool.

The “Codex for (almost) everything” launch included features such as computer use, an in-app browser, PR review, SSH connections to remote dev boxes, and over 90 new plugins. More than 3 million developers use Codex every week, and many of them probably opened the app the next morning and didn’t notice anything different.

I noticed. And now I have opinions.

## The setup

I spent a day testing three of the biggest new features against the same real-world codebase I used to test [Cursor 3 and Claude Code in this article](https://thenewstack.io/cursors-agents-window-vs-claude-code/) (but tested a different bug). The test codebase is HTTPie, a popular open source [Python](https://thenewstack.io/python/) [CLI](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/) tool for making HTTP requests.

I ran my tests on the [Codex desktop app.](https://openai.com/codex/) I was able to access all its new features with my OpenAI account. I use the free version. Computer use requires a Mac and specific system permissions (more on that later).

## Codex in-app browser

This is the feature I was most excited to test because it changes the prompt workflow entirely. Instead of copying and pasting a bug description into the chat, I opened the GitHub issue directly inside Codex and pointed the agent at it. The browser is a plugin, so there isn’t an option for the browser in the initial pop-up menu in the text box. You’ll find it once you select the plugin option. Yes, that tripped me up. No, I don’t want to talk about it.

I opened [GitHub issue #1665](https://github.com/httpie/cli/issues/1665) in the in-app browser and typed:

*“I have the GitHub issue open in the browser. Please read it and fix the bug described there.”*

And I was very happy with everything that followed. The page opened in a split-screen layout, directly beside the chat interface.

> Codex understands not only the task at hand but also the codebase itself.

Codex fixed it in 3 minutes. It read the issue, traced the bug to three files in the codebase, wrote a fix, added a regression test, and ran the relevant tests. It also noticed that downloads.py had unrelated changes from my earlier testing and explicitly left it untouched. That let me know Codex understands not only the task at hand but also the codebase itself.

## Codex computer use test

Computer use is a big feature. Codex can now see your screen, move its own cursor, click, and type in apps on your Mac. I had mixed feelings about granting Codex that much access, but I was willing to try for the sake of this article.

> A coding agent with unrestricted terminal access is a security risk.

I granted screen recording and accessibility permissions and asked Codex to open Terminal, navigate to the HTTPie repo, and fix the same bug hands-free. Codex immediately flagged that Terminal.app is blocked from computer use in this session, citing security reasons. It completed the task using its built-in shell instead. I think this limitation is for the best. [A coding agent with unrestricted terminal access is a security risk](https://thenewstack.io/securing-ai-agent-systems/).

I moved to a less risky task. I asked Codex to open Finder, navigate to the project folder, and take a screenshot. It navigated the folder correctly, but the screenshot capture failed. It generated a text-based rendering of the folder contents instead and acknowledged the limitation. The text-based rendering was accurate, though.

Computer use is real, and it works for GUI tasks such as running desktop apps, performing browser-based workflows, and visual UI testing. For terminal-heavy developer workflows, I wouldn’t recommend it. For frontend developers testing UI flows or operating desktop apps, it may prove more beneficial.

## Codex pull request review test

For this test, I pushed a branch with a fixed bug to my GitHub fork and asked Codex to review the PR. Codex read the pull request, confirmed the fix was conceptually correct, and cited the relevant urllib3 and Requests documentation to support its assessment. It then ran the specific regression tests and flagged a genuine gap in the test coverage. The mock test doesn’t exercise real gzip streaming end-to-end, it said, and suggested a follow-up integration test.

The sandbox blocked the full test suite again due to port binding restrictions. This keeps showing up across every tool I have tested, and it is a real limitation of sandboxed agent environments.

It wasn’t perfect, but it worked. The PR review read a real GitHub PR, cited documentation, performed tests, and gave actionable feedback.

Codex is now more than the standard coding agent we’ve come to know and love in the past year. Though not without room for improvement (looking at you, computer use), it’s the most complete [alternative to Claude Code](https://thenewstack.io/agentic-coding-how-googles-jules-compares-to-claude-code/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)