**Every Claude Code user has watched** a new session start from zero. You open it on a system you built last week, ask for a small feature, and the agent begins by rediscovering your own architecture: which service owns the data, which frontend calls it, which type the two of them share. The conversation that explained all of that is gone or compressed into a summary, and the source files show what exists without saying what depends on what.

So far, the main answer is memory. Claude Code loads CLAUDE.md instructions and its own auto-memory notes at the start of every session, and since September 17, the redesigned Projects, in beta in Claude Code cloud sessions, keep a shared memory across threads, so Claude can recall that “the release moved to Friday” or “who to check in with before touching the billing service.” I wanted to test a different source of context: the dependency records a build platform writes when it creates each version of a component.

*Disclosure: I’m an engineer at Bit Cloud, a platform that builds, hosts, and deploys even a single app from its first component, with coding agents working on it over MCP. I asked Claude to build on it to see what an agent can do when the platform records each part and its dependencies as they are versioned. The project and its build records are public.*

## **What can a fresh session recover without memory?**

The system was a small support console I had built with Claude Code earlier, and I wrote up [how I built and deployed it](https://dev.to/nachoaldamav/how-i-built-and-deployed-a-support-platform-with-claude-code-k) separately. The prompt that started that build mentioned tooling in two words, “using Bit”, and otherwise described the product. It has four components: a React app, an Express service backed by MongoDB, a shared ticket entity, and a [platform component that puts the app and the service behind](https://thenewstack.io/agent-runtime-application-server/) one gateway. All four are versioned in [a public scope](https://bit.cloud/bit-oss/support), bit-oss.support, and the console runs in production over HTTPS.

To test what the records alone could carry, I opened a fresh Claude Code session in an empty workspace, with no conversation history and no local code, and asked:

```
Add filtering by ticket status and assignee to the support console in bit-oss.support.
```

Claude checked the workspace and found no local components. Its next message was: “The workspace is empty, so the support console lives remotely. Let me read the bit-oss.support scope through the MCP.” It called `read\_scope` for `bit-oss.support`. That returned the four components and their dependencies. It then called `read\_components` for the app, service, and ticket entity, retrieving API references and file inventories before importing source or editing code.

The app and service both depended on the same version of the ticket entity. Its class documentation read, “shared between the support service and the agent-facing app,” and the API reference included that sentence. The project could supply this context without the original conversation.

Claude imported all four components with `bit import`, inspected the source, and implemented client-side filtering within the app. Validation reported 41 passing tests, including nine new filtering tests. MCP helped it discover the system; source inspection and tests established how to change it. The change stayed inside the app, leaving the shared ticket entity and the service alone. Knowing what is shared also tells an agent what not to touch.

## **Where did the records run out?**

They ran out at behavior. The app’s API reference does list the routes it calls, `GET /tickets`, `POST /tickets`, `PATCH /tickets/:id` and `POST /tickets/:id/comments`, in the documentation for a fake service it uses in tests, but nothing checks that list against the real service. The records told Claude which components shared the ticket contract; whether the routes on each side still matched had to be read by hand and tested.

A green build also proves less than it seems to. The MongoDB integration tests skip when their temporary database cannot start on the CI runner, so a passing build doesn’t show they ran. I checked persistence by hand: create a ticket, add a comment, restart the platform against the same database, and see that both are still there.

And this is a demo, with a predefined demo account and a public signing secret. Concurrency control, migrations, recovery procedures, and mandatory database tests are all still to do. That is ordinary engineering work, and it is where I want an engineer’s time to go.

## **Memory files or dependency records?**

Memory holds what someone chose to write down. In Claude Code, that means CLAUDE.md (or AGENTS.md) instructions a person writes, and auto-memory notes Claude writes from corrections and preferences, and the redesigned Projects add decisions, such as why an export was dropped, which no build system will ever record. Each note is accurate as of the moment it was written. Claude Code records each memory file’s write time, and its documentation explains why: “the timestamp shows how current the fact is.”

The build system writes a dependency record when it creates a component version, and it is part of that version. When the support app was versioned, the build system recorded its dependency on one specific version of the ticket entity, without anyone deciding it was worth noting, and the record cannot drift from the version it describes. And because `read\_scope` returns each component at its latest version, the records Claude read were current. A memory note carries the time it was written, but nothing ties it to a code version. In the test, the session had no conversation and no local code. The only memory in the workspace was the generic AGENTS.md that `bit new` writes, which tells the agent to look things up on the platform, and the records did the rest: they were enough to find the shared contract.

The two cover different ground and work best together: memory for intent, such as the release date, the person to ask, or why a feature was cut, and records for structure and meaning, which version of what depends on which. Nx serves its project graph to agents over MCP, and Sourcegraph serves code search and navigation across repositories; both do that well. For this test, I wanted something narrower: a record per component, written when its version was created, that still holds when the other side of a dependency lives somewhere the agent hasn’t indexed.

## **When should a team start?**

At the first component. The records in this test cost nothing extra, because they were written as each version was made, starting on day one. I had created the workspace with `bit new`, which supplied the Bit Cloud MCP connection in `.mcp.json` and an AGENTS.md with instructions for the agent, and at the start of the original build Claude used that connection to look through [an existing design-system scope](https://bit.cloud/bitdesign/sparks) for parts it could reuse; the four components now depend on 16 that already existed, ten of them from that design system. Rebuilding that map later, after one team renames a shared field and another finds out from its error logs, is the expensive version of the same work.

None of it requires our product; it just needs dependencies recorded wherever the work happens.

Agents can already reach production, and what they still lack, on every request after the first, is a view of the system they are about to change. That view is cheapest to build before the second component exists.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/10/9bb801a8-screenshot-2026-10-09-at-8.34.38-am-600x600.png)

Ignacio Aldama is an engineer at Bit Cloud. Bit Cloud gives a single project the build, CI, hosting and database it needs from its first component, and lets coding agents such as Claude Code, Cursor and Codex work on it...

Read more from Ignacio Aldama](https://thenewstack.io/author/ignacio-aldama/)