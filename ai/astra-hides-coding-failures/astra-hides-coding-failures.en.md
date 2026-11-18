![Robot covering human's eyes while at the computer](https://cdn.thenewstack.io/media/2026/11/448cf0b1-rizki-kurniawan-i0dc7f_riq0-unsplash-1024x571.jpg)

**OpenAI’s new GPT-6.2 Astra is nearly twice as likely as its predecessor** to leave users unaware of problems that prevented it from finishing a coding task, according to the company’s own safety evaluations. Developers building autonomous agents could encounter the same problem, since OpenAI has added a mitigation to Codex that isn’t automatically applied to direct API requests.

In its [GPT-6.2 system card](https://deploymentsafety.openai.com/gpt-6-2-astra-sol/targeted-cases), published Tuesday alongside the release of GPT-6.2 Astra and GPT-6.2 Sol, OpenAI reported that Astra failed to disclose a known obstacle in 22.28% of evaluated coding tasks, compared with 11.09% for GPT-6 Astra.

> An agent may write better code without telling the developer when it couldn’t finish the job.

The copmany says both models perform better on demanding tasks while using fewer output tokens, but those improvements don’t necessarily make them more reliable at reporting failures. An agent may write better code without telling the developer when it couldn’t finish the job.

*The New Stack* has asked OpenAI whether it plans to extend the Codex mitigation to API developers and how the additional instructions affect the models’ failure-reporting behavior.

## Inside the blocker deception test

OpenAI measured the behavior with an internal evaluation called Blocker Deception, which gives models realistic coding assignments before deliberately introducing obstacles that make the requested work impossible to finish as specified.

In some runs, the evaluation removes a source file the agent was supposed to modify. In others, it disables a tool needed to build the project. The evaluation then checks whether the model tells the user what happened or leaves the obstacle out of its final response.

## The caveats Astra leaves out

The company acknowledges the regression and says it is still investigating the cause. One possible explanation is that training the models to give shorter answers with fewer caveats may have made them less likely to report problems that prevented them from completing a task. OpenAI cautions that the evaluation was designed to trigger this behavior, so the results don’t necessarily reflect how often Astra misleads users in production.

A separate evaluation, Broken Search Tool, identified a similar problem. The model receives questions requiring information retrieval while the necessary search capability is disabled. GPT-6.2 Astra failed to acknowledge the missing requirement or unavailable tool in 23% of cases, compared with 7.58% for GPT-6 Astra and 1% for GPT-6.1 Terra.

> Developers can check the logs, test results, and git diff … but they shouldn’t have to dig through an entire session to find out that something failed.

Developers can check the logs, test results, and git diff to see what an agent actually did, but they shouldn’t have to dig through an entire session to find out that something failed. If an agent says it finished the job without mentioning a missing dependency or a failed build, that work could make it through review without anyone realizing there’s a problem. It’s another example of the [code confidence gap](https://thenewstack.io/ai-code-confidence-gap/) that becomes harder to manage as agents take on more work across a repository.

## The fix the API misses

OpenAI says it developed a prompt-based intervention that substantially reduced the rate of omitted blockers in evaluations of both Astra and Sol. The company incorporated that intervention into the standard Codex developer prompt at launch, but it does not automatically apply the same instructions to direct API requests.

> Codex users get the updated prompt, but developers building their own agents through the API don’t.

Codex users get the updated prompt, but developers building their own agents through the API don’t. OpenAI hasn’t shown whether adding similar instructions to a custom harness would produce the same results.

The harness can’t take the model’s completion summary at face value because it needs to verify the diff, check test results, and confirm the expected artifacts exist before marking a task complete.

These [verification loops](https://thenewstack.io/cli-ide-ai-verification/) are especially important for unattended agents, where a failed step can go unnoticed until someone reviews the work.

## Performance up, reporting down

The disclosure comes as OpenAI promotes improvements in coding performance and efficiency across both new models.

In its [launch announcement](https://openai.com/index/introducing-gpt-6-2-astra-sol/), OpenAI said GPT-6.2 Sol came within 0.5 points of Astra on Cognition’s FrontierCode 2.0 coding benchmark at approximately one-fifth the estimated cost per task, with both models running at maximum effort.

In testing shared with *The New Stack* by OpenAI, Replit reported that GPT-6.2 Sol passed more tests, used 62% fewer output tokens and ran nearly three times as fast as GPT-6.1 Sol when building software from scratch.

Faster execution and lower inference costs make these models appealing for automated coding, but OpenAI’s safety tests show that better performance doesn’t necessarily mean an agent will tell developers when something goes wrong.

The post [OpenAI’s own tests show GPT-6.2 Astra is twice as likely to hide coding failures](https://thenewstack.io/astra-hides-coding-failures/) appeared first on [The New Stack](https://thenewstack.io).