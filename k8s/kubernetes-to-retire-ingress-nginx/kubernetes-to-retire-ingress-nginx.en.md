We warned you!

Today, [Ingress NGINX](https://github.com/kubernetes/ingress-nginx) is still being used by [50% of Kubernetes users](https://isovalent.com/blog/post/state-of-kubernetes-networking-report-2025/) to manage incoming traffic, but [it’s long been slotted for retirement](https://thenewstack.io/cncf-retires-the-ingress-nginx-controller-for-kubernetes/). We warned you, but did you listen? Nope. After the news was out, [44% of you were still using it](https://www.reddit.com/r/kubernetes/comments/1ox4doz/results_of_what_ingress_controller_are_you_using/), according to a Reddit survey!

Wow. Seriously, are you folks gluttons for punishment? Because I hate to break it to you, but the Kubernetes Steering and Security Response Committees just announced on January 29th that “In March 2026, Kubernetes will retire Ingress NGINX.”

So, can you deploy an Ingress NGINX replacement in the next two months? Or, shades of those who are [still running CentOS Linux](https://thenewstack.io/havent-migrated-off-centos-yet-you-have-until-june-30/) after it kicked the bucket on June 30, 2024, will you keep running it and hope against hope that no one exploits it? 

Mind you, [Chainguard will still support Ingress NGINX via its EmeritOSS program](https://thenewstack.io/chainguard-emeritoss-backs-minio-other-orphaned-projects/), so there is that. If that’s your plan, you should start talking to [Chainguard](https://www.chainguard.dev/) really, really soon.

Keep in mind, though, that, as the Kubernetes Steering Committee (KSC) says, “There will be no more release bug fixes, security patches, or any updates of any kind after the project is retired.”

![](https://cdn.thenewstack.io/media/2026/02/d92f5a9c-kubernetes-ingress.png)

How Kubernetes Ingress works (credit: CNCF).

## Security concerns

You should also remember that first, if you’re using Ingress NGINX, it’s core to your Kubernetes deployment. Second, the program’s been prone to security vulnerabilities such as “[IngressNightmare.](https://securitylabs.datadoghq.com/articles/ingress-nightmare-vulnerabilities-overview-and-remediation/)” This set of five vulnerabilities, uncovered in March 2025, included one security hole, which, as security company [Datadog](https://www.datadoghq.com/) put it, should be “considered the most serious of the five and has been assigned a CVSS score of 9.8 (critical). When chained with one of the lower-severity vulnerabilities, it allows for unauthenticated remote code execution.”

Do you want to face this kind of problem on your lonesome? I don’t think so!

Adding insult to injury, the KSC warns, “Existing deployments will continue to work, so unless you proactively check, you may not know you are affected until you are compromised.” In short, what you don’t know can hurt you. Hurt you badly! 

## Why retire Ingress NGINX?

So, why is the KSC putting Ingress NGINX out to pasture if it’s so vital to so many Kubernetes deployments? Well, none of you stepped up to support the program.

Open-source programs start as someone scratching an itch, but those that end up being used by tens of thousands need support. They need funding, programmers, and maintainers. Guess how many maintainers this mission-critical program had towards the end. Go ahead, guess.

That would be one, occasionally two. As the KSC writes, “it has been maintained solely by one or two people working in their free time. Without sufficient staffing to maintain the tool to a standard both ourselves and our users would consider secure, the responsible choice is to wind it down and refocus efforts on modern alternatives like [Gateway API](https://gateway-api.sigs.k8s.io/guides/getting-started/).”

The KSC members continue, “To be abundantly clear: choosing to remain with Ingress NGINX after its retirement leaves you and your users vulnerable to attack.”  Get the picture?

If you soon find yourself stressed by trying to maintain the program on your own or switching to another one — oh, and by the way, there are no drop-in replacements for Ingress NGINX — you have no one to blame but yourself.

Can’t someone come to the rescue on a white horse now? Nope. The KSC has reached the end of its tether. “We did not make this decision lightly; as inconvenient as it is now, doing so is necessary for the safety of all users and the ecosystem as a whole. Unfortunately, the flexibility Ingress NGINX was designed with, which was once a boon, has become a burden that cannot be resolved. With the technical debt that has piled up, and fundamental design decisions that exacerbate security flaws, it is no longer reasonable or even possible to continue maintaining the tool even if resources did materialize.”

Good luck. You’re going to need it. 

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)