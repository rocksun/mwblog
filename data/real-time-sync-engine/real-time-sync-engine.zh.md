在为 [Suga](https://docs.suga.app/introduction) 编写第一行代码之前，我们就知道最终需要多人交互功能，以便团队可以在项目上进行协作。然而，由于功能需求列表已经排得很长，我们认为可以将其作为“锦上添花”的功能推迟。因此，第一个画布实现是基于基础的“最后写入胜出”（last-write-wins）冲突解决机制构建的。

遗憾的是，Jye 和我通过惨痛的教训发现，我们关于冲突解决的假设过于天真了。在使用 Suga 的早期版本时，我们在没有意识到的情况下开始同时处理同一个共享项目。我当时正在添加一个服务，以及它的 Postgres 数据库、配置、环境变量，并调整位置以使布局合理。Jye 则在项目的另一端，添加函数并编写集成代码。

当你工作时，更改会自动保存为草稿，因此每当我们移动节点或添加连接时，草稿都会更新。然而，因为没有合并机制，每次保存只是用客户端拥有的任何内容替换了整个草稿。我的保存悄无声息地覆盖了 Jye 的工作，而他的保存又覆盖了我的。当 Jye 刷新浏览器标签页时，他构建的一切都消失了，因为我做了最近的更改，最后的草稿写入是我的。我们确实会自动跟踪项目的历史记录，但仅针对已部署的更改，由于这些内容尚未部署，所以就直接丢失了。

这清楚地表明，针对整个画布的“最后写入胜出”策略是行不通的。虽然我们可以通过其他锁定/冲突解决技术来改善情况，但我们知道最终需要完整的多人协作，因此实时同步才是正确的选择。

## 你关注过同步引擎吗？

如果你对同步引擎不熟悉，Jye 去年对此变得非常痴迷，并[写了一篇相关的博文](https://bytemash.net/posts/i-went-down-the-linear-rabbit-hole/)。我最近也看了一个 [Syntax 视频](https://www.youtube.com/watch?v=_tHSAKVCJQo)，视频中他们使用 Zero 构建了一个竞争性编程游戏，那种同步模型让我瞬间开窍。在下一次站会中，我们都同意需要放下其他功能，把这个做出来。

我们最终选择了 [Zero](https://zero.rocicorp.dev/)，这是来自 Rocicorp 的同步引擎。简单来说，每个客户端都有一个本地 SQLite 数据库，并与服务器上的 PostgreSQL 保持同步。写入首先在本地发生，然后在服务器上重演；如果存在冲突，以服务器为准，客户端会自动进行协调。

为什么选择 Zero 而不是其他方案？像 Yjs 和 Automerge 这样的 CRDT 库是为文档型协作（如文本编辑器和绘图工具）设计的。而我们的[数据是关联性的](https://thenewstack.io/dont-let-time-series-data-break-your-relational-database/) Postgres 行，包括一些较大的 JSONB 列。像 ElectricSQL 和 PowerSync 这样的工具也可以同步 Postgres，但 Zero 的 [mutator](https://zero.rocicorp.dev/docs/mutators) 模型让我们能够对 JSON 值的冲突解决进行细粒度控制。

## 两种类型的更改

我们很早就意识到，并非所有更改都是对等的；有些可以合并，有些不能，还有一些可以忍受“最后写入胜出”。弄清楚哪些属于哪一类，成为了核心的设计问题。画布是基于 [React Flow](https://reactflow.dev/) 构建的，每一次改变状态的交互都会通过一个 Zero mutator。

> “弄清楚哪些属于哪一类，成为了核心的设计问题。”

![改变状态的交互图示，通过 Zero mutator 进行。](https://cdn.thenewstack.io/media/2026/04/43e36fed-11-1024x654.png)

### 细粒度 mutator

为了简单起见，画布节点的位置存储为单个 JSON 值。我们想要的是当我拖动一个节点时，只有该节点的位置发生变化。如果有人同时拖动另一个节点，两次写入都能顺利完成，不会产生冲突。如果我们以某种方式同时拖动同一个节点，则最后写入者胜出，因为对于节点位置来说，这没问题，既没有有意义的合并方式，数据也不至关重要。如果我将节点放在 (400, 200)，而 Jye 将其放在 (600, 300)，我们中的一个人会胜出。

以下是处理节点位置的 mutator 代码：

```typescript
export const updateNodePosition = defineMutator(
  z.object({ environmentId: z.string(), nodeId: z.string(), position: PositionSchema }),
  async ({ tx, ctx, args: { environmentId, nodeId, position } }) => {
    // 权限检查仅在服务器端运行
    if (tx.location === "server") {
      await verifyAccess(tx, environmentId, ctx.activeOrganizationId);
    }

    const env = await getEnvironment(tx, environmentId);

    // 展开现有位置，仅覆盖此节点
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

展开（spread）操作是关键部分：我们读取当前位置并仅覆盖那一个节点。在客户端，这从本地缓存读取；在服务器端，它从数据库读取。两者运行相同的函数，但服务器的视图具有权威性。

> “展开操作是关键部分：我们读取当前位置并仅覆盖那一个节点……服务器的视图具有权威性。”

类似的模式也适用于基础设施的更改，这解决了我们的覆盖问题。当我添加一个服务时，mutator 读取当前的计算数组，追加我的更改，然后写回。如果有人同时添加一个函数，他们的 mutator 也会执行同样的操作。服务器重演这两者，结果就会包含这两项更改。

```typescript
export const addCompute = defineMutator(
  z.object({
    environmentId: z.string(),
    compute: ComputeSchema,
    position: PositionSchema.optional(),
  }),
  async ({ tx, ctx, args: { environmentId, compute, position } }) => {
    // ... 同样的权限检查模式

    const env = await getEnvironment(tx, environmentId);
    const def = env?.draftDefinition;

    // 读取当前计算资源，追加新的，写回
    const updatedDef: ProjectDefinition = {
      version: "v1",
      computes: [...def.computes, compute],
      volumes: def.volumes,
    };

    await tx.mutate.environment.update({
      id: environmentId,
      draftDefinition: updatedDef,
      // ... 如果提供了位置，也会在画布上设置节点位置
    });
  },
);
```

我们考虑过[使用 CRDT](https://thenewstack.io/fireproof-uses-merkle-crdts-to-cut-database-latency/) 来合并这些更改，但我们的数据模型需要大量工作才能分解为 CRDT 友好的结构。[构建自定义](https://thenewstack.io/custom-integrations-for-complex-scenarios-7-best-practices/) CRDT 会增加复杂性，但在位置的“最后写入胜出”或计算资源的“读取-修改-写入”模式面前，并无明显的优势。

### 批量 mutator

某些操作无法细粒度化；例如，`undo` 会用之前的快照替换整个画布。部署和舍弃操作也是如此。

```typescript
export const updateDraftAndCanvas = defineMutator(
  z.object({ environmentId: z.string(), draftDefinition: ProjectDefinitionSchema, canvasMetadata: CanvasMetadataSchema }),
  async ({ tx, ctx, args: { environmentId, draftDefinition, canvasMetadata } }) => {
    // ... 同样的权限检查

    // 没有展开，没有合并。直接替换所有内容。
    await tx.mutate.environment.update({
      id: environmentId,
      draftDefinition,
      canvasMetadata,
    });
  },
);
```

目前这里没有合并；快照胜出。对于撤销操作来说，这是一个正确的权衡，因为其意图就是“精确回到这个状态”。

## Drizzle 作为架构的单一事实来源

我们使用 [Drizzle](https://orm.drizzle.team/) 作为 ORM。其架构定义同时充当 Zero 同步架构的单一事实来源。

```typescript
export const environment = pgTable('environment', {
  id: uuid('id').primaryKey().defaultRandom(),
  projectId: uuid('project_id').references(() => project.id),
  canvasMetadata: jsonb('canvas_metadata').$type<CanvasMetadata>(),
  draftDefinition: jsonb('draft_definition')
    .default(InitialProjectDefinition)
    .$type<ProjectDefinition>(),
  // ...
});
```

两个 JSONB 列保存协作状态：`canvasMetadata` 用于位置和便签，`draftDefinition` 用于基础设施图。另一种选择是规范化到单独的表中，这将提供零行级别的差异。我们目前选择 JSONB 是因为它更简单，而且 mutator 级别的合并已经给了我们足够的控制权。如果我们遇到扩展性问题，规范化将是显而易见的下一步。

我们遇到的一些坑：

*   JSONB 是复制单元，Zero 不会对 JSON 内部进行差异对比，这就是为什么细粒度 mutator 要采用那种展开模式。
*   如果你在架构迁移后忘记重新生成，客户端会静默地遗漏新列而没有错误，导致数据丢失。
*   我们必须编写自定义脚本来创建 Zero 发布（publications）和过滤器。正确配置发布内容需要几轮调试，以确定哪些内容需要复制，哪些不需要。

## 用于本地状态的 Nanostores

Zero 处理同步状态，但某些状态仅属于客户端，例如用户特定的撤销历史；为此，我们使用 Nanostores。这些存储库实际上只是消费 Zero 数据的一种只读方式，由 Zero 处理所有变更，然后与存储库同步。[Nanostores](https://github.com/nanostores/nanostores) 非常轻量，能够干净地处理全局可访问的状态部分。

```typescript
export const $nodePositions = map<Record<string, Position>>({});
export const $stickyNotes = atom<StickyNote[]>([]);
export const $draftDef = atom<ProjectDefinition>(InitialProjectDefinition);
export const $undoState = atom<UndoState>({ past: [], future: [] });
```

对于撤销，我们在每次有意义的更改前捕获一个完整快照，并将其存储在包含 20 个项目的历史堆栈中。撤销操作会在本地恢复快照，并通过 Zero 触发一个批量 mutator 以同步给其他客户端。

## 本地运行正常，部署后报错

在本地运行 Zero 非常顺利；我们只需运行一个 compose 文件进行本地开发，CLI 就会从 Drizzle 自动生成架构。我向团队演示了它，每个人都能看到彼此的更改、实时出现的节点等等。它成功运行了，我感觉非常棒。

我们部署到预发环境（staging），它立刻就挂了。

### 隐蔽的 401 错误

我们的预发和预览部署启用了部署保护。Zero-cache 作为一个独立的服务器运行，需要调用主应用程序上的 `/api/zero/query` 和 `/api/zero/mutate`。部署保护以 401 错误阻止了这些请求。

令人沮丧的是，在浏览器中，看起来并没有明显的异常。故障发生在 Zero 和我们其他端点之间，而不是在浏览器的网络标签页中。我不得不调出工作负载日志才能看到不断堆积的实际错误。一旦我发现了它们，修复方法就是在查询和变更请求中添加适当的请求头。

### Cookie 问题

Zero 默认使用基于 Cookie 的身份验证，而我们的预览和预发环境会为每个 PR 生成新的临时 URL。Cookie 是作用于域名的，每个预览部署都有一个新域名，这使得 Cookie 认证基本上无法可靠运行。

对于本地和预发环境，我们通过 `ZeroProvider` 组件上的 `auth` 属性直接传递会话令牌，而不是依赖 Cookie，而生产环境仍然使用 Cookie。虽然这在认证路径上造成了一点分歧，但它是支持我们使用预览部署方式的一种可靠方案。

## 现已上线

自从添加了用于同步和冲突解决的 Zero 之后，Suga 用户现在可以同时在同一个项目中工作。如果你对我们如何改善你的体验有任何反馈，请联系我们。我们一直在寻找改进的方法。