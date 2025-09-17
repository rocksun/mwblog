This year’s Stack Overflow survey found that 24% of developers are happy at work. That’s nearly one in four developers.

Granted, it’s not an overwhelming percentage, but it’s better than last year when only one in five, or 20%, said they were happy in their current job.

At the same time, they seem to have made an uneasy peace with AI: 78.5% said they are using AI anywhere from daily to monthly. That compares to 16.2% who are not using AI tools and do not plan to do so. Another 5.3% are not yet using tools but plan to soon. More than 33,660, or 68.7%, of respondents answered the question.

Programmers also seem to be growing a little more comfortable about AI agents usage, with [23% using AI agents regularly](https://thenewstack.io/23-of-devs-regularly-use-ai-agents-per-stack-overflow-survey/).

The [2025 Stack Overflow Developer Survey](https://survey.stackoverflow.co/2025/) found that 64% now say AI isn’t a threat to their jobs, which is down slightly from 68% last year. The survey also found that respondents who are currently [using mostly AI tools to complete tasks](https://thenewstack.io/ai-combined-with-agile-lets-developers-focus-on-craft/) in the development workflow are highly satisfied with and frequently using AI to search for answers or learn new concepts.

[![Stack Overflow Developer survey shows 1 in four developers are happy at work, up from last year. 28.4% are unhappy and 47.1% are complacent.](https://cdn.thenewstack.io/media/2025/09/d0a703aa-stackoverflow-dev-survey-2025-work-job-satisfaction-job-sat-social.png)](https://cdn.thenewstack.io/media/2025/09/d0a703aa-stackoverflow-dev-survey-2025-work-job-satisfaction-job-sat-social.png)

Image via Stack Overflow’s 2025 Developer survey, licensed under the [Open Database License](https://opendatacommons.org/licenses/odbl/).

The New Stack spoke with Jody Bailey, the chief product technology officer at Stack Overflow, about the survey results. We also asked what he’s seeing in terms of AI within Stack Overflow’s own IT department and among enterprise developers.

“The definition of developer is going to evolve,” Bailey predicted. “In reality, we’re going to have more people developing, because it will be easier. The tooling, the AI models, will continue to get better.”

Better AI will lead to more workers, including developers, using AI to bring their ideas to life, he says.

“We have a lot of engineers and developers that have really great ideas, [but a] limited amount of time, limited amount of capacity,” he said. “Similarly, on the design and product side, the tooling will allow people to present their ideas more effectively. It will allow them to do more innovation and to actually focus on solving user problems, as opposed to just wrangling code all the time.”

But there are challenges to using AI for development, particularly in enterprise settings, he noted.

## Challenge One: Executive Mandates About AI Use

Despite increased usage, trust in AI-generated answers and code is declining, indicating a healthy skepticism about AI tools, Bailey said.

Of all Stack Overflow respondents, the majority somewhat or highly distrust AI results — at 45.7%, versus 30.7% that trust it (only 60.78% of respondents answered the question). When the survey broke that down to professional developers only (52.4% responses), they found 46% did not trust AI while 32.3% trusted it.

[![Graph showing 3.1% highly trust AI; 29.6% somewhat trust AI; 26.1% somewhat distrust AI; and 19.6 highly distrust AI.](https://cdn.thenewstack.io/media/2025/09/0f1c7776-stackoverflow-dev-survey-2025-ai-developer-tools-ai-acc-social.png)](https://cdn.thenewstack.io/media/2025/09/0f1c7776-stackoverflow-dev-survey-2025-ai-developer-tools-ai-acc-social.png)

Image via Stack Overflow’s 2025 Developer Survey, licensed under the [Open Database License](https://opendatacommons.org/licenses/odbl/).

There’s also a disconnect between senior leadership and developers. Executives tend to think AI can just make everything happen and that it’s really fast to do so, Bailey said. Some leaders are even putting a cap on hiring unless a team can prove the job can’t be done with AI. Others have said if developers won’t use AI, then they don’t have a job.

Bailey thinks both approaches are wrong.

“My experience [is] that kind of mandate often backfires,” he said. “Expecting all code to be written by AI is probably setting the wrong expectation. Blindly trusting that anything that we generate from AI without proper review and understanding is a no.”

## Challenge Two: Bad AI-Generated Code

While leaders seem to think AI can handle coding tasks, that’s not what senior developers see. They see AI doing about 80% of the project, but leaving 20% undone. Unfortunately, that 20% undone ends up requiring more than its share of effort.

A good bit of developer distrust also tracks back to AI producing bad or nonsensical code. For senior developers, this leads to a bad choice between fixing incorrect AI code that’s possibly created from inadequate prompts, or just write the code themselves from scratch.

“The senior engineers [are] asking themselves, is it going to be faster to [generate the code](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/) and fix it or just write the code,” Bailey said. “Sometimes it’s more work to edit than it is to adjust.”

> “There’s still a lot of learning around how to use AI to generate code. One of the things that we see is how much of a difference the way you prompt something can impact what’s actually generated.”  
> **– Jody Bailey, Stack Overflow chief product technology officer**

One way enterprises are addressing the problem of AI-created [bad code](https://thenewstack.io/bad-code-stalls-developer-velocity/) is by requiring developers to submit their prompts along with the pull requests, Bailey said.

“There’s still a lot of learning around how to use AI to generate code,” he said. “One of the things that we see is how much of a difference the way you prompt something can impact what’s actually generated.”

Senior engineers say if somebody doesn’t understand the code, how can they ask the right questions, he added. By including the prompt with the pull request, senior developers determine what role a poorly-worded prompt played in creating flawed code.

“I thought that was a really clever idea, because it’s a lot like when you interview an engineer, where you may ask them to solve a problem. You don’t expect them to necessarily write out all the code, but tell me how you would think about it,” he said.

## Challenge Three: AI Lacks Data About Internal Code and Practices

Another common problem is that [large language models (LLMs)](https://thenewstack.io/introduction-to-llms/) lack the specific, proprietary knowledge that’s unique to the company’s codebase, standards and best practices. To offset these problems, developers need access to tools that are grounded in their organization’s own internal coding knowledge base.

[![Nearly 64% of developers said AI is not a threat to their job.](https://cdn.thenewstack.io/media/2025/09/8e3971e8-stackoverflow-dev-survey-2025-work-job-satisfaction-ai-threat-social.png)](https://cdn.thenewstack.io/media/2025/09/8e3971e8-stackoverflow-dev-survey-2025-work-job-satisfaction-ai-threat-social.png)

Image via Stack Overflow’s 2025 Developer Survey, licensed under the [Open Database License](https://opendatacommons.org/licenses/odbl/).

“The other thing, especially within large enterprises, is almost all of the AI tools that they’re using are built on a public corpus of information that may or may not be relevant to their particular organization,” Bailey said. “So how do you get the more nuanced or proprietary information into the hands of the developers in the moment that they need it?”

One way Stack Overflow is helping solve that problem is by surfacing knowledge about coding. For instance, Stack Overflow offers Stack Overflow for Teams, an enterprise SaaS solution for engineers that is used by more than 20,000 organizations. It provides a knowledge intelligence layer to help developers access relevant internal documentation and best practices as they code.

The plan is to also surface additional knowledge through [Model Context Protocol](https://thenewstack.io/building-your-first-model-context-protocol-server/) or IDEs, he added.

LLMs provide a lot of the coding standards: They can complete functions and they can write code for you, Bailey said. But it’s all based on the standard practices of the industry. The question then is how to surface those specific standards within an organization and make them part of the process.

“One of the things that we’re building out is really that knowledge intelligence layer,” Bailey said. “What we want to do is we want to [put that at their fingertips as they’re writing code](https://thenewstack.io/developers-put-ai-bots-to-the-test-of-writing-code/), as opposed to having to stop and go find that information.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)