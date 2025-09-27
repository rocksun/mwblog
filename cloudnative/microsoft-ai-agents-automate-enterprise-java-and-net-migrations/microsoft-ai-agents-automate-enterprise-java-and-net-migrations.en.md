Microsoft has rolled out new development tools powered by [AI agents](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/) designed to dramatically reduce the time and complexity of migrating legacy enterprise applications.

The company’s latest offerings help reduce the months-long process of updating [.NET](https://thenewstack.io/net-modernization-github-copilot-upgrade-eases-migrations/) and [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) applications from months to days, [Scott Hunter](https://azure.microsoft.com/en-us/blog/author/scott-hunter/), Microsoft’s vice president of product management for Azure, told The New Stack.

## The Enterprise Legacy Problem

[Enterprise IT departments](https://thenewstack.io/agentic-ai-is-the-next-frontier-in-enterprise-operations/) face a mounting challenge with aging application portfolios. Over 37% of enterprise applications require modernization today, Hunter said. Microsoft announced these capabilities at the [Migrate and Modernize Summit](https://www.microsoft.com/en-us/events/launch-events/migrate-and-modernize-summit) this week.

“Most enterprise customers have acquired companies, which means they acquire technologies,” explained Hunter, who is overseeing the migration initiative. “They’ll have a portfolio of .NET and Java applications — it might be old .NET framework; it could be some old [Java 8](https://thenewstack.io/end-of-the-road-for-javafx-in-jdk-8-keeping-your-apps-alive/). When I talk to my field and sales teams, on average, it takes about eight months to move one of those projects to Azure.”

Hunter said that by postponing critical updates, organizations can accumulate security vulnerabilities and technical debt while missing opportunities to leverage modern cloud capabilities.

Migrations and dependency updates are important, especially with security updates, but they usually don’t deliver value to customers and are a pain for developers, [David Mytton](https://www.linkedin.com/in/davidmytton/), CEO of [Arcjet](https://arcjet.com/), maker of a developer-first security platform, told The New Stack.

“Using AI to speed this up makes a lot of sense with languages like .NET and Java, where code will simply build or not or the tests fail or pass,” he said. “It becomes more difficult if there are subtle breaking changes, like with UI libraries or in edge case user flows. Infrastructure and database upgrades are even harder. Do you really want to let an agent manage a major database version update in production?”

## Agentic Workflows for Migration

Microsoft’s approach starts with [Azure Migrate](https://azure.microsoft.com/en-us/products/azure-migrate), which provides comprehensive discovery and assessment of enterprise application portfolios, he said. The tool automatically takes inventory of applications, dependencies, operating systems and framework versions across an organization’s infrastructure.

“We really want to reduce the number of front doors that a customer has to see,” Hunter said. “I don’t want to come to you and go, ‘Hey, I’ve got 20 different little tools. You can run them all together to migrate your application and get it running in Azure.’ I’d really like to start with a single front door.”

The unified platform eliminates the need for IT teams to coordinate multiple separate tools. Azure Migrate can automatically generate GitHub issues containing complete technical context about applications selected for migration, including operating system details, runtime versions and database dependencies, Hunter said.

## Developer-Centric Workflow

The migration process integrates directly with [GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/)‘s AI agents and popular development environments. Developers receive structured prompts they can use within Visual Studio Code or Visual Studio to initiate agentic workflows that handle much of the technical complexity automatically.

“The most important thing here is we don’t just go run off and do work on your behalf,” Hunter emphasizes. “We build the full plan, let you edit the plan, and when you’re ready to go, you tell it to start moving.”

The AI agents generate detailed migration plans before making any code changes. Developers can review these plans, modify recommendations, and add or remove specific updates based on their application’s requirements. This ensures developers maintain oversight while benefiting from autonomous execution of routine tasks.

## Measurable Time Savings

Early implementations show substantial productivity gains. Hunter said Microsoft’s Xbox team recently used these tools to migrate multiple projects to newer .NET versions, reducing the migration effort by 88%. Also, [Ford China](https://finance.yahoo.com/news/ford-establishes-subsidiary-china-090612787.html) achieved a 70% reduction in time and effort when modernizing middleware applications, he said.

“This is all about optimizing the time for a company to make these transitions,” Hunter noted. “In many cases, companies won’t even make these transitions because they’re afraid of it.”

The AI agents handle complex scenarios, including dependency updates, security patches and framework-specific compatibility issues. When the agents encounter problems they cannot resolve automatically, they provide detailed analysis and specific recommendations for manual intervention.

## Beyond Version Updates

The platform extends beyond simple framework upgrades through Microsoft’s [Azure Migrate application and code assessment tool (AppCAT)](https://learn.microsoft.com/en-us/azure/migrate/appcat/overview?view=migrate-classic), which analyzes applications for cloud optimization opportunities. The primary Microsoft tool for assessing application code, especially for migration and modernization to Azure, is AppCAT, which analyzes .NET and Java applications to identify potential issues and opportunities when moving an application to the cloud. The tool identifies specific improvements, such as replacing local file storage with content delivery networks or updating authentication methods for better security.

“We have a tool that can identify these problems,” Hunter explains. “For example, if you’re running a .NET application and it’s got a SQL Server connection string, well, as you move that out to Azure, you’re better off not having a connection string, because that’s a security risk.”

Organizations can implement these recommendations through prebuilt [agentic workflows](https://thenewstack.io/what-agentic-workflows-mean-to-microservices-developers/) or create custom patterns based on their own code changes, enabling consistent updates across entire application portfolios, he said.

## Multi-Platform Development Support

Microsoft is expanding tool compatibility beyond its own development ecosystem. GitHub Copilot now works within [JetBrains IDEs](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/), [Eclipse](https://thenewstack.io/eclipse-theia-the-deepseek-of-ai-tooling/) and [Xcode](https://thenewstack.io/start-your-apple-coding-journey-with-xcode/), allowing developers to use their preferred development environments, Hunter said.

“We want to meet developers where they are,” he stated. “I don’t want to say you have to use one of my IDEs to do this kind of work.”

Microsoft also has broadened database support, recently adding [PostgreSQL](https://thenewstack.io/postgresql-18-delivers-significant-performance-gains-for-oltp-and-analytics/) migration assessment alongside existing capabilities for SQL Server, [Oracle](https://www.oracle.com/developer?utm_content=inline+mention) and Sybase workloads.

## Integrated Operations Support

The migration tools connect with [Microsoft’s Site Reliability Engineering (SRE) AI agents](https://learn.microsoft.com/en-us/azure/sre-agent/overview?tabs=explore) for ongoing application monitoring and maintenance. After migration and deployment, the platform provides detailed performance analysis and proactive recommendations for scaling and optimization.

“Before, I used to just get a pager saying something’s broken,” Hunter noted, describing the traditional approach. “Now I get a detailed analysis. I might even get a memory dump. It might even show me where it thinks the code issue is, and it offers me the chance to actually scale the application up while I’m working on the issue.”

## Reducing Development Overhead

The initiative reduces what Hunter calls “developer toil” — routine maintenance tasks that prevent development teams from focusing on new feature development and innovation.

“This is all about developer toil. How do we reduce that developer toil?” Hunter explains. “That’s not what I as a software engineer want to go do. I want to write new code. I want to build new applications.”

The AI agents handle time-consuming activities like dependency management, security updates and compatibility fixes that previously required extensive manual effort from senior developers.

## Industry Impact

With general availability now announced for Java and .NET applications, Microsoft is targeting a fundamental constraint in enterprise software development. The platform represents a shift from manual, resource-intensive migration processes to AI-driven agentic workflows that can handle complex enterprise scenarios efficiently.

[Torsten Volk](https://www.linkedin.com/in/torstenvolk/), an analyst at Enterprise Strategy Group, said everything that Microsoft does needs to be evaluated in front of their goal of onboarding cloud workloads faster than [AWS](https://aws.amazon.com/?utm_content=inline+mention) and [GCP](https://cloud.google.com/?utm_content=inline+mention) can.

“That’s why they embraced Linux, acquired GitHub and invested heavily into OpenAI,” he told The New Stack. “Now these investments all come together nicely, with GitHub and Copilot nicely packaging workloads for easy Azure onboarding. Microsoft also doesn’t care what database companies are using; they are ready to give them anything that makes it easier to get them on board. Pushing their own software is much less important than getting companies onboarded and getting them hooked on lots of revenue-generating services from the bottom to the top of the application stack. Of course, AWS and GCP follow that same playbook, but of course, Microsoft has a much stronger foothold inside the enterprise, as that’s where they started from.”

Meanwhile, [Holger Mueller](https://www.linkedin.com/in/holgermueller/), an analyst at Constellation Research, said when the technical debt load gets too high, “the good news is that AI can help understanding old code, and more and more help renovate, if not even innovate, the older code.”

And enterprises should not lift and shift their automation, but also take advantage of innovations like AI and more modern, advanced databases.

“That is what Microsoft is going after with its Migrate and Accelerate offerings,” Mueller said. “As usual, it’s back to CxOs to decide how valuable they are — and if they want to move to Azure, where all these migration tools point to.”

Organizations can now approach application modernization as a manageable, predictable process rather than a major project requiring dedicated teams and extended timelines, Hunter said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)