# OpenAPI Initiative: New Standards and a Peek at the Roadmap
![Featued image for: OpenAPI Initiative: New Standards and a Peek at the Roadmap](https://cdn.thenewstack.io/media/2025/02/62ff094f-openapi-standards-2-1024x576.jpg)
OpenAPI is a standard way to describe your [API](https://thenewstack.io/api-management/) for both human and machine audiences. From an OpenAPI description, API producers can check their API for compliance, run automated testing tools for their API and publish instant documentation. API consumers can also use these files to power their own integrations.

While the OpenAPI standard itself isn’t new, recent months have seen some updates from the [OpenAPI Initiative](https://www.openapis.org/), including an update to the OpenAPI specification and the publication of two new standards.

The OpenAPI Overlay Specification, released in October, describes a series of edits to apply to an OpenAPI description, making it easier to repeat the same updates to a description. The almost-as-new OpenAPI Arazzo Specification, released in May, provides a mechanism for outlining a sequence of API calls and how a process involving multiple API operations is performed.

## OpenAPI Updates
As a patch release, the [3.1.1 version of the specification](https://spec.openapis.org/oas/v3.1.1.html), released in October, received only minor updates. But as the first updates since early 2021, those updates do show that the project is alive and well. Many of the changes were also included in an update to OpenAPI 3.0, which is now at version 3.0.4.

Most of the changes in these patch versions are [improvements to the wording in the specification document](https://github.com/OAI/OpenAPI-Specification/releases/tag/3.1.1), clarifying a lot of ambiguous clauses, and adding examples. Some sections were refactored into five new appendices, and a new introductory text was added.

Parts of the document were expanded and re-worded to address common issues or questions from the community and provide clearer guidance to both tooling and end-user communities. Some of the areas around document parsing, data types and serialization, in particular, have benefited from attention.

Alongside the changes to the specification itself, the published [JSON Schema representations](https://spec.openapis.org/#openapi-specification-schemas) also received some updates.

## A New Overlay Specification
The Overlay Specification has been in draft for some time, and had a formal release in October. An Overlay is a JSON or YAML document that describes a series of actions to perform on an OpenAPI document.

Some good use cases for an Overlay could be:

- Updating the description for an operation, parameter or tag to clarify and otherwise improve the wording before publishing documentation.
- Adding pagination parameters to all
`GET`
endpoints in an OpenAPI description. - Removing all the operations marked as
`deprecated`
, or matching some other criteria - Adding tool-specific extensions such as display names for a documentation tool or method and module names for an SDK generator.
An Overlay can target a specific OpenAPI description or be used against any/many OpenAPI descriptions. The following example Overlay adds a license to an OpenAPI description:

While “design-first” is considered best practice for API development, many projects use a “code-first” approach and create an OpenAPI description automatically from the code for the API application. Working this way makes it difficult to improve the OpenAPI description because it gets regenerated when the code changes. Overlays allow repeatable changes to be made to the regenerated OpenAPI.

Multiple API tools include production-ready support for working with Overlays. Try the CLI tools from [Speakeasy](https://www.speakeasy.com/docs/speakeasy-reference/cli/getting-started) or [Bump.sh](https://github.com/bump-sh/cli), or visit the [OpenAPI Overlays repository](https://github.com/OAI/Overlay-Specification/) for more options.

## New Arazzo Specification
As stated previously, the Arazzo specification was released last May, but this January saw a patch release (the most minor update) for the spec, to [version 1.0.1](https://spec.openapis.org/arazzo/latest.html). An Arazzo description is a JSON or YAML document detailing sequences of API calls, chaining them together into more complex workflows.

For our modern applications, where operations are more involved than making a single API call, Arazzo helps to connect the dots in order to draw the bigger picture.

An Arazzo document describes one or more workflows, each containing a series of steps. Each step is an API call and can refer to an existing OpenAPI document for the details of the call. Each step includes criteria for success; the next step is only executed if the criteria is met.

Representing the more complex flows is great for creating interactive documentation to walk users through the steps, generating SDKs that can perform multiple API calls as a single function, or testing realistic API workflows.

Tooling for Arazzo is in its early stages, but there are some great [examples in the Arazzo specification repository](https://github.com/OAI/Arazzo-Specification/tree/main/examples/1.0.0), which serve as a good starting point for anyone who wants to use the new format. Both [Spectral](https://meta.stoplight.io/docs/spectral/) and [Redocly CLI](https://redocly.com/docs/cli) have also added Arazzo support to their linting tools, which is a big boost to getting to know and use the format.

Most of the API tool providers have Arazzo on their roadmaps, with tools for documenting and testing API workflows, so this is a “one to watch” topic for 2025.

## What’s Next in OpenAPI?
OpenAPI is an active project with big plans. Next on the agenda for the main OpenAPI specification is a 3.2 release, expected over the coming months. Version 3.2 will include updates to security schemes, expanded tags functionality and other improvements.

Currently in the early planning stages is the OpenAPI 4.0 project, codenamed “Moonwalk.” That project will be one to watch.

OpenAPI specifications are open standards and the projects to develop them are also open and welcome to contributors and spectators alike. Check out the project website to find out about the repositories, open meetings and Slack community.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)