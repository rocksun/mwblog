# Revised Docker Hub Policies: Unlimited Pulls For All (Paying Customers)
![Featued image for: Revised Docker Hub Policies: Unlimited Pulls For All (Paying Customers)](https://cdn.thenewstack.io/media/2025/02/d92ef3a7-amie-johnson-vjxlzqi5tle-unsplash-1024x683.jpg)
[Docker](https://www.docker.com/?utm_content=inline+mention), the popular containerization platform, has announced significant changes to its [Docker Hub](https://hub.docker.com/) policies, set to take effect on April 1, 2025. The [Docker Hub changes](https://www.docker.com/blog/revisiting-docker-hub-policies-prioritizing-developer-experience/), which were initially planned for March 1, have been delayed by a month.
When they appear, I expect paying Docker customers to be happy. Docker has revised its previously announced pull limits and eliminated consumption-based charges for image pulls. The new policy includes:

- Unlimited pulls are available for all paid Docker subscribers, subject to fair use limits.
- Unauthenticated users are limited to 10 pulls per hour per IP address.
- Free authenticated users are now allowed 100 pulls per hour, up from the previously announced 40.
- No more pull count limits or consumption charges at all.
In addition, Docker has indefinitely delayed implementing storage-based billing. The company plans to focus on developing better tools for managing storage before considering future charges. If storage pricing is introduced in the future, customers will be given at least six months’ notice.

These changes came after [Docker raised its subscription plan prices](https://thenewstack.io/docker-overhauls-simplifies-subscription-plans/) for Docker Pro and Docker Team. These policy changes aim to maintain Docker Hub as a reliable and scalable platform while prioritizing developer experience. The company estimates that only about 7% of Docker users will be affected by the new limitations on unauthenticated pulls.

## Reaction from the Community
Those free users are especially vocal. Over at [Ycombinator](https://www.ycombinator.com/), users of the free service [are complaining](https://thenewstack.io/bypass-docker-hub-rate-limits-with-this-stateless-image-cache/) about how this will damage their work and how Docker didn’t give them enough notice. Others, however, are pointing out that “[There’s been a good 2-3 months of communication](https://news.ycombinator.com/item?id=43129450), though it may not have been as granular or targeted as some would have liked.”

Still, other opponents to the change snarl, “[It’s bait and switch](https://news.ycombinator.com/item?id=43131967) that has the stakes of ‘adopt our new policy, that makes us money, that you never signed up for, or your business fails.'” The most popular post on the thread, however, observes, “[Can’t believe the sense of entitlement in this thread](https://news.ycombinator.com/item?id=43125967). … why would you expect a commercial company to give you containers for free?”

Of course, if you can’t stand this Docker Hub policy change, no one’s holding a gun to your head insisting you use this service. Some have already [turned to Podman](https://thenewstack.io/whats-new-with-podman-5-multiplatform-images-vm-support/), while there are also new services such as [Spegel, a stateless cache for locally storing image artifacts](https://thenewstack.io/bypass-docker-hub-rate-limits-with-this-stateless-image-cache/). Besides, while Docker Hub is still the most popular container storage service, there are many others, such as GitLab Container Registry, GitHub Container Registry, and JFrog Artifactory.

## Security Issues
The policy changes come in the wake of a recent security incident involving a [malicious Kong Ingress Controller image on Docker Hub](https://hackread.com/malicious-kong-ingress-controller-image-dockerhub/), highlighting the importance of robust security measures in container registries. Security doesn’t come for free.

As the containerization landscape continues to evolve, Docker’s policy updates reflect the company’s efforts to balance platform sustainability, business profitability, and user needs. These changes’ effectiveness and impact on the broader container ecosystem remain to be seen as the implementation date approaches. I expect both Dockers and its customers to benefit.

*TNS Analyst Lawrence Hecht contributed to this post.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)