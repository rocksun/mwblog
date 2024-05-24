# Does Garbage Collection Logging Affect App Performance?
![Featued image for: Does Garbage Collection Logging Affect App Performance?](https://cdn.thenewstack.io/media/2024/05/032fd6c0-garbage-1024x625.jpg)
We sometimes encounter Java users who believe enabling garbage collection logging will have a significant impact on their performance metrics. Let’s examine the facts and myths.
## About the Garbage Collector
The Java garbage collector is a crucial part of the Java Virtual Machine (JVM) that affects your application’s performance and reliability. If you want to dive into the details of the different types of garbage collectors that are available in the
[Java runtime](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/) and how they work, check out this earlier blog post: “ [What Should I Know About Garbage Collection as a Java Developer](https://www.azul.com/blog/what-should-i-know-about-garbage-collection-as-a-java-developer/).”
## What Is GC Logging?
Garbage collection (GC) logging is a feature of the JVM that provides information about the garbage collection process. Thanks to the generated log files, you can get insights into how the
[JVM manages memory dynamically](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/) at runtime by collecting and disposing of objects that the program no longer needs. This is very useful when you want to monitor the performance of a [Java application](https://thenewstack.io/java-adapts-to-cloud-native-computing/), diagnose memory leaks and tune the JVM’s garbage collection configuration. *“*Some of our customers chase every microsecond to improve the performance of their applications, but they still enable GC logging,” notes Daniel Witkowski, sales engineer at Azul. “Because it has little to no impact on application performance and allows debugging many different problems, it is vital for these companies to always be able to retrieve the GC logs after a problem has occurred. *”*
When garbage collection logging is enabled, every time the JVM performs a garbage collection, the following information is stored in a log file:
**Type**of GC event **Minor GC**: Cleaning the young generation space **Major GC**: Cleaning the old generation space **Full GC**: Cleaning the entire heap space
-
**Time**when the GC event started **Duration**of the GC event **Amount of memory**before and after the GC event for each memory pool **Total available memory**in each pool
The log file is human-readable, and the content looks like this:
The stored information and format may vary depending on the JVM and the GC algorithm you use.
## Enabling GC Logging
GC logging is enabled with the Java command line argument
-Xlog. This has been available since Java 9, thanks to
[JEP 158 “Unified JVM Logging”](https://openjdk.org/jeps/158):
-Xlog:gc,safepoint:gc.logto enable default logging of the important garbage collection events including all safepoint pauses.
-Xlog:gc*,safepoint:gc.logto enable more detailed logging, including all safepoint pauses and smaller garbage collector events and phases that are normally not logged. For OpenJDK, this is often needed; otherwise, some Java heap memory metrics are not recorded, and not all pauses are tracked. On Zing, it’s not needed, as all necessary data is already logged by default with just
gc. The tradeoff between
gcand
gc*is usually 10 times more log data amount, which will reduce the time interval your log covers.
-Xlog:gc,safepointto write the log data to
stdout, which can be helpful in containers to avoid storing local log files.
-Xlog:gc,safepoint:gc.log::filecount=10,filesize=100Mto change the default log rotation of 5 files of 20MB each to 10 files of 100MB each.
-Xlog:gc,safepoint:gc.log::filecount=0to disable log file rotation, useful for quick test runs or for processes that are restarted often. Note the double colon.
You can even repeat the
-Xlog argument and use it to specify different outputs at the same time — for example, the following writes it to
stdout and to a local file:
$ java -Xlog:gc,safepoint -Xlog:gc,safepoint:/opt/log/gc.log -jar myApp.jar
There are more options available with the unified logging system, as you can see when you run the following command:
## Impact of GC Logging
Enabling GC logging in a Java application generally has minimal performance impact, especially with modern JVMs. However, the exact impact may vary based on the JVM version, the GC algorithm used, the settings of GC logging and the I/O performance of the system where logs are written. These are a few facts you’ll need to take into consideration:
**Risk of filling the filesystem**: Filling a file system to 100% or near 100% is the most practical performance impact often seen in relation to logging, and needs to be avoided. By default, Java 9 and newer versions have log file rotation enabled and will only write five log fragments of 20MB size each. **I/O operations**: GC logs are written directly to the disk. This creates I/O operations, and can therefore slow down the application if the disk is slow or there’s a high percentage of disk usage. **Memory buffering**: Modern JVMs typically use a memory buffer for GC logs. When the buffer is full, the logs go to disk to reduce the I/O impact. However, the buffer takes up memory that the application could otherwise use. **Detailed GC logs**: If detailed GC logs are enabled, such as those that record per-thread timing or object statistics, the performance impact may become noticeable since this data needs to be recorded and processed, which can consume CPU resources. **Safe points**: All GC logging activity happens at “safe points” in the application’s execution, meaning it doesn’t cause more “stop the world” pauses than would occur naturally due to GC activity itself.
“The practical performance topic users should consider regarding GC logging is the amount of data in the filesystem,” says Holger, customer staff engineer at Azul. “A system halt due to a full filesystem would result in really bad performance. When using only
-Xlog:gc:gc.log for Zing or
-Xlog:gc,safepoint:gc.log for OpenJDK, you get all necessary performance-relevant metrics without wasting too much space. Especially on Zing,
-XX:+PrintGCDetails, gc*, or safepoint are not needed as they don’t add more graphs in GCLogAnalyzer.”
*“*A big part of the GC log tasks is saving the data to a log file. The type of I/O used to store these files can impact the logging performance, not directly the application itself,” explains Deepak Sreedhar, principal software engineer at Azul. “So, some of the problems that may occur are not related to the performance of the GC logging but to the speed of the I/O. If the logs can’t be saved fast enough in real time, OpenJDK has the option to use asynchronous unified logging with
Xlog:async.
## GC Log With Azul Zing
When using Azul Zing, you only need to add
-Xlog:gc:gc.log to instruct Zing to store garbage collector log files. Extra arguments like
gc* or safepoint to increase the detail level are not needed, as Zing always logs safepoint pauses and even additional information not seen in OpenJDK GC logs by default, like just-in-time (JIT) compiler activity, CPU and memory usage, Linux page cache metrics, and a few more metrics often relevant for system performance analysis.
## Analyzing GC Logs
There are various tools available to analyze the content of GC log files:
**JVM’s built-in**: This utility displays performance statistics and can be used to output garbage collector statistics.
jstatcommand
**VisualVM**: This tool offers several views into different JVM aspects, like garbage collection. It also provides live metrics, which can be helpful for analyzing issues in real time. You can download this tool from [GitHub](https://visualvm.github.io/). **Azul GC Log Analyzer**: Reads the GC log and visualizes it as a set of graphs over time (wall clock and uptime). It shows information about the garbage collector, the JIT compiler, system metrics and ReadyNow statistics. This graphical desktop application is [documented here](https://docs.azul.com/prime/GC-Log-Analyzer), and a video walk-through is [available here](https://www.azul.com/tutorial/garbage-collection-log-analyzer/).
## Conclusion
Although garbage collection logs can introduce minimal performance costs, the trade-off is usually worthwhile, as the logs are often invaluable when tuning garbage collection and diagnosing memory issues. Without GC logs enabled, you can lose insights into how the JVM manages memory dynamically at runtime. This information is very useful for monitoring the performance of a Java application, diagnosing memory leaks and tuning the JVM’s garbage collection configuration.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)