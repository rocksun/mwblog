**Every enterprise runs on open source**, but keeping it secure has become significantly harder. Frontier AI models are uncovering vulnerabilities faster than maintainers can comfortably process them, while giving attackers many of the same capabilities. The result is a growing backlog of fixes that organizations are expected to evaluate and deploy ever more quickly.

That shift is forcing enterprises to look beyond the software itself. The question is no longer simply which open-source projects to trust, but who is maintaining them — and how quickly they can respond when new flaws emerge.

In that environment, first-party support from the maintainers of an open-source project is becoming less an operational convenience and more a critical part of enterprise risk management.

## **AI has turned a trickle into a flood**

Open source remains the foundation of modern software development. Virtually every enterprise application depends on hundreds – or thousands – of open source components. The challenge isn’t adopting open source; it’s keeping those dependencies secure when AI is finding flaws faster than organizations can reasonably process them.

[Ryan Morgan](https://www.linkedin.com/in/ryanmorgan2/), head of Spring R&D at Broadcom, tells *The New Stack* that the industry has experienced a fundamental shift.

“Historically, the trickle of a security vulnerability in this library, or that library, is something that was very manageable,” Morgan says. “What’s happened with frontier AI is that what was a trickle has now turned into a tidal wave.”

> “What’s happened with frontier AI is that what was a trickle has now turned into a tidal wave.”

Organizations are now examining not only whether vulnerabilities exist, but also whether the projects they depend on have the resources to respond quickly.

“I don’t want to say that the free lunch is over,” Morgan says, “But there’s this temporary time where everyone is taking a closer look at what dependencies they take, the health of those communities, and really trying to future-proof what they’re doing.”

[Michael Minella](https://www.linkedin.com/in/michaelminella/), director of Open Source Spring R&D at Broadcom, has watched that shift play out inside the Spring portfolio. Historically, the team received around seven security reports a month. Once frontier AI models entered the picture, those numbers climbed sharply.

“In March, we saw 55 reports coming from the community,” Minella says. “In April, that went to 112. April is also when we finally got access to those frontier models and started doing internal scanning, and our internal scans gave us another 370 internal reports.”

That isn’t simply more work for maintainers; it’s forcing teams to rethink how software is triaged, validated, and released.

## **Finding bugs is no longer the hard part**

If AI has changed one thing, it’s where the bottleneck sits. Both Morgan and Minella say today’s models are remarkably good at uncovering vulnerabilities and even generating proof-of-concept exploits. Producing reliable fixes that won’t break production systems remains far more difficult.

“What we’ve also seen is [AI is] not perfect yet at being able to automatically patch or create fixes for you,” Morgan says, adding that Broadcom still relies on experienced engineers to write and validate every Spring security patch before release.

“For our most recent set of CVE patches, every single one of them was handwritten,” Morgan says. “AI helped identify and validate the issues, but the actual code itself was written directly by humans because we want to be able to move fast, but we can’t do so in a reckless way that’s going to create regressions or bigger problems down the road.”

That distinction becomes particularly important for frameworks like Spring, where even small changes can affect millions of downstream applications.

## **Why first-party support has an edge**

One advantage first-party maintainers have is that they’re usually the first to hear about newly discovered vulnerabilities. Security researchers report flaws directly to the project team, giving maintainers time to investigate, develop a fix, and validate it before the details become public. That head start is becoming increasingly valuable as the gap between disclosure and exploitation continues to shrink.

> “We are the source of truth with regard to security vulnerabilities.”

“We are the source of truth with regard to security vulnerabilities,” Minella says. “If a security researcher is looking into Spring and they find a vulnerability, the Spring team at Broadcom is the one they report it to.”

That gives first-party maintainers a significant head start. “We build the patch in private. We work with them… before anybody else knows,” Minella added. “Every other third party, their clock starts to get their patch out when we’ve already announced we fixed something.”

When some vulnerabilities are exploited within hours of disclosure, those days can matter.

Maintainers also understand the long-term roadmap for their projects [in a way that third parties cannot](https://go-vmware.broadcom.com/the-fallacy-of-third-party-support). Fixes need to solve today’s problem without creating tomorrow’s compatibility headache, particularly for enterprise customers running applications expected to remain in production for years.

## **Keeping pace with the threat landscape**

The volume of AI-generated findings has also forced maintainers to rethink their own development processes.

Historically, releasing updates across Spring’s portfolio of more than 60 interconnected projects could take around two weeks.

“In a world where vulnerabilities are being exploited in less than a day, a two-week release cycle is outdated,” Minella says.

The team is rebuilding the release process to ship coordinated updates across the entire Spring portfolio in a single day, giving customers a predictable cadence that’s easier to consume.

> “In a world where vulnerabilities are being exploited in less than a day, a two-week release cycle is outdated.”

That matters because every release creates work for customers. Security updates need to arrive quickly, but they also need to be deployable in ways organizations can realistically use.

Morgan says enterprise patching strategies are changing just as rapidly. “The biggest change that I’ve seen is people have gotten away from trying to analyze piece by piece,” he says. “They’re just patching and getting up to the latest across the board.”

That shift is forcing organizations to rethink their own deployment pipelines. Delivering patches faster only helps if customers can validate and deploy them just as quickly.

## **Open source isn’t broken**

Neither Morgan nor Minella sees AI as an existential threat to open source. If anything, they expect the current wave of vulnerability discovery to leave the ecosystem in a stronger position.

AI is exposing weaknesses that previously went unnoticed while encouraging maintainers to build security scanning earlier into the development lifecycle and collaborate more closely across projects. Commercial providers, meanwhile, are increasingly expected to take responsibility for proactively scanning and maintaining the software they steward rather than leaving that burden to customers.

> As AI accelerates vulnerability discovery, enterprises need fixes that are not only fast but also accurate, tested, and unlikely to break production systems.

“I do think we’re already seeing today that there’s going to be an expectation that, as providers of commercial open source, you’re spending the time and the resources to do scanning of your own software,” Morgan says.

Community-led development isn’t going anywhere, but the demands placed on the people maintaining critical open source projects are changing rapidly.

As AI accelerates vulnerability discovery, enterprises need fixes that are not only fast but also accurate, tested, and unlikely to break production systems. That’s increasingly where support from the teams actually building the open source software can make the biggest difference.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/05/1cf43e50-cropped-bc46c9c3-headshot-disrupt-600x600.png)

Carly Page is a technology journalist covering cybersecurity, digital policy, and emerging tech, with more than 15 years’ experience reporting on how systems break and who gets burned when they do. She previously served as senior cybersecurity reporter at TechCrunch,...

Read more from Carly Page](https://thenewstack.io/author/carly-page/)