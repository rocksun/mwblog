# Framework Lets React Developers Create Video With Code
![Featued image for: Framework Lets React Developers Create Video With Code](https://cdn.thenewstack.io/media/2024/09/4a1d9a03-pexels-mediocrememories-1117132-1-1024x683.jpg)
React is known for its ability to create frontend web animations and special effects. Programmer [Jonny Burger](https://www.jonny.io/) found video editors challenging to use, so he decided to take React’s animation capabilities and build a framework that uses [React code to create videos](https://github.com/remotion-dev/remotion/blob/main/packages/docs/static/img/fireship-quickgif). It’s called [Remotion](https://www.remotion.dev/).

“There are many unsolved problems left for video, for people who want to build their own video editor,” Burger told The New Stack. “Our mission is to allow people … to allow an individual to build their own really good video editor in a weekend.”

## Why Create Videos with React Code?
Why would anyone want to create video with code? First, it’s difficult to programmatically alter video using existing tools, Burger said.

“Video editors that let you click a button to export video and to interface with these programs programmatically — it’s very hard because it’s not what they were made for,” he said.

Second, it’s possible to do more than just create a video with Remotion. In fact, there are three main use cases for using Remotion:

- Creating motion graphics, which add operations such as subtitling or special effects such as zoom to your video;
- Producing videos en masse; and
- Creating your own video editor for multiple users.
One marathon organizer in Switzerland used Remotion to provide a personalized video for runner showing them crossing the finish line. The organizers used Remotion to batch render the video, incorporating an animation of their time and a cut-in greeting from a famous marathon runner.

Some users are even adding AI to the mix, allowing them to combine AI avatars with special effects animations and subtitles using Remotion, he said. That approach is already used to create videos for YouTube and TikTok, he added.

[Submagic](https://www.submagic.co/) is one [company that uses Remotion](https://www.remotion.dev/showcase) in this way, allowing users to upload long-form videos and use AI to extract short snippets, which are captioned, and special effects added to make them more engaging for social media sites. Burger said they’re creating more than 100,000 videos a month with this technique.
Software developers can also create their own video editor with Remotion, he added.

![React code used in Remotion to render video.](https://cdn.thenewstack.io/media/2024/09/0535431d-remotion.jpg)
Screenshot from [Remotion’s site](https://www.remotion.dev/).

“There are so many different video, audio formats and codecs out there, and to deal with whatever the user throws at it is actually really difficult,” he said. “Our plan is to solve a lot of boring problems so that you are able to create a video editor like you’re used to, but you don’t need to spend decades building it.”

## Remotion’s Unique License
Remotion is open source so the code is available, and more than 200 developers have contributed to it. That said, Remotion does have an [unusual approach to licensing](https://github.com/remotion-dev/remotion/tree/main?tab=License-1-ov-file). There is a [free license](https://github.com/remotion-dev/remotion/tree/main?tab=License-1-ov-file#free-license) for individuals, non-profits, evaluation purposes and businesses of only three people, and then there is a separate [business license](https://github.com/remotion-dev/remotion/tree/main?tab=License-1-ov-file#company-license) for larger companies that want to use the framework commercially.

Burger said the license grew out of a fear that the project would prove popular but he wouldn’t have the resources to properly manage it.

“I usually would publish all my projects as open source, and I had a fear that this would blow up so much, but open sourcing, it’s literally giving it away for free,” he said. “I’m also an advocate for other maintainers that they should, before [open sourcing a project](https://thenewstack.io/the-future-of-open-source-needs-more-give-and-less-take/), think about how it’s looking on the [sustainability side](https://thenewstack.io/how-to-build-open-source-sustainability/), from the money and time that they have to invest to make the project big. I hope that people in general think more about this and adopt similar licenses.”

Thanks to the licensing tiers, Remotion is in a break-even state, he said, and Burger can pay himself and Mehmet Ademi, Remotion’s business manager.

## Competitors
There are other open source options for creating video, such as [FFmpeg Hi](https://sourceforge.net/projects/ffmpeg-hi/), but they’re not “really programmable” with if statements and the ability to pull in data, Burger said. They also do not show live preview, he added.

“Our videos are fully programmable with code, so you essentially code a website. We use the browser as our canvas, because the browser is really good at displaying all kind of of graphics. Then we provide a way to turn that into a video.”

— Jonny Burger, creator of Remotion
Remotion is a pioneer in using code to create videos, Burger contended, adding that there two similar, but not really the same, projects: Framer Revolution, a React animation library, and [Motion Canvas](https://www.remotion.dev/docs/compare/motion-canvas).

“Our videos are fully programmable with code, so you essentially code a website. We use the browser as our canvas, because the browser is really good at displaying all kind of of graphics. Then we provide a way to turn that into a video,” he said.

If the plan is to make only one video, then a traditional video editor will probably meet your needs, Ademi added.

“If you have the skills for the traditional video editors and you want to create only one video, you’d rather use those,” Ademi said. “What we provide is basically a solution for scalable video production. So a full use of Remotion would be creating your own web video editor so that people can use it to create their videos, which is a simplified version of an Adobe After Effects video editor, for example.”

## Video Legos
Moving forward, Remotion plans to add small packages so developers can just install a package to solve a specific video problems — like [Legos pieces](https://thenewstack.io/how-to-build-an-interactive-lego-robot-using-python/) for video, he said. For instance, there is already a package that automates transcription, and Burger plans to add a package for including a GIF in the video.

“Over time, we plan on making this more and more like Legos, where you just put together the right packages,” he said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)