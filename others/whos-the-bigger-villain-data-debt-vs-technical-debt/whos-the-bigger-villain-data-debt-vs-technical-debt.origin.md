# Who’s the Bigger Villain? Data Debt vs. Technical Debt
![Featued image for: Who’s the Bigger Villain? Data Debt vs. Technical Debt](https://cdn.thenewstack.io/media/2024/12/7752d08e-haunted-960998_1280-1024x768.jpg)
[Stephen Dawson](https://unsplash.com/@dawson2406?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/turned-on-monitoring-screen-qwtCeJ5cLYs?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
Everyone in IT knows about [technical debt](https://thenewstack.io/use-these-ai-workflows-to-reduce-your-technical-debt/). Technical debt (also known as tech debt, code debt, or design debt) is a metaphor that describes the possible consequences of development teams prioritizing the delivery of a functionality or project, which later needs to be refactored or redone.

Technical debt can be intentional and should be reserved for cases when developers consciously adopt a design strategy that is not sustainable in the long run but yields a short-term benefit, such as shipping a release. Unintentional tech debt may result from a “quick-and-dirty” or a “move fast and break things” approach.

Martin Fowler’s [2009 article](https://docondev.com/blog/2009/10/martin-fowler-on-technical-debt) on the technical debt quadrant describes a second axis, making a pertinent distinction between prudent and reckless technical debt.

Data debt is a type of technical debt that refers to the accumulated cost of poor data management practices, such as incomplete, inaccurate, or unstandardized data, which hampers efficiency and decision-making over time.

More than a nuisance, data debt results in unreliable data and manual data management. Data debt undermines an organization’s ability to be data-driven by reducing data quality, slowing decision-making, increasing costs, and eroding trust in insights.

Although data debt and tech debt are closely connected, there is a key distinction between them: you can declare bankruptcy on tech debt and start over, but doing the same with data debt is rarely an option.

Reckless and unintentional data debt emerged from cheaper storage costs and a data-hoarding culture, where organizations amassed large volumes of data without establishing proper structures or ensuring shared context and meaning. It was further fueled by resistance to a design-first approach, often dismissed as a potential bottleneck to speed. It may also have sneaked up through fragile multi-hop medallion architectures in data lakes, warehouses, and lakehouses.

Much like [coding without design leads to technical debt](https://thenewstack.io/how-to-use-self-healing-code-to-reduce-technical-debt/), this lack of strategic planning resulted in inconsistent, redundant, and siloed data, making integration, analysis, and value extraction increasingly complex.

## Shift Left in Data Management
With data debt, prevention is better than relying on a cure. Shift left is a practice that involves addressing critical processes earlier in the development lifecycle to identify and resolve issues before they grow into more significant problems. Applied to data management, shift left emphasizes prioritizing data modeling early, if possible — before data is collected or systems are built.

Data modeling allows for following a design-first approach, where data structure, meaning, and relationships are thoughtfully planned and discussed before collection. This approach reduces data debt by ensuring clarity, consistency, and [alignment across teams](https://thenewstack.io/entrepreneurship-for-engineers-why-team-alignment-matters/), enabling easier integration, analysis, and long-term value from the data.

By using data modeling at the outset, organizations can define the structure, meaning, and relationships of data in alignment with business needs. This proactive strategy reduces data debt by preventing the creation of inconsistent, redundant, or poorly understood data. It also ensures that technical teams and business users share a clear understanding of the data, leading to better data quality, easier integration, and long-term scalability. In essence, shift-left empowers teams to “design for the future” rather than fix problems after they occur.

Advocates of a code-first approach should recognize that data modeling is no longer a bottleneck when agile principles are applied alongside __domain-driven data modeling__.

However, every organization most likely already has some level of data debt. What is the plan to get it under control?

## Chart Your Existing Data
A data model, like a map or a blueprint, is a visual representation of how data is organized. By examining existing databases, data sources, and data exchanges, organizations can map out entities, attributes, and connections between them into an entity-relationship diagram or a more straightforward graph diagram.

This reverse engineering process involves analyzing and charting existing data structures to uncover their underlying design and relationships. It helps identify inconsistencies, redundancies, and gaps, enabling better understanding and documentation of the data for improved integration, analysis, and redesign if necessary.

By charting existing data, the process makes definitions, relationships, and structures explicit, bridging gaps between IT and business users. It enables business teams to align on how data reflects operations and processes. At the same time, IT departments gain clarity on how the data is used in decision-making, self-service analytics, machine learning, and artificial intelligence. This shared understanding fosters collaboration, reduces misinterpretations, and ensures that everyone — from technical teams to business stakeholders — works with consistent and meaningful data.

Metadata management tools and data dictionaries often rely on reverse engineering and profiling to harvest existing data structures, uncover relationships, and document attributes. While these processes provide valuable insights into the current state of data, they are inherently reactive, focusing on cataloging what already exists rather than designing data structures proactively. This limitation means they cannot prevent data debt from accumulating, as they cannot enforce proper design principles or align data with business needs from the outset.

## Design Your Future Data
Data modeling complements these tools by enabling a design-first approach, where data is thoughtfully structured with shared meaning, context, and [future scalability in mind](https://thenewstack.io/building-for-integrations-is-a-future-minded-growth-strategy/).

A data model is not an end goal. Its purposes include, on the technical side, establishing schema contracts that align with the business requirements of subject-matter experts and are mutually agreed upon by both data producers and consumers. On the business side, it facilitates easy sharing and access to the meaning and context of the data being exchanged and stored.

Data modeling prevents new data debt by creating a solid foundation and facilitating the evolution of existing structures. By guiding changes to align with technical and business requirements, data modeling helps organizations create a more sustainable and efficient future for their data, reducing the burden of past mistakes while ensuring ongoing value.

## Data Model Also Applied to Data Exchanges
Data modeling has traditionally been associated with relational databases for transactional or analytical purposes. Over time, this expanded with the rise of NoSQL databases, APIs, event-driven architectures, and microservices.

While developers initially focused on the underlying technologies, it has become clear that the key to successful data exchanges lies in the structure of the payload. Data publishers and consumers must agree on a data contract with the schema at its core for effective communication. This schema defines the structure of the exchange, whether it’s an API or a Kafka event.

## Conclusion
To reduce your data debt, chart your existing data into a transparent, comprehensive data model that maps your current data structures. This can be approached iteratively, addressing needs as they arise — avoid trying to tackle everything at once.

Engage domain experts and data stakeholders in meaningful discussions to align on the data’s context, significance, and usage.

From there, iteratively evolve these models — both for data at rest and data in motion—so they accurately reflect and serve the needs of your organization and customers.

Doing so creates a strong foundation for data consistency, clarity, and scalability, unlocking the data’s full potential and enabling more thoughtful decision-making and future innovation.

*This article is part of The New Stack’s contributor network. Have insights on the latest challenges and innovations affecting developers? We’d love to hear from you. Become a contributor and share your expertise by filling out this form or emailing Matt Burns at mattburns@thenewstack.io.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)