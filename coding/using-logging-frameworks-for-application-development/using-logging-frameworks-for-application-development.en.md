##### *Editor’s Note: This article is an excerpt from the Manning book [Logging Best Practices: A Practical Guide to Cloud Native Logging](https://chronosphere.io/resource/logging-best-practices). This book provides the practical framework you need to transform logging from a reactive debugging tool into a proactive competitive advantage, and can be downloaded to read in its entirety.*

---

A logging framework is a structured toolset that handles how logs are generated, formatted, filtered and routed. It enables developers to [configure log behavior](https://thenewstack.io/logging-best-practices-defining-error-codes) (like log levels or destination) without modifying code, improving observability and reducing friction across environments. It also conveys more meaning and value about an application’s behavior than log events alone.

This excerpt from the Manning book *[Logging Best Practices](https://chronosphere.io/resource/logging-best-practices/?utm_source=TNS&utm_medium=sponsored-content)* explores the logging framework landscape, as there is a range of commonalities in their capability and in design. A general understanding will help you appreciate the “art of the possible” and make informed decisions when choosing a framework.

By [downloading the book](https://chronosphere.io/resource/logging-best-practices/?utm_source=TNS&utm_medium=sponsored-content), you can explore whether the more dominant frameworks for different languages can support the ability to connect directly to Fluentd, one of the [most widely deployed](https://thenewstack.io/what-are-the-differences-between-otel-fluent-bit-and-fluentd) technologies for log collection in the enterprise. Fluentd provides logging libraries for multiple programming languages, so we also look at those to understand how they may fit into the options we have.

If frameworks or Fluentd libraries aren’t an option, you can have applications write to files, since [Fluentd](https://chronosphere.io/learn/fluentd-to-fluent-bit-a-migration-guide/?utm_source=sponsored-content&utm_id=TNS) can consume such information. But connecting via a file is less efficient than connecting the application directly.

If you are working with a Function as a Service (FaaS) like [AWS](https://aws.amazon.com/?utm_content=inline+mention) Lambda or Functions services from [Oracle](https://www.oracle.com/developer?utm_content=inline+mention) Cloud, [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure and [Google](https://cloud.google.com/?utm_content=inline+mention), or even self-hosted functions via [Fn Project](https://fnproject.io/), you’ll recognize that the services are very transient. As a result, these very transient services are more challenging to efficiently log from. Trying to connect to storage can be more complex to configure and slower to connect, and therefore more suited to network-based logging.

## Value of Logging Frameworks

Regardless of the genesis of the logging framework(s), all address the following key themes to a greater or lesser extent:

* Providing an easy way to output [log events](https://chronosphere.io/learn/what-is-log-file-and-log-data?utm_source=sponsored-content&utm_id=TNS) using a log level classification.
* Allowing the control of log events sent via configuration.
* Directing the log events to different output forms, such as files, stdout, HTTP, etc.

While log levels can be traced back to Syslog standards ([RFC 5424](https://tools.ietf.org/html/rfc5424)), for application development (as opposed to OS-level tooling that led to the definition of RFC 5424), one of the strongest influencers on logging libraries is Apache Log4J. This influence could be attributed to the fact that the Apache Software Foundation ported the design and implementation to several different languages. But its influence goes further than that.

While it is possible to arrive at very similar or even the same answers based on the same needs, you can see very similar if not the same APIs and features in the logging frameworks for many other languages. Some logging frameworks not linked to the Apache Software Foundation openly acknowledge drawing on the design principles of Log4J.

To be open and transparent, one of these authors’ entry into open source was when they started developing with [Java](https://thenewstack.io/introduction-to-java-programming-language/) 1.2, so our perspective may be a little biased.

The beauty of following the Log4J route is the ability for third parties to implement certain parts of the framework, so the application doesn’t see any difference. Still, the configuration could change behaviors, such as how the logs are stored, from flat files to databases. We’ll see this in more detail in the next couple of sections.

*NOTE References to Log4J can cause some confusion, as there are two versions: Log4J and Log4J2. When referencing Log4J today, you can assume it refers to version 2. Version 1 was declared at the end of its life in Typical structure of a logging framework 45 2015. Versions 1 and 2 aren’t radically different in terms of ideas. But version 2 was rewritten to address some weaknesses of the version 1 implementation; this meant the implementation could be written to utilize new language features.*

## Typical Structure of a Logging Framework

Given the Log4J influence across many logging frameworks and languages, it is best to start by examining the Log4J structure. Doing so, you can easily understand and master other frameworks. The figure below illustrates this structure and the relationships with the different classes (we’ve used [UML class notation](https://www.omg.org/spec/UML) with a couple of tweaks, as the key shows).

As shown in the diagram, the classes or modules involved are the Logger Context, Configuration, Filter, Logger, Logger Config, Formatter and an Appender.

[![Common logging structure represented using UML class notation, including indicating the quantities in the relationships, such as 0 or 1 to many.](https://cdn.thenewstack.io/media/2025/08/c6dbaaea-logging-structure.png)](https://cdn.thenewstack.io/media/2025/08/c6dbaaea-logging-structure.png)

Common logging structure represented using UML class notation, including indicating the quantities in the relationships, such as 0 or 1 to many.

In the following sections, we’ll describe the role that each of these components plays. We have ordered the components based on how much their logic impacts the use and behavior of the logging framework.

### Logger Context

This is the foundation of the framework within your application. It takes responsibility for holding the references to specific logger objects. It will process any configuration files, creating the necessary logger objects as necessary.

The logger context typically forms a “one-stop shop” for all your logging elements; within the application, this class is used to retrieve an object that will handle the relevant processing of log events (represented by an instance of a logger object).

When a request is made on the logger context for a logger object, it can derive or use parameters to determine which logger object to provide. If no specific logging configurations are associated with the identifier provided (usually a logical name or classpath), then a default logging behavior will be provided.

Depending on the implementation, it may also orchestrate any details such as connection pools, and so on. This is the only point where there is a certainty of having a single object, making it the root for all Log4J configuration values.

### Appender

The appender’s task is the easiest to relate to and is key to processing log events. Depending upon the specific logging framework implementation, the appender may be called an adaptor or transport, as this layer is responsible for taking the log events and sending them to the appropriate destination. For example:

* Transmitting them using techniques such as TCP/IP messages.
* Using API calls to services such as Logstash.
* Writing or appending the log event to the end of a file (hence the name).

Each appender will make use of filters to control which log events it may need to append. An appender can also use a formatter to convert the internal representation of the event to how it should be outputted; this can range from JSON to tab-separated rows. Some types of appender can only emit log events in a specific way; this relationship can sometimes get simplified and combined into a single class or module.

Within the configuration of a logging framework, it is possible (and expected) to see several different appenders configured to address sending some events to multiple destinations with different log levels.

### Logger

It is possible to define multiple loggers (or just the context defaults) so that different application parts can use logging in different ways — for example, a separate logger for recording [official audit events](https://chronosphere.io/resource/how-to-transform-your-logs-to-meet-your-observability-and-security-needs/?utm_source=sponsored-content&utm_id=TNS) versus generic application audit trails.

The official audit events may need to be sent to the database, and all events, including the audit, should be sent to the logging framework. These loggers can then be selected within the code. There will be different configurations with different loggers, such as which appender to use, which filters to apply, and so on.

By having multiple loggers, you benefit from varying the configuration for different parts of the code base and even having multiple configurations for parts of the application (e.g., log errors to stdout and log everything to file).

### Filter

The filter determines which log events should be emitted, primarily by determining whether the log event is at a level above or below the threshold set in the configuration. As filters are associated with appenders, different log destinations can be configured with different log levels.

For example, you could set the console appender to have a log level of Warning and a file appender set to Info. The result is that only Warning and Error events go to the console, but more details are included in the file.

### Formatter

As described by the appender, the formatter’s task is to construct the appender output so that the log entry is presented as wanted or required (e.g., time in a 12- or 24-hour format). Some appenders will allow flexibility (e.g., file appenders).

### Configuration

Typically, you want to drive the logging of an application through configuration rather than code, as this allows the logging to be configured without necessarily making invasive code changes. This also makes for a quicker turnaround in the verification of configurations. It allows changing how logs are processed, depending upon the deployment context.

For example, you could have a configuration that sends everything to stdout for your development machines. However, in test and production environments, the configuration is set to send the logs to Elasticsearch.

### Logger Config

The logger config is a subset of the total logging configuration for a particular logger (see the “Logger” section above). This will track the relevant configuration section and translate it into the correct objects in the code. This may include using things like factory design patterns.

## Appender Structures

Typically, appenders are built through a hierarchy of inheritance or encapsulation so that each layer of sophistication can leverage simpler operations. Ultimately, this will depend on a standard interface definition so that regardless of appender, they are orchestrated the same way, just as Fluentd does with its plugins.

The figure shows how Log4J has organized its appenders through inheritance from a base class that realizes an interface and provides common logic, which is then extended to provide a set of basic appenders, such as the console appender.

From this layer of derivation, the layering builds an increase in specializations. This is most notable with the `AbstractOutputStreamAppender`, which is then used for general socket use cases and is further specialized for sending logs into a Syslog-compliant solution.

[![UML representation of how some of the appenders of Log4J are related.](https://cdn.thenewstack.io/media/2025/08/d226aee1-log4j-appenders.png)](https://cdn.thenewstack.io/media/2025/08/d226aee1-log4j-appenders.png)

UML representation of how some of the appenders of Log4J are related.

To keep reading, download *[Logging Best Practices](https://chronosphere.io/resource/logging-best-practices/?utm_source=TNS&utm_medium=sponsored-content)* to learn more about how to evaluate logging frameworks and optimize your architecture.

## FAQs

**Q:** How do I choose the right logging framework for my application?

**A:** Choose a framework that:

* Supports log level control and flexible configuration.
* Offers multiple appenders (e.g., file, stdout, HTTP).
* Aligns with your language/platform ecosystem.

Look for community adoption (e.g., Log4J in Java, its influence in others), extensibility and compatibility with log routing tools like Fluentd.

**Q:** What is an “appender” in logging frameworks?

**A:** An appender is a component that sends log events to a specific destination, like a file, console or remote service. It often includes filters and formatters to control what gets logged and how. Log4J-style appenders are common across many frameworks.

**Q:** What’s the difference between a logger and a logger context?

**A:** The logger context is the central point that manages all jogger instances, processes configuration and orchestrates logging behavior. A logger is the actual object your code uses to emit log events, often scoped by module or purpose (e.g., [audit logs](https://chronosphere.io/learn/audit-log-definition-guide/?utm_source=sponsored-content&utm_id=TNS) vs. general logs).

**Q:** Can I change logging behavior without modifying application code?

**A:** Yes. Most modern logging frameworks are configuration-driven. You can change log levels, outputs or formats via config files depending on environment (e.g., stdout for dev, Elasticsearch for production), enabling flexibility and faster deployment cycles.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/04/530d1b86-cropped-4cf8b90d-manning-platform-eng_thumbnail-image.webp)

This is an excerpt from the Manning Early Access Program (MEAP) book "Effective Platform Engineering" by Ajay Chankramath, MD & CTO of Industry Solutions, Platform and Product Engineering for Brillio; Nic Cheneweth, Principal Consultant at Thoughtworks; Bryan Oliver, Principal Consultant...

Read more from Manning Book Authors](https://thenewstack.io/author/manning-book-authors/)