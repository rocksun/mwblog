# Heroku Moved Twelve-Factor Apps to Open Source. What’s Next?
![Featued image for: Heroku Moved Twelve-Factor Apps to Open Source. What’s Next?](https://cdn.thenewstack.io/media/2025/01/b4f717e5-kccnc-na-24_gail-frederick_featured-1024x576.png)
SALT LAKE CITY — In November, [Heroku](https://www.heroku.com/?utm_content=inline+mention) announced that it had open sourced the development methodology [Twelve-Factor Apps](https://github.com/twelve-factor/twelve-factor). The company had created the method to help developers develop their applications locally and “package it portably across cloud providers, and then have it be able to run resiliently and have it be a delightful experience to build that,” said [Gail Frederick](https://www.linkedin.com/in/gfred/), who serves as Heroku CTO at [Salesforce](https://www.salesforce.com/), in this episode of The New Stack Makers.

Why did Heroku move the project? To get a community involved in updating it, Frederick said.

Heroku Founder “[Adam Wiggins](https://www.linkedin.com/in/adam-wiggins-a7623845) wrote [Twelve-Factor](https://thenewstack.io/learn-12-factor-apps-before-kubernetes/) in 2011 and 13 years later, while the factors have inspired a generation of cloud developers, there are just some areas that are dated, and those are the ones that we’re excited to update after the open source release,” she told host [Alex Williams](https://thenewstack.io/author/alex/), TNS founder and publisher, in this episode recorded at [KubeCon + CloudNativeCon North America](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/).

The “Twelve Factors” Heroku documented were based on common mistakes the company saw customers make in building their applications. But a decade-plus is a lifetime in tech. Frederick described some of the areas of the methodology that demand updating.

For example, “The [Twelve-Factor] manifesto talks about logs and treating logs as event streams,” she said. “And what’s changed in [cloud native development](https://thenewstack.io/cloud-native/) since then is developers need metrics, a wide variety of metrics coming out of their applications, not just textual logs or data format logs.”

A likely change in the new open source Twelve-Factor Apps will be “updating that factor specifically to translate to telemetry and identifying best practices for what metrics your app should be emitting, and then how you move them through into whatever visualization you want.”

The increasing adoption of [OpenTelemetry](https://thenewstack.io/observability-in-2025-opentelemetry-and-ai-to-fill-in-gaps/) might be a factor in modernizing this section of the methodology.

## Reference Architecture Examples
At the time of the Makers recording, Frederick said, the Twelve-Factor team had spent about three months talking with its current maintainers to determine what needs to be done to update the methodology. The focus on telemetry is one thing that came out of those discussions, she said.

“We all also recognize that cloud native developers do not just deploy one app anymore,” she said. “They deploy a system of apps together with multiple backing stores. Twelve-Factor is pretty clear about one app with backing services and a data store, and that’s not the reality for app developers in the cloud today.”

Going forward, Frederick said, she believes the Twelve-Factor Applications project maintainers “will add supporting documents with details about how a factor might be implemented. We will offer [reference architectures](https://thenewstack.io/reference-architectures-and-experience-kits-for-cloud-native/). We will provide code that is an example of a factor in action. And I even think of the Heroku platform as a reference architecture for all of the factors.”

How will success be measured? “I think our work is sufficient in refreshing Twelve-Factor only if we are incorporating app development use cases that include the edge, that include [the Internet of Things], that include serverless, and even that include heavyweight distributed systems that you wouldn’t think of as being cloud native.”

Check out the full episode to learn more about what’s ahead for open source Twelve-Factor Apps and for Heroku.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)