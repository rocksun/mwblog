Until now, I’ve generally only used LLM tools with existing projects. Attempts to create detailed projects from scratch via agentic LLMs like Claude with “vibe coding” often fail, despite the earnest efforts of the LLM. It often forgets information or burns tokens running in a non-productive loop.

In this post, I’ll look at the popular Claude extension [GSD](https://github.com/glittercowboy/get-shit-done), and how it works to defeat [context rot](https://redis.io/blog/context-rot/).

# **Something rotten in the state of LLMs**

It is important to differentiate between trends that are genuine improvements on a pattern and those that are just getting around current restrictions. Dealing with “context rot” is the latter, so it shouldn’t be considered anything more than a temporary workaround reflecting LLM technology as it exists at the moment. But it definitely exists.

The now-famous paper [“Attention is all you need”](https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf) has guided researchers towards LLMs that manage to work their way through meaning and emulate an understanding of sentence structure. But [research](https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.arxiv2023.pdf) does suggest that earlier tokens get more attention than later ones, whatever the size of the context window. Hence, we get rot.

For the usual short prompts, this is no issue at all. But for lengthier tasks, the research notes “attention dilution”, as if the LLM is a bored 6-year-old. One answer to this is to split problems up into tasks for sub-agents to consume, and yet somehow keep the overall context intact.

### So what is GSD?

[GSD](https://github.com/glittercowboy/get-shit-done) (I’ll stick with the acronym for this post) adds some meta-programming (described as a context engineering layer) on top of Claude. I’ve looked at one of the earlier spec-driven systems, [AWS’s Kiro](https://thenewstack.io/aws-kiro-testing-an-ai-ide-with-a-spec-driven-approach/), but this isn’t quite the same.

GSD fights the context rot problem by providing an internal task planning framework with judicious use of sub-tasks that already exist in Claude Code. I’ll attempt a small project with it and see how we do.

As I described in the article about [Claude Cowork,](https://thenewstack.io/how-claude-cowork-helps-developers-spread-the-ai-knowledge/) overly ambitious projects will just end up as a bonfire of tokens. So I’ll stick to what I often ask for — a front end for viewing a set of JSON objects via ID as if they were a database. If asked, I’ll provide the JSON templates. I won’t specify a particular front end.

### Installing and planning

I installed GSD via npx:

![](https://cdn.thenewstack.io/media/2026/01/8cd46f7d-image-1024x802.png)

Then I started Claude in that directory from my Warp terminal:

![](https://cdn.thenewstack.io/media/2026/01/628dfe65-image-1-1024x450.png)

And then used `/gsd:new -project`. (Note I’m using Claude Pro, not an API plan.)

![](https://cdn.thenewstack.io/media/2026/01/51eebba5-image-2-1024x286.png)

And then after GSD examines its start conditions, the ~~interrogation~~ questioning begins:

![](https://cdn.thenewstack.io/media/2026/01/245a06ec-image-3-1024x181.png)

Note the green percentage progress meter at the bottom, which I assume moves towards completion. GSD starts a git repository — so all that remains is for me to do is to define the project as I have above. It is vague, but enough to start a conversation with.

The quality of the project will now obviously hinge on the quality of my responses to GSDs questions. They are largely the right questions, but there are many:

![](https://cdn.thenewstack.io/media/2026/01/9b74131c-image-4-1024x323.png)

First, it explores who the audience is — much like the release of any product. However, in this case, the answer is exactly the first option above. This is for colleagues.

I wasn’t actually expecting the next question:

![](https://cdn.thenewstack.io/media/2026/01/0fed1d23-image-5-1024x474.png)

The answer is a mixture of things, but technically it may as well be the first answer; I want to avoid colleagues working directly with JSON files. Again, the next question is very well targeted. My initial purposeful vagueness is being carefully skewered:

![](https://cdn.thenewstack.io/media/2026/01/922591d5-image-6-1024x476.png)

I didn’t mention whether users would need to edit the data. That would obviously be good, but might extend the project quite a bit. Yet it feels reasonable to set that as an expectation. Ok.

![](https://cdn.thenewstack.io/media/2026/01/5d25f63a-image-7-1024x27.png)

So while I never explicitly stated the app was for viewing (I used the term “search”), GSD intelligently picked up on my concerns. This is how GSD differentiates between requirements, phases, and overall planning.

After describing the type of objects, and the rough number, and how the search begins, we came to the question of which platform to target. Because I added the overall requirement for editing, thus the need to work with a set of inconsistent files, I went for a desktop app. It recommended a Web app, which I would certainly agree with if it were just for viewing.

So far, all I have done is answer the same type of questions that a sensible designer would ask of a manager who woke up one morning with an idea he couldn’t implement himself.

The first multi-select question was also (indirectly) about CRUD:

![](https://cdn.thenewstack.io/media/2026/01/77d32bd7-image-8-1024x511.png)

For ease of use, I also fixed the target OS to macOS.

I was deeply amused by one of the last planning questions:

![](https://cdn.thenewstack.io/media/2026/01/af069461-image-9.png)

This underlines the principle of planning a product with a known purpose. That my colleagues use the app is always at a premium.

It created a [PROJECT.md](http://PROJECT.md) file and the tokens started to be burned, as expected. That green percentage row/dial seemed still to be under 30%, which was interesting. It committed its own project and meta files and continued. I let it work “YOLO” (i.e. non-interactively) and chose “quick” planning. I also let it work on plans in parallel.

If you’re about to ask whether this process made me think harder about what I actually needed, the answer is a definite yes.” I chose no research options, just for implementation from planning. I also didn’t bother with verification steps. These were recommended but would use many more tokens.

In summary, we have this for a planning configuration:

![](https://cdn.thenewstack.io/media/2026/01/dce358b9-image-10-1024x707.png)

It then created a plan for version 1, which I defined as just a viewer, with all the basic viewing functions as expected. No editing needed. So we reached a fair set of v1 requirements:

![](https://cdn.thenewstack.io/media/2026/01/b7baba93-image-11-1024x522.png)

It could also be said that if I just started doing this myself, I would be a good way through it by now, but this is the developer’s dilemma. Human vibe coding is no more sensible than letting an LLM do it. I think I initially refused a roadmap, but I think GSD ignored me and produced one anyway:

![](https://cdn.thenewstack.io/media/2026/01/55eb1507-image-12-1024x559.png)

So it created a simple roadmap along with phases, goals, requirements, criteria, and verification steps. Progress is still only a third, but we now have more files.

GSD throws attention between the different stages, creating a network of documentation based on what it gleaned from my answers.

We finally got to an execution phase.

![](https://cdn.thenewstack.io/media/2026/01/0f7d6bb9-image-13-1024x632.png)

It chose to use SwiftUI, which was fine. And lots of files were created. But we’ll stop here for this week. I’ve never used Swift, but part of the point of this form of coding is that my job is limited to direction and planning, not execution.

Here is what was built, with verification steps. We’ll examine this next week.

![](https://cdn.thenewstack.io/media/2026/01/bdc69542-image-14-1024x822.png)

### Conclusion

We’ve seen that Claude, via GSD, is capable of detailed project planning, extracting sensible steps from a vague project. What is a little different is that this planning structure is managed directly by GSD — they were not defined by me.

Now, in order to drive the process, I did have to understand how planning works, but the questions were definitely “product” centred. Neither of us mentioned design principles such as CRUD directly, and I never discussed the target implementation platform explicitly.

In my next post, we’ll look at the SwiftUI application that GSD just cooked up and see how it performs.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)