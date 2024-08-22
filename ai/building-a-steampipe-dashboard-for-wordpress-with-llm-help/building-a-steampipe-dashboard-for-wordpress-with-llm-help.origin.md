# Building a Steampipe Dashboard for WordPress, With LLM Help
![Featued image for: Building a Steampipe Dashboard for WordPress, With LLM Help](https://cdn.thenewstack.io/media/2024/08/5e54c3a6-francesco-ungaro-hqgfte2ri9s-unsplash-1024x683.jpg)
It had been a while since I [built a Steampipe plugin](https://thenewstack.io/how-llms-helped-me-build-an-odbc-plugin-for-steampipe/) using LLMs, which have since evolved, so I decided to team up with my assistants and tackle another item on my wishlist: a plugin to enable [SQL queries of the WordPress API](https://github.com/judell/steampipe-plugin-wordpress). Of course, a Steampipe plugin doesn’t really come to life until its foreign tables power a set Powerpipe dashboards. Here’s one of them, for a selected The New Stack author.

That’s the end result, but let’s unpack how I got there.

## Find the Supporting Go SDK
A Steampipe plugin usually begins, as this one did, with a hunt for a [Go](https://thenewstack.io/go-the-programming-language-of-the-cloud/) SDK that wraps the API of interest. If one doesn’t exist you’ll have to wrap the API yourself, which can be done directly in the plugin, but ideally happens in a standalone module — as seen in the case of the [hypothes.is](https://github.com/turbot/steampipe-plugin-hypothesis) plugin, for which I had to write the supporting [hypothesis-go](https://github.com/judell/hypothesis-go). In many cases, fortunately, there’s an existing Go SDK for the API you are targeting with your plugin.

This is the kind of configuration ceremony that I do infrequently, and thus poorly, but LLMs have seen this a million times and can quickly guide me to the happy path.

There can often be more than one of them, though, so the plugin writer’s first task is to figure out which Go SDK to use. A search of *pkg.go.dev* usually yields an obvious answer, and in this case it was [https://github.com/robbiet480/go-wordpress](https://github.com/robbiet480/go-wordpress), which though not recently active, is imported by more Go modules than any of the others.

But things can get a bit complicated. *robbiet480/go-wordpress* is a fork that’s 46 commits ahead of *o1egl/go-wordpress*, which in turn is 1 commit ahead of *sogko/go-wordpress*. As a user of *robbiet480/go-wordpress*, the plugin’s package will actually be importing *sogko/go-wordpress*, by way of some fancy redirection in its *go.mod*.

As I mentioned [last time](https://thenewstack.io/how-llms-guide-us-to-a-happy-path-for-configuration-and-coding/), this is the kind of configuration ceremony that I do infrequently, and thus poorly, but LLMs have seen this a million times and can quickly guide me to the happy path. The commented-out *replace* here, by the way, is another piece of the puzzle. At one point I needed to debug *go-wordpress*, and that’s how you can make your locally-built plugin use a local Go SDK with custom debug logic.

Even after arriving at the correct set of magic incantations, there were still some speed bumps. One of [my assistants](https://thenewstack.io/elevating-the-conversation-with-llm-assistants/) recommended using *go get* but my weak knowledge of the Go ecosystem suggested that *go mod tidy* should suffice. Then another assistant reminded me to use *go clean -modcache* and that did the trick. As usual I would have gotten there eventually, but life’s too short to waste time shaving yaks, so I’m grateful for assistance that cuts down on the time I waste doing that.

## Implement the First Table
With the SDK in hand, my starting point for a new plugin is [github.com/judell/steampipe-plugin-hello](https://github.com/judell/steampipe-plugin-hello), which provides a trio of tables that don’t call any APIs. Why? It’s a working skeleton that I can copy, build, use, and then keep using as I add the tables I really want. As I proceed, the new plugin — initially modified with a search-and-replace of *hello* for *wordpress* — mostly keeps working; or, when it breaks, can easily be brought back to a working state.

Within my team of assistants there are two squads, one with only world knowledge (ChatGPT, Claude) and another with a combination of world knowledge and local knowledge (Cody, Copilot, Unblocked).

So, which assistant to tap first? It’s an embarrassment of riches lately: ChatGPT, Claude, [Cody](https://sourcegraph.com/cody), GitHub Copilot, and [Unblocked](https://getunblocked.com) are all ready to help. In this case, somewhat arbitrarily, I showed Claude one of the *hello* tables and asked for a new *wordpress_post* table. The result, as is typical, was a decent jumpstart.

Things that it got right:

- The structure of the core table function, with (mostly) correct mappings from the Go SDK’s
*wordpress.Post*type to corresponding Steampipe database types. - Use of a call to the Go SDK’s
*Posts.List*along with the companion*wordpress.PostListOptions*. - Use of
*wordpress.BasicAuthTransport*to authenticate to the WordPress API.
Things that it missed:

- Pagination to handle queries returning more than 100 results.
- The
*Transform*needed to turn an API-flavored date into a database-flavored date. - Use of
*KeyColumns*to enable SQL qualifiers like*where date > date(‘2024-08-01’).*
Had I started with Unblocked, I would have gotten a more Steampipe-idiomatic result. After the fact, I asked it for an initial version of the same table and it did include a declaration of *KeyColumns* along with an appropriate use of them to enable Steampipe to “push down” SQL qualifiers into the WordPress API.

Within my team of assistants, there are two squads, one with only world knowledge (ChatGPT, Claude) and another with a combination of world knowledge and local knowledge (Cody, Copilot, Unblocked). In theory, the latter would always give better results, but in practice I find myself recruiting assistance from both squads in order to get things done.

In this case, I kept iterating mostly with Claude while weaving in pieces from other assistants and pieces from my own prior experience. On one turn of the crank — and without being asked! — Claude added pagination to the plugin’s *listPosts* function. For other refinements, including proper handling of the *wordpress.spc* configuration file and an appropriate *Transform* for the date column, I drew mainly on my own experience. Once I’d hammered everything into good shape, it was time to move on to the next table: *wordpress_author*.

## Implement the Second Table
With the first table as a template, the next one naturally went much faster. The main point of interest here was pagination. The *wordpress_author* table’s pagination logic was copied from the *wordpress_post* table. That needed refactoring, a topic I’ve touched on before. In [When the rubber duck talks back](https://blog.jonudell.net/2023/05/24/when-the-rubber-duck-talks-back/) I wrote about using ChatGPT and Cody to work through a similar refactoring for the [Mastodon plugin](https://hub.steampipe.io/plugins/turbot/mastodon). And in [Pairing With AI: A Senior Developer’s Journey Building a Plugin](https://thenewstack.io/pairing-with-ai-a-senior-developers-journey-building-a-plugin/) we saw how James Ramirez arrived at an elegant reflection-based technique for his [Kolide plugin](https://hub.steampipe.io/plugins/grendel-consulting/kolide).

LLMs keep absorbing more world knowledge, perhaps including the column in which I described James’ method.

I knew that I wanted to do something like what James had done, but I didn’t want to lead the witness, so I didn’t say anything about reflection, I just showed Claude the two tables and prompted:

“Here are two tables. Refactor to use common pagination.”

Lo and behold, it came up with an implementation very similar to the one James uses in the Kolide plugin. It’s hard to know exactly how this happened. On the one hand, the big models (Claude, ChatGPT) keep evolving, and there’s been a lot of chatter about their improved coding prowess. On the other hand, they keep absorbing more world knowledge, perhaps including the column in which I described James’ method. Maybe both factors played into the result, but in any case it was stunning.

The final version of this technique remains just as Claude proposed, but I prodded for and got it to produce a set of comments that help me understand how it works. Here’s the core pagination function.

And here’s how the *wordpress_post* table uses it.

All the other tables use *paginate* in the same way. I’d never have come up with this on my own and, per Simon Willison’s [personal AI ethics](https://simonwillison.net/2023/Aug/27/wordcamp-llms/#personal-ai-ethics) (“never commit if I can’t both understand and explain every line”), I wouldn’t have been comfortable with the initial uncommented version. But after iterating through a chorus of explanations with Claude, and rewriting them as we went along, I am now comfortable with this code.

## A Failed Attempt at Concurrency
With two tables in hand, I turned my attention to dashboards. My test case was this very site, *thenewstack.io*, which is one of the hundreds of millions that are powered by WordPress. I knew that the *wordpress_post* table would be too big to display on a dashboard. For posts, I’d need to rely on the *date KeyColumn* to select subsets, for example:

1 |
select * from wordpress_post where date > now() - interval '1 month' |
But I thought it would be possible, and useful, to have a dashboard with all of the nearly 3,000 authors who have contributed during the site’s 10-year tenure. The query *select * from authors* was doable, but slow. So I had a conversation with ChatGPT about ways to speed that up. One suggestion was to enable HTTP [keep-alive](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Keep-Alive) which, for some reason, was disabled in the Go SDK. (That’s why the commented-out *replace* statement found its way into the plugin’s *go.mod*.) That made a small difference, but not enough to warrant extending the chain of forks in order to depend on yet another variant of the Go SDK.
I was skeptical but ChatGPT was willing to give it a try, so I went along with the experiment.

The next idea was to implement concurrency. The Steampipe engine exploits concurrency [at various levels](https://steampipe.io/blog/release-0-10-0#better-concurrency--caching--faster-control-runs), notably by means of [aggregators](https://steampipe.io/docs/managing/connections#querying-multiple-connections) that parallelize queries across multiple connections. For example, I can set up my *wordpress.spc* configuration file like this:

Now I can write these queries:

*select title, date, link from jon.wordpress_post where date > now() – interval ‘1 month’* — query my site
*select title, date, link from newstack.wordpress_post where date > now() – interval ‘1 month’* — query newstack
*select title, date, link from all_wordpress.wordpress_post where date > now() – interval ‘1 month’* — query both
When I run the *all_wordpress* version of the query, Steampipe queries both sites concurrently. But there isn’t normally a way to parallelize a individual connection. How might that work?

When a query asks the API for more than one gulp of data, the pagination logic kicks in and chunks the query into a series of API calls. Could those perhaps be parallelized? I was skeptical but ChatGPT was willing to give it a try, so I went along with the experiment. We tried a few variants of a strategy that spins up a batch of goroutines and assigns offset-based API calls to each. So one goroutine makes the API call with offset 0, another with offset 100, and so on. The calls can happen in any order, so the success of this approach would depend on the willingness of the WordPress API to accommodate that.

With a batch of 10 goroutines, there was in fact a roughly 10x speedup in the time required to query the *wordpress_author* table. Were the results consistent and accurate? Initially it seemed to work, but more aggressive testing showed that while it *usually* did the right thing, the query sometimes returned too many results (because some were duplicates) and sometimes too few. We tried a number of different ways to make this technique work reliably, and in the end I set it aside as a failed experiment. The key point here, though, is that it was cheap to try. I’m not fluent in the mechanics of goroutines, so I’d have wasted a lot of time on that. ChatGPT’s fluency with those mechanics enabled us to iterate rapidly through various approaches. If there actually is a solution, by the way, I’d love to hear about it!

## Now Add Dashboards
Because Steampipe exposes a [Postgres](https://thenewstack.io/puzzling-over-the-postgres-query-planner-with-llms/) endpoint, you can connect to it from [Metabase](https://turbot.com/pipes/docs/connect/metabase), [Tableau](https://turbot.com/pipes/docs/connect/tableau), or from a variety of other visualization tools. There’s also [Powerpipe](https://powerpipe.io), formerly known as *Steampipe dashboards*, which enables an approach to [writing dashboards](https://powerpipe.io/docs/build/writing-dashboards) that uses SQL to fetch data and HCL to define dashboard widgets that display and interact with that data. [github.com/judell/steampipe-mod-wordpress](https://github.com/judell/steampipe-mod-wordpress) provides a set of Powerpipe dashboards that display data fetched using the WordPress plugin, including the author view shown above.

LLMs will readily produce queries that work, but fail on those criteria, and I don’t want to commit a query that I can’t fully explain.

There are two ways LLMs can help build these dashboards. For SQL, the big models are impressively good. As discussed in [The Future of SQL: Conversational Hands-on Problem Solving](https://thenewstack.io/the-future-of-sql-conversational-hands-on-problem-solving/), I find them especially helpful when iterating toward queries that are easy to test, debug, and understand. Simon Willison’s dictum applies here too. LLMs will readily produce queries that work, but fail on those criteria, and I don’t want to commit a query that I can’t fully explain. You have to push the LLMs to make them cough up clear and maintainable queries, but if you twist their arms they will do it.

Then there’s the HCL aspect of Powerpipe dashboards. HCL (HashiCorp Configuration Language) is well known to the DevOps folk who are the primary users of Steampipe and Powerpipe, and the big models know a lot about [Terraform](https://thenewstack.io/terraform-isnt-dead/)-oriented uses of it. But Powerpipe takes HCL in a different direction: still a way to declare configurations of resources, but in this case the resources aren’t virtual machines and network interfaces, they are dashboard widgets. So HCL as used in Powerpipe is an example of a specialized programming language that the big models don’t yet know much about.

When world knowledge is scarce, you turn to local knowledge. Cody, Copilot, and Unblocked are three ways to augment the big models with specific knowledge of your code. Because it has also indexed the Powerpipe documentation, Unblocked was the most helpful. At one point, for example, I needed the syntax to link an author name in the authors dashboard to the author page in the related dashboard for a selected author. Because that’s something I do rarely, I’ve always needed to look it up in the docs. But Unblocked spared me the trouble.

Thanks Unblocked!

## Querying WordPress
There’s a certain irony here. WordPress uses a MySQL database that you can query directly if you have access. The WordPress API wraps a REST interface around that database, and the plugin in turn wraps a SQL interface around that REST interface. If you can query WordPress directly, and if that’s appropriate in your case, then by all means do so. If you like Powerpipe’s HCL+SQL style, you could even connect Powerpipe dashboards to a WordPress instance of MySQL. The plugin can be useful in complementary ways. Users of the WordPress API might enjoy the abstraction — and standardization — that a SQL interface provides. If you need to query multiple WordPress sites, Steampipe’s connection aggregator will be really handy. And if you want to integrate data from WordPress with data from other APIs wrapped by other plugins in the [Steampipe hub](https://hub.steampipe.io), performing literal SQL JOINs across disparate APIs is a heady experience.

For me, this was the smoothest plugin-writing project so far.

This WordPress plugin is brand new, and not yet available in the Steampipe hub or in [Pipes](https://turbot.com/pipes). So you might want to wait until it’s official. But if you’re champing at the bit, it’s actually quite easy to build and use a Steampipe plugin. And if you want to try extending the plugin, that’s pretty easy as well. I’ve implemented *table_wordpress_post*, *table_wordpress_comment*, *table_wordpress_author*, *table_wordpress_category*, and *table_wordpress_tag*. I asked Claude for suggestions and it proposed:

- table_wordpress_user
- table_wordpress_media
- table_wordpress_plugin
- table_wordpress_theme
- table_wordpress_custom_post_type
- table_wordpress_revision
If you try any of these, let me know how it goes!

For me, this was the smoothest plugin-writing project so far. I attribute that to a mix of factors that are hard to tease apart. The LLMs are more capable, I’ve gained more experience as a plugin writer, and I’ve also learned more about wrangling LLMs effectively. Many of us in the Steampipe community have imagined a fully automated way to generate plugins from API specs. We’re not there yet, but meanwhile it’s clear that LLM assistance makes this kind of project more accessible than ever to those (like me) with only modest programming skill.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)