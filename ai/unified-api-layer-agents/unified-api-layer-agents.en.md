**Building the app was never the hard part.** Now, with AI agents assisting with development, teams complete applications and internal tools faster than ever. The problem is getting access to live operational data. Teams rebuild access rules and connections by hand for every project, as fast as they can, to unblock the build. Sometimes direct access is refused, so the build is forced to run on a copy: stale by definition, and a dead end for anything that needs to write back to the source.

## The cost of access

Applications use data to complete mission-critical tasks, so they need access to the APIs, databases, and cloud services that provide it. Each connection is bespoke, requiring different access levels and different subsets of the available data. To get this access, teams create tickets with each system owner to request it. And the waiting game begins. You may have to defend your reasoning for access and follow up on unanswered emails, stuck waiting to finish the tool simply because gaining access to data is so slow.

Fast forward to three years later — the PostgresDB is being migrated to a new server. Do you know every tool connected to it? Missing one could lead to an outage. An employee leaves the company. Are you sure that you’ve removed access from every tool? And with the rise of AI agents, do you know who is connecting them to production systems, and for what purpose?

As teams grow and the number of connections multiplies, the busywork of creating and maintaining connections snowballs. Access control involves a dozen different logins across systems and takes time away from building. Onerous, repetitive tasks slow down every team’s productivity.

A unified API layer could be the solution.

## What is a unified API layer?

Think of a unified API layer as a single governed access layer for any data source that contains business-critical data. Instead of filing requests with the owner of each database, API, and business tool, teams request access in one place.

This also means that access control for every data source is centralized in the unified API layer. Instead of relying on many different systems, each with different access parameters and rules, there’s one place with one set of rules and one consistent record of every change made to that data.

Access in the unified API layer uses least-privilege, role-based access control for every data source in your organization. In addition to team members, applications and AI agents also have identities, each scoped to exactly the data that they require.

> “So two agents may make the same request, but get a different response, depending on what each one is allowed to see.”

As [James White](https://linkedin.com/in/james-white-directus?originalSubdomain=uk), VP of Product at [Monospace](https://monospace.io/), puts it, “A gateway covers the connection. We go deeper, because we know the schema, we know who’s asking, and we understand the response. So two agents may make the same request, but get a different response, depending on what each one is allowed to see.”

Teams can point their agents at the unified API layer over MCP, and each agent gets exactly the data its identity allows. Developers get a typed SDK, one consistent interface regardless of what sits underneath.

White adds, “You ask for data the same way no matter where it lives. If it’s a database, we translate the request to SQL. If it’s an API, we turn it into that API’s call, with filtering and pagination handled either way. From the developer’s side, it’s one typed interface for everything.”

## What AI changed: agent identity and access control

An agent inherits whatever credential it was handed. Developers may give the agent their personal API keys and credentials — tying the agent’s identity to the developer. What happens to the agent when the developer rotates their keys? What happens when the developer leaves the organization?

Agents need their own role-based access, disconnected from other users and applications. A unified API layer creates an identity for each AI agent and scopes its access controls.

Connecting AI agents to production data is where most leaders get nervous. They worry the agent might run amok and put production systems at risk. Field-level permissions are among the strongest guardrails you can put on agents because they’re enforced at the data layer rather than relying on the agent to follow prompt instructions. Set on the agent’s identity, they control what it can read and where it can write. Unified API layers already excel at this.

Imagine a rule: “The agent can update the shipping address on an order, but not the payment method, and only on orders that haven’t shipped yet.” Field-level permissions let the agent write to shippingAddress but not paymentMethod, while record-level permissions restrict it to unshipped orders. With discrete rules in place, changes in the system of record are tightly controlled.

Access controls and discrete permissions are at the core of unified API layers, which is exactly why they fit AI agents.

## What has to be true for unified API layers to work

* The layer has to reach systems as they are — federating data across them in place rather than migrating or consolidating it as a copy
* Every consumer should have its own scoped set of access controls
* A unified record of every connection and request made into every system: No more digging into multiple servers to piece together connection logs
* Consumers get one consistent interface, whatever the underlying source. Apps and agents query the layer, never the systems behind it
* Agents connect over MCP with a unique identity, and their roles and policies determine what they can access

## Monospace

Monospace is one example of this unified API layer model. Connect databases (e.g., PostgreSQL, Supabase, MySQL, MariaDB), SaaS platforms, and internal APIs once, and it introspects the existing schema or endpoints and maps them to a common data model without migrating the underlying system. That’s what reaching systems “as they are”‘” means in practice: Monospace keeps a metadata layer on top, and the data stays where it lives.

Every identity gets a role with specific policies. The policies set access per action (create, read, update, delete), and further limit access to specific fields and items. Rules like “can change the shipping address, but not payment method” are evaluated on every request. Monospace can also filter the response to prevent exposure of data to the wrong parties.

Developers get a typed SDK generated straight from the schema, with autocomplete in the IDE. Agents get an MCP endpoint — one governed entry point instead of hand-wiring a separate connection per tool. Same underlying access model either way.

## Who knew access control would slow us down?

It was never about building the apps. It’s about provisioning data to them quickly and safely.

Scoping access for agents is another issue that many enterprises have kicked the can on, knowing they’ll have to solve it someday.

A unified API layer doesn’t make that problem go away. It gives you one place to solve it — once, instead of once per system, per application, per agent. [Monospace](https://monospace.io/) is one such solution.

***Check out the*** [***docs***](https://docs.monospace.io/en/getting-started/installation) ***and get started building your unified API layer today.***

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/11/1c01c260-doug-sillars.jpg)

Doug is a lifelong learner and educator, having focused his career on improving developer knowledge and experiences.  A Google Developer Expert for the web, O’Reilly author, international keynote speaker, and a prolific blogger, he relishes in simplifying the complex. When...

Read more from Doug Sillars](https://thenewstack.io/author/doug-sillars/)