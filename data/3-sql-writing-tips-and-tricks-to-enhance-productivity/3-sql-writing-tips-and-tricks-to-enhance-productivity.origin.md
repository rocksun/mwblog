# 3 SQL Writing Tips and Tricks To Enhance Productivity
![Featued image for: 3 SQL Writing Tips and Tricks To Enhance Productivity](https://cdn.thenewstack.io/media/2025/03/96a7ebe2-sql-writing-productive-1024x576.jpg)
If you’re a database developer, database administrator or data analyst, writing [SQL](https://www.oracle.com/database/technologies/appdev/sql.html?source=:ex:pw:::::TNS_SQL_FEB25_A&SC=:ex:pw:::::TNS_SQL_FEB25_A&pcode=) to get data into and out of [databases](https://thenewstack.io/introduction-to-databases/) is a key part of your job. Doing this quickly and effectively improves your productivity. Conversely, working with a tangled mess of statements and data leaves you stuck.

In the [first part of this series](https://thenewstack.io/3-foundational-principles-for-writing-efficient-sql/), I demonstrated how choosing good names, normalizing your tables and creating constraints give you a solid structure to be productive when writing SQL.

In this article, I’ll cover ways to [structure SQL](https://roadmap.sh/sql) to make it easier to read and debug. Techniques such as common table expressions (CTEs) and table aliases can transform statements from indecipherable riddles to clear logic.

## Structure Queries Clearly
Large SQL statements can be hard to read and debug. CTEs, aka the `with`
clause, enable you to break them into smaller parts.

CTEs are named subqueries that come at the top of `select`
statements. You access these subqueries like regular tables later in the query.

This brings a few benefits:

- You can build the query bit-by-bit.
- You can give each CTE a meaningful name.
- You can check the results of each CTE.
For example, the [Oracle Dev Gym](https://devgym.oracle.com/pls/apex/dg/class/databases-for-developers-foundations.html?source=:ex:pw:::::TNS_SQL_FEB25_F&SC=:ex:pw:::::TNS_SQL_FEB25_F&pcode=) offers free quizzes, workouts and classes to help you learn SQL. Each of these activities has its own tables. Combining all these in one query to report all activities is a daunting task.

Using the `with`
clause, you can create a CTE for each activity type. You can start with getting [quiz](https://thenewstack.io/how-to-build-a-quiz-app-with-nuxt-and-xata/) totals:

12 |
with quiz_totals as ( … ) select * from quiz_totals |
Then add workout totals and verify they are correct:
123 |
with quiz_totals as ( … ), workout_totals as ( … ) select * from workout_totals |
Repeat this for class totals and combine the results of each CTE to get all totals, like so:
123456789 |
with quiz_totals as ( … ), workout_totals as ( … ), class_totals as ( … ), all_totals as ( select * from quiz_totals union all select * from workout_totals union all select * from class_totals ) select * from all_totals |
If you need to change the queries for any activity type, it’s clear that the logic is contained in the corresponding CTE. It is far simpler than hunting through a mass of nested subqueries.
Using CTEs to break up logic into smaller problems makes the process more manageable. However, each CTE can still reference many tables. Whenever you’re working with many tables, there’s an important question to answer: Which columns belong to which table?

Make this clear by prefixing each column with its table’s alias.

## Use Good Table Aliases
Without table aliases, knowing where each column is from is tough. This makes queries harder to understand and change.

However, unaliased columns have a bigger problem: they can lead to errors.

The most common issue is when two tables have columns with the same name. If you use the unaliased name, the database cannot identify which table it’s from, and the statement will fail. What’s worse is this problem can affect existing SQL if you add a column that causes a name clash.

Qualifying columns with their table avoids these problems. Single-letter table aliases taken from the start of the table name are appealing but can quickly lead to problems. For example, say you write a query that accesses both the customers and contracts tables. If you give one the alias “c,” how do you know which it relates to without scrolling through the statement?

A better approach is to use four-character aliases taken from the start of the table name:

- For a single-word table, the alias is its first four characters.
- Two-word tables take the first two letters of each word.
- Three-word tables use the first two letters of the first word and the first letter of the last two words.
- Four-word tables use the first character of each word.
For example,

`customers`
=>`cust`
`order_items`
=>`orit`
`shipment_list_batches`
=>`shlb`
In rare cases, this gives different tables the same alias. If this happens, pick a new alias for one table, following this system as closely as possible. If you need to access the same table twice in a query, add a prefix to the alias stating the table’s role. The columns you’re joining them on are a good source for this.

For example, you may need to join customers to their delivery and payment addresses, both stored in the addresses table. Adding `deli`
or `paym`
as appropriate makes it clear which role the address table plays:

12345 |
from customers custjoin addresses deli_addr on cust.delivery_address_id = deli_addr.address_idjoin addresses paym_addron cust.payment_address_id = paym_addr.address_id |
Using a standard aliasing system quickly becomes second nature, makes it clear which table columns belong to and avoids errors. A standard structure is key to further aid the readability of your code.
## Use a Consistent Style
The best way to format your SQL is the source of many debates. We all have our own preferences for where and how to indent clauses. Whether keywords should be in uppercase or lowercase is a long-running battle.

Ultimately, most of these choices come down to personal preference. So, the most important advice is:

**Choose a formatting style and stick to it.**
However you like to format your SQL, we can all agree that mixing and matching styles within a statement like this is jarring and hard to read:

1234 |
SELECT Some_Columns From a_table JOIN another_table on … |
The best way to ensure a standard style is to use your editor’s auto formatter. Run it after writing each statement. This is quicker than formatting as you go. You can also share the rules with your colleagues to keep your whole codebase formatted similarly.
Occasionally, auto formatters can struggle to spot where to place line breaks in complex SQL using niche features. This can result in combining expressions into long lines that scroll right off the edge of the screen.

If you hit this problem, a trick to overcome it is to place an empty comment where you want line breaks. The formatter has to respect these, guaranteeing a line break exactly where you want it.

For example:

123 |
select case -- when formatted_lines_are_too_long -- then 'Use comments to break them up' -- |
Using a standard formatter is one of the many ways your editor can help you write SQL faster, so it’s worth investing time to learn your editor’s productivity features.
## Get To Know Your Editor
You’ve likely enabled autocomplete for table and column names to help you write SQL. But this is just one way your tools can help you be more productive.

For example, the [Oracle SQL Developer extension for VS Code](https://www.oracle.com/database/sqldeveloper/vscode/?source=:ex:pw:::::TNS_SQL_FEB25_G&SC=:ex:pw:::::TNS_SQL_FEB25_G&pcode=) has a few gems to help you.

You can drag tables or columns from the schema browser into the editor. It then asks you whether to use these in a `select`
,` insert`
,` update `
or `delete`
statement:

This saves you from having to type out every column by hand, a tedious task for tables with many columns.

You can also configure code snippets in VS Code that expand short sequences into large code blocks. Here are a few that I rely on to speed up the process of writing SQL:

`ssf`
=>`select * from`
`ii`
=>`insert into $1 values ( $2 )`
`crt`
=>`create table $1 ( c1 int );`
`drt`
=>`drop table $1 cascade constraints purge;`
Spending time learning the keyboard shortcuts in your editor for everyday tasks can also reap good rewards.

## Conclusion
Business requirements can be complex. Translating these to SQL can be challenging and can lead to massive monstrosities if you’re careless.

Taking care to structure SQL clearly by using CTEs and good table aliases can speed up SQL’s writing and maintenance processes. Using auto-formatters and other tools in your editor can further streamline tasks and enhance your productivity.

However, as we saw in the first part of this series, the most significant gains come from building a solid data model. Choosing good names, normalizing your tables and creating constraints make understanding your schema simple and writing SQL a snap.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)