“Java is old, boring and enterprise-y!” That’s what my co-founder Travis Reeder shouted over the wind as we boated and bounced along the Sacramento-San Joaquin Delta, somewhere between corporate burnout and midlife coding crisis. “I want to have fun writing code again!”

That’s why we launched our consulting firm in Ruby in 2009. And in 2011, we switched our next startup, Iron.io, to Go — posting what might’ve been the first-ever job listing to the go-nuts mailing list.

Fast forward 15 years, and [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) is going through a [full-blown renaissance](https://thenewstack.io/java-modernizes-new-tools-for-ai-and-quantum-age/). It’s becoming fun again, and strangely, I’m on the team making that happen.

## **Whoops! It Worked.**

I get Travis’ sentiment. In 2005, when the creator of Ruby on Rails, David Heinemeier Hansson, [dropped his famous](https://www.youtube.com/watch?v=Gzj723LkRJY) quote — “Whoops! It worked. We are up and running.” — while demoing Rails scaffolding for the first time, Travis was likely using Java 1.4. Not only were there no record classes, switch expressions or pattern matching — there were also no lambda functions, streams or generics, and J2EE was the framework du jour, complete with SOAP and WSDL support. And here was DHH building a functioning blog from scratch, live on stage in 16 minutes, without ever saying the word “enterprise” or “bean.” It was glorious.

And so, the next decade of my life was spent writing Ruby and Go, staying uninterested and uninformed of Java’s quiet and rapid progress, until a series of events led to the acquisition of our company and my joining the Java Platform Group at Oracle.

## **Release Cadence**

We recently launched [Java 24](https://blogs.oracle.com/java/post/the-arrival-of-java-24?source=:ex:pw:::::TNS_Java_Renaissance_A&SC=:ex:pw:::::TNS_Java_Renaissance_A&pcode=) at JavaOne 2025. New versions of Java are released every six months, like clockwork, on the Tuesday of ISO weeks 12 and 38, and have been for over seven years. This [time-based release model](https://www.java.com/releases/) is a big change from the former feature-based model, where a release would be pinned to a specific feature that often took over three years to get out the door.

This predictable six-month release cadence has delivered numerous benefits, such as getting new features into the hands of developers faster, breaking large concepts (such as pattern matching) into smaller incremental changes (pattern matching for `instanceof`), establishing predictability for companies that rely on Java, and enabling a process for preview features that can collect real-world feedback and change before going final. The six-month release cadence also means there is no rushing to include things before they are ready — because if a feature needs more time, another train is right around the corner.

A ton of functionality has gone into Java under this cadence: records, pattern matching, virtual threads, a foreign function and memory API, and a super-low-latency garbage collector, just to name a few. I’ll cover some of the themes of this work, but first let’s discuss the enabler of all of this: OpenJDK.

## **OpenJDK**

[OpenJDK](https://openjdk.org/) was launched in 2006 as a place to collaborate on an open source implementation of Java, and today, many companies and individuals contribute to Java through OpenJDK. See the contribution map to OpenJDK for JDK 24 [here](https://blogs.oracle.com/java/post/the-arrival-of-java-24?source=:ex:pw:::::TNS_Java_Renaissance_A&SC=:ex:pw:::::TNS_Java_Renaissance_A&pcode=).

Notice I said OpenJDK is a “place,” not a thing. OpenJDK has projects, groups, members, mailing lists, wikis, JDK Enhancement Proposals (JEPs), and artifacts such as source code or even images of Java’s mascot, Duke. OpenJDK is not a “build of Java” that someone can download and use to run their applications. In addition to stewarding and contributing a majority of the work that goes into OpenJDK, Oracle also builds distributions, including some licensed under the GPLv2 (with Classpath Exception), some under the Oracle “No Fee Terms and Conditions” license, and others under Oracle’s commercial license for longer-term support.

## **Java’s Language Renaissance**

Project Amber, led by Oracle’s chief language architect, Brian Goetz, is the primary driver responsible for Java’s current language evolution. This project has delivered significant improvements across three vectors: first, making the Java language more expressive (and thus concise); second, making it more “data-oriented”; and third, simplifying it for new learners and small programs — all while enabling the language to remain readable, maintainable and compatible. This is a tall order, but with careful evolution, it has been a successful endeavor.

Expressiveness is obvious across the features from Amber. For example, text blocks and local-variable type inference turn code like this:

|  |  |
| --- | --- |
|  | String html = "<html>\n" +                "    <body>\n" +                "        <p>Hello, world</p>\n" +                "    </body>\n" +                "</html>\n"; |

into this:

|  |  |
| --- | --- |
|  | var html = """             <html>                 <body>                     <p>Hello, world</p>                 </body>             </html>             """; |

Record classes turn the hundreds if not thousands of lines of “data carrier” classes we’ve written into this:

|  |  |
| --- | --- |
|  | record Person(String name) { } |

And pattern matching allows for simple type patterns like this example with `instanceof`:

|  |  |
| --- | --- |
|  | if (obj instanceof Person p) {  System.out.println(p.name());  } |

… as well as object deconstruction use cases with record patterns:

|  |  |
| --- | --- |
|  | if (obj instanceof Person(String name)) {  System.out.println(name);  } |

And we can combine all of the above into patterns for `switch`:

|  |  |
| --- | --- |
|  | switch(o) {  case Person(String name) && !name.isEmpty() -> "Person: " + name  case Vehicle(String plate) && !plate.isEmpty() -> "Vehicle: " + plate  } |

This is probably the most common form of pattern matching.

This is not just less code but also less error-prone code, and it becomes more expressive and powerful as you start to unpack the power of these features together.

But it’s not just the details that are changing; the types of programs people are writing are changing too. Many programs now are essentially receivers, processors, and senders of data to/from external sources: databases, APIs, large language models (LLMs), etc.

To use an example: A Slack bot takes a support request from one of your customers, which then calls your CRM API, and then asks an LLM to use all of that to structure a response back to your customer. Rather than using classes to model business entities and processes, which is a traditionally great idea for larger complex applications, you can now use classes to simply model the data itself. You can use a record to model the JSON API response, patterns to deconstruct the data, sealed classes for exhaustive analysis, and text blocks to form the LLM prompt. The features we’ve talked about allow you to write beautifully structured data-oriented programs.

Finally, the language is not just becoming better and more beautiful for professional developers solving modern problems, but it is also becoming simpler for learners and small programs. An effort called “Paving the On-Ramp,” part of Project Amber, tackles this simplification. In short, the first Java program has gone from this:

|  |  |
| --- | --- |
|  | public class HelloWorld {  public static void main(String[] args) {  System.out.println("Hello, World!");  }  } |

… to this:

|  |  |
| --- | --- |
|  | void main() {  IO.println("Hello, World!");  } |

Java is an incredible platform for teams building larger programs, but for students and learners, the perception that the example of the first Java program gave was one of complexity and verbosity, especially in a multilingual world where other languages simply offer `print()` as the one and only line of code.

And there’s more to paving the on-ramp. For example, the single/multi-file source code introduces the ability to launch a source-code program with the Java launcher without first needing to explicitly compile the source code. And there’s also a new shebang construct that allows your Java file to launch like a script. Taking the following source file:

|  |  |
| --- | --- |
|  | #!/path/to/bin/java --source 24 --enable-preview    void main() {    IO.println("Hello, World!");  } |

… and making it executable:

You can now run it:

|  |  |
| --- | --- |
|  | $ ./myscript  Hello, World! |

This is just the beginning for what’s possible with modern Java, which is once again fun to write, still backwards compatible, easy to maintain and even easier to read. We haven’t even touched upon other areas of innovation like new APIs, better performance, cleaner observability, better runtime ergonomics and more.

So, the next time I get Travis out on the boat, we should have a lot to talk about, given how much Java has evolved under the six-month release cadence to address modern architectures, styles and program types. He really has no reason not to start his next project in Java.

In the next installment of this three-part series, we’ll talk about Java’s platform renaissance, and in the third part, we’ll discuss Java’s AI renaissance.

Stay tuned!

*To learn more about where the Java language is going, watch* [*Brian Goetz’s talk*](https://www.youtube.com/watch?v=1dY57CDxR14) *from JavaOne.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/06/24c6b501-cropped-02c6541f-chad-arimura-600x600.jpeg)

Chad Arimura is vice president of Java Developer Relations at Oracle, overseeing the developer relations and Java in Education teams. Before joining the Java Platform Group at Oracle, Chad led an engineering team that delivered the Fn Project, and downstream...

Read more from Chad Arimura](https://thenewstack.io/author/chad-arimura/)