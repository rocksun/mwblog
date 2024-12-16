[Policy as Code](https://www.permit.io/blog/what-is-policy-as-code) has revolutionized how organizations manage access control, compliance, and governance. By codifying policies, teams can ensure consistent enforcement, automate processes, and adapt to evolving requirements with agility. Yet, despite its undeniable advantages, implementing Policy as Code often feels like an uphill battle.
This is especially true when faced with the complexities of the Rego policy language, which, while extremely powerful, highlights the challenges of making Policy as Code accessible to a broader audience.

Everyone loves Policy as Code, but no one wants to write Rego.

Why does this happen? To answer, let’s first explore why Policy as Code and its sister alternative, Policy as Graph, have become indispensable before addressing the barriers to their adoption.

**Policy as Code: The Foundation of Modern Governance**
At its core, Policy as Code enables teams to codify rules governing who can access what, under what conditions, and why. In software development, everyone involved—developers, security teams, compliance officers, and product managers—needs to connect people and systems to what was built. Policy as Code provides a framework to achieve this reliably and transparently through some key benefits:

**Consistency**: Policies written as code are uniformly applied across environments, reducing errors and discrepancies.**Transparency and Auditability**: Policies stored in code repositories can be easily reviewed, tested, and audited, making compliance demonstrable.**Automation**: Integrating policies into CI/CD pipelines ensures they are tested and enforced automatically, preventing policy drift.**Version Control**: Policies evolve alongside the systems they govern, with every change tracked and reversible via tools like Git.
Despite these advantages, the path to implementation is far from easy, particularly when crafting complex policies.

**Rego as a Case Study: Challenges of Policy Writing**
Rego, the policy language of [Open Policy Agent (OPA)](https://www.permit.io/blog/introduction-to-opa), serves as a prime example of the hurdles organizations face when adopting Policy as Code.

OPA is very efficient and built for performance - It keeps the policy and data for which it needs to evaluate the rules in the cache, and supports having multiple instances as sidecars to every microservice, thus avoiding network latency.

It also supports [Role-Based Access Control (RBAC)](https://www.permit.io/blog/what-is-rbac), [Attribute-Based Access Control (ABAC)](https://www.permit.io/blog/what-is-abac), and [Relationship-Based Access Control](https://www.permit.io/blog/what-is-rebac) (ReBAC, With certain adjustments), enabling highly granular permissions management.

With its significant industry adoption, its backed by a thriving community, making it a reliable choice for building [fine-grained](https://www.permit.io/blog/what-is-fine-grained-authorization-fga) authorization policies.

Its language, Rego, Rego differs significantly from mainstream languages like Python, Java, or Go. Its roots in Prolog and Datalog give it a steep learning curve, especially for developers unfamiliar with logical programming paradigms.

In simple cases, Rego can feel quite declarative - Here’s a simple example of a Rego policy to illustrate access control:

```
package example.allow
default allow = false
allow {
input.user == "alice"
input.action == "read"
input.resource == "file1"
}
```
In this policy:

- The
`default allow = false`
line ensures that access is denied unless explicitly allowed. - The
`allow`
block specifies conditions where access is granted (e.g., if the user is "alice" and wants to "read" "file1").
While this example seems straightforward, real-world policies often involve recursion, nested logic, and integrations with external systems, which quickly escalate complexity. For instance, consider the following slightly more advanced example involving ReBAC and ABAC:

```
package access
default allow = false
# Define the relationships
relations = {
"user1": {"resources": {"resource1": ["owner"]}},
"user2": {"resources": {"resource1": ["viewer"], "resource2": ["manager"]}}
}
# Fetch the current time from an external service
current_time = time_response {
some resp
http.send({
"method": "GET",
"url": "<http://worldtimeapi.org/api/timezone/Etc/UTC>"
}, resp)
resp.status_code == 200
parsed_body := json.unmarshal(resp.body)
time_response := parsed_body.datetime # Example ISO 8601 time string: "2023-10-25T14:23:42+00:00"
} else = "1970-01-01T00:00:00+00:00" # Default fallback value if HTTP request fails
# Parse the hour from the fetched current time
current_hour = hour {
split(current_time, "T", parts)
split(parts[1], ":", time_parts)
hour := to_number(time_parts[0])
}
# ReBAC logic to check relationships using `walk`
allow_rebac(user, resource) {
walk(relations, [user, "resources", resource, role])
role == "owner" # Example: Only owners can access the resource
}
# ABAC logic to check time-based constraints
allow_time_based_access {
current_hour >= 9 # Access allowed from 9:00 AM
current_hour < 17 # Access disallowed after 5:00 PM
}
# Combined policy
allow {
input.user
input.resource
allow_rebac(input.user, input.resource)
allow_time_based_access
}
```
This example demonstrates how Rego can integrate multiple access control models but also underscores its complexity. Can we easily say this code is declarative? Even slightly pushing some logic shifts the balance towards the imperative. This challenge and tendency towards the imperative only worsen as policy grows.

[Styra’s Regal project](https://docs.styra.com/regal) can significantly lower the effort of writing policies in Rego with its extensive set of linter rules, documentation and editor integrations.
But the problem isn’t really limited to Rego itself - it also exists in other models, such as Policy-as-Graph.

**Policy-as-Graph: A Different Model**
As an alternative, some organizations have adopted policy-as-graph frameworks, like [Google’s Zanzibar](https://www.permit.io/blog/what-is-google-zanzibar), to simplify access control. These systems model policies as relationships between entities (e.g., users, roles, and resources) stored as graph nodes and edges.

For example:

```
document:123 {
writer: alice
reader: group:editors
}
group:editors {
member: bob
}
```
Graph-based approaches excel at representing hierarchical relationships and group memberships. However, they often struggle with advanced conditional logic, such as attribute-based or time-bound access control, which becomes cumbersome in this schema. While policy-as-graph improves some aspects of policy readability, it lacks the flexibility needed for more nuanced scenarios.

**Barriers to Policy as Code Adoption**
Both Rego and policy-as-graph systems highlight common challenges in adopting Policy as Code:

**Complexity**: Many Policy as Code languages are tailored for precision and flexibility but are difficult to write and maintain.**Limited Accessibility**: Non-technical stakeholders, such as compliance officers or product managers, often lack the tools or skills to contribute directly to policy definitions.**Steep Learning Curves**: Logical programming paradigms (e.g., Rego) and schema configurations (e.g., Zanzibar) require specialized knowledge, alienating even experienced developers.**Scalability**: As policies grow in size and sophistication, debugging, testing, and extending them become increasingly challenging.
So how can we help users bridge this gap and increase the adoption of these systems?

**Bridging the Gap with Higher-Level Interfaces**
To unlock the full potential of Policy as Code, organizations need tools and practices that lower these barriers:

**High-Level Abstractions**: Defining policies through roles, relationships, and attributes abstracts away the underlying code complexity.**Low-Code Interfaces**: Tools like[visual policy editors](https://www.permit.io/)or[Terraform providers](https://docs.permit.io/integrations/infra-as-code/terraform-provider)make policy management accessible to non-technical users.
*Permit.io**’s no-code policy editor UI generates Rego code for you.*
```
resource"permitio_resource" "document" {
key = "document"
name = "Document"
description = "A confidential document"
actions = {
"read" : {
"name" : "Read",
"description" : "Read a document",
},
"write" : {
"name" : "Write",
"description" : "Write a document",
}
}
}
```
```
resource"permitio_role" "reader" {
key = "reader"
name = "Reader"
description = "A role that allows reading documents"
permissions = [
"document:read"
]
extends = []
depends_on = [
permitio_resource.document # This is required to ensure that the resource is created before the role (for the permissions assignment)
]
}
```
*Creating Resources and Roles with **Permit.io**’s Terraform provider*
**Templates and Reusability**: Pre-built policy templates and modular designs reduce the effort of writing policies from scratch.
For these purposes, [ Permit.io](http://Permit.io) offers a platform that generates Policy as Code (in Rego or other languages) for users while allowing them to interact with high-level objects like roles and user sets. This abstraction enables security, compliance, and operations teams to participate without needing deep programming expertise.

**Conclusion**
Policy as Code is a powerful tool for modern governance, but its complexity often prevents it from achieving its full potential. Whether through logical programming languages like Rego or graph-based models like Zanzibar, the industry faces a common challenge: how to make policies both precise and accessible.

By adopting best practices—such as high-level abstractions, low-code interfaces, and reusable templates—organizations can democratize Policy as Code, enabling all stakeholders to contribute effectively. Tools like [Permit.io](https://www.permit.io/) exemplify these principles, but the broader industry must continue innovating to make policies as inclusive as the systems they govern.

Ultimately, everyone loves Policy as Code because it transforms governance. The key to success lies in ensuring that everyone—not just developers—can engage with and benefit from it.

Need help with creating Rego policies? Generating them with [Permit.io](http://Permit.io) is free - so be sure to check that out, and if you have any more questions about Rego, authorization or its implementation, you're more than welcome to ask them in our [ Slack community](https://io.permit.io/se-slack).

## Written by
### Or Weis
Co-Founder / CEO at Permit.io

## Related Tags
Like this Article?

[Star us on Github](https://github.com/permitio)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgithub.35b09e10.svg&w=48&q=75)
Disagree?

[Tell us why](https://io.permit.io/blog-slack)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fslack.cbb6ed5c.svg&w=48&q=75)
Want more?

[Join our Substack](https://io.permit.io/blogstack)![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fpen.e40711f5.svg&w=48&q=75)