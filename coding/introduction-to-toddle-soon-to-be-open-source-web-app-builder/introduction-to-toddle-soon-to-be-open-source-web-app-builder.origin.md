# Meet Toddle: the Next Open Source Web App Builder
![Featued image for: Meet Toddle: the Next Open Source Web App Builder](https://cdn.thenewstack.io/media/2024/08/5c6b6f6c-kelly-sikkema-jrvxgakzism-unsplash-1024x678.jpg)
Usually the posts I write are for developers who are controlling the majority, if not all, of their stack. But there is also a need to understand how [low-code](https://thenewstack.io/the-highs-and-lows-of-low-code-tools/) solutions can or should be used.

[Toddle](https://toddle.dev), which recently announced an [open source play](https://toddle.dev/blog/toddle-is-soon-open-source?ref=dailydev), is one such low-code/no-code web application builder. It focuses on a component hierarchy for the frontend, with adoption of data at the backend. (My first thought was that if Toddle produces “toddlers” then I think [Tiddlywiki](https://tiddlywiki.com/), which has “tiddlers,” might want a word.)
## Get Started With Toddle
After you sign up, Toddle gets straight into onboarding, asking for your programming experience. In reality, it is checking your role: product designer, no-code developer or software engineer. For the last, it suggests, “You need a professional development environment to collaborate with developers,” which can sometimes be true.

It gives you a prep video from a founder (Andreas Møller) that is quick and informative, while also making clear there are example apps, which is how I usually explore functionality.

I like the two “get started” options because they express the natural fork in how people break things down. Sadly, neither button worked, and I had to start again — but that might just have been an artifact of my aging Mac. Going back in again worked just fine.

## Tinker With an Example Project
The example project it created for me was a live weather app that was already populated with the forecast for my local area. I was impressed.

There wasn’t a very explicit definition of what type of web apps Toddle likes to make, but I intimated earlier that it means [frontend](https://thenewstack.io/frontend-development/) control with [backend](https://thenewstack.io/backend-development/) API support, and the weather app is a perfect example:

The left-hand side is a component hierarchy, with standard HTML, custom bits and things called the result of **formulas**, which I will get onto. The current view of the app is in the middle. I can see a **forward** button to test it and a **publish** button for later on.

My first place to poke (and I could have started anywhere) was to inspect the weather API call. After all, I was running it in the location it suggested, so the weather app clearly uses live data.

By hitting the “weather” API button on the right hand side (the **data panel**), I could clearly see this was from [https://toddle.dev/_api/weather](https://toddle.dev/_api/weather), which I guess is a guarded API of some sort:

The next question is, how do I extract the right value from the API and stick it in the text box? It looks like the value “broken clouds” was added to the cloudy image in this example.

When I clicked on the text box in the hierarchy, I could see where the text box formula was placed:

I could then access its formula:

And yes, I noticed that the result was capitalized, for good measure. The first things I saw were process connection boxes that also exist in [Unreal Engine Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/blueprints-visual-scripting-in-unreal-engine), which are strong enough to run Fortnite.

Now before I drill into the final part of this process, let me criticize it briefly. Technically, you do not have to be a programmer to use these process box flows (formulas). However, you need to **think** like a programmer. I would gently suggest that if, like me, you realize the steps needed to produce the output could be presented neatly in code, or in this slightly lengthy diagram, you are already too far gone to rescue — you are a developer. I’m so sorry. You may just as well get with the coding. Having said that, this process is far more transparent, is perfectly valid, and if customers like it, then nothing further needs to be justified.

I had a little trouble working out how to go back to the data panel displaying APIs, but I’m doing this on a Macbook — naturally the bigger the screen, the easier it is to manipulate a lot of visual pieces. The help function did indicate how I might recover the **data panel:**

Escape didn’t work, but clicking outside the canvas did. I would have gotten there eventually. But it is healthy to remember that this is more than a playpen; it is a tool and has to be learned.

Looking at the data, I can see the path of the description key value:

(I’m in the UK, so the weather is changing as I speak.) I can see that the path of the result within the JSON behind the scenes is “Response” / “data” / “current” / “weather” / “description.” This key gives the value “overcast clouds” right now.

Looking at that weather box in the formula, I have:

For some reason, I can’t expand the box itself, but I can scroll the path parts, and they read “weather” / “data” / “current” / “weather’ / “description,” which matches the path for the data (where ‘Response” is replaced by the API name “weather”).

I made a mistake with the editor, but I was able to step back with the controls at the bottom. By manipulating the API with a tool within the block, I replaced the “description” part of the path with “main,” and the value “Clouds” was immediately visible in the main app:

I found the editing process to make this simple change slightly fiddly, but otherwise straightforward. As I’ve mentioned, this is not too different from using Blueprints in the Unreal editor. Also, tools do need time to learn.

Behind the scenes, Toddle clearly made a random project page, as you can see from the lengthy URL I am using. It also maintains a bit of state information about my edit view:

1 |
https://toddle.dev/projects/weather_web_app_3nhqjtm/branches/start/components/HomePage?mode=design&leftpanel=design&rightpanel=style&canvas-width=800&canvas-height=800&selection=nodes.WVNFMOKheuHNxO7t_BoFU |
I can test the app, and I see a publish button too. Pressing that, I effectively check-in my app:
And finally, I get a live app to look at, maintaining the project name within the URL, which you [can visit too](https://weather_web_app_3nhqjtm.toddle.site/).

I’m not in Lambeth — but all location APIs seem a little inaccurate. Reloading it fixed that.

## Decide Whether Toddle Is Right for Your Team
To decide whether this is the development approach you want to use for yourself or with your team to make web apps, consider these points:

- Take a note of how Toddle wants to recognize the
**roles**of its customers. Check if your team has visual creators and data guys, and how those boundaries work within your team. - If you are using this tool to make working prototypes, you can start immediately. However, If you want to go beyond that, understand what you own and what services the platform maintains. In this case, Toddle is clearly moving towards
[open source](https://toddle.dev/terms/open-source-terms), which is good. - Make sure everyone has a nice large screen. They are cheap and plentiful, fortunately.
- Make sure that creators understand how to manipulate the formulas, or how to hand that off to developer types.
- Work out where old-fashioned coding can be used to rescue any work before you may need to. This isn’t defeatist; it is just making sure you know the boundaries of where your growth and need for efficiency may move beyond the tool’s limitations.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)