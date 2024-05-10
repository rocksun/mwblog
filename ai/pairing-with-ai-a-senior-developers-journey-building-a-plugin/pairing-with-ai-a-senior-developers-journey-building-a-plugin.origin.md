# Pairing With AI: A Senior Developer’s Journey Building a Plugin
![Featued image for: Pairing With AI: A Senior Developer’s Journey Building a Plugin](https://cdn.thenewstack.io/media/2024/05/08083d58-getty-images-hot2zb6x-gk-unsplash-1024x683.jpg)
Although it’s always helpful to improve
[documentation for developers](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/), many (myself included) prefer to dive in and learn while doing. That’s the seventh and arguably most important of my [seven guiding principles](https://thenewstack.io/7-guiding-principles-for-working-with-llms/) for working with LLMs: Because you acquire knowledge in task-oriented teachable moments, learning isn’t prospective — it’s immediate and tangible.
When an experienced dev partners with an LLM, its machine intelligence supports and amplifies your human intelligence.
The benefits have been clear to me. Writing an
[ODBC plugin for Steampipe](https://thenewstack.io/how-llms-helped-me-build-an-odbc-plugin-for-steampipe/) in the LLM era felt much easier than the experience I’d had writing plugins without such assistance. But that’s admittedly a subjective assessment, so I was on the lookout for an opportunity to compare notes with another plugin developer when [James Ramirez](https://www.linkedin.com/in/ramirezj/) showed up in our community Slack to announce a new plugin for the [Kolide API](https://hub.steampipe.io/plugins/grendel-consulting/kolide). I invited him to tell me about his experience building it, and he graciously walked me through a long conversation with ChatGPT in which he familiarized himself with three buckets of technical knowledge that were all new to him: the Kolide API, the Go language, and the Steampipe plugin architecture.
As an additional challenge: although plugin developers usually find suitable Go SDKs for the APIs their plugins target, that wasn’t the case here. So it was necessary to create a Go wrapper for the Kolide API and then integrate that into the plugin.
## Testing ChatGPT’s Go Ability
James began with a few warmup exercises. First, to test ChatGPT’s Go ability, he provided a pair of Go functions he’d written to call the related APIs
*/devices/* and */devices/ID*, and asked for an idiomatic refactoring to isolate logic shared between them.
Next, he explored optional parameters to functions using simple variadic arguments versus the more complex
[functional options pattern](https://davidbacisin.com/writing/golang-options-pattern) and determined that the simple approach — using a slice of *Search* structs to encapsulate the field/operator/value style of Kolide’s [query parameters](https://www.kolide.com/docs/developers/api#search) — would suffice. He asked for a function to serialize that slice of *Search* structs to form a REST URL, then refined the version ChatGPT proposed to create a final [serializeSearches](https://github.com/grendel-consulting/steampipe-plugin-kolide/blob/92614f899c402b28e7bb95ccdabf50b43b1e8762/kolide/client/search.go#L24-L49) that adds support for mapping friendly names to parameters and uses a string builder.
AI handles the nitpicking and often provides committable suggestions.
Several of these refinements, including the use of a string builder, were suggested by an AI-powered bot,
[CodeRabbit](https://coderabbit.ai/), which provided useful code review. It’s the kind of feedback that helps you and your team focus on the big picture, he says, because it handles the nitpicking and often (though not always) provides committable suggestions. It also takes a wider view to [summarize pull requests](https://github.com/grendel-consulting/steampipe-plugin-kolide/pull/60) and assess whether a closed PR addresses the objectives stated in its linked issue.
## Mapping Operators
He went on to explore ways to map from Steampipe operators like
*QualOperatorEqual* to Kolide operators like *Equals*. Here too the approach suggested by ChatGPT turned out to be a throwaway, enroute to a clean and simple approach. But as James confirmed in our interview, since you’re going to be iterating on throwaway versions anyway, it’s helpful to be able to generate plausible iterations rather than coding them by hand much more tediously. Along the way, he was picking up basic Go idioms. **James:**
Is there a do-while loop in Go?
**ChatGPT**
No, but …
**James:**
Is there a ternary operator in Go?
**ChatGPT**
No, but …
**James:**
How do I append to a
*map[string]string*? **ChatGPT**
Like this …
## The Visitor Pattern Enhanced With Reflection
After digesting the basics and developing a Go client for the Kolide API, James was ready to tackle the real work of plugin development: defining tables that map from Go types returned from an API wrapper to the Steampipe schemas that govern SQL queries against those tables.
Like all plugin developers, he started with one table that could list a set of resources, then enhanced it with filtering and pagination. After adding a second table, it was time to consider how to abstract common patterns and behaviors. The final result was an elegant implementation of the visitor pattern. Here are the Steampipe
*List* functions that correspond to the tables [kolide_device](https://hub.steampipe.io/plugins/grendel-consulting/kolide/tables/kolide_device) and [kolide_issue](https://hub.steampipe.io/plugins/grendel-consulting/kolide/tables/kolide_issue).
And here is the common
*listAnything* function used by all the plugin’s tables.
With this setup, adding a new table to the plugin is almost entirely declarative: you need only define the schema, along with the
*KeyColumns* and associated operators that form the bridge between *where* (or *join*) clauses in SQL queries and API-level filters. Then you write a tiny *List* function that defines a visitor and passes it to the common *listAnything* function which encapsulates marshaling of query parameters, connecting to the API client, calling the API, unpacking the response into a collection, and iterating over the collection to stream items to Steampipe’s foreign data wrapper.
James used ChatGPT to jumpstart an idiomatic implementation of the visitor pattern in Go. This entailed learning how to define a type for the visitor function, and then declare a function to satisfy the type. Each table’s visitor encapsulates a call to the API client and returns an interface. It’s all fairly generic, but the visitor’s response was specific to the Go type of the wrapped API response, and that would have meant writing a distinct
*List* function for each table. How to avoid that? James asked: “The field references on the res variable need to be of variable type, specified on execution time. Could you suggest an approach?”
ChatGPT’s suggestion, which he adopted, was to use reflection so that a call to
*listAnything*, like *listAnything(ctx, d, h, “kolide_device.listDevices”, visitor, “Devices”)*, could pass a name (“Devices”) which enables *listAnything* to access fields of the response struct in a type-agnostic way, for example, the *Devices* field here.
|
1
2
3
4
|
type DeviceListResponse struct {
Devices []Device `json:"data"`
Pagination Pagination `json:"pagination"`
}
With that,
*listAnything* finally lived up to its name as a fully generic Steampipe *List* function. The solution uses reflection sparingly and retains Go’s strong type checking in both the API layer and the Steampipe layer.
## What Did LLM Assistance Really Mean?
It most certainly did
*not* mean that an LLM wrote a plugin that embodies sophisticated design patterns in response to a prompt like: “I need Steampipe plugin for the Kolide API, please create it.” What it has meant for me, and what it also meant for James, is something I find more interesting: “Let’s talk through the process of writing a plugin for the Kolide API.” It’s like talking to a rubber duck in order to think out loud about requirements and strategies. But an LLM is [a rubber duck that talks back](https://blog.jonudell.net/2023/05/24/when-the-rubber-duck-talks-back/). Sometimes the responses are directly applicable, sometimes not, but either way, they can often help you gain clarity.
As a senior software engineer with broad experience, James could have figured it out — but it would have taken much longer.
“The conversation required me to be quite particular about what I was asking,” James said. Although he was starting from scratch with Go, he brought a wealth of experience that enabled him to rapidly orient and figure out which were the right questions to ask. As a senior software engineer with broad experience, James could have figured all this out on his own. But it would have taken much longer, and he’d have spent a lot of up-front time reading articles and documentation instead of learning by doing. And that time might not have been available! As I’ve now heard from many others, the acceleration provided by LLMs often makes the difference between having an idea and being able to execute it.
James also mentioned an open source angle I hadn’t considered. Pre-LLM, he wouldn’t have done this work in a completely public way. “I’d have kept it private until I felt more confident,” he says, “but this was out there from the start, and I was happy to have it out there.” That made it possible to engage with the Turbot team sooner rather than later.
This isn’t a story of automation, but rather of augmentation. When an experienced developer like James Ramirez partners with an LLM, its machine intelligence supports and amplifies his human intelligence. Both work together — not just to write code, but more importantly, to think through architecture and design.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)