# End of the Road for JavaFX in JDK 8: Keeping Your Apps Alive
![Featued image for: End of the Road for JavaFX in JDK 8: Keeping Your Apps Alive](https://cdn.thenewstack.io/media/2024/10/d3e01363-gravel-1024x576.jpg)
JavaFX is a popular set of graphics and media packages that enables developers to design, create, test, debug and deploy rich client applications that operate consistently across diverse platforms. Since JDK 11, JavaFX has no longer been included in most distributions of OpenJDK. Instead, you can download it separately from the [OpenJFX website](https://openjfx.io/). [OpenJDK](https://github.com/openjdk/jdk) and [OpenJFX](https://github.com/openjdk/jfx) evolved as open source projects on GitHub and follow the same release cadence, so both have been available in [version 23](https://thenewstack.io/oracle-unveils-java-23-simplicity-meets-enterprise-power/) since last month.

Few OpenJDK distributors still provide builds with JavaFX included, ensuring the combined OpenJDK and OpenJFX are fully compatible.

[Oracle](https://developer.oracle.com/?utm_content=inline+mention) will end support for JavaFX in JDK 8 next March and will stop providing Java 8 builds with OpenJFX included, as explained in the [Oracle Java SE Support Roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html). This means that from April 2025 and onward, if you are using JavaFX, you need to find an alternative distribution if you’d like to continue to receive [security updates](https://thenewstack.io/the-hidden-threats-lurking-in-outdated-java/). This applies to all desktop applications with a user interface, server-side image handling, infotainment applications in cars and planes, set-top boxes, etc., built using the JavaFX tooling.
Lack of support for JavaFX brings several risks:

- Your CI/CD builds will fail as new Oracle JDK 8 versions no longer support JavaFX.
- You can’t fix these failing builds, as JavaFX 8 is no longer maintained as an open source project, and no separate downloads are available.
- If you decide to stick to the latest released Oracle Java 8 package with JavaFX, your system will become vulnerable to CVEs, as no new releases or security patches will become available. The same applies to bug fixes in Java and JavaFX for that version.
What are your options?

Of course, there are multiple solutions to every problem. Here are options to consider:

- You can stop upgrading your Java 8 systems and stick to the latest release of Oracle Java 8 with JavaFX. However, as mentioned, this opens up your organization to security hacks and risks.
- Upgrade your code to a newer Java version and use the free JavaFX runtime (17+). This brings additional benefits like improved performance, new Java features, APIs and more. However, it also carries many functional regression risks, and you may need to change your
[application code and review and test your entire code base](https://thenewstack.io/how-to-test-how-much-memory-your-java-application-uses/)and runtime environment. - The easiest solution is switching to another OpenJDK distribution that provides a build of OpenJDK 8 with JavaFX included. It should support the included components, including WebKit, multimedia and more. As a result, you can use your code and compiled applications as-is simply by swapping out your OpenJDK-compliant runtime.
## Conclusion
While it’s recommended that you update your applications to newer Java versions for many reasons, we understand that it’s not always possible or the investment is too significant. In that case, other OpenJDK distributions can help you keep your systems with JavaFX running on Java 8.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)