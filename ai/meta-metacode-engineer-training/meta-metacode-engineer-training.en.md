**Meta is asking thousands of its software engineers** to help train its internal AI coding tools by simply fixing code, something the team does all day.

Last month, [Maher Saba](https://www.linkedin.com/in/maher-saba-5363705/), vice president of Meta’s Applied AI Engineering organization, asked engineers across the company to submit at least one code “diff” each week using MetaCode, the company’s internal AI coding agent, according to an internal memo obtained by [*The Information.*](https://www.theinformation.com/newsletters/ai-agenda/meta-plans-close-gap-anthropic-openai-coding)

Saba said the corrections that come from engineers fixing a bad batch from MetaCode have already helped improve Muse Spark 1.1 and will be used to post-train an upcoming model known internally as Watermelon. According to the memo, 7,000 weekly active users have already submitted more than 800 fixes so far. Meta has even added colored badges to employees’ internal profiles based on the number of changes they contribute to encourage them to find more.

> MetaCode gives Meta access to that entire process, which gives the company the ability to see the original task and MetaCode’s response, followed by the engineer’s correction and whatever tests or reviews were needed to approve it.

## Engineers fix what AI breaks

Public repositories contain enormous amounts of working software, but they rarely capture things such as the model’s first attempt, where it went wrong, and what an experienced engineer changed before the code was ready to merge. But MetaCode gives Meta access to that entire process, allowing the company to see the original task and MetaCode’s response, followed by the engineer’s correction and whatever tests or reviews were needed to approve it.

After enough submissions, Meta may be able to spot recurring problems. Those mistakes are what the company can collect during ordinary development, without creating artificial coding exercises for the model.

Worth noting, Meta has not explained how it prepares or weighs these corrections during post-training. Nor has it said that every patch and code review automatically becomes training data. The memo describes a deliberate process in which engineers submit corrections after MetaCode gets something wrong.

## Chasing a moving leaderboard

Meta introduced Muse Spark 1.1 on July 9, 2026. The company said developers and researchers inside Meta already use it daily and that the new version was much better at coding than the original Muse Spark. Yet, it still trails the strongest models on public tests. Muse Spark 1.1 scored 53% on the DeepSWE 1.1 leaderboard, which tests coding agents on 113 long-running software engineering tasks.

At launch, Meta compared that result with GPT-5.5 at 67% and Claude Opus 4.8 at 59%. OpenAI and Anthropic have since moved ahead again. GPT-5.6 Sol, released in mid-July, scored 73%, while Claude Opus 5 reached 74% after its July 24 release.

Those numbers require context. DeepSWE tests models using the same mini-swe-agent harness, but it does not test MetaCode, which is Meta’s internal coding product. Improvements to MetaCode should not be presented as improvements to Muse Spark’s public DeepSWE score unless Meta reports that connection directly. That said, the leaderboard makes Meta’s problem clearer, highlighting that its model is chasing competitors that continue to improve.

## Token costs compound at scale

Cost gives Meta another reason to make this work. Coding agents can burn through tokens as they search repositories, test solutions and revise their code. Multiply that by thousands of engineers, some running agents on lengthy jobs, and the bill becomes significant.

Muse Spark 1.1 costs $1.25 per million input tokens and $4.25 per million output tokens through Meta’s API. That is considerably less than Anthropic and OpenAI charge for their frontier models. If Meta can narrow the performance gap, it could run coding agents across the company without paying a competitor each time one of its engineers assigns a task.

That pricing looks even more favorable after OpenAI [slashed GPT-5.6 Luna costs by 80%](https://thenewstack.io/gpt-5-6-api-price-cuts/) in late July, dropping input tokens to $0.20 per million — a move driven in part by pressure from efficient Chinese open-weight models. The price war makes Meta’s position more complex: its model is cheaper than the frontier options, but the frontier options are getting cheaper fast.

> The price war makes Meta’s position more complex: its model is cheaper than the frontier options, but the frontier options are getting cheaper fast.

## Competitors aren’t standing still

Meta is not the only company trying to close the loop between AI-generated code and real-world engineering. Alibaba recently ran its Qwen model on a [16-day autonomous coding stretch](https://thenewstack.io/qwen-autonomous-coding-audit/) with every commit published to GitHub, a different approach to the same underlying bet that production coding is a better training signal than synthetic benchmarks.

During the company’s second-quarter earnings call, CEO Mark Zuckerberg said Meta has more coding and productivity tools on its roadmap.

MetaCode could eventually become one of them, or it could remain an internal tool. For now, its value to Meta comes from what happens every time it makes a mistake.

> For now, its value to Meta comes from what happens every time it makes a mistake.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)