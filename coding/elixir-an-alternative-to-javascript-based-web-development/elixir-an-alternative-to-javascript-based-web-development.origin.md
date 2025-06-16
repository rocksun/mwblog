# Elixir: An Alternative to JavaScript-Based Web Development
![Featued image for: Elixir: An Alternative to JavaScript-Based Web Development](https://cdn.thenewstack.io/media/2025/06/24ea64d5-elixir-1024x581.jpg)
It may sound like heresy, but some developers regret their commitment to JavaScript. [Brian Cardarella](https://www.linkedin.com/in/briancardarella/), the founder of web and mobile development firm [DockYard](https://dockyard.com/), is one such developer.

“I’ve been in software development for over 30 years [and] I’ve seen this multiple times, where your technology decision will impact your productivity at the end of the day, especially as the application’s complexity grows in scale,” Cardarella told The New Stack. “In JavaScript, just the nature of it is such that it is very difficult to scale properly.”

That’s despite the community’s efforts, he added.

“The JavaScript community has done heroic work to try to work around JavaScript limitations, and it’s really impressive how that ecosystem has evolved and grown over the past 10 years,” he said. “But the underlying problem is really that the way that JavaScript manages memory and what it’s doing in terms of how you build applications — [it] is really going to scale out of control.”

Cardarella has seen businesses complain about development taking weeks or months to implement features that used to take a day or two, due to scaling issues. Meanwhile, he added, delivery goes down while the costs go up.

Cardarella solved his own JavaScript problems by switching to Elixir and the Elixir-based web development framework [Phoenix](https://github.com/phoenixframework/phoenix), which is open source.

DockYard is the largest Elixir consultancy, according to Cardarella. Its client list includes [Netflix](https://thenewstack.io/netflix-engineers-rethink-mock-testing-for-graphql/), the NASDAQ and [Adobe](https://thenewstack.io/adobe-developers-use-webassembly-to-improve-users-lives/). Phoenix was created by [Chris McCord](https://www.linkedin.com/in/chris-mccord-98b47a37/) right before he started working for DockYard. He spent six years with DockYard’s support developing the framework and a frontend framework called Phoenix LiveView.

## Elixir: A Functional Language
[JavaScript](https://thenewstack.io/javascript-framework-reality-check-whats-actually-working/) is a multi-paradigm programming model, meaning it supports multiple programming styles — including object-oriented, functional, and event-driven programming.
Elixir, by contrast, is a functional programming language. It changes functions, instead of data. Rather than altering the data, a functional program just adds more data. That was more of a challenge when compute was more expensive.

“Historically, functional programming has been less performant,” Cardarella said. That’s because it does memory copying or memory allocation, where new memory is created in functional programming.

“It says any values being passed in have to be copied, and then you’re working on a copy of that original value,” he said. “So there’s a cost for copying and in slower computing days, this cost was very, very obvious because the programs will run slower, require more memory, because you have duplication of certain values.”

“Elixir has so much data out there showing that it requires less people, has less costs, makes the really, really hard things in computer science easy to accomplish, but it doesn’t have the backing of a big company.”

– Brian Cardarella, founder of DockYard
It also handles [garbage collection differently](https://www.cloudbees.com/blog/comparing-elixir-go) than JavaScript. Instead of a single, global garbage collector that might pause the entire application, each Elixir process has its own isolated heap and garbage collector. This means a long-running process doesn’t hog memory indefinitely without collection.

The result is a cleaner program with fewer side effects, he said. That means the developers can move faster and fix problems significantly faster, at a lower cost.

“Elixir has so much data out there showing that it requires less people, has less costs, makes the really, really hard things in computer science easy to accomplish, but it doesn’t have the backing of a big company,” he said. He pointed to a [case study of the Bleacher Report](https://www.erlang-solutions.com/case-studies/bleacher-report-case-study/).

The Bleacher Report, a division of Turner Sports, is the second-largest sports website in the world. It consulted with [Erlang Solution](https://www.erlang-solutions.com/) to move off [Rails](https://thenewstack.io/dhh-wants-to-make-web-dev-easy-again-with-ruby-on-rails/) and onto Phoenix.

“They were able to basically cut their team down to 10% of what it previously was, because they didn’t need that many people anymore,” Cardarello said.

They also went from 150 production servers down to only eight, according to the case study, and saw the following gains:

- The ability to handle eight times the traffic without autoscaling;
- 95th percentile latency hovered around 100ms and was not noticeably affected by traffic spikes due to breaking news or other events;
- The time to add content to all streams went from 30-40 seconds to 3-4 seconds;
- Resource-intensive features, previously requiring aggressive horizontal scaling, ran on about 1/10th of the servers with low CPU utilisation.
Warner Media later moved Bleacher Report off Elixir, which Cardarella (and [this Reddit commenter](https://www.reddit.com/r/erlang/comments/18f3kl3/bleacher_report_gutting_out_otp/)) attributed to corporate politics.

Still, Elixir can be frustrating for those accustomed to JavaScript, Cardella said. For one, the syntax is significantly different. By contrast, Rust has been able to pull in many from the JavaScript community because there are facets of its syntax that feel familiar to JavaScript developers, he added.

## Elixir Development Tools
In addition to the Phoenix framework for web development, McCord created [Phoenix LiveView](https://dockyard.com/blog/2018/12/12/phoenix-liveview-interactive-real-time-apps-no-need-to-write-javascript), which was released in [version 1.0 in December](https://dockyard.com/blog/2024/12/03/phoenix-liveview-goes-1-0). Phoenix LiveView leverages server-rendered HTML and Phoenix’s native [WebSocket](https://thenewstack.io/the-challenge-of-scaling-websockets/) tooling to build real-time features.

Cardarella admitted in a blog post that, at first, he had a hard time seeing the value of LiveView.

“Around that time I had, internally, announced DockYard’s intention to distance ourselves from the Ember.js project,” he wrote. At the time, they were using Phoenix on the backend, but his announcement caused some concern within the company about it’s frontend specialization.”

“I saw the order of magnitude in developer productivity benefit that came from writing Elixir compared to any other language I’ve used in my career,” he said. “So I was looking for that replacement when Chris was building it right before my very eyes. Unfortunately, it was too close to my face and I’m too old to read something so close, so I spent a ton of money trying to compile Elixir to WebAssembly.”

What sold him on LiveView was how easy it made several key issues compared to JavaScript-based [frontend development](https://thenewstack.io/introduction-to-frontend-development), he continued, including:

- Managing application state;
- Complexity with server-side rendering and application start time;
- No complex compilation pipeline; and
- Ecosystem stability. (“Admittedly, the JS ecosystem is somewhat less volatile than it was back in 2018,” he added.)
There’s also [LiveView Native](https://github.com/liveview-native/live_view_native), a cross-platform open source framework for building native applications using the same code base as Phoenix LiveView. It allows developers to create native UIs with a single set of Elixir code, streamlining the development process and enabling faster release cycles.

If you’re interested, Elixirland has published a list of [tools in the Elixir ecosystem](https://elixirland.dev/ecosystem).

## The Politics of Web Development
Elixir is one of the great untold stories in technology, claims Cardarello. He says it’s overlooked because of political reasons, marketing reasons, financial backing or simply because people want to copy large companies.

“Generally, you think that software developers make the best technology decisions in what they’re doing, and that’s rarely the case,” he said. “Instead, what we tend to see is that the languages and the frameworks that end up being popular are popular for reasons that have nothing to do with their capabilities, … whereas something like Elixir is solving all these problems and allowing for orders of magnitude of productivity increase, but it hasn’t seen mass adoption yet.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)