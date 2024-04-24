# The Future of SQL: Conversational Hands-on Problem Solving
![Featued image for: The Future of SQL: Conversational Hands-on Problem Solving](https://cdn.thenewstack.io/media/2024/04/39c095b8-getty-images-umbdzvnab-q-unsplash-1024x683.jpg)
If you’re returning to SQL after a long absence, as I did a few years back, there are
[important changes](https://modern-sql.com/) to know about. First, JSON. Many SQL-oriented databases now support [JSON columns](https://thenewstack.io/why-and-how-you-should-manage-json-with-sql/) for arbitrary tree-structured data. Second, [common table expressions](https://thenewstack.io/how-to-make-sql-easier-to-understand-test-and-maintain/) (CTEs) that you can use to express a complex query as a pipeline of steps that are simple to understand and verify.
The JSON features can be confusing, for example in Steampipe queries like this one which implicitly joins the table
[github_my_gist](https://hub.steampipe.io/plugins/turbot/github/tables/github_my_gist) with the expansion of its JSON column
files.
|
1
2
3
4
5
6
7
8
9
10
|
select
file ->> 'language' as language,
count(*)
from
github_my_gist g,
jsonb_array_elements(g.files) file
group by
language
order by
count desc;
*Exhibit A*
The query counts GitHub gists by language, and produces output like this.
|
1
2
3
4
5
6
|
| language | count |
|-------------|-------|
| Python | 15 |
| Markdown | 34 |
| JavaScript | 7 |
| null | 7 |
Here’s a different version of the query that produces the same result.
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
|
-- cte 1 to unnest the json
with expanded_files as (
select
g.id as gist_id,
jsonb_array_elements(g.files) AS file
from
github_my_gist g
),
-- sample cte 1 output
-- | gist_id | file |
-- |---------|------------------------------|
-- | 1 | {"language": "Python"} |
-- | 2 | {"language": "Markdown"} |
-- | 3 | {"language": "JavaScript"} |
-- | 4 | {"language": "Python"} |
-- cte 2 to extract the language
languages AS (
select
file ->> 'language' as language
from
expanded_files
)
-- sample cte 2 output
-- | language |
-- |-------------|
-- | Python |
-- | Markdown |
-- | JavaScript |
-- | Python |
-- final phase to count languages
select
language,
count(*) as count
from
languages
group by
language
order by
count desc;
-- sample final output
-- | Python | 2 |
-- | Markdown | 1 |
-- | JavaScript | 1 |
*Exhibit B*
## Levels of Expertise
If you’re well versed in set-returning JSON functions like Postgres’
jsonb_array_elements, which converts a JSON list into a set of rows, and if you can visualize how that transformation interacts with joins, you can craft powerful queries like exhibit A very concisely.
That economy of expression can be good for experts, but newcomers can struggle to mentally unroll the implied steps of the transformation. By “newcomer” I do not mean novice; I mean not yet an expert in this combination of disciplines. (That includes me, by the way, despite years of engagement with SQL at this level.)
From that perspective, you might want to see the steps spelled out explicitly, as in exhibit B. Creating versions of exhibit B is something I do in our support channel, and wanted to do more easily. So I made a simple
[GPT](https://thenewstack.io/creating-a-gpt-assistant-that-writes-pipeline-tests/) for that — and when I say “simple GPT,” I mean something like a simple bash script: a quickly built tool that can save more time and/or effort than it costs to build it.
Because it’s broken down into a pipeline of checkable steps, exhibit B is easier to debug, use confidently and revise safely. You could then collapse it down to exhibit A, which might be more efficient, though that’s not necessarily true.
You could even make both versions available, so experts and nonexperts can each see through their preferred lenses. Arguably that’s another form of accessibility, along with everything else that we mean by accessibility.
Here’s
[the prompt](https://gist.github.com/judell/9341d7210d46fe269fdb024a2c3b70c4) for this GPT. I used it to ask for the names of the issue templates for a given repo, given [this schema](https://hub.steampipe.io/plugins/turbot/github/tables/github_repository#inspect) and an
issue_templates column that looks like this:
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
|
+------------------------------------------------------------------------------------------------------------------
| issue_templates
+------------------------------------------------------------------------------------------------------------------
| [
| {
| "body": "**Describe the bug**\nA clear and concise description of what the bug is.\n\n**Steampipe version
| "name": "Bug report",
| "about": "Create a report to help us improve",
| "title": "",
| "filename": "bug_report.md"
| },
| {
| "body": "**Is your feature request related to a problem? Please describe.**\nA clear and concise descript
| "name": "Feature request",
| "about": "Suggest an idea for this project",
| "title": "",
| "filename": "feature_request.md"
| }
| ]
+------------------------------------------------------------------------------------------------------------------
In that context, I literally just asked for a query that (per above) lists the names of issue templates for a given repo. Here’s the concise version of the generated (and documented) query.
|
1
2
3
4
5
6
7
|
SELECT
template ->> 'name' AS template_name
FROM
github_repository,
jsonb_array_elements(issue_templates) AS template
WHERE
full_name = 'your-repository-full-name'; -- Replace 'your-repository-full-name' with the actual full name of your repository
And here’s the expanded version.
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
|
-- CTE to expand the JSON array of templates
WITH expanded_templates AS (
SELECT
r.id AS repo_id,
jsonb_array_elements(r.issue_templates) AS template
FROM
github_repository r
WHERE
r.full_name = 'your-repository-full-name' -- Replace 'your-repository-full-name' with the actual full name of your repository
),
-- Sample data after CTE 1
-- | repo_id | template |
-- |---------|-----------------------------------------|
-- | 1 | {"name": "Bug report", ...} |
-- | 1 | {"name": "Feature request", ...} |
-- CTE to extract the template names
template_names AS (
SELECT
template ->> 'name' AS template_name
FROM
expanded_templates
)
-- Sample data after CTE 2
-- | template_name |
-- |------------------|
-- | Bug report |
-- | Feature request |
-- Final selection
SELECT
template_name
FROM
template_names;
This approach works well enough for simple cases like these, but not so much for more complex ones like
[this one](https://hub.steampipe.io/plugins/turbot/aws/tables/aws_s3_bucket#list-bucket-policy-statements-that-grant-external-access-for-each-bucket), which finds S3 buckets with policies that grant external access. In that situation, you don’t just need Postgres knowledge: You also need to know how AWS policies are constructed, and then you need to work out how to use Postgres joins and JSONB operators to query them. If the GPT initially fails to do that for you, that isn’t the end of the story. Having provided a description of the result you want, along with the schema for a table and a sample of a required JSON column, you’ve set up a context for a conversation with an entity that has seen vastly more SQL patterns and AWS policy patterns than you ever will.
## Conversational Hands-on Learning
I keep returning to the theme of choral explanations (
[#4 on my list of best practices](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)), and it’s especially relevant in the SQL domain where there are just so many ways to write a query.
Exploring the range of possibilities used to be arduous, time-consuming and hard to justify. Now it’s becoming hard to justify
*not* doing that; optimizations (sometimes major ones) can and do emerge.
Arguably it has always required a kind of alien intelligence to grok SQL, not to mention
[query planners](https://blog.jonudell.net/2023/11/28/puzzling-over-the-postgres-query-planner-with-llms/). In conversation with LLMs, we can now rapidly explore the space of possibilities and more easily evaluate how different approaches will perform. How else could I write this query? Why would I do it that way? How will the database handle it? (Maybe you can fluently read and understand query plans but I can’t, and I gratefully accept all the help I can get.)
I routinely ask LLMs these kinds of questions and receive answers that are not theoretical, but are versions of my query — working with my data — that I can immediately try, and that lead to follow-up questions that I can also explore cheaply.
Arguably it has always required a kind of alien intelligence to grok SQL, not to mention query planners.
In one test of my latest GPT, I wondered about translating Postgres idioms to SQLite. Postgres and SQLite JSON patterns are quite different. Holding both sets of patterns in your head, and mentally mapping between them, is only a means to an end. If I’m considering whether it’s feasible to switch databases, I don’t want to invest in a deep understanding of SQLite patterns that I wind up never needing. I just want to know what’s possible.
The GPT, which was nominally about Postgres, was happy to help. All you’re really doing with these GPTs is setting an initial context. At any point, you can steer the conversation wherever you want it to go.
Here’s the SQLite counterpart to the query that counts gists by language.
|
1
2
3
4
5
6
7
8
9
10
|
select
json_extract(value, '$.language') as language,
count(*) as count
from
github_my_gist,
json_each(github_my_gist.files)
group by
language
order by
count desc;
ChatGPT gave it to me instantly, I tested it and it worked. Of course, I then wanted to unroll this compact version to visualize the query in a step-by-step manner. It turns out that you can’t eliminate the join, as far as I can tell. Here is ChatGPT’s explanation.
json_each: This is SQLite’s equivalent to jsonb_array_elements, but it functions slightly differently. It must be used in the FROM clause and typically combined directly with the table it is extracting data from due to the less flexible nature of SQLite’s query planner regarding complex JSON operations.
Is that strictly accurate? I don’t know, but it comports with the behavior I’m seeing, which of course is behavior that ChatGPT enabled me to effortlessly conjure into being. This sort of conversational hands-on learning is the signal I’m following to cut through the noise and hype around AI.
Ultimately I don’t care about SQL or JSON; I want to climb up the ladder of cognition in order to solve problems that yield to data acquisition and analysis. I’m not blind to the dark patterns embodied in the most powerful LLMs, but I’m unable to ignore the boost they can deliver. Many kinds of work require us to reason over information at scale, and not just over your code and documentation, though that’s our focus here. I don’t want radiologists to rely solely on AI, but I do want them to consult entities that have seen far more X-rays and diagnostic interpretations than they ever will. In the realm of infotech, I want wranglers of code and data to make the best possible use of these new reasoning partners.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)