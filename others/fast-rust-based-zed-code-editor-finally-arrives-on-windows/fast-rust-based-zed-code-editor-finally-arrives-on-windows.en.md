[Zed](https://zed.dev/), the “next-generation” code editor from the creators of Atom and Tree-sitter, has finally arrived on Windows. Zed is a quick, Rust-based general code editor with GPU acceleration that [I first reviewed two years ago](https://thenewstack.io/zed-a-new-multiplayer-code-editor-from-the-creators-of-atom/) when it was MacOS only.

When I first reviewed Zed, I wondered when it would come to Windows. As a fundamental programming tool, a code editor has to work on as many systems as reasonably possible. A software developer cannot always choose their working or target platform, so they need reliable tools they can be sure will cover all platforms.

Zed’s initial reluctance to build for Windows is a reflection of their team’s size and experience, not their dedication. So while this review hits a few negative points, I’m confident they will align with the Windows development scene and fix any issues.

I use Zed as my “other” editor — the one that handles files in and around the main project. For me, it can’t take the place of Visual Studio / Visual Code for C#, but is more than good enough for JSON files, Ruby support scripts, etc. I certainly look for it to replace the aging Sublime Text.

Zed always supports keyboard efficiency, and there is almost always a way to bind an operation to the keyboard. However, in 2025 most people do use the mouse, and this is well supported too.

[![](https://cdn.thenewstack.io/media/2025/10/ce6e7d6d-image.png)](https://cdn.thenewstack.io/media/2025/10/ce6e7d6d-image.png)

## First Impressions and Initial Setup on Windows

I’ll test on my old Windows 10 machine, which hosts the Windows side of my development. It feels like I’ve had to use Sublime forever on that machine, so it’s nice to do a virgin install of Zed:

[![](https://cdn.thenewstack.io/media/2025/10/7c24e849-image-1.png)](https://cdn.thenewstack.io/media/2025/10/7c24e849-image-1.png)

It starts with this nice setup page, and you’ll note I could import my Sublime bindings. As I finished setup, it opened out with this welcome page:

[![](https://cdn.thenewstack.io/media/2025/10/9d96f54f-image-2.png)](https://cdn.thenewstack.io/media/2025/10/9d96f54f-image-2.png)

I was intrigued by the “Clone Repository” option, so I entered the url for a repo, entered a target folder and got the following response:

[![](https://cdn.thenewstack.io/media/2025/10/3c4a42ce-image-3.png)](https://cdn.thenewstack.io/media/2025/10/3c4a42ce-image-3.png)

Nothing else was explained. After an update, the opening screen no longer had this available. So I guess we should forget this for now and assume it will be fixed in the background. As I said, this is the bleeding edge.

## Language Support and File Encoding Issues

After opening a project, Zed detects the language of the code file and invites you to load up the correct language server. (It would have to be a much more obscure language than C# not to detect it):

[![](https://cdn.thenewstack.io/media/2025/10/41f60bf7-image-4-1024x576.png)](https://cdn.thenewstack.io/media/2025/10/41f60bf7-image-4-1024x576.png)

We then immediately get the expected ordered coloration.

If you look closely at the screenshot above, you can see an underscore as the very first character, which the file apparently ignores, but it can’t be deleted without problems. This is because the format the file is saved in is UTF-8 with BOM (or Byte Order Mark), which Zed does not recognize. As mentioned, this is something that Zed will be more aware of as they synch with issues more likely to appear with Windows.

I also found refreshing diagnostics did not work particularly smoothly, but again this seems minor. Lets get into multibuffers and cursors.

## Understanding Multibuffers and Multiple Cursors

Multibuffers act as windows into different files, but all on one page. As an example, I can search for references to a method. In VS Code, these would be listed in another pane. But in Zed we see them all together:

[![](https://cdn.thenewstack.io/media/2025/10/e3cff681-image-5.png)](https://cdn.thenewstack.io/media/2025/10/e3cff681-image-5.png)

Expanded, these are all windows into the relevant file, with a few lines for context above and below in each case:

[![](https://cdn.thenewstack.io/media/2025/10/2caa0991-image-6-1024x393.png)](https://cdn.thenewstack.io/media/2025/10/2caa0991-image-6-1024x393.png)

I can enter any buffer and edit it directly. You can also see that I can jump to the source file as well. In addition, I can make global changes. When in a multibuffer, it is possible to use multiple cursors to edit every file simultaneously. Below, I selected instances of the class term `GainedKnowledge` and extended all of them at the same time:

[![](https://cdn.thenewstack.io/media/2025/10/5d15d754-image-7.png)](https://cdn.thenewstack.io/media/2025/10/5d15d754-image-7.png)

This is a more generic feature than the close equivalent “change symbol.”

## Integrated AI with Anthropic’s Claude

One of the nice conveniences is `control-+`, which allows you to zoom in on just the file text content, and it works quickly.

When I first reviewed Zed, “signing in” seemed to be a strange and even controversial requirement for an editor, even though it was mainly for using the collaboration features. Now, of course, people sign in their AI vendors anyway. Speaking of which, Zed goes with Anthropic’s Claude as its default built-in large language model (LLM) agent, though it can work with any vendor:

[![](https://cdn.thenewstack.io/media/2025/10/4577b2b6-image-8.png)](https://cdn.thenewstack.io/media/2025/10/4577b2b6-image-8.png)

I wasn’t going to look at the AI part, as that will clearly operate at least as well as it [has done before](https://thenewstack.io/an-introduction-to-zed-ai-and-how-it-compares-to-cursor-ai/https://thenewstack.io/how-rust-based-zed-built-worlds-fastest-ai-code-editor/). However, it did help me introduce the terminal.

## Using the Integrated Terminal

When authenticating Claude, it defaulted to the cute terminal login:

[![](https://cdn.thenewstack.io/media/2025/10/7aa6b62f-image-9.png)](https://cdn.thenewstack.io/media/2025/10/7aa6b62f-image-9.png)

After choosing options, this allows Zed to separate from Anthropic’s charging authentication in a nice fashion, while also answering the payment question:

[![](https://cdn.thenewstack.io/media/2025/10/bddef958-image-10.png)](https://cdn.thenewstack.io/media/2025/10/bddef958-image-10.png)

While it did have to go to the web to finish, the terminal disappeared once I was done on the web — a nice touch.

I brought up the terminal again via the command palette `ctrl-shift-p`, which ties commands to keybindings. After requesting a fresh terminal return, I noted it used Powershell:

[![](https://cdn.thenewstack.io/media/2025/10/1322daed-image-11.png)](https://cdn.thenewstack.io/media/2025/10/1322daed-image-11.png)

Of course, what exactly “the terminal” is in Windows varies depending on what you need, [as Warp for Windows also discovered](https://thenewstack.io/developer-review-of-warp-for-windows-an-ai-terminal-app/). For me, it is [git bash](https://gitforwindows.org/), but others use [WSL](https://learn.microsoft.com/en-us/windows/wsl/). I think these options will be improved over time.

Finally, the costs have now centered on AI use. Though as before, most people will probably not be paying initially.

[![](https://cdn.thenewstack.io/media/2025/10/cadcb82d-image-12.png)](https://cdn.thenewstack.io/media/2025/10/cadcb82d-image-12.png)

## Conclusion: Zed’s Future on Windows

There is enough here for Zed to stake a claim in having a fully supported editor in every major system, and that in itself lifts it to an exalted position. The longer it can withstand the Windows-specific bug reports in its Discord channel, the quicker the product will mature.

Zed is still slightly at odds with the developer community, in that it focuses on speed and AI. But I expect it to get increasing traction as everyone’s “other” editor.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)