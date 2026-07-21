Comic Sans has been mocked, memed, and muzzled from corporate communications since time immemorial, but most people won’t know that it actually came to prominence via a 1990s IRC client called [Comic Chat](https://en.wikipedia.org/wiki/Microsoft_Comic_Chat) that turned typed conversations into comic strips.

Now, Microsoft has announced that it’s open-sourcing the Comic Chat client, handing the codebase over to the community to explore and build on.

In a [blog post](https://opensource.microsoft.com/blog/2026/07/16/microsoft-comic-chat-is-now-open-source/) published Thursday, [Robert Standefer](https://www.linkedin.com/in/rstandefer/), principal program manager on Microsoft’s Copilot Acceleration Team, and [Scott Hanselman](https://www.linkedin.com/in/shanselman/), VP and member of technical staff at Microsoft/GitHub, explain that the release is an act of preserving a piece of internet history, one born at a point when the norms of online communication were still being created.

“It emerged during a period when the internet was still discovering what it wanted to become,” they write. “Many rules had not yet been written, which gave developers permission to try bold concepts that might seem unusual even today.”

> “It emerged during a period when the internet was still discovering what it wanted to become.”

## Comic timing

Microsoft debuted Comic Chat in 1996 as a novel way to experience Internet Relay Chat ([IRC](https://en.wikipedia.org/wiki/IRC)), a text-only protocol for real-time group conversation that predates modern chat apps.

Rather than scrolling text, the client read what people typed, then built comic-style panels around it in real time — picking illustrated characters, speech bubbles, poses, and facial expressions to match. Crack a joke, and a character might grin and slap its knee; get combative, and it could fold its arms and scowl.

![Comic Chat + Comic Sans](https://cdn.thenewstack.io/media/2026/07/eda00d75-fasf-1024x656.png)

*Comic Chat meets Comic Sans*

Those speech bubbles needed lettering that looked hand-written rather than typed, which is where [Comic Sans](https://en.wikipedia.org/wiki/Comic_Sans) entered the fray. Microsoft typographer [Vincent Connare](https://en.wikipedia.org/wiki/Vincent_Connare) had designed the font back in 1994, and it was first introduced as part of a Microsoft Windows add-on pack. However, Comic Chat’s comic-book styling was to prove a more natural showcase, long before it turned up on office birthday flyers and became design circles’ favorite thing to hate.

Comic Chat wasn’t a standalone download, instead riding on the back of Microsoft’s biggest software of the era. The client first reached users bundled with Internet Explorer 3 in 1996, then found a larger audience when Windows 98 shipped with it built in as a default component, putting an IRC comic generator on millions of desktops.

Comic Chat, like many early internet applications, slowly gave way to more sophisticated forms of online communication as the web matured — instant messengers, forums, and eventually the messaging apps we use today.

Some three decades on, Microsoft has now decided the client is worth revisiting, but more as a piece of history to hand over to the people who might still find something in it.

## Comic Chat comes alive for modern systems

The [GitHub repository](https://github.com/microsoft/comic-chat) includes the original Comic Chat source largely untouched, alongside a few updates Microsoft calls “AI-powered modernization attempts.” These make the ancient code build in current versions of Visual Studio, connect it to modern IRC servers, and fix its display on today’s high-resolution screens.

> “These are not polished re-releases, but worked examples that show Comic Chat can still come alive on modern systems.”

Microsoft is careful to position the updates more as a demonstration, inviting the community to take the code further from here.

“These are not polished re-releases, but worked examples that show Comic Chat can still come alive on modern systems,” the authors write. “We’re excited to see what improvements, ports, experiments, and entirely new forms the community brings to it next.”

It’s also worth remembering that Comic Chat’s tone-reading was rules-based: a fixed set of triggers mapped to a fixed set of poses and expressions, with no fancy LLM behind it. That gap is a fair comparison point for how different today’s AI-driven chat agents and avatars are from the halcyon days of yore, since a modern model generalizes to text it’s never seen, while Comic Chat could only react to cues its developers anticipated in advance.

> “It anticipated the idea that software could interpret a conversation and give an avatar expressive behavior, rather than merely displaying text.”

Asked whether there are any conceptual similarities between the engine of Comic Chat and today’s AI-driven avatars and agents, Hanselman tells *The New Stack* that while he does see a throughline, there is no legitimate way of describing that earlier technology as generative AI.

“It anticipated the idea that software could interpret a conversation and give an avatar expressive behavior, rather than merely displaying text,” he says.

Moreover, Hanselman singles out how Comic Chat pulled off its expressiveness in the first place: human-drawn art, paired with a set of rules simple and visible enough for anyone to inspect.

“It is both a wonderful nostalgia release and an important example of human-centered computational creativity,” Hanselman continues. “In some ways, it is less an ancestor of image generation than an ancestor of expressive avatars and agents.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)