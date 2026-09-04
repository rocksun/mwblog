**Michael Loewy, co-founder of the [Tide Foundation](https://tide.org/),** says the security industry was already losing ground to hackers *before* AI. Everything from a typo to a state actor could create a breach.

“Before AI even came into the developer consciousness, a developer or a platform owner needed to be perfect all the time — perfectly patched, free of errors, free of bugs — and an attacker only needed to be right once to get in,” [Loewy](https://www.linkedin.com/in/michaelloewy/) tells *The New Stack*. “It’s virtually impossible, which is why we’re seeing breaches in the news every day, and the biggest companies in the world getting breached. It could be one poorly written line of code, one misconfiguration, and then you’re done.”

AI has, of course, compounded the risks.

Loewy warns that vast amounts of inadequately reviewed, error-prone code are being produced just as advanced AI models are becoming highly skilled at discovering and exploiting vulnerabilities. Meanwhile, AI agents are creating software and performing sensitive, privileged actions.

Attackers gain access by getting past authentication and authorization. But what Loewy and co-founder [Ben Waters](https://www.linkedin.com/in/benjamin-d-waters/) are most worried about is the authority agents gain once inside.

Authority, as they define it, is the power to decide who or what can get into which system, who can access and decrypt which data, and who can authenticate, authorize and assign permissions. It lives in the systems we’re forced to unquestioningly trust in the form of admin credentials, root keys, identity providers, and service accounts. As Loewy says, “the problem is that it always lives somewhere, and someone always has access to it.”

Tide’s answer is a model it calls “emergent authority.” Under it, authority isn’t permanently held by any person, system, administrator, or AI. Instead, it is generated only when identity, policy, context, and intent align — before it disappears again. Loewy and Waters spoke exclusively with *The New Stack* about what that means for developers.

## **The flaws of the all-eggs, one-basket approach**

Most systems at most organizations keep application secrets, user credentials, and permissions in one place, then build more and more defenses around that central location, such as firewalls, key vaults, multi-factor authentication, and endpoint detection and response.

> “That root paradigm is flawed. Tide seeks to overcome that by using cryptography to compute authority in pieces so that it can’t be reassembled.”

“Even if your code is perfectly free of bugs, it’s sitting in someone else’s cloud on someone else’s operating system. There’s this whole suite of dependencies where the code and everything needs to be perfectly patched all the time, everywhere, and configured correctly for your security to be perfect,” Waters explains in our interview. “That root paradigm is flawed. Tide seeks to overcome that by using cryptography to compute authority in pieces so that it can’t be reassembled.”

In reality, just about every system is porous. Tide’s goal is that if and when you are breached, and the attacker has root on your server, there is nothing there for them to inherit, because the authority has been architecturally distributed elsewhere.

## **From IoT middleware to distributed authority by default**

Founded about a decade ago, Tide started as an Internet of Things analytics platform sitting between brands and consumers’ connected health devices, smart homes, and wearables. Its regulated customers demanded proof that no breach could leak highly sensitive information, trigger a GDPR fine, or destroy a reputation.

The infrastructure the team built to secure itself became the product, and, with it, a way out of the perpetual safety-speed tension between DevSecOps and product teams. At the pace of AI, this tension has only sharpened.

That infrastructure is now the developer product, [TideCloak](https://tide.org/tidecloak), which fits where your identity and access management system sits and handles authentication, authorization, end-to-end encryption, and governance on top of [Tide’s Cybersecurity Fabric](https://tide.org/howtideworks), so consequential authority remains out of everyone’s and everything’s reach.

The implementation is fully inspectable through Tide’s open-source [public GitHub repositories](https://github.com/tide-foundation). The accompanying white [paper on emergent authority](https://tide.org/whitepaper) was published using a chatbot to explain the underlying concepts and cryptography.

## **Let your coding agent do the integration**.

The part most likely to interest developers is how you’re meant to adopt it, not by reading those loads of documentation, but by handing the job to your coding agent.

“We needed this security apparatus or infrastructure that we’ve created to be something that can be seamlessly integrated into an existing project or best practice in a greenfield project, in a way where the developer doesn’t need to read loads of documentation,” Loewy says.

On Monday, Tide released [Raziel](https://tide.org/agent-plugins), an MCP server named after the archangel of secrets, that gives AI assistants deep knowledge of Tide authentication, threshold cryptography, end-to-end encryption, and governance. Point your agent at it, and it can recommend self-hosted versus managed hosting and generate verified playbooks for the integration. A [TideCloak quickstart](https://docs.tide.org/get-started/Tidecloak%20Quickstart) covers the greenfield case for those who’d rather start from a clean project.

Where most security tooling begins by looking for ways an attacker might get in, one of Raziel’s prompts instead maps out your blast radius.

> “We’ve said: they’re already in. Here’s what they’re going to find. Here’s where they can impersonate any user. Here’s where they can assign themselves access to whatever they want.”

“Where a typical cybersecurity scanner tries to find vulnerabilities- how someone’s going to get into your platform — we’ve started the opposite way,” Loewy explains. “We’ve said: they’re already in. Here’s what they’re going to find. Here’s where they can impersonate any user. Here’s where they can assign themselves access to whatever they want.”

[Tide has also partnered with a Lloyd’s of London underwriter](https://www.smh.com.au/technology/this-aussie-start-up-plans-to-make-medibank-style-breaches-impossible-20251104-p5n7ko.html), enabling organizations integrating TideCloak to obtain preferential cyber insurance terms. He says that “It’s a rare case of a security claim being backed by capital.”

## **Coordination at scale, without custody at scale**

The team likens their ambition to DNS. They hope that one day soon Tide will become infrastructure that nobody owns and everybody benefits from.

Tide is not just about breach prevention. To let an AI agent, a contractor, a partner, or a new vendor do anything consequential, you have to trust them with dangerous power. That trust requirement caps how far you can safely delegate or automate.

> “The point isn’t just safer systems. Once nobody has to hold dangerous power to get something done, you can delegate real responsibility to an agent, a contractor, or a five-person startup without creating a dangerous insider.”

“The point isn’t just safer systems. Once nobody has to hold dangerous power to get something done, you can delegate real responsibility to an agent, a contractor, or a five-person startup without creating a dangerous insider,” Loewy says. “That’s what lets developers ship with AI at full speed. It’s coordination at scale without custody at scale.”

If that holds up in practice, Tide’s biggest effect may not be on cybersecurity at all, but on the cost of delegation, and on how much a small team, working with agents, can safely be trusted to build.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)