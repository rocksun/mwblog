# It’s Time To Start Shifting Left
![Featued image for: It’s Time To Start Shifting Left](https://cdn.thenewstack.io/media/2024/09/5798c9ad-nick-fewings-s7cyjr_3prc-unsplash-1024x683.jpg)
[Nick Fewings](https://unsplash.com/@jannerboy62?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash.](https://unsplash.com/photos/selective-focus-photography-of-white-arrow-signage-S7cyjr_3prc?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
Imagine a house passed down through generations, each owner adding their personal touch. Over time, the original structure becomes obscured by layers of renovations. Walls are built over, plumbing is rerouted, and electrical systems are patched together. Eventually, the house becomes a maze of mismatched updates, and simple repairs become daunting tasks — mainly if the house wasn’t built on strong foundations in the first place.

This is the state of much of the world’s software today. It’s not crumbling before our eyes as a house would exactly — it’s just slowly eroding. High-profile recent outages like Crowdstrike are simply making people finally notice. Outages have also stopped [people from buying baked goods](https://www.bbc.co.uk/news/technology-68628348), disrupted[ rail and flight travel](https://www.theguardian.com/business/article/2024/jul/19/uk-airports-trains-disrupted-microsoft-global-it-outage), and prevented[ online bank transfers](https://www.bbc.co.uk/news/business-68671228).

One [assumption from these outages](https://thenewstack.io/why-we-shift-testing-left-a-software-dev-cycle-that-doesnt-scale/) is that software engineers aren’t testing their code enough. But this isn’t true. [The average developer spends 42% of their work week on maintenance](https://stripe.com/files/reports/the-developer-coefficient.pdf) — not innovating, not writing new code, just *fixing what’s already there. *So why are so many outages still happening?

One root cause that often underlines many outages is that [developers are testing code](https://thenewstack.io/platform-engineering-reduces-cognitive-load-and-raises-developer-productivity/) within an overly convoluted software architecture. It’s a towering Jenga stack where no one wants to risk adding another block for fear of collapse. And this is before a senior executive asks for AI to be implemented, despite no one remembering how the code was even built in the first place.

**How Software Erosion Happens**
Software is too complex today. Companies have to keep up with competitive market pressures, [asking developers to add new features](https://thenewstack.io/want-killer-features-foster-dev-user-communication/) to an already bloated codebase. No surprises here — the code becomes more complex and prone to breaking.

[Software erosion](https://thenewstack.io/bringing-back-the-joy-of-software-development/) typically unfolds like this: The developer is tasked with adding a new feature. This addition inevitably bloats the codebase. The developer implements a shortcut to meet tight deadlines, inadvertently increasing complexity. Later, when a manager requests an expansion of the product, the developer discovers that the earlier shortcut breaks the new update. The developer begins patching, which consumes excessive time. To expedite the fix, another shortcut is introduced — well-intentioned, perhaps, but soon they’re back at square one, and things start breaking again.
**We Need To Get Out of (Technical) Debt**
The larger the codebase grows, the more software erosion becomes a self-perpetuating cycle, where minor updates trigger a domino effect of issues. Simple quality-of-life improvements turn into a complex operation, fraught with risks of disrupting functionality across siloed teams. This fragility stops developers from innovating and iterating on a product and wastes valuable developer time. Instead of coming up with new ideas, they’re [consumed by technical debt](https://thenewstack.io/technical-debt-continues-to-mount-heres-how-to-solve-it/) and scrambling to fix bad code. When you factor in meetings, feedback sessions, and chats at the coffee machine, developers will likely spend less than half their week on value-added development.

The cycle of patching, mixed with the need to re-invent, encourages developers to look for ways to speed up their workflow. By doing this, developers have unfortunately become the wind itself, slowly eroding software.

**Breaking the Cycle and ‘Shifting Left’**
We’ve heard about “shifting left” for years, but the message hasn’t quite hit home. Many companies are still in the reactive habit of trying to bail out a sinking ship with a teaspoon. They throw more testing time at developers or bring in external QA teams. It looks busy — feels busy. But if new bugs pop up due to the “fixes” meant to squash bugs, that’s not a great use of time.

Companies need to incorporate quality into their product development process from the start. It’s much easier (and cheaper) to fix a house’s foundations before the walls are up. This means integrating QA into your development process from day one, starting at the design phase, not after the code is written.

To achieve this, you need to leverage multiple tools and perspectives. Run static code analysis as you write. Perform automated functional tests regularly. Understand your code duplication, dependency chains, and component interactions. It’s then that you clearly understand where the problems lie, even if they can’t be fixed overnight.

Failing that, it might be time to step back and look at the bigger picture. Is your architecture still fit for purpose? For many SME companies, a complete overhaul might be painful in the short term, but it could save them from a world of hurt. It’s trickier for larger organizations with years of legacy code.

Different team members have different priorities. Developers might resist additional analysis steps because they see them as extra work. It’s crucial to establish early on who’s responsible for what and why these steps are necessary. C-suites especially need to be convinced that without these fundamental QA processes, they, too, might soon be staring at a Crowdstrike-level nightmare.

Software erosion isn’t just a developer’s problem — it’s a company-wide issue. As software failures increasingly make headlines and threaten to tank businesses, organizations must prioritize a solid foundation for their software architecture. Unfortunately, too many teams are navigating systems they don’t fully understand. But, by aligning new features with the original design and understanding the intricacies of their systems, you reduce the need for workarounds. The result is a more stable system — everyone wins.

## Additional Coverage
[Take the ‘Shift Left’ Approach a Step Further by ‘Starting Left’]
[Why We Shift Testing Left: A Software Dev Cycle That Doesn’t Scale]
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)