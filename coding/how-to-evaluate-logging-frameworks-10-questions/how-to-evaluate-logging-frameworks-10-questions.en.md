*Editor’s Note: This article is an excerpt from the Manning book “[Logging Best Practices: A Practical Guide to Cloud Native Logging](https://chronosphere.io/resource/logging-best-practices/).” This book provides the practical framework you need to transform logging from a reactive debugging tool into a proactive competitive advantage, and can be downloaded to read in its entirety.*

*Read also:*

The number of logging frameworks is substantial, with most languages having a native capability and open source frameworks. In addition to logging frameworks, some libraries provide a programmatic interface and a mapping between the API and several different popular frameworks.

Those familiar with Log4J will probably have heard of [SL4J](http://www.slf4j.org?utm_source=sponsored-content&utm_id=TNS), which abstracts Log4J, the Java native logging framework and another called Logback. As a result, it is possible to switch the logging frameworks transparently. With these abstractions, a means to instantiate the desired logging framework is needed. This can be achieved by implementing a [factory](http://mng.bz/KB00?utm_source=sponsored-content&utm_id=TNS) or [dependency injection](http://mng.bz/DxZw?utm_source=sponsored-content&utm_id=TNS) pattern. Another example of this abstraction is [.NET native logging](http://mng.bz/9KV1?utm_source=sponsored-content&utm_id=TNS).

## Choosing a Framework

When evaluating a logging framework to adopt, some [things should be considered](https://chronosphere.io/learn/controlling-log-volume/?utm_source=sponsored-content&utm_id=TNS) to help select the most appropriate one. We have developed a set of questions that will help you evaluate your needs and select a framework to meet those needs. Reviewing these questions will help you determine your priorities in terms of a logging framework.

Once the questions have been given some form of priority, it becomes easier to evaluate the frameworks against the questions to see how well they match your needs. The questions are the following:

1. What appenders are available? Are they limited to one type of appender, such as files? Are there out-of-the-box appenders that can work with your log unification solution, such as Fluentd or Logstash?
2. Can the appender behavior be tailored or optimized? For example, are log rotation or network ports and addresses configurable?
3. Is it possible to tailor the output of log events based on the different parts of the application? For example, log thresholds for the application framework, such as Spring or .NET Core, are set to `Warning` and `Error`, but your custom logic can have thresholds set to `Info`.
4. How easy is it to tailor the logging configuration (without using code)? You may wish to tune logging, and if there is an operational issue, you can ideally update or override the default logging configurations to selectively get more information.
5. How much information does the framework derive for you (such as providing method and class names for tracepoints) with correctly structured timestamps?
6. Can you tailor the [log output formatting](https://chronosphere.io/learn/what-is-log-file-and-log-data/?utm_source=sponsored-content&utm_id=TNS) (JSON, XML)? The best logs have a structure allowing the log event to be both humanly readable and machine-readable.
7. How compact is the footprint? For Internet of Things (IoT) and mobile solutions, we need to have a tight footprint to limit resource use.
8. Can you make the log output secure — use TLS, encrypt files, and so on? Is the security good enough for the data being handled?
9. Will the framework have a material impact on my application’s throughput/performance, particularly the final I/O phase? Can logging end up being a thread-blocking mechanism?
10. How easy is the logging framework’s API to work with? If the calls within the application code are difficult to use, developers may avoid creating log events. Ideally, the interfaces will be intuitive, but having good supporting documentation to reference can be invaluable, particularly for those starting their development careers.

Rather than evaluating every possible option, it is worth trying to narrow the field of options.

## Putting Optimizing Application Logging Into Action

The [adoption of Fluentd](https://chronosphere.io/learn/fluent-bit-vs-fluentd/?utm_source=sponsored-content&utm_id=TNS) in your organization is going well, and you have been asked to determine whether the current logging framework in use is up to the job going forward, or whether the success of Fluentd allows supporting a case of changing logging frameworks. Using the factors described, evaluate the current solution being used by your development team. Compare this with an alternative.

## Finding the Answer

As we clearly cannot give you a specific solution for this exercise, we hope you have found that you are already using a logging framework, and it fits well with your needs. If your logging framework is not a great fit, you will probably have recognized the issues already. If you haven’t pinpointed the issues with your current framework, this list of considerations should have helped qualify the problems.

Download the [ebook](https://chronosphere.io/resource/logging-best-practices/?utm_source=sponsored-content&utm_id=TNS) to explore what happens if the logging framework being used does not provide support specific to Fluentd and learn ways to overcome this issue.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/05/c3489f3d-cropped-ba30d14d-phil-wilkins.jpeg)

Writing for Chronosphere, Phil Wilkins has spent more than 30 years in the software industry, with broad experience in businesses and environments from multinationals to software startups and consumer organizations to consultancy. He started as a developer on real-time, mission-critical...

Read more from Phil Wilkins](https://thenewstack.io/author/phil-wilkins/)