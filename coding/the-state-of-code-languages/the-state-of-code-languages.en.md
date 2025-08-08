*This article explores Volume 4 of a four-part report series. Click* [*here*](/blog/the-state-of-code-reliability/ "here") *to start from the beginning.*

Over the last few weeks, Sonar's [**The State of Code**](/the-state-of-code/ "The State of Code") report series has helped development teams explore the real-world state of software development. We’ve uncovered the most common reliability bugs, security vulnerabilities, and maintainability issues found across billions of lines of code. This article covers the fourth and final report in the series, where we shift from universal principles to the [specific challenges within the programming languages](/resources/the-state-of-code-languages-report/ "specific challenges within the programming languages") that development teams use every day.

This analysis is not based on surveys, but on concrete data from the real issues developers are encountering in their work. Our findings are drawn from an analysis of Sonar's massive dataset from the last six months of 2024, which includes:

* More than 7.9 billion lines of code.
* Contributions from over 970,000 developers across more than 40,000 organizations
* Analysis of Java, JavaScript, TypeScript, Python, C#, C++, and PHP

Here are some of the most prevalent language-specific issues we uncovered, why they create problems for development teams, and how to fix them before they ever reach production.

### Top Java issue: Delivering code with debug features activated

One of the most common security issues in Java code is leaving debug features enabled in production. This often happens when a developer uses a feature like a stack trace printout for troubleshooting and forgets to remove it before deployment—an easy mistake to make, but one with severe consequences.

* **Why it's a problem:** For developers, managers and business leaders, it’s a critical security risk. Leaked stack traces and other debug information provide a roadmap for attackers, exposing sensitive details about your application’s frameworks and architecture. This intelligence expands the attack surface and can turn a minor intrusion into a catastrophic breach. Fixing these issues late in the development cycle leads to lost time and costly delays.
* **How to fix it:** The key is to ensure that all debug-related settings are turned off in the final production build. Relying on manual review is prone to error, especially under tight deadlines. SonarQube automates this check, systematically detecting debug features that are unsafe for production. By integrating it into the CI/CD pipeline, you can use a quality gate to automatically prevent this code from being deployed, protecting your application from inadvertently giving attackers the information they need.

### Top JavaScript issue: Code that doesn’t do anything

The most frequent bug in JavaScript is the presence of statements that have no side effects and don’t change the program’s control flow. Often a sign of incomplete refactoring or a simple typo, this dead code can completely alter an application's logic. A classic case is an “if” statement followed by a lone semicolon, which silently causes the condition to be ignored and the next block of code to run unconditionally.

* **Why it's a problem:** For a developer, this is a frustrating bug. The code looks correct at a glance but behaves unexpectedly, leading to wasted hours spent debugging. For a manager, this is a productivity killer. It represents a preventable error that creates instability and consumes valuable developer cycles that should be spent on innovation. These "do-nothing" statements increase maintenance time and overhead as teams chase down logical mistakes.
* **How to fix it:** The best defense is a static analyzer that understands JavaScript’s nuances. SonarQube flags these useless but potentially dangerous statements as you code, providing real-time feedback directly within the developer's IDE. This ensures that the code behaves as intended and prevents these subtle bugs from derailing a project.

### Top Python issue: Using clear-text protocols

A critical security risk frequently observed in Python applications is the use of unencrypted, clear-text protocols like FTP and HTTP. Using unencrypted channels is the digital equivalent of sending login credentials on a postcard, exposing applications to data theft, malware, and malicious redirects.

* **Why it's a problem:** For developers, using an insecure protocol creates a gaping and unjustifiable security hole. For business leaders, this is a direct threat. It not only risks a data breach but can also lead to significant financial penalties from data protection violations and cause severe reputational damage. The risk of leaving an application perpetually exposed to data theft and unauthorized access far outweighs any perceived convenience.
* **How to fix it:** All data transmission must use secure, encrypted protocols. SonarQube’s security analysis automatically detects the use of insecure protocols like FTP, Telnet, and HTTP within your Python code. By identifying these vulnerabilities early in the development lifecycle, Sonar empowers teams to build applications that are secure by design and ensures all transport channels are secured.

### Building secure code in every programming language

Understanding and addressing these common pitfalls is about more than just avoiding errors; it’s about mastering the tools of the trade. This has never been more critical, especially as AI coding assistants generate more code than ever before. The quality of the human-written code these tools learn from is paramount to ensuring a secure and reliable software future.

These findings are just the beginning. Our new report provides a much deeper analysis of the top issues across these three major languages, as well as TypeScript, C#, C++, and PHP.

[**Download The State of Code: Languages report**](/resources/the-state-of-code-languages-report/ "Download The State of Code: Languages report") today to see:

* The most prevalent bugs and security issues across the most popular programming languages software developers use.
* A breakdown of the most common maintainability issues (aka code smells) in each language.
* Actionable solutions to help you eliminate these language-specific issues.