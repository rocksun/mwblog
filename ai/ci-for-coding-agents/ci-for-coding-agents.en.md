For years, integration tests have lived inside CI pipelines, triggered on push and answered ten, twenty, or thirty minutes later. That worked when humans pushed code. It doesn’t work now: [developers are driving coding agents](https://thenewstack.io/claude-code-agent-view/) that iterate in seconds, and the round trip to a remote pipeline is too slow to fit inside the loop where the work is happening.

> “Developers are driving coding agents that iterate in seconds, and the round trip to a remote pipeline is too slow to fit inside the loop where the work is happening.”

Recently, we’ve been rethinking what integration testing should look like in this new world. What we landed on is something we’re calling plans: small, agent-pickable, end-to-end checks that run inside the agent’s session against a real integration environment.

## The two-loop tax

Validation has traditionally been split into two loops:

* **Inner loop**: local dev, unit tests, docker-compose. Fast feedback, partially synthetic.
* **Outer loop**: CI pipelines, on push, against staging. Higher fidelity, ten minutes at least for a verdict.

For agents, that round trip is too long to be useful. An agent writes a change in seconds and can’t wait fifteen minutes for a remote verdict, so it ships from the inner loop. The only validation it runs is whatever the inner loop can provide, which, in most cases, is partial and mocked. The burden of verifying the code works against the full system is handed off to a developer, leaving the loop open.

A natural reach is to put the agent inside [CI itself](https://thenewstack.io/introduction-to-ci-cd/). Let it author pipelines, generate test stubs, and react to failures. That direction is right, and that’s where this is going. But the primitive that makes agent-in-CI work is the same one the inner loop needs first: a unit of validation small enough for an agent to author, select, and run against a real environment in seconds.

Build that primitive, and the inner loop can call it directly during authoring. The outer loop can call the same thing on push. The developer’s agent can reach into CI as a verification library instead of waiting on a remote pipeline. We start at the inner loop because that’s where the time-to-verdict bottleneck binds hardest today, but the same primitive is what lets the loops collapse into one.

## Environments are no longer the hard part

The first piece of the answer is something people are already doing in the inner loop today: ephemeral, on-demand environments that are isolated, scoped per run, and provide access to real downstream services and dependencies in a way that can scale to meet agent demand. I’ve written about how to build these [on The New Stack before](https://thenewstack.io/using-istio-or-linkerd-to-unlock-ephemeral-environments/), and the pattern is broadly applicable.

What matters here is the property it gives you: **an integration environment with production-grade fidelity, available on demand, scoped to the work being done.** An agent can summon one in seconds, validate against it, and tear it down when it’s no longer needed.

![A real-fidelity environment, summoned per run, scoped to the work being done.](https://cdn.thenewstack.io/media/2026/05/4b2a2693-1-1024x484.png)

## Workflow matters too

Environments are necessary, but not sufficient. The other half of integration testing, the question of how validation gets *defined*, selected, run, and reacted to, is where the pre-agent assumptions are most deeply baked in. Integration testing today runs in pipelines: heavyweight artifacts designed to run far away with elaborate bootstrapping, on push triggers, against a fixed set of steps. None of that is reachable from inside an agent’s session.

So the question becomes: what should the right primitive look like? It would need to be small enough to live inside an agent’s working session, but real enough to catch integration bugs against the live cluster. Something the agent can author in seconds, a human can review, and the team can keep around and reuse. Closer to a function the agent calls when it needs to than a pipeline that runs on its own schedule.

We call that primitive a **plan**.

## Actions & plans

A plan is a small two-layer system. It’s easier to explain by drawing the layers.

![Workflow diagram of the layers between agent plans and actions](https://cdn.thenewstack.io/media/2026/05/6accb923-2-1024x471.png)

### Actions

Typed, deterministic building blocks. This should be a familiar shape if you’ve used GitHub Actions or any other workflow runner. Two things worth flagging:

* **They run against real infrastructure inside an integration environment**, not against mocks. `request-http` hits a live endpoint, `playwright` drives a real browser, k6 loads a real service.
* **They’re described in markdown.** Each action’s interface, inputs, and usage are documented inline, so a planning agent can read the action like a developer reading docs and compose unfamiliar ones correctly on the first try.

### Plans

A plan is a DAG (directed acyclic graph) compiled from actions, stitched together to validate one user-visible behavior end-to-end. These are intended to be authored by agents. The bits worth pointing out:

* **Authored in [natural language.](https://thenewstack.io/sentrys-seer-agent-debug/)** A developer or agent describes the behavior they want validated (“walk the ride-request flow and assert that the itinerary shows both location names”), and a planning agent produces the DAG.
* **Selection hint.** Every plan carries a prose description of what it validates. When a change comes in, an agent reads the hints across the catalog and selects the right plan for the diff.

Here’s an example:

```

spec:
  selectionHint: "End-to-end ride-request check for HotROD: pick pickup +
    dropoff in the React app, request a ride, assert the resulting
    itinerary shows both location names."
  steps:
  - id: e2e_ride
    action: { actionID: &lt;playwright-action-id> }
    args:
      values:
        script: |
          test('itinerary shows pickup and dropoff', async ({ page }) => {
            await page.goto(process.env.BASE_URL + '/');
            await page.getByRole('button', { name: 'Request Ride' }).click();
            await expect(page.locator('.itinerary')).toContainText("Rachel's Floral Designs");
          });

```

### Why plans work for the inner loop

Each plan covers one user-visible behavior end-to-end, not a pipeline or a full test suite. That makes it small enough to fit inside an agent’s session, and easy for the agent to pick the right one via `selectionHint`.

A diff touching the ride-request path runs the one or two plans that cover it, not anything about billing or auth. The environment underneath is real, so the answer that comes back is useful, in seconds, before the PR is ever opened.

## How this works in practice

This example uses the [HotROD rideshare demo app](https://github.com/signadot/hotrod), a modified version of the one created by Jaeger. It simulates a ride-hailing backend on Kubernetes with four Go services. The frontend orchestrates calls to the location, driver, and route services, backed by Redis, MySQL, and Kafka.

An agent renames a Go struct field on the location service: `Name` becomes `LocationName`. The kind of refactor that compiles, passes unit tests, and looks done.

![Example screenshot of an agent renaming a Go struct field on the location service.](https://cdn.thenewstack.io/media/2026/05/6890afa2-3-1024x471.png)

*The change as the agent sees it. The integration break is invisible from here.*

Before opening a PR, the agent picks the existing ride-request plan from the catalog via its selection hint and runs it. The plan is a Playwright check that walks through the booking flow in a real browser against an ephemeral environment that contains the modified service.

It fails. The frontend still reads Name from the JSON. The field is gone, the itinerary renders empty, and the assertion fails.

![Example of a structured report of which assertion failed, and what was captured along the way.](https://cdn.thenewstack.io/media/2026/05/b100963b-4-1024x423.png)

*The failure as the agent sees it: a structured report of which assertion failed and what was captured along the way.*

The agent reads the failure, traces it to the contract, finds the frontend as the affected consumer, edits four files there, and re-runs the plan.

It passes. The PR that opens is already validated against the real cluster.

![Screenshot of the final report, which as the agent sees it, has passed.](https://cdn.thenewstack.io/media/2026/05/b2c141ef-5-1024x606.png)

*Final report. The fix has propagated to the consumer, and the diff lands on the reviewer already passing.*

## What this changes about the SDLC

Validation moves up. Integration tests that used to run when CI got around to them now run in the agent’s session, against a real cluster, before the PR is ever opened. Bugs that used to surface in staging (locally correct, systemically broken) get caught and fixed within a single-agent loop. Staging goes back to being a final sanity check rather than the primary test bed.

The engineer driving the agent feels the shift first. Validation that used to mean waiting on CI now arrives inside the authoring session, so integration failures surface while the engineer and the agent are still working on the code together, not after the loop has closed. A downstream review, either by the engineer themselves or by a teammate, becomes a review of behavior rather than a stand-in for validation. What lands in front of human eyes is a diff already passing against the real cluster, with an environment URL and a plan run anyone can audit.

Over time, the team builds up a versioned library of plans. Each plan is a small description of what “correct” means for one behavior. The library ends up doubling as a reference that agents validate against, and humans can read to understand the system.

> “As agents compress code generation into seconds at one end of the pipeline, leaving integration validation pinned to the outer loop turns CI into a growing backlog rather than a feedback mechanism.”

We feel that this is a necessary shift. As agents compress code generation into seconds at one end of the pipeline, leaving integration validation pinned to the outer loop turns CI into a growing backlog rather than a feedback mechanism. The verdict has to arrive while the agent is still in the loop, or the gap between code generated and code shipped will keep widening for cloud-native teams.

## How we shipped this: agent skills

The primitives above describe what validation needs to look like for agents. The question is how an agent reaches for them. Agent skills are the right form factor: scoped, loadable instructions that Claude Code, Cursor, Codex, and other modern harnesses already pick up as first-class extensions.

Skills made sense for a few reasons. They live where the agent already works, so Claude Code, Cursor, Codex, and most modern harnesses load them as a first-class extension. They’re narrow on purpose: authoring a plan and running one are different kinds of work, and splitting them keeps each skill small enough that the agent can pick the right tool without ambiguity.

The plan workflow ships as two skills, split by the shape of the work:

[`signadot-plan`](https://www.signadot.com/docs/integrations/coding-agents/agent-skills#signadot-plan?utm_source=tns&utm_medium=sponsorship&utm_campaign=q2_26_sponsored_content) handles authorship. A developer or agent describes the behavior they want validated, and the skill produces a draft plan, composed from the action catalog, ready to review and commit alongside the code.

[`signadot-validate`](https://www.signadot.com/docs/integrations/coding-agents/agent-skills#signadot-validate?utm_source=tns&utm_medium=sponsorship&utm_campaign=q2_26_sponsored_content) is the runner. It reads the diff, picks the right plan via selection hints, spins an ephemeral environment, runs the plan against the real cluster, and surfaces failures the agent can act on.

Splitting them keeps each skill small enough that the agent picks the right one without ambiguity. The [plan-based validation quickstart](https://www.signadot.com/docs/tutorials/quickstart/plan-based-validation?utm_source=tns&utm_medium=sponsorship&utm_campaign=q2_26_sponsored_content) walks the example above end-to-end.

The skills run inside the agent’s session today, which is where the bottleneck has been. The same primitive extends the other way: the same plans can run in CI on push, against the same ephemeral environments, as a backstop for anything the inner-loop check missed. More on that another time.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/10/3796d92e-cropped-e856ab4f-anirudh-ramanathan.jpg)

Anirudh Ramanathan is CTO of Signadot where he focuses on cloud native development. Prior to this, he worked at Google focusing on Kubernetes core controllers and extensibility. He's also a committer on the Apache Spark project with a focus on...

Read more from Anirudh Ramanathan](https://thenewstack.io/author/anirudh-ramanathan/)