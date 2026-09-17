**Anthropic recently published its AI-Native SDLC Playbook**. Its central claim is that “code is no longer the bottleneck.” When agents can produce an implementation in minutes, the constraint moves to everything around the build phase: planning, review, verification, deployment, and governance.

The risk, if organizations get this wrong, is producing ten times the changes at the same quality per change or worse, with no way to identify which changes are the bad ones. The traditional answer is that a person looks at each one, and that is exactly what stops working at this volume.

> The risk… is producing ten times the changes at the same quality per change or worse, with no way to identify which changes are the bad ones.

The [playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) gets the foundations right. What it doesn’t capture is that an organization’s process has nuance: it is really a family of processes that vary with the change at hand, not a single flow every change travels through.

## **The spec-driven wave**

The playbook is part of a broader wave of spec-driven development tooling, including Amazon’s [Kiro](https://kiro.dev/) and GitHub’s [Spec Kit](https://github.com/github/spec-kit). The tools share a common shape. Written artifacts drive the work: an intent document becomes a spec, a plan, a diff, and review findings, all committed to version control. Policy is enforced by deterministic mechanisms such as hooks, rather than by instructions in a prompt. Agents check their own work before a human sees it. Humans own the approvals.

But each of these tools also prescribes a particular process: a fixed sequence of stages that produce fixed artifacts, and that every change travels through. Adopting the tool means adopting its process.

## **One organization runs many processes**

No real organization runs a single process. The right process for a change depends on the risk it carries and the accountability it requires. A documentation fix, a dependency upgrade, and a schema migration in a payments service should not travel the same path. They need different levels of verification, different approvers, and different records. In regulated domains, the process itself is part of the compliance obligation: auditors expect a record of who approved each change and based on what evidence. What must be recorded differs by the type of change.

> When a tool prescribes one process, teams route around it for changes that don’t fit, which is the worst outcome because the real process becomes invisible.

When a tool prescribes one process, teams route around it for changes that don’t fit, which is the worst outcome because the real process becomes invisible. Or the vendor keeps adding configuration until the tool becomes a workflow engine that nobody fully understands.

The tool should not prescribe a process. It should give the organization a way to define its own.

## **Processes as state machines**

A better model is to define each process as a state machine. The states are facts about a change: reviewed, validated against its dependencies, approved for production. Those facts live in systems no single tool owns: the repository, CI, the cluster, the tracker. So a process cannot be a program that executes steps. It is a set of rules that react to observations about those systems. Each rule specifies:

1. The facts it requires before it can fire.
2. Its gate: fire automatically, or wait for a person’s approval.
3. The permission it grants when it fires, such as merging or deploying.

The definition is this set of rules, stored as data and reviewed like code. An organization runs many small machines, one per risk class.

At runtime, this behaves nothing like a workflow engine. No component tracks “we are on step four”: the process advances when a fact appears in the system that owns it, and rules react. Events that arrive late, twice, or after a restart are handled like any other, because rules only react to current state. The gate is one of a rule’s conditions, so you can hold firing during an incident or a release freeze without editing any definition.

Gates need enforcement. A gate implemented as a prompt instruction depends on the model following it. The agent harness can provide the determinism required to run the state machine and enforce its gates, stopping the agent between actions until a gate is answered, while the infrastructure enforces the rest.

## **The process adapts to the change**

One fixed process definition per repository is not enough: every change in that repository would still travel the same path, regardless of its risk. The path a change takes should depend on what the change is, and this routing comes from classifying the change, not from the author choosing a path. The organization defines classification using signals it already has: the paths a change touches, the repository it lives in, a label on its tracking issue, etc.

The definitions themselves also need to change over time, and that has to be safe. Because a process definition is data, editing it is itself a change, and it goes through its own gated process. Loosening an approval gate on the release process gets reviewed the way a schema migration does, not edited the way a config file does.

![](https://cdn.thenewstack.io/media/2026/09/69869781-img_1-1024x481.png)





*Click to enlarge graphic.*

Concretely, consider three changes to the same service:

* **A documentation fix** is classified by the paths it touches. Its process has two states: the build passes, and it merges. No person is involved.
* **A dependency upgrade** skips design review, but its process requires compatibility evidence: the upgraded service runs its integration tests against real dependencies. A major version bump adds an approval that a patch bump does not.
* **A schema migration in the payments service** is classified by the component it touches, no matter what kind of change it claims to be. Its process adds states the others never see: review by a payments owner, validation against production-shaped data, and a release approval from someone accountable for that domain.

Each transition, in each path, is logged with who approved it and on what evidence.

## **Tenets**

The tenets these processes should follow:

* **Autonomy is granted per action, and grows over time.** Each transition is set to fire automatically, require approval, or hold. As agents prove reliable on a class of change, that setting is relaxed, so the process absorbs agent improvements without redesign.
* **Human attention is spent only where judgment is needed.** Agent effort keeps getting cheaper; supervision hours do not. A person is brought into the loop only when the decision requires human judgment, and is given the context to decide quickly.
* **Evidence comes from outside the agent.** An agent’s own report never moves a change forward. Transitions fire on facts from systems the agent cannot write to, such as test results and [validation in a realistic environment](https://thenewstack.io/enabling-autonomous-agents-with-environment-virtualization/).
* **The process record is the audit trail.** The definition is the written policy, and the transition log shows who approved each step, on what evidence, under which version of the policy.

## **Quality at scale**

The playbook and its peers get the foundations right. What is missing is the ability for an organization to define its own processes, vary them by the risk of each change, and evolve them safely. The goal is not fewer humans in the loop. It is spending human judgment only where it is needed, backed by evidence agents cannot produce about themselves, so that quality holds while throughput multiplies.

We are building these ideas at [**Signadot**](https://www.signadot.com/?utm_source=tns&utm_medium=sponsorship&utm_campaign=q3_26_sponsored_content) and acting as our own guinea pigs, running our own development through this process. If you’re experimenting with these ideas too, we’d love to talk!

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/10/3796d92e-cropped-e856ab4f-anirudh-ramanathan.jpg)

Anirudh Ramanathan is CTO of Signadot where he focuses on cloud native development. Prior to this, he worked at Google focusing on Kubernetes core controllers and extensibility. He's also a committer on the Apache Spark project with a focus on...

Read more from Anirudh Ramanathan](https://thenewstack.io/author/anirudh-ramanathan/)