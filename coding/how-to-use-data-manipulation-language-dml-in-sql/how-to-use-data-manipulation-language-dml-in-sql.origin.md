# How to Use Data Manipulation Language (DML) in SQL
![Featued image for: How to Use Data Manipulation Language (DML) in SQL](https://cdn.thenewstack.io/media/2024/03/74b34769-use-dml-sql-1024x576.jpg)
SQL is generally seen as one of the best high-level programming languages for analyzing and manipulating data due to its easy-to-learn syntax. It’s a declarative language, so users declare what results they want, rather than how to get the results, like imperative languages such as C, Java and Python. It’s also easy to read, because its syntax is
[similar to the English language](https://thenewstack.io/how-to-make-sql-easier-to-understand-test-and-maintain/).
In the first part of this series, I broke down the
[syntax used for SQL queries](https://thenewstack.io/how-to-write-sql-queries/). In this article, I’ll discuss the anatomy of SQL’s Data Manipulation Language (DML), which as you’d expect, is used to manipulate data.
## Defining DML Elements
The Data Manipulation Language is a set of SQL statements used to add, update, and delete data. SQL used for
[data manipulation](https://thenewstack.io/data/) uses
INSERT,
UPDATE,
DELETE and
MERGE statements.
INSERT: Inserts data in a table by adding one or more rows to a table.
UPDATE: Updates one or more rows in a table.
DELETE: Deletes one or more rows from a table.
MERGE: Can be used to add (insert) new rows, update existing rows or delete data in a table, depending on whether the specified condition matches. It is a convenient way to execute one operation, where you would otherwise have to execute multiple
INSERTor
UPDATEstatements.
## Using DML
Now that you’re familiar with what the various DML statements mean, you can start using them. You can follow along with these exercises using the data model in my
[GitHub repository](https://github.com/gvenzl/sample-data/tree/main/countries-cities-currencies).
### INSERT INTO
The
INSERT INTO statement adds rows to a table. It can be used by either defining one or more rows using the
VALUES clause or by inserting the result of a subquery. Take a look at the
VALUES clause first:
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
|
SQL> -- Creates an empty copy of countries called my_tab
SQL> CREATE TABLE my_tab AS SELECT * FROM countries WHERE rownum=0;
Table MY_TAB created.
SQL> INSERT INTO my_tab (country_id, country_code, name, population, region_id)
2* VALUES (1, 'GV', 'State of Gerald', 1, 'AN');
1 row inserted.
SQL> SELECT * FROM my_tab;
COUNTRY_ID COUNTRY_CODE NAME OFFICIAL_NAME POPULATION AREA_SQ_KM LATITUDE LONGITUDE TIMEZONE REGION_ID
_____________ _______________ __________________ ________________ _____________ _____________ ___________ ____________ ___________ ____________
1 GV State of Gerald 1
The
VALUES clause allows multiple rows to be defined by separating them with a comma (
,):
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
SQL> INSERT INTO my_tab (country_id, country_code, name, population, region_id)
2 VALUES (2, 'VX', 'Venzi Country', 1, 'AN'),
3* (3, 'XX', 'Gerald Island', 1, 'AN');
2 rows inserted.
SQL> SELECT * FROM my_tab;
COUNTRY_ID COUNTRY_CODE NAME OFFICIAL_NAME POPULATION AREA_SQ_KM LATITUDE LONGITUDE TIMEZONE REGION_ID
_____________ _______________ __________________ ________________ _____________ _____________ ___________ ____________ ___________ ____________
1 GV State of Gerald 1 AN
2 VX Venzi Country 1 AN
3 XX Gerald Island 1
To use a SQL query as input for the
INSERT statement, just replace
VALUES with
SELECT. The columns of your table and the
SELECT list must match:
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
|
SQL> INSERT INTO my_tab SELECT * FROM countries;
196 rows inserted.
SQL> SELECT *
2 FROM my_tab
3* FETCH FIRST 5 ROWS ONLY;
COUNTRY_ID COUNTRY_CODE NAME OFFICIAL_NAME POPULATION AREA_SQ_KM LATITUDE LONGITUDE TIMEZONE REGION_ID
_____________ _______________ ___________________________________ ___________________________________ _____________ _____________ ___________ ____________ _____________________ ____________
VAT VA Vatican City Vatican City State 1000 0.44 41.90225 12.4533 Europe/Vatican EU
VCT VC Saint Vincent and the Grenadines 102000 389 13.08333 -61.2 America/St_Vincent NA
VEN VE Venezuela Bolivarian Republic of Venezuela 31689000 912050 8 -66 America/Caracas SA
VNM VN Vietnam Socialist Republic of Vietnam 97040000 331210 16.16667 107.83333 Asia/Ho_Chi_Minh AS
VUT VU Vanuatu Republic of Vanuatu 288000 12189 -16 167 Pacific/Efate OC
### Update
The
UPDATE statement updates entries in a table. It has a
SET clause that sets columns to a given value and a
WHERE clause to specify which rows to update. You almost always want a
WHERE clause for your
UPDATE statement; otherwise, the
UPDATE statement will update all rows in the table.
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
SQL> UPDATE my_tab
2 SET population = 2
3* WHERE country_code = 'GV';
1 row updated.
SQL> SELECT *
2 FROM my_tab
3* WHERE country_code = 'GV';
COUNTRY_ID COUNTRY_CODE NAME OFFICIAL_NAME POPULATION AREA_SQ_KM LATITUDE LONGITUDE TIMEZONE REGION_ID
_____________ _______________ __________________ ________________ _____________ _____________ ___________ ____________ ___________ ____________
1 GV State of Gerald 2
The
UPDATE statement can also join other tables to update rows based on a
WHERE clause condition outside of the table that is being updated. For example, say you want to adjust the population of all countries in South America by 10% more (an expression formulated as
population*1.1). You can filter the rows to update based on a filter via the
regions table for the
countries that have the appropriate
region_id for South America:
|
1
2
3
4
5
6
7
|
SQL> UPDATE countries c
2 SET c.population = c.population*1.1
3 FROM regions r
4 WHERE c.region_id=r.region_id
5* AND r.name = 'South America';
12 rows updated.
### DELETE
The
DELETE statement deletes rows in a table and works very similarly to the
UPDATE statement. As with
UPDATE, with the
DELETE statement you almost always want a
WHERE clause; otherwise, you will delete all rows in a table.
|
1
2
3
4
|
SQL> DELETE FROM my_tab
2* WHERE country_code = 'GV';
1 rows deleted.
Also like the
UPDATE statement, you can apply the same filter based on other tables’ column values:
|
1
2
3
4
5
6
|
SQL> DELETE FROM my_tab c
2 FROM regions r
3 WHERE r.region_id=c.region_id
4* AND r.name = 'Antarctica';
2 rows deleted.
### MERGE
The
MERGE statement is more sophisticated than the
INSERT,
UPDATE and
DELETE statements. The
MERGE statement allows you to conditionally insert or update (and even delete some) rows with one execution. This is most helpful when you want to load data into tables with existing rows and, for example, do not want to manually check whether a given row already exists. If it does, you would need to issue an
UPDATE statement or an
INSERT statement otherwise. Instead, you can write one statement with a matching condition that will do the
INSERT or
UPDATE automatically for you.
Imagine every night you get a file with updated data from all the countries in the world. Some countries may have reported new population numbers, and very occasionally a new country is formed. Instead of running a bunch of
UPDATE statements and rerunning the corresponding
INSERT statement only when an
UPDATE statement returns 0 rows updated, you can do both with one
MERGE statement.
First, load all the data into an empty staging table (in this example,
my_tab), and from there run the
MERGE statement to merge the data into the target table (in this example, the
countries table):
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
SQL> MERGE INTO countries c
2 USING my_tab m
3 ON (c.country_id=m.country_id)
4 WHEN NOT MATCHED THEN
5 INSERT VALUES (m.country_id, m.country_code, m.name, m.official_name, m.population, m.area_sq_km, m.latitude, m.longitude, m.timezone, m.region_id)
6 WHEN MATCHED THEN
7* UPDATE SET c.population=m.population;
196 rows merged.
The statement above merges data into the
countries table based on matching
country_id (primary key) values. If the
countries table includes a row with the same
country_id value as the
my_tab table, then the statement just updates the
population column (as seen within the
WHEN MATCHED THEN UPDATE clause). If the
MERGE statement doesn’t find a corresponding row with the same
country_id values in the
countries table, then it inserts the row with all the fields into the
countries table.
The
MERGE statement also provides some flexibility. Say that you just want to update the
countries table but never insert into it. You can just omit the
WHEN NOT MATCHED INSERT clause:
|
1
2
3
4
5
6
7
|
SQL> MERGE INTO countries c
2 USING my_tab m
3 ON (c.country_id=m.country_id)
4 WHEN MATCHED THEN
5* UPDATE SET c.population=m.population;
196 rows merged.
## Conclusion
SQL is a powerful, widely adopted, declarative language for data processing and data manipulation. Understanding the core components of SQL and how it operates is the first step to unleashing its power on your data. You can find the data model used in this article and
[part one](https://thenewstack.io/how-to-write-sql-queries/) in my [GitHub repository for this exercise](https://github.com/gvenzl/sample-data/tree/main/countries-cities-currencies). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)