***Editor’s Note:** This article is an excerpt from Chapter 1 of The Manning book “[Logging Best Practices: A Practical Guide to Cloud Native Logging](https://chronosphere.io/resource/logging-best-practices/).” Download the full book to finish reading Chapter 1 to learn about a few best practices to maximize log value.*

## Why Context Matters in Logging

Understanding any [log event](https://chronosphere.io/learn/logging-best-practices/?utm_source=sponsored-content&utm_id=TNS) requires context. When we’re developing and using trace and debug logs, the context will, to an extent, be known to us, perhaps implicitly, as the position in the code will be part of the context or the test scenario being run will be the context. But when we come to production, the context is not likely to be implicit, so we need to make it explicit.

The key to the context is how well we’re answering the following:

* **What** — What is being reported, an error or just a trace?
* **When** — The date and time. This is the easy bit if you’re using some form of logging framework.
* **Where** — Where in the code and where in the infrastructure the source of the log event is.
* **Why** — When it comes to log levels of info and higher, why we provide the information is essential. Is there a problem about to occur, or are we reporting something you want to track, like a login action?
* **Who** — Who triggered the action? Whose data could be impacted?

Let’s explore these points in a bit more detail.

## ‘What’: Identifying What a Log Event Represents

The log event’s “what” is partially addressed by the log level being included in the event. For trace log events, the fact that the event is logged is probably enough when combined with “where.” For info log level and above, we’re going to provide some additional detail: Is the info record for audit purposes? What kind of error has occurred? What does the warning relate to (such as a shortage of storage)?

The “what” is best supported with details that allow a transaction to be identified, including the type of transaction. The transactional data or a proxy, such as a unique ID for a transaction (so we can look up the actual transaction data), should [provide sufficient insight](https://chronosphere.io/learn/controlling-log-volume/?utm_source=sponsored-content&utm_id=TNS); for example, if the transaction is missing a reference to associated data, we need to see that the value isn’t set.

## ‘When’: Handling Time Zones, Clocks and Global Systems

[Logging frameworks](https://chronosphere.io/learn/application-loggings-to-fluentd/?utm_source=sponsored-content&utm_id=TNS) address most of this for you without any effort, but are likely to go back to the server’s system clock. The implications of time zones, clock skew and so on can catch you out if you’re looking for a solution that is running in a time zone that applies daylight saving time (because someone is looking at the timestamp and it appears to be out because they’re applying daylight saving time, but the log isn’t) or the solution is globally distributed. So you need to know which time zone the server is in. One option is to configure the logging framework to include the time zone in the log, but better still, align all servers to UTC (Coordinated Universal Time).

When trying to align a log analysis with a user error report, you will need to be clear about which time zone the user is working in and whether the error report is recorded against their time or system time.

## ‘Where’: Code Location and Deployment Considerations

Naming the code location requires some awareness of how the code is handled. This is especially important when the code is deployed for a commercial solution where obfuscation and minifier tools are likely to be used, particularly on script-based solutions such as [JavaScript](https://chronosphere.io/learn/best-languages-for-microservices/?utm_source=sponsored-content&utm_id=TNS). As a result, relying on reflection to get details of where the code is can be unhelpful. Although there are tools, some obscurification providers will include mapping information to identify the original code, given the correct information.

**Note:** For more information on code minifying and obscuring, check out the following resources:

### Using IDs and Versions to Improve Clarity

Applications are typically either multithreaded (such as Java) or context-switched on an I/O wait (Node.js), and they are single-threaded. Context switching means we don’t handle one transaction at a time, so understanding whether log events preceding or following the event of interest are related can become challenging. This can be overcome by incorporating transaction IDs or session IDs, or by using open tracing or open [telemetry IDs as part of the log event](https://thenewstack.io/why-events-are-the-critical-telemetry-type-youre-missing/).

Some logging frameworks will help you capture a thread or process ID in their configuration. For example, in Fluentd, we can use the WorkerId in the log file output.

“Where” can also be influenced by software versions. We can have multiple versions of the same logic in production at one time to support activities such as:

* Operating A/B deployments to help evaluate whether one implementation improves user interaction.
* Operating with high availability, so software updates require rolling updates to occur.

Here’s another way to look at it: You spot an image that has not been rendered very well in this book. You contact Manning. To help you, we need to know which figure is faulty. What if the issue has been seen before and been fixed in a new edition of the book? This isn’t saying that every log event needs to publish every aspect of version information, but we do need to make it easy to supply sufficient information.

Perhaps when we log errors or worse, this information is written into the log. This is an area where injecting into log events can be helpful. If a log event is identified as reposting something abnormal in the software, such as an error, then Fluentd could retrieve the version of the [software running and inject it into the logs](https://thenewstack.io/using-logging-frameworks-for-application-development/) for future reference.

## ‘Why’: Understanding the Purpose Behind Log Events

This comes down to why an event has occurred — is it an error or just a signal to show where the code is (trace) or the application’s current state (debug)? As we move to the higher levels (warning, error and fatal in our classification), “why” becomes more important and less evident from just the [log level](https://chronosphere.io/learn/guide-to-log-parsing/?utm_source=sponsored-content&utm_id=TNS). The information-level log events could be an audit or a periodic snapshot of the system’s current state, regardless of whether things are good or bad — for example, logging how deep a message queue is. However, the log event consumer needs to be able to understand why the event is being generated. With a bit of thought, this is easily solved.

A simple attribute, such as “current status” or “audit action,” could be included along with the shared data. We are, in effect, providing a secondary classification in many cases for the log event. Given that we provide additional metadata, we might [structure](https://chronosphere.io/learn/structured-logging-and-reduced-storage/?utm_source=sponsored-content&utm_id=TNS) it as long as we are consistent within the development organization.

### Distinguishing Primary Errors From Side Effects

When it comes to reporting warnings and errors, the “why” comes back to “what” triggered the warning or error. Is it the primary error, or has something occurred as a by-product of a previous issue? Trying to indicate whether an error is cause or effect is difficult. If we can be certain, we should be clear; if it isn’t, we can perhaps give the log event consumer some hint about the possibility. Coding such information can be complicated and hard to test. But it is easy to link to an error code and provide steps to confirm cause or effect.

The record we generate with the event needs to clearly provide the information to help perform a diagnosis, not just operationally, but also whether something in the code may be needed, such as a more defensive code or better data validation. As the solution is now on an unhappy path, we should not be afraid to be generous with the information — as long as it doesn’t raise sensitivity issues, which we’ll look at shortly. For error-handling paths, we’re in a place where performance should not be a consideration, as this part of the codebase should only execute infrequently. Generally, too little information is a lot worse than too much.

## ‘Who’: Balancing Identity, Privacy and Compliance

Logging of “who” can be tricky. Logging information that is identifiable to an individual will make our [log processing](https://chronosphere.io/learn/mastering-log-data-transformation-at-scale-with-chronosphere/?utm_source=sponsored-content&utm_id=TNS) subject to legislative, contractual and commercial requirements.

The important thing is to consider when the “who” is necessary and whether we can safely use other data as a proxy for the true identity. For example, perhaps the “who” is relevant only during the logged-in session, so we just need to carry the session ID and use that. If we need to attribute the actions in a session back to a specific individual, we record that separately in a secure way. That session ID could equally be a transaction or order ID, and so on.

When recording events such as failed logins or application interactions that do not require a specific individual, we may still need a value for “who,” such as an originating IP address. For example, a single server ping may be harmless (alive service reporting is likely to just do this), but a really rapid repeated occurrence from the same location is not good. However, having that IP means it is possible to determine that it was the same system calling and therefore who to block.

### ‘Who’ Context in Action

Working with a client’s DevOps team, we discovered the client’s [security team](https://chronosphere.io/learn/security-logs-explained/?utm_source=sponsored-content&utm_id=TNS) employed a third-party organization to regularly run probes across all their internet-facing servers. We figured out what was happening, as we’d see our API gateway servers reporting illegal requests originating from one of several IPs on a regular frequency. Once we identified the pattern and the logged details like the IP origin, time and the HTTP request, we raised our suspicions with the security team, who confirmed the use of a third party.

### System vs. Human Actors in Log Events

Don’t forget that the “who” could be a system or application component. For example, when processing payroll, that activity is triggered by a scheduler. So it is helpful to know which schedule or scheduler triggered the process.

## A Practical Checklist for Capturing Context

Addressing what, when, where, why and who can be a little abstract. Personally, I try to address it using the following questions:

* Where in the code is the event coming from?
* Is there a chance that there are multiple versions of your code in production? If so, then which version becomes important.
* How is the transaction handled? This is especially important if the impact of a problem needs to be remediated in the data later.
* Which server, process or thread experienced the problem? If the issue is infrastructure-related, you need to know which server, virtual machine (VM) or container it relates to.
* Is the cause of the error identifiable (divide by zero as an error identifies the values involved in the error)? Can the [error log](https://thenewstack.io/logging-best-practices-defining-error-codes/) be tracked back to a location in the code? At a minimum, express the nature of the error and, if practical, the data values associated (a divide-by-zero error — say what was being divided by zero and the values involved).
* What data values led the execution in a specific path?

## Frequently Asked Questions

### 1. How do I handle time zones and global systems in my logging without creating confusion during incident response?

Time zones cause confusion due to daylight saving shifts, server location differences and user vs. system time mismatches. A best practice is to align all servers to UTC and clearly note whether timestamps are user-reported or system-generated.

### 2. How do I distinguish between primary errors and side effects in my logs to avoid chasing the wrong problems during incidents?

It’s often unclear whether an error is the cause or a side effect, so logs should include hints or references (like error codes) for clarification. Providing rich context like correlation IDs, classification attributes and extra details (without exposing sensitive data) is better than too little information.

### 3. How do I handle the ‘Who’ context in logs while balancing privacy requirements and operational needs?

* Only capture identity when necessary — use session IDs or proxies instead of full user details.
* For operations, the “who” may be a system or automated process.
* If storing personal identifiers, logs fall under compliance requirements, so use the minimal data needed.

This article is an excerpt from the Manning book, “Logging Best Practices.” Even with a health check in place, you need to know why a check might fail. This is where Fluent Bit’s error codes come in, offering a window into the exact issues affecting your inputs and outputs. You can read “Logging Best Practices” in its entirety [here](https://chronosphere.io/resource/logging-best-practices/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/05/c3489f3d-cropped-ba30d14d-phil-wilkins.jpeg)

Writing for Chronosphere, Phil Wilkins has spent more than 30 years in the software industry, with broad experience in businesses and environments from multinationals to software startups and consumer organizations to consultancy. He started as a developer on real-time, mission-critical...

Read more from Phil Wilkins](https://thenewstack.io/author/phil-wilkins/)