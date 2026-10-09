I measured what an AI agent actually holds when it authenticates as me. Authentication turned out to be a token whose scope string literally says `user_impersonation`. Authorization came almost entirely from group membership that standard permission checks cannot see.

Permission scoping differed by two orders of magnitude between two production stores reached an hour apart, and audit coverage ran inversely to what the credential could do. The environment where the agent could delete from a secure database was the only one with no audit trail.

When I measured the machine identity our own [unattended agent runs](https://thenewstack.io/incredibuild-ai-agents-sandbox-coding/) under, built properly and scoped per resource, it broke in the same place mine does.

> “The environment where the agent could delete from a secure database was the only one with no audit trail.”

I gave a coding agent my own Azure credentials, which is standard practice, and then investigated what it could reach. The answer: two permissions on one production store and 107 on another. The environment where it could delete from a secure database was the only one with auditing switched off. None of that was a misconfiguration. All of it was reasonable when the only thing holding that credential was a human.

## The setup nobody calls an identity model

Eleven agent skills in our working repository connect to databases. They all authenticate the same way:

```

Bash
sqlcmd -S &lt;server> -d &lt;db> --authentication-method ActiveDirectoryAzCli -C -Q "&lt;query>"

```

That flag tells `sqlcmd` to ask the Azure CLI for its cached token and present it. No connection string, no stored password, and no credential belonging to the agent itself. When the agent runs a query, the database sees me.

Engineers describe this as the agent “not having an identity yet.” It does have one. It has mine.

> “Engineers describe this as the agent ‘not having an identity yet.’ It does have one. It has mine.”

Using borrowed credentials is a known bad practice. It leads to three common outcomes: attribution collapses, the agent inherits whatever permissions the human accumulated, and revoking the agent revokes the human. I wanted to measure these predictions against a live, running estate. The results show that two of those three outcomes are much stranger than they appear on the surface.

First, I checked what the database records about incoming connections:

```

SQL
SELECT login_name, program_name, host_name, client_interface_name 
FROM sys.dm_exec_sessions 
WHERE session_id = @@SPID;

Plaintext
login_name: naseeb.ahmed@<redacted> 
program_name: sqlcmd 
host_name: <my workstation> 
client_interface_name: go-mssqldb

```

These identity fields reflect my login, my machine, and the tool. Not one of them changes depending on whether I typed the query or the agent decided to run it. Because no fourth field exists for an agent to declare itself, agent actions and human actions are identical by design.

Every guardrail downstream of this point relies on these same three values. No downstream control can be conditional on the agent: not a rate limit, not an approval step, and not a different retention policy for machine-initiated statements.

> “The record is accurate about the credential, but silent about the intent.”

This creates a reverse problem, too. If someone questions a query I typed six months from now, I have no way to prove it was mine rather than something an automated tool executed. The record is accurate about the credential, but silent about the intent.

## Authentication: what the token actually says

Our approach to authentication was simple: nobody actually designed it. A developer signs in once with a directory account and a second factor, the CLI caches the result, every skill in the repository picks it up, and agent authentication simply piggybacks on whatever the human did earlier that morning. It avoids storing passwords and eliminates the need to provision an identity before you know whether the agent is useful.

Decoding the access token the CLI hands over for database connections reveals the following claims:

```

Plaintext
aud: https://database.windows.net/
appid: &lt;Azure CLI public client ID>
appidacr: 0
scp: user_impersonation
exp - iat: 84 minutes
groups: 37 entries
amr: ['pwd', 'mfa']

```

Two of these claims stand out:

* **The scope is** **`user_impersonation`.** RFC 8693 defines impersonation as a principal receiving all rights of another while remaining indistinguishable from it. My session record matches that definition.
* **The** **amr** **(authentication methods) claim carries** **mfa****.** Every action the agent takes arrives with an attestation that a human satisfied a second factor, even if that factor was completed hours earlier for an unrelated task.

The 84-minute lifetime looks like a safety boundary, but it is not. The CLI refreshes automatically using its refresh token, so an unattended run does not stop after 84 minutes. It stops only when the refresh token expires or when someone deactivates the user account.

## Authorization: the check that shows nothing

Listing role assignments across every subscription in the tenant returned a single row: `Reader` on a non-production subscription.

However, group membership tells a different story:

* 34 active group memberships
* 7 visible subscriptions (including production)

The access-relevant groups mirror an organizational chart:

* `<environment> - SQL Database Viewer`
* `<environment> - SQL Elevated`
* `<environment> - Resource Contributor`
* `<environment> - SQL Database Manager`
* `<environment> - Resource Viewer`
* `<environment> - Readers`

Groups carry everything that grants actual data access and live in the data plane, where control-plane queries cannot see them. A security reviewer checking an agent’s authority through standard role assignments gets a single row and a false sense of a small blast radius.

The token’s groups claim shows 37 entries, while the directory’s direct-membership query shows 34. The difference comes from nested groups. The two authoritative answers for group membership don’t agree, and the database uses the larger number.

Some of those memberships are managed just-in-time (JIT). Querying which ones are temporary resulted in an error:

```

Plaintext
Forbidden: PermissionScopeNotGranted 
PrivilegedEligibilitySchedule.Read.AzureADGroup, PrivilegedAccess.Read.AzureADGroup

```

The credential that can delete rows in a secure database cannot read whether its privileges are standing or temporary. Per vendor documentation on JIT group activation, an application that has already cached a membership may keep honoring it after deactivation. The window binds the directory record, but it does not reach into an already issued token.

## Permission scoping: two production stores, one hour apart

Using `fn_my_permissions` to check what the connected principal actually holds on the production database server showed:

* **Visible databases:** 1,382 (692 business tier, 687 secure tier)
* **Business tier permissions:** CONNECT, SELECT
* **Secure tier permissions:** mssql: login error: Login failed for user ‘<token-identified principal>’

The token holds two permissions, and the secure tier refuses the connection outright. Read access is enforced where necessary, with no path to the sensitive tier. The agent inherits a tight, correct scope here.

However, querying the production analytics endpoint over our lakehouse with the same token revealed:

* **Tables:** 430
* **Permissions:** 107 (spanning read, write, schema definition, and database administration)

One identity accessed two production stores an hour apart, holding two permissions on one and 107 on the other. A grant that wide is no longer a job description; it is a full role assigned to a human who occasionally looks at analytics, now handed to a tool running thousands of statements unattended.

Vendor documentation notes that the analytics endpoint is read-only over the underlying tables, with modifications passing through a different engine. Security rules configured on that endpoint govern access through it, but they do not follow the data when another engine accesses it. Effective access depends on the path, not the principal.

> “Code enforces one restriction, while the other is a sentence in a file. The agent reads both, verifies neither.”

Furthermore, the instruction file the agent reads before touching that endpoint states the surface is read-only. The credential the agent presents grants 107 permissions. Code enforces one restriction, while the other is a sentence in a file. The agent reads both, verifies neither, and operates on an instruction set that contradicts its actual privileges.

In a non-production environment, the scope opens up entirely:

* **Business tier:** CONNECT, SELECT, INSERT, UPDATE, DELETE
* **Secure tier:** CONNECT, SELECT, INSERT, UPDATE, DELETE

Write and delete rights apply to both tiers. In most software estates, non-production environments allow team members to break things by design.

## Audit trails and misleading checks

Checking database-level audit configurations returned six enabled specifications:

```

SQL
SELECT name, is_state_enabled FROM sys.database_audit_specifications;

```

While the database reported auditing as enabled, querying the monitoring sink returned an empty result rather than a permission error. Nothing was writing to the log.

Audit configurations live on the server resource, not inside the database. Querying the management API revealed that one environment had server auditing enabled with statement-level action groups attached:

* BATCH\_COMPLETED\_GROUP
* SUCCESSFUL\_DATABASE\_AUTHENTICATION\_GROUP
* FAILED\_DATABASE\_AUTHENTICATION\_GROUP

The second environment had auditing completely disabled at the server level, with no destination attached. The six database specification objects were remnants from past environment copies.

The internal database check reported “enabled” for an environment recording zero activity.

Audit coverage runs inversely to what the borrowed credential can do. Production environments are audited, while non-production environments are left unmonitored to save on [storage and processing costs](https://thenewstack.io/observability-can-get-expensive-heres-how-to-trim-costs/).

This logic holds until an agent replaces the human user. The agent removes the core assumption behind both configurations without alerting either system.

Additionally, failed logins under directory authentication do not reach the SQL audit log because credentials are verified before touching the database. The refusal that protected the secure tier remains invisible in the logs. Auditing is also best-effort under heavy load, with statements truncated past 4,000 characters.

## What breaks when using a service account instead

Our repository also contains an unattended agent running on a 15-minute timer trigger. Its identity uses a user-assigned managed identity per app group with explicitly named role grants:

* Key Vault Secrets User (shared vault)
* AcrPull (container registry)
* Storage Blob Data Contributor (storage account)
* Storage Queue Data Contributor (function storage)
* Storage File Data SMB Share Contributor (file share)
* Storage Blob Data Reader (public storage)

This structure represents a properly configured machine identity. However, when connecting to databases, the managed identity is not used. Instead, it authenticates via a standard SQL login and password set at deploy time.

The database cannot distinguish between different callers. The machine identity stops where the data path begins. At the database, the automated agent is just as unattributable as a human user.

Both models fail at the same place. [Giving every agent](https://thenewstack.io/databricks-electric-wasm-agentic-postgres/) its own service account changes the name in the log, but it does not resolve attribution.

## What a purpose-built identity model requires

Tightening permissions and turning on auditing in non-production environments limits potential damage, but it does not fix root-cause attribution. The system still logs human credentials for automated actions.

Addressing these issues requires five core changes:

1. **Separate the actor from the subject at the credential level.** RFC 8693 distinguishes between impersonation tokens (which carry only a subject) and delegation tokens (which carry both the subject and the acting party). Agent credentials should derive from human credentials and carry both identities so session logs can record both.
2. **Enforce effective permissions as an intersection.** An agent should only reduce access, never widen it.
3. **Scope by action rather than by principal.** Permissions should apply to specific operations rather than granting broad, identity-wide roles.
4. **Tie audit coverage to privilege levels instead of environments.** If a credential holds write or delete access on a database, statement logging must follow the credential regardless of the environment.
5. **Provide independent revocation mechanisms.** Cutting off an agent should not require deactivating the primary human user account.

The Model Context Protocol (MCP) authorization specification explicitly prohibits servers from forwarding client tokens to ensure downstream services can verify caller identity. Command-line tools need to adopt the same standard.

## Unresolved limits

These findings represent measurements taken across a single estate over two days:

* The gap between permission levels across stores may stem from platform defaults rather than intentional design choices.
* We evaluated production audit log rows via session records and configured action groups rather than direct bulk extraction of user query logs.
* Verifying which group memberships are permanent versus JIT requires diffing directory queries after temporary activations expire.
* Implementing per-agent authorization flows introduces friction. The frictionless model remains popular because it works out of the box, but it leaves behind an audit log that attributes machine decisions to human identities.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/09/d1b04cef-naseeb-600x600.jpeg)

Naseeb is a Full Stack Software Engineer with 7+ years of experience building analytics and data-intensive web applications across .NET Core, Node.js, and React/TypeScript. He is currently engaged full-time at Vantaca through Andela, where he architected the Vantaca IQ analytics...

Read more from Naseeb Ahmed Mian](https://thenewstack.io/author/naseeb-ahmed-mian/)