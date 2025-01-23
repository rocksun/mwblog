# Root Out Vulnerabilities in GitHub as You Merge Code Changes
![Featued image for: Root Out Vulnerabilities in GitHub as You Merge Code Changes](https://cdn.thenewstack.io/media/2025/01/db8e76c9-code-1024x597.jpg)
For all the talk about the [need to “shift left”](https://thenewstack.io/shifting-left-is-now-mainstream-for-developers-or-is-it/) security to earlier in the software development life cycle, little has been done to make developers’ lives easier. That’s according to [James Wickett, ](https://www.linkedin.com/in/wickett/)CEO and co-founder of [DryRun Security](https://www.dryrun.security/).

“It’s actually shifted a lot of the burden over to developers, but it hasn’t really made their lives any better. … As an industry, we took these tools that were made for penetration testers and application security code reviewers, stuff that was meant to run for a long amount of time [then be sorted through.] We took those, forklifted them to the left …and then we made developers deal with the output from those tools,” he said.

“And those tools are too noisy, they’re too prone to too many what we call false positives. They don’t generate true results for developers, and they take too long to run. And so just those three facts alone, really kind of disqualify them from being developer-friendly, to be useful to developers. But that’s generally the state of most of the tools out there today.”

Austin, Texas-based DryRun Security applies AI and machine learning in GitHub to root out vulnerabilities as each code change is made. It has just introduced Natural Language Code Policies (NLCP) enabling users to define security policy in plain, conversational language for all their code bases without worrying about language or framework.

## Generating More Code Faster
Use of [AI coding assistants](https://thenewstack.io/how-generative-ai-coding-assistants-increase-developer-velocity/) such as GitHub Copilot is [growing rapidly](https://thenewstack.io/a-developer-health-check-on-github-copilot-and-ai-assistants/) — 76% of all respondents in a Stack Overflow survey are using or are planning to use them. That means developers are [generating ever more code faster](https://thenewstack.io/code-quality-becomes-even-more-vital-in-the-ai-era/).

“Generating more code is awesome, but that generates more of everything else that happens after the code — and there’s a lot down that line. From security testing, to unit testing, the overall governance, the amount of deployments that happen, the number of dependencies that get pulled in.” said [Martin Reynolds](https://www.linkedin.com/in/martinreynolds/), field CTO, speaking of Harness’s [State of Software Delivery 2025](https://www.harness.io/state-of-software-delivery) report.

More control mechanisms added for security in the development process add to build times, making developers reluctant to use them or to commit code changes less frequently, according to DryRun.

First off, DryRun aims to help developers find problems fast. It maintains that a process called contextual security analysis run in GitHub takes only 10 seconds.

Contextual security analysis uses context data gathered as developers are writing code (codepath, functions, author, language) to make contextually aware assertions in near real time. It’s designed for modern applications that are distributed, microservices-based and rely heavily on APIs and third-party components.

“That process looks across five key factors for any code change… We use the acronym SLIDE to think about contextual security analysis: surface, language, intent, design and environment, and we gather a bunch of data around all those elements, and we build out this contextual window for that particular code change, Wickett explained.

And using Natural Language Code Policies you’re able to ask questions in plain English about changes and the risk involved.

## Not Just Matching Patterns
Most security tools use static application security testing (SAST) or software composition analysis (SCA) — just two data points — when there is a wealth of [other data that can inform the risk](https://www.linkedin.com/pulse/unpacking-contextual-security-analysis-dryrun-securitys-amit-jhvze/?trackingId=QLk5Bl8gS4%2BwvPowV1wwsQ%3D%3D) of a code change, cofounder Ken Johnson explains in a LinkedIn article.

“All those previous tools that we that have kind of built up in our industry, they’re all pattern-based, and really, we’ve been doing the same approach to code analysis for, I don’t know, 20-25, years plus,” Wickett said.

“They’re all regex and pattern-based, calling a syntax tree. And that’s generally the approach that every single tool, even kind of the more modern tools do. That only works if you know what patterns you want to look for ahead of time, and it also puts a lot of burden on your developers, or AppSec people, to write a bunch of rules and to learn, like a whole another domain-specific language where they have to express those rules for different [programming languages](https://thenewstack.io/programming-languages/), whether it’s Java or Python or whatever.”

DryRun offers a series of analyzers for whether authentication/authorization are used correctly, whether secrets or sensitive information are exposed and more.

“We have our own policies [that] we run out of the box that are just sort of work for 80 to 90% of what someone would need. And then, generally, our customers find that they have questions or that they have particular code policies around like authorization issues, encryption settings, and changes for third-party vendors they’re working with. So that’s how people extend the product, using natural language questions — stuff like, is this code change affecting our password reset flows? Is this code change modifying encryption? Is this code change changing the way we do authorization at our company. They can fill in more details that’s relevant to them,” Wickett said.

## Applying LLMs to Provide Relevant Context
The 10-person startup launched in 2023 and just announced $8.7 million in seed funding. Wickett and Johnson are veterans of the application security space and regularly present webinars and conferences, most recently about [incorporating large language models (LLMs) in AppSec](https://www.dryrun.security/webinars/hands-on-with-ai-using-llms-to-detect-idor-and-auth-flaws).

They’re learning about AI like everyone else, and have documented how they’ve [incorporated LLMs](https://www.dryrun.security/blog/one-year-of-using-llms-for-application-security-what-we-learned) into their work.

“Some of the things that people have used LLMs and AI for is just taking a block of code and throwing it over to the AI system and seeing what it says. We have our own knowledge base that we have based on all of our languages and frameworks. We also have discovered our unique way to do code inquiry, which is all LLM-based. So we’re using LLMs at every layer as we’re gathering all this context and are able to answer questions.

“But … we’re able to do it fast, accurately, giving developers real guidance …we’re not pointing them off to some generic place on the web that says, ‘Hey, look, you have cross-site scripting, or you have IDOR (insecure direct object references) or some other vulnerability.’ We’re actually explaining the problem with their own code, with their own variables and their functions and the calls that they’re making right there. So it’s super relevant to developers.” Wickett said.

He maintains that AI and LLMs are able to resolve problems you could never have figured out in the traditional SAST approaches.

“This is particularly true, and we found this for almost all of our customers around like, authorization, where they release new endpoints, but they don’t have authorization applied correctly. Developers accidentally put the wrong roles or the wrong authorization components on different endpoints, and that’s a real security concern that traditional SAST tools just can’t figure out because of the way they’re just trying to match patterns.”

DryRun is an app that works inside GitHub cooperatively with Copilot. A version for GitLab is in the works. Wickett maintains that modern IDEs are increasingly weeding out a lot of simple errors, but errors will only grow more complex, reinforcing the idea that developers need fast, contextually relevant help to address them.

“The GitHub integration ensures that our developers get precise and instant feedback directly in their workflow, enabling them to fix security issues without skipping a beat. The tool has not only helped us catch risks like hard-coded credentials early but has also fostered a culture of security among our developers. DryRun Security is an indispensable part of our AppSec toolkit,” said Gary Gonzalez, CTO at PlanetArt.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)