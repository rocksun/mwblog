# We CAN Have Nice Things: Upgrading to Java 21 Is Worth It
![Featued image for: We CAN Have Nice Things: Upgrading to Java 21 Is Worth It](https://cdn.thenewstack.io/media/2024/02/a2feedba-update-java-21-nice-things-1024x576.jpg)
It’s that time of year again — New Relic’s annual “
[State of the Java Ecosystem](https://newrelic.com/resources/report/2023-state-of-the-java-ecosystem)” survey results are out and, as always, I dug into it. And while I think the report is well done and asks great questions, I was disheartened by how many Java developers are using archaic versions.
## Are You Using Java 21? You Should Be.
Before I get into the survey, as a Java lover, I want to talk about some of my favorite things about Java 21.
I’ll start by saying that Spring Boot 3.x, the current generation of the most popular server-side stack on the Java virtual machine (JVM), requires at least Java 17. It does not support Java 8, which is the second most used version, according to the survey.
I’m excited to see that adoption of Java 17 is moving relatively quickly, but you really should be using Java 21. Java 21 is infinitely better than Java 8. It’s technically superior on all fronts. It’s faster, more secure, more operations-friendly, more performant and more memory efficient.
It’s also morally superior. You won’t like the look of shame and sadness in your children’s eyes when they find out that you’re using Java 8 in production.
Do the right thing and be the change you want to see in the world: Use Java 21. It’s just
[chock-full of goodness](https://thenewstack.io/java-21-is-nigh-whither-javaone/), basically a totally new language since Java 7: Lambdas. Multiline strings. Smart switch expressions.
var. Pattern matching. Named tuples (they’re called
records in Java).
And of course, the majesty, the crowning achievement that is virtual threads. Virtual threads are a huge deal. They provide the same benefits of
async/
await or suspensions, but without the endless verbosity of code in other languages.
Yes, you heard me right. Java’s virtual threads provide a better solution, and do so in less code, than other languages.
If you don’t know what I’m talking about, and you use those other languages, then you’re seething right now. Java? Less verbose than your favorite language? Impossible! But I’m not wrong.
## Why Virtual Threads Are a Big Deal
To
[understand virtual threads](https://openjdk.org/jeps/444?utm_source=thenewstack&utm_medium=website&utm_content=inline-mention&utm_campaign=platform), you need to understand the problem they were created to solve. If you haven’t experienced virtual threads yet, they’re sort of hard to describe. I’ll try.
Java has blocking operations — things like
Thread.sleep(long),
InputStream.read and
OutputStream.write. If you invoke one of these methods, the program won’t advance to the next line until those methods finish doing what they’re doing and return.
Most network services are I/O bound, meaning they spend the majority of their time in input and output methods like
InputStream.read and
OutputStream.write.
It’s very common to log in to a service that has no more threads in the thread pool, and yet still can’t return a response because all the existing threads are waiting on some I/O operation to happen, like I/O across the HTTP boundary, I/O to the database, or to the message queue.
There are ways to unblock the I/O. You could use
java.nio, which is anxiety-inducingly complex. You could use reactive programming, which works paradigmatically but is a complete refactoring of the entire codebase.
So, the thinking goes: Wouldn’t it be nice if the compiler knew when you did something potentially blocking (like
InputStream.read) and reordered the execution of the code? So when you do a blocking thing, the waiting code is moved off the current executing thread until the blocking thing finishes, and then it’s put back on another thread once it’s ready to resume execution.
This way, you can continue to use blocking semantics. Line one executes before line two. This promotes debuggability and scalability. You’re no longer monopolizing threads only to waste them while waiting around for something to finish. It would be the best of both worlds: the scalability of non-blocking I/O with the apparent simplicity, debuggability and maintainability of the simpler blocking I/O.
Many other languages, like Rust, Python, C#, TypeScript and JavaScript, support
async/
await. Kotlin supports
suspend. These keywords cue the runtime that you’re going to do something that blocks and it should reorder the execution. Here’s an example in JavaScript:
The trouble is that to invoke
async functions, you must also be
*in* an
async function:
The keyword is viral. It spreads. Eventually, your code ends up a quagmire of
async/
await — because why wouldn’t you use
async/
await everywhere you could? So it’s better than using low-level, non-blocking I/O or reactive programming, but barely.
Java offers a much better way. Just use a different factory method for your threads.
If you’re using an
ExecutorService to create new threads, use the new version that creates virtual threads.
If you’re creating threads directly, at a low level, then use the new factory method:
Most of your code remains completely unchanged, but now you get much improved scalability. The runtime won’t wheeze if you create millions of threads. I can’t predict what your results will be, but there’s a real chance you won’t need to run nearly as many instances of a given service to handle the load anymore.
If you’re using
[Spring Boot 3.2](https://tanzu.vmware.com/content/white-papers/spring-boot-3) (you are, aren’t you?), then you don’t even need to do any of that. Just specify
spring.threads.virtual.enabled=true in your
application.properties — and then ask your management for a raise, paid for by the dramatically reduced cloud infrastructure costs.
If you aren’t using Spring 3.2, check out how easy it is to upgrade in this 9-minute video presented by my fellow Spring advocate DaShaun Carter.
Not every application can technically make the jump yet, but the very large majority of them can and should.
## Channeling Shakespeare
Which, finally, brings me back around to the New Relic report. Don’t get me wrong: It is very well done, and worth a read. Like a Shakespearean tragedy, it’s well-written and tells a sad story.
There’s a whole section that sort of confirms the obvious: The sky is blue, and clouds are everywhere. Deploying workloads in containers seems to be the dominant pattern, with respondents reporting 70% of Java workloads using containers. Frankly, I’m surprised it’s that low.
Also of interest is the trend towards switching to multicore over single-core configurations. According to the survey, 30% of containerized applications are using Java 9’s
-XX:MaxRAMPercentage flag, which caps RAM use. And G1 is the most popular garbage collector in use. All well and good.
The report takes a tragic turn when it gets to Java versions. More than half of applications — 56% — are using Java 11 in production, up from 48% in 2022. Java 8 — which came out a decade ago in 2014 — is a close second, with nearly 33% of applications using it in production. According to the survey, a third of applications are still using a version of Java that debuted the same year that the Flappy Bird game was taken down, the Ice Bucket Challenge swept Vine and the Ellen DeGeneres Oscar selfie went viral.
The plurality of users are on Amazon’s distribution of
[OpenJDK](https://thenewstack.io/microsoft-releases-its-own-distro-of-java-21/). The report suggests that is because [Oracle](https://developer.oracle.com/?utm_content=inline-mention) temporarily introduced more restrictive licensing for its distribution. But I wonder how much of it is just a function of the distribution being the default for Java workloads on [Amazon Web Services](https://aws.amazon.com/?utm_content=inline-mention), the most prolific Infrastructure-as-a-Service (IaaS) vendor. The distribution has seen massive uptake since its debut a few years ago. In 2020, it had 2.18% of the market, and now it’s got 31%. Yowza! If so many people can move so quickly to a completely different distribution, then they ought to be able to use new versions of the same distribution, no?
There is a bit of hope, I suppose, in the
[trends](https://thenewstack.io/java-usage-keeps-climbing-according-to-new-survey/). Java 17 user adoption grew 430% in one year. So maybe we’ll see similar numbers for Java 21 — which [has been out](https://thenewstack.io/microsoft-releases-its-own-distro-of-java-21/) in general availability for almost six months now.
## So, What Are You Waiting For?
As I said in
[my talk at Voxxed Days](https://youtu.be/8l0tv3_jFoY?si=itYItELoRw78VC-d&t=1), I believe there’s never been a better time to be a Java and Spring Boot developer. Java and Spring developers have the best toys to play with. And I haven’t even mentioned GraalVM native images, which dramatically improve startup time and reduce memory footprint for a given Java application. And this works perfectly with Java 21 already.
These things are here and they’re amazing. It’s up to us to make the jump. And it’s not hard. Try it out.
Install
[SDKMan](https://sdkman.io), run
sdk install java 21.0.2-graalce and then run
sdk default java 21.0.2-graalce. This will give you Java 21 and the GraalVM native image compiler. Visit the Spring Initializr, which is my second favorite place on the web (after production), at
[start.spring.io](https://start.spring.io). Configure a new project. Select Java 21 (naturally!). Add
GraalVM Native Support. Add
Web. Hit the
Generate button and load it up in your IDE. Specify
spring.threads.virtual.enabled=true in your
application.properties. Create a simple HTTP controller:
Compile it into a GraalVM native image:
./gradlew nativeCompile. Run the binary in the
build folder.
Now you’ve got an application that takes a tiny fraction of the RAM a non-GraalVM native image would, and also able to scale to many times more requests per second. Easy, and amazing.
## Getting to Production Has Never Been This Easy
We can do this. Let’s try to get Java 21 (or Java 22?) to 99% adoption by the time New Relic does its next report — who’s with me?
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)