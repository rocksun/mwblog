# Java: Where the Wild Things Aren’t
![Featued image for: Java: Where the Wild Things Aren’t](https://cdn.thenewstack.io/media/2024/10/210626fb-monster-1024x576.jpg)
Over the last decade, the OpenJDK community has made [Java](https://thenewstack.io/oracle-unveils-java-23-simplicity-meets-enterprise-power/) significantly safer for users while also simplifying the development process for software engineers. This combination has resulted in [fewer security issues](https://thenewstack.io/5-javascript-security-best-practices-for-2024/) and a clearer process for handling the inevitable security issues that happen with all software.

Specifically, there are three things that have helped with this improvement:

- A secure Java Development Kit (JDK) that patches vulnerabilities in a prompt manner and releases on schedule.
- A modular JDK that decreases the attack surface by creating a trust boundary and helping remove unnecessary modules.
- A managed community with clear ownership of software libraries.
## A Secure JDK With Prompt Updates
The Java Development Kit is released four times a year, following a pre-published schedule. Each release makes standard improvements as well as patching any new security risks. The dedicated OpenJDK Vulnerability Group helps triage and prioritize vulnerabilities so that they can be fixed with appropriate haste. This coordination with researchers who report vulnerabilities ensures that patching is performed in a timely manner.

A secure JDK does not mean one in which no vulnerabilities occur; it means that when vulnerabilities do occur, they are addressed promptly and correctly.

### Scheduled Patches
Security and improvements are released four times a year, all on pre-published dates. These dates allow project managers and others to schedule Java patching as a known quarterly activity. Rather than subscribing to an email list and reacting to alerts, users can slot time in on or after the third Tuesday every three months: January, April, July and October.

A crucial part to [addressing and patching vulnerabilities](https://thenewstack.io/the-hidden-threats-lurking-in-outdated-java/) is keeping track of what they are and telling people about them. A key part to community work is attributing credit to the researchers who find security issues and properly disclose them to help open source projects.

### Common Vulnerabilities and Exposures (CVEs) Advisories
The OpenJDK Vulnerability Group maintains [a list of the CVEs patched in each Java release](https://openjdk.java.net/groups/vulnerability/advisories/), with acknowledgements to the different researchers who engaged in responsible disclosure. This offers downstream Java users the ability to answer a simple question: If I use a previous version of Java, what risk do I accept by doing so?

Another excellent aspect that the OpenJDK Vulnerability Group does in these advisories is to track CVEs by component, since not all Java users leverage every component.

In short, simply saying that an older Java installation contains a CVE is not sufficient to indicate that the vulnerability exists on that system.

### Consistent Naming
In early 2019, the primary OpenJDK distribution on Docker was serving “[mystery meat Java](https://www.infoq.com/news/2019/06/docker-vulnerable-java/),” a build of the source code taken out of sync with the patch schedule that missed various security patches but still used the version number of the JDK that contained the security flaws. As a result, users of the Docker image were left insecure while users of known downstream Java distributions were secure.

By recognizing the need for vulnerability disclosure and using the pre-published quarterly patch cadence, Java vendors working on OpenJDK revolve around the same numbering scheme via [JEP 322](http://openjdk.java.net/jeps/322) (time-based release versioning). Through coordination of version numbers centered around the quarterly patch schedule, most Java vendors use the same numbers in a way that can be understood and compared against each other to know which was released later and which security patches are present in that version.

The alternative to this coordination would be a situation of semi-predictable yet meaningless numbers that would require special lookup tables to know which security patches were present where.

## A Module-Based JDK Decreases the Attack Surface
The original documentation for Java 8 and below provides a [conceptual diagram](https://docs.oracle.com/javase/8/docs/) of where certain features are. From a threat-modeling perspective, this is the same location where vulnerabilities live.

A few slices are readily identifiable:

- The risk of drive-by downloads or execution is concentrated solely in the Deployment Plugin, which is no longer available in modern Java runtime environments (JREs).
- SQL injection can only occur if the application uses Java Database Connectivity (JDBC). Applications that do not use SQL are not vulnerable to SQL injection.
- Attacks against XML, such as
[XXE](https://www.youtube.com/watch?v=x6QQzgf0j7o&feature=emb_logo), occur within the XML JAXP area. [Deserialization attacks](https://github.com/frohoff/ysoserial)stem from the deserialization component and the IO structures.
The benefit to developers and those who run applications is that it becomes possible to look at an application and trim down the things that you should worry about to the things that you use. This emphasizes the importance of the module information within the quarterly security advisories from the OpenJDK Vulnerability Group.

Developers can look at these modules and examine the risk present in each as it pertains to their application. An example is sensitive data and the risk of exposure; this would be present in the Logging module, but far less so with a module like Image/IO. The core benefit is simply understanding which risks are present and where those risks are, rather than worrying about ambiguous and unidentifiable threats, with defenses in the wrong places.

Another point is to recognize what does not appear in the conceptual diagram and focus on the area where it does appear. For example, in the core Java diagram and modules, there is no concept of “web” or HTML. This means that work against web threats, such as cross-site scripting (XSS), belongs in the frameworks or tools that provide that functionality.

### Reducing Risk by Removing Modules
Hackers cannot attack what isn’t there. Rather than defending applications against myriad threats, simply removing unneeded modules provides 100% mitigation of any threat that requires that module.

A [conceptual diagram](https://docs.oracle.com/javase/8/docs/) lays out what these modules look like and how they relate to each other. Developers who create an application or service can use tools like jlink to [create custom JREs](https://www.baeldung.com/jlink) that remove certain modules.

- Removing JDBC (database connectivity) will prevent SQL injection attacks from working because database queries will no longer be there.
- Removing ImageIO will prevent any image-related vulnerabilities, such as
[CVE-2020-14562](https://nvd.nist.gov/vuln/detail/CVE-2020-14562). That CVE was in ImageIO, so when ImageIO is removed, there is no more attack surface. - Removing the XML JAXP area mitigates
[XXE](https://www.youtube.com/watch?v=x6QQzgf0j7o&feature=emb_logo)vulnerabilities, as XML is no longer present. (XML was deprecated in Java 9 and removed in 11, so this is now the default.)
When modularity is used, the default security of a JDK is much stronger. A JDK version that is flagged as “vulnerable” may not actually be vulnerable.

This distinction is crucial, as many software teams are expected to do vulnerability scanning in the form of open source dependencies. Scanners often look only at the library names and then assume that all the libraries used contain all CVEs. In the case of a custom jlink-ed JRE, any scanner that reported the JRE as vulnerable to this flaw would be incorrect. Removing the component removes the vulnerabilities and risk in that component. Hackers cannot attack what isn’t there.

## A Managed Community Clearly Owns Software Libraries
The majority of Java dependencies come from Maven Central, where libraries are composed of three parts: a group, an artifact and a version. By providing a clear level of ownership, [Sonatype](https://www.sonatype.com/?utm_content=inline+mention), which runs Maven Central, has created an environment where Java developers don’t really need to worry about attacks like [dependency confusion](https://fossa.com/blog/dependency-confusion-understanding-preventing-attacks/) that occur in other communities.

All Maven dependencies are identified by a combination of three things: group, artifact and version. The group represents a namespace, often using Java’s reverse-DNS style. To publish an artifact, developers need some level of connection to the namespace. For instance, a developer who works for example.com could not publish artifacts under an established group (not com.example) where they had no affiliation.

Additionally, having one primary source of libraries blocks another series from obtaining components from random places on the internet, where domains expire and are sold. This happened in the JavaScript community, where [a firm bought Polyfill](https://arstechnica.com/security/2024/07/384000-sites-link-to-code-library-caught-performing-supply-chain-attack/) and replaced the original library with new code that was immediately served to hundreds of thousands of sites. When code is swapped or groups don’t quite match, Java makes it very easy to detect.

## Tactical Takeaways
Ultimately there are three actions teams can take to ensure that their applications and systems remain secure.

- Patch Java, ideally once per quarter along with the published schedule.
- Use modularity to decrease the attack surface of their applications.
- Regularly patch dependencies from trusted sources.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)