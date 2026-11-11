![Anthropic Claude AI March 2026 roundup — abstract illustration with colorful overlapping circles on a dark background representing the rapid pace of AI model releases and MCP protocol growth](https://cdn.thenewstack.io/media/2026/03/21bf8ca8-screenshot-2026-03-27-at-12.21.10-1024x670.png)

**Anthropic is expanding Claude’s ability to work directly inside** enterprise applications; it can now open full software interfaces, retrieve information, and make changes without requiring users to move between applications.

At [The Briefing: Work at the Frontier](https://www.anthropic.com/events/the-briefing-work-at-the-frontier-ls) in San Francisco on Tuesday, the company announced expanded interactive connectors, along with new tools for meetings, spreadsheets, shared workspaces, and business data.

“For years, we’ve learned to work around software. Now Claude works around you,” said [Ami Vora](https://www.linkedin.com/in/amvora/), Anthropic’s chief product officer, in remarks prepared for the event.

> “For years, we’ve learned to work around software. Now Claude works around you,”

## Full apps open inside Claude

Anthropic’s [interactive connectors](https://claude.com/resources/articles/interactive-connectors-full-tool) previously let users see a small preview of a connected app in Claude. Now, they can open and work in the full application within the conversation, starting with Adobe, Atlassian, and HubSpot.

For example, Claude can edit a Confluence page directly or update an Adobe design using assets from a company’s brand kit. Users do still need to approve those changes before Claude executes.

## Built on MCP Apps

The expanded connectors are built on [MCP Apps](https://modelcontextprotocol.io/docs/extensions/apps), which lets MCP servers provide interactive interfaces instead of relying solely on tool calls. Developers can bring existing application interfaces into Claude using app tools and embedded websites, without rebuilding them for the assistant. The new capabilities are in public preview and aren’t limited to Claude, since other AI clients that support MCP Apps can use them too.

> The new capabilities are in public preview and aren’t limited to Claude, since other AI clients that support MCP Apps can use them too.

Anthropic says Claude Marketplace now includes more than 9,000 connectors and plugins, continuing [the effort to connect AI systems with enterprise infrastructure](https://thenewstack.io/mcp-sql-the-secret-weapon-to-connect-ai-to-enterprise-systems/). For applications without a supported connector, Claude can use its built-in browser to interact with them.

## Existing permissions still apply

The company says connectors respect the permissions employees already have in the underlying application. For example, a user who cannot access a particular Google Drive document cannot retrieve it through Claude.

Administrators can also restrict individual connector capabilities, including allowing Claude to read Slack messages without permission to send messages.

Additionally, Anthropic is introducing Claude auto-connect in beta, a ten-minute setup that lets administrators enable connectors across an organization without requiring employees to configure them individually. Smart Reports, meanwhile, gives administrators visibility into team usage, completed work, and spending.

## Claude Data gets certified queries

Anthropic is also making Claude Data generally available, following its October launch as [Claude Dashboards](https://thenewstack.io/claude-dashboards-data-motion/).

> The update introduces certified queries, allowing data teams to approve the queries Claude uses for reporting so different teams get consistent numbers from the same data.

The update introduces certified queries, allowing data teams to approve the queries Claude uses for reporting so different teams get consistent numbers from the same data. A second feature, live sharing, lets employees access updated dashboards without needing direct access to the underlying data source.

Both features are still in beta. Anthropic hasn’t detailed how it handles versioning for certified queries or changes to the source data’s schema.

## Task delegation moves beyond engineering

Claude Meetings, which Anthropic says is coming soon, will join video calls to create project plans, answer questions, and retrieve information from connected applications. The feature is planned for Team and Enterprise customers but won’t be available to organizations using zero data retention, HIPAA-ready configurations, or customer-managed encryption keys.

Another feature, Claude Whiteboards, gives teams a shared space to develop projects with Claude, while Claude Sheets lets them build and edit spreadsheets together. Both are available in beta on paid plans.

## Enterprise adoption moves beyond engineering

At Datadog, product managers are using Claude to develop product requirements documents and testable prototypes. [Uday Tennety](https://www.linkedin.com/in/udaytennety/), the company’s head of technology partnerships, said the approach has shortened the time between an initial idea and a working prototype.

Anthropic also reports that Mercado Libre has deployed Claude to more than 26,000 employees, with 78% using it weekly. These figures have not been independently verified.

The post [Anthropic wants Claude to be the front end for your entire enterprise app stack](https://thenewstack.io/claude-enterprise-apps-connectors/) appeared first on [The New Stack](https://thenewstack.io).