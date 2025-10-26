Vibe coding helps people bring ideas to life quickly. It gives them the courage to create when inspiration strikes, especially when they don’t know where to begin. The ability to move a concept from the first line of code to a fully-fledged application in production within days is powerful for developers. But in the rush to bring an idea to fruition, security can get lost in the shuffle.

[Previously](https://thenewstack.io/vibe-coding-when-ai-writes-the-code-who-secures-it/), I explored why AI-generated code is inherently insecure and how its inclusion in projects can lead to a slew of security concerns. My biggest takeaway was that poorly crafted and vulnerable code requires human review and correction before being pushed to production.

With that understanding in mind, how can organizations or individuals working with AI-generated code systematically identify and mitigate security risks before they lead to a breach? By applying threat models like [STRIDE](https://www.practical-devsecops.com/what-is-stride-threat-model/?srsltid=AfmBOopCqyD8P_nGRmdesaieyMdRYsZa9rZg9vY3-7zctR9zxuaTcUFO) and checklists like the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/), vibe coders, developers and maintainers can continue to reap the benefits of AI-generated code without compromising on security.

I think about it like “Star Trek: The Next Generation.” In one episode, the Enterprise’s autopilot was unable to navigate a particularly congested asteroid field. Captain Picard was forced to take manual control to save the ship and its crew. AI-generated code is like our autopilot. It accelerates progress, but when security storms hit, humans must take the helm.

## Review AI-Generated Code Through a Threat-Minded Lens

The STRIDE threat model, developed by Microsoft and standing for spoofing, tampering, repudiation, information disclosure and denial of service, is a cybersecurity framework for proactively identifying potential security threats. It provides a structured guide to assess and map the threats unique to AI-generated code, some of which I’ve outlined below:

* **Spoofing**
  + AI-generated code can be submitted under stolen or false (spoofed) identities, which makes attribution and accountability challenging.
  + Authentication logic may be weak or missing altogether in AI-generated code, as seen with Jack Dorsey’s [Bitchat](https://www.theregister.com/2025/07/08/jack_dorsey_debuts_bitchat/).
* **Tampering**
  + AI-generated code can introduce insecure default configurations.
  + AI-generated code may introduce insecure initial access vectors that attackers can exploit, such as inadvertent misconfigurations placed by unknowing contributors.
* **Repudiation**
  + A lack of code provenance or code signing creates accountability gaps. For instance, who is responsible for flaws introduced by AI-generated code?
* **Information disclosure**
  + AI-generated code may unintentionally embed secrets, APIs or credentials from prompts or data sets in its output, leaking sensitive information.
* **Denial of service**
  + Lengthy code contributions or an excessive number of contributions may overwhelm and overburden maintainers, essentially creating a “review DoS.”
  + Lengthy code may also overwhelm the context windows of code review tools or IDEs, allowing risks to slip through the review process.
* **Elevation of privilege**
  + Similar to the lack of authentication, AI-generated code often omits proper authorization checks, allowing attackers to escalate privileges with minimal guardrails.
  + Logic flaws in AI-generated code can enable attackers to elevate privileges within applications.

By mapping security concerns to real-world coding scenarios, STRIDE can help guide users toward informed and practical defenses when using AI-generated code.

## Knowledge is Power, Diligence is Key

The OWASP GenAI Security Project offers a [Top 10 list of LLM and GenAI](https://www.sysdig.com/blog/owasp-top-10-for-llms) risks for LLM-based systems. However, many of the risks map directly to issues associated with AI-generated code contributions.

Below are some of the expected risks of AI-generated code output, inspired by the OWASP Top 10 for LLMs:

1. **Injection flaws**: AI-generated code may include unresolved SQL, command or template injection vulnerabilities or misconfigurations. Just as prompt injection is the weaponization of untrusted or malicious prompts, insecure code can be weaponized when merged into existing software.
2. **Lack of input validation**: AI-generated code often takes the path of least resistance, and failing to validate or sanitize it can increase the attack surface and lead to inadvertent sensitive information leaks.
3. **Hardcoded secrets**: AI-generated code may not sanitize API keys, passwords or tokens, leaving sensitive information exposed.
4. **Poor error handling**: AI-generated code may include errors that are not identified (silent failures) or expose debug information to users, rather than logging it, which can be advantageous to attackers.
5. **Insecure defaults**: Disabled SSL checks or ignored error handling may [cascade into software supply chain vulnerabilities](https://thenewstack.io/get-a-handle-on-software-supply-chain-security-with-lfx/).
6. **Insecure dependencies**: AI-generated code may include unsafe or malicious libraries and/or packages, which can in turn expand the attack surface.
7. **Unapproved components**: AI-generated code may introduce unverified or third-party projects or connections. Similar to adding insecure dependencies, this could introduce vulnerabilities and increase the risk of supply chain attacks.
8. **Code provenance**: Unreviewed AI-generated code merged into a project may be a poisoned commit, similar to poisoning training data.
9. **Overly permissive code**: AI-generated code may disregard the principle of least privilege and establish insecure defaults, [resulting in poor Kubernetes and cloud configurations](https://thenewstack.io/kubescape-3-0-the-result-of-lessons-learned-with-ebpf-for-security/) or inadequate identity and access management roles, which can lead to excessive privileges within an application.
10. **Complex code**: AI-generated code may be too lengthy, confusing and unreadable for humans, making review difficult and increasing the likelihood that applications or projects are compromised or poisoned. This is, in part, a human process risk that seriously affects security posture.
11. **Misinformation**: AI-generated code may use outdated practices or inaccurately write code comments, which could confuse reviewers and allow risks to otherwise slip through the cracks.
12. **Review overload**: An increase in contributions and excessive review cycles, driven by AI-generated code, leads to maintainer burnout. This is another human-born risk that affects security.

Treating this list as a code review companion can help developers catch the most frequent and dangerous AI-generated code failures.

## The Age of AI Still Needs a Human in the Loop

Securing your vibe-coded applications is like dancing the tango: It’s fast-paced and requires both precision and control. It demands a balance between speed and safety, and it begins with the way you review and maintain code. Apply threat modeling, such as STRIDE, early in the ideation, creation or initial review stage, not after the code has been shipped. The goal is to expose risks before they become vulnerabilities. However, there’s no need to turn threat modeling into a complex cycle, as even a quick check can expose glaring risks.

Beyond threat modeling, you can automate safety guardrails by [embedding dependency scanners and CI/CD pipeline security checks](https://thenewstack.io/use-these-devops-pipelines-to-cut-automation-tool-costs/) into your workflows and blocking hardcoded secrets with pre-commit hooks.

Also, before any new code hits production, you should use AI to review AI. Though it may sound ironic, AI-powered linters or code review tools can identify common AI coding mistakes, especially when paired with traditional [static analysis tools and code](https://thenewstack.io/level-up-your-software-quality-with-static-code-analysis/) scanners. However, even after the automated scans are complete, a human must serve as the ultimate gatekeeper for making informed judgment calls and providing final approval.

Here’s the hardest pill to swallow: Security doesn’t stop even after the code is reviewed, approved and committed. You must ensure accountability and provenance by maintaining metadata for AI-assisted contributions when possible to support future audits. Include clear comments that denote what was written by AI, which models were used and when the code was generated.

Lastly, talk about it. None of this works without awareness. New coders may lack formal security training, and seasoned developers should advocate for secure AI code education. It’s essential to highlight not only the value of vibe coding, but also where it might fall short. As with most things in life, knowledge is power.

## Securing the New Era of Coding

AI isn’t going away. The ability to quickly pivot from idea to running code in days is transformative. But without structured review, threat modeling and guardrails, vibe coding can just as easily accelerate compromise as it does innovation.

My motto? “Use the tool; trust the human.” By using security frameworks and checklists like STRIDE and OWASP and adapting our review practices to meet the evolving needs, we can ensure that AI-driven coding remains an accelerator of creativity, not a liability to security.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/08/dfbfb486-i5jnccyk-nxw7aqbydo31zeacz696mlu70ufdwdl9fo-scaled-600x600.jpeg)

Crystal Morin is a senior cybersecurity strategist at Sysdig. She translates complex security concepts and cutting-edge research into clear, actionable guidance for leaders and practitioners alike, helping organizations defend against modern threats. Previously, Crystal served as a linguist and intelligence...

Read more from Crystal Morin](https://thenewstack.io/author/crystal-morin/)