# How Heroku Is ‘Re-Platforming’ Its Platform
![Featued image for: How Heroku Is ‘Re-Platforming’ Its Platform](https://cdn.thenewstack.io/media/2025/04/56e4407a-kccnc-eu-25_betty-junod_featured-1024x576.png)
Building an internal platform, or moving a legacy monolith to microservices and the cloud, can be a huge undertaking. Such projects might pale in comparison, though, to what [Heroku’s](https://www.heroku.com/?utm_content=inline+mention) been up to for the last year and a half.

In that time frame, the Platform as a Service company has been “re-platforming the platform,” according to [Betty Junod](https://www.linkedin.com/in/bettyjunod/), chief marketing officer and senior vice president of [Heroku at Salesforce](https://thenewstack.io/how-heroku-is-positioned-to-help-ops-engineers-in-the-genai-era/). (Salesforce has owned Heroku since 2011.)

“That’s a big enough decision for end-user organizations,” Junod told me in this On the Road episode of The New Stack Makers, recorded at [KubeCon + CloudNativeCon Europe](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/), in London.

“But then for someone like us, who is hosting thousands and thousands of end users on our platform, it was kind of a big decision.”

The next generation of Heroku, [codenamed Fir](https://blog.heroku.com/heroku-fir-generally-available-new-platform-capabilities), will move to general availability this month.

As part of its re-platforming, Heroku reaffirmed its open source bona fides. It moved to [Kubernetes OCI](https://thenewstack.io/kubernetes-1-31-arrives-with-new-support-for-ai-ml-networking/) ([Open Container Initiative](https://opencontainers.org/)), open standards that govern container formats and runtimes.

The new, improved platform also includes [Heroku Cloud Native Buildpacks](https://github.com/heroku/buildpacks), which allow developers to create a production-ready container image for their applications without using a Dockerfile.

Heroku, which started in 2007, was an early developer of [Buildpacks](https://buildpacks.io/), said Junod. “It was before [Docker](https://www.docker.com/?utm_content=inline+mention), it was before containers. It was the early days of [AWS](https://aws.amazon.com/?utm_content=inline+mention). And so our service is built on AWS, but we, our engineers, had to custom roll our own containerization using LXC and our own orchestration.”

The project started out on Ruby on Rails, Junod noted. Today, it supports eight languages, including [Go](https://thenewstack.io/introduction-to-go-programming-language/), [Java](https://thenewstack.io/introduction-to-java-programming-language/), [PHP](https://thenewstack.io/php-creator-rasmus-lerdorf-shares-lessons-learned-from-the-last-25-years/) and [Python](https://thenewstack.io/python/).

## Rethinking the ‘Twelve-Factor Apps’ Methodology
Heroku has become a platinum member of the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention), Junod told the Makers audience, signaling an increased commitment to the open source community.

.As part of its three-year platinum membership, “we have a seat on the governing board, so we’re actively participating there,” she said. “As we’re looking at the technologies we can bring into the platform, it allows us to kind of engage with those contributors and projects.”

For instance, “OpenTelemetry is another one we’ve been … spending more time with because we’re bringing that into the platform. So this has really been the beginning of a much more fruitful journey with the entire cloud native ecosystem.”

This past November, Heroku open sourced its [Twelve-Factor Apps](https://github.com/twelve-factor/twelve-factor) methodology (you can learn more about that from [a previous episode of Makers](https://thenewstack.io/heroku-moved-twelve-factor-apps-to-open-source-whats-next/)). The Twelve-Factor Apps standards were “kind of a manifesto methodology… on how to build reliable, performing apps for the cloud,” Junod said. “Because it was still new. People didn’t know; how should we do certain things?”

Going forward, she said, the community will be involved in updating that methodology, addressing issues like secrets and workload identity that have gained in relevance over the years.

The question project contributors will be asking about the Twelve Factors, she said is, “How do they still apply in today’s world? Because now we have lots of companies who have run massive amounts of infrastructure and massive amounts massive applications at web scale.

“So how can we take those learnings, codify them into updating those factors, and maybe some factors need to be looked at and applied differently now that we know more. And then sharing that back out with the community. “

Check out the full episode for more on the next generation of Heroku, including how it’s integrating AI and the needs of data scientists as well as developers into its platform.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)