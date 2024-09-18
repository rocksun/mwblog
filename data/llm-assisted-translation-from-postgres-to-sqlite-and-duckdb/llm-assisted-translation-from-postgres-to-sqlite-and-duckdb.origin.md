# LLM-Assisted Translation From Postgres to SQLite and DuckDB
![Featued image for: LLM-Assisted Translation From Postgres to SQLite and DuckDB](https://cdn.thenewstack.io/media/2024/09/f23034f0-ray-hennessy-k75eq2gk_zq-unsplash-1024x683.jpg)
My
[Hacker News](https://github.com/jonudell/hackernews) repo provides a set of [Powerpipe](https://powerpipe.io) dashboards that use a [Steampipe plugin](https://hub.steampipe.io/plugins/turbot/hackernews) to acquire data from the Hacker News API and provide interactive visualizations of the data. Originally it worked only with Postgres, but more recently Powerpipe gained the ability to flow data into its dashboards from SQLite and DuckDB.
Once I got SQLite and DuckDB ports working, I found that both ran the dashboard’s several dozen queries almost twice as fast as Postgres.
Here is the home dashboard:
In theory, these Postgres-based dashboards should work identically with SQLite and DuckDB. In practice, there are differences to be ironed out at two levels: HCL and SQL. Powerpipe uses HCL to define widgets — including charts, tables, infocards, and picklists — and SQL to flow data into those widgets. Let’s start with the HCL layer. Here’s the HCL definition for the triptych of panels that compare the languages mentioned in Hacker News titles at three different timescales.
These, and similar triptychs for companies, databases, and so on, reuse a common SQL query,
*query.mentions*. Each chart instance passes three parameters to the query: a list of names (of languages, companies, etc.), and a pair of integers that define the age, in minutes, of Hacker News posts. Here’s the current list of languages, represented as regular expressions so that the SQL query can do fuzzy matching.
And here’s the query that receives those parameters.
## From HCL Lists to SQL Rows
The first CTE (common table expression) turns the list of names into a set of rows. Powerpipe passes the names as an array of strings, which is a native Postgres type that can use its
*unnest* function to unroll. For each of those names, the second CTE counts the posts in the *hn* table with titles that match the name and timestamps in the desired range.
That didn’t work in either SQLite or DuckDB. Neither could accept an array of strings as a parameter. The solution, proposed independently by both ChatGPT and Claude, was to turn the list into a comma-separated string in the HCL layer, and then unroll it differently in the SQL layer. Here’s the HCL part.
The unrolling was straightforward in DuckDB, thanks to its
*string_to_array* and *unnest* functions. It was surprisingly gnarly in SQLite.
I’d rather avoid SQL recursion if possible. In this case, both ChatGPT and Claude pointed to the same solution, though, so I reluctantly accepted it.
## Matching Names and Filtering Times
Now the query has to count mentions for each name in the unrolled list. Here are the solutions I landed on for the three databases.
This kind of thing is always fiddly, and while ChatGPT and Claude were certainly helpful, I had to supervise them heavily. Both have a burning desire to write complete new versions of a query, function, or other substantial chunk of code. Those rewrites often fail, and while relaying the errors back to the LLMs can sometimes lead to a quick resolution, that strategy can become a death spiral — as it did in this case.
The correct strategy isn’t rocket science: decompose the problem into small testable pieces, run those tests, resolve problems in a granular way, and build back up toward the complete thing. It’s only what you ought to be doing anyway, and the LLMs can be very helpful if strictly supervised. But it does take effort to keep them focused.
I tried customizing ChatGPT’s base user-level prompt with these instructions.
I need practical solutions that build step-by-step, with clearly defined and testable intermediate states.
Please do not write code unless I explicitly ask you to, I always want to start by talking about strategy.
That doesn’t seem to rein in its code-happy style, though. I have to really hold its feet to the fire to work in small testable increments.
## Further Translations
The remaining queries on the home dashboard ported to SQLite and DuckDB with varying degrees of difficulty. Regular expressions worked differently across the three databases and were easy for the LLMs to adapt. Datetime types and expressions also work differently, they present
[intrinsically harder problems](https://thenewstack.io/an-llm-turbocharged-community-calendar-reboot/), and the LLMs were less helpful in those cases. As always, I relied on two [guiding principles](https://thenewstack.io/7-guiding-principles-for-working-with-llms/): *never trust, always verify* and *compare outputs from LLMs*. But it was still a bit of a slog.
On reflection, the difficulty shouldn’t have been surprising. I’ve mostly worked with Postgres, which is popular, well-known to search engines and, thus, also well-known to LLMs. But while
[SQLite](https://thenewstack.io/the-origin-story-of-sqlite-the-worlds-most-widely-used-database-software/) has been gaining ground for years, and [DuckDB](https://thenewstack.io/duckdb-in-process-python-analytics-for-not-quite-big-data/) is coming on strong, its online footprints are smaller.
The dashboard we’re discussing here provides an informal measure of relative popularity. Here are the counts of recent mentions of the three databases in Hacker News titles.
If I needed to work regularly with SQLite or DuckDB, I’d use an LLM that supports
[retrieval augmented generation](https://thenewstack.io/freshen-up-llms-with-retrieval-augmented-generation/) (RAG)— for example, [Unblocked](https://getunblocked.com) — to enrich the LLM context with documentation and discussions. The same principle applies to languages other than Python and JavaScript. LLMs give you a smoother ride when you’re working with the most popular technologies; out on the long tail, you have to work harder to reap the benefits.
## Powerpipe and DuckDB
Once I got SQLite and DuckDB ports working, I found that both ran the dashboard’s several dozen queries almost twice as fast as Postgres. Considering both SQLite and DuckDB as analytics alternatives to Postgres, DuckDB is intriguing. It feels almost as light as SQLite, Postgres-flavored SQL ports more readily to it than to SQLite, and it can even attach Postgres tables. But DuckDB has a whole other personality too. Sometimes called “SQLite for columns,” it can tear through huge datasets (typically in Parquet format) that neither Postgres nor SQLite is built to handle.
Until now, I’ve mainly built Powerpipe dashboards that connect to Steampipe, an instance of Postgres that works with a
[suite of plugins](https://hub.steampipe.io) that translate many APIs and file formats to SQL. Now that I’ve worked with DuckDB in a row-oriented way, I want to explore its column-oriented personality as well and find out what it’s like to use SQL as a bridge between the two worlds. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)