**Attackers aren’t always the reason for DNS failures** — they can often be something much more routine.

For example, the failure could result from regular domain management operations at the registrar level, as one [study](https://dl.acm.org/doi/10.1145/3419394.3423623) points out.

A live example of DNS failure was the [Cloudflare 1.1.1.1 2025 DNS global outage](https://blog.cloudflare.com/cloudflare-1-1-1-1-incident-on-july-14-2025/) last summer that lasted for 62 minutes. It occurred not because of a cyberattack, but a misconfiguration in their systems.

![](https://cdn.thenewstack.io/media/2026/07/8cfe6b9a-anthony-eden-dnsimple.jpg)

Anthony Eden, founder and CEO of DNSimple

Beyond routing traffic, domains carry business value, intellectual property, and brand identity for enterprises, which is why those enterprises spend large sums on them.

Those domains breathe inside the vendor dashboard — whether a registrar’s or a DNS host — and multiple stakeholders manage them manually, often leaving no record of who changed what.

When asked about the management gap, [Anthony Eden](https://www.linkedin.com/in/aeden/), founder and CEO of [DNSimple](https://dnsimple.com/) — a developer-focused domain management automation and DNS hosting company — tells *The New Stack*, “Most engineers who are working at companies are already required to use tools like Terraform or Ansible to control all of their other services. So that means deploying servers and managing storage instances, things like that.

“And I think DNS and domain management need to be treated the same way.”

## **Domain management as code**

According to Eden, domains deserve the same operational rigor an enterprise applies to its servers, cloud infrastructure, and deployments. In enterprises, Terraform already provisions compute and storage as Infrastructure as Code (IaC). DNS belongs in that same category, as Eden reveals that DNSimple, as a DNS provider, ships a Terraform provider built on its API, where domains and DNS exist as code in configuration files for maintenance, automation, and version control.

“Wherever you store all of that, whether GitHub or GitLab, then you have a repeatable historical reference of all of the changes that any of your team members made”. Unlike a static dashboard, Terraform ensures stakeholders agree on changes and enables corrections if anything drifts. Eden confirms, “I want my infrastructure to look like these configuration files. I want to be configured this way, and it constantly runs to ensure that your infrastructure looks like that.

Ask Eden what mature domain management looks like, and he shares three best practices.

**Multiple user access**: He explains that having two or more users manage domains can prevent downtime if one person loses access, while the other can restore the settings.

**Different email addresses**: Eden explains that a clever strategy is to use a non-domain recovery email. “If the account has issues and the zones get turned off, then you don’t lose access completely to your email at the same time,” Eden adds, suggesting seamless account reactivation.

**Secondary DNS:** Eden explains, “As you get into larger configurations, more important domains that can’t go down, you have tooling like secondary DNS which allows you to put the zone on different providers.” A secondary DNS provider holds a synchronized replica of the primary zone on separate infrastructure.

This means if the primary provider goes down, resolvers can still reach the secondary provider, and the domain keeps working. Eden describes that a provider hosts many tenants on a shared infrastructure, so an attack targeting either the provider or its tenant can take other domains down as well. Eden shares the solution with *The New Stack*: “One provider, for example, has a denial of service attack that is large enough to affect that entire infrastructure, you have a second provider that hopefully can withstand that same denial of service attack.” This means that domains with secondary DNS—replicated zones across two providers are less likely to witness downtime.

## **DNSimple API does the heavy lifting**

Engineers have been working with APIs to communicate with web services—but use vendor dashboard tabs to manage domains. That’s because enterprises follow the reverse practice: someone opens a dashboard, edits a record, and closes the tab. No request. No approver. No history of the change.

The DNSimple API for DNS and domain management transforms every domain operation into a JSON-encoded HTTP request, something which a pipeline can perform, a reviewer can approve, and a repository can record.

Eden favors the REST API-driven approach for domain and DNS management automation. Through the DNSimple Terraform provider, a DNS change stops being an edit and becomes a reviewable request which is proposed, approved, and recorded like any other infrastructure change, with a version history behind it.

Access control is where domain management becomes serious for larger portfolios. While API requests help servers understand what the developer wants, API tokens specify what the developer has access to.

DNSimple offers account, user, and scoped API tokens–A deployed pipeline gets a token for a specific zone and nothing more. Revoke it and nothing else breaks.

Eden tells *The New Stack*, “If a domain status had changed, it had gone from registered to expiring. You could call the API on a scheduled basis once a day and could check that yourself.” He goes on to explain the world of webhooks: “Webhooks provide a push mechanism. You register a URL, and we will send events essentially whenever they happen in our system so that you can react to those events.”

Instead of waiting for the user to notice, webhooks chase the user when something changes, whether a domain renews or records update. According to Eden, users can listen to state changes through webhooks.

Eden explains, “You can listen to when your domain is entering into an expired phase if you don’t have it autorenewed, and then your system can act automatically.” Webhooks don’t miss out on certificates either. Eden adds, “You could listen to see when a certificate is ready to be installed.”

He explained that once the certificate authority issues a certificate, the webhook fires, “Hey, this certificate is available”. Eden shares a tip with *The New Stack:* “You can then call the API to pull down the certificate and install it on your server all automatically”.

For day-to-day work, Eden’s answer is unambiguous: “CLI, 100%”. The CLI keeps the work already where it is. Writing APIs is to build requests and parse JSON. The CLI is the API without raw HTTP; each request becomes a command, where the tool writes it on behalf of the user.

## **DNSimple CLI reduces context switching**

DNSimple CLI for DNS and domain management enables users to perform routine checks and manage domains, DNS records, and certificates from the command line instead of making manual API requests. “Our CLI provides an interface on top of the API”, Eden shares with *The New Stack. “*It essentially does almost all the endpoints that our API provides except in a really nice command-line interface.”

He shares an example with *The New Stack:* “I can do something like dnsimple domains list, and it’ll list all of my domains”–in tabular format for reading, or JSON for scripts. It’s like automating at a distance without leaving your desk.

Eden adds, “You could write a script that just says do step C, step D, and it just calls out to those CLI tools.” This means that the DNSimple API matches with the hosting CLI, deployment pipelines, and whatever is called upon.

A dashboard cannot be called from a script; that’s the difference between routine manual management and CLI-based automation. “They can just keep working right in the same environment, which is nice because it avoids the context switching necessary to open a web browser, log in, go to the web interface, and so on and so forth”, Eden adds.

Eden puts it plainly, “API is like plumbing….Anybody can build on top of it.” He shares, “DNSimple has libraries for nine different languages. Anybody could hook in and build an entire tool chain on top of it. And we actually have customers that have done that.”

Customers of customers integrated through API for transparent domain management in their home environment. Eden shares the truth with *The New Stack,* “It allows other folks to build sort of vertical tooling or very specific niche tooling without having to expose all the complexities of the underlying DNS and domain management.”

## **Agentic AI in the CLI**

AI agents reach DNSimple the same way a script does. Eden recalls Claude agentic AI and explains how the AI tool can run through the CLI. He shares a use case with *The New Stack* in which users can deploy multiple AI agents:“Spin up a project and say—Hey, I need a domain for this project. Register it through DNSimple and configure it”. A simple prompt that does the work.

He shares another example*: “*You wanted to send yourself a monthly report with all of your domains and when they expire and where they’re pointing”. Claude will go through the CLI and provide all the relevant information.

Production is where Eden gets careful, saying, “if you’re going to be using tools that are variable in their output, which essentially any sort of generative AI tool is going to be, you need those safety nets in place.”

Eden considers API tokens, whether user, account, or scoped, as an access control mechanism for AI agents. “You could give it access to only one domain in your portfolio of domains or only a few domains in your portfolio”, he explains. The credential sets the boundary, not the AI agent’s judgment. No prompt, no matter how smartly phrased, cannot jail-break the token’s order.

## **Certificates snub domain vulnerabilities**

Eden reveals that all DNSimple tools are exposed via the API and CLI, enabling users to order and manage certificates.

The timing matters because in April 2025, [CA/Browser Forum](https://postquantum.com/security-pqc/sc081v3-47day-certificate/) passed Ballot SC-081v3, cutting maximum TLS certificate validity from 398 days to 100 days in March 2027, and to 47 days by March 2029. Eden says, “When you get down to that point, it’s going to be very difficult to manually rotate certificates every 90 days. So, some sort of automation is necessary regardless of who you use.”

That’s roughly 4-8 rotations per year, beyond what manual rotation can keep up with. Eden recommends Let’s Encrypt certificates. As a DNS provider, DNSimple handles the validation step: “We will put the necessary tokens into the DNS for you. We will wait until Let’s Encrypt has issued the certificate”, he explains. Once issued, relevant webhooks are sent to users. He reveals that renewals start 7-15 days before expiry.

Wildcard certificates make automation unavoidable; they cover every domain and its subdomains beneath it, including those that don’t exist yet. Eden recommends, “Wildcard certificates must use DNS for verification.” There’s no server-side plugin to do the same.

## **Why DNSimple?**

DNSimple is built by developers for fellow developers, software engineers, domain operators, and enterprises. Whether developers provide domain-related services to clients, restaurants own domains to take online orders, or Airbnb properties need domains for direct bookings—DNSimple supports them through a usable interface, workable API, easy-to-use CLI, honest pricing, and customer support.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/07/e86f3866-cropped-874219b8-bf2b0e02-00b9-4a36-958c-b76f1796dfe5-600x600.jpeg)

Venus Kohli is an electronics and telecommunications engineer turned technical content writer. She covers everything related to electronics, IT, and her favorite, quantum physics, for the engineers and decision-makers who build the technology. During college, her group project resulted in...

Read more from Venus Kohli](https://thenewstack.io/author/venus-kohli/)