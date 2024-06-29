# Don’t Sleep on Source Code Updates
![Featued image for: Don’t Sleep on Source Code Updates](https://cdn.thenewstack.io/media/2024/06/ac0e3c26-dont-sleep-source-code-updates-1024x576.jpg)
Retracing the steps to maintain and update source code is a daunting task, particularly for organizations relying on open source software (OSS) with limited support windows. As time goes on and code is released more frequently, it becomes harder to remember what’s what, which version you used and why someone wrote the code the way they did. And as [technical debt builds up](https://tanzu.vmware.com/content/webinars/jul-19-stop-tech-debt-and-start-using-faster-more-secure-paths-to-production), it becomes increasingly difficult to go back and remediate potential issues or CVEs. Also, as OSS frameworks and tools evolve, the lift required to move to the latest version gets heavier.

Organizations that operate within highly regulated industries have even greater challenges. To adhere to mandates and standards, upgrades can act as a critical checkpoint that must be completed as policy dictates or as CVEs arise. Doing these upgrades only as one-off events when mandated adds another barrier into an often complicated and process-heavy application delivery pipeline.

We saw this firsthand in late 2023, when the [end of OSS support](https://spring.io/blog/2023/11/23/spring-boot-2-7-18-available-now) for versions of open source Java framework [Spring Boot](https://roadmap.sh/spring-boot) (2.x) had many organizations trying to carve out room on their roadmap to upgrade or to extend their support window via commercial support.

## Business Value Always Triumphs
Back when delivering new code required months of work, when code was left untouched, running smoothly in the data center for half a year, the mantra was simple: “If it ain’t broke, don’t fix it.” Quarterly releases were the best-case scenario. More often, updates would occur twice a year, sometimes even just annually.

Most code updates were focused on delivering new functionality to the business, with little time spared for addressing technical debt. [Security and stability](https://tanzu.vmware.com/content/blog/5-ways-to-master-security-with-vmware-tanzu-platform), unless explicitly requested by end users, were often overlooked. Engineers and software architects struggled to advocate for these crucial elements, only to see them snowball into larger issues over time. As such, patching old code turned into a Herculean task as developers kept their distance from the aging codebase.

This fostered the perception that updating source code is a complicated, difficult and low-business-value process. Continually updating source code has yet to find its place in the heart of organizational culture, and many companies are still holding their breath, resorting to any measure to help them evade the looming threat of CVEs.

## Why Upgrades Matter: The Spring/Java Example
The Java/Spring ecosystem is a great example of why continual code upgrades matter. [Java](https://thenewstack.io/java/) is a remarkable language, and over the course of its [25-year history](https://thenewstack.io/how-spring-and-java-shaped-internal-developer-platforms/), very few updates broke existing code. An incredible feat — but a double-edged sword. While code written in the ’90s might still run on the latest version of Java, if none of the patching, none of the maintenance and none of the dependency updates happened along the way, you’d be in a bad spot.

Today things are moving faster, and there are more threats to applications’ surface area than ever. On a more positive note, the pace of innovation is also rapidly increasing, and demand for the latest and greatest tools and tech creates more incentives for development teams to upgrade.

For example, [Java 21](https://openjdk.org/projects/jdk/21/) and [Java 22](https://openjdk.org/projects/jdk/22/#:~:text=JDK%2022%20reached%20General%20Availability,by%20the%20JEP%202.0%20proposal.) are broadly considered among the most significant releases in Java’s history, providing critical new [features and innovations](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/) for those who make the upgrade. While it’s been possible to carry on with Java support provided by [Oracle](https://developer.oracle.com/?utm_content=inline+mention), many organizations are leaving potential savings and benefits on the table by not upgrading.

Some organizations resist upgrades believing that older versions are more stable, but this often isn’t the case. Patches for Spring Boot 3.1 and 3.2 are both released on the same day and fix the same things, so there is nothing that makes one inherently more stable. But by sticking with 3.1, you are missing out on the new features introduced in 3.2.

For example, Spring Boot’s ability to leverage [Coordinated Restore at Checkpoint](https://openjdk.org/projects/crac/) speeds up startup times. Meanwhile, [Native Images](https://docs.spring.io/spring-boot/reference/packaging/native-image/index.html) enable creating smaller application footprints, reducing the surface area of what’s being exposed. This combination makes applications less vulnerable to potential threats and reduces the memory required to host them.

## A Culture of Continuous Upgrades
Creating a culture of continuous upgrades enables your organization to keep pace with innovations and better defend against bad actors. When upgrades become a normal part of your software development life cycle, it no longer takes two or three sprints to upgrade, and you don’t need to tell the project manager that you can’t deliver a feature because you’re working through a list of technical chores. It’s Tooling + Automation + Discipline to do this as you go. The path forward isn’t about how cool and fancy you can get, it’s how maintainable your code is. It’s about being able to look forward a few years and feel confident that your code will be maintained and not add more technical debt to what’s running in production. While major updates may still require some lift, there will be easy buttons and recipes to keep up.

The goal is creating a culture where continuous upgrades become so embedded in your process that they don’t require a second thought. It’s reassurance that what you ship out into the market today will stand the test of time, remaining safe and secure in the years to come, and ensuring you meet [compliance requirements](https://tanzu.vmware.com/content/blog/digital-transformation-bottlenecks-compliance). This sounds great, but there is an investment required to get there.

## Building Your Upgrade Muscle
For organizations that haven’t been in the process of making upgrades and are still on older versions of Java, the upgrade muscle is not always an easy muscle to turn on. There is no cheat code to skip the training and make this work at scale. Every organization has patterns or methods (such as internal libraries or old APIs) that can’t simply be plugged into an existing recipe … code changes will be involved.

It’s time to hit the gym — and you need a workout plan. Here are three tips to consider.

### 1. Start With Leadership Buy-In
Like any major change to the way things are done within an organization, cultural change championed by leadership is critical to success. The people who are responsible for more than just the functionality of applications must be on board before you can move forward. This could mean the CIO, CSO, enterprise architects and even the application leaders who own the portfolios

Software leaders can no longer afford to bet their business (and their customer’s business) on their code being safe and secure. Reducing the time from a CVE being announced to code being patched is now critical.

### 2. Prioritize Release Planning and Portfolio Visibility
Above all else, a good plan and visibility are the critical prerequisites before getting hands-on with any code. This starts with understanding which releases are headed your way. As an example, there were only four weeks in 2023 in which the Spring Framework didn’t have a release. The Spring team is continually pulling in third-party dependencies so that everything under each release is patched, has been tested against each other and is validated to work.

Being aware of what is coming up and understanding the release train of those dependencies is valuable, so you will always know when everything has been patched.

Equally important, your CSO also needs to have a list of all the known CVEs that are coming in and visibility into what’s actually running in production within your application’s portfolio. As the features and codebase grow, it’s easy for things to get lost. Developers are always looking for solutions to fix their problems, so maybe along the way they inserted a library here and there to help them solve what they needed. You need continual visibility into all of that.

### 3. Leverage Tools and Automation
By using scanning tools and application discovery, you can identify where the biggest risks in your portfolio are, bucket apps into easy opportunities to upgrade and identify what will require a bit more effort. This is where automation comes in.

#### Automation Tools
When you’re ready to start upgrading your apps, you need to determine a reasonable starting point that won’t affect or interrupt your existing development pipeline. It might not be sustainable to have all your teams start individually tackling upgrades; instead, a small team and some [automation might be a good starting point](https://thenewstack.io/state-of-finops-survey-points-to-room-for-more-automation/).

For the apps that your analysis identifies as being easy to upgrade or requiring less of a white-glove approach, tools such as [Open-Rewrite](https://docs.openrewrite.org/) offer a simple way to start automating your refactoring and remediation. Open-Rewrite consists of an auto-refactoring engine that runs prepackaged, open source refactoring recipes for common framework migrations, security fixes and stylistic consistency tasks.

Once you have tackled the easy-to-upgrade applications, you can start working on the complex applications that don’t have existing recipes. As you learn more about your apps that need to be upgraded, you can develop your own recipes to scale out your upgrade efforts and establish your own framework going forward.

#### Application Platforms
One question that might come up when looking to upgrade source code is how to manage your code running in production while working on the upgrade. Do you take the application down while upgrading? This is where application platforms shine vis-a-vis stitched-together tools and services. According to the [2024 State of Cloud Native Application Platforms report](https://thenewstack.io/cloud-native-app-platforms-new-research-shows-struggles-and-hope/), enterprises are looking for a single platform experience that supports multiple app types and deployment patterns. A cloud native app platform allows you to run multiple instances that can be upgraded or patched while other instances are running, or change the OS layer for something running in a cloud native buildpack in production.

## Rinse, Repeat and Learn
To truly get to a state of continuous upgrades, there is an aspect of “going back to the gym, even when you’re tired and sore.” But once you’ve found the right workout for your lifestyle, you’ll make it a regular part of your routine. By working through the upgrade process, you will figure out which patterns will work for your organization, learn how to better leverage tools like Open-Rewrite, and create recipes and your own frameworks to help apply them at scale.

Today, everything is moving faster with more opportunities for bad actors, but also more possibilities and innovations to take advantage of. So don’t bet your business on the way things have always been done; start implementing small changes today, and work toward building out your own culture of continuous upgrades.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)