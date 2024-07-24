# Back to the Basics: Understanding Source Code
![Featued image for: Back to the Basics: Understanding Source Code](https://cdn.thenewstack.io/media/2024/07/a7636ab3-code-1024x576.jpg)
Whether you’re browsing websites, watching a TV show, using an app on your phone or even turning on the AC in your car, source code drives all those capabilities.

Developers use source code to describe to a computer how electronics should behave. But coding isn’t just for programmers anymore. Because computers are the heart of almost every modern device, programming has become more ubiquitous. Anyone interested in the basics of creating and maintaining software should understand not only why code is important but also the logic concepts and design patterns of coding principles.

**What Is Source Code?**
Source code is the set of logic instructions a programmer writes to create software. These instructions, which make up algorithms, are written in a specific programming language, such as [JavaScript](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/), HTML, CSS, [Python](https://thenewstack.io/what-is-python/), [Java](https://thenewstack.io/java-22-making-java-more-attractive-for-ai-apps-workloads/) or C#. These instructions act as a detailed recipe for computers to follow, laying out each action needed to execute a series of tasks. Those tasks are collected in a file called a program, which is written in a language a person can understand.

Just as DNA carries the instructions determining how cells should grow and function, think of source code as the DNA of every piece of software you use. Code facilitates software creation, maintenance and enhancement. It’s the epicenter of all our digital tools, apps and systems.

**Why Is Source Code Important?**
From calculating basic math to a complicated system running billions of transactions, such as a stock exchange, source code is the foundation of software for devices and technology we use daily.

Source code is essential to software maintenance, from fixing issues to optimizing and enhancing it in new ways. Through open source projects, software developers collaborate on applications and shared libraries of reusable functionality, fostering innovation and accelerating technology advancements.

One of the most critical aspects of coding is security. Identifying and resolving vulnerabilities in code prevents attackers from exploiting applications. Understanding what constitutes a threat in code is often extremely difficult and one of the challenges in building secure and stable applications.

**What Are Common Types of Source Code?**
While there are multiple ways to categorize source code, the most common approaches are:

**Open source vs. proprietary**: As the name suggests, open source is open for anyone to use or modify. It is collectively owned by the community and free for everyone. Often, the authors of open source relinquish their rights to the code so it can be used without restriction. The open source movement is extremely powerful because it fosters innovation, and technology advancements immediately spread to everyone. Proprietary or closed source code is private and can only be used by those who own it. Companies or individuals who own proprietary code only allow it to be modified or used with explicit permission. The purpose of keeping code private is to protect the owner’s intellectual property, often for profit.**Compiled vs. interpreted**: Code can not only be categorized by language but also by whether the language is compiled into an executable application or executed by an interpreter. For compiled languages, a compiler transforms high-level source code into machine code instructions of ones and zeros that a CPU understands and packages that into a stand-alone application. The application can then be read and executed directly by the computer. On the other hand, interpreted languages, like JavaScript, are read and converted to CPU instructions on the fly by an interpreter. Interpreted languages allow greater flexibility and are easier to test, but often perform poorly compared to compiled applications.
**What Are Source Code Examples?**
Let’s quickly review some examples of JavaScript and C code to see how they differ. Both examples define a function that adds two numbers together into a variable and then prints and returns the sum. If you’re unfamiliar with the concept, a function is a repeatable set of instructions a program uses.

**JavaScript**
Developers commonly use JavaScript to build web and server applications. The function shown here takes in two parameters, calculates the sum of the parameters and displays the sum using the built-in method `console.log`
. You’ll see that the argument to `console.log`
uses JavaScript’s handy string concatenation by adding a static string to the variable named `sum`
.

**C**
Developers often use the C language for system software (platforms for running other software) and embedded systems. This C function performs the same actions as the JavaScript function above. However, it outputs the sum using the C standard library function `printf`
. The `%d`
in the `printf`
statement is a placeholder for the integer sum, demonstrating C’s type-specific formatting for output.

At first glance, the syntax of the two functions looks very similar, but as you observe the subtleties, you’ll see how the two languages differ.

**What Are Source Code Tools?**
Coding tools help developers create, manage, analyze and improve code quality all while assisting them in working more effectively. Many automation tools exist to detect issues in code that result in bugs, security vulnerabilities and code smells. With these tools, a [developer can get the best value out of their code](https://thenewstack.io/arming-developers-with-the-power-of-clean-code/).

Here are the most common types of coding tools:

**Integrated development environments (IDEs)**, such as VS Code, Visual Studio and IntelliJ, are vital to aiding[developers in software development](https://thenewstack.io/10-pitfalls-to-keep-in-mind-with-ai-software-development/). IDEs include a specialized text editor that annotates code as you type, identifying syntax or other issues with your code. They also integrate into code repositories and the build pipeline to manage version control as you develop.**DevOps CI/CD tools**, such as GitHub, GitLab, BitBucket and Azure DevOps, include code repositories that store your code in a single source of truth to make it easily accessible and shareable between dev team members. Additionally, repositories track changes in source code, so you can manage different versions and undo changes. Branch and merge capability exists so developers can work on the code simultaneously without the risk of clobbering each other’s work or corrupting stable code as you develop. DevOps tools include automation of the build process so changes can be quickly and easily released.**Static code analyzers**work seamlessly in the developer workflow to detect issues in code that result in errors, vulnerabilities and technical debt without having to build and execute the application. These analyzers allow developers to catch coding errors at the earliest cycle in the development process before the application is tested and released into production. Additional benefits include helping enforce coding standards and best practices, reducing manual code reviews and educating developers on how to code correctly, which helps elevate their skills.
Source code tools don’t just detect issues. They help make developers better and improve the quality of their work, which leads to more reliable, secure software that businesses prize. Tools and solutions like [SonarQube, SonarCloud and SonarLint](https://www.sonarsource.com/lp/products/all/?utm_medium=referral&utm_source=newstack&utm_campaign=ss-sonar-products24&utm_content=media-tns-sourcecode-240718-&utm_term=&s_category=Organic&s_source=External%20Referral&s_origin=newstack) improve code quality and help developers achieve the best value from their No. 1 asset: source code.

**Final Thoughts**
Source code quality can determine the success or failure of applications and systems that are essential for our daily lives and work. As a developer, you must not only understand coding concepts but also ensure you’re using the proper development and testing tools. By integrating these essential components, you will efficiently produce quality work, securing your success.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)