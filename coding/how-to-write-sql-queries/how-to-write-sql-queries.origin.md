# How to Write SQL Queries
![Featued image for: How to Write SQL Queries](https://cdn.thenewstack.io/media/2024/03/aa2e781b-sql-query-1024x576.jpg)
SQL is a declarative, English-like domain language for querying, analyzing and manipulating data. SQL originated from
[relational databases](https://thenewstack.io/json-and-relational-tables-how-to-get-the-best-of-both/) but has since been widely adopted elsewhere. SQL is considered a declarative language, meaning users declare *what* results they want and not *how* to get to these results (the latter is the approach of imperative programming languages, such as C, Java and [Python](https://thenewstack.io/python/)). Because of this and the ability to read SQL statements almost as English-language sentences, SQL is generally seen as one of the best high-level declarative programming languages for analyzing data due to its [easy-to-learn syntax](https://thenewstack.io/how-to-make-sql-easier-to-understand-test-and-maintain/).
SQL has different language elements that can be divided at a high level between
**queries** and **data manipulation**. SQL queries use the
SELECT statement, while SQL used for data manipulation uses the
INSERT,
UPDATE,
DELETE and
MERGE statements. The data manipulation statements are collectively called
**Data Manipulation Language** or DML.
This article will break down the anatomy of SQL query language, while the second part of the series will describe DML.
## Defining SQL Queries
SQL queries are probably the most common operations used in SQL, as they allow users to retrieve and analyze data from one or more tables. SQL query statements include the following elements:
SELECTand
FROM
SELECTwithout
FROM
JOIN
WHERE
GROUP BY
HAVING
ORDER BY
OFFSET
FETCH
OFFSET and FETCH
The
SELECT statement includes a couple of elements, but only the first two are required:
SELECT and
FROM. However, some databases including
[Oracle Database](https://www.oracle.com/database/?source=:ex:pw:::::TheNewStack_A&SC=:ex:pw:::::TheNewStack_A&pcode=) and MySQL make the
FROM clause optional if the
SELECT refers only to self-contained expressions, such as
SELECT 1;SELECT sysdate; and
SELECT my_function();. In these cases, the data is not derived from a table, hence
FROM is not required.
Optional components are illustrated by putting
[ ] around them.
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
|
SELECT <expressions>
FROM <table or sub-query>
[ JOIN <to other table> ON <join condition> ]
[ WHERE <predicates> ]
[ GROUP BY <expressions>
[ HAVING <predicates> ] ]
[ ORDER BY <expressions> ]
[ OFFSET ]
[ FETCH ]
A common misconception is that these components execute in the same order as they appear in the query. This is not the case, as the
SELECT component is processed after the
HAVING clause. The following lists the order that which the clauses are processed and their purpose:
**: Indicates which table(s) to retrieve data from. The**
FROM
FROMclause determines the working set of data that is being retrieved. This usually refers to a table but can also include a subquery (another
SELECTquery that acts as the input source for the current query).
**: Specifies the rules for joining multiple tables. The**
JOIN
JOINclause is part of the
FROMclause and combines the data from multiple tables into one data set. It is one of the fundamental operators of the relational model to combine different relations into one set. The
JOINclause allows join conditions that ensure that only rows that logically belong together are joined (rows with matching primary key –> foreign key relationships). Multiple
JOINclauses can be specified to join multiple tables into the data set. Because the
JOINclause is part of the
FROMclause, it cannot be specified without a preceding
FROMstatement in the query.
**: Filters the rows returned by the query. The**
WHERE
WHEREclause filters the data set based on the provided
*predicates*or filter conditions and discards all rows that do not match them. It narrows down the results, for example, to retrieve all
countriesfrom the continent of
Europeinstead of all countries in the world.
**: Aggregates (or groups) rows with common values in the specified column(s) into one row. The resulting row is sometimes referred to as a**
GROUP BY
*grouping set*. Because rows with common values are aggregated into one row, there will only be as many rows as there are unique values. For values of columns not specified in
GROUP BY, aggregate functions in the
SELECTclause are required to aggregate these values per group.
**: Filters rows resulting from the**
HAVING
GROUP BYclause. It is therefore a part of the
GROUP BYand cannot be used without a preceding
GROUP BYstatement in the query.
**: Defines the list of column(s) and expression(s) to appear in the query result output. The**
SELECT
SELECTclause computes any expressions and defines the list of columns to be returned, or
*projected*, as the query result. **: Identifies which column(s) to use to sort the resulting data and in which direction to sort them (ascending or descending). If the**
ORDER BY
ORDER BYis omitted, the order of the rows returned by a SQL query is undefined.
**: Specifies the number of rows to skip in the result set before returning the data.**
OFFSET
**: Specifies the number of rows to return from the result.**
FETCH
## Using SQL Queries
Now that you’re familiar with what the various SQL query clauses mean, you can start using them. You can follow along with these exercises using the data model in my
[GitHub repository](https://github.com/gvenzl/sample-data/tree/main/countries-cities-currencies).
### SELECT and FROM
In its simplest form, a SQL query is comprised of a
SELECT and a
FROM clause:
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
|
SQL> SELECT *
2* FROM regions;
REGION_ID NAME
____________ ________________
AF Africa
AN Antarctica
AS Asia
EU Europe
NA North America
OC Oceania
SA South America
7 rows selected.
This query selects all rows and all columns (as indicated by the
* after
SELECT, which is short for “all columns”) from a table called
regions. If you want to return a given list of columns, you can call them out specifically:
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
|
SQL> SELECT name
2* FROM regions;
NAME
________________
Africa
Antarctica
Asia
Europe
North America
Oceania
South America
7 rows selected.
### SELECT without FROM
The
SELECT statement can also compute expressions, for example,
1+2. Technically, neither the constant
1 nor the constant
2 come from any table, but the ISO SQL standard nevertheless requires a
FROM clause. Many databases have “dummy” tables to enable such queries, such as the
dual table in Oracle Database.
|
1
2
3
4
5
6
|
SQL> SELECT 1+2
2* FROM dual;
1+2
______
3
However, many databases, including Oracle Database, have loosened this restriction from the SQL standard and allow queries to omit the
FROM clause in such cases:
|
1
2
3
4
5
|
SQL> SELECT 1+2;
1+2
______
3
### JOIN
The relational model is all about normalizing data, that is putting independent data into separate tables and defining
*relationships* between these tables. To recombine normalized data, you can use *joins* to join these tables back together.
The following example has two tables: the previously queried
regions table, and the new
countries table. To write a query that joins both tables into one result, you use the
JOIN clause. Without a
JOIN clause, if you specify the two tables in the
FROM clause, every row from the table regions will be multiplied by every row from the table
countries. This is often referred to as the
*cross product* and it’s a common mistake that SQL beginners make. For example:
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
|
SQL> SELECT r.name, c.name
2* FROM regions r, countries c;
NAME NAME
_________ ___________________________________
Africa Kosovo
Africa Yemen
Africa South Africa
Africa Zambia
Africa Zimbabwe
Africa Andorra
Africa United Arab Emirates
Africa Afghanistan
Africa Antigua and Barbuda
Africa Albania
Africa Armenia
Africa Angola
Africa Argentina
Africa Austria
Africa Australia
...
...
...
South America Uzbekistan
South America Vatican City
South America Saint Vincent and the Grenadines
South America Venezuela
South America Vietnam
South America Vanuatu
South America Samoa
1,372 rows selected.
The output from this query is obviously incorrect. There are neither 1,372 countries, nor is Austria located in Africa. What we really want is to join all rows from the
countries table with the
regions table
**where the**
region_id
**is the same**. This is generally referred to as the *join condition* and can be specified in the
ON clause as part of the
JOIN clause:
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
|
SQL> SELECT r.name, c.name
2 FROM regions r
3 JOIN countries c
4* ON (r.region_id=c.region_id);
NAME NAME
_________ ___________________________________
Africa South Africa
Africa Zambia
Africa Zimbabwe
Africa Angola
Africa Burkina Faso
Africa Burundi
Africa Benin
...
...
...
South America Ecuador
South America Guyana
South America Peru
South America Paraguay
South America Suriname
South America Uruguay
South America Venezuela
196 rows selected.
That’s more like it!
There is one more thing to note: The above queries specified
SELECT r.name, c.name and put the letters
r and
c next to the table names. These are
*table aliases* and are required to tell the database which table column you want. If the statement just said
SELECT name, name, it would be unclear whether the query refers to the
regions table column name or the
countries table column name.
### WHERE
The
WHERE clause filters the rows produced by the
FROM clause. Until now, you always got all the rows that were in the tables. If you want to return only all countries in South America, this is where the
WHERE clause comes in. It can be used to match all rows with the
regions.name column value
'South America':
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
|
SQL> SELECT r.name, c.name
2 FROM regions r
3 JOIN countries c
4 ON (r.region_id=c.region_id)
5* WHERE r.name = 'South America';
NAME NAME
________________ ____________
South America Argentina
South America Bolivia
South America Brazil
South America Chile
South America Colombia
South America Ecuador
South America Guyana
South America Peru
South America Paraguay
South America Suriname
South America Uruguay
South America Venezuela
12 rows selected.
### GROUP BY
The
GROUP BY clause is often a puzzle for SQL beginners. The clause is used to aggregate multiple rows into a group, essentially combining multiple rows into one row. When would such a thing ever be useful? Well, for example, the
countries table contains a column called population but the
regions table does not:
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
|
SQL> SELECT r.name, c.name, c.population
2 FROM regions r
3 JOIN countries c
4 ON (r.region_id=c.region_id)
5* WHERE r.name = 'South America';
NAME NAME POPULATION
________________ ____________ _____________
South America Argentina 44694000
South America Bolivia 11306000
South America Brazil 208847000
South America Chile 17925000
South America Colombia 48169000
South America Ecuador 16291000
South America Guyana 741000
South America Peru 31331000
South America Paraguay 7026000
South America Suriname 598000
South America Uruguay 3369000
South America Venezuela 31689000
12 rows selected.
A common business question might be: “What is the total population of each region?” Given that the
regions table does not have a column with that information, the answer can be provided only by calculating the sum of the
population column for each country per region. So, you need a mechanism that takes the 196 rows of the
countries table and puts them into seven groups or buckets based on their region (because there are seven rows in the
regions table). However, the query cannot just put the 196 rows into seven rows; it needs to calculate the sum of the population per region based on the populations of the countries belonging to the region.
This can be done by applying the
SUM() aggregate function over the
population column:
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
|
SQL> SELECT r.name, SUM(c.population)
2 FROM regions r
3 JOIN countries c
4 ON (r.region_id=c.region_id)
5* GROUP BY r.name;
NAME SUM(C.POPULATION)
________________ ____________________
Africa 1263685000
Asia 4439011000
Europe 748985000
North America 575767000
Oceania 37556000
South America 421986000
6 rows selected.
This query shows something else interesting. Although there are seven regions in the regions table, the query produced six rows. This is because there is a region
'Antarctica', but there is no country with that
region_id in the
countries table. Hence, the
JOIN clause filters that region out (because there is no matching
region_id in the
countries table as specified by the
ON clause).
A
GROUP BY clause does not require any
JOIN clause; you can create groups in just a single table. For example, “How many countries start with the same letter?” can also be answered via a
GROUP BY. To do this, create as many groups per the unique first letter value for all rows by using the
SUBSTR() function, and then count the rows that fall into that group or category:
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
|
SQL> SELECT SUBSTR(name,1,1), COUNT(*)
2 FROM countries
3* GROUP BY SUBSTR(name,1,1);
SUBSTR(NAME,1,1) COUNT(*)
___________________ ___________
K 6
Y 1
S 26
Z 2
A 11
U 7
B 17
C 17
D 5
G 11
E 8
F 3
M 18
H 3
I 8
J 3
N 11
L 9
O 1
P 9
Q 1
R 3
T 12
V 4
24 rows selected.
### HAVING
The
HAVING clause filters rows resulting from the
GROUP BY clause based on the predicate(s) provided. For example, if you want to return only the regions that have a population of more than 500 million people, this cannot be specified in the
WHERE clause because the
WHERE clause is processed before the
GROUP BY clause. Hence, the
WHERE clause has no notion of the population of a region. This is where the
HAVING clause comes in. From a logical perspective, it behaves the same as the
WHERE clause, but it filters at a different processing stage:
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
|
SQL> SELECT r.name, SUM(c.population)
2 FROM regions r
3 JOIN countries c
4 ON (r.region_id=c.region_id)
5 GROUP BY r.name
6* HAVING SUM(c.population) > (500 * 1000 * 1000);
NAME SUM(C.POPULATION)
________________ ____________________
Africa 1263685000
Asia 4439011000
Europe 748985000
North America 575767000
### ORDER BY
The
ORDER BY clause sorts the resulting data. So far, the undefined sorting of the rows has worked out, except when it came to “countries per first letter.” The
ORDER BY clause can be used to return the rows in alphabetical order:
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
|
SQL> SELECT SUBSTR(name,1,1), COUNT(*)
2 FROM countries
3 GROUP BY SUBSTR(name,1,1)
4* ORDER BY SUBSTR(name,1,1);
SUBSTR(NAME,1,1) COUNT(*)
___________________ ___________
A 11
B 17
C 17
D 5
E 8
F 3
G 11
H 3
I 8
J 3
K 6
L 9
M 18
N 11
O 1
P 9
Q 1
R 3
S 26
T 12
U 7
V 4
Y 1
Z 2
24 rows selected.
By default, rows are sorted in ascending order, but you can reverse it with the
DESC (DESCENDING) keyword:
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
|
SQL> SELECT SUBSTR(name,1,1), COUNT(*)
2 FROM countries
3 GROUP BY SUBSTR(name,1,1)
4* ORDER BY SUBSTR(name,1,1) DESC;
SUBSTR(NAME,1,1) COUNT(*)
___________________ ___________
Z 2
Y 1
V 4
U 7
T 12
S 26
R 3
Q 1
P 9
O 1
N 11
M 18
L 9
K 6
J 3
I 8
H 3
G 11
F 3
E 8
D 5
C 17
B 17
A 11
24 rows selected.
### OFFSET
The
OFFSET clause specifies the number of rows to skip before starting to return data. This clause is shorthand for what would otherwise require analytic queries or subqueries. For example, asking “Give me all countries in South America ranked by square kilometers except the first three” can be answered with:
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
|
SQL> SELECT c.name, c.area_sq_km
2 FROM countries c
3 JOIN regions r
4 ON (c.region_id=r.region_id)
5 WHERE r.name = 'South America'
6 ORDER BY area_sq_km DESC
7* OFFSET 3 ROWS;
NAME AREA_SQ_KM
____________ _____________
Colombia 1138910
Bolivia 1098581
Venezuela 912050
Chile 756102
Paraguay 406752
Ecuador 283561
Guyana 214969
Uruguay 176215
Suriname 163820
9 rows selected.
### FETCH
The
FETCH clause specifies the number of rows to return from the result. Some databases call this the
LIMIT clause. Like the
OFFSET clause, this is also a shorthand and can be used to answer business questions like “What are the top three countries in terms of population?” This can be answered with:
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
SQL> SELECT name, population
2 FROM countries
3 ORDER BY population DESC
4* FETCH FIRST 3 ROWS ONLY;
NAME POPULATION
________________ _____________
China 1384689000
India 1296834000
United States 329256000
You may wonder what would happen if two rows tie on the third position; will both rows be returned? Or just the first? For these cases, the
FETCH clause provides the
ONLY and
WITH TIES keywords. The above just used
ONLY because it is unlikely that two countries have the same population.
However, when ranking countries by letter, there is much more room for overlap. For example, in the countries per first letter example, when ranked by number of countries, it is clear that some letters have the same number:
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
|
SQL> SELECT SUBSTR(name,1,1), COUNT(*)
2 FROM countries
3 GROUP BY SUBSTR(name,1,1)
4* ORDER BY COUNT(*) DESC;
SUBSTR(NAME,1,1) COUNT(*)
___________________ ___________
S 26
M 18
B 17
C 17
T 12
A 11
N 11
G 11
L 9
P 9
I 8
E 8
U 7
K 6
D 5
V 4
J 3
H 3
F 3
R 3
Z 2
Q 1
Y 1
O 1
24 rows selected.
If you run the same
FETCH clause on this query, the letter
C would be omitted from the results, although it has exactly the same number of countries as the letter
B:
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
|
SQL> SELECT SUBSTR(name,1,1), COUNT(*)
2 FROM countries
3 GROUP BY SUBSTR(name,1,1)
4 ORDER BY COUNT(*) DESC
5* FETCH FIRST 3 ROWS ONLY;
SUBSTR(NAME,1,1) COUNT(*)
___________________ ___________
S 26
M 18
B 17
This is where the
WITH TIES keyword comes in, as it will include ties in the results:
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
|
SQL> SELECT SUBSTR(name,1,1), COUNT(*)
2 FROM countries
3 GROUP BY SUBSTR(name,1,1)
4 ORDER BY COUNT(*) DESC
5* FETCH FIRST 3 ROWS WITH TIES;
SUBSTR(NAME,1,1) COUNT(*)
___________________ ___________
S 26
M 18
B 17
C 17
### OFFSET and FETCH
Combining the
OFFSET and FETCH clauses allow another nice shorthand that would otherwise require an analytical query or subquery. Consider the question “What is the second smallest country on the planet in terms of square kilometers?” This can be answered by combining
OFFSET to return results starting from the second row, and
FETCH to fetch just the second row:
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
|
SQL> SELECT name, area_sq_km
2 FROM countries
3 ORDER BY area_sq_km
4 OFFSET 1 ROW
5* FETCH FIRST 1 ROW ONLY;
NAME AREA_SQ_KM
_________ _____________
Monaco 2
## What’s Next?
My second article in this series will break down the anatomy of SQL’s data manipulation language (DML). You can find the data model used in this article and part two in my
[GitHub repository for this exercise](https://github.com/gvenzl/sample-data/tree/main/countries-cities-currencies). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)