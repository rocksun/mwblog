Serious applications make data **durable**; they store data on disk or in a database so it doesn’t disappear the second a program stops working for any reason. But what about the application itself?  Let’s say your server handles hotel reservations, and it's halfway through processing a reservation when it’s restarted. What happens to the reservation? Alternatively, what if your server is ingesting a batch of 10,000 documents for AI analysis, but is restarted after only finishing 4,000?  What happens to the other 6,000 documents?

**Durable execution** helps solve these problems. The idea is to periodically checkpoint the state of an application to a persistent store (like a database) so that if the application ever fails, crashes, or is interrupted, it can use its checkpointed state to recover from where it left off. This way, no data is lost, and processes–especially costly batch processing jobs–do not have to restart from the beginning.

Most durable programs are written as **workflows** of **steps**. Each step takes in an input, does some work, and returns an output. The workflow wires all the steps together. A durable execution system persists the state of the workflows (which steps have completed and what their outputs were) so if the application is interrupted, all workflows can be resumed from their last completed steps.

![How durable execution works diagram](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d92484dbfd039ce77b_AD_4nXfB0sV0DXrhRAfJvfLm784u_Jhdqnj8igxk802o8ZoanK7vPkLznsbMlz-mA-q5fQxBsYjH8KfDlhaHCB5VbdWFyODd3abLikmOiUYk5Fv9_TpH1fS7t2cmwXWPYyFWmLcLUCc2RA.png)

### External vs. Embedded Durable Execution

There are two broad approaches to implementing durable execution:

* **External orchestration** systems define and execute durable workflows separately from your application using an **orchestrator** and **workers**. The orchestrator manages workflow execution, dispatching steps to the workers. The workers execute the steps, then return their output to the orchestrator. The orchestrator persists each step’s output, then dispatches the next step. Typically, the orchestrator and workers run on separate servers and communicate via message-passing.
* **Embedded durable execution** systems integrate into your application code via **an open-source library**. Developers annotate workflows and steps within their applications. When the application runs, the library persists the state of workflows and steps to a data store. If the application is interrupted in any way, the library detects incomplete workflows when the application restarts and resumes them. Because the library handles the logic of durable execution, there is no need for an external orchestration service.

In this blog post, we compare the architectural effort required to add durable execution to an existing application using Temporal (an external orchestration system) and DBOS (an embedded durable execution library).

We show that integrating DBOS into an existing application requires only minor code changes (7 lines of code (LoC) in a 110-LoC application) and no changes in the app’s architecture or operations. By contrast, integrating Temporal requires rearchitecting the app, splitting it into two services (a Temporal worker and an API server), adding a runtime dependency on a third service (the Temporal server), and adding or changing >100 lines of code.

