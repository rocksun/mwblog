![Glowing laptop with eyes](https://cdn.thenewstack.io/media/2026/11/eb49a6c7-allison-saeng-p41rhm6ivjo-unsplash-1024x576.jpg)

Perplexity’s new Teammates can coordinate multiple agents, remember where previous sessions left off, and keep working without another prompt. The challenge is keeping everything in sync, especially when agents are working at the same time, sharing project state, and operating with different permissions.

[Announced Wednesday](https://www.perplexity.ai/en-GB/hub/blog/teammates-are-agents-for-complex-ongoing-work), Teammates builds on infrastructure Perplexity has spent much of the year developing. The launch puts that earlier work to use in workflows where agents can delegate tasks and continue operating across sessions.

## The challenge of keeping agents stateful

When [Nate Kupp](https://www.linkedin.com/in/natekupp/), Perplexity’s vice president of infrastructure, took *The New Stack* [inside the company’s agent sandboxes](https://thenewstack.io/perplexity-space-agent-sandboxes/), he described the difficulty of maintaining reliable systems at that scale.

“Stateful systems are incredibly hard to build,” Kupp said, pointing to the durability and uptime requirements of operating millions of sandboxes.

> “Stateful systems are incredibly hard to build”

Teammates relies on Perplexity Computer’s existing infrastructure, which separates persistent project state from individual execution environments. That allows agents to continue working on the same project without depending on a single uninterrupted session.

## Shared state lives in Git

In a [technical breakdown of its shared workspaces](https://www.perplexity.ai/en-GB/hub/blog/building-shared-workspaces-for-people-and-agents), the company described how it uses Git-backed repositories to keep project state intact across sessions. Each Computer project has its own repository, while agents work in separate sandboxes and submit their changes back to the shared project.

That gets more complicated when agents are working on the same code at once since if one agent commits its changes first, another may have to reapply its work against the latest version.

Perplexity says fewer than 2% of submissions are rejected because they’re based on outdated repository state. Median submission latency is under 1.7 seconds, while p99 stays below eight seconds.

> Median submission latency is under 1.7 seconds, while p99 stays below eight seconds.

Memory is handled separately through Perplexity’s Brain system, which keeps what agents have learned in dedicated repositories. That lets background agents update shared knowledge without interfering with changes to the project’s files.

## Pausing and forking agents

Perplexity built SPACE around Firecracker microVMs and Btrfs snapshots, making it possible to pause, resume, or fork agent sessions without losing their saved state.

With Teammates, developers can connect tools like Slack and GitHub and set up triggers that tell agents when to act. Perplexity hasn’t said much about what happens when that work gets stuck, particularly when one agent is waiting on another or acting on information that’s already out of date.

## The open permission questions

Each teammate runs in its own isolated environment and browser session, with access managed through Computer’s existing permissions and credentials handled securely through encryption. Users can also monitor progress and take control when needed.

It’s unclear how it prevents agents from accessing resources beyond their permissions when tasks are handed off. For enterprises, that uncertainty could influence how much autonomy they’re willing to give agents without requiring human approval.

Teammates is initially available on the web for Perplexity Max subscribers, with iOS support planned.

> Teammates is initially available on the web for Perplexity Max subscribers, with iOS support planned.

The post [Perplexity’s AI agents keep working after you close the tab](https://thenewstack.io/perplexity-teammates-agent-orchestration/) appeared first on [The New Stack](https://thenewstack.io).