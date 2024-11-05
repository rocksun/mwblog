# DevOps Moves Beyond Automation to Tackle New Challenges
![Featued image for: DevOps Moves Beyond Automation to Tackle New Challenges](https://cdn.thenewstack.io/media/2024/11/24340e25-quino-al-uwu5qhetnvc-unsplash-1-1024x683.jpg)
NEW YORK — Speakers and exhibitors at the recent [DevOpsCon New York](https://devopscon.io/new-york/) conference here made it clear that [DevOps](https://thenewstack.io/devops/) is moving on to new challenges, most of which build on the DevOps foundation.

New challenges include [DevSecOps](https://thenewstack.io/decoding-devsecops-striking-the-right-balance/), improving resilience and safety procedures, reducing the time to resolve an incident, introducing [AI assistants](https://thenewstack.io/augment-ai-code-assistant-targets-large-development-teams/), and realigning organizational roles and responsibilities to better implement the DevOps methodology.

By most accounts, DevOps began [about fifteen years ago](https://devops.com/the-origins-of-devops-whats-in-a-name/) as a way to reduce friction between development and operations teams and speed up software deployment.

Many organizations found DevOps to be a culture change as well as a technology change, since it alters the demarcation line between operations and development staff. Many of the new directions for DevOps would also impact IT culture.

The conference keynotes described architectural considerations of [Kubernetes](https://thenewstack.io/kubernetes/), AI expertise strategies for developer productivity, next-level observability, improving resilience, and building organizational trust.

Vendors in the exhibitors’ area extolled the virtues of doing DevOps the right way, stepping up automated testing and remediation, deploying better observability, and improving [CI/CD](https://thenewstack.io/ci-cd/) pipeline technology.

## It’s Not a One-Way Street
When DevOps started about 15 years ago, “people were looking at it as a one-way street.”

[Steve Barreto](https://www.linkedin.com/in/stevebarreto/), senior solutions architect at exhibitor [Keysight](https://www.keysight.com/us/en/products/software/software-testing.html) told The New Stack.
“But it’s not — it’s a circle of life,” he said, in which products such as Keysight’s [Eggplant](https://www.keysight.com/us/en/products/software/software-testing/eggplant-test.html) continuously test application behavior and improve it. “What happens when a UI anomaly is discovered in pipeline testing?”

Eggplant’s Digital Automation Intelligence (DAI) capability increases the rate of integration with CI/CD pipelines, Barreto said. “DAI finds anomalies based on the behavior of past tests and automatically opens a ticket with notes.

“For example, if an anomaly occurs with a mobile app button that doesn’t work as expected, Eggplant DAI will attach a screen shot along with the error report to the ticket.”

After a developer corrects the anomaly and restarts the pipeline, the circle of the development life cycle starts again. Developers realize it isn’t enough to simply automate the deployment process — the next step is continuously deploying fixes.

## Improving Resilience By Design
In his keynote session, “The Practices of Resilience: Narrative, Common Ground, and Complexity,” [Jabe Bloom](https://www.linkedin.com/in/jabebloom/), principal at [Ergonautic](https://www.ergonautic.ly/), outlined an approach to improving resilience with DevOps taking into account risk in design and risk in use.

Risks in design are risks that you can anticipate during the planning process, whereas risks in use are unexpected incidents that occur in production, Bloom said.

First, eliminate as many risks in design as possible, then focus on the process for handling risks in use. In particular, pay attention to the cognitive load on the humans involved in responding to systems that are strained or failing.

While you cannot completely eliminate risk, Bloom said, you want to design the system so it can recover quickly. Importantly, resilience in recovering quickly from unexpected events comes only from human interaction.

Technology, such as a CI/CD pipeline, influences the scope of human action within a system, he said and should be oriented to reduce cognitive load on the humans involved.

## Improving the Pipeline
“One of the biggest challenges developers have is safely introducing change and empowering development teams to make the change with confidence,” CircleCI Vice President of Product Management [Aakar Shroff](https://www.linkedin.com/in/aakarshroff/) told The New Stack.

“When CircleCI started out over a decade ago, developers were just getting comfortable with the idea of continuous testing and were just starting to implement CI/CD,” he said.

CircleCI ensures developers have visibility in the overall system regarding their changes, where they are running, whether there’s an incident that requires a rollback, and so on, Shroff added.

“It’s not easy to mimic Production Work/User Workloads in other environments,” he said. “Analysis runs can help — run two versions of the application and compare results. It’s always a trade-off between speed and safety, but rollouts happen faster when you remove fear of a change that causes an incident.”

In particular, “CircleCI includes in its visibility scope aspects external to the code repository. For example, when a third-party library or an API you’re relying on changes, we will automatically validate the change in relation to your application,” Shroff said, “ultimately, this provides teams with more confidence to speed up and allows them to deliver value to their customers.”

CircleCI recommends developers use progressive rollouts to help shift traffic safely to a new code version during an update. When integrated with an app such as Argo rollouts, developers can validate key pipeline metrics to either confirm a deployment or trigger a rollback.

“To improve the developer experience,” Shroff said, “we ensure constant pipeline optimization based on constant feedback to developers to highlight deviations from standard practice.”

In this regard, pipeline standardization can be seen as among the next challenges for DevOps as well.

## Improving the Organization
[John Willis](https://www.linkedin.com/in/johnwillisatlanta/), founder of Botchagalupe Technologies, author of three DevOps books, a frequent contributor of DevOps articles and popular DevOps conference speaker, focused his session on organizational transformation.
His keynote, “Beyond Checkboxes: Embedding True Cyber Resilience,” presented an organizational blueprint for incorporating security intrinsically into business capabilities.

He spoke about “Debt and Resilience” and described how GenAI can help identify issues and potential resolutions.

Willis’s talk incorporates [W. Edwards Deming](https://en.wikipedia.org/wiki/W._Edwards_Deming)’s [system of profound knowledge](https://deming.org/explore/sopk/), which he cites as a methodology for organizational transformation. Willis, who has also written a [book about Deming](https://www.amazon.com/Journey-Profound-Knowledge-Altered-Industry/dp/1950508838), said he sees Deming’s system as something that influences how we work today and how we will work in the future.

“We are people who run DevOps and infrastructure and are not always aware of risks created by technical debt,” Willis said, including the risks of [shadow IT](https://thenewstack.io/how-to-bring-shadow-kubernetes-it-into-the-light/) and [shadow AI](https://cloud.google.com/transform/spotlighting-shadow-ai-how-to-protect-against-risky-ai-practices).

To eliminate such risks and accomplish transformation, Willis recommends breaking down institutional silos to better align business, IT, and cybersecurity roles and responsibilities to improve incident response.

To Willis, success with DevOps is as much about getting the organizational structure right and improving the quality of all systems to create true cyber resilience.

In that sense, successful DevOps transformation is not just about new systems or technologies, but also about changing mindsets and cultivating a culture that embraces continuous improvement.

## Is DevSecOps the Future?
“The future of DevOps is DevSecOps,” [Jonathan Singer](https://www.linkedin.com/in/jonathanayalsinger/), senior product marketing manager at [Checkmarx](https://checkmarx.com/), told The New Stack.

“Developers need to consider high-performing code as secure code. Everything is code now, and if it’s not secure, it can’t be high-performing,” he added.

Checkmarx is an application security vendor that allows enterprises to secure their applications from the first line of code to deployment in the cloud, Singer said.

The DevOps perspective has to be the same as the application security perspective, he noted. Some people think of seeing the environment around the app, but Checkmarx thinks of seeing the code in the application and making sure it’s safe and secure when it’s deployed, he added.

“It might look like the security teams are giving more responsibility to the dev teams, and therefore you need security people in the dev team,” Singer said

Checkmarx is automating the heavy mental lifting by prioritizing and triaging scan results. With the amount of code, especially for large organizations, finding ten thousand vulnerabilities is fairly common, but they will have different levels of severity.

If a vulnerability is not exploitable, you can knock it out of the results list. “Now we’re in the noise reduction game,” he said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)