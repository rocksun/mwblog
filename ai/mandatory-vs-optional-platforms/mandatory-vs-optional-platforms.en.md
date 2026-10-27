**Platform teams that mandated their internal platform** were more than twice as likely to say it delivered most or all of its goals: 62.2%, compared with 27.5% for teams that made adoption optional. Over the same year, the share of mandated platforms in our research fell from 63.0% to 45.9%, and optional platforms became the majority.

That puts the data at odds with the most repeated advice in platform engineering. [Team Topologies](https://teamtopologies.com/), the [CNCF’s Platform Engineering maturity model](https://maturitymodel.cncf.io/), and a 2026 review of the [platform engineering literature](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full) all say a platform should earn adoption through self-service instead of forcing it. [Evan Bottcher’s](https://martinfowler.com/articles/talk-about-platforms.html) 2018 description, still widely cited, said a platform “cannot stand on a mandate alone.” Going into the [2026 Future of Platform Engineering report](https://octopus.com/publications/future-of-platform-engineering-report), we expected optional adoption to win out. The data pointed the other way.

> “An agent never chooses a platform. It works within whatever access someone configures for it…”

Mandates also travel with leadership backing and budget confidence, so the mandate alone probably isn’t what drives results. That distinction matters more now that coding agents open pull requests and, in some organizations, trigger deployments. An agent never chooses a platform. It works within whatever access someone configures for it, which shifts the useful question from whether to mandate the platform to which policies the platform should enforce.

## Mandatory adoption delivers, even as optional takes over

For teams reporting mandatory adoption, 62.2% say they delivered most or all of the benefits they set out to achieve. Among teams with optional adoption, that figure is 27.5%.

![](https://cdn.thenewstack.io/media/2026/10/371b81d4-image-1024x899.png)

***High-performing teams by adoption strategy. Asterisk indicates significance (\*p<0.05).*** *(source:* [*Octopus*](https://octopus.com/publications/future-of-platform-engineering-report)*).*

Here’s what adds real weight to this contradiction: the industry isn’t just recommending optional adoption; it’s moving toward it. A year ago, 63.0% of platforms in this research were mandated, and 37.0% were optional. This year, that’s flipped; optional platforms are now the majority at 54.1%, compared with 45.9% that are mandatory. Teams are following industry advice; however, the performance data suggest there is more to the picture.

**Two different questions get two different answers.** Mandatory adoption is the stronger predictor of whether a platform delivers on its goals. Optional adoption, however, speaks to something else entirely: a platform earns its place because developers choose to use it, not because they are being asked to, which is a success in its own right.

## What comes bundled with mandatory platforms

Mandatory adoption tracking, goal delivery, and performance make more sense when you consider several other factors. In the network analysis of the survey data, we found that mandatory adoption doesn’t travel alone (see network analysis figure below). It clusters with stronger leadership direction, higher job satisfaction, and greater confidence in budget safety, and all of these correlate with one another and with goal delivery.

![](https://cdn.thenewstack.io/media/2026/10/371b81d4-image-1-1024x691.png)

***Network analysis for mandatory adoption, organizational governance, goal delivery, and AI.*** *(source:* [*Octopus*](https://octopus.com/publications/future-of-platform-engineering-report)*)****.***

The simplest explanation here is likely leadership support. Leaders who genuinely sit behind a platform are the ones who make it mandatory, and that same support helps secure budget. In this sense, mandatory adoption is just one piece of a bundle that includes funding and leadership direction.

AI sits in a similar cluster. Respondents who reported the most positive impact from AI also reported stronger budget confidence, clearer leadership direction, and higher job satisfaction. AI’s impact was also associated with mandatory adoption, though to a lesser extent.

This data is cross-sectional, so we can’t establish which factor comes first or influences the other. Either way, the takeaway is the same: without leadership engagement and the budget commitment that usually accompany it, a mandate is unlikely to deliver the same result.

## Where mandatory adoption matters most

A closer look at the same data shows where mandatory adoption delivers value and where it doesn’t. Mandatory platforms are considerably more likely to report higher confidence in budget renewal (78.9%) than optional platforms (50.0%). When considering adoption strategy, budget confidence, and goal delivery together, we found that budget confidence matters more for optional platforms than for mandatory ones.

Moving from low to high confidence in budget renewal for optional platforms, goal delivery, or performance lifts, from 9.5% to 52.4%, is a big jump (see figure below). For mandatory platforms, budget confidence shifts similarly, but less dramatically (from 37.5% to 70.0%).

![](https://cdn.thenewstack.io/media/2026/10/fa44af14-image-1024x686.png)

***Budget confidence by goal delivery for both optional and mandatory adoption strategies*** *(source:* [*Octopus*](https://octopus.com/publications/future-of-platform-engineering-report)*)****.***

What does this mean in practice? Mandating platforms makes performance less dependent on budget safety. An optional platform’s success is tightly bound to whether its funding feels secure; a mandatory platform holds up more consistently either way. It’s less about mandating an underfunded platform and more about mandatory platforms being less exposed to the budget risk that clearly makes or breaks optional platforms. For a platform lead who can advocate for only one thing, this is worth knowing: mandatory platforms appear most effective when funding is uncertain, and less so once the budget is secure.

Mandatory adoption also helps standardize, alongside budget confidence. It may reduce decision fatigue and tool sprawl that inevitably come with everyone choosing their own path, letting the platform handle security, compliance, and governance rather than leaving every team to solve them.

This matters more as agents take on more delivery work. Where a developer might consider deviating from standard processes, an agent will follow whatever routes the system makes available, and standardization helps make those routes safer.

## What a mandate can’t do on its own

None of this suggests that mandatory adoption is a guaranteed win. Relying on mandatory adoption can carry a problem rather than fix it. Our data hints at this: less reliable documentation tracks more closely with mandatory adoption than with optional adoption. When developers have no choice, getting the basics right is not a priority, since the mandate addresses problems that would normally drive users away.

> “When developers have no choice, getting the basics right is not a priority…”

In our dataset, mandatory platform adoption was weakly associated with higher overall job satisfaction. Even more interesting, mandatory platforms were no more likely to track developer satisfaction. Under mandatory adoption, this matters because adoption numbers no longer show whether the platform is working.

The more cautious position here isn’t “forcing adoption wins”; it’s this: mandate the policies (i.e., security, cost control, the standards a business actually needs) and make platform adoption itself optional. A platform that’s the path of least resistance in meeting those policies will win people over on its own. When done well, this retains the benefits of mandatory adoption, including scale and standardization, while preserving the signal from developers choosing the platform. A useful measure of any platform is whether developers would still choose it if they weren’t required to.

This case grows as agents take on more of the work. Documented policies and manual reviews are only effective when people engage with them. Agents need the same policies, but they must be built into the delivery process, making the platform that enforces them the most practical option for both developers and agents.

> “The strongest platforms probably need both: a reason people have to use them, and a reason they would want to.”

[Evan Bottcher’s](https://martinfowler.com/articles/talk-about-platforms.html) 2018 statement was correct: forcing people onto a platform isn’t enough. But our data suggests that relying on people to choose the platform may not be enough either. The strongest platforms probably need both: a reason people have to use them, and a reason they would want to.

For agents, who don’t choose at all, the platform itself has to build in the safe path.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/63781866-cropped-c61358ad-unnamed.png)

Charlotte Fleming, is a developer researcher at Octopus Deploy, conducting industry research on Platform Engineering, AI adoption, and Continuous Delivery. She is the author of Octopus Deploy's Platform Engineering Pulse report and the lead researcher and author of the AI...

Read more from Charlotte Fleming](https://thenewstack.io/author/charlotte-fleming/)