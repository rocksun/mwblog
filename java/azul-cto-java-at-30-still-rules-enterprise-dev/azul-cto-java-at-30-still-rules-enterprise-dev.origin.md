# Azul CTO: Java at 30 Still Rules Enterprise Dev
![Featued image for: Azul CTO: Java at 30 Still Rules Enterprise Dev](https://cdn.thenewstack.io/media/2025/05/71dcac54-jac-alexandru-nx6fp9n4xgw-unsplash-1-1024x576.jpg)
The Java programming language turned 30 today.

And 30 years after its debut, [Java](https://thenewstack.io/java-at-30-the-genius-behind-the-code-that-changed-tech/) remains the champion of [enterprise software development](https://thenewstack.io/why-pure-ai-coding-wont-work-for-enterprise-software/), defying decades of predictions about its demise and continuing to power the world’s most critical business applications.

“Java has by far the best track record answer to that,” [Gil Tene](https://www.linkedin.com/in/giltene/), co-founder and CTO of [Azul Systems](https://www.azul.com/), told The New Stack when asked about long-term application maintainability. “You can hire people today. You have millions of people to hire today with the skills to maintain applications written 10 and 15 years ago in Java. There’s no other language that can actually say that.”

## Surviving Hype Cycles
Java has weathered numerous technological challenges that were supposed to supplant it. Tene cited examples: “I remember answering that question 20 years ago, and I’ve been answering it kind of the same way ever since, because you might remember in the early 2000s there was the [LAMP](https://thenewstack.io/should-the-lamp-stack-add-an-open-llm-like-metas-llama/) [[Linux](https://thenewstack.io/introduction-to-linux-operating-system/), [Apache](https://thenewstack.io/configure-multiple-websites-on-a-single-rhel-based-apache-host/), [MySQL](https://thenewstack.io/a-cheat-sheet-to-database-access-control-mysql/), [PHP](https://thenewstack.io/why-php-usage-has-declined-by-40-in-just-over-2-years/)/[Perl](https://thenewstack.io/this-week-in-programming-pondering-the-evolution-of-perl-7/)/[Python](https://thenewstack.io/what-is-python/)] stack that was going to take over the world and going to kill Java, and not a lot of LAMP stack programmers around anymore.”

The list of Java “killers” reads like a graveyard of once-hot technologies. “Then we had [Ruby on Rails](https://thenewstack.io/dhh-wants-to-make-web-dev-easy-again-with-ruby-on-rails/) that was going to take over the world and kill Java, and really hard to find [Ruby programmers](https://thenewstack.io/ruby-creator-yukihiro-matsumoto-on-the-challenges-of-updating-a-programming-language/) to maintain that stuff anymore,” Tene added.

What’s remarkable isn’t just Java’s survival — it’s its continued growth. “Java hasn’t shrunk at all. Java has just kept growing and growing and growing, and it has neighbors that also grow and grow and grow,” Tene explained.

## From Hardware Pioneer to Software Innovator
Azul Systems itself embodies Java’s evolution. Founded in 2002, the company initially took a novel approach to addressing Java performance by building custom hardware. “We built some interesting hardware solutions for data centers around running Java applications and in consolidating them, centralizing them in what we called computer appliances and farms of compute appliances,” Tene recalled. “Today, we would call it a virtual Java cloud.”

But as the computing landscape shifted, so did Azul. “We shifted away from, pivoted away from hardware in the late 2000s as commodity hardware became good enough, and as hypervisors, virtualizers and eventually cloud took over,” he explained. The company transformed into what he calls “a pure software company” about 15 years ago.

Today, Azul occupies a unique position in the Java ecosystem. “We have the largest engineering team in Java,” Tene said. “We have probably the biggest commercial offering other than [Oracle](https://developer.oracle.com/?utm_content=inline+mention) in the Java space as well,” he said. The company now serves customers across every industry vertical, focusing on making Java run faster and more efficiently.

## Breaking Performance Barriers
Azul’s [Optimizer Hub](https://www.azul.com/products/components/azul-optimizer-hub/) represents a fundamental shift in how [Java virtual machines](https://thenewstack.io/introduction-to-java-programming-language/) (JVMs) operate. Instead of each JVM optimizing code independently, the technology allows entire fleets of JVMs to share optimization data.

“It allows a fleet of JVMs to coordinate, share experiences and cross-optimize together, rather than each JVM run on its own and deal entirely with the problem that it has to deal with on its own,” Tene said.

Some “really big places” have adopted the technology, taking it into production environments with tens of thousands of JVMs and “coordinating fleets,” he said.

Azul’s latest innovation is [JVM Inventory](https://www.azul.com/products/components/jvm-inventory/), launched last month. A feature of Azul Intelligence Cloud, JVM Inventory is a Java discovery tool and “cloud service that continuously catalogs running JVMs to slash months off Oracle Java migration timelines and help ensure ongoing Oracle license compliance for audit defense,” the company asserts.

In addition, the company’s [Falcon JIT compiler](https://www.azul.com/products/components/falcon-jit-compiler/), built on the LLVM framework, demonstrates Azul’s commitment to pushing Java performance boundaries. “The Falcon JIT compiler produces the fastest Java of any JVM in the world by a big margin. It is 30 to 40% faster than the [C2 compiler](https://www.baeldung.com/jvm-tiered-compilation) in [OpenJDK](https://thenewstack.io/microsoft-releases-its-own-distro-of-java-21/),” Tene claims.

## From Applets To AI
Java’s evolution tells the story of modern computing itself. What started as “this interesting, quirky little thing in a web browser 30 years ago” has become the backbone of enterprise computing, Tene said.

In the late ’90s, Java “kind of barged into the field of enterprise computing and then dominated enterprise applications within three or four years of its initial introduction,” he added.

“If you look at the beginning of Java and how quickly it displaced everything else that was used to build business applications before it, we can say that we haven’t yet seen the thing that will displace Java,” Tene noted. “From the point where it happens until everybody’s just building applications in that [new language] and not Java, it’ll probably only be about two to four years, and we haven’t seen the signs of that kind of trend happening at all.”

Yet, even in the emerging AI landscape, Java is finding its place. “Java is currently, from stats I heard a couple months ago, the number three language for that, with Python being by far the first,” Tene said about AI application development. “We’re seeing a really large increase in the number of applications that are looking to incorporate AI into the application, and that becomes a natural thing for Java applications to do.”

## The Enterprise Advantage
Java’s staying power comes down to a simple business reality: enterprises need software that lasts. “When you try and figure out what you want to build your application in, one of the things you should think of is, how are you going to maintain it five years from now, 10 years from now? Are you going to be able to hire the people you need in order to keep this thing alive and going?”

This philosophy extends to Java’s open source ecosystem. “The Java community as a whole tends to produce long-lived frameworks and projects and libraries people use and then rely on for many, many years,” Tene explained. “Most Java community projects, if you look at them, don’t have a lot of scandals going on, don’t have a lot of dictators or annoying people running them.”

Azul has witnessed this stability firsthand across its customer base. “Since Java is so universal, so prevalent, we have customers in pretty much every vertical you can think of, of all sizes,” Tene said. “When they want to run Java well or better, when they want either good metrics for Java applications, which is what our prime platform is excellent at, or they just want very good, responsibly built, supported, open source, that is what our core platform is. We serve those customers.”

Moreover, JavaScript is for web GUIs and Python is a way developers “write their very lightweight things and services. But anytime you see things mature — go from prototyping and some initial functionality to ‘I need to run this at scale, and I can’t have it cost 50 times what it needs to,’ they tend to transition to something like Java,” Tene said. He cited [Twitter](https://www.infoq.com/articles/twitter-java-use/) (now X) and [LinkedIn](https://www.linkedin.com/blog/engineering/infrastructure/linkedin-s-journey-to-java-11) as examples.

“We see a lot of people rewriting large backends in Java or Java-based languages like [Kotlin](https://thenewstack.io/get-started-using-kotlin-multiplatform-with-a-network-listener-project/) or [Scala](https://thenewstack.io/scala-creator-proposes-lean-scala-for-simpler-code/) or whatever the new language this year for the JVM is, but they’re all Java-based in that sense, we just see more, not less,” Tene said.

## Modern Java’s Renaissance
Meanwhile, users who may remember Java as verbose and cumbersome might be surprised by its modern incarnation. “[Java 25](https://openjdk.org/projects/jdk/25/), which is coming out later this year, is dramatically more approachable and nicer and easier to get something off the ground than Java 8 was,” Tene said.

The language has also embraced [cloud native development](https://thenewstack.io/cloud-native/) with innovations like virtual threads, which promise to simplify concurrent programming. “One of the shifts that is attempted, at least in Java, and I think with Java 25 and above, we’ll have an interesting chance of going back to the simple old notion of a thread that an operation runs in, and the ability to run millions of those threads at the same time.”

Azul is also contributing to Java’s instant-start capabilities through projects like [Coordinated Restore at Checkpoint ](https://openjdk.org/projects/crac/)[(CRaC](https://openjdk.org/projects/crac/)[)](https://openjdk.org/projects/crac/). “That OpenJDK project that we lead is focused on providing very quick starts to Java applications and cloud environments. So, think of microservices that autoscale or cloud functions that need to start very quickly.”

## Nothing Lives Forever
Despite Java’s current dominance, Tene acknowledges that nothing lasts forever in technology. Something will eventually displace Java. “When that happens, I’m sure, whether it’s called Java or something else, I’m sure we’re going to be playing a lot with it and talking a lot about it and excited about it, too.”

But for now, three decades after its birth, Java continues to prove that sometimes the best technology is not the newest — it’s the one that works, scales and endures. As Tene put it, regarding what big programming language might come next: “We just haven’t seen it yet, and I’ve been saying this since the early to mid-2000s so, you know, I have been looking, I just haven’t seen it.”

Meanwhile, in an industry obsessed with the next big thing, Java, at its 30th anniversary, continues to thrive, showing that reliability, maintainability, and a strong ecosystem often matter more than cutting-edge features.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)