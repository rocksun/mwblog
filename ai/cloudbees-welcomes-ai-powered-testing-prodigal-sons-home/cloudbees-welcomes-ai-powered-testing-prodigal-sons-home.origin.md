# CloudBees Welcomes AI-Powered Testing, ‘Prodigal Sons’ Home
![Featued image for: CloudBees Welcomes AI-Powered Testing, ‘Prodigal Sons’ Home](https://cdn.thenewstack.io/media/2024/08/3d9881df-welcome-sign-724689_1280-1-1024x576.jpg)
[DevOps](https://thenewstack.io/devops/) specialist [CloudBees](https://thenewstack.io/cloudbees-scales-jenkins-redefines-devsecops/) has enhanced its [CI/CD](https://thenewstack.io/ci-cd/) and [DevSecOps](https://thenewstack.io/kubernetes-security-report-evolving-landscape-of-devsecops/) platform with new AI capabilities by acquiring [Launchable](https://www.launchableinc.com/), an AI company focusing on optimizing software testing and development processes.
Ironically, a key factor in this move is the return to CloudBees of [Kohsuke Kawaguchi](https://www.linkedin.com/in/kohsukekawaguchi/) and [Harpreet Singh](https://www.linkedin.com/in/singhharpreet/), former CloudBees employees who worked on Jenkins (previously known as [Hudson](https://en.wikipedia.org/wiki/Hudson_(software))). The two left CloudBees to launch Launchable in 2019.

The two returnees will be AI co-leads at CloudBees, said [Shawn Ahmed](https://www.linkedin.com/in/shawnahmed/), the company’s chief product officer. The founders of Launchable have extensive experience in both DevOps and AI, making the acquisition valuable for CloudBees’ future AI initiatives.

![](https://cdn.thenewstack.io/media/2024/08/252320d6-image001-4-1-300x300.png)
Shawn Ahmed, chief product officer, CloudBees

## Two Main Challenges
With the new AI capability, CloudBees aims to address two of the main challenges in software development: Optimizing QA and testing processes; and triaging pipeline failures, Ahmed said.

AI and ML have had a profound impact over the last two years on software development, and particularly in the arena of generating code with solutions such as [Microsoft](https://news.microsoft.com/?utm_content=inline+mention)/[GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/), [Amazon](https://aws.amazon.com/?utm_content=inline+mention)[ Q](https://thenewstack.io/amazon-q-apps-ai-powered-development-for-all/), he noted. And developers have drawn tremendous benefits from being able to have a coding assistant on their side to be able to generate a whole lot more code.

“But here’s the thing, the delivery pipelines are still the same,” Ahmed told The New Stack. “The other constant is that there’s 24 hours in the day, and you have to run your build pipelines, your test pipelines, your deploy pipelines within that same time window. When you have this very large increase in the amount of code being generated coming through those same pipelines with those constraints through them, the question that has been on everybody’s mind is how do you apply technologies like large language models, machine learning and AI to use cases and everything else that happens after you commit your code?”

Rather than spending hours in the testing stage of the pipeline, Launchable has taken an innovative way to look at things like “flaky” tests, Ahmed said. They started looking at test failures and began to draw relationships between types of code changes a developer does and the type of tests that will fail and started looking at predicting what kind of code changes would lead to what kind of failures, he explained.

“Now imagine if you had like 50 tests you’re running and the first 49 passed but the 50th failed and it took those 55 hours to run. Why wait all those hours for 49 tests that you know that are going to pass to pass when you know the 50th will fail?” he said. “Why not just run the 50th first and create a test suite for that and fail the code faster so that you can take all that time that was spent running tests that otherwise passed and run them later but focus on giving time back to the developers?”

That lies at the core of Launchable and with Jenkins in use across the CloudBees customer base, users can “complement their pipelines with a few calls out to Launchable’s technology and gain tremendous time back for their developers by predicting which tests are going to fail and using AI to triage the errors and provide solution facts to the developer on what to fix,” Ahmed explained.

This can save developers time by reducing unnecessary testing and providing faster feedback on potential failures.

In [Stack Overflow’s 2024 Developer Survey](https://survey.stackoverflow.co/2024/) conducted in July, 46% of developers said they are interested in using AI to test code — the highest percentage of all the workflows asked about. And 81% of professional developers said they thought using AI to test code would be more integrated with their workflow in the next year.

## The Jenkins Boys Come Home
“So they [Kawaguchi and Singh] had an amazing experience and were kind of the first ones to think about how AI could be applied to DevOps,” [Sacha Labourey](https://www.linkedin.com/in/sachalabourey), co-founder and chief strategy officer at CloudBees, told The New Stack. “And that was well before anybody was talking about [LLMs](https://thenewstack.io/choosing-when-to-use-or-not-use-llms-as-a-developer/). Those guys since 2019 have been doing DevOps and AI day in, day out. So it’s a great fit for us in terms of making this very real. Kohsuke and Harpreet are back in the house, so that’s really cool.”

![](https://cdn.thenewstack.io/media/2024/08/ebe40b25-kohsuke-300x296.jpg)
Kohsuke Kawaguchi, creator of Jenkins, Launchable co-founder

Perhaps the AI-driven testing will indeed give developers time back to work on new development, one analyst says.

“Kohsuke returning home to the Jenkins community is really cool, but he’s bringing with Launchable a way to inject deep AI test analysis into the CI/CD pipeline that should greatly reduce false positives from whatever test frameworks they are running, which in turn will reduce developer triage and investigation time,” [Jason English](https://www.linkedin.com/in/jasonenglish/), an analyst with [Intellyx](https://intellyx.com/), told The New Stack. “Since Launchable was already developed with Jenkins in mind, existing users should be able to turn on the capability on day one.”

Moreover, “Jenkins continues to dominate the CI/CD DevOps market. Jenkins oversees hundreds of thousands of test suites, and CloudBees can deploy the Launchable solution to each one and use AI to improve their efficiency,” Singh wrote in a [blog post](https://www.launchableinc.com/blog/cloudbees-acquires-launchable-to-bring-ai-powered-insights/). “There are also several CI vendors in the market, in addition to Jenkins. Launchable’s approach is also CI agnostic. Thus, CloudBees can help folks struggling with QA regardless of which provider these pipelines exist on.”

[Jenkins holds about 47%](https://6sense.com/tech/continuos-integration/jenkins-market-share) of the market for CI/CD tools. The top three of Jenkins’s competitors in the Continuous Integration and Delivery category are Atlassian Bitbucket with 18.47%, CircleCI with 5.76%, TeamCity with 5.52% market share, according to [6sense](https://6sense.com/).
“You cannot talk about CloudBees without talking about Jenkins, and you cannot talk about Jenkins without speaking about Kohsuke (co-CEO, Launchable), its creator,” Singh wrote.

Indeed, “What makes the journey sweet for both Kohsuke and me (the founders of Launchable) is that we have stood side-by-side with CloudBees founders to help build CloudBees in an earlier life. It is a homecoming for us, and we couldn’t be more excited,” he stated in the post.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)