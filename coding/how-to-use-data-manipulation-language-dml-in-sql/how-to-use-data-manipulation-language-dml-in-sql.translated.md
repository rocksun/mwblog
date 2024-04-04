## 如何在 SQL 中使用数据操作语言 (DML)

![如何使用 SQL 中的数据操作语言 (DML) 的特色图片](https://cdn.thenewstack.io/media/2024/03/74b34769-use-dml-sql-1024x576.jpg)

由于 SQL 具有易于学习的语法，因此它通常被视为用于分析和操作数据的最佳高级编程语言之一。它是一种声明式语言，因此用户声明他们想要的结果，而不是像 C、Java 和 Python 等命令式语言那样声明如何获取结果。它还易于阅读，因为它的语法类似于英语。

在本系列的第一部分中，我分解了用于 SQL 查询的语法。在本文中，我将讨论 SQL 的数据操作语言 (DML) 的解剖结构，正如你所料，它用于操作数据。

## 定义 DML 元素

数据操作语言是一组用于添加、更新和删除数据的 SQL 语句。用于数据操作的 SQL 使用 INSERT、UPDATE、DELETE 和 MERGE 语句。

- **INSERT：**通过向表中添加一行或多行来插入表中的数据。
- **UPDATE：**更新表中的一行或多行。
- **DELETE：**从表中删除一行或多行。
- **MERGE：**可用于添加（插入）新行、更新现有行或删除表中的数据，具体取决于指定的条件是否匹配。这是一种执行一项操作的便捷方式，否则你将不得不执行多个 INSERT 或 UPDATE 语句。

## 使用 DML

既然你已经熟悉了各种 DML 语句的含义，就可以开始使用它们了。你可以使用我的 GitHub 存储库中的数据模型来完成这些练习。

### INSERT INTO

INSERT INTO 语句向表中添加行。可以通过使用 VALUES 子句定义一行或多行或通过插入子查询的结果来使用它。首先查看 VALUES 子句：

```sql
SQL> -- 创建一个名为 my_tab 的国家/地区空副本
SQL> CREATE TABLE my_tab AS SELECT * FROM countries WHERE rownum=0;
创建表 MY_TAB。
SQL> INSERT INTO my_tab (country_id, country_code, name, population, region_id)
2* VALUES (1, 'GV', 'State of Gerald', 1, 'AN');
插入 1 行。
SQL> SELECT * FROM my_tab;
COUNTRY_ID COUNTRY_CODE NAME OFFICIAL_NAME POPULATION AREA_SQ_KM LATITUDE LONGITUDE TIMEZONE REGION_ID
_____________ _______________ __________________ ________________ _____________ _____________ ___________ ____________ ___________ ____________
1 GV State of Gerald 1
```

VALUES 子句允许通过逗号 (,) 将多行分隔开来进行定义：

```sql
SQL> INSERT INTO my_tab (country_id, country_code, name, population, region_id)
2 VALUES (2, 'VX', 'Venzi Country', 1, 'AN'),
3* (3, 'XX', 'Gerald Island', 1, 'AN');
插入 2 行。
SQL> SELECT * FROM my_tab;
COUNTRY_ID COUNTRY_CODE NAME OFFICIAL_NAME POPULATION AREA_SQ_KM LATITUDE LONGITUDE TIMEZONE REGION_ID
_____________ _______________ __________________ ________________ _____________ _____________ ___________ ____________ ___________ ____________
1 GV State of Gerald 1 AN
2 VX Venzi Country 1 AN
3 XX Gerald Island 1
```

要将 SQL 查询用作 INSERT 语句的输入，只需将 VALUES 替换为 SELECT。表的列和 SELECT 列表必须匹配：

```sql
SQL> INSERT INTO my_tab SELECT * FROM countries;
插入 196 行。
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
```

### 更新

UPDATE 语句更新表中的条目。它有一个 SET 子句，将列设置为给定值，还有一个 WHERE 子句来指定要更新哪些行。你几乎总是希望为 UPDATE 语句使用 WHERE 子句；否则，UPDATE 语句将更新表中的所有行。

```sql
SQL> UPDATE my_tab
2 SET population = 2
3* WHERE country_code = 'GV';
更新 1 行。
SQL> SELECT *
2 FROM my_tab
3* WHERE country_code = 'GV';
COUNTRY_ID COUNTRY_CODE NAME OFFICIAL_NAME POPULATION AREA_SQ_KM LATITUDE LONGITUDE TIMEZONE REGION_ID
_____________ _______________ __________________ ________________ _____________ _____________ ___________ ____________ ___________ ____________
1 GV State of Gerald 2
```
## UPDATE

UPDATE 语句还可以联接其他表，以根据表外部的 WHERE 子句条件来更新行。例如，假设您想将南美洲所有国家的总人口调整为增加 10%（表达式为 population*1.1）。您可以通过 regions 表对国家/地区进行筛选，以更新具有南美洲相应 region_id 的国家/地区：

```sql
UPDATE countries c
SET c.population = c.population*1.1
FROM regions r
WHERE c.region_id=r.region_id
AND r.name = 'South America';
```

12 行已更新。

### DELETE

DELETE 语句用于删除表中的行，其工作方式与 UPDATE 语句非常相似。与 UPDATE 一样，使用 DELETE 语句时几乎总是需要一个 WHERE 子句；否则，您将删除表中的所有行。

```sql
DELETE FROM my_tab
WHERE country_code = 'GV';
```

1 行已删除。

与 UPDATE 语句类似，您还可以根据其他表的列值应用相同的筛选器：

```sql
DELETE FROM my_tab c
FROM regions r
WHERE r.region_id=c.region_id
AND r.name = 'Antarctica';
```

2 行已删除。

### MERGE

MERGE 语句比 INSERT、UPDATE 和 DELETE 语句更复杂。MERGE 语句允许您有条件地插入或更新（甚至删除一些）行，只需执行一次。当您想将数据加载到具有现有行的表中时，此功能非常有用，例如，您不想手动检查给定行是否已存在。如果已存在，则需要发出 UPDATE 语句或 INSERT 语句。相反，您可以编写一条带有匹配条件的语句，它将自动为您执行 INSERT 或 UPDATE。

想象一下，您每晚都会收到一个包含来自世界所有国家/地区的更新数据的文件。一些国家/地区可能报告了新的总人口数，而且偶尔会形成一个新国家/地区。您可以使用一条 MERGE 语句同时执行大量 UPDATE 语句和仅在 UPDATE 语句返回 0 行已更新时重新运行相应的 INSERT 语句。

首先，将所有数据加载到一个空的暂存表中（在本例中为 my_tab），然后从该表运行 MERGE 语句，将数据合并到目标表中（在本例中为 countries 表）：

```sql
MERGE INTO countries c
USING my_tab m
ON (c.country_id=m.country_id)
WHEN NOT MATCHED THEN
INSERT VALUES (m.country_id, m.country_code, m.name, m.official_name, m.population, m.area_sq_km, m.latitude, m.longitude, m.timezone, m.region_id)
WHEN MATCHED THEN
UPDATE SET c.population=m.population;
```

196 行已合并。

上面的语句根据匹配的 country_id（主键）值将数据合并到 countries 表中。如果 countries 表包含与 my_tab 表具有相同 country_id 值的行，则该语句只会更新 population 列（如 WHEN MATCHED THEN UPDATE 子句中所示）。如果 MERGE 语句在 countries 表中找不到具有相同 country_id 值的相应行，则它会将具有所有字段的行插入到 countries 表中。

MERGE 语句还提供了一些灵活性。假设您只想更新 countries 表，但从不向其中插入数据。您可以省略 WHEN NOT MATCHED INSERT 子句：

```sql
MERGE INTO countries c
USING my_tab m
ON (c.country_id=m.country_id)
WHEN MATCHED THEN
UPDATE SET c.population=m.population;
```

196 行已合并。

## 结论

SQL 是一种功能强大、被广泛采用的声明式语言，用于数据处理和数据操作。了解 SQL 的核心组件及其操作方式是释放其在数据上强大功能的第一步。您可以在本文和 [第一部分](https://thenewstack.io/how-to-write-sql-queries/) 中找到用于此练习的数据模型，并可以在我的 [GitHub 存储库](https://github.com/gvenzl/sample-data/tree/main/countries-cities-currencies) 中找到此练习。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。