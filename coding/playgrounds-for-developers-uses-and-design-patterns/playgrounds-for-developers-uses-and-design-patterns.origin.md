# Playgrounds for Developers: Uses and Design Patterns
![Featued image for: Playgrounds for Developers: Uses and Design Patterns](https://cdn.thenewstack.io/media/2024/11/ca93c214-steve-johnson-y3x_x_6_7pw-unsplashb-1024x576.jpg)
If there is one thing that makes it easier for me to look at new software — and share functionality with others — it is a well executed example playground. In recent times they have become staples of the developer relations experience, encouraging developers to try out example code or even prototype solutions.

So what exactly is a code playpen or playground? They’re typically websites that allow small code examples, displayed in an editable panel, to be run with the output visible on the same page. They use code examples to show off a target platform, library or API. The user (or player) can edit the examples or totally rewrite them. For user interface (UI) components, this means the example layout would run in the next panel, giving instant feedback.

How exactly a playground is made, or even exactly what purpose it serves, tends to vary considerably. But they are clearly fruits of the web and offer convenience.

Playgrounds are typically websites that allow small code examples, displayed in an editable panel, to be run with the output visible on the same page.

So what are the negatives? Clearly the infrastructure of a playground needs to be managed or require the attention of otherwise busy devs. Other things, like which library version is currently used or how long to maintain a persistent instance, also require policy.

One issue for smaller startups is that they may not maintain public running instances of their libraries at all. If you don’t see yourself as a platform, it can be a bit of a jump to publicly host your own libraries in front of mock data. But with ChatGPT and similar AI services, we have the opposite case: The product is already a public-facing site where a query is run in the cloud and the result returns to a response panel.

## Hints on Playgrounds
It is common for playgrounds to morph into their own paid services, even when they originate as ways to show off a platform’s abilities. So what they offer commercially needs to be assessed by the provider on a regular basis.

Reporting the version of the target library or platform is important — or rather, not doing so just causes unnecessary problems for players. The ability to switch versions is cute, but whether that is worth the infrastructure complexity depends on how pronounced the edge between versions is.

Clearly some playgrounds could just be [WebAssembly](https://thenewstack.io/webassembly/) containers, but many collect, process and output data specifically through their own platforms. The big difference in design is the ability to define a unique playground instance that allows a player to share or return easily to their example. This isn’t a complete necessity, but it is a boon to prototypers.

Defining policy for playgrounds helps guide players and devs alike.

Error output can be tricky. The people using a playground probably don’t want to sort through dense style exception output, so a quick AI parse is preferable. As a maintainer, you don’t really owe a player a detailed explanation, but if it is part of the product or service you are pushing, sensible error reporting will be remembered. As with all consumer-facing infrastructure, you probably want an instance ID visible on screen to help with observation and error-fixing. This can sit alongside branding.

As stated earlier, defining policy helps guide players and devs alike. For example, how long a saved instance lasts — even with free use — should be noted somewhere in any documentation pages.

## Playground Examples From Around the Web
Here is one example from [db-fiddle](https://www.db-fiddle.com/f/6Fj2vw8bFhzVADG4UFUjD6/0) that I cut down from my post [about SQL schema generation with LLMs](https://thenewstack.io/sql-schema-generation-with-large-language-models/).

This playground, which has been around for a while, offers an upgrade to a paid service and hosts ads on the site. The ability to create and run [SQL](https://roadmap.sh/sql) against a schema is particularly useful from an educational standpoint. The basic design has separate panels for editing and output, which is the norm. The input has to be split into schema and query, which marks this out as a slightly more cumbersome case. But already we can see some of those bells and whistles that mark the better playgrounds:

- It can convert the response into Markdown. This makes the results more portable.
- It clearly states the target SQL Server flavor and version, which can be switched.
- It creates a URL for you and allows further versioning with your example entries.
- It has (limited) panel arranging.
- As mentioned, the example above is made from a previous post and still bears the title and description of that
[instance](https://www.db-fiddle.com/f/6Fj2vw8bFhzVADG4UFUjD6/0).
Limited and contained AI options can also aid the user — note the “Text to DDL” button to help with rapid schema creation.

A more recent playground is from [Deno](https://thenewstack.io/how-oop-developers-can-get-to-know-typescript-through-deno/). It has a much more obvious use case: to show you examples of code that can use its deployment service.

This example is designed more as a tutorial but has the classic code and response panels. While it deploys a live URL (which you can [still visit](https://share-duck-20.deno.dev/)), it also displays the result in a panel, along with other options. As it is showing how its key/value store works, there is a detailed tab to help. The Deno playground doesn’t show version information, although that wasn’t an issue. The live examples are managed under a dashboard.

Here is one last, very simple example, just to ensure the definition is wide enough. In [this example](https://labs.os.uk/public/os-api-resources/code-playground/web-maps/leaflet-basic-map), the Ordnance Survey wants to show users how to embed its map information into a leaflet:

You can play with the map data in the code to point to anywhere in the UK. While this is very simple, it does demonstrate how an API key and some JSON data can provide what you need without having to spend time setting up any form of development environment. This has no bells and whistles, even though some help with famous places, along with their longitude and latitude, would have helped.

**Conclusion**
Playgrounds are wonderful windows into the potential of new libraries, APIs and platforms. I encourage startups to carefully maintain their own, and consumers to push their providers into making them.

While playgrounds should be free to use initially, the developers need to be disciplined in stating policy, cleaning up their resources and keeping a lid on costs. All these aspects show the company in a good light, while delighting players.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)