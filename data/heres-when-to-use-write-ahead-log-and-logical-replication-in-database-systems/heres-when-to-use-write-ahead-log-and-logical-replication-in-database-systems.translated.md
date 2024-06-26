# 何时在数据库系统中使用预写式日志和逻辑复制

![用于：何时在数据库系统中使用预写式日志和逻辑复制的特色图片](https://cdn.thenewstack.io/media/2024/06/615ca37a-alphabets-1839737_1280-1024x682.jpg)

在数据库复制方面，两种广泛使用的方法是预写式日志 (WAL) 和逻辑复制。这些技术对于：

- [维护数据可用性](https://thenewstack.io/maintaining-data-resiliency-in-the-age-of-kubernetes/)
- 促进灾难恢复
- [扩展数据库系统](https://thenewstack.io/techniques-for-scaling-applications-with-a-database/)

至关重要。由于结构、功能和实际应用的不同，需要不同的策略来掌握它们的优点和局限性。

## 预写式日志 (WAL)

预写式日志 (WAL) 这种方法通常用于数据库系统中，例如 [PostgreSQL](https://thenewstack.io/postgresql-takes-a-new-turn/)。它涉及利用存储在 WAL 文件中的修改流，将数据从数据库复制到一个或多个辅助副本。以下是它的分解方式：

在 WAL 中，主数据库通过在数据文件中最终确定所有更改之前将其记录到其预写式日志 (WAL) 文件中来保证持久性。然后，辅助副本从服务器获取这些 WAL 文件，并按顺序将其应用到它们自己的数据文件中。这种复制技术需要辅助服务器之间的异步通信，以维护整个系统中数据的 [一致性和可靠性](https://thenewstack.io/its-time-for-data-reliability-engineering/)。

WAL 通过从数据库的事务日志中复制更改来维护 [数据完整性和一致性](https://thenewstack.io/change-data-capture-for-real-time-access-to-backend-databases/)。此过程确保复制的数据与数据保持同步，从而确保整个过程的完整性。此外，WAL 支持时间点恢复，允许备用服务器重放特定时间段的 WAL 文件，从而在发生故障或数据损坏时实现恢复。在主服务器不可用的故障转移事件中，WAL 通过使用最新的 WAL 文件提升备用服务器成为新的主服务器，从而实现转换，以持续运行。

WAL 通过复制主数据库事务日志中的更改来维护数据完整性和一致性，从而在复制期间保持数据完整性。此方法还会影响数据库的性能，因为更改首先记录在 WAL 文件中，然后才应用到数据文件中。这种方法允许主数据库高效运行并在负载下写入。此外，WAL 非常适合灾难恢复场景，因为备用服务器会不断更新数据库中的更改，确保它们是最新的，并准备好在服务器故障时接管。确保数据库系统的可靠备份 [计划可保证灾难恢复](https://thenewstack.io/supercharge-your-disaster-recovery-plan-in-5-simple-steps/) 措施。

在使用 WAL 时，为了使复制有效，必须意识到一些缺点。有时，由于网络延迟或高活动级别，备用副本落后于服务器时，可能会发生复制滞后。此滞后会导致备用服务器上的数据出现差异，从而影响数据一致性。此外，在某些情况下，可能需要手动步骤将服务器指定为新的主服务器。此手动过程可能会导致延迟。它需要参与，可能会延长恢复操作所需的时间。

## 逻辑复制

另一方面，逻辑复制是一种用于 PostgreSQL、MySQL 和 [MongoDB](https://thenewstack.io/mongodb-vs-scylladb-performance-scalability-and-cost/) 等数据库系统中的技术。它在复制 SQL 语句或数据修改的级别上运行。与在字节级别复制更改的 WAL 不同，逻辑复制提供了一种 [同步数据的方法](https://thenewstack.io/the-zero-trust-approach-to-data-management/)。此方法由于其设计和功能而具有不同的优点和挑战。

在复制中，主数据库将一组更改（可能包括 SQL 语句或行修改）发送到副本服务器。这些更改集通常通过副本服务器之间的复制连接传输。在收到这些更改集后，副本服务器通过执行 SQL 语句或应用修改将其实现到它们的数据集中。此方法允许备份服务器通过镜像其数据集中的更改来保持与数据库的更新。逻辑复制通常在发布者向订阅者分发更改的模型上运行，从而实现复制设置和可扩展性选项。
### 与 WAL 等方法相比，逻辑复制提供了优势。

- 首先，它提供了复制的优势，允许复制表或数据库，而不是所有更改，从而提高了灵活性和效率。
- 其次，它支持复制，促进了不同类型数据库之间的同步，这在具有多样化系统的环境中特别有用。
- 此外，逻辑复制授予对复制行为的控制，包括冲突解决和数据转换，从而实现准确的数据同步管理。
- 根据设置，逻辑复制可以异步或同步运行，提供根据要求优先考虑性能或数据一致性的选项。
- 这些功能将复制确立为在分布式系统中维护同步数据的强大工具。

### 逻辑复制为管理员提供了一定的适应性，允许他们选择要复制哪些数据以进行有针对性的同步。

- 此功能通过复制表或数据库并减少不必要的工作负载来简化流程。
- 此外，它对复制的支持促进了数据库类型之间的同步——促进了组织内不同系统之间的无缝数据迁移和集成。
- 此外，通过复制过程中的数据转换，逻辑复制允许在必要时进行格式调整或数据清理。
- 此功能确保信息在系统中保持统一和兼容，从而提高数据质量和可用性。

### 虽然逻辑复制提供了好处，但也带来了一系列挑战。

- 首先，与 WAL 等方法相比，它通常需要资源。解析和执行 SQL 命令的过程会影响系统性能。
- 此外，如果复制过程因事务负载或网络延迟而落后，则有可能出现数据不一致，这可能导致主数据库和备份数据库之间出现差异。
- 配置和管理复制设置可能比使用 WAL 等方法更复杂。此复杂性要求规划和监控以确保复制系统的操作。

## 比较 WAL 和逻辑复制

- WAL 通常因其成本而受到青睐，因为它以字节级复制更改，这更有效率。
- 另一方面，逻辑复制可能会导致开销，尤其是在处理大量数据或复杂 SQL 命令时。
- 这种增加的成本可归因于解析和处理 SQL 命令的必要性，在发生重大数据修改或使用复杂查询的情况下，这会消耗资源。

## 数据一致性

- WAL 通过从事务日志复制更改来保证数据一致性，确保副本与主数据库保持同步。
- 相比之下，逻辑复制可能会表现出一致性，主要是在从数据库复制更改时出现延迟。
- 这可能导致在主数据库上进行更改和在副本上反映更改之间的时间间隔，从而可能导致两个数据库之间出现差异。
- 尽管如此，一旦复制赶上，数据一致性将重新建立。

## 灵活度

- 逻辑复制以其在选择要复制的数据和支持环境类型方面的适应性和灵活性而闻名。
- 通过复制，管理员可以选择要复制的表或数据库，根据他们的要求自定义同步。
- 此外，它支持数据库类型之间的复制，简化了跨平台的数据迁移和系统集成的过程。
- 另一方面，WAL 遵循数据复制的方法。它以字节级复制所有更改，而无法选择性地复制数据元素。
- 此外，它需要在备用服务器上使用数据库引擎，这限制了它在具有混合数据库技术的环境中的有效性。

## AWS RDS PostgreSQL 的主动-主动复制扩展

- Amazon RDS 上 PostgreSQL 的 PGActive 主动-主动复制扩展允许多个 RDS 实例同时处理读写操作，通过复制和冲突解决技术确保数据一致性。
- 此扩展允许管理员选择性地复制数据并支持环境以及自动化 Amazon RDS 上 PostgreSQL 数据库的故障转移和负载平衡功能，以实现可用性和可扩展性。

## 结论
### 预写日志 (WAL) 和逻辑复制

预写日志 (WAL) 和逻辑复制在实现数据库系统中的可用性、灾难恢复和可扩展性方面发挥着作用。

**WAL** 非常适合优先考虑数据一致性且对性能有影响的场景，例如灾难恢复设置。

**另一方面，逻辑复制**提供了对复制行为的灵活性与控制，使其非常适合具有不同需求的复杂环境。架构师和管理员必须了解差异，才能设计出有弹性的数据库复制设置。

建议将预写日志 (WAL) 与复制结合起来，在混合一致性模型中，这适用于需要容错的高弹性系统。