All source code for this comparison is [available on GitHub](https://github.com/dbos-inc/durable-execution-benchmark).

### Reference Application

As a reference application, we use a document indexing pipeline based loosely on the [SEC Insights](https://github.com/run-llama/sec-insights) application from [LlamaIndex](https://www.llamaindex.ai/). The application ingests and indexes documents, then provides Retrieval Augmented Generation (RAG)-based querying of those documents. For example, it can ingest a company’s SEC filings for some years then accurately answer detailed questions about the company’s financial performance during that time. Because the application can ingest many documents concurrently and because each document takes a long time to ingest, it greatly benefits from durable execution to ensure it correctly ingests all requested documents.

![durable execution reference application architecture](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d977f6c3eb43585b86_AD_4nXdJTxPLnl_mIDW06rov_SaDc2CJ6i_ABmW9Yb0zEOhdvOKO34-S02_Fru2YFR577dicdfLI4ZIN8zXYKqDT7IMaxs-CHTJqFRVNEk5W7wAbqQIh66FdNFtAQQ6Vw4MgX0ciGtpyyw.png)

Here is the source code for the document ingestion pipeline. The index\_endpoint HTTP endpoint receives a request containing the URLs of documents to ingest. It calls index\_documents on that list in a background thread, which in turn calls index\_document on each document to process it, using a thread pool to process multiple documents concurrently.

Because this application is not durably executed, indexing documents is **unreliable**. If the application is interrupted after receiving an indexing request, there is no way for the caller to know that ingestion failed (because it happens asynchronously), no way for the caller to know which documents were successfully ingested before the failure, and no way to recover and ingest the remaining documents. You could wait for a complaint from a user that the indexing hung, and then manually check logs to see where it stopped and then manually upload the remaining docs for them. But what if this application serves hundreds or thousands of analysts or investors? Ideally, you’d like this application to resume everyone’s work automatically–that’s what durable execution does.

![durable execution reference application code](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d917182387cf7a1f2e_AD_4nXfLtE0qa5KtQIky8qwL5wF68SZ3W_8p3wSFA7hGEetZ1rCTPo58JFNNJ9Kvsm1tDpi41TJiA1WbpoCSdF-NymJ_mpxkp92ck8a7PTRBQUpjYvtjnSvjBaYdT-f7gNluL85Wfq4e3g.png)

The full source code for the reference application (110 LoC) is [here](https://github.com/dbos-inc/durable-execution-benchmark/blob/main/reference-application/app/main.py).

### Embedding Durable Execution With DBOS

Now, we add durable execution to the application using the [open-source DBOS Python library](https://github.com/dbos-inc/dbos-transact-py). Adding durable execution makes indexing documents **robust**. If the application fails after receiving an indexing request, it automatically recovers, indexing all documents that had not been indexed before the failure. Here is the document ingestion pipeline source code with DBOS, with changes highlighted:

![durable execution code DBOS Transact example](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d95bbc3510b337a601_AD_4nXeo_PuSTDWnjG_5ofEpums5ARg1xReR-ofPM_7Tbs8GnH9olyFmOOjRSF5cTkocgyoc8SbS9z7qmiaKjkOLxokzTsjZzJ-it2hMOY32pwsU__arY1lPf-ydNqzsx_cJ7_dgmIRC1A.png)

The only changes are annotating index\_documents as a workflow and index\_document as a step. Additionally, the thread pool executor is replaced by a DBOS queue to process multiple documents concurrently. In total, adding durable execution with DBOS requires adding or changing just 7 lines of code (the five highlighted lines plus two lines of configuration not shown) in the application.

The full source code for the DBOS application (113 LoC) is [here](https://github.com/dbos-inc/durable-execution-benchmark/blob/main/dbos-application/app/main.py).

### Integrating with an External Durable Execution Service (Temporal)

Now, let's add durable execution to the application using Temporal. Because Temporal is externally orchestrated, this requires rearchitecting the application. The document ingestion code must be split off into a separate service, which runs as a Temporal worker. This worker is externally orchestrated by a separate Temporal workflow server. The original application’s API server must be reconfigured into a Temporal client, which receives HTTP requests and submits workflows to the Temporal server for execution on the worker.

![Temporal durable execution application architecture diagram](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d91501865ec2865430_AD_4nXfxPl-HJf8rcjItQ-kuzrBd9KKEPAeyfh1ubL29HE1iHS1ItXz8Lz_sIYSZP3xTxPzA0Z4Zpl6a8yp4RSp8_5VAv_QLLp4W9l_3sfM98im0P1ITK7bPPnOcqsTW7Zl7nOhZ7OwLNg.png)

Here is the source code using Temporal. First, we annotate index\_document as a Temporal activity (step):

![Temporal durable execution step sample code](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d9b1de9ee05d8b491e_AD_4nXdCkrCgGTPmUlfugJO1zgqP34XXTWKr2bySyHd02hN-BfzLvldDVxN7xItTkKOYyBUzYPbhdWnlAjHDfprvogJf4dlyqxgSVBODZTwwM1ITNbQ8LSvvzsqReSved1KbQFNy7RD4Wg.png)

Then, we rewrite index\_documents as a Temporal workflow executing the activity:

![Temporal durable execution workflow code example](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d912bb2d1abe2269d7_AD_4nXfLa9bIycc5EsY84wocGNqaiY4zO0m3AlakuQDkc4tk2WJM08G6_pezsnhnZ7wyp2RfLoLa_lxIO9TKxgw4CglAdxCz3KOrglHdpABR9JhN9Cwpj-ZCqRT22IAa0W5PoqPyrkiYDQ.png)

Then, we add code to start the Temporal worker as its own service:

![Temporal durable execution worker code sample](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93da2b8156c2fd8fe63d_AD_4nXcr7eaCJp0n_pm477qT5LfuCCQMF5Xt_nzQ4f2CR6N5LcE_SStRuZ2OD8LO50jkcKucFA2IGxjd7-AM_K-IGD5C3boUH8IwFg6fHBOg3D95AI6K5QTFTKLVSO8B-Uh6rIIzmSgYaw.png)

Finally, back in the API server, we rewrite index\_endpoint as a Temporal client:

![temporal durable execution endpoint code example](https://cdn.prod.website-files.com/672411cbf038560468c9e68f/67db93d95bbc3510b337a5fb_AD_4nXdIJsckRJt7bwcVUp98L5NMXwBy24G8xERUbkuYmdMB9vyJ7_Q7gw5DnSLiB-7PvKCYJZX7yC0vaWN6M8gu-qZopz-B4S6ORwEIlDauFlm1BeJK9pRWDgJdKYfMfTp29Ze7mGuZ.png)

The code changes are substantial, requiring adding or changing >100 lines of code. Overall, the application increases from 110 lines of code to 187 with Temporal.

Even more substantial is the increase in architectural and operational complexity. The reference application is implemented in a single service, with no external dependencies except Postgres as its vector store. By contrast, the Temporal application is split into two services (the Temporal worker and the API server) with a runtime dependency on a third (the Temporal server). These three services are tightly coupled–if any one of them becomes unavailable, the other two will not function. Thus, operating the Temporal application requires managing, scaling, and ensuring the availability of all three services, potentially tripling operational complexity.

The full source code for the Temporal application (187 LoC) is [here](https://github.com/dbos-inc/durable-execution-benchmark/tree/main/temporal-application).

### Discussion

The reason DBOS is more lightweight than Temporal is because of the fundamental architectural difference between an **external orchestrator** and an **embedded durable execution library**. An external orchestrator like Temporal separates durable execution from the rest of your application, placing durably executed code in its own silo (the worker) which the orchestrator can manage. By contrast, for a library like DBOS, durable execution is a property you can give to code in your application by annotating workflows and steps.

We believe the library approach is the right one because durably executed code is usually hard to separate from the rest of your application–it’s the business logic at the core of your application, tightly coupled to everything else. A durable execution library respects that, letting you annotate the code that needs to be durable and leave the rest of your application alone. An external orchestrator, by contrast, requires you to rearchitect your app to add a single durable workflow.

Also, durable execution is all about reliability. Adding additional services that must be up and running at all times adds another point of failure. One major advantage of a library approach is that it does not add extra points of failure–it just leverages the application and database that you are already using.

### Try It Out

The DBOS durable execution library is completely open source. To learn more, check it out (and give it a star) on Github.

‍