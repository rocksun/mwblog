# 3 Foundational Principles for Writing Efficient SQL
![Featued image for: 3 Foundational Principles for Writing Efficient SQL](https://cdn.thenewstack.io/media/2025/02/d7f3f409-sql-writing-efficient-1024x576.jpg)
The tables in a [database](https://thenewstack.io/introduction-to-databases/) form the foundations of data-driven applications. Laboring with a schema that’s a haphazard muddle of confusing names and data flaws is a challenge. Building on tables with clear names and clean data simplifies your selects.

In this article, I’ll lay the groundwork for productive [SQL](https://www.oracle.com/database/technologies/appdev/sql.html?source=:ex:pw:::::TNS_SQL_FEB25_A&SC=:ex:pw:::::TNS_SQL_FEB25_A&pcode=) writing by giving tables clear names and avoiding data errors through normalization and constraints.

The second part of this series will cover ways to structure SQL to make it easier to read and debug. So, let’s start by looking at how to get the foundations in place.

## Choose Good Names
Good table names are clear and concise. The names for core tables in your application will be single-word nouns. These map to the corresponding business concepts. For example, `customers`
, `payments`
and `invoices`
. Children of these tables extend the parent name with context like `customer_addresses`
and `invoice_items`
.

Sadly, naming your database objects is a rare luxury. Once you create a table or column, its name is fixed. While you can rename them, you have to change all code to the new name simultaneously. In large codebases, this is impractical.

So, what do you do if you’re working with a schema full of cryptic names? Are you doomed forevermore?

The good news is there are tricks you can use to bring clarity to confusing names:

- Use views to do virtual renames.
- Add schema metadata.
A view is a stored query. You can use these to give a more understandable name to tables or columns. For example, this view makes it clear that the table `cust_adrs`
stores customer addresses and the purpose of its columns:

123456 |
create view customer_addresses as select c_id customer_id, a_id address_id, st start_date, en end_date from cust_adrs; |
You can then use the view like a regular table. Provided you only give new aliases in the view — i.e., the only SQL clauses are `select`
and `from`
, and the `select`
has no expressions — accessing the view is the same as using the table. Over time, you can shift code to use views with better names.
But this approach takes time. There will be an extended period while you’re still working with the original opaque names. Adding metadata can help give context to these.

Table and column comments — free-form text describing objects — are a widely supported way to do this.

[Oracle Database 23ai](https://www.oracle.com/database/?source=:ex:pw:::::TNS_SQL_FEB25_B&SC=:ex:pw:::::TNS_SQL_FEB25_B&pcode=) extended this concept with [schema annotations](https://blogs.oracle.com/coretec/post/annotations-the-new-metadata-in-23c?source=:ex:pw:::::TNS_SQL_FEB25_C&SC=:ex:pw:::::TNS_SQL_FEB25_C&pcode=), the key-value pairs you can use [to document](https://thenewstack.io/how-to-document-database-objects-with-annotations) your tables, views, columns and indexes. For example, these statements annotate the unclear names for the table `cust_adrs`
and its column `c_id`
with a descriptive display value:
12345 |
alter table cust_adrs modify ( c_id annotations ( display 'Customer ID' ) );alter table cust_adrs annotations ( display 'Customer Addresses' ); |
You can view the annotations by [querying](https://thenewstack.io/how-to-write-sql-queries/) the `[dba|all|user]_annotations_usage`
views:
1234567 |
select object_name, column_name, annotation_name, annotation_value from user_annotations_usagewhere object_name = 'CUST_ADRS';OBJECT_NAME COLUMN_NAME ANNOTATION_NAME ANNOTATION_VALUE CUST_ADRS <null> DISPLAY Customer Addresses CUST_ADRS C_ID DISPLAY Customer ID |
Using clear names is the first step to building a good foundation. The next is to structure your tables effectively.
## Normalize Your Schema
Database normalization is the process of removing redundant information from your tables. This avoids data duplication and makes certain types of data errors impossible.

Working with normalized data means you spend less time dealing with data quality issues, such as [finding and removing duplicate rows](https://blogs.oracle.com/sql/post/how-to-find-and-delete-duplicate-rows-with-sql?source=:ex:pw:::::TNS_SQL_FEB25_D&SC=:ex:pw:::::TNS_SQL_FEB25_D&pcode=). This frees you up for more productive tasks like building new features.

The normalization process defines a series of normal forms. These are rules that tables must conform to in order to reach that level of normalization. The first three normal forms are:

**First normal form (1NF):**Each row and column stores a single value and there are no duplicate rows.**Second normal form (2NF):**There are no columns that depend on part of a primary or unique key.**Third normal form (3NF):**There are no columns that depend on columns that are not part of a primary or unique key.
While higher normal forms exist, these relate to overlapping keys and multiple many-to-many relationships. These are rare in practice. Ensuring your tables are in 3NF will cover most cases you work with.

A good smell check to see if a table is normalized to at least 3NF is to ask:

*“If I update one column in a table, does that imply I have to update other columns simultaneously?”*
If the answer is yes, you’ve almost certainly violated a normal form. To fix this, split the dependent columns into a new table or remove them altogether.

For example, say you’re building [a quiz-taking app](https://thenewstack.io/how-to-build-a-quiz-app-with-nuxt-and-xata). When players submit answers, you want to record the time they started, finished, and took to complete a quiz, alongside their answer. This gives a table like:

123456789 |
create table quiz_answers ( quiz_id integer, user_id integer, answer clob, start_time timestamp, end_time timestamp, time_taken interval day to second, primary key ( quiz_id, user_id ) ) |
But there’s a relationship between non-key values: `time taken = end time – start time`
. Changing any of these three columns implies you have to change at least one of the other two also. Avoid this inconsistency by removing one of these columns from the answers table.
Note there is an exception to the update test. This arises if you change all the columns in a table’s primary key or one of its unique constraints. In this case, you’re changing an identifier for the row, so other values will likely change as well.

As with bad names, unnormalized tables are tricky to change in existing applications. Normalizing your data from the start saves you from wading through junk data.

But normalization alone is not enough to save you. To keep your data clean, you should also create constraints.

## Create Appropriate Constraints
[Database constraints](https://docs.oracle.com/en/database/oracle/oracle-database/23/sqlrf/constraint.html?source=:ex:pw:::::TNS_SQL_FEB25_E&SC=:ex:pw:::::TNS_SQL_FEB25_E&pcode=) enforce data rules. The database ensures all data meet these rules.
Without constraints in place, data errors will creep in, which can cause customers to lose faith in your applications. Finding and fixing these errors is time-consuming. Creating constraints at the start avoids this pain.

The main constraints are:

**Primary key:**Ensures values are mandatory and unique. A table can only have one primary key.**Unique constraints:**Like a primary key, a unique constraint stops you from storing duplicate values. Unlike a primary key, you can store nulls in unique columns, and one table can have many unique constraints.**Foreign keys:**Define a parent-child relationship. The foreign key points from columns in the child table to the primary key or a unique constraint in the parent. With this in place, you can’t have orphaned rows.**Not-null constraints:**Ensure you can store only non-null values in the columns, i.e., they’re mandatory.**Check constraints:**Verify a condition is true or unknown for every row.
Defining these constraints helps cement the foundations laid by normalization. For example, primary keys or unique constraints are necessary to enforce the “no duplicate rows” rule in 1NF.

Constraints can also help if you find yourself working with unnormalized data. While discussing normalization, we saw how storing start times, end times and durations for quiz answers can lead to inconsistencies. While removing one of these columns is the best solution, this may be impractical in a longstanding application.

Instead, you can ensure that all data conforms to the formula by adding this check constraint:

123 |
alter table quiz_answers add constraint quan_answer_time_c check ( ( end_time – start_time ) = time_taken ) |
Once in place, new data that violates this rule will be rejected.
Unfortunately, it’s likely there is existing data where this rule is false. If so, adding the constraint will fail, and you’ll have the time-consuming job of fixing it. Fortunately, there’s a trick you can use to stop more invalid data from arriving:

Create unvalidated constraints.

These ignore existing data and apply the rules only to new data. Do this in Oracle Database with the following:

1 |
alter table … add constraint … novalidate; |
While you should still clean the existing data, you can be sure that no new errors will creep in.
## Building on Solid Foundations
Working with poorly named tables and invalid data means spending time deciphering and correcting them; a drag on your productivity.

Choosing good names, normalizing your tables and creating constraints give you a solid structure to be productive when [writing SQL](https://roadmap.sh/sql). With these foundations in place, you can turn your attention to structuring your SQL effectively. Stay tuned for the second article in this series for tips and tricks to help you do this.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)