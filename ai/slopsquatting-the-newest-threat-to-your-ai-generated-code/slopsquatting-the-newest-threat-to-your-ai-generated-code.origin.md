# Slopsquatting: The Newest Threat to Your AI-Generated Code
![Featued image for: Slopsquatting: The Newest Threat to Your AI-Generated Code](https://cdn.thenewstack.io/media/2025/04/5ff2de77-toa-heftiba-ghlljhftdgw-unsplash-1-1024x683.jpg)
Software developers are increasingly using AI to create code, a trend that’s not surprising given the increasing demands put on them to build products and get them out the door faster.

A study last year by [GitHub](https://github.com/) found that [97% of programmers surveyed](https://github.blog/news-insights/research/survey-ai-wave-grows/) said they are using AI coding tools at some point. A similar survey by [Stack Overflow](https://stackoverflow.com/questions) in 2024 found that 76% of 65,437 developers said they were either [using or planning to use such tools](https://survey.stackoverflow.co/2024/). The list of reasons is growing, ranging from improved productivity and enhanced code quality to faster [debugging](https://thenewstack.io/master-the-art-of-python-debugging-with-these-tips/) to greater consistency across teams.

However, due to AI’s double-edged sword nature, [there are risks](https://www.legitsecurity.com/aspm-knowledge-base/ai-code-generation-benefits-and-risks), including code reliability, security vulnerabilities, and [technical debt](https://thenewstack.io/technical-debt-continues-to-mount-heres-how-to-solve-it/) that could slow down the process and drive more costs, according to [Legit Security](https://www.legitsecurity.com/), an [application security posture management](https://thenewstack.io/consolidate-with-application-posture-security-management/) (ASPM) company.

Another risk is that [large language models](https://thenewstack.io/top-5-large-language-models-and-how-to-use-them-effectively/) (LLMs), as they’ve been known to do since [OpenAI](https://openai.com/) first released [ChatGPT](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/) in 2022, will create “[hallucinations](https://thenewstack.io/ai-agentic-evaluation-tools-help-devs-fight-hallucinations/),” wrong or misleading outputs. For most of the world, that means a response to a prompt might misstate financial numbers, include incorrect information in an essay, or — in one famous case — [make up court citations](https://www.theguardian.com/technology/2023/jun/23/two-us-lawyers-fined-submitting-fake-court-citations-chatgpt) that a lawyer used in a court filing.

For developers, it could mean generating references to software libraries, modules, or other code packages that don’t actually exist. It’s not a new phenomenon. [Security firms](https://vulcan.io/blog/ai-hallucinations-package-risk/) and analysts have known about it for a while.

## Watch Out for Slopsquatting
That said, it’s being raised again, thanks to a focus put on a supply-chain attack that could be launched in code repositories by exploiting these hallucinations that has a colorful name — “[slopsquatting](https://fosstodon.org/@sethmlarson/114328275927451797)” — and a recent [study](https://arxiv.org/pdf/2406.10279) by researchers at three universities that outlines how it can be done.

The name is a play on the well-known cyberthreat “typosquatting,” where bad actors register malicious domains with names that are very similar to legitimate websites in the hope that a developer will make a spelling mistake and inadvertently end up on the fake site.

In the case of slopsquatting, a threat actor may create a malicious package that uses the name of an LLM-created non-existent library and place it for download on a popular code repository like GitHub, [Python Package Index](https://pypi.org/) (PyPI), or [npm](https://www.npmjs.com/), in hopes that a programmer will grab it for their work.

[IDC](https://www.idc.com/) analysts [wrote about such threats](https://blogs.idc.com/2024/04/22/package-hallucination-the-latest-greatest-software-supply-chain-security-threat/) last year, noting that “package hallucination creates novel opportunities for threat actors to plant malicious code within software supply chains and prey on developers who use generative AI to write code.”
## Research in the ‘Nascent Stages’
The researchers from the University of Texas, San Antonio, the University of Oklahoma, and Virginia Tech went deeper, arguing that most research on AI hallucinations has focused on those in natural language generation and prediction jobs like summarization and machine translation. Studies of them in [code generation](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/) are “still in the nascent stages,” they wrote.

For their work on package hallucinations in [Python](https://thenewstack.io/python/) and [JavaScript](https://thenewstack.io/javascript/) code, the researchers tested 16 popular code generation models like ChatGPT-4, [DeepSeek](https://thenewstack.io/deep-dive-into-deepseek-r1-how-it-works-and-what-it-can-do/), [CodeLlama](https://ollama.com/library/codellama), [Claude](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/), [Mistral](https://mistral.ai/), and [OpenChat](https://oc.app/) and used two prompt datasets to get a feel for the scope of the problem. The LLMs generated 576,000 Python and JavaScript code samples, of which 19.7% of the recommended packages didn’t exist.

So, would the models repeat the hallucinations in the same package? Using a collection of 500 prompts that had created package hallucinations, they repeated the queries 10 times for each prompt and found that 43% of the package hallucinations were repeated in all 10 queries, and 58% of the time, a package was repeated more than once in 10 iterations.

The test results show “that a majority of hallucinations are not simply random errors, but a repeatable phenomenon that persists across multiple iterations,” the researchers wrote. “This is significant because a persistent hallucination is more valuable for malicious actors looking to exploit this vulnerability and makes the hallucination attack vector a more viable threat.”

Another interesting note from the study was that most models were able to detect their own hallucinations more than 75% of the time, with the researchers writing that it indicated that “these models have an implicit understanding of their own generative patterns that could be leveraged for self-improvement is an important finding for developing mitigation strategies.”

## The AI Challenge for Developers
The study and the publicity that the threat of slopsquatting is getting is an important reminder for developers about the care they need to take when using AI to generate code. [Sonatype](https://www.sonatype.com/) is one of a growing number of vendors in a [software composition analysis](https://thenewstack.io/software-composition-analysis-and-sboms-a-united-defense/) (SCA) market that is expected to grow from $328.84 million last year to almost [$1.7 billion by 2033](https://straitsresearch.com/report/software-composition-analysis-market). SCA tools automate the process of identifying and managing open source components.

[Mitchell Johnson](https://www.linkedin.com/in/mitchell-johnson-124562/), chief product development officer at Sonatype, told The New Stack that the use of AI in software development rings back to when open source was new — “kind of outlaw tech” — that developers were warned against. Now most software includes open source elements.
“AI is kind of where open source was, say, 20, 25 years ago, where organizations are just dipping their toes in it,” Johnson said. “But in reality, developers are always ahead of the curve because we’re pushed as developers to be more productive, to be faster, to ship faster, to ship higher quality. Faster, better, cheaper drives us. Unfortunately, the bad actors understand that and they’re really smart.”

A problem is that AI eases some of the pressure on programmers who are told to go fast, and often, security is put to the side. In asking vice presidents of engineering and development managers about goals for the year, “you just don’t hear ‘security’ very often,” he said. “You hear, ‘Deliver this thing on time, deliver this thing on budget, deliver this innovation, take this expense out,’ but you just don’t hear security. It’s not to say developers don’t think about it. We’re seeing it more and more, but on the whole, no. The innovation and the speed is happening too fast.”

[Casey Ellis](https://www.linkedin.com/in/caseyjohnellis/), founder of [Bugcrowd](https://www.bugcrowd.com/), told The New Stack that developers’ incentive “is to ‘make the thing work,’ as opposed to ‘making sure the thing doesn’t do all of the things it potentially shouldn’t.’ When this misalignment exists, issues like this exist, and [when] you add an accelerating function like AI-generated code, attacks like slopsquatting are the natural byproduct.”
## The Need To Validate
Even with the help that AI delivers, the onus is still on developers to validate their code to ensure there’s nothing malicious in it. Johnson compared it to an engineer’s Hippocratic Oath: Do no harm to the code.

“You have to be responsible for every line of code that gets checked in — for the quality of it, the security of it, the functionality of it, the performance of it,” he said. “And you can’t say, ‘Well, AI told me.’ As engineers, it’s easier than ever to crank out code with these large language models and these tools, but we owe it the same duty of care that we are not checking in unsafe or non-functional code. That’s what this slopsquatting is attempting to exploit.”

Developers can’t blindly trust what AI generates, several security pros said.

“Most developers know that AI can make mistakes, but many still trust the output too much and don’t always check for hidden problems,” [J Stephen Kowski](https://www.linkedin.com/in/jstephenkowski/), field CTO at [SlashNext Email Security+](https://slashnext.com/), told The New Stack. “It’s easy to get caught up in the speed and convenience, but that can lead to missing security flaws or using fake packages. The best protection is to use automated tools that check dependencies and code for issues and to always review what the AI suggests before using it.”

It will be important to use such protections as developers expand their use of AI. Sonatype’s Johnson said he expects generative AI to soon start separating those organizations and programmers who can control and manage the technology from those who can’t.

“The really, really good developers who can challenge the machine, who understand what’s coming out, if it’s right or if it’s wrong, are seeing that geometric gain in productivity,” he said. “You’re going to see certain enterprises that already had good security and engineering practices, where they were working together, get even better. And the ones that were lax are going to fall even further behind and have major issues, breaches. It’s going to separate and sharpen the haves from the have-nots organizationally and individually.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)