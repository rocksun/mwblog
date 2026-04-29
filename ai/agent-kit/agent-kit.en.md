![Agent Kit — storage primitives for AI agents on Tigris](/blog/assets/images/hero-img-58f7f68426b7bcd6174fba2fa2c01ef8.webp)

**[Forks.](#forks)** Give every agent its own writable copy of the same dataset in one function call, with one storage bill and zero risk of contaminating the source.

**[Workspaces.](#workspaces)** Hand an agent a scratch bucket it can't escape, and stop paying for it the moment its TTL expires — even if nobody remembers to clean up.

**[Checkpoints.](#checkpoints)** Pin an exact moment in a bucket's history so you can replay what an agent saw when things went wrong, without freezing live data.

**[Coordination.](#coordination)** Trigger the next stage of a pipeline the instant an object lands, with no polling loops, cron jobs, or glue services to keep running.

[**`@tigrisdata/agent-kit`**](https://www.npmjs.com/package/@tigrisdata/agent-kit)
is a new TypeScript SDK for the storage workflows AI agents actually need. Four
primitives — forks, workspaces, checkpoints, coordination — each with a
`teardown` that cleans up credentials and storage. No dangling keys, no
half-provisioned state.

Tigris already gives you the primitives: buckets, scoped access keys, snapshots,
object notifications. Agent Kit composes them into the four workflows that every
agent system ends up rebuilding from scratch.

## The gap between object storage and agent workflows[​](#the-gap-between-object-storage-and-agent-workflows "Direct link to The gap between object storage and agent workflows")

Object storage is low-level on purpose. A bucket is a namespace for keys. Put an
object, get an object, list keys under a prefix. That surface is the right level
when you're building a CDN or a backup system. It's the wrong level when you're
building agents, where the requests sound like:

* "Give me a writable copy of the training set. If the agent messes it up, throw
  it away."
* "Spin up a scratch bucket I can write into. Delete it in 24 hours."
* "Mark the state of this bucket right now so I can come back to it."
* "When someone else finishes writing to `stage-1/`, wake me up."

Each is three to five API calls against `@tigrisdata/storage` and
`@tigrisdata/iam`. For fifty parallel agents, that's a lot of code to get right.
The failures are mundane: forgotten access keys, unset TTLs, scratch buckets
that quietly bill for a year.

[**Agent Kit is our answer to that gap.**](https://www.tigrisdata.com/docs/ai/agent-kit/)
Four primitives that match how agent systems are actually structured, each one
composed from the underlying storage and IAM APIs you already have.

@tigrisdata/agent-kitForksWorkspacesCheckpointsCoordination@tigrisdata/storage@tigrisdata/iam

## The four primitives[​](#the-four-primitives "Direct link to The four primitives")

Each primitive composes a few storage and IAM calls into one function with a
matching teardown.

### Forks: give every agent its own copy of a dataset[​](#forks "Direct link to Forks: give every agent its own copy of a dataset")

![A fleet setting out together — every fork sends an agent off with its own writable copy of the same dataset.](/blog/assets/images/sailing-d6eae0f3be05ca29b171b3dde6d3538d.webp)

Forks are copy-on-write clones of a bucket. Create a fork, and you get a new
bucket that shares the underlying data with the source but diverges the moment
either side writes. Fifty forks don't cost fifty times the storage. They cost
one times the storage plus whatever the forks produce.

The source bucket needs snapshots enabled. For new buckets, use
`createWorkspace({ enableSnapshots: true })` or
`tigris buckets create --enable-snapshots`. Checkpoints have the same
requirement.

Doing this by hand is one snapshot of the source plus two calls per fork —
create a bucket from the snapshot, mint a scoped access key — and a matching set
of revoke-and-delete calls when you're done. For fifty agents, that's over a
hundred API calls against `@tigrisdata/storage` and `@tigrisdata/iam`, each with
its own error path you have to wire together. Agent Kit still makes those calls
under the hood — it just composes them, so you write one function instead of the
orchestration around it:

```
import { createForks, teardownForks } from "@tigrisdata/agent-kit";  
  
const { data: forkSet, error } = await createForks("training-data", 50, {  
  credentials: { role: "Editor" },  
});  
if (error) throw error;  
  
  
await Promise.all(  
  forkSet.forks.map((fork) => {  
      
    if (!fork.credentials) return;  
    return runAgent(fork);  
  })  
);  
  
  
await teardownForks(forkSet);  

```

Scoped credentials are first-class

Pass `credentials: { role: "Editor" }` or `"ReadOnly"` and Agent Kit mints one
IAM key per fork, scoped to that fork bucket only. A leaked key scopes the blast
radius to one agent, not the whole dataset.

If one fork in the batch fails to create, `createForks` stops and returns the
ones that succeeded along with the snapshot ID, so you can retry or tear down
the partial result. The failed fork's error doesn't surface in the returned
data; if you need to know exactly which one tripped, instrument the call or
inspect the snapshot directly. Teardown is best-effort: it continues through
failures and reports every error in a single aggregated result. Agent systems
fail partially, and the API is shaped around that.

### Workspaces: scratch buckets that clean themselves up[​](#workspaces "Direct link to Workspaces: scratch buckets that clean themselves up")

![Claiming a beachhead — a workspace is a staked-out scratch bucket the agent writes into before moving on.](/blog/assets/images/beachhead-6ed495ca6289efa9bc3b53b4c3ab567e.webp)

Forks are for sharing a starting dataset across agents. Workspaces are for an
agent that needs its own empty bucket — intermediate outputs, generated
artifacts, per-session state. Think of the difference as fork vs. `mkdir`: both
are about isolation, but one starts from a dataset and the other starts from
nothing.

```
import { createWorkspace, teardownWorkspace } from "@tigrisdata/agent-kit";  
  
const { data: workspace, error } = await createWorkspace("agent-session-xyz", {  
  ttl: { days: 1 },   
  enableSnapshots: true,   
  credentials: { role: "Editor" },   
});  
if (error) throw error;  
  
  
  
if (!workspace.credentials) {  
    
}  

```

Under the hood, that's still three calls — create bucket, set TTL, mint
credentials — with three separate failure modes. Agent Kit composes them, so you
write one function and check one result instead of orchestrating the sequence
yourself.

The TTL field pays for itself

`ttl` is the option that most commonly gets forgotten when you do this by hand,
and it's the one that turns a one-off agent run into a slow-leaking storage
bill. Setting it here means a workspace you never tear down still stops costing
money after a day.

### Checkpoints: mark a bucket's state before risky work[​](#checkpoints "Direct link to Checkpoints: mark a bucket's state before risky work")

When an agent does something surprising, the question you want to answer is
"what was in the bucket when the agent read from it?" Without checkpoints, you
can't answer it. The bucket now contains whatever the agent overwrote on top of
whatever anyone else changed in the meantime.

Checkpoints are named snapshots. Take one before a risky operation, keep going.
If things go sideways, restore the checkpoint into a fresh fork and investigate.
The original bucket stays untouched:

```
import { checkpoint, restore } from "@tigrisdata/agent-kit";  
  
const { data: ckpt, error: ckptErr } = await checkpoint("training-data", {  
  name: "before-fine-tune",  
});  
if (ckptErr) throw ckptErr;  
  
  
  
const { data: investigation, error: restoreErr } = await restore(  
  "training-data",  
  ckpt.snapshotId,  
  { forkName: "debug-fine-tune-attempt" }  
);  
if (restoreErr) throw restoreErr;  
  

```

Restore uses the same copy-on-write machinery as forks, so it's instant even for
terabyte-scale buckets. You can restore the same checkpoint into multiple forks,
run different agents against them, and compare results without paying for
multiple copies of the data.

### Coordination: trigger the next stage on object events[​](#coordination "Direct link to Coordination: trigger the next stage on object events")

![A camp struck and the signal given — each stage of an agent pipeline wakes the next when it finishes writing.](/blog/assets/images/tent-8526863543d711d9635f25f050935a72.webp)

Multi-agent systems need a way for stages to trigger each other without polling
or running another scheduler. Tigris buckets already fire webhooks when objects
change, and Agent Kit wraps that in a primitive shaped like an agent pipeline
stage:

```
import { setupCoordination, teardownCoordination } from "@tigrisdata/agent-kit";  
  
const { error } = await setupCoordination("pipeline-bucket", {  
  webhookUrl: "https://orchestrator.example.com/hook",  
  filter: 'WHERE `key` REGEXP "^results/"',  
  auth: { token: process.env.WEBHOOK_SECRET },  
});  
if (error) throw error;  

```

When any agent writes to `results/` in that bucket, the orchestrator gets a
POST. No polling loop or queue to stand up; the next stage runs when the
previous stage finishes writing.

Webhook delivery is at-least-once with retries on `5xx`. Make your endpoint
idempotent, or let the next stage deduplicate on object key.

## Composing the primitives in one agent run[​](#composing-the-primitives-in-one-agent-run "Direct link to Composing the primitives in one agent run")

The primitives are designed to stack. Here's a multi-agent eval run that pins
the corpus's known-good state, forks it for parallel runs, and wakes the
orchestrator the moment any agent drops a report:

```
import {  
  createForks,  
  teardownForks,  
  checkpoint,  
  setupCoordination,  
} from "@tigrisdata/agent-kit";  
  
  
  
const { data: baseline, error: ckptErr } = await checkpoint("training-data", {  
  name: "pre-eval-baseline",  
});  
if (ckptErr) throw ckptErr;  
  
  
const { data: forkSet, error: forkErr } = await createForks(  
  "training-data",  
  5,  
  { credentials: { role: "Editor" } }  
);  
if (forkErr) throw forkErr;  
  
  
await setupCoordination("eval-reports", {  
  webhookUrl: "https://orchestrator.example.com/eval-complete",  
  filter: 'WHERE `key` REGEXP "^reports/"',  
  auth: { token: process.env.WEBHOOK_SECRET },  
});  
  
  
await Promise.all(forkSet.forks.map((fork) => runEvalAgent(fork)));  
  
  
  
await teardownForks(forkSet);  

```

This is the shape most multi-agent runs end up in. The primitives stay close to
their underlying storage and IAM calls, so when a step fails you can reason
about what actually got provisioned and what didn't. If your agents don't need a
starting dataset and just need empty scratch space, swap `createForks` for
`createWorkspace` — same lifecycle, different starting point.

## Which primitive fits which job[​](#which-primitive-fits-which-job "Direct link to Which primitive fits which job")

Use this table as a quick decision guide:

| Scenario | Primitive |
| --- | --- |
| N agents need the same starting dataset but divergent writes | Forks |
| One agent needs an empty scratch bucket with a TTL | Workspaces |
| Mark a known-good state before a risky operation | Checkpoints |
| Stage B should run when stage A writes to a prefix | Coordination |

## Where Agent Kit fits in your stack[​](#where-agent-kit-fits-in-your-stack "Direct link to Where Agent Kit fits in your stack")

LangGraph has a checkpointer. OpenAI Assistants has threads and file search.
Bedrock Agents has session memory. **Agent Kit sits a layer below all of them**
— at storage and credentials, not at state machines or prompts. Your LangGraph
checkpointer persists graph state; an agent-kit checkpoint snapshots the bucket
that graph is reading from. Your OpenAI Assistant has a thread; an agent-kit
workspace is the private scratch bucket that assistant writes artifacts into.
Use Agent Kit alongside whatever framework you're already on, not instead of it.

## A thin layer over storage and IAM[​](#a-thin-layer-over-storage-and-iam "Direct link to A thin layer over storage and IAM")

Agent Kit is a handful of composed workflows that sit below whatever framework
you're already using — LangChain, CrewAI, your own, or something that doesn't
exist yet. It isn't trying to replace any of them.

Today the whole package is under six hundred lines of TypeScript. As we add more
composite workflows, the design rules stay the same: every function returns
`TigrisResponse<T>` — a discriminated union of `{ data }` or `{ error }`, no
exceptions; every `create*` or `setup*` has a matching `teardown`; config maps
to both storage and IAM.

Agent tooling has a habit of over-abstracting: libraries hide what they're
doing, which is fine until something breaks and you need to know exactly which
API calls ran in what order. Agent Kit stays close to the primitives, so every
function maps to one or two underlying storage or IAM calls and you can reason
about a failure when it happens.

## Install Agent Kit[​](#install-agent-kit "Direct link to Install Agent Kit")

```
npm install @tigrisdata/agent-kit  

```

Credentials come from the environment, shared with `@tigrisdata/storage` and
`@tigrisdata/iam`:

```
TIGRIS_STORAGE_ACCESS_KEY_ID=tid_...  
TIGRIS_STORAGE_SECRET_ACCESS_KEY=tsec_...  

```

Or pass them inline via the `config` parameter on any function. Full API
reference, per-primitive guides, and failure-mode notes live in the
[Agent Kit documentation](https://www.tigrisdata.com/docs/ai/agent-kit/).

Agent Kit is published as `0.1.x`. The API is usable today but may evolve before
1.0 — pin the version if you need stability. Feedback on the abstractions is
welcome on [GitHub](https://github.com/tigrisdata/storage/issues).

Source lives in the
[`tigrisdata/storage`](https://github.com/tigrisdata/storage) monorepo under
`packages/agent-kit`, MIT-licensed. If you want to add a primitive, fix a bug,
or tell us we got the abstraction wrong, PRs are welcome.

Give your agents storage primitives that match how they actually work

Install @tigrisdata/agent-kit and replace a hundred API calls worth of scaffolding with four functions. Your first 5 GB on Tigris are free.