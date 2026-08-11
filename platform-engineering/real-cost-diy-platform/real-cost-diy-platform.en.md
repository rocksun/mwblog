What it actually costs to build your own internal developer platform over five years, and why most “we’ll just build it” pitches are pricing the cheap version.

Sixty people and $7.5 million a year, every year, is what it costs to build and operate your own internal developer platform if you do it the way most enterprises end up doing it, and most of the executives signing off don’t see the number, because it’s spread across multiple cost centers under “engineering.”

The cheap version of the pitch they hear — one team, weekend work, a control plane with a bit of YAML on top — ships v1 and turns into the maintenance burden nobody wants to own. The version that actually works is a sixty-person product engineering organization, indefinitely. The numbers below come from a recent [VMware Tanzu Platform paper](https://images.sw.broadcom.com/Web/CAInc2/%7B68c6ad82-a684-4e39-8feb-12803e4b1f0e%7D_The_Upside_Down_Economics_of_DIY_PaaS.pdf) I helped update, so flavor it with a vendor-salt up front if you feel like you need to. But the staffing structure is good enough to think through.

## The weekend project that turned into a 60-person infinite financial commitment

From what I’ve seen, if you align your platform team with something that feels like the [CNCF platform reference architecture](https://tag-app-delivery.cncf.io/whitepapers/platforms/), you end up with about seven product teams: infrastructure, operations, deployment, runtime and middleware, database, security, and coaching/developer enablement. Each team is a mythic two-pizza team, 7–9 engineers. There’s no personal pan pizzas when it comes to [building your own platform](https://thenewstack.io/internal-platforms-are-products/). Shake a couple of scrum masters and product owners on top to coordinate and manage, and you’ve got about 60 people total. At a conservative salary of $125,000/year per engineer, you’re at $7.5 million in payroll, every year, indefinitely.

> “There’s no personal pan pizzas when it comes to building your own platform.”

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| Annual | $7.5M | $7.5M | $7.5M | $7.5M | $7.5M |
| Cumulative | $7.5M | $15M | $22.5M | $30M | $37.5M |

Five years in, you’ve spent $37.5 million on payroll alone for the team that builds your platform, not even your apps.

## What “buy” actually staffs to

Instead of spending money building and maintaining a platform, enterprises that buy a commercial platform pay staff to operate the platform. And the number of staff needed for that is much lower, as shown by ratios of platform team sizes I’ve collected over the years:

### By developer:

* 6,500 devs / 16 ops
* 2,500 devs / 5 ops
* 1,200 devs / 6 ops

### By developer teams:

* 45 app teams / 5 ops
* 300 app teams / 4 ops

### By apps:

* 350 apps / 7 ops
* 300 apps / 8 ops

These numbers are lower because the above teams do not need to build and continue building the platform. They avoid the constant need for platform maintenance, working on: APIs, integrations, developer frameworks, security pipelines, dashboards, upgrade tooling, the next AI capability your developers want, the next compliance regime your auditors want.

In conversations I’ve had with organizations that built their own platform over the years, there’s a shadow platform engineering “group.” Each development group tends to have at least one person, if not more, who does the glue work between the platform and what the applications teams do. This is often around build and pipeline integration, security, or just figuring out how to deploy apps and hook up to services. This staffing cost is completely unaccounted for in the business case spreadsheets.

## Why this gets ignored

When you expand the cost to build a platform rather than buying it, you see the value in [build vs. buy](https://thenewstack.io/build-vs-buy-the-platform-engineers-guide/) much more clearly. In contrast, if you don’t model the comparison out, the visible cost line for a commercial platform is one license number on one purchase order. The build-your-own headcount is spread across multiple cost centers, often done in the shadows, and looks like normal hiring. The license number is right there on the page; the build-your-own total has to be calculated, and nobody runs =SUM on all those people.

## Works as designed

Engineers also have a story they tell themselves about building their own platform. People get promoted for shipping platforms, and “we shipped a platform built on Kubernetes” is a better promotion-packet line than “we onboarded everyone to a thing we paid for.” This isn’t some moral failing; it’s how many engineering organizations and the HR policies that pay them work, I hope unintentionally. The pattern is called [résumé-driven development](https://arxiv.org/abs/2101.12569), and there’s even a study about it.

When employees are rewarded in pay and prestige based on their ability to deliver new technologies, they start to seek out skills and track records in new technologies. This gets them more compensation in their present job, and sets them up to job-hop to a better-paying job elsewhere. But, as one study found, this pattern doesn’t result in operational perfection:

|  |
| --- |
| Extensive RDD-based technology selection may therefore lead to complex or even unmaintainable software consisting of technologies which are not suitable for the requirements, which are unfamiliar to current or future employees, or which did not deliver on their promise and were discontinued.  *–“*[*Résumé-Driven Development: A Definition and Empirical Characterization*](https://arxiv.org/abs/2101.12569)*,” Jonas Fritzsch, Marvin Wyrich, Justus  Bogner, Stefan Wagner, January 2021.* |

In this dysfunctional system, the more heroics, the more reward. And building your own platform takes a lot of heroics, so it’s attractive.

## Left behind

When it comes to ROI, the most damaging factor is the velocity gap. When you build your own, the vendors keep shipping; you’re shipping too, but against a moving target. Our [paper](https://images.sw.broadcom.com/Web/CAInc2/%7B68c6ad82-a684-4e39-8feb-12803e4b1f0e%7D_The_Upside_Down_Economics_of_DIY_PaaS.pdf) puts it at 12–18 months before the commercial innovation curve outstrips most build-your-own efforts, and the gap widens rather than closes, because the vendor’s team is bigger than yours and their roadmap is funded by every customer they have, not just your one company. The year-three meeting where someone says “we need to add the AI services that Vendor X shipped last quarter” is the meeting where the ROI quietly evaporates.

## For the strategy-nerds: comparative advantage, with a 200-year-old assist

The notion of outsourcing non-core infrastructure is older than computers. In 1817, David Ricardo argued that even if you can do something well, you should focus on what you do best and trade for the rest. Portugal could grow grapes and weave cloth, but it specialized in wine and traded for British cloth because that’s where the marginal return was.

> “The year-three meeting where someone says ‘we need to add the AI services that Vendor X shipped last quarter’ is the meeting where the ROI quietly evaporates.”

If you’re not into early 19th-century economics thought leadership, [Simon Wardley updated the thought leadership with his much-beloved Wardley maps](https://blog.gardeviance.org/2013/01/a-first-map.html): anything that’s already become a commodity should be bought rather than built, so that your scarce engineering capacity is spent on the parts of the business that actually differentiate you from the competition.

Abby Bangser put this in plain English at [KubeCon NA 2025](https://www.youtube.com/watch?v=gmAfYEPBYr0):

*“It’s not about rebuilding what we can purchase that is available on the market. It’s about making sure we spend our time building the things that are bespoke and important for our organization.”*

For most organizations, the platform itself isn’t where you differentiate. Your apps are! The platform is plumbing — necessary, valuable plumbing, but plumbing. A useful test: would your customers pick you over a competitor because of your platform? In Dutch grocery, the answer at Albert Heijn and Jumbo is “no” — shoppers care about prices, the app, the checkout, not the orchestrator behind it. At Picnic, the answer is “yes,” but only for one piece — [the custom narrow delivery trucks that make their last-mile economics work](https://www.ey.com/en_nl/insights/ai/how-technology-made-picnic-the-undisputed-market-leader). Everything else, including the platform, they buy. Knowing which kind of business you are answers the build-vs-buy question for you.

Letting your best engineers spend their careers [writing YAML](https://thenewstack.io/kubernetes-is-getting-a-better-yaml/), wiring continuous integration into your registry, and tracking CVEs in container base images is trading down. You’re spending one of the most expensive resources you have, engineering capacity, on something a vendor will take care of for you. The opportunity cost is what you didn’t build with that capacity: the apps that would actually move the business.

## What to do about it

Here are three practical moves for anyone staring at this decision now:

* Calculate the all-in headcount before the meeting. Sixty is the high end; thirty is the low end if you cut corners. Either way, multiply by your fully loaded engineering cost and put the number on the slide. The license-vs-engineers comparison ends most of these debates by itself. Don’t forget to multiply this out in one, three, five, and more years. History shows that the platform will be with you for a long time.

* Be honest about year three. You want to cost out the full platform and everything that you need to keep it going. This is things like maintenance, integration, and a steady new-feature cost as your developers ask for things commercial vendors shipped two quarters ago. Look at how frequently AI has been changing and improving over the past two years. Can your platform team adapt that fast to make sure you’re getting [those tasty, new AI capabilities](https://www.youtube.com/watch?v=lp1vGxDurOc)?

* Build the developer-facing layer, buy the rest. Portals, golden paths, integrations into your specific business systems are differentiated, so build them. Infrastructure, observability backplane, secrets, certificate management, container registry are commodities, so buy them.

Every enterprise that builds its own internal platform is, whether the executives say so or not, choosing to spin up a small platform vendor inside the company. The economics of running a platform vendor are well known and largely punishing. The companies that pick this path should at least know that’s the choice they’re making. Most don’t, because the choice was never made out loud. It was made by inertia, in the meeting where someone said: “We’ll just build it ourselves this weekend.”

> “Stop building platforms. Start building apps.”

You should avoid the mess and instead [buy a platform](https://www.vmware.com/products/app-platform/tanzu). Or, more bluntly: stop building platforms. Start building apps.

Read more in our paper, “[The Upside-Down Economics of DIY PaaS](https://images.sw.broadcom.com/Web/CAInc2/%7B68c6ad82-a684-4e39-8feb-12803e4b1f0e%7D_The_Upside_Down_Economics_of_DIY_PaaS.pdf).” You can also see a 15-minute presentation on all of this in [my recent talk at PlatformCon 2026](https://talks.cote.io/platformcon2026/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/01/a4afb134-cropped-2f47e82b-michael-cote-e1674132550806.png)

Michael Coté studies how large organizations get better at building software to run better and grow their business. His books "Changing Mindsets," "Monolithic Transformation" and "The Business Bottleneck" cover these topics. He’s been an industry analyst at RedMonk and 451...

Read more from Michael Coté](https://thenewstack.io/author/cote/)