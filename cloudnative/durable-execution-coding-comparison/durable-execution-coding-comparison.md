<!--
title: DBOS：十倍代码精简，应用稳如磐石！
cover: https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67dbba9ed505e94c43290996_Durable-Execution-DBOS-vs-Temporal.jpg
summary: 持久性执行确保应用中断后恢复。外部编排（如Temporal）需重构应用、增服务；嵌入式库（如DBOS）集成简便，代码改动少，不改架构。
-->

持久性执行确保应用中断后恢复。外部编排（如Temporal）需重构应用、增服务；嵌入式库（如DBOS）集成简便，代码改动少，不改架构。

> 译自：[Making Apps Durable with 10x Less Code | DBOS](https://www.dbos.dev/blog/durable-execution-coding-comparison)
> 
> 作者：Peter Kraft

严肃的应用程序会使数据具有**持久性**；它们将数据存储在磁盘或数据库中，这样即使程序因任何原因停止工作，数据也不会立刻消失。但应用程序本身呢？假设您的服务器正在处理酒店预订，当它重新启动时，预订处理了一半。预订会发生什么？或者，如果您的服务器正在摄取 10,000 份文档进行 AI 分析，但在完成 4,000 份后重新启动了怎么办？剩下的 6,000 份文档会发生什么？

**持久性执行**有助于解决这些问题。其理念是定期将应用程序的状态检查点保存到持久性存储（如数据库）中，这样如果应用程序出现故障、崩溃或中断，它可以使用其检查点状态从中断处恢复。这样，数据不会丢失，并且进程——尤其是耗时的批处理作业——不必从头开始。

大多数持久性程序都被编写为**步骤**的**工作流**。每个步骤接收输入，执行一些工作，并返回输出。工作流将所有步骤连接起来。持久性执行系统会持久化工作流的状态（哪些步骤已完成以及它们的输出是什么），这样如果应用程序中断，所有工作流都可以从它们上次完成的步骤恢复。

![持久性执行工作原理图](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d92484dbfd039ce77b_AD_4nXfB0sV0DXrhRAfJvfLm784u_Jhdqnj8igxk802o8ZoanK7vPkLznsbMlz-mA-q5fQxBsYjH8KfDlhaHCB5VbdWFyODd3abLikmOiUYk5Fv9_TpH1fS7t2cmwXWPYyFWmLcLUCc2RA.png)

### 外部与嵌入式持久性执行

实现持久性执行有两种主要方法：

*   **外部编排**系统使用**编排器**和**工作器**将持久性工作流的定义和执行与您的应用程序分开。编排器管理工作流执行，将步骤分派给工作器。工作器执行步骤，然后将输出返回给编排器。编排器持久化每个步骤的输出，然后分派下一个步骤。通常，编排器和工作器在不同的服务器上运行，并通过消息传递进行通信。
*   **嵌入式持久性执行**系统通过**开源库**集成到您的应用程序代码中。开发人员在应用程序中注释工作流和步骤。当应用程序运行时，库会将工作流和步骤的状态持久化到数据存储中。如果应用程序以任何方式中断，库会在应用程序重新启动时检测到未完成的工作流并恢复它们。由于库处理持久性执行的逻辑，因此不需要外部编排服务。

在这篇博文中，我们比较了使用 Temporal（一个外部编排系统）和 DBOS（一个嵌入式持久性执行库）将持久性执行添加到现有应用程序所需的架构工作。

我们表明，将 DBOS 集成到现有应用程序中只需要少量代码更改（在一个 110 LoC 的应用程序中只需 7 行代码）并且不需要更改应用程序的架构或操作。相比之下，集成 Temporal 需要重新架构应用程序，将其拆分为两个服务（一个 Temporal 工作器和一个 API 服务器），增加对第三个服务（Temporal 服务器）的运行时依赖，并添加或更改 >100 行代码。

此比较的所有源代码 **[可在GitHub上获取](https://github.com/dbos-inc/durable-execution-benchmark)**。

### 参考应用程序

作为参考应用程序，我们使用基于 [LlamaIndex](https://www.llamaindex.ai/) 的 [SEC Insights](https://github.com/run-llama/sec-insights) 应用程序的文档索引管道。该应用程序摄取和索引文档，然后提供基于检索增强生成 (RAG) 的文档查询。例如，它可以摄取公司多年来的 SEC 备案文件，然后准确回答有关公司在此期间财务表现的详细问题。由于应用程序可以并发摄取许多文档，并且每个文档的摄取时间很长，因此它极大地受益于持久性执行，以确保它正确摄取所有请求的文档。

![持久性执行参考应用架构图](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d977f6c3eb43585b86_AD_4nXdJTxPLnl_mIDW06rov_SaDc2CJ6i_ABmW9Yb0zEOhdvOKO34-S02_Fru2YFR577dicdfLI4ZIN8zXYKqDT7IMaxs-CHTJqFRVNEk5W7wAbqQIh66FdNFtAQQ6Vw4MgX0ciGtpyyw.png)

这是文档摄取管道的源代码。 `index_endpoint` HTTP 端点接收一个包含要摄取文档 URL 的请求。它在后台线程中对该列表调用 `index_documents`，后者又对每个文档调用 `index_document` 进行处理，使用线程池并发处理多个文档。

因为此应用程序不是持久性执行的，所以索引文档是**不可靠**的。如果应用程序在收到索引请求后中断，调用者无法知道摄取失败（因为它是异步发生的），无法知道在失败之前哪些文档已成功摄取，也无法恢复和摄取剩余的文档。您可以等待用户抱怨索引挂起，然后手动检查日志以查看它停止的位置，然后手动上传剩余的文档。但是，如果此应用程序服务于数百或数千名分析师或投资者呢？理想情况下，您希望此应用程序自动恢复每个人的工作——这就是持久性执行所做的。

![持久性执行参考应用代码](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d917182387cf7a1f2e_AD_4nXfLtE0qa5KtQIky8qwL5wF68SZ3W_8p3wSFA7hGEetZ1rCTPo58JFNNJ9Kvsm1tDpi41TJiA1WbpoCSdF-NymJ_mpxkp92ck8a7PTRBQUpjYvtjnSvjBaYdT-f7gNluL85Wfq4e3g.png)

*参考应用程序（110 LoC）的完整源代码 **[在此处](https://github.com/dbos-inc/durable-execution-benchmark/blob/main/reference-application/app/main.py)**。*

### 使用 DBOS 嵌入持久性执行

现在，我们使用[开源 DBOS Python 库](https://github.com/dbos-inc/dbos-transact-py)为应用程序添加持久性执行。添加持久性执行使文档索引变得**健壮**。如果应用程序在收到索引请求后失败，它会自动恢复，索引所有在失败前未索引的文档。这是带有 DBOS 的文档摄取管道源代码，更改已突出显示：

![持久性执行代码 DBOS Transact 示例](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d95bbc3510b337a601_AD_4nXeo_PuSTDWnjG_5ofEpums5ARg1xReR-ofPM_7Tbs8GnH9olyFmOOjRSF5cTkocgyoc8SbS9z7qmiaKjkOLxokzTsjZzJ-it2hMOY32pwsU__arY1lPf-ydNqzsx_cJ7_dgmIRC1A.png)

唯一的更改是将 `index_documents` 标记为工作流，将 `index_document` 标记为步骤。此外，线程池执行器被 DBOS 队列取代，以并发处理多个文档。总而言之，使用 DBOS 添加持久性执行仅需在应用程序中添加或更改 7 行代码（五行突出显示的代码加上未显示的两个配置行）。

DBOS 应用程序（113 LoC）的完整源代码 **[在此处](https://github.com/dbos-inc/durable-execution-benchmark/blob/main/dbos-application/app/main.py)**。

### 与外部持久性执行服务 (Temporal) 集成

现在，让我们使用 Temporal 为应用程序添加持久性执行。由于 Temporal 是外部编排的，这需要重新架构应用程序。文档摄取代码必须拆分为一个单独的服务，作为 Temporal 工作器运行。这个工作器由一个单独的 Temporal 工作流服务器外部编排。原始应用程序的 API 服务器必须重新配置为 Temporal 客户端，它接收 HTTP 请求并将工作流提交到 Temporal 服务器，以便在工作器上执行。

![Temporal 持久性执行应用架构图](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d91501865ec2865430_AD_4nXfxPl-HJf8rcjItQ-kuzrBd9KKEPAeyfh1ubL29HE1iHS1ItXz8Lz_sIYSZP3xTxPzA0Z4Zpl6a8yp4RSp8_5VAv_QLLp4W9l_3sfM98im0P1ITK7bPPnOcqsTW7Zl7nOhZ7OwLNg.png)

这是使用 Temporal 的源代码。首先，我们将 `index_document` 标记为 Temporal 活动（步骤）：

![Temporal 持久性执行步骤示例代码](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d9b1de9ee05d8b491e_AD_4nXdCkrCgGTPmUlfugJO1zgqP34XXTWKr2bySyHd02hN-BfzLvldDVxN7xItTkKOYyBUzYPbhdWnlAjHDfprvogJf4dlyqxgSVBODZTwwM1ITNbQ8LSvvzsqReSved1KbQFNy7RD4Wg.png)

然后，我们将 `index_documents` 重写为执行该活动的 Temporal 工作流：

![Temporal 持久性执行工作流代码示例](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d912bb2d1abe2269d7_AD_4nXfLa9bIycc5EsY84wocGNqaiY4zO0m3AlakuQDkc4tk2WJM08G6_pezsnhnZ7wyp2RfLoLa_lxIO9TKxgw4CglAdxCz3KOrglHdpABR9JhN9Cwpj-ZCqRT22IAa0W5PoqPyrkiYDQ.png)

然后，我们添加代码以将 Temporal 工作器作为其自己的服务启动：

![Temporal 持久性执行工作器代码示例](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93da2b8156c2fd8fe63d_AD_4nXcr7eaCJp0n_pm477qT5LfuCCQMF5Xt_nzQ4f2CR6N5LcE_SStRuZ2OD8LO50jkcKucFA2IGxjd7-AM_K-IGD5C3boUH8IwFg6fHBOg3D95AI6K5QTFTKLVSO8B-Uh6rIIzmSgYaw.png)

最后，回到 API 服务器，我们将 `index_endpoint` 重写为 Temporal 客户端：

![Temporal 持久性执行端点代码示例](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d95bbc3510b337a5fb_AD_4nXdIJsckRJt7bwcVUp98L5NMXwBy24G8xERUbkuYmdMB9vyJ7_Q7gw5DnSLiB-7PvKCYJZX7yC0vaWN6M8gu-qZopz-B4S6ORwEIlDauFlm1BeJK9pRWDgJdKYfMfTp29Ze7mGuZ.png)

代码更改是巨大的，需要添加或更改 >100 行代码。总的来说，使用 Temporal 后，应用程序从 110 行代码增加到 187 行。

更重要的是架构和操作复杂性的增加。参考应用程序是在一个服务中实现的，除了 Postgres 作为其向量存储之外没有外部依赖。相比之下，Temporal 应用程序被拆分为两个服务（Temporal 工作器和 API 服务器），并对第三个服务（Temporal 服务器）具有运行时依赖。这三个服务是紧密耦合的——如果其中任何一个不可用，其他两个都将无法运行。因此，操作 Temporal 应用程序需要管理、扩展和确保所有三个服务的可用性，这可能会使操作复杂性增加三倍。

Temporal 应用程序（187 LoC）的完整源代码 **[在此处](https://github.com/dbos-inc/durable-execution-benchmark/tree/main/temporal-application)**。

### 讨论

DBOS 比 Temporal 更轻量级的原因在于**外部编排器**和**嵌入式持久性执行库**之间根本的架构差异。像 Temporal 这样的外部编排器将持久性执行与应用程序的其余部分分开，将持久性执行的代码放在自己的孤岛（工作器）中，由编排器进行管理。相比之下，对于像 DBOS 这样的库，持久性执行是您可以通过注释工作流和步骤赋予应用程序代码的属性。

我们认为库方法是正确的方法，因为持久性执行的代码通常很难与应用程序的其余部分分开——它是应用程序核心的业务逻辑，与所有其他部分紧密耦合。持久性执行库尊重这一点，让您可以注释需要持久性的代码，而无需动应用程序的其余部分。相比之下，外部编排器要求您重新架构应用程序才能添加单个持久性工作流。

此外，持久性执行都是关于可靠性的。添加必须始终运行的额外服务会增加另一个单点故障。库方法的一个主要优点是它不会增加额外的单点故障——它只是利用您已在使用的应用程序和数据库。

### 试用一下

DBOS 持久性执行库是完全开源的。要了解更多信息，请在 Github 上查看它（并给它一个星标）。

- Python: https://github.com/dbos-inc/dbos-transact-py
- TypeScript:  https://github.com/dbos-inc/dbos-transact-ts