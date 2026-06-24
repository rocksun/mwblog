AWS has launched a native iOS app for [Kiro](https://thenewstack.io/kiro-requirements-analysis-automated-reasoning/), its [AI-powered development environment](https://thenewstack.io/agentic-ai-is-quickly-revolutionizing-ides-and-developer-productivity/), giving developers a way to monitor, steer, and approve agentic coding sessions from their phones, with no laptop required.

The app, announced at the [AWS New York Summit](https://aws.amazon.com/events/summits/new-york/), lets developers start sessions, review diffs, and approve changes while away from their desks. Compute runs in AWS’s cloud backend, meaning a session kicked off from a phone continues running even after the screen goes dark.

“There’s this little quote-unquote developer anxiety of like, I want to go back to my agent and do stuff,” [Darko Mesaros](https://www.linkedin.com/in/darko-mesaros/), Principal Developer Advocate for Kiro at AWS, tells *The New Stack*. “Developers were asking for a way to interact with these agents.”

The release reflects a broader shift in how AWS thinks about agentic development, he notes. “As [autonomous agents](https://thenewstack.io/ai-agents-database-challenge/) take on longer-running tasks across multiple repositories, the bottleneck moves from writing code to managing the agents doing the writing. Kiro Mobile is designed to keep developers in the loop without chaining them to a workstation,” Mesaros says.

“Kiro now lets you delegate, walk away, and come back to a PR,” writes [Kyle Seaman](https://www.linkedin.com/in/kyleseaman/), Principal Product Manager for Kiro, in a blog post about the release. “Continue a spec-driven workflow and let Kiro pick up where you left off. Or kick off an autonomous session from your phone or the web and Kiro runs independently in the cloud sandbox, inspecting files, and running tests. When Kiro needs your input, it pauses. You respond from wherever you are, pick a direction, and the work continues from where it left off.”

## Three modes, one agent

The app supports the same three session modes available on Kiro Web: Chat, for quick queries; Spec, for requirements-driven workflows; and Autonomous, for fully delegated tasks. Sessions started on the web surface automatically in the mobile app, with the same identity, model preferences, and connected repositories.

Diffs render as native red and green cards with file headers, designed for readability on a small screen. PR and code review status appears on every session row. AWS built the experience natively rather than adapting its web interface for mobile. Mesaros was direct about this.

“Instead of a relatively clunky web interface, it’s a native application for the iPhone,” he says.

## Spec-driven as the foundation

The iOS launch arrives alongside AWS bringing spec-driven development to Kiro Web, a workflow the company describes as central to how engineers build software internally.

Rather than prompting an agent to implement a feature and hoping for the best, spec-driven development asks the agent to first produce a requirements document, a design document, and a task list. The developer reviews and approves those artifacts before the agent writes a line of code.

“Spec-driven development is the solution to AI coding slop,” Mesaros explains. “It’s a contract between the agent and the developer. It keeps these agents from wandering off and making changes to stuff they shouldn’t necessarily be making.”

Mesaros said roughly 80% of AWS software engineers currently use Kiro, with spec-driven workflows built into that practice. Kiro automates the generation of design docs and requirements specs, reducing the manual overhead that historically made the spec-driven development difficult to sustain, he notes.

## Availability

Kiro Mobile is available in preview on iOS 26 and later for Kiro Pro, Pro+, Pro Max, and Power subscribers. Sign-in is supported via Google, GitHub, IAM, or AWS Builder ID. The company did not set a general availability date.

Android support is not currently planned. AWS said it made the iOS-first decision based on developer requests submitted through GitHub issues and Discord, and that it would evaluate Android based on future demand.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)