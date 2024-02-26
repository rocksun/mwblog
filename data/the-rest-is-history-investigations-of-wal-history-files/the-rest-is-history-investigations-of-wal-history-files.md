<!--
title: 历史就在这里：WAL历史文件的调查
cover: ./cover.png
-->

PostgreSQL使用时间线的概念来识别一系列WAL记录在时间和空间上的标识。每个时间线都由一个数字标识，在某些地方是十进制，在其他地方是十六进制。每次使用基于时间点的恢复恢复数据库时，有时在备用/复制推广期间，都会生成一个新时间线。

> 译自 [The Rest is History: Investigations of WAL History Files](https://www.crunchydata.com/blog/the-rest-is-history-investigations-of-wal-history-files)，作者 Brian Pace。

一个常见的错误是假设较高的时间线号同义于最新的数据。虽然最高的时间线指向数据库的最新版本，但它不能保证数据库确实持有从应用程序的角度来看最有用的数据。为了判断这一说法的有效性，仔细检查写前日志(WAL)历史文件是必不可少的，揭开它们所传达的信息。

在本次讨论中，我们将探索一个恢复的数据库，并追踪历史文件中嵌入的叙述。到最后，您将对Postgres中这些历史文件的功能有了更深入的洞察，这将使您能够解答与恢复过程和数据库的历史之旅(或者我可以称之为“家谱”)相关的查询。

## 评估当前状态

让我们开始通过洞悉数据库的当前状态来开始。从`pg_controldata`输出获得的信息表明，数据库当前位于时间线11上。请注意最新的检查点写前日志(WAL)文件，标识为“0000000B0000000100000039”。参见我之前关于[WAL文件命名和编号的文章](https://www.crunchydata.com/blog/postgres-wal-files-and-sequuence-numbers)。

值得注意的是，时间线有时以十进制形式表示，如11的情况，有时以十六进制形式表示，如“0000000B”。虽然这种双重表示形式最初可能会令人困惑，但熟悉这些不同形式的使用时间和地点将有助于更清楚地理解。

```bash
$ pg_controldata
...
pg_control last modified:             Tue 06 Feb 2024 03:10:53 PM EST
Latest checkpoint location:           1/39000060
Latest checkpoint's REDO location:    1/39000028
Latest checkpoint's REDO WAL file:    0000000B0000000100000039
Latest checkpoint's TimeLineID:       11
...
```

另一个需要考虑的关键方面是检查pg_wal目录的内容，以识别存在的历史文件。如果当前数据库在创建时间线11时不是主数据库，则可能只存在最新的历史文件。在这种情况下，我们正在调查的服务器是并且仍然是主Postgres实例。

```bash
$ ls -1 $PGDATA/pg_wal/*.history
00000003.history
0000000A.history
0000000B.history
```

乍一看，人们可以假设时间线11(请记住，历史文件和段文件使用十六进制)的家谱来自时间线10(0000000A)和3(00000003)。对于任何假设，我们必须在确认此假设为事实之前对其进行验证。为此，让我们看一下时间线11的历史文件内容。

```bash
$ cat 0000000B.history

1	0/710000A0	no recovery target specified

2	0/72000000	no recovery target specified

3	1/22000CE0	before 2024-02-03 00:37:49.381764-05

10	1/230000A0	no recovery target specified
```

查看历史文件内容，我们可以看到时间线11的“家谱”。时间线11是从时间线10在LSN 1/230000A0创建的。时间线10是从时间线3在LSN 1/22000CE0创建的。等等! 4到9之间的时间线怎么样了？“没有指定恢复目标”和“在2024-02-03 00:37:49.381764-05之前”是什么意思？这些都是正确的问题。让我们继续探索。

## 历史文件内容

从时间线11的历史文件顶部开始，我们从上至下读取列表以查看家谱。“没有指定恢复目标”让我们知道该时间线很可能是从提升(例如**select pg_promote()**)创建的。另一方面，时间线10是针对时间线3执行基于时间点的恢复而创建的。时间戳从哪里来？那是否是最后一个事务的时间戳？更多非常好的问题。让我们来探讨这些问题。

我们需要做的第一件事是检查创建时间线10的WAL段的内容。在这种情况下，时间线10是从时间线3在LSN 1/22000CE0创建的。[将LSN转换为](https://www.crunchydata.com/blog/postgres-wal-files-and-sequuence-numbers)确切的WAL段给我们000000030000000100000022。斜杠前的LSN中的数字是“高位数”，而斜杠后的前几个字符是低位数。这两个由时间线作为前缀的数字给出了WAL段名称(记住是十六进制)。下面是该段pg_waldump的摘录。

```bash
$ pg_waldump 000000030000000100000022
rmgr: Standby     len (rec/tot):     50/    50, tx:          0, lsn: 1/22000028, prev 1/21000138, desc: RUNNING_XACTS nextXid 1035 latestCompletedXid 1034 oldestRunningXid 1035
rmgr: Heap        len (rec/tot):     61/  1666, tx:       1035, lsn: 1/22000060, prev 1/22000028, desc: DELETE xmax: 1035, off: 4, infobits: [KEYS_UPDATED], flags: 0x00, blkref #0: rel 1663/5/16684 blk 0 FPW
rmgr: Heap2       len (rec/tot):   1460/  1460, tx:       1035, lsn: 1/220006E8, prev 1/22000060, desc: MULTI_INSERT ntuples: 1, flags: 0x02, offsets: [5], blkref #0: rel 1663/5/16684 blk 0
rmgr: Heap2       len (rec/tot):     63/    63, tx:       1035, lsn: 1/22000CA0, prev 1/220006E8, desc: PRUNE snapshotConflictHorizon: 1034, nredirected: 0, ndead: 4, nunused: 0, redirected: [], dead: [1, 2, 3, 12], unused: [], blkref #0: rel 1663/5/16684 blk 0
rmgr: Transaction len (rec/tot):     34/    34, tx:       1035, lsn: 1/22000CE0, prev 1/22000CA0, desc: COMMIT 2024-02-03 00:37:49.381764 EST
rmgr: Standby     len (rec/tot):     50/    50, tx:          0, lsn: 1/22000D08, prev 1/22000CE0, desc: RUNNING_XACTS nextXid 1036 latestCompletedXid 1035 oldestRunningXid 1036
rmgr: XLOG        len (rec/tot):     24/    24, tx:          0, lsn: 1/22000D40, prev 1/22000D08, desc: SWITCH
```

在LSN 1/22000CE0是创建时间线10的位置。从上面可以看出，该位置有一个提交的时间戳为“2024-02-03 00:37:49.381764 EST”(LSN的最后一组字符是WAL段内的偏移量)。WAL历史文件告诉我们时间线10是在此提交之前创建的(“before ...”)。在CE0提交的任何事务都不会在时间线10中。

那么，为什么这个时间戳很重要呢？为了理解这一点，让我先提供一些背景信息。传递给 pgBackRest 用于恢复到某一时间点的时间戳是 '2024-02-03 00:30:10 EST'。在 CE0 提交的是我们恢复目标时间之后的第一个事务。因此，历史文件显示的是 '在 2024-02-03 00:37:49.381764 EST 之前'。

在我们继续之前，还有一件事要说。历史文件为我们提供的最后一条信息是时间线 11 是由时间线 10 创建的。基于 '未指定恢复目标'，我们可以安全地假设这是由于升级类型事件或恢复后没有更多的 WAL 段被知晓或可用。

## 缺失的时间线

那么时间线 4 - 9 呢？别担心，我没有忘记这个问题。为了获取这些时间线的历史文件，我们需要去 pgBackRest 存储库。为了检索它们，我将执行类似以下语句来从 pgBackRest 中恢复它们：

```bash
$ pgbackrest archive-get 00000004.history --stanza=rhino /app/pgdata/rhino.16/pg_wal/00000004.history
```

类似的步骤会对时间线 4 - 9 进行重复。我们将从时间线 9 的历史文件开始我们的调查。以下是其内容：

```bash
$ cat 00000009.history
1	0/710000A0	no recovery target specified

2	0/72000000	no recovery target specified

3	3/DA0000A0	no recovery target specified

4	3/DB0000A0	no recovery target specified

5	3/DC000000	no recovery target specified

6	5/2E0000A0	no recovery target specified

7	5/300000A0	no recovery target specified

8	5/570000A0	no recovery target specified
```

从上面可以看出，从时间线 1 到 9 有一个正常的进展（表示没有恢复）。这并不意味着，例如时间线 4，过 LSN 3/DB0000A0 后就没有任何更新。这是一个不同博客主题的不同话题。如果我们能够绘制我们的时间线，它看起来会像这样：

![WAL 历史树](https://imagedelivery.net/lPM0ntuwQfh8VQgJRu0mFg/ba555588-5228-4355-6ae1-aa92f6a33f00/public)

我们的旅程已经进行得很顺利。然而，在我们回答关于哪个时间线具有最新数据的开头问题之前，我们需要知道时间线 10 和 11 存在了多久。为了做到这一点，我们将再次使用 **pg_waldump** 对时间线 10 的起始 WAL 段进行转储（提示，将使用不同的时间线前缀相同的段名称）。看一下这个段的内容：

```bash
$ pg_waldump 0000000A0000000100000022
rmgr: Standby     len (rec/tot):     50/    50, tx:          0, lsn: 1/22000028, prev 1/21000138, desc: RUNNING_XACTS nextXid 1035 latestCompletedXid 1034 oldestRunningXid 1035
rmgr: Heap        len (rec/tot):     61/  1666, tx:       1035, lsn: 1/22000060, prev 1/22000028, desc: DELETE xmax: 1035, off: 4, infobits: [KEYS_UPDATED], flags: 0x00, blkref #0: rel 1663/5/16684 blk 0 FPW
rmgr: Heap2       len (rec/tot):   1460/  1460, tx:       1035, lsn: 1/220006E8, prev 1/22000060, desc: MULTI_INSERT ntuples: 1, flags: 0x02, offsets: [5], blkref #0: rel 1663/5/16684 blk 0
rmgr: Heap2       len (rec/tot):     63/    63, tx:       1035, lsn: 1/22000CA0, prev 1/220006E8, desc: PRUNE snapshotConflictHorizon: 1034, nredirected: 0, ndead: 4, nunused: 0, redirected: [], dead: [1, 2, 3, 12], unused: [], blkref #0: rel 1663/5/16684 blk 0
rmgr: XLOG        len (rec/tot):     42/    42, tx:          0, lsn: 1/22000CE0, prev 1/22000CA0, desc: END_OF_RECOVERY tli 10; prev tli 3; time 2024-02-06 13:25:33.877840 EST
...
```

根据上述内容，数据库的恢复在东部标准时间下午 1:25 PM（美国东部时间）于 2024 年 2 月 6 日完成。这意味着数据库（时间线 10 和 11）现在包含了 2 小时的应用更改（假设应用程序立即在恢复后恢复）。现在，让我们将这与时间线 9 中的最后一个 WAL 段进行比较：

```bash
$ pg_waldump 000000090000000500000057
...
rmgr: Transaction len (rec/tot):     34/    34, tx:       1661, lsn: 5/570032B0, prev 5/57002B28, desc: COMMIT 2024-02-06 13:23:51.110938 EST
rmgr: Standby     len (rec/tot):     50/    50, tx:          0, lsn: 5/570032D8, prev 5/570032B0, desc: RUNNING_XACTS nextXid 1662 latestCompletedXid 1661 oldestRunningXid 1662
...
```

我们可以通过查看 PostgreSQL 日志和/或 pgBackRest 存储库来确定最新的 WAL 段。在本例中，WAL 段 000000090000000500000057 是最新的。此段已经恢复，上面的 **pg_waldump** 显示最后提交的事务发生在东部标准时间下午 2/6/24 1:23:51。这意味着时间线 9 有 84 小时多一点的应用程序更改。这是通过测量时间线 11 的历史文件中 'before' 时间戳（它从时间线 3 分叉的时间）和时间线 9 中的最后一个事务之间的差异来确定的。

回到我们的问题。时间线 11 是否具有最新数据？也许，它最多有几小时的更后处理数据，但要接受这一点意味着失去 84 小时的数据。

## 总结

时间线历史文件加上一些方便的调查工作可以告诉我们数据库“家谱”的故事。如果您被要求恢复数据库，现在您可以对哪个时间线可能包含从业务角度来看最有用的数据做出一些明智的选择。

在执行恢复、重新初始化备用或副本之前，以下是一些有用的步骤，以帮助您进行调查以确定从业务角度来看什么时间线具有最有用的数据:

- 查看pg_controldata以查看数据库当前位于哪个时间线上
- 查看$PGDATA/pg_wal/*.history中存在的WAL历史文件
- 如有必要，从备份存储库/位置恢复丢失的*.history文件
- 查看时间线的创建时间
- 检查WAL段的内容
