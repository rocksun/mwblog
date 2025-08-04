As I’ve mentioned elsewhere, a lot of regular development work is engineering — not coding. Coding makes up a good bit, but even setting up a project with an IDE and getting the environment working is engineering. It means manipulating OS commands, etc. And because good developers treat their code as data too, they’re used to the idea of targeting it with tools and scripts outside of the IDE experience. This is where agentic **command line interfaces** (CLIs) come in.

## Just Run a Terminal?

Large language models (LLMs) are [better at the engineering than the actual coding](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/). That’s mainly because code development in an IDE can’t really be expressed as a continuous set of request/response pairs. However, move to a shell session within a terminal and that is exactly what we have: command and response.

But because terminal sessions almost span back in time before computing existed, their definition is rather wide. I remember playing Lunar Lander on a teletype session (keyboard, printer and paper) in the school resource room. I could emulate the same queries and response today, but no other physical aspect of that experience would be shared.

It appears that we just have a text interface — some sort of string buffer that gets altered over time. What could possibly go wrong?

I was using the [Render](https://render.com/) service, running my instance, and I connected to a terminal over the web.

Render offers a classic Linux shell via the web, but I needed to quickly copy some text from a file. As the service spins your code up in a transient area, there is no persistent disk to access (well, unless you pay extra).![](https://cdn.thenewstack.io/media/2025/08/aaa3f52e-image-1024x156.png)

Although I can give the `cat` command to show the file, the first thing to remember is that if this is too long, you won’t be able to see the top of the file. Scrollback has a limited number of lines. I didn’t know how to alter this in a window view of a shell I didn’t start. No problem, I could run `less` or `vim`. The first wasn’t available, and the second didn’t want to work over the full screen. It was also impossible to copy any text via the web interface.

![](https://cdn.thenewstack.io/media/2025/08/affe583c-image-1.png)

Vim didn’t want to fill the screen.

On a hosted system, via the web, you simply can’t make too many assumptions. In this case, the web interface is presenting a terminal. While the shell is something very specific, the terminal is more of an ideal that can be implemented in different ways. While you can get around all these issues eventually (and Render is a fine service), agile engineering is about rotating through ever-improved solutions — not spending time on individual tool interpretations.

## Developing a Good Text UI

So there is more to a terminal than just the frontend to an OS shell. The point is well made [in this article by](https://willmcgugan.github.io/announcing-toad/) [Will McGugan](https://willmcgugan.github.io/), CEO of Textualize, a startup promoting rich applications for the terminal. I don’t think the product is ready for review yet, but what McGugan recognizes is important: Emulated terminals are often messy things. And he wasn’t that impressed with what he saw when he used [Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/) and [Gemini CLI](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/).

He first mentions the problems with flicker. This isn’t a showstopper, but it will wear you down with constant use. The problem comes when the screen updates can’t keep up with the changes in information, usually when scrolling. As a game developer, I’m aware of the old issue of finishing changes to the screen before it’s drawn, and the reasons for implementing double buffering solutions, for example. There is a reason why [Zed works hard at keeping its Rust-based editor fast](https://thenewstack.io/how-rust-based-zed-built-worlds-fastest-ai-code-editor/).

There is also the ability to copy just text, not square blocks of the screen. You also need to read the nonprinting characters to maintain line integrity. This always works within a modern IDE, but isn’t so dependable within every terminal session.

Anyone reading my articles in The New Stack will already know of the advantages of using stronger terminal applications like [Warp](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) or [Ghostty](https://thenewstack.io/ghostty-will-get-you-excited-about-using-a-terminal-again/). But there is more to it than that.

## A Console Within a Console

Claude Code, for example, is a terminal application. That needs a little explanation. It’s a program that assumes it’s running within some type of specified terminal.

Claude Code itself is a Node.js application, written mainly in TypeScript and compiled with webpack. If you feel the need to get deeper into this, [Geoffrey Huntley can help](https://ghuntley.com/tradecraft/). You might have discovered that while Claude Code is on GitHub, there is no actual source code available.

To maintain control of a session, most agentic AIs effectively take over from the terminal within which they run.

You can see this in the case of Gemini CLI, where the session is maintained in one block, so to speak, where queries are separated from responses in awkward boxes:

![](https://cdn.thenewstack.io/media/2025/08/fde37fe9-image-2-1024x535.png)

But this isn’t the only way to do it. Compare this with how Warp clearly puts each query and response pair in its own block:

![](https://cdn.thenewstack.io/media/2025/08/148bf16a-image-3-1024x445.png)

This means you can mix normal shell tasks with your agentic session. Obviously, this is easier for Warp, which has added its [agentic CLI to its own terminal application](https://thenewstack.io/developer-review-of-warp-for-windows-an-ai-terminal-app/), but it continues to show that there is much variety in the implementation of a terminal.

## What About Just Talking

Of course, you don’t have to use a keyboard at all. You can just talk. I’ve seen video clips of this working just fine with an agentic CLI, just as it works with your phone. The voice is converted into text so quickly that it’s close to instantaneous. When we thought about conversational programming in the past, some people were always referring to using voice input — but we do need access to the text.

The quickest way to snatch a previous command or response is to scroll back and grab it. There is also the ability to type simple bits of code; you don’t want to do that by voice. Or add images.

Notice how I add some simple code structure in this query:

![](https://cdn.thenewstack.io/media/2025/08/b83b469e-image-4-1024x207.png)

This isn’t going to work via voice. The narrative of conversational programming is too close to Captain Kirk speaking to the Enterprise computer to be a close match to what developers need. In fact, you may remember Spock used a different interface when the computer showed images:

![](https://cdn.thenewstack.io/media/2025/08/6d525a92-image-5.png)

This was a clever way to convey narrative without actually having to show the audience complex diagrams of alien physiology, etc. But it also proved there is a limit to the voice interface, even in fiction.

## Conclusion

For agentic CLI to succeed over the long run, these console sessions need to be quick, responsive and fully interactive. You need to be able to cut and copy quickly and accurately, for example.

Is the right approach for someone to write a very good terminal application with hooks for AI, or a strong common framework to be run within a terminal session, or the Warp approach of working from soup to nuts? Regardless of which approach wins out, developers will not adopt great IDEs only to move down a notch to work with agentic LLMs in a low-quality terminal session.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)