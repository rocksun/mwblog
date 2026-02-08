Last month, [I reviewed Claude Desktop](https://thenewstack.io/give-claude-ai-full-access-to-your-local-filesystem-with-mcp/) and noted that the simple addition of giving Model Context Protocol (MCP) permission to use one of your local folders was a strong idea in itself. Anthropic clearly came to the same conclusion, and with agile business speed, it was able to productise this observation quickly with the release of [Claude Cowork](https://claude.com/blog/cowork-research-preview). At the moment, this is “available as a research preview for Pro and Max plan subscribers using the Claude Desktop app on macOS.” But more on that later.

This offering is squarely aimed at nondevelopers. But by releasing this, Anthropic is also doing something that will benefit senior devs — it confirms how their local and practical knowledge of AI can improve colleagues in other departments.

While developers are always respected, we all know we tend to be a “node” in a business because of our specialism. But it turns out that large language models (LLMs) have applications in as many places outside development as in it, and adoption of apps like Cowork suddenly makes the knowledge of developers shine “horizontally,” if you will, across a business. The term “Cowork,” as [Kate Holterhoff points out](https://redmonk.com/kholterhoff/2026/01/16/will-your-ai-teammate-bring-bagels-to-standup/), is carefully chosen for how “vendors want us to think about where agents fit into the future of work.”

For posts like this, referring to any price model is usually foolish, since this is the first piece of information that becomes out of date. I tried using my API usage, but this didn’t work, so I signed up for the Pro plan. I note this only to say that introducing this technology to a general audience will lead to a lot of unexpected token usage and commensurate expense.

## Starting up

I already had Claude Desktop installed and Cowork lives inside Claude Desktop. But I downloaded a fresh copy, just in case.

You can just about see the “Cowork” tab behind the Cowork modal window as I started up the app:

![](https://cdn.thenewstack.io/media/2026/01/10b8d959-image-1024x426.png)

Selecting Cowork gets you the basic user interface:

![](https://cdn.thenewstack.io/media/2026/01/66877b6e-image-1-1024x750.png)

To take it for a spin, I’ll ask it to help tidy my desktop screenshots. In laptop parlance, this is just the temporary folder that ends up holding screenshots. In general, I’m happy to delete everything here. Note that the offer is to “identify” the screenshot image, which allows the LLM to make sense of it. The design means that Cowork connects with only one actual folder — and it knows that a Mac user has a “Desktop” folder.

![](https://cdn.thenewstack.io/media/2026/01/5d617f91-image-2-534x1024.png)

Initially, I was running this in a cafe with a slow connection, and it took an age to finish “setting up Claude’s workspace.” It is only 10% done in the shot above. When the setup was done, I asked for the given option of sorting the screenshots on my desktop.

An important piece of Cowork is to replace the [MCP](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) language with the normal language of folder access. Accordingly, Cowork has to ask MacOS for permission to alter the desktop. This is the equivalent of setting an accessible folder connection through configuration (as discussed in the article about Claude Desktop).

I start the task, and can see the progress steps as it moves through its plan.

![](https://cdn.thenewstack.io/media/2026/01/bbccfd3b-image-4-1024x854.png)

Unfortunately, this all came to a crashing halt with the error shown below:

```

API Error: 400 {
  "type":"error",
  "error":{
    "type":"invalid_request_error",
    "message":"messages.5.content.17.image.source.base64.data: At least one of the image dimensions exceed max allowed size for many-image requests: 2000 pixels"
   },
   "request_id":"req_011CXNQbsiJBdoFGmfdXTs7X"
 }
```

As usual, please remember that this is a research preview, so these are self-imposed limits by Anthropic to prevent issues. To be charitable, I went to my desktop and erased the very large files. A dimension of over 2,000 is quite a large image — and I asked Cowork to identify these for me.  It didn’t want to delete them, but gave me a command to trash them.

![](https://cdn.thenewstack.io/media/2026/01/ef28bbb7-image-6-744x1024.png)

Cowork concluded with an option to ignore the problematic files:

![](https://cdn.thenewstack.io/media/2026/01/a022df7d-image-7.png)

It understood that it had a path to continue the task even with the large files still present, so I agreed to this. While it was working away, I could see the progress:

![](https://cdn.thenewstack.io/media/2026/01/7a41509f-image-8.png)

It finished with a summary of my screenshots and added this very interesting warning:

![](https://cdn.thenewstack.io/media/2026/01/0f38bf8a-image-9.png)

This was correct — only the left side of the code was visible from my post on [Codegate](https://thenewstack.io/getting-started-with-codegate-an-intermediary-for-llm-devs/), but adding this was a nice touch.

It now presented a nice plan with options to take:

![](https://cdn.thenewstack.io/media/2026/01/103f8215-image-10-705x1024.png)

After viewing the complete plan markdown file that it had produced, I chose the (recommended) Full Organization just to see how this would perform. Shortly, it finished with the final layout:

![](https://cdn.thenewstack.io/media/2026/01/0a485f25-image-11.png)

This included renaming the files into something readable; frankly, some people might find this a big win all on its own.

## Conclusion

While Cowork still has to smooth through the error conditions (these are always the last thing eager developers want to work on) and avoid leaving the user in limbo, I found the whole thing very usable. It gave enough options so I could work around its own limitations. Yes, I did use a “developer” mindset while I worked, but I think anyone who works regularly with a laptop would feel comfortable with the user experience.

Given that I thought [Claude Desktop](https://thenewstack.io/give-claude-ai-full-access-to-your-local-filesystem-with-mcp/) plus access to your local folders was a good thing, Claude Cowork is a logical product step, if not a milestone in LLM development. As a developer, you will almost certainly be more interested in Claude Code as a product, but as a knowledge worker and colleague to other people in your workplace, think about Claude Cowork as a way to spread practical knowledge about the scope of LLMs. Depending on the stage of your career, this might be a handy string to your bow.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)