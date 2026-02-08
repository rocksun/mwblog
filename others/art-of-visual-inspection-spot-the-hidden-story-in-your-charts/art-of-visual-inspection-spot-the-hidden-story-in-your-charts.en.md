You have a nice set of data, but how do you convey its meaning to an audience?

In the latest of a [series of free technology talks](https://learning.acm.org/techtalks-archive), the Association for Computing Machinery presented [noted](https://scholar.google.com/citations?user=uAsnKo0AAAAJ&hl=it) researcher and author [Angelica Lo Duca](https://alod83.medium.com/) to talk about “How to Extract Meaningful Insights from Data.”

If the topic seems hopelessly broad for a one-hour tutorial, you’ll be pleasantly surprised by how effectively she boils it down to a few key principles, ones that could be used to give a narrative to any set of data.

Lo Duca offers several “heuristic techniques” to pull the insight from data. For this talk, she did not worry about the statistical unpinning; rather, she focused on what can be learned from eyeballing a chart (“visual inspection”). She developed these techniques by teaching data journalism students, she told the virtual audience.

Lo Duca is a researcher for Italy’s Institute of Informatics and Telematics of the National Research Council, and author of [“Become a Great Data Storyteller: Learn How You Can Drive Change with Data”](https://www.wiley.com/Become+a+Great+Data+Storyteller%3A+Learn+How+You+Can+Drive+Change+with+Data-p-9781394283323) as well as the upcoming [“Learning Generative AI Tools for Excel: Speed Up Your Everyday Tasks with Microsoft Excel, Copilot, ChatGPT, and Beyond.”](https://www.oreilly.com/library/view/learning-generative-ai/9781098190163/)

Any discovery you make in your data is an insight, she said. Data can contain multiple insights, depending on the analysis you perform. But when thinking about these things, you want to focus on one insight at a time.

She offered ways to analyze data in three formats: temporal, location and categorical.

## Temporal analysis

Temporal analysis studies [data patterns through time](https://thenewstack.io/how-time-plays-a-crucial-role-in-aggregating-mobile-data/). On a simple X/Y analysis, a period of time can elapse along the horizontal Y axis  while an aggregation of all the [events at a certain point of time are captured](https://thenewstack.io/fluent-bit-a-specialized-event-capture-and-distribution-tool/) on the X axis:

![Screenshot](https://cdn.thenewstack.io/media/2026/01/a4393d7d-acm-lo_duca-01.png)

The chart shows the number of times something happens each year, with a peak number of these events taking place in 2021.

Here, the insight comes not from the peak point, however, but from the range between the points where the events started increasing each year (2014), and the year they started declining (2021). That’s where the story lies.

One approach would be to explain what [happened at the starting event](https://thenewstack.io/what-happens-to-relicensed-open-source-projects-and-their-forks/) that kicked off this trend, and then explain what happened at the ending event to bring the trend to a close.

But to find this story, you usually have to look outside the data itself, Lo Duca advised. The explanation can be in the public sphere, such as a news item of interest that took place in these inflection points. Or it could be an event that happened internally to the company itself.

For example, in the chart above, the data may have been about product sales. So, 2016 may have been the start of a new sales campaign, and 2021 was the year that a new competitor entered the market.

The same analysis can be done with a negative peak, or the lowest point in a chart.

If there are no peaks, then compare the starting and ending points of the line, calculate the difference between the two. There’s the story; The product may have an 186% increase in sales, or 50% decrease.

### Everything is under control

But what if nothing is happening to your data? Your temporal line is neither on the ascension nor the descension? What if it is just bouncing around?

There’s a story there, too.

In these cases, Lo Duca advised, you need to set up a “threshold” either above or below all the data.

If the data line is under the threshold, then the insight is that the “situation is under control.”

Logging systems operate by this idea, with the user being alerted only when the data line breaks over the threshold. The situation is no longer under control.

Over the threshold? The situation remains out of control.

## Spatial analysis

With spatial analysis, you are plotting points in space, rather than in time.

While temporal analysis looks for changes over time, spatial analysis [seeks how data](https://thenewstack.io/the-rise-of-community-driven-data-analysis-in-the-age-of-ai/) moves in space. It’s the same logic, but in a different dimension.  Both look for peaks, tends and stability.

In an example, Lo Duca showed a map of Europe dotted with data points.

Locations with many points could be called “hot spots.”

Insights can be gained by comparing different locations. Why does Italy have more points than France or Germany? What’s the story there?

![Map of Europe with dots scattered around.](https://cdn.thenewstack.io/media/2026/01/86716dc7-acm-luca-data_storytelling-2.png)

You can also find insight in [comparing neighboring regions](https://thenewstack.io/cloud-pue-comparing-aws-azure-and-gcp-global-regions/). Why does Italy have this trait, but Spain not so much?

Locations with other commonalities can be compared as well, she said: “If I’m analyzing weather, I can look at locations with the same climate.”

For maps without hotspots, you can look for gradients, which highlight a trend in a particular direction.

A gradient can be drawn through Europe, from south to north, which will then allow you to measure the extremes. (In these cases, make sure all the other variables associated with areas being compared, such as [time of the data](https://thenewstack.io/how-time-series-data-empowers-telcos-to-stay-competitive/) sampling, are relatively equal.)

![A map of Europe](https://cdn.thenewstack.io/media/2026/01/a64bffa9-acm-luca-data_storytelling-3.png)

A gradient through Europe.

No gradients? No problem. Use your thresholds, as described earlier. Thresholds can be derived from [historical model data](https://thenewstack.io/historical-data-and-streaming-friends-not-foes/), defined by laws or standards, or some other external factor.

## Comparing categories

Another form of data comparison is that of categorization. Different types of a thing can produce different data points, and those can be compared.

An insight, then, may come from looking at the leading category, and seeing how far ahead it is from the others.

![Bar chart.](https://cdn.thenewstack.io/media/2026/01/35de2a8b-acm-luca-data_storytelling-4.png)

A group of categories, with a clear leading category.

In other cases, you may not have a dramatically leading category. But here, you can gain insight from looking at how the categories are distributed. What are the numerical differences between each category?  Are there a set of categories that exceed the values of the rest? Perhaps the first five categories have 90% of the values. There’s an insight.

Or, you can also use your old friend the threshold,  to separate categories that are doing well, for instance, from those that aren’t doing so well.

## Other tricks

Temporal, spatial and categorical were the three types of analysis that Lo Duca concentrated on for her talk. Once she explained them, you could see how similar they are:

| Temporal Analysis | Spatial Analysis | Multi-Category Analysis |
| --- | --- | --- |
| Peaks | Hotspots | Leading category |
| Trends | Gradients | Ranking |
| Stability | Uniformity | Stable |

In the talk, she also discussed a few other forms of analysis and what to do with anomalies. Like all ACM Tech Talks, this one is free, so give the entire talk a listen if you want to learn more.

And, if you want to get fancy with your stories, also check out the talk Lo Duca gave earlier this year, [“Applying Cinematic Techniques to Data Storytelling.”](https://learning.acm.org/techtalks/datastorytelling)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)