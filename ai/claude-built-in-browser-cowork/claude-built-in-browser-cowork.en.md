Anthropic is [giving](https://claude.com/blog/cowork-built-in-browser/) Claude its own browser.

As the company announced on Wednesday, Claude on the desktop (Mac, Windows, and Linux) now has access to a built-in Chromium-based browser in Cowork that allows it to surf the web right where you’re already doing your work.

This finally puts Anthropic’s Claude desktop app in line with OpenAI, which recently gave up its ambitions to build Atlas, its stand-alone browser, and instead added it to its [ChatGPT desktop app](https://thenewstack.io/openai-codex-work-atlas/).

This new feature is now rolling out to paying Pro, Max, and Team plan subscribers.

## A browser, not your browser

Previously, for Claude to browse the web, you had to install a [Chrome extension](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn?hl=en-US&pli=1&utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform). That always felt a bit like a hack, though it worked reasonably well. But having used the ChatGPT app with the built-in browser — and the ability to quickly take screenshots in the browser and discuss them with the model — having a dedicated browser in these apps makes many workflows much easier.

Fun fact: the original Claude Chrome extension launched exactly a year ago, on August 26, 2025. It’s also only been two weeks since Anthropic [launched](https://thenewstack.io/claude-chrome-cowork-sessions/) a major update to the Chrome Extension, essentially turning it into a Cowork session. But the AI development cycle moves quickly, and two weeks is a very long time.

![](https://cdn.thenewstack.io/media/2026/08/4471347a-cowork-browser-1024x576.png)

Credit: Anthropic.

“Until now, giving Claude the ability to use the web in Cowork meant giving it access to your browser through the [Claude in Chrome](http://claude.com/claude-in-chrome) extension,” Anthropic explains. “When the work is on a page you already have open, that’s still the right choice. But a lot of web tasks don’t need *your* browser, just*a* browser, and now Claude has one.”

There is still a use-case for the Claude Chrome extension, though. It’s still useful to have Claude in the sidebar to talk about a page you have open in your browser.

“Claude in Chrome is for the page you already have open, with the accounts you’re already signed in to, such as updating your CRM, working through your inbox, or editing the doc in front of you,” Anthropic explains.

Also, if you have the extension installed already, it will remain the default for Claude to surf the web, unless you explicitly change your preferred browser in the Claude Desktop settings.

## Bringing your logins across

The team notes this is very much “Claude’s browser, not yours.” But since it’s separate from your day-to-day browser, it doesn’t have your login info, for example. To work around that, Anthropic lets you bring your logins from Chrome, Edge, and Firefox on macOS — and Firefox on Windows and Linux.

The company very explicitly notes that logins from your banking and email providers, as well as any single sign-on sites, are explicitly excluded, unless you really insist on giving Claude access to your Schwab accounts.

The reason this list is inconsistent based on the operating system is likely that Chrome and Edge on Windows ensure that third-party applications can’t read your local cookies as an infostealer countermeasure. Firefox still stores these in a plain SQLite database. On MacOS, Chrome’s key is in Keychain, and other apps can request it from the user.

## The risk is not zero

In this context, Anthropic also stresses that there is always a risk of prompt injections when letting an agent loose on the web. The company built safeguards into the Chrome extension and the built-in browser, but also notes that despite its best efforts, “the risk is not zero.”

Since the browser isn’t likely to be logged into many sensitive sites, if something goes wrong, the blast radius here is hopefully small.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)