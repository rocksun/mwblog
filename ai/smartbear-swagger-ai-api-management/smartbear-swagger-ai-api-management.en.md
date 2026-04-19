Last week, [SmartBear](https://smartbear.com/) announced new capabilities for its commercial [Swagger](https://swagger.io/about/) toolset designed to help organizations govern, validate, and scale APIs as AI coding tools accelerate software development.

The updates center on two additions: A revamped Swagger Catalog that gives platform teams centralized visibility into API portfolios, and contract testing with drift detection that continuously verifies API behavior matches [OpenAPI](https://thenewstack.io/openapi-how-to-handle-file-management/) specifications.

Swagger enables design, governance, and testing across the full AI-enabled API lifecycle, ensuring quality at every step, SmartBear says. It enables users to build APIs ready for humans, LLMs, agents, and continuous innovation.

## AI is writing code faster than specs can follow

The company is pitching both new additions under the banner of “application integrity” — a term SmartBear chief product and technology officer [Vineeta Puranik](https://www.linkedin.com/in/vineeta-puranik/) defines as continuous, measurable assurance that software works as intended with governance to operate at AI speed and scale.

The problem Puranik is trying to solve is that tools like [GitHub Copilot](https://thenewstack.io/github-copilot-wants-to-become-your-peer-programmer/) and [Claude](https://thenewstack.io/claudes-free-plan-can-now-remember-you/) can generate or modify thousands of lines of code in minutes, but the specifications those APIs are supposed to conform to don’t update themselves. The result is what SmartBear calls drift — a divergence between what an API contract says and what the code actually does.

“Platform leaders struggle with fragmented discovery and a lack of lifecycle visibility, and engineering and [QA teams](https://thenewstack.io/is-genai-replacing-your-qa-team-a-sobering-reality-check/) face silent spec-to-runtime divergence,” Puranik tells *The New Stack*.

## Shift left, or pay later

The SmartBear drift detection feature runs in [CI/CD](https://thenewstack.io/a-brief-devops-history-the-road-to-ci-cd/) pipelines, catching divergence before code reaches production. That’s a distinction from what [API gateways](https://thenewstack.io/ai-gateways-vs-api-gateways-whats-the-difference/) like [Kong](https://thenewstack.io/kong-new-ai-infused-features-for-api-management-dev-tools/) or [Apigee](https://cloud.google.com/apigee) provide — those tools observe traffic in production, meaning an error has already escaped. SmartBear’s pitch is [shift-left](https://thenewstack.io/shifting-left-is-now-mainstream-for-developers-or-is-it/): Find the drift in the build cycle, not after deployment, Puranik says.

The Swagger Catalog addresses the visibility side of the problem, she says. As AI tools generate and modify APIs at scale, platform teams lose track of what exists, what’s compliant, and what’s production-ready. The catalog provides lifecycle tracking and governance enforcement across an organization’s full API portfolio — including APIs ingested from code repositories, [CI/CD pipelines](https://thenewstack.io/how-to-build-scalable-and-reliable-ci-cd-pipelines-with-kubernetes/), and imported specifications from tools like Postman.

## One place to see everything

Jason Burch, a senior lead solution architect at an automotive company that beta tested the features, said the catalog’s value is as much organizational as it is technical.

“When you surface hundreds of internal APIs in one place, it creates visibility across product, development, and architecture teams — and it elevates governance in a way that just isn’t possible with our current workflow,” he said in a statement.

The announcement also includes several additional Swagger platform updates arriving this quarter. They include a new editor with AI-powered API generation, context-aware documentation, Spectral-based governance enforcement, [MCP server](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) support for natural-language API automation, and expanded protocol support for OpenAPI 3.1, AsyncAPI 3.0, and [GraphQL](https://thenewstack.io/why-every-api-strategy-needs-graphql/).

## APIs as agent infrastructure

The MCP server supports matters for a specific reason. Agent-to-agent communication runs over APIs, which means machine-readable, current specifications aren’t a best practice anymore — they’re a hard dependency, Puranik says.

Drift doesn’t just break a test in that environment. It breaks the integration. Puranik put it plainly: “What are agents talking to each other with? It’s APIs.”

Beyond the catalog and drift detection, SmartBear is also positioning a new AI-native testing product called [BearQ](https://smartbear.com/product/bearq/) as part of the same application integrity story. The tool starts with a URL, autonomously explores application functionality, generates test cases, runs them, and flags failures — all without requiring scripting knowledge from the tester.

“You can tell it to go look at this functionality and it will know what you meant,” Puranik said. “You don’t need to tell it any scripting language.” [Agentic workflows](https://thenewstack.io/what-agentic-workflows-mean-to-microservices-developers/) for bulk [API testing](https://thenewstack.io/reining-in-the-api-wild-west-5-api-testing-best-practices/) — pointing the tool at an entire repository — are targeted for Q2, she said.

## A platform play, not a point solution

SmartBear’s Swagger tooling is used by more than 16 million developers across 32,000 organizations, including Samsung, Ford, and Marriott. A Forrester Consulting Total Economic Impact study commissioned by the company found the platform delivered 227% ROI over three years for a composite enterprise with 200 developers.

Meanwhile, at the end of last month, SmartBear announced its [SmartBear Application Integrity Core](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fsmartbear.com%2Fapplication-integrity%2F&esheet=54472517&newsitemid=20260331994897&lan=en-US&anchor=SmartBear+Application+Integrity+Core&index=2&md5=27b72faf4974b2ea7006e6b5d061be95). Like the two newly released features, these capabilities improve and accelerate application testing to keep pace with the increased speed and volume of AI-driven code creation.

The new capabilities add agentic and AI muscle to human-led testing workflows — including leveraging AI for on-premises applications. They also follow SmartBear’s recent release of BearQ, which rounds out its portfolio of AI-infused application testing products.

Enhancements include:

* New agentic capability in the SmartBear test automation platform, [Reflect](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Freflect.run%2F&esheet=54472517&newsitemid=20260331994897&lan=en-US&anchor=Reflect&index=6&md5=a0eb90335f9bbd23ca1b48470c86660d), that lets developers and QA engineers generate automated tests directly from their coding environment. By invoking Reflect through the [SmartBear MCP server](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fdeveloper.smartbear.com%2Fsmartbear-mcp%2Fdocs%2Fmcp-server&esheet=54472517&newsitemid=20260331994897&lan=en-US&anchor=SmartBear+MCP+server&index=7&md5=85485a9877179628a6fc2e2cf7dbcbf6), teams can pull in richer context, drawing on existing test assets, unified visibility and reporting, and development history. This creates context-aware tests agentically and accelerates automation adoption without starting from scratch.
* New Rovo agent skills for [Zephyr](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fsmartbear.com%2Ftest-management%2Fzephyr%2F&esheet=54472517&newsitemid=20260331994897&lan=en-US&anchor=Zephyr&index=8&md5=434ffb4010d0532e648caf2200c300c6) enable natural-language queries within Atlassian Jira to evaluate test coverage, search test executions, and assess release readiness, so QA teams can quickly identify gaps and prioritize testing work.
* AI capabilities to SmartBear’s on-prem tools for desktop testing and secure, local environments—including natural-language AI test generation in [ReadyAPI](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fsmartbear.com%2Fppc%2Fready-api%2Ftrial%2F%3Futm_source%3Dgoogle-paid%26utm_medium%3Dppcg%26utm_campaign%3DG%2B-%2BReadyAPI%2B-%2BNA%2B-%2BBR%26utm_term%3Dsmartbear%2520readyapi%26utm_content%3De%26gclsrc%3Daw.ds%26gad_source%3D1%26gad_campaignid%3D22677754068%26gbraid%3D0AAAAAD_lD115EYpIfhXyZNc_N-Pz-Nq_0%26gclid%3DCj0KCQjw7IjOBhDyARIsAFzrWQzLcmuWLqbP4glQIuJm4vyBIcrIOX9ySp2CjzAxHNMLi4MtRfgTWvMaArQ_EALw_wcB&esheet=54472517&newsitemid=20260331994897&lan=en-US&anchor=ReadyAPI&index=9&md5=57423f77eed27cbe2ca6aed96ec977b9) for building complex multi-step API tests, and enhanced AI-based object detection in [TestComplete](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fsmartbear.com%2Fproduct%2Ftestcomplete%2Ffree-trial%2F%3Futm_source%3Dgoogle-paid%26utm_medium%3Dppcg%26utm_campaign%3DG%2B-%2BTestComplete%2B-%2BNA%2B-%2BBR%26utm_term%3Dtestcomplete%26utm_content%3De%26gclsrc%3Daw.ds%26gad_source%3D1%26gad_campaignid%3D22668117066%26gbraid%3D0AAAAAD_lD111N9JQpjkNohRX33XpToCZf%26gclid%3DCj0KCQjw7IjOBhDyARIsAFzrWQzfnxV0KVtTVGXh13avFcDk4GA8LtuxDzFZiRNVXxLxpAx2AsB7l_kaAmdsEALw_wcB&esheet=54472517&newsitemid=20260331994897&lan=en-US&anchor=TestComplete&index=10&md5=932cbdd2564532cffa33dba0ab32ed89). This will improve automation reliability for rapidly changing applications, all with enterprise governance controls to meet compliance and quality standards.

“SmartBear is firing on all cylinders to enable QA teams to move faster and improve application-level testing. We see some teams racing toward fully autonomous solutions like BearQ, and others deploying AI-enabled tools to complement human-directed automation or even manual workflows,” Puranik said in a statement. “We meet customers where they are on their AI journeys by helping teams adopt AI confidently, scale testing effectively, and maintain application integrity as software delivery accelerates.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)