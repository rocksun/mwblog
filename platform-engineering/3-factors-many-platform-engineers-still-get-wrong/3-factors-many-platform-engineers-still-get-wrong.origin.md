# 3 Factors Many Platform Engineers Still Get Wrong
![Featued image for: 3 Factors Many Platform Engineers Still Get Wrong](https://cdn.thenewstack.io/media/2025/05/e3dc6828-platform-engineer-3-mistakes-1024x576.jpg)
The world of cloud infrastructure and application deployment has changed radically over the last decade. We’ve seen the meteoric rise of cloud providers, Kubernetes and OpenTelemetry, and the fall of once-common tools like Subversion, Yeoman and Grunt. Even in the midst of the cloud’s evolution, many of the basics, including Twelve Factor-based software development, have remained foundational.

In 2011, Heroku’s co-founder, Adam Wiggins, presented the [Twelve Factor App](https://blog.heroku.com/twelve-factor-apps), a manifesto of best practices based on lessons learned at Heroku. With confidence that comes from launching thousands of applications into the cloud, the Heroku team leveraged their experience on what was working and what was not working for developers. They applied the lessons they learned to create the Twelve Factor model — [12 paradigms for successful application deployments](https://thenewstack.io/open-source-drives-the-twelve-factor-modernization-project/).

![Twelve Factor principles](https://cdn.thenewstack.io/media/2025/05/707baa04-12-factors-heroku_350px.png)
(Source: Heroku)

But deploying to the cloud has changed radically in the last 10 years, and the Twelve Factors don’t cover certain new development practices — things like modern observability, logs, tracing and error handling. So in late 2024, Heroku [open sourced and started modernizing](https://thenewstack.io/heroku-moved-twelve-factor-apps-to-open-source-whats-next) the Twelve Factors for today’s infrastructure.

## Building a Strong Foundation
The Twelve Factors have become so well known that “many of its principles are just considered to be standard best practices across the industry,” [Vish Abrams](https://www.linkedin.com/in/vishvananda/), Heroku’s chief architect, said in an interview with The New Stack.

This article takes a closer look at the first three factors, since they [set the foundation](https://thenewstack.io/platform-engineers-must-have-strong-opinions) for the higher levels of Twelve Factor. “If you look at the structure of the Twelve Factors, they build off of one another,” he continued. “You start with the first three — codebase, dependencies, config — and those build into the concepts of the later factors.”

## Factor 1: Codebase
“A Twelve-Factor app is always tracked in a version control system, such asGit,Mercurial orSubversion. A copy of the revision tracking database is known as a code repository, often shortened to code repo orjust repo.”
The first factor revolves around the use of a [codebase](https://12factor.net/codebase) version-control system. The more wizened readers may remember [Mercurial](https://www.mercurial-scm.org/) or [Subversion](http://subversion.apache.org/), but every developer is familiar with [Git](https://roadmap.sh/git-github), which is most widely used today as GitHub.

The first factor is very clear: If there are “multiple codebases, it’s not an app; it’s a distributed system.” Code repositories reinforce this: Only one codebase exists for an application.

So, where are we today? Abrams explained: “When Heroku was first created, it was not super common to use source code management, especially across a team. That has become a standard practice now, and even more so, platforms like GitHub have allowed for the discovery and sharing of projects.”

As GitHub has become a de facto standard in software development, the paradigms of development have also changed. Code reviews and approvals are now centralized and have become an integral part of the deployment process. Code is more secure, as all changes are automatically recorded ([DORA metrics](https://thenewstack.io/dora-2024-ai-and-platform-engineering-fall-short/) FTW!), and permissions can be set to allow only specific members of the team to perform updates. Deployment automation has moved from home-grown scripts to GitHub Actions that are also code reviewed and tested by the team.

Heroku has also evolved and grown with the [new paradigms](https://thenewstack.io/sustainable-development-balancing-innovation-with-longevity) of modern deployments. As Abrams explained: “Initially, the expectation was that you would `git push heroku main`
to launch your application. But now with GitHub integrations, you can push your code to GitHub and build off of pull requests (PRs), and it will create a Heroku deployment so that you can test that your application still works.”

Heroku has also built several open source libraries that facilitate automation with GitHub Actions. Hosting your own instance of the [GitHub Runner](https://github.com/heroku-reference-apps/github-self-hosted-runner-for-github-actions) at Heroku gives you a self-hosted runner for your automated workflows. For example, you can create a Heroku Review Apps API and deploy Heroku Apps from your self-hosted GitHub Runner. You can also upload your private GitHub repo source code to Heroku with [Heroku Flow Actions](https://github.com/heroku-reference-apps/github-heroku-flow-action).

## Factor 2: Dependencies
“A Twelve-Factor app never relies on the implicit existence of systemwide packages.It declares all[dependencies,]completely and exactly, via a dependency declaration manifest.”
Factor number two is about never relying on the implicit existence of packages. While just about every operating system in existence has a version of `curl`
installed, a Twelve Factor-based app does not assume that `curl`
is present. Rather, the application declares `curl`
as a dependency in a manifest.

Every developer has copied code and tried to run it, only to find that the local environment is missing a dependency. The dependency manifest ensures that all of the required libraries and applications are defined and can be easily installed when the application is deployed on a server.

“One of the biggest challenges in dependency management is that it is different in every language — and it’s not just per language; sometimes it is per framework in the language,” Abrams said. “Heroku’s buildpacks allow the user to manage dependencies in the way that they want to and still get an artifact that is built, easy to run and manage.”

The number of external libraries available for developers to use has exploded since the Twelve Factors were published. This has led to another concern: the over-reliance on and potential security risks from third-party libraries. Widespread security events like the [Log4j zero day](https://thenewstack.io/log4j-the-pain-just-keeps-going-and-going/) and the [critical vulnerability in OpenSSH](https://thenewstack.io/malicious-code-in-linux-xz-libraries-endangers-ssh/) are reminders that we must be vigilant in our deployments.

“Be careful about bringing in dependencies,” Abrams advised. “Don’t bring in dependencies when the functionality is simple; just write it yourself. For more complicated functionalities, choose libraries that are well supported and have maintenance and releases so that they can deal with security vulnerabilities as they come up.”

## Factor 3: Config
“

Apps sometimes store config as constants in the code. This is a violation of Twelve Factor, which requires. Config varies substantially across deploys; code does not.”[strict separation of config from code]
Most applications have environmental variables and secrets stored in a `.env`
file that is not saved in the code repository. The `.env`
file is customized and manually deployed for each branch of the code to ensure the correct connectivity occurs in test, staging and production. By independently managing credentials and connections for each environment, there is a strict separation, and it is less likely for the environments to accidentally cross.

For testing, Heroku allows you to manage your configuration securely across the different stages of deployment using the dashboard or the command-line interface (CLI) using a command such as `heroku config:set SECRET_TOKEN=test-secret`
.

## Building on the First Three Factors
The first three factors form the base of the remaining nine. They have been shown to be prescient — the advice still holds just as strongly today as it did in 2011.

Abrams said: “One of the most amazing things is that we have applications that have been running on Heroku for years, and they are resilient because they follow those principles. Not only do the Twelve Factors make these apps easy for us to update, it also keeps them stable and functioning when we make changes.”

For anyone building resilient, maintainable cloud infrastructure, “the most important thing is to go back and read the Twelve Factors. You’ll be surprised at how much still holds… the concepts still make sense today. If you are not following them, you’ll have an application that is not well maintained and hard to keep running,” Abrams concluded.

**If you’d like to learn more, please check out these additional resources:**
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)