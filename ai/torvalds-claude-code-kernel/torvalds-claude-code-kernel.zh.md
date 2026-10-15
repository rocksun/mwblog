Linux 创始人兼长期首席维护者 [Linus Torvalds](https://www.linkedin.com/in/linustorvalds/) 利用 Anthropic 的 Claude Code 解决了一个困扰开发者两年多的内核性能问题。周二，他[提交了一组包含 10 个补丁的系列代码](https://lkml.iu.edu/2610.1/13146.html)，在其 Ryzen Threadripper 上运行的综合基准测试中，吞吐量实现了 23 倍的提升。

Torvalds 曾花了一年半的时间运行他自己修复页面缓存引用计数瓶颈的残缺版本，而其他开发者在尝试他们的方法时也遇到了问题。新的补丁从常见的缓冲读路径中消除了 folio 引用计数操作，尽管 Torvalds 警告说，在真实工作负载中，基准测试的收益会小得多。

此后，审查人员发现了一个竞态条件，并对内存回收提出了担忧。Torvalds 已将进一步的开发交给了 [Kiryl Shutsemau](https://www.linkedin.com/in/kiryl-shutsemau-78153330/)，他是一位曾参与解决同一瓶颈的 Linux 内核开发者。

> Torvalds 曾花了一年半的时间运行他自己修复页面缓存引用计数瓶颈的残缺版本，而 other 开发者在尝试他们的方法时也遇到了问题。

## 页面缓存争用问题

[据 Hardware Busters 报道](https://hwbusters.com/news/linus-torvalds-uses-claude-code-to-rework-the-linux-page-cache-tripling-small-read-throughput/)，在 Torvalds 的 Core i7-8565U 笔记本电脑上，在八线程测试中，folio 引用计数争用占了跨核心负载 HITM 的 99.92%。

Oracle 工程师兼长期 Linux 内核内存管理开发者 Matthew Wilcox 在客户工作负载中浮出水面后，于 2024 年标记了这一瓶颈。

## Claude Code 编写补丁

周日，Phoronix 的 [Michael Larabel](https://www.linkedin.com/in/michaellarabel/) 在 Torvalds 的代码树中发现了一个名为 `noref-filemap-read-with-llm` 的实验性分支，该分支极少包含主开发分支之外的内容。

这组基于 Linux 7.3-rc6 的八个补丁，附带了对 Claude Code 所做工作的清晰说明。Torvalds 表示，在她的指导下，这个智能体编写了实现、测试和初始文档，并审查了代码。尽管他之前曾[批评开发者声称 AI 编写了他们 99% 的代码](https://thenewstack.io/torvalds-ai-programming-productivity/)，但他还是亲自运行了基准测试。

早期的方法在不持有 folio 引用的情况下复制数据并随后检查其有效性，这留下了涉及回收和替换的竞态。随后的 10 个补丁构成的 `rcu-free-v3` 系列转而使用新的 `PG_rcu_free` 标志和 RCU 延迟回收，以在不发生故障的情况下通过用户空间复制来保护 folio。

> 早期的方法在不持有 folio 引用的情况下复制数据并随后检查其有效性，这留下了涉及回收和替换的竞态。

## Threadripper 基准测试结果

[据 Hardware Busters 报道](https://hwbusters.com/news/linus-torvalds-uses-claude-code-to-rework-the-linux-page-cache-tripling-small-read-throughput/)，最初的八个补丁分支使 Torvalds 笔记本电脑上的吞吐量几乎翻了两番，将八线程性能从每秒 1000 万次读取推高至多达 3300 万次，同时将每次读取的内核周期从大约 2950 个削减至 725 个。在拥有 64 线程的 Threadripper 的高争用情况下，修改后的系列带来了更大的收益，吞吐量从每秒 1330 万次跃升至 3.04 亿次读取，每次读取的周期从近 20,000 个下降到 735 个。

> 最初的八个补丁分支使 Torvalds 笔记本电脑上的吞吐量几乎翻了两番，将八线程性能从每秒 1000 万次读取推高至多达 3300 万次，同时将每次读取的内核周期从大约 2950 个削减至 725 个。

性能的提升伴随着权衡。在第一次实现中，每当 CPU 排队超过 1,024 个页面时，延迟回收就会强制加速宽限期。读取未映射的用户页面也会在退回到现有路径之前触发额外的故障，从而将 16 字节的单线程读取从大约 4,150 个周期推高到 6,550 个周期。这种回归是否在 `rcu-free-v3` 中持续存在尚不清楚。

## 维护人员对回收设计提出质疑

Wilcox 对新的 `PG_rcu_free` 标志提出质疑，并建议改用页面类型，以及在 RCU 宽限期后回收非活动列表 folio。

Torvalds 拒绝了这两种方法，他认为必须在 folio 仍可映射到用户空间时设置该标志，并且非活动列表回收无法涵盖截断和打孔操作。Shutsemau 随后建议将该标志限制在 64 位系统上，这一方法得到了 Arm 工程师兼 Linux 内存管理维护人员 [David Hildenbrand](https://www.linkedin.com/in/david-hildenbrand-73416154/) 的支持。

Shutsemau 还指出了 `filemap_read_rcu_batch()` 中的一个竞态，其中 folio 替换后跟对 `i_size` 的扩展可能会暴露从未写入的数据。Torvalds 建议更早地读取文件大小并合并 folio 检查，Shutsemau 将这些建议合并到了修改后的补丁中。