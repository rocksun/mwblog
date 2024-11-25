# Use These DevOps Pipelines To Cut Automation Tool Costs
Many IT organizations utilize licensed automation tools, but providing licenses to all QA and development personnel is impractical. Typically, licenses are allocated to designated automation engineers who create and run tests as needed. This [creates a challenge in allowing any team](https://thenewstack.io/top-challenges-to-creating-high-performing-engineering-teams/) member to execute tests as required. With most automation engineers located offshore, additional licenses would be needed for onshore test execution, which can be expensive. Furthermore, ensuring high code quality, adequate coverage, absence of code smells, and thorough security scans is crucial.

My organization is large and operates in several domains, such as ERP, Data, Laboratory Information Management Systems (LIMS), Automation and Robotics Software, Bioproduction, and Cell/Gene Therapy Software. Each domain utilizes its own in-house DevOps solution, mostly Jenkins, which incurs monthly costs. To have a unified DevOps framework across the organization, I researched several DevOps tools to identify the best cost-effective solution. The intent was to have a single framework that can be utilized across various projects in different domains.

In return, this DevOps solution reduced the license cost for third-party automation tools used by different projects. Once this CI Pipeline is ready, anyone with DevOps tool access can invoke automation tests without worrying about the need for an automation test tool license.

So, I started contacting several vendors and finally listed Jenkins, GitHub Actions(GHA), and Gearset as common tools that can be used across several domains. On further analysis with my team, we found GHA to be the winner in terms of cost and ease of inculcating security checks and unit tests in the Pipeline.

In this article, I demonstrate the advantages of GitHub Actions (GHA) as a CI tool. GHA is open source but incurs costs based on runner usage. I propose an innovative solution to eliminate runner costs, too. Integrating code quality tools like [SonarQube and CodeQL into the pipeline also ensures security](https://thenewstack.io/how-to-install-the-sonarqube-security-analysis-platform/) scans and highlights issues before deployment.

## Advantages of Implementing a Continuous Integration (CI) Pipeline
-
**No Automation Tool User Access Is Required for Invoking Tests**
Automation tools that require licenses can only be used by licensed individuals. However, when integrated with a CI pipeline, any user with CI access can initiate jobs without needing a direct license. This approach optimizes the management of the license pool, reduces costs, and extends the tool’s utility for test automation. For instance, all developers with GitHub Actions (GHA) access can now invoke the automation tool without requiring individual licenses.

-
**Eliminating Requirement for QA Resources**
Some automation tools prevent testers/developers from navigating away from the UI screen during UI test execution, blocking them from performing other tasks on their computers. Utilizing the GitHub Actions (GHA) pipeline to invoke the automation tool removes this restriction, allowing [developers and testers to work](https://thenewstack.io/using-ai-to-help-developers-work-with-regular-expressions/) on other tasks while the automation runs in the background. After execution, an email with a detailed, user-friendly PDF test results report is sent.

![](https://cdn.thenewstack.io/media/2024/11/7aeaa9aa-image_7.png)
Fig – Depicting Automation helps in reducing manual efforts

Before CI Pipeline — The Manual Test Execution Setup has effectively reduced our hours from XXX to XX, but we still need to allocate XX hours because a QA resource must monitor the screen during test execution.

![](https://cdn.thenewstack.io/media/2024/11/246aeb70-image_8.png)
Fig – Depicting Github Actions further reducing Automation efforts to ZERO

Automated CI/CD Integration — reduces these XX hours to zero, as the CI pipeline manages sessions, eliminating the need for manual monitoring during test execution.

**Other Benefits of Using GHA as CI/CD Tool for Automation Tests**
-
**GHA Access Is Free With a User GitHub Account**
GitHub Actions is a GitHub feature that is by default enabled; hence, no explicit access is required for GHA. It supports CI/CD workflows directly in your repositories.

-
**Cost Savings****—****Eliminating AWS Infrastructure Cost**
For the CI/CD pipeline, we need to integrate a runner (virtual machine needed for running CI jobs), which typically is provisioned in a cloud such as AWS, incurring additional cost that grows as load increases. With this solution, however, we are utilizing organization-provided Win365 machines as runners, hence eliminating the additional [infrastructure runner cost incurred when using cloud services](https://thenewstack.io/cloud-vs-on-prem-comparing-long-term-costs/). All automation engineers are provided with Win365 machines for installing and executing automation scripts.

![](https://cdn.thenewstack.io/media/2024/11/354c6eef-image_5.png)
Fig – Microsoft Win365 vs AWS EC2 Instances

## Replacing AWS Runners With Win365 Runners
If provided with a virtual machine mirroring their desktop, [automation team members are required](https://thenewstack.io/platform-teams-automate-infrastructure-requirement-gathering/) to install automation tools. This cloud instance incurs fixed charges. QA resources use this cloud instance only during their business hours, leaving it free for the remaining 16 hours each business day. We can significantly reduce AWS usage by leveraging these VMs as CI pipeline runners during this free time, eliminating the need to spin up new EC2 instances.

The diagram below depicts cost savings. Here, we incur a fixed monthly VM cost of $55; hence, a pipeline using these VMs will incur a $0 runner cost, but if a new AWS instance were being used as a runner, we could have incurred an $80 monthly cost.

![](https://cdn.thenewstack.io/media/2024/11/bace220b-image_2.png)
Fig – Cost Savings Calculation

-
**Firewall Constraints and Automation Tool Configurations**
With GitHub being managed internally within the organization network, we can avoid any security system and automation tool API permission issues which is a challenge with externally hosted CI/CD tools.

-
**Code Quality Checks Implementation**
In the CI pipeline itself, we can implement CodeQL and SonarQube code quality tools avoiding any separate need for testing. CodeQL is a heavy tool in terms of time. It takes a lot of time for the pipeline to be executed, so triggering CodeQL in a separate pipe, line, and results that can be viewed within GitHub is always recommended.

### What Is CodeQL
![](https://cdn.thenewstack.io/media/2024/11/7158fdea-image_4-1024x471.png)
Fig -Post running the pipeline, errors, if any, highlighted by CodeQL can be viewed.

Finally, the DevOps pipeline for deploying code and running automation tests against the newly released cut branch will look like this:

![](https://cdn.thenewstack.io/media/2024/11/d60e743b-image_3-1024x707.png)
Fig – DevOps Pipelines for deploying code, running code quality checks, and finally running automation tests

## Conclusion
The decision to move forward with GitHub Actions as a CICD tool for various domains has proved to be fruitful for my organization. We eliminated the cost of additional automation tool licenses and leveraged internally available virtual machines as pipeline runners, reducing cloud instances cost. Also, GHA’s ease of integrating Code Quality tools like SonarQube and CodeQL was beneficial for maintaining coding standards.

In today’s world, when organizations face budget challenges, such techniques can be impactful. We should think creatively about utilizing existing solutions around us and look for open source tools to deliver secure and cost-effective automation solutions.

*This article is part of The New Stack’s contributor network. Have insights on the latest challenges and innovations affecting developers? We’d love to hear from you. Become a contributor and share your expertise by filling out this form or emailing Matt Burns at mattburns@thenewstack.io.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)