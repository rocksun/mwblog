I’ve never entirely understood the Microsoft roadmap. I certainly enjoyed using Visual Studio 2022 (VS 2022) for C# and .NET development, but when it was dropped for Mac users (replaced with VS Code for the Mac), I assumed we would soon all be using Visual Studio Code — even on PC. As it is, VS Code is fine, but it feels like a Lego solution that you have to build yourself. For example, there isn’t a simple “build” button straight out of the box.

I also don’t know if I have a license or not — I think so, but maybe that’s for Office. Or maybe Pro. Or maybe I am running the Community edition. I can’t remember. Microsoft has always understood how to communicate with their many enterprise customers, but less so with individual developers.

> In response to the AI whirlwind, Microsoft refers to this release with deeper Copilot integration as the first Intelligent Developer Environment (IDE).

What I do know is that [Visual Studio 2026](https://visualstudio.microsoft.com/insiders/) is now available via “Insiders,” its beta build channel. I’ve used [Insiders before](https://thenewstack.io/tutorial-set-up-an-mcp-server-with-net-and-github-copilot/), and the build sat beside my current version without incident. With essential tools like Visual Studio, which so many of us depend on, there is no revolution — just evolution. In response to the AI whirlwind, Microsoft refers to this release with deeper Copilot integration as the first **Intelligent Developer Environment** (IDE). I detect a degree of tongue-in-cheek here; there has been a lot of grand renaming of platforms using AI over the past year.

In this post, I’ll mainly be checking the groundwork, giving developers the confidence to try it out for themselves (or not). But I’m expecting it to be faster and have deeper AI hooks with Copilot (whether I want them or not); plus, I’m hearing the UI is sharper. I’ve also heard it works with the “dead” Windows 10, which is where my current PC dev environment sits — so I’m keen to check that.

## Installing the Visual Studio 2026 Insider Build

So we’ll go for an install on my Windows 10 PC. It is a good idea to note the slightly different icon designs between 2022 and 2026, so you don’t get confused between the two builds. As I start the install the questions start, but they are brief:

[![](https://cdn.thenewstack.io/media/2025/11/be6dd358-image.png)](https://cdn.thenewstack.io/media/2025/11/be6dd358-image.png)

It’s made clear that they will pick up extensions properly, as well things that might be out of support. I use VS 2022 with the Unity extensions, and I checked that it was the Community version:

[![](https://cdn.thenewstack.io/media/2025/11/55db3363-image-1.png)](https://cdn.thenewstack.io/media/2025/11/55db3363-image-1.png)

My email seemed to be sufficient for Microsoft to confirm my identity, but it also asked for GitHub (for Copilot), which enforces full two step authentication. This is what it had to install:

[![](https://cdn.thenewstack.io/media/2025/11/c20a681a-image-2.png)](https://cdn.thenewstack.io/media/2025/11/c20a681a-image-2.png)

So as we finally start the app, loading a known and managed project, the screen looks like this:

[![](https://cdn.thenewstack.io/media/2025/11/58706ad0-image-3-1024x568.png)](https://cdn.thenewstack.io/media/2025/11/58706ad0-image-3-1024x568.png)

First of all, I use a dark theme and I would not have Copilot in the right pane by default. Before I changed to the Unity Project pane, I asked Copilot: “How do I set dark mode?” It gave plenty of answers. In a trice, we were good. Although there was no option to “just do it,” it did offer a script. It also offered screenshots for 2026, so at least it knew the version for sure.

## A Look at the User Interface Enhancements

New files were loaded into the editor fairly rapidly after selecting. The User Interface (UI) is a little clearer — compare the new version of the top pane…

[![](https://cdn.thenewstack.io/media/2025/11/d1d32e9e-image-4.png)](https://cdn.thenewstack.io/media/2025/11/d1d32e9e-image-4.png)

…with the old version below. Same layout, but the old version uses the solid folders. There is little difference beyond that.

[![](https://cdn.thenewstack.io/media/2025/11/a8194fcb-image-5.png)](https://cdn.thenewstack.io/media/2025/11/a8194fcb-image-5.png)

The project was built in about 8.5 seconds, which was probably without the help of a cache.

## Putting Copilot’s AI Features to the Test

Microsoft’s Copilot is the default AI presentation with VS, as you would expect. Now, VS is definitely not intended for vibe coding, but after using so many excellent Agentic CLIs recently, the ChatGPT style of help feels a little dated.

However, Code Completions are my main use of AI in everyday coding. They seem to be a bit smoother in VS 2026 — perhaps the line completion is quicker, and the suggested code is a little less insistent. But I will need more time to assess this properly.

I do have woeful code coverage (49%) in the loaded project, so I was happy to let Copilot create extra tests and see if it can boost coverage. I’ll select one class area where I have recently moved more functionality into:

[![](https://cdn.thenewstack.io/media/2025/11/7e584cc6-image-6-1024x26.png)](https://cdn.thenewstack.io/media/2025/11/7e584cc6-image-6-1024x26.png)

(For those who can’t guess what the columns mean in coverage reports, there are 138 lines of code covered and 232 lines not covered, giving us 37% coverage. So while I don’t believe in leaving tests exclusively to LLMs, we can let it make suggestions. I also have a Mock framework.

[![](https://cdn.thenewstack.io/media/2025/11/33bccad5-image-7.png)](https://cdn.thenewstack.io/media/2025/11/33bccad5-image-7.png)

As it says, this is using GPT-5 mini. I could have changed to Claude Haiku. After running, it created an extra test fixture:

[![](https://cdn.thenewstack.io/media/2025/11/adcfca40-image-8.png)](https://cdn.thenewstack.io/media/2025/11/adcfca40-image-8.png)

I have to put the new tests in myself, which after using agentic tools that do this for me, feels a bit disappointing. The style used is similar to mine, with uses of Mocks when needed. In this example, the only slightly odd thing is the lengthy method name:

```
[Test] public void FetchRoadPoint_ReturnsAssociatedRoadPoint() { 
  var locMock = new Mock<LightweightLocation>(); 
  var locObj = locMock.Object; var mp = new MapPosition(new System.Numerics.Vector2(0, 0), MapPosition.LocTypeCue.None); 
  mp.trackId = 1; 
  RoadPoint rp = ss.RegisterRoadPoint(mp, 0, 0); 
  ss.RegisterAssociation(rp, locObj); 
  RoadPoint found = ss.FetchRoadPoint(locObj); 

  Assert.AreEqual(rp, found); 
}
```

The code builds, so I run the tests through Unity (which is the intended target).

All the tests in the new fixture run:

[![](https://cdn.thenewstack.io/media/2025/11/ccef77ea-image-9.png)](https://cdn.thenewstack.io/media/2025/11/ccef77ea-image-9.png)

Unfortunately, they don’t have any serious effect on the code coverage:

[![](https://cdn.thenewstack.io/media/2025/11/d090365d-image-10-1024x35.png)](https://cdn.thenewstack.io/media/2025/11/d090365d-image-10-1024x35.png)

So it has only covered an extra three lines! I fully admit that since I run the tests from Unity, even an agentic running task couldn’t improve this easily via Visual Studio. It has probably chosen to cover methods that point directly into other structures which don’t help to cover the calling class.

Maybe a better analysis of the task (the coverage reports were accessible) would have helped, but we know there are other apps that specialise in creating tests. By just creating the code templates, I can add my own tests; and actually I would find this more useful.

## Conclusion: An Evolutionary Step Forward

There is much more to Visual Studio than I’ve looked at here, like [profiling with Copilot](https://devblogs.microsoft.com/visualstudio/copilot-profiler-agent-visual-studio/) for example. I can see that my extensions for Unity have been fully respected, and my existing project has been built immediately without a hitch. There is probably no reason not to try this out if you are using Visual Studio 2022 — but expect evolution, not revolution.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)