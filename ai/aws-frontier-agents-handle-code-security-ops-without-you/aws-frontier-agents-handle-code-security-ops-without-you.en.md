[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) has launched three [AI agents](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/) designed to work autonomously across the [software development lifecycle](https://thenewstack.io/ai-agents-are-finally-starting-to-revolutionize-the-software-development-lifecycle/).

This move marks a shift from tools that require constant human oversight to agents that can operate independently as team members. AWS announced the agents, known as frontier agents, at the [AWS re:Invent](https://reinvent.awsevents.com/) conference today. These three agents, now in preview, are the first of what will likely be many, AWS indicated. Frontier agents can be created across any domain or industry.

The three frontier agents — [Kiro](https://thenewstack.io/aws-kiro-brings-automated-reasoning-to-agentic-development/) autonomous agent, AWS Security Agent, and AWS [DevOps](https://thenewstack.io/introduction-to-devops/) Agent — can run for hours or days without intervention, handle multiple tasks simultaneously and work toward broad goals rather than requiring step-by-step direction, according to AWS.

“Up until now, with a lot of developer tools in this space, it’s mostly been human in the loop,” said [Amit Patel](https://www.linkedin.com/in/amit-patel-040453/), GM/Director of Agentic AI at AWS, told The New Stack. “With these frontier agents, what we’re planning is these agents will be able to essentially work on their own, autonomously, without intervention from the developer.”

[AI coding assistants](https://thenewstack.io/ai-coding-assistants-12-dos-and-donts/) have accelerated individual tasks but also created new friction by requiring developers to act as the “human thread” that holds work together — rebuilding context when switching tasks, manually coordinating cross-repository changes and stitching together information scattered across tickets, pull requests and chat threads, AWS said.

“With these frontier agents, what we’re planning is these agents will be able to essentially work on their own, autonomously, without intervention from the developer,” Patel said.

AWS developed the frontier agents by observing its own development teams building services at Amazon scale, according to the company. Three insights emerged: teams could move from babysitting every small task to directing agents toward broad outcomes; velocity was tied to how many agentic tasks could run simultaneously; and the longer agents could operate independently, the better. The company realized it needed these capabilities across the entire software development lifecycle — not just coding — or risk creating new bottlenecks, Patel said.

“You can think of these agents as kind of members of the team, as opposed to just a tool that the developer is interacting with on a regular basis.”

The agents behave like another member of the team. They learn over time. They have memory about how the team works on particular things or particular issues or bug fixes or roadmap items, and they then, based on that learning, will take actions and submit pull requests so that another team member can review it and accept it, Patel noted.

“Over time, it learns that it has memory. So, it keeps learning, and it keeps getting better — kind of the same way as if you bring a new junior engineer onto the team,” he said. “Over time, they get better and better, and they learn how the team works, and they adapt to the way the team is working and then they’re able to be more effective.”

## Kiro Autonomous Agent: Your Virtual Developer

The Kiro autonomous agent maintains persistent context across sessions and continuously learns from pull requests and feedback. It can handle tasks ranging from triaging bugs to improving [code coverage](https://thenewstack.io/ai-testing-more-coverage-fewer-bugs-new-risks/), with a single change spanning multiple repositories, AWS said.

Developers can ask questions, describe tasks, or assign work from their backlog directly through GitHub. The agent independently determines how to complete the work, sharing changes as proposed edits and pull requests so developers maintain control over what gets incorporated.

“The idea would be that you can give it a straightforward mission like, monitor my GitHub for issues, and as they arise, resolve them and submit pull requests,” Patel explained. “You can imagine coming in in the morning, overnight, the agent has looked at 10 different issues, submitted 10 different pull requests, and you can then decide if you want to merge those or not.”

The agent integrates with repos, pipelines, and tools like [Jira](https://thenewstack.io/why-developers-hate-jira-and-what-atlassian-is-doing-about-it/), [GitHub](https://thenewstack.io/github-loses-its-ceo-and-independence/), and [Slack](https://thenewstack.io/slack-takeaways-from-this-weeks-service-outage/), maintaining context as work progresses. Every code review, ticket, and architectural decision informs the agent’s understanding, making it more useful for the team over time.

## AWS Security Agent: Shifting Security Left

Security teams face a dual challenge: proactively identifying risks throughout development while reacting quickly when issues emerge. Current tools often provide generic recommendations, and penetration testing can take so long that it can’t keep up with fast-moving development teams, Patel said.

AWS Security Agent embeds security expertise throughout the development lifecycle, proactively reviewing design documents and scanning pull requests against organizational security requirements and common vulnerabilities, he noted. Organizations define their security standards once, and the agent automatically validates them across applications during reviews.

“What we’re doing with the security agent is we’re actually bringing the Security Agent into the early part of the development lifecycle,” Patel said. “So, when you’ve done your design documentation, when you’re starting to code, when you’re submitting your first pull requests, the security agent can be there in the background looking.”

The agent also transforms [penetration testing](https://thenewstack.io/penetration-testing-with-kali-linux-as-a-docker-container/) from a manual process that takes weeks into an on-demand process that completes in hours. It returns validated findings with remediation code to fix the issues it finds. If multiple apps are deployed simultaneously, teams can scale the number of agents to meet demand.

[SmugMug](https://www.smugmug.com/), a SaaS platform for photographers, added AWS Security Agent to its automated security portfolio to transform its security testing approach.

“AWS Security Agent helped catch a business logic bug that no existing tools would have caught, exposing information improperly,” said [Andres Ruiz](https://www.linkedin.com/in/andres-ruiz-torres-57514040/), staff software engineer at SmugMug, in a statement. “To any other tool, this would have been invisible. But the ability for the security agent to contextualize the information, parse the API response, and find the unexpected information there represents a leap forward in automated security testing.”

## AWS DevOps Agent: Always-On Operations

When an application goes down, everything stops. Modern distributed applications — with [microservices](https://thenewstack.io/introduction-to-microservices/), cloud dependencies, and [telemetry](https://thenewstack.io/telemetry-pipelines-collectors-and-agents-whats-the-difference/) spread across multiple tools — make it increasingly difficult to isolate issues and understand system behavior.

AWS DevOps Agent delivers what AWS calls “fewer alerts and more sleep” through always-on incident triage, guided resolution, and recommendations for continuously improving application reliability and performance across AWS, multicloud and hybrid environments.

“If you’re an on-call engineer at Amazon and your service has operational issues, you’re going to be woken up at two o’clock most nights,” Patel said. “And if you have an agent that can essentially proactively deal with issues and problems that they see in the logs or in the dashboards, you’re gonna get more sleep.”

The agent responds instantly to issues, using its knowledge of application architecture and the relationships between components to find root causes. It learns resources and their relationships spanning observability tools like Amazon CloudWatch, Dynatrace, [Datadog](https://thenewstack.io/is-datadog-becoming-a-platform-engineering-company/), [New Relic](https://thenewstack.io/new-relics-intelligent-observability-platform-is-ambitious/), and [Splunk](https://thenewstack.io/understand-kubernetes-and-containers-with-splunk-observability-cloud/), plus runbooks, code repositories, and [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) pipelines.

“The idea would be that it will constantly monitor your dashboards. It will have full access to all your runbooks,” Patel said. “It will be able to detect trends that could potentially lead to outages and take some action to correct it, and it will do all of that proactively.”

The agent also analyzes patterns across historical incidents to provide targeted recommendations that strengthen observability, infrastructure optimization, deployment pipeline enhancement and application resilience, AWS said.

The company also said Commonwealth Bank of Australia, one of Australia’s leading providers of integrated financial services serving over 17 million customers, prototyped AWS DevOps Agent on a complex network and identity management issue that typically takes experienced DevOps engineers hours to identify. The agent found the root cause in under 15 minutes.

“AWS DevOps Agent thinks and acts like a seasoned DevOps engineer, helping our engineers build a banking infrastructure that’s faster, more resilient, and designed to deliver better experiences for our customers,” said [Jason Sandry](https://www.linkedin.com/in/jason-sandery-84752b2/?originalSubdomain=au), head of cloud services at Commonwealth Bank of Australia, in a statement. “This isn’t just about faster resolution times — it’s about maintaining the trust our customers put in us.”

The agent will also prevent outages, Patel told The New Stack.

“It will be able to detect trends that could potentially lead to outages and say, ‘okay, I’m seeing this on the dashboard, or I’m seeing this in the logs, I’m going to take some action to correct it,’ and it will do all of that proactively,” he said. “So essentially, it may, in fact, either avoid an outage, or if an outage happens, it will detect it very early and it will solve it.”

## Addressing the Full Lifecycle

AWS designed the three agents to work across the software development lifecycle rather than solving just one piece and creating bottlenecks elsewhere, Patel said.

“The reason we’re looking across the lifecycle is that we wanted to make sure that we weren’t just solving one piece of it and then having bottlenecks in other parts of the lifecycle,” he said.

The agents can learn not just from code or explicit instructions but from understanding how teams work. Integrations with Slack, Jira and GitHub allow the agents to observe team interactions and pick up tasks without being told to do specific subtasks.

AWS has been testing the agents internally throughout 2025, with different engineering teams using them as part of their workflows to help improve the products, Patel said.

All three frontier agents are available today in preview. Early adopters include Commonwealth Bank of Australia, SmugMug, Western Governors University, and [Presidio](https://www.presidio.com/).

## Replacing Engineers?

While Patel mentioned the impact of the frontier agents on junior engineers, he argued that the agents will likely not replace them but make those engineers more productive.

“If you have 100 issues coming in on your repo and you don’t have the engineers to essentially deal with all 100 of those, and you need your engineers focused on building new features and new value-added capabilities to your application,” having one of these agents in the background looking at those 100 issues and being able to submit pull requests without you having to worry about them is actually big productivity gain for the team, Patel said.

“It allows the team itself to focus on the more value-added stuff that customers are interested in,” he added.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)