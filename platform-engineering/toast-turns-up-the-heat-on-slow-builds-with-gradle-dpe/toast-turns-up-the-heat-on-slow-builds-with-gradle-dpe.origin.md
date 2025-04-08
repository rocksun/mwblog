# Toast Turns up the Heat on Slow Builds With Gradle DPE
![Featued image for: Toast Turns up the Heat on Slow Builds With Gradle DPE](https://cdn.thenewstack.io/media/2025/04/79ded7e8-masha-rayt-uwjtxqprswm-unsplash-1024x575.jpg)
When developer [Aida Issayeva](https://www.linkedin.com/in/aidaisay/) joined [Toast](https://pos.toasttab.com/) in March 2023, the company was having serious problems with long [release cycles](https://thenewstack.io/3-steps-for-automating-software-release-management/) for its popular restaurant management and food ordering app. Due to the long release cycles, Toast was having a hard time quickly getting new features into the app releases and out to customers right away. The delays were also causing frustrations and development backlogs for Toast.

“We saw a problem, and the biggest issue for us was around the lead time to value,” Issayeva, a software engineer and tech lead for the [Point of Sale productivity team at Toast](https://central.toasttab.com/s/article/Get-Started-with-the-Toast-Now-App), told The New Stack. “And we started looking at why our release cycles are longer. The more we shifted left, we saw developers spending more time building features because the build times on [continuous integration](https://thenewstack.io/ci-cd/) (CI) were slow.”

A closer look showed that it was taking more time to fix the issues because Toast was not getting good-quality data to validate what was happening with the build times and tests that were being done on them, she said.

Toast already had a homegrown [platform engineering platform](https://thenewstack.io/3-key-benefits-of-platform-engineering/), but the long release cycle problems were outside the purview of that system.

## Choosing a Strategy To Find a Build Time Remedy
After spending some time at Toast, Issayeva eventually discovered that the long release cycles they were experiencing correlated with long build times, which were hampering the dev teams.

With all this in mind, Issayeva started thinking about how she and her team could solve Toast’s long release cycle challenges by bringing in a [developer productivity engineering (DPE)](https://thenewstack.io/metrics-driven-developer-productivity-engineering-at-spotify/) tool. She had worked with one such tool, [Gradle](https://thenewstack.io/ai-improves-developer-workflow-says-gradle-dev-evangelist/) Enterprise, in previous jobs at Twitter and DoorDash, so she began to evaluate it again. Now called [Gradle Develocity](https://gradle.com/develocity/), the build tool works to accelerate builds and provide testing locally and on CI systems so that dev teams can see what is happening in their code. Using Develocity, she said, developers could fix problems and bottlenecks as they turned up within [Android applications](https://thenewstack.io/dev-news-android-apps-on-rust-astro-db-and-storybook-8/) during the build process.

“Developers would say they would think things were happening but could not know for sure,” as they struggled through problematic builds, she said. “It was a combination of tools and processes. The first step for us was to identify the tool that we lacked. We all had hunches, and we knew it felt like ‘is this part wrong or is that part wrong,’ but we could not quantify that feeling. So, not having back data [on the issues], that is what drove us to get into DPE and Gradle Develocity.”

With Develocity, Toast could quantify data around what was happening with its builds and see how long tasks were taking, while also identifying successful and failed tests, said Issayeva.

“If we know that one of the tests out of 50,000 or 100,000 tests is flaky, that means our build system, Gradle, needs to execute that test multiple times,” she said. “And executing that test that many times comes with the price tag of resources and slows things down. It takes up energy and does not allow you to run other things that you need to run. And imagine, if we have not just one test, but if 80% of those tests are hogging resources, that is a major problem.”

Develocity helps by clearly showing the dev teams and leaders how things are performing and what percentages of builds were caused by flaky tests. By identifying the culprits, Issayeva and her team can then intervene and take actions to resolve the issues, she said. “Plus, because we now have historic data, we can tell when it started flaking out, like before or after new code was added to it. It is easier for us to identify it.“

## Watching the Long Build Times Drop
Just how bad were the build time increases being seen at Toast before Gradle Develocity was brought in?

In 2022, before Issayeva arrived, build times were around 55 minutes each, she said. When she joined the company in March 2023, the average build time had increased to 78 minutes. But three quarters later, using Develocity, the build times were down to 27 minutes, she said.

“It provided us with data on every task,” said Issayeva. “Being able to see each task and how long it takes and what it depends on; all this information is available in Develocity. That is why we can get to a granular level and find out the issues that are causing us problems in real time.”

The final analyses of all the data come from Issayeva and her team, which reads and deciphers the data from Gradle, but those analyses are only possible because the tools provide details that were not accessible in the past, she said.

“Every time when a build happens, whether it is local or remote, Gradle publishes a snapshot of that build scan,” she said. “We load it into our database, which is a special database of all the build scans. And then based on that information, we get the trends and patterns from Gradle Develocity, identifying what we can see about trends for build times. We do not do that every time. We have metrics reviews that we do every two weeks, and that is when we look at this data.”

For Issayeva, finding and solving damaging bottlenecks like these is an important part of her role at Toast.

“Usually, it is my job to find the problem and say, ‘Hey, this is the problem right now and it is going to get two to three times worse in two or three months,’” she said. “Then I bring it up to the leadership so that they can see it. It was an interesting moment when I [identified why] we had slower build times.”

## How Are Platform Engineering and Developer Productivity Engineering Related?
[Brian Demers](https://www.linkedin.com/in/bdemers/), a developer advocate at Gradle and a longtime [Java](https://thenewstack.io/introduction-to-java-programming-language/) developer, told The New Stack that platform engineering and DPE are “complementary approaches that companies and developer teams can use to increase developer productivity,” with each addressing different aspects of improving developer productivity.
“[Platform engineering](https://thenewstack.io/platform-engineering/) looks at developer productivity from an organizational standpoint and focuses on building and maintaining [internal developer platforms (IDPs)](https://thenewstack.io/internal-developer-platforms-the-heart-of-platform-engineering/) that provide self-service capabilities for developers,” said Demers. “DPE goes a step further and focuses on optimizing builds, tests, and troubleshooting processes — things that affect every engineer, regardless of their development environment.”

DPE can specifically help companies that may be struggling with slow build and test cycles, he said, to optimize and accelerate their build and test performance. Meanwhile, platform engineering provides a streamlined and efficient environment where developers can build their applications with curated tools, he said.

“A mature and effective strategy will ultimately involve both DPE and platform engineering,” said Demers. “For example, platform engineering provides a unified environment with self-service capabilities, while DPE ensures that those tools and processes run as efficiently as possible.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)