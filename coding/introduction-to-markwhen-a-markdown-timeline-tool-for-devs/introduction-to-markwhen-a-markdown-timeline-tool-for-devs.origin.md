# Introduction to Markwhen, a Markdown Timeline Tool for Devs
![Featued image for: Introduction to Markwhen, a Markdown Timeline Tool for Devs](https://cdn.thenewstack.io/media/2024/12/a9f3d4a6-diana-light-fpbtaoqvi-k-unsplashb-1024x576.jpg)
As a developer, [I like Markdown](https://thenewstack.io/obsidian-and-the-case-for-using-more-markdown/). The argument against its use is that the format is not ruthlessly enforced — it allows divergent versions and similarly named patterns, for instance. Yet its weakness is also a strength. Which brings us to [Markwhen](https://www.notion.so/Markwhen-152ba3b27486804f8093c832a18cafc6?pvs=21), which describes itself as a “text-to-timeline tool where you write markdown-ish text and it gets converted into a nice looking cascading timeline or other visualizations.”

So Markwhen is both a format for time, and an editor showing gant-chart-like time series or cascading timelines. There is an Obsidian plug in too, which I’ll try out later. In looking at Markwhen, a service designer can also peer into the complexities of dealing with time representations.

## An Event
The basic unit of expression is the *event,* which is made of a date range and a description separated by a colon. However, quite a lot of things make the running as “dates”. All of these are acceptable events for Markwhen:

- “12/2012: End of the world”
- “1961: Year after 1960”
- “2020-02-22T12:13:14Z-now: How long the pandemic has been going on?”
- “1892/2021-08-12: Example of EDTF date range”
This is pretty liberal, so we need to look a bit more closely at what is going on.

## Lets Make It a Date
Markwhen deals in *date ranges* but if we just mention a single date, it will look at the granularity and mark the edges as the range. So for “1961”, the range defined is between 1st January 1961 and 31st December 1961.

Markwhen understands the usual human readable date formatting:

- “04/1776” would be April 1776
- “11/11/2024-12/12/2024” would be 11th November to 12th December.
We can deal with whether we use the American Month/Day/Year format a bit later.

As we will be looking at dates, let’s familiarize ourselves with the [Extended Date/Time Format (EDTF)](https://www.loc.gov/standards/datetime/), which Markwhen also uses.

These things refer to dates:

- “1985-04-12” refers to the calendar date 1985 April 12th.
- “1985-04-12T23:20:30” refers to the date 1985 April 12th at 23:20:30 local time.
- “1964/2008” is a 44-year range.
- “2004-02-01/2005-02” is a time interval beginning with a date but ending in a month. So, this is a far more fuzzy period definition than you might expect.
- “2004-02-01/2005” similarly starts with a date but ends in a year.
Markwhen also understands “now” and relative dates. Fortunately, there is [a playground](https://docs.markwhen.com/parser/playground.html) that spits out JSON, so we can examine different events.

So for the event “12/2012: End of the World”, you get several useful snippets from the JSON:

123456789101112131415 |
"firstLine": { "full": "12/2012: End of the world", "datePart": "12/2012", "rest": " End of the world", "restTrimmed": "End of the world" }, ... "metadata": { "earliestTime": "2012-12-01T00:00:00.000Z", "latestTime": "2013-01-01T00:00:00.000Z", "maxDurationDays": 31, ... } |
Here is a relative date, and the output clears up what is meant by ‘1 year: When is this’ when I asked it just now, which is Friday 6th December in the afternoon.
123456789101112131415 |
"firstLine": { "full": "1 year: When is this", "datePart": "1 year", "rest": " When is this", "restTrimmed": "When is this" }, ... "metadata": { "earliestTime": "2024-12-06T13:26:19.958+00:00", "latestTime": "2025-12-06T13:26:19.958+00:00", "maxDurationDays": 365, ... } |
So it is clearly a year from now.
## Front Matter
As you would imagine, it would help to throw this tool some cues about what format to expect. Fortunately, Markwhen can read [front matter](https://gohugo.io/content-management/front-matter/), which starts many Markdown documents. So, to fix the European format, we could use:

12345 |
--- title: My Timeline dateFormat: d/M/y #Travel: blue --- |
That third entry is a *tag,* and in the front matter, you can express a color that you want any visuals to use when expressing that event. Just pop the tag at the end of the event to apply it.
## Finally Some Visuals
While we can play around with Markwhen format, output and visuals on the front page [app](https://markwhen.com/), we really want to use the specialist editor [Meridiem](https://docs.markwhen.com/interface/overview.html) to show off a bit more. I downloaded the app, but it also exists [here](https://meridiem.markwhen.com/example) on the web.

The only extra things in this example are *sections and groups*, which are self-explanatory visual organizers. The calendar pops up when you click into a date range.

## Obsidian
So we’ll end up using the tech in an existing app — after all this is the ultimate proof it can live in the real world. Remember that the only portable data is the Markwhen code; and currently you are limited by the number of apps that support it. Fortunately, Obsidian is one.

In my version 1.7.7 Obsidian, through settings, I turned on community plugins with restricted mode off:

From that, I could Browse for Markwhen, which has been updated recently:

The sidebar shows the Markwhen icon, from where we can start a new file.

As soon as I start the front matter, it had a nice helper.

This fairly simple effort…

…produced this chart:

(Naturally, this is just for illustrative purposes) The timespans can all be manipulated, as you might expect.

## If Not Now, Markwhen?
This has only been unveiled recently by [Rob Koch](https://github.com/kochrt), so where this is going — and in what contexts — are open to question. There is a [VS Code](https://marketplace.visualstudio.com/items?itemName=Markwhen.markwhen) extension, for example. The web app editor is not open source, but the rest seems to be.

Clearly, this needs to grow into an ecosystem with enough solutions that it becomes established. Koch [mentions](https://news.ycombinator.com/item?id=42289690) working on a blog app that uses the format to organize post entries. He also mentions an iCal integration, which would be a good idea. Before Markwhen can proliferate, devs will need to have ready-made add-ons that they can use to enhance their own products.

To be fully successful, Markwhen would have to work bottom-up with libraries as well as top-down with apps. Whichever direction emerges first is already delivering timeline goodness.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)