Mistral is giving enterprise customers until August 31 to replace the Google Drive and Microsoft SharePoint Knowledge Connectors they use in Vibe Work with MCP-based alternatives. The company says in its [Knowledge Connectors documentation](https://docs.mistral.ai/vibe/work/connectors/knowledge-connectors) that both existing connectors will be shut down and deleted on that date.

There is no automatic migration, so administrators will need to install the MCP replacements before every user reconnects their Google or Microsoft account. The move changes how Vibe Work reaches company documents, but Mistral has said little about the retrieval architecture behind the new connectors.

## Mistral stores a searchable index

With the current system, an administrator chooses which Google Drive folders or SharePoint sites the organization wants to make available, then Mistral processes those files and stores the resulting index in its European data centers.

Once the index is ready, users connect their personal accounts, and when they search in Vibe Work, the connector checks permissions copied from Google Drive or SharePoint so the results include only files they can access, while scheduled synchronizations pick up later changes and deletions.

This setup lets Mistral handle retrieval by searching a prebuilt index whenever a user submits a query. The company says indexing can take anywhere from a few minutes to several hours, depending on how much data the organization includes, although that work is completed before users begin searching.

> The company says indexing can take anywhere from a few minutes to several hours, depending on how much data the organization includes, although that work is completed before users begin searching.

## MCP shifts retrieval off-platform

The company defines MCP as a common interface that lets models call tools and retrieve data from external services — the same protocol layer that [is reshaping how AI products connect to external APIs](https://thenewstack.io/api-mcp-agent-integration/) across the industry.

In June, Mistral added Google Drive and SharePoint to a directory containing more than 60 integrations, but it did not explain how those two connectors retrieve documents or say who operates the underlying MCP servers. The setup can range from live calls to the source API to a server-managed search index, with any combination of the two in between. That flexibility is part of what makes [MCP appealing in some environments and unnecessary in others](https://thenewstack.io/when-is-mcp-actually-worth-it/), but it also means that the behavior of a given connector depends entirely on its operator.

Permissions rules remain unclearThe company doesn’t run the third-party servers behind these connectors, so it can’t promise how they will behave or what they will do with customer data. That gap between the governance Mistral once provided and what it’s now handing off to third parties reflects a trend in how enterprises are adopting MCP connectors [without fully resolving the governance layer](https://thenewstack.io/mcp-enterprise-agent-governance/). As other platforms have learned, opening the door to external servers means trusting the protocol and the operator and [building the guardrails to go with it](https://thenewstack.io/godaddy-developer-platform-domains/).

The migration notice offers even less detail. It doesn’t say whether the Google Drive and SharePoint MCP servers retrieve files directly from Google and Microsoft. Any caching remains unexplained, leaving customers unsure where retained data would live. Mistral makes no promise that searches will be as fast or return results of the same quality.

> Mistral makes no promise that searches will be as fast or return results of the same quality.

The outgoing Google Drive connector follows the sharing rules already attached to each file, including group and domain access. A file set to “anyone with the link” still isn’t automatically visible to everyone in the organization. SharePoint uses Microsoft Entra ID groups, so older groups created only within SharePoint aren’t picked up.

Mistral hasn’t said whether the MCP replacements will follow the same rules. OAuth can limit a server’s access to the connected user, but that doesn’t mean search results will be filtered exactly as they were in the outgoing index. The [protocol wasn’t designed to enforce that kind of enterprise permission model](https://thenewstack.io/openai-elastic-enterprise-context/); the connector’s retrieval layer has to do it.

> OAuth can limit a server’s access to the connected user, but that doesn’t mean search results will be filtered exactly as they were in the outgoing index.

## Deletion timeline still unresolved

The company says disabling a Knowledge Connector results in permanent deletion of the indexed data, but the deprecation notice does not say whether the August shutdown will trigger that process automatically or how long the deletion will take. It also leaves administrators unsure whether they should disconnect the old connectors themselves before the deadline.

Because the same connectors work in Vibe Code and Mistral’s workflow system, teams can use the same approach to expose external data across chat, coding and automated jobs — a pattern that is [becoming more common as MCP connectors spread from chatbots into production infrastructure](https://thenewstack.io/elevenlabs-mcp-voice-agents/).

Mistral also recommends checking server output for signs of prompt injection — advice that underscores the [still-emerging challenge of securing the space between AI agents and the external services they access](https://thenewstack.io/red-teaming-enterprise-ai-agents/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)