**Earlier this month**, Vercel released [Agent Plugins 1.0.0](https://agent-plugins.org/specification) with core maintainers from AWS, Cursor, Microsoft, and OpenAI. [Google announced](https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/) the same day that it was joining them. The format fixes something that genuinely annoys developers: A skill and an MCP server that work fine on their own still have to be forked and maintained twice the moment you ship them to a second client.

Though the six companies agreed on where components live, they don’t standardize on what they do. Section 7.1 of the spec hands the skill format to the [Agent Skills specification](https://agentskills.io/specification). Section 7.2 hands wire behavior and lifecycle to [MCP](https://modelcontextprotocol.io/specification). Both came out of Anthropic, which released them openly but does not sit on the steering committee.

The project is candid about this. Its own documentation calls the result a small interoperability floor, and Google’s post describes v1 as a package format and nothing more. The obvious discrepancy is not between promotional rhetoric and technical truth. Rather, the issue is that terms like “compatible,” “portable,” and “plugin” suggest much more in everyday use than this narrow agreement actually provides.

## What Anthropic released, and to whom

Anthropic donated MCP to the Agentic AI Foundation, a Linux Foundation-directed fund, on 9 December 2025. Agent Skills followed nine days later, published as an open standard and now developed in the open at [agentskills.io](https://agentskills.io/). The governance stories differ. MCP belongs to an independent foundation, while Agent Skills is an openly developed specification without a comparable legal steward.

The Agent Plugins project lacks authority over both standards. This is the detail that defines every subsequent development in the ecosystem.

The Agent Plugins Technical Steering Committee is Clare Liguori of Amazon, Roshan Sadanani of Cursor, Harald Kirschner of Microsoft, Gav Verma of OpenAI, and Jonathan Hefner of Vercel, who serves as Lead Core Maintainer. The [Technical Charter](https://github.com/agentplugins/agent-plugins-spec/blob/main/GOVERNANCE.md) is carefully worded, stating that governance roles are held by individuals rather than organizations, that no seats are reserved for specific companies, and that no single vendor may control a majority of Core Maintainer seats.

Google’s post says it “is joining that group as a Core Maintainer, represented by Kevin Hou.” As of this writing, the [MAINTAINERS file](https://github.com/agentplugins/agent-plugins-spec/blob/main/MAINTAINERS.md), which the charter names as the roster of record, still lists five people and no Google. Joining is in progress rather than complete, and if you are tracking who holds a vote, that file is the one to watch.

No primary source explains Anthropic’s absence, so I am not going to invent one.

## The specification governs locations, not behavior

A plugin is a directory containing a plugin.json file at its root. Skills go in skills/, with one subdirectory per skill. MCP servers go in mcp.json. Those locations are fixed, and the manifest cannot move them or declare components inline, which kills the discovery indirection and precedence rules every client would otherwise have invented separately.

```
reports-plugin/
├── plugin.json          # Agent Plugins governs this
├── skills/
│   └── summarize/
│       └── SKILL.md     # Agent Skills governs this
├── mcp.json             # Agent Plugins governs the config shape
└── com.vendor.client/   # nobody governs this

```

The manifest requires two fields: `$schema` and `name`. Everything else is optional metadata.

```
{
  "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
  "name": "reports-plugin"
}

```

On the components themselves, the spec says somebody else defines them. Section 7.1 is explicit that the Agent Skills specification “is the source of truth for the SKILL.md format, frontmatter fields, and directory layout,” and that Agent Plugins govern only how skills are discovered inside a plugin. Section 7.2 does the same for MCP.

Nothing forced that choice. A specification can constrain implementations of another specification by defining a profile, mandating a subset, or prohibiting optional features. Agent Plugins declines to. Because it treats Agent Skills and MCP as separately governed contracts, it mostly avoids layering behavioral requirements on top of them and instead standardizes addresses.

## Which is why compatible is a range, not a state

Section 11.1 lists the minimum for a conformant client, and the last item needs emphasis. A client must support at least one component type: skills or MCP servers. Section 11.2 spells out the consequence that a skills-only client can conform without supporting MCP at all.

Transport support takes a similar approach. An MCP-capable client must implement at least one of stdio or Streamable HTTP and should support both, while legacy HTTP+SSE stays optional. Section 7.2.2 requires clients to skip server entries for which they do not implement transport and continue loading everything else.

Stack those together, and the range of things a conformance claim can mean gets wider.

| Client | Skills | MCP | stdio | Streamable HTTP | Conformant |
| --- | --- | --- | --- | --- | --- |
| A | Yes | No | n/a | n/a | Yes |
| B | No | Yes | Yes | No | Yes |
| C | Yes | Yes | No | Yes | Yes |

Client A and Client B share nothing. Both pass. A plugin containing a skill and a bundled stdio server runs in full on neither one, because A loads only the skill and B loads only the server, and in each case the client behaves exactly as the specification requires.

To be fair to the project, no such client exists today. The [compatible clients page](https://agent-plugins.org/compatible-clients) lists VS Code, Cursor, GitHub Copilot, ChatGPT, Codex, Kiro, Hermes Agent, OpenClaw, and Grok Bot, and each of them supports Agent Skills plus MCP, with its transports itemized. The list has also grown well past the launch-week six, which is a real adoption signal.

While the fragility is more specific than the matrix implies, it remains a detail worth noting. The bare claim of Agent Plugins conformance does not predict interoperability. What predicts it is the per-client capability matrix, and that matrix is documentation, not part of the conformance claim itself. Nothing stops a future client from shipping the skills-only profile the spec permits and describing itself the same way the eight current ones do.

## The manifest rule that contradicts its own schema

Most explainer coverage says the same thing about plugin.json: the schema is closed, and a stray top-level field invalidates the manifest. Copy a field across from a package.json, and the plugin dies.

The specification says otherwise. Section 5.2 lists the ten permitted top-level fields, then continues that if the manifest contains any other top-level field, “Clients MUST report and ignore each unknown field and MUST continue loading the plugin if the manifest otherwise satisfies this section.” Unknown top-level fields are non-fatal by design. Any other schema violation is fatal.

Then look at the [published schema](https://github.com/agentplugins/agent-plugins-spec/blob/main/schemas/1.0.0/plugin.schema.json), which sets “additionalProperties”: false at the top level. Run a stray-field manifest through a standard JSON Schema validator, and it fails. Hand the same manifest to a conforming client, and it must load.

Section 5.2 anticipates this, saying the specification text is authoritative where it conflicts with the schema. Fine as a tiebreaker, though it means the machine-readable artifact and the normative text disagree about a case that will come up constantly, and the artifact is the one your CI will reach for. If you are writing a plugin linter, do not generate it from the schema alone.

## Two files named plugin.json

Claude Code has used .claude-plugin/plugin.json for its own plugin system. Agent Plugins uses plugin.json at the package root. Same filename, different location, different schema, no relationship between them.

This genuinely creates confusion. Search results in an editor show two identical filenames. The documentation refers to “the plugin manifest” without specifying which one. A migration guide that tells you to edit plugin.json is ambiguous unless it gives the full path every time.

It’s important to clarify what Anthropic’s absence means and what it doesn’t. Claude Code is not a launch client for the format, but the npx plugins add CLI lists it as a supported install target and translates the portable package into Claude’s native plugin system. The accurate phrasing is that plugins are installed into Claude Code via the CLI, not that Claude Code implements Agent Plugins. That translation step is where behavior can drift, and nothing in the specification governs it.

## Where the client namespace takes portability back

Section 8 defines client extensions, which are reverse-domain namespaces for anything outside the portable core. A client can claim manifest data under extensions[“com.vendor.client”], a top-level com.vendor.client/ directory, or both.

Read what the spec assigns to that namespace. “Agent Plugins assigns no portable discovery, validation, loading, or failure semantics to client extension data or files. Each client defines the contents and behavior of its own namespace.”

Commands, hooks, agents, rules, and LSP servers all live outside v1, on the stated grounds that their formats have not converged. Every one of them is something developers actually build plugins for. When [Adam Dalloul of EmpirioLabs warned](https://thenewstack.io/agent-plugins-open-standard/) that useful behavior ending up inside vendor namespaces would leave the standard open on paper while fragmentation moved elsewhere, he was describing the escape-hatch section 8 documents.

Whether that matters depends on how much of your plugin’s value lives in hooks. If it is most of it, the portable part is the wrapper, and the fork you were trying to avoid is still there under a different directory name.

## Your plugin is portable until it needs a password or a binary

Two smaller findings that will cost the developer’s time.

Section 7.2.1 says header values are “visible package data, not a portable secret mechanism,” that plugins must not embed credentials in headers or env, and that v1 defines no OAuth configuration and no portable credential-reference fields. Authorization discovery, user interaction, and credential storage are client-managed. Any plugin that talks to an authenticated service is therefore portable in packaging and client-specific in setup, and setup is the part where users get stuck.

The second is more subtle. For stdio servers, the command must be a bare executable name or a plugin-relative path. Whether a configured PATH value participates in resolving a bare name is, in the spec’s words, client-defined, and plugins claiming conformance must not depend on that behavior. Clients may also inherit, omit, or sanitize ambient environment variables as they see fit. Two conformant clients can launch the same server with different environments and different resolution results. If your plugin ships an executable, use a plugin-relative command and stop relying on the ambient environment.

## What a v1.1 would need to fix

The project is candid about the gaps. Its [future considerations document](https://github.com/agentplugins/agent-plugins-spec/blob/main/FUTURE_CONSIDERATIONS.md) lists permission declarations, cryptographic signature verification, attestation chains, a secrets mechanism, organization allowlists, audit event schemas, dependency resolution, and a conformance test suite.

Two of those do different jobs and are worth calling out. A conformance suite would make implementation claims testable, establishing that a client correctly does what it claims to do. A machine-readable capability profile would make the remaining optional surface predictable, turning today’s compatible-clients page into something a build can check. You want both, and the second is the cheaper win.

Signatures and permissions matter more than either. A permission model forces every client to agree on what a plugin may touch, and an IDE, a CLI, and a managed enterprise platform each answer that differently today. The charter gives no vendor enough votes to break the tie. I should flag that as my inference, since the project has not mentioned it explicitly.

Agent Plugins does the narrow thing its authors set out to do, and the restraint is deliberate rather than an oversight. Just read the compatibility page as a capability list rather than a promise, because the specifications defining the semantics of its two portable component types are governed somewhere else.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)