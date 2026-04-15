Before writing the first line of code for [Suga](https://docs.suga.app/introduction), we knew we eventually wanted multiplayer interactions, so that teams could collaborate on projects. However, with a long feature wishlist already, we figured we could defer it until later as “nice to have”. So instead, the first canvas implementation was built with basic last-write-wins conflict resolution.

Unfortunately, Jye and I figured out the hard way that our assumption about conflict resolution was pretty naive. Using an early build of Suga, we started working in a shared project at the same time without realizing. I was adding a service, along with its Postgres database, config, env vars, and tweaking positions so the layout made sense. Jye was on the other side of the project, adding functions and coding up integrations.

Changes get saved as a draft automatically as you work, so every time one of us moved a node or added a connection, the draft updated. However, because there was no merging, each save just replaced the entire draft with whatever the client had. My saves were silently overwriting Jye’s work, and his were overwriting mine. When Jye refreshed the browser tab, everything he’d built was gone, since I’d made the most recent change, the last draft write was mine. We do automatically track a project’s history, but only for deployed changes, so because none of this had been deployed yet, it was just lost.

It made it obvious that last-write-wins for the entire canvas wasn’t going to work. Although we could have improved the situation with other locking/conflict resolution techniques, we knew we wanted full multiplayer eventually, so real-time sync was the right choice.

## Have you looked at sync engines?

If you’re unfamiliar with sync engines, Jye got kind of obsessed with them last year and [wrote a blog about it](https://bytemash.net/posts/i-went-down-the-linear-rabbit-hole/). I’d also recently watched a [Syntax video](https://www.youtube.com/watch?v=_tHSAKVCJQo) where they used Zero to build a competitive coding game, and the sync model clicked immediately. In our next standup, we both agreed we needed to drop other features and get this built.

We ended up going with [Zero](https://zero.rocicorp.dev/), which is a sync engine from Rocicorp. Basically, every client gets a local SQLite database that stays in sync with our PostgreSQL on the server. Writes happen locally first, then are replayed on the server; if there’s a conflict, the server wins, and clients reconcile automatically.

Why Zero and not something else? CRDT libraries like Yjs and Automerge are designed for document-style collaboration, things like text editors and drawing tools. Our [data is relational](https://thenewstack.io/dont-let-time-series-data-break-your-relational-database/) Postgres rows, including some larger JSONB columns. Tools like ElectricSQL and PowerSync also sync Postgres, but Zero’s [mutator](https://zero.rocicorp.dev/docs/mutators) model gave us fine-grained control over conflict resolution for JSON values.

## Two kinds of changes

We realized early that not all changes are equal; some can be merged, some can’t, and some can tolerate last-write-wins. Figuring out which was which turned out to be the core design problem. The canvas is built on [React Flow](https://reactflow.dev/), and every interaction that changes state goes through a Zero mutator.

> “Figuring out which was which turned out to be the core design problem.”

![Diagram of interactions that change state, going through a Zero mutator.](https://cdn.thenewstack.io/media/2026/04/43e36fed-11-1024x654.png)

### Granular mutators

The canvas node positions are stored as a single JSON value for simplicity. What we want is when I drag a node, only that node’s position changes. If someone else drags a different node at the same time, both writes land cleanly, without conflict. If we somehow drag the same node simultaneously, the last write wins, since that’s fine for node positions where there’s no meaningful way to merge them and the data isn’t critical. If I place a node at (400, 200) and Jye places one at (600, 300), one of us will win.

Here’s what that mutator looks like for node positions:

```

typescript
export const updateNodePosition = defineMutator(
  z.object({ environmentId: z.string(), nodeId: z.string(), position: PositionSchema }),
  async ({ tx, ctx, args: { environmentId, nodeId, position } }) => {
    // Access check runs server-side only
    if (tx.location === "server") {
      await verifyAccess(tx, environmentId, ctx.activeOrganizationId);
    }

    const env = await getEnvironment(tx, environmentId);

    // Spread existing positions, overwrite just this node
    await tx.mutate.environment.update({
      id: environmentId,
      canvasMetadata: {
        ...env?.canvasMetadata,
        nodePositions: {
          ...env?.canvasMetadata?.nodePositions,
          [nodeId]: position,
        },
      },
    });
  },
);

```

The spread is the key part: we read the current positions and overwrite only the one node. On the client, this reads from local cache; on the server, it reads from the database. Both run the same function, but the server’s view is authoritative.

> “The spread is the key part: we read the current positions and overwrite only the one node… the server’s view is authoritative.”

A similar pattern applies to infrastructure changes, which is what fixed our clobbering problem. When I add a service, the mutator reads the current compute array, appends mine, and writes it back. If someone else adds a function at the same time, their mutator does the same. The server replays both, and the result has both changes.

```

typescript
export const addCompute = defineMutator(
  z.object({
    environmentId: z.string(),
    compute: ComputeSchema,
    position: PositionSchema.optional(),
  }),
  async ({ tx, ctx, args: { environmentId, compute, position } }) => {
    // ... same access check pattern

    const env = await getEnvironment(tx, environmentId);
    const def = env?.draftDefinition;

    // Read current computes, append the new one, write it back
    const updatedDef: ProjectDefinition = {
      version: "v1",
      computes: [...def.computes, compute],
      volumes: def.volumes,
    };

    await tx.mutate.environment.update({
      id: environmentId,
      draftDefinition: updatedDef,
      // ... also sets node position on canvas if provided
    });
  },
);

```

We considered [using CRDTs](https://thenewstack.io/fireproof-uses-merkle-crdts-to-cut-database-latency/) to merge these changes, but our data model would require significant work to decompose into CRDT-friendly structures. [Building a custom](https://thenewstack.io/custom-integrations-for-complex-scenarios-7-best-practices/) CRDT would have added complexity without a clear win over last-write-wins for positions, or read-modify-write for computes.

### Bulk mutators

Some operations can’t be granular; for example, `undo` replaces the entire canvas with a previous snapshot. Deploy and discard do the same.

```

typescript
export const updateDraftAndCanvas = defineMutator(
  z.object({ environmentId: z.string(), draftDefinition: ProjectDefinitionSchema, canvasMetadata: CanvasMetadataSchema }),
  async ({ tx, ctx, args: { environmentId, draftDefinition, canvasMetadata } }) => {
    // ... same access check

    // No spread, no merge. Just replace everything.
    await tx.mutate.environment.update({
      id: environmentId,
      draftDefinition,
      canvasMetadata,
    });
  },
);

```

There is currently no merging here; the snapshot wins. That’s the right tradeoff for undo, where the intent is “go back to exactly this state.”

## Drizzle as the schema source of truth

We use [Drizzle](https://orm.drizzle.team/) as our ORM. Its schema definitions double as the source of truth for Zero’s sync schema.

```

typescript
export const environment = pgTable('environment', {
  id: uuid('id').primaryKey().defaultRandom(),
  projectId: uuid('project_id').references(() => project.id),
  canvasMetadata: jsonb('canvas_metadata').$type&lt;CanvasMetadata>(),
  draftDefinition: jsonb('draft_definition')
    .default(InitialProjectDefinition)
    .$type&lt;ProjectDefinition>(),
  // ...
});

```

Two JSONB columns hold the collaborative state: `canvasMetadata` for positions and sticky notes, `draftDefinition` for the infrastructure graph. The alternative would be to normalize into separate tables, which would give zero row-level diffs. We chose JSONB for now because it’s simpler and the mutator-level merge gives us enough control. If we hit scaling issues, normalizing is the obvious next step.

A few gotchas we hit:

* JSONB is the replication unit, and Zero doesn’t diff inside the JSON, which is why the granular mutators do that spread pattern.
* If you forget to regenerate after a schema migration, the client silently misses new columns without errors, resulting in missing data.
* We had to write custom scripts to create Zero publications and a filter. Getting the publication config right took several rounds of tuning what gets replicated and what doesn’t.

## Nanostores for local state

Zero handles synced state, but some state belongs only on the client, such as user-specific undo history; for that, we use Nanostores. These stores are really just a read-only way to consume Zero data, where Zero handles all mutations and then syncs with the store. [Nanostores](https://github.com/nanostores/nanostores) is lightweight and handles the globally accessible state part cleanly.

```

typescript
export const $nodePositions = map&lt;Record&lt;string, Position>>({});
export const $stickyNotes = atom&lt;StickyNote[]>([]);
export const $draftDef = atom&lt;ProjectDefinition>(InitialProjectDefinition);
export const $undoState = atom&lt;UndoState>({ past: [], future: [] });

```

For undo, we capture a full snapshot before each meaningful change and store it in a 20-item history stack. Undo restores the snapshot locally and fires a bulk mutator via Zero to sync it with other clients.

## Works locally, breaks on deploy

Getting Zero running locally went well enough; we just run a compose file for local dev, and the CLI auto-generates the schema from Drizzle. I demoed it to the team, and everyone could see each other’s changes, nodes appearing in real time, the whole thing. It worked, and I was feeling good about it.

We deployed to staging, and it broke instantly.

### The silent 401s

Our staging and preview deployments run with deployment protection enabled. Zero-cache runs as a separate server and needs to call `/api/zero/query` and `/api/zero/mutate` on the main application. Deployment protection was blocking those requests with 401s.

The frustrating part was that in the browser, nothing looked obviously wrong. The failures were happening between Zero and our other endpoints, not in the browser’s network tab. I had to pull up the workload logs to see the actual errors stacking up. Once I saw them, the fix was adding the appropriate header to the query and mutation requests.

### The cookie problem

Zero uses cookie-based auth by default, and our preview and staging environments generate new temporary URLs for every PR. Cookies are scoped to a domain, and with a new domain per preview deployment, cookie auth was basically impossible to get working reliably.

For local and staging environments, we pass the session token directly via the `auth` prop on the `ZeroProvider` component instead of relying on cookies, while production still uses cookies. It’s a small split in the auth path, but it was a reliable way to support the way we use preview deployments.

## It’s live now

Since adding Zero for sync and conflict resolution, Suga users can all work in the same project at the same time. If you have feedback on how we can improve your experience, reach out. We’re always looking for ways to improve.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/aa54bd50-cropped-734146d4-david-moore.jpg)

David Moore, head of engineering at Nitric, is a skilled software architect. He specializes in innovative product development and open source software solutions. With a strong record of spearheading major fintech and government projects, David has led UX framework development,...

Read more from David Moore](https://thenewstack.io/author/david-moore/)