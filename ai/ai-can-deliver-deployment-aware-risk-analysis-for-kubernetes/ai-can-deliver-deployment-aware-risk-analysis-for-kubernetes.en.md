For Kubernetes platform engineers or DevSecOps leads, the experience is all too familiar: You open your security dashboard and are greeted by a list of 10,000 deployments, all flagged with critical vulnerabilities, configuration issues and suspicious activities. The sheer volume of alerts creates a paradox: When everything is a priority, nothing is.

Traditional risk scoring solutions evaluate the risk indicators detected by scanners in isolation, relying on predefined heuristics and static vulnerability scores. These solutions prioritize risks largely based on these static labels, but do not consider whether these risks are truly [applicable to the specific deployment environment](https://thenewstack.io/distributed-applications-need-a-consistent-security-posture/) or whether they pose an actual exploitation path.

Addressing this lack of context is an area of focus for [Red Hat](https://www.openshift.com/try?utm_content=inline+mention), in collaboration with IBM Research, as they develop future capabilities for Red Hat Advanced Cluster Security. By introducing an AI-driven Risk Investigation Agent, the teams are moving away from static scoring toward “deployment-aware” risk analysis.

## **The Problem: The Context Gap**

In many current [Kubernetes security practices](https://thenewstack.io/5-kubernetes-vulnerabilities-to-watch-out-for/), risk scores are often assigned based on static metadata rather than the actual behavior of the deployment in its live environment. Determining true [risk requires understanding whether the vulnerable library](https://thenewstack.io/we-need-to-rethink-risk-in-vulnerability-management/) is loaded at runtime, whether the affected port is exposed or whether the workload is even active.

Configuration weaknesses may intensify the impact of certain vulnerabilities, and multiple common vulnerabilities and exposures (CVEs) within the same deployment may interact to form chained exploitation paths. One vulnerability may enable or support the exploitation of another, creating an exploit chain.

Moreover, behavioral indicators such as anomalous processes, unusual network activity or unauthorized access attempts may signal an ongoing exploitation attempt. These signals must be correlated with vulnerability data and deployment context to produce accurate and meaningful risk assessments.

The goal of the new collaboration is to refine risk scoring based on real deployment context. To do this, the system addresses two critical gaps in traditional scanning:

* **Deployment-aware risk assessment:** Using AI to correlate findings detected by Red Hat Advanced Cluster Security to deliver deployment-aware risk assessments. This includes evaluating the applicability of each risk indicator to the actual deployment context, such as determining whether a CVE is truly exploitable within a specific workload. It also includes correlating multiple indicators to identify cases where they combine to create amplified or chained risks.
* **Context and explainability:** Using the capabilities of [large language models (LLMs)](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) to generate clear, natural language explanations that describe the specific factors influencing the risk score. This provides customers with transparency into how each assessment was derived, enables them to validate the quality of the AI-driven insights and helps them better understand the underlying risk.

## **The Solution: The Risk Investigation Agent**

The core of this new capability is the Risk Investigation Agent developed by IBM Research Labs for use with Red Hat Advanced Cluster Security.

This feature is designed as an add-on for users with the resources to power an [LLM-based](https://thenewstack.io/what-are-large-action-models/) agent. It functions through a sophisticated flow designed to provide more context-aware risk assessment:

* **Data aggregation:** The agent continuously ingests data from Red Hat Advanced Cluster Security services, including vulnerability scan results, runtime process monitoring, network activities, Kubernetes configuration metadata and access events. It also enriches this view using external sources such as CVE databases, Exploit DB intelligence, MITRE ATT&CK tactics and remediation guidelines.
* **Investigation agent (the “brain”):** This component serves as the reasoning layer. Its primary role is to determine whether each finding represents a true, exploitable risk within the live deployment. It evaluates network exposure, workload behavior, configuration posture and runtime evidence to assess whether the prerequisites for exploitation are actually present. This includes verifying if the vulnerable component is loaded, whether the service or port is exposed and whether the workload is active and reachable. Beyond individual findings, the agent also performs cross-correlation across signals. It identifies when configuration weaknesses amplify a vulnerability, when suspicious process execution or unusual network traffic suggests active exploitation or when multiple vulnerabilities combine to form a potential exploit chain.
* **LLM processing and risk explanation:** Once enriched and contextualized, the data is processed by an LLM to generate a refined generative AI (GenAI) risk score. More importantly, the LLM provides a natural-language explanation describing why the risk is significant, referencing specific deployment behaviors, potential exploit paths, chained vulnerabilities and observed indicators of compromise. This enables security teams to understand not just the risk level, but the reasoning behind it.

## **Under the Hood: How the AI ‘Thinks’**

To understand the value here, let’s look at a specific evaluation scenario.

Consider a Windows Server Update Services (WSUS)-like service running on a Kubernetes deployment. A standard scan might flag CVE-2025-59287, a remote code execution vulnerability targeting WSUS over TCP ports 8530 and 8531.

* **The false positive:** In one cluster, Red Hat Advanced Cluster Security detects that the vulnerable WSUS package exists in the image, but during runtime analysis, it confirms that TCP ports 8530 and 8531 are closed**,** with no network exposure. There is also no indication of any WSUS-related process activity. The LLM determines that although the library is present, the vulnerability is “not exploitable under current configuration” and marks the exploit suspicion as False, effectively deprioritizing it.
* **The true positive:** In another deployment, Red Hat Advanced Cluster Security observes that ports 8530 and 8531 are open and reachable. Runtime network monitoring detects internal port scanning attempts targeting these ports from another pod. The LLM identifies these not as generic system events, but as behavior strongly correlated with remote code execution probing. It flags this as “Highly relevant – suspicious” port scanning activity associated with CVE-2025-59287, marking it as “True.”

The system then generates a human-readable summary: “The risk is related to the exposed WSUS service running on unpatched containers with open TCP ports 8530/8531. Detected anomalous port scanning activity in the cluster increases the likelihood of exploitation and contributes to the overall risk score.”

## **Explainability: Interactive, Environment-Aware Insights**

While traditional AI explainability focuses on clarifying how a risk score is calculated, additional capabilities are being developed to take Red Hat Advanced Cluster Security a step further by making the system interactive and responsive to the deployment environment. The goal is that platform engineers and administrators will be able to query the AI about specific workloads or configurations and receive clear, contextual answers tailored to their environment.

This interactive explainability allows users to provide feedback directly to the model. For example, if a deployment is flagged as high risk but the user knows it is a temporary sandbox, they can annotate that context. The system then incorporates this feedback, continuously adapting and refining its understanding of the enterprise environment. The result is a “white box” AI that not only explains its reasoning but learns from the environment and user input, enabling more accurate, actionable and trustable guidance.

## **The Road Ahead: From Analysis to Remediation**

IBM and Red Hat are exploring capabilities that enable the AI to proactively propose remediation actions tailored to the specific deployment context. Future iterations aim to generate remediation options that users can apply directly to mitigate identified risks. These include risk-aware patching strategies aligned with the environment’s operational constraints, mitigation steps for vulnerabilities that cannot be patched immediately and configuration changes to reduce exposure and harden the deployment.

The integration of GenAI into Red Hat Advanced Cluster Security represents a maturity milestone for Kubernetes security. We are moving past the era of simple pattern matching and into an era of contextual understanding.

By combining IBM’s research in correlation analysis with Red Hat’s platform capabilities, Red Hat Advanced Cluster Security is attempting to solve the signal-to-noise ratio problem that plagues modern SecOps. For the IT manager, this means less time chasing false positives. For the Kubernetes user, it means a clearer understanding of what is actually running in their clusters.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/12/969bf435-cropped-0471b7de-yair-allouche-600x600.png)

Yair Allouche is the head of the IBM Beer Sheva Research Lab in Israel, which focuses on applying generative AI to real-world cybersecurity challenges and on securing GenAI itself. With a strong background in cybersecurity and over a decade at...

Read more from Yair Allouche](https://thenewstack.io/author/yair-allouche/)

[![](https://thenewstack.io/wp-content/uploads/2025/12/2c9f18cb-cropped-4f4a5cb8-screenshot-2025-12-03-at-9.04.43%E2%80%AFam-600x600.png)

Sabina Aledort is a product manager for Red Hat Advanced Cluster Security. Sabina has spent the past five years gaining diverse experience across several teams at Red Hat. She began as a software developer within the Networking team for the...

Read more from Sabina Aledort](https://thenewstack.io/author/sabina-aledort/)