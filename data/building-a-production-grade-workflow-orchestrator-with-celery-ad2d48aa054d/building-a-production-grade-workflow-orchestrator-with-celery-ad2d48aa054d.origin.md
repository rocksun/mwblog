# Building a Production Grade Workflow Orchestrator with Celery
A step by step guide on building complex workflows with celery for a high RPS data processing engine from designing to implementation to making a new production on K8s.
Celery is a pretty awesome tool for orchestration and data engineering specially for it canvas workflows features. Be it processing asynchronous tasks, long background processes, making complex workflows, fault tolerance mechanisms, making microservices patterns and what not , combine it with K8s and you have the best platform for your product.
This is an article i have written with an year of experience with celery and deploying a product on it .
Consider this as your “How to” guide for building a workflow orchestrator that processes tasks across multiple computes , how to communicate them , how to coordinate and deploy a product with it.
# Step 1: Understanding the business.
Getting a view on the business flow is the first step before jumping into the code, like quick processing speeds, how the features will be implemented, what sort of processing the data has to go through and all the steps in between ,how it will be deployed for on prem and on cloud infrastructure and lot of other questions like that.
The business journey in the case starts with data ingestion API bringing in the Raw Data , leading to producing different ML/NLP datasets , getting analytics insights and hitting the callback API for the next in line system. The diagram above is a quick glance at the entire journey
**The workflow must satisfy the following requirements**
- Modular Design to integrate different types of analytical services easily
- In real time processing
- Scale for high RPS ingestions.
- Must finish the entire process in as low as 10 seconds
- The system includes working with files and will have frequent interactions with databases like DynamoDB, S3 , kms so must also satisfy cost optimized architectures.
# Step 2: Converting it to a celery workflow.
The real head scratching of converting it to a workflow is to define the tasks, the workers that will perform these tasks and how all of it gets communicated using queues.
The beauty of celery is its features like celery canvas workflows and different types of worker pools it gives which makes it flexible to different design patterns and architectures.
[The Curious Case of Celery Work-flows — DEV Community](https://dev.to/akarshan/the-curious-case-of-celery-work-flows-39f7) **We first start by defining the different celery tasks.**
And that is by breaking down each component into an individual task that must be responsible for achieving its own business goal, it can even fail or retry but must achieve its goal.
Tasks like domain dataset generator and analyst tasks in the diagram below takes care of the ML, NLP and Pandas and is isolated to its particular business goal. Each business domain can produce its own data set with its own logic and models, each can be broken down into a different task of its own.
**Then comes the orchestration tasks**These tasks come out as coordinators, they don't have any business logic of its own but actually define how the actual data processing tasks have to to executed and coordinated to run sequentially.
The first process initiator serves as an entry point to the orchestrator and coordinates with dataset generator then service task in sequence.
The next data generator and service tasks makes sure proper sub tasks get executed parallelly
**We then decide celery workers that will be responsible for these tasks and use appropriate configurations.**
We will have many workers that will execute multiple tasks but we can have a broad classification of 3 types,
**Orchestration**, **Distributor** and **Task **workers **Orchestration worker:**This is the central coordinator of the entire workflow on how tasks get executed sequentially, how it can control the flow of messages and makes the data pipeline from ingestion to analytics to consumption. **Distributor worker**: Responsible for executing tasks in parallel and waiting till they finish, like data generator and Comprehensive analytics initiator workers. **Tasks Worker:**Responsible for executing the actual tasks that involves pandas and model predictions and is compute heavy as well.
Each worker here is containerized and deployed as a pod on K8s cluster and can scale as you want it.
**Defining the worker configurations:**
Celery has some different types of worker configurations available for different concurrency and task duration requirements like gevent, forkpool and eventlets. For something that is short and only has IO operations or simple api calls you might want to use gevent and eventlet that execute tasks in a non blocking manner, for something that needs compute and memory, use forkpool worker that works on child processes to achieve concurrency
The first 2 workers orchestration and distributors are for short duration tasks that do not require compute or memory and would generally be directing messages in queues and handle DynamoDB operation. These tasks can have higher
[and use concurrency ](https://docs.celeryq.dev/en/stable/userguide/concurrency/gevent.html) [worker pools](https://docs.celeryq.dev/en/stable/userguide/concurrency/gevent.html) *gevent*
The
**Task worker** on the other hand where the data magic happens and has lower concurrency, it is compute heavy and must use default celery *forkpool* **worker. **
Configuring the right worker with right pools achieves the goals of faster data journey, moving from one task to another in case of orchestration worker itself can satisfy high RPS and concurrent processing.
**With the tasks defined and what worker will execute them the next important step is ** *routing* *.* [Adopting Asynchronous Messaging With Azure Service Bus | by Jamahl Carter | The Startup | Medium](/swlh/adopting-async-messaging-with-azure-service-bus-4c936396b334)
Celery has this amazing feature of task routing that can be mention in its configuration.
It automatically routes task to different queues based on names, Yeah!! names … so if you name a task in some naming convention celery will route those tasks to that queue using regex and glob matching patterns.
# Step 3: Bringing in the optimizations
Celery has some really awesome features for production systems, the community was real smart with this.
Some features that I came across sped up the the long running processes, these features focus on how tasks gets polled by the workers, the task distribution mechanisms over the specified concurrency, retry mechanisms and handling failures.
** By default, preforking Celery workers distribute tasks to their worker processes as soon as they are received, regardless of whether the process is currently busy with other tasks. The -O Fair flag:** **-**option disables this behavior, waiting to distribute tasks until each worker process is available for work. *Ofair* [](http://Three quick tips from two years with Celery) [Three quick tips from two years with Celery](/@taylorhughes/three-quick-tips-from-two-years-with-celery-c05ff9d7f9eb) **Worker types in distributed systems offer varied concurrency models to optimize performance. Eventlet and Gevent are lightweight libraries for asynchronous I/O operations in Python. Eventlet uses coroutines and green threads, while Gevent employs greenlet-based cooperative multitasking. Forkpool workers, like those in Celery, utilize a process-based model, creating independent worker processes suitable for CPU-bound tasks, ensuring robust resource management and isolation. These options provide flexibility to enhance performance based on application’s needs. Workerpools: ** ** Workers by default poll 4 times the concurrency from their queue. For a task that is long running and needs to be processed instantly from the queues changing the multiplier to 1 will only poll as many as its available concurrency from the queue allowing another worker to poll messages from the queue. prefetch multiplier:** ** Celery tasks can have their own individual time limits to fail if they run longer. But it gives multiple options to handle them as well such as task time limits and handling:** *soft time limit*and *hard time limit*exception handling. These can allow to revers the db transaction that happened because of task getting killed due to limits. **Your code can fail but how to handle the failures is an option, with task failures and retries: ** *propagate flag*tasks failing in chords and groups will not impact the execution of other ones, adding retry mechanisms will atomically ensure a task gets retried by the workers. *Redis for caching:* **When you are building a workflow application using ML models one best optimization technique is to load them as a global variables, in this sense the model loading happens at the worker initialization and can be used as a shared static files. Preloading machine learning model files: **
# Step 4: Add Alerting and Monitoring Setup
Now that we have a distributed compute architecture the next best thing is to add mechanisms for alerting, monitoring and logging.
**ELK Stack : **One way to send all the celery task status logs is to high jack the celery loggers on worker startup and attach fluentd handlers with them, this will send logs with task duration, the args and kwargs passed to the task during execution and the status of your task. **Sentry: **Errors can be unexpected with high volumes of traffic especially dealing with different sorts of data that can surprise you, sentry could be your best friend to alert you if things go wrong, set up the sentry on start of celery workers and let it alert you to your slack and email groups with the error stack trace. **Datadog: **Need something extremely robust with logs monitoring, stack monitoring, network tracing??… datadog could be the most advanced tool for all the needs.
# Step 5: Deploy to production, Less gooo!!
Workflow build? ✅
Failures and exception handling? ✅
Optimizations? ✅
Processing speeds? ✅
Logging and alerting? ✅
We are now ready to take this setup into production. And we do this by containerizing the application and start each worker on different pods on K8s cluster.
Container orchestration here will allow us to satisfy out on demand traffic, our workers can scale as per messages in queues and process them much faster.
Since we are using SQS Queues, scaling can be done using
**for short Kubernetes event driven auto scaler KEDA **
KEDA combined with SQS metrics helps achieve scaling with Approximate age of oldest message in queue.
Ideally for a high RPS workflow the workers must consume a message from queue right away and process them. If the traffic is high more workers listening to the same queue will solve the problem. To define the best scaling policies we look at queue metrics such that provided on Amazon SQS,
SQS provides all sorts of metrics like messages in flight, approximate age, packet size, No of messages sent/deleted/received/not visible. We would ideally want the minimum in oldest message queue metrics.
Scaling and production setup?? ✅
All systems are a go and we have successfully made a production grade orchestrator that can serve high RPS requirements, and scale on demand
So that was for now on using celery in its best essence for data engineering and building complex workflows and deploying your product . I hope this gives a little idea on how complex coordination and execution of tasks can be achieved across multiple computes using celery, but not just limiting yourself to building but also making it a production grade system with scaling , monitoring and optimizations in place.