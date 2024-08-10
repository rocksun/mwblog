# CloudBees Welcomes AI-Powered Testing, ‘Prodigal Sons’ Home

![Featued image for: CloudBees Welcomes AI-Powered Testing, ‘Prodigal Sons’ Home](https://cdn.thenewstack.io/media/2024/08/3d9881df-welcome-sign-724689_1280-1-1024x576.jpg)

[DevOps](https://thenewstack.io/devops/) experts [CloudBees](https://thenewstack.io/cloudbees-scales-jenkins-redefines-devsecops/) have added new AI capabilities to their [CI/CD](https://thenewstack.io/ci-cd/) and [DevSecOps](https://thenewstack.io/kubernetes-security-report-evolving-landscape-of-devsecops/) platform through the acquisition of AI company [Launchable](https://www.launchableinc.com/), which focuses on optimizing software testing and development workflows.

Ironically, a key factor in the move is the return of [Kohsuke Kawaguchi](https://www.linkedin.com/in/kohsukekawaguchi/) and [Harpreet Singh](https://www.linkedin.com/in/singhharpreet/) to CloudBees, who were previously employees of CloudBees and involved in the development of Jenkins (formerly known as [Hudson](https://en.wikipedia.org/wiki/Hudson_(software))). The two left CloudBees in 2019 to found Launchable.

The company's Chief Product Officer, [Shawn Ahmed](https://www.linkedin.com/in/shawnahmed/), said the two returnees will serve as CloudBees' co-heads of AI. The founders of Launchable have extensive experience in DevOps and AI, making the acquisition valuable for CloudBees' future AI initiatives.

![](https://cdn.thenewstack.io/media/2024/08/252320d6-image001-4-1-300x300.png)
Shawn Ahmed, Chief Product Officer, CloudBees

## Two Major Challenges

With the new AI capabilities, CloudBees aims to address two major challenges in software development: optimizing QA and testing workflows; and classifying pipeline failures, Ahmed said.

Ahmed pointed out that in the past two years, AI and ML have had a profound impact on software development, particularly in the area of code generation using solutions like [Microsoft](https://news.microsoft.com/?utm_content=inline+mention)/[GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/), [Amazon](https://aws.amazon.com/?utm_content=inline+mention)[ Q](https://thenewstack.io/amazon-q-apps-ai-powered-development-for-all/). Developers have benefited greatly from having a coding assistant that can help them generate more code.

“But the problem is, the delivery pipeline remains the same,” Ahmed told The New Stack. “The other thing that remains the same is that there are only 24 hours in a day, and you have to run your build pipeline, your test pipeline, and your deployment pipeline within the same time window. When you have these constraints in these same pipelines, and you have this massive increase in code generation, the question everyone is thinking about is how do you apply technologies like large language models, machine learning, and AI to the use cases and everything that happens after the code is committed?”

Instead of spending hours in the testing phase of the pipeline, Launchable took a novel approach to dealing with “flaky” tests, Ahmed said. They started looking at test failures and began to establish a correlation between the types of code changes developers were making and the types of tests that were going to fail, and started looking at predicting which code changes would lead to which types of failures.

“Now imagine you’re running 50 tests, the first 49 pass, but the 50th fails, and it took 55 hours to run those tests. Why wait until the 49 you already know will pass pass, and you already know the 50th will fail?” he said. “Why not run the 50th first, create a test suite for it, and get the code to fail faster so you can reclaim all the time you spent running the tests that would have passed anyway, and run them later, but focus on saving time for developers?”

That’s the core of what Launchable does, and with Jenkins being widely used among CloudBees’ customer base, users can “supplement their pipelines with some calls to Launchable technology and save their developers a lot of time by predicting which tests will fail and using AI to classify errors and provide developers with solutions on how to fix them,” Ahmed explained.

This can save developers time by reducing unnecessary testing and providing faster feedback on potential failures.

In the [Stack Overflow 2024 Developer Survey](https://survey.stackoverflow.co/2024/) (conducted in July), 46% of developers said they were interested in using AI to test code — the highest percentage of any workflow asked about. 81% of professional developers said they believe using AI to test code will be more integrated into their workflows in the next year.

## Jenkins Boys Home


### TRANSLATOR'S RESPONSE

### EDITOR'S RESPONSE
“所以他们[Kawaguchi 和 Singh] 有了很棒的体验，并且是第一个思考如何将 AI 应用于 DevOps 的人，”CloudBees 的联合创始人兼首席战略官 [Sacha Labourey](https://www.linkedin.com/in/sachalabourey) 在接受 The New Stack 采访时表示。“这早于任何人在谈论 [LLMs](https://thenewstack.io/choosing-when-to-use-or-not-use-llms-as-a-developer/)。从 2019 年开始，这些人一直在日复一日地进行 DevOps 和 AI。所以，在使这一切变得非常现实方面，这对我们来说非常合适。Kohsuke 和 Harpreet 回来了，这真的很酷。”

![](https://cdn.thenewstack.io/media/2024/08/ebe40b25-kohsuke-300x296.jpg)
Kohsuke Kawaguchi，Jenkins 的创建者，Launchable 的联合创始人

一位分析师表示，也许 AI 驱动的测试确实会让开发人员有更多时间来开发新功能。

“Kohsuke 回到 Jenkins 社区真的很酷，但他带着 Launchable 来到了这里，它提供了一种将深度 AI 测试分析注入 CI/CD 管道的方法，这应该会大大减少他们运行的任何测试框架的误报，从而减少开发人员的分类和调查时间，”[Jason English](https://www.linkedin.com/in/jasonenglish/), Intellyx 的分析师，在接受 The New Stack 采访时表示。“由于 Launchable 已经考虑到了 Jenkins，因此现有用户应该能够在第一天就启用该功能。”

此外，“Jenkins 继续主导 CI/CD DevOps 市场。Jenkins 管理着数十万个测试套件，CloudBees 可以将 Launchable 解决方案部署到每个测试套件中，并使用 AI 来提高其效率，”Singh 在一篇 [博客文章](https://www.launchableinc.com/blog/cloudbees-acquires-launchable-to-bring-ai-powered-insights/) 中写道。“除了 Jenkins 之外，市场上还有几个 CI 供应商。Launchable 的方法也是 CI 独立的。因此，CloudBees 可以帮助那些无论这些管道存在于哪个提供商上，都难以进行 QA 的人。”

[Jenkins 占据了 CI/CD 工具市场约 47%](https://6sense.com/tech/continuos-integration/jenkins-market-share)。根据 [6sense](https://6sense.com/) 的数据，Jenkins 在持续集成和交付类别中的前三大竞争对手分别是 Atlassian Bitbucket，市场份额为 18.47%，CircleCI，市场份额为 5.76%，TeamCity，市场份额为 5.52%。

“你不能不谈论 Jenkins 就谈论 CloudBees，你不能不谈论 Kohsuke（Launchable 的联合首席执行官），它的创建者，”Singh 写道。

事实上，“让 Kohsuke 和我（Launchable 的创始人）的旅程变得甜蜜的是，我们曾经与 CloudBees 的创始人并肩作战，帮助他们在早期建立 CloudBees。这对我们来说是一个回家之旅，我们对此感到无比兴奋，”他在帖子中写道。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)