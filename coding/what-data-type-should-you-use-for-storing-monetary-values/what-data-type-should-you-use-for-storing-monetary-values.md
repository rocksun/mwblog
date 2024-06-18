
<!--
title: 应该使用什么数据类型存储货币值？
cover: https://cdn.thenewstack.io/media/2024/06/18e770b7-monetary-value-data-type-1.jpg
-->

这是一个价值百万美元的问题：如何以最佳方式在数据库中处理多种货币的货币值？

> 译自 [What Data Type Should You Use for Storing Monetary Values?](https://thenewstack.io/what-data-type-should-you-use-for-storing-monetary-values/)，作者 Chris Saxon。

一些数据库有货币类型，但这些类型有局限性。例如，小数位数是固定的，并且值的货币可能取决于数据库设置。它们也特定于[数据库](https://thenewstack.io/data/)系统，这使得移植变得困难。你可以在数据库中创建一个用户定义的货币类型，但这有类似的挑战。

为了避免这些问题，你可以使用数字类型存储货币值。这只能部分解决问题。如果你处理多种货币，你需要存储：

- 货币金额。
- 此值的货币的 ISO 代码。
- 从此货币到通用货币的汇率。

例如：

```sql
create table product_prices ( 
  product_id    integer, 
  unit_price    number,
  currency_code char(3 char), 
  exchange_rate number  
);
```

这有帮助，但它有挑战。例如，你如何：

- 确保所有货币代码都是三个大写字母？
- 查找存储货币值的表和列？
- 在所有应用中使用相同的货币转换公式？

[Oracle Database 23ai](https://www.oracle.com/database/?source=:ex:pw:::::&SC=:ex:pw:::::&pcode=) 帮助你使用数据用例域来解决这些问题。这些增强了[SQL](https://thenewstack.io/how-to-write-sql-queries)标准域对象。使用域，你可以使用诸如默认值、约束和[注释](https://thenewstack.io/how-to-document-database-objects-with-annotations/)等属性扩展基本类型（例如number,date,char），用于数据用例。

当你将域应用于表列时，数据库会将域属性复制到表列。这有助于开发人员和应用以相同的方式处理所有表和应用程序中相同用例的值。

在 [SQL 标准](https://roadmap.sh/sql)中，域有一个值。Oracle Database 23ai 使你能够使用多列域将值分组在一起。你可以使用这些值创建包含货币值所有部分的货币域。

## 创建货币域

这将创建一个包含其货币金额、货币代码和到通用货币的汇率的货币域：

```sql
create usecase domain currency as (
  amount            as number(10,2),
  iso_currency_code as char(3 char) strict
    constraint curr_code_three_letters
    check ( regexp_like ( iso_currency_code, '^[A-Z]{3}$') ),
  exchange_rate     as number
    default 1
);
```

正则表达式 iso_currency_code 确保它只能存储三个大写字母。exchange_rate 的默认值假定 1:1 转换，即值已经以通用货币表示。

然后，你可以在创建或更改表列时将域与表列关联：

```sql
-- Apply currency domain to an existing table
alter table product_prices 
  modify ( unit_price, currency_code, exchange_rate )
  add domain currency;
 
-- Use currency domain when creating a table
create table order_items (
  order_id          integer, 
  product_id        integer,
  total_paid        number,        -- monetary value
  currency_code     char (3 char), -- monetary value
  usd_exchange_rate number,        -- monetary value
  domain currency ( total_paid, currency_code, usd_exchange_rate )
);
```

请注意，域和表列可以有不同的名称。要将域与表链接，所有域列都必须与相应的表列匹配，例如，两者都是 number,varchar2,timestamp 等。默认情况下，域和表列可以具有不同的长度、精度或比例。这允许你为特定列覆盖这些值。

例如，在货币域中，汇率是一个不受约束的number。你可以使用不同的 API 来获取产品价格和付款金额的汇率。这些 API 可能会为汇率提供不同的位数。

你可能希望汇率列与这些 API 提供的精度匹配。货币域让你可以灵活地做到这一点。

其他时候，值可以有固定的定义，例如 ISO 货币代码。这些被定义为三个字母的字符串，因此这些值的列都应包含三个字符。两个太少；四个太多。

这就是 iso_currency_code 上的 strict 子句的用武之地。这意味着域和表列之间必须有完全的类型匹配，例如，在此示例中，它们必须是char(3 char)。你还可以将其与char(N byte)关联，其中 N 是数据库字符集中每个字符的最大字节数。）尝试将 iso_currency_code 域与 char(2 char) 或 char(4 char) 的列链接，你将收到错误。

将货币与表关联也会将约束和默认值应用于该表。这可确保您只能在货币代码列中存储大写字母，并且如果您省略汇率，则汇率默认为 1：

```sql
insert into product_prices 
  values ( 1, 0.99, 'N/A', 1 );
ORA-11534: check constraint (CHRIS.SYS_C008450) involving column CURRENCY_CODE due to domain constraint CHRIS.CURR_CODE_THREE_LETTERS of domain CHRIS.CURRENCY violated
 
insert into product_prices ( 
  product_id, unit_price, currency_code
) values ( 1, 0.99, 'USD' );
 
select * from product_prices;
 
PRODUCT_ID UNIT_PRICE CUR EXCHANGE_RATE
---------- ---------- --- -------------
         1        .99 USD             1
```

使用多列域可确保所有货币值都具有金额、货币代码和汇率。您只需定义一次货币代码约束，即可减少出错的可能性。它还可以帮助您在数据库中找到所有货币值。

## 使用用例域查找货币列

货币值的表列可能具有许多不同的名称；例如：

- 金额可以是 transaction_value、unit_price 或 gross_amount。
- 货币代码可以是 currency_code、iso_currency 或 iso_currency_code。

很难知道具有相似名称的列是否存储相同数据用例的值。这可能导致处理它们的逻辑出现不必要的差异。

将货币域与表列关联可以清楚地表明它们都属于同一用例。要查找它们，您可以像这样查询数据字典中的 `domain_name` 列：

```sql
select table_name, column_name
from   user_tab_cols
where  domain_name = 'CURRENCY';
 
TABLE_NAME           COLUMN_NAME         
-------------------- --------------------
ORDER_ITEMS          TOTAL_PAID          
ORDER_ITEMS          CURRENCY_CODE       
ORDER_ITEMS          USD_EXCHANGE_RATE   
PRODUCT_PRICES       UNIT_PRICE          
PRODUCT_PRICES       CURRENCY_CODE       
PRODUCT_PRICES       EXCHANGE_RATE
```

这使得影响分析变得更加容易，并且可以帮助您检查是否以相同的方式处理所有货币值，无论列的名称如何。

不过，在不同应用程序中使用这些值时仍然存在挑战。例如，您如何确保它们在对值进行排序或显示时都使用相同的货币转换公式？

## 以通用货币对值进行排序和显示

如果您在同一表中存储多种货币的值，则仅按价格或金额排序会产生误导性结果。日元 (JPY) 和印度卢比 (INR) 等货币是美元或欧元的许多倍数。因此，即使 JPY 和 INR 在转换为相同货币后金额较小，它们的行也会出现在排序结果的底部。

为了克服这个问题，首先将值转换为通用货币。然后按标准化值排序。

这可能是一个常见的操作。重复转换会导致细微的差异，例如将值四舍五入到多少位小数。

数据用例域使您能够在域本身中使用排序和显示表达式集中化此逻辑。

例如，您可以将转换公式定义为：

```
amount * exchange_rate
```

您可以像这样将此内容作为排序表达式添加到货币域：

```
alter domain currency 
  add order amount * exchange_rate;
```

要激活它，请将域列传递给 `domain_order`：

```sql
insert into order_items
values (1, 1,    9.99, 'USD', 1 ),
       (2, 2,    8.99, 'GBP', 1.27 ),
       (3, 3,    8.99, 'EUR', 1.09 ),
       (4, 4, 1399,    'JPY', 0.00697 ),
       (5, 5,  110.20, 'NOK', 0.09062 );
 
select order_id, product_id, 
       total_paid, currency_code, usd_exchange_rate
from   order_items
order  by domain_order ( total_paid, currency_code, usd_exchange_rate );
 
  ORDER_ID PRODUCT_ID TOTAL_PAID CUR USD_EXCHANGE_RATE
---------- ---------- ---------- --- -----------------
         4          4    1399.00 JPY            .00697
         3          3       8.99 EUR              1.09
         5          5     110.20 NOK            .09062
         1          1       9.99 USD                 1
         2          2       8.99 GBP              1.27
```

此时，输出更加混乱——`total_paid` 值的顺序似乎是随机的！为避免这种情况，请将转换后的金额添加到输出中。

您可以使用排序表达式以通用货币显示值来执行此操作。但您可能需要额外的格式，例如：

- 将值四舍五入到两位小数。
- 添加小数和千位分隔符。
- 显示原始值的货币代码。

为此，请向域添加显示表达式：

```sql
alter domain currency 
  add display '(' || iso_currency_code || ')' || 
      to_char ( round ( amount * exchange_rate, 2 ), '999G999G990D00' );
```

然后通过调用 `domain_display` 函数激活它：

```sql
select order_id, product_id, 
       domain_display ( total_paid, currency_code, usd_exchange_rate ) usd_value
from   order_items
order  by domain_order ( total_paid, currency_code, usd_exchange_rate );
 
  ORDER_ID PRODUCT_ID USD_VALUE           
---------- ---------- --------------------
         4          4 (JPY)           9.75
         3          3 (EUR)           9.80
         5          5 (NOK)           9.99
         1          1 (USD)           9.99
         2          2 (GBP)          11.42
```

在域上定义顺序和显示表达式意味着您只需编写一次此逻辑。所有读取域数据的应用程序都可以通过调用 `domain_order` 和 `domain_display` 函数来使用它们。这意味着您可以编写更少的代码，并为所有应用程序中的常见数据规则标准化逻辑。

## 使用用例域描述数据意图

所有数据库系统都有数字、日期和字符串的类型。这些类型灵活，支持广泛的用例。但是，将值存储在这些基本类型中意味着您会丢失存储在这些列中的值的用例上下文。这使得使用复合值（如货币金额）变得具有挑战性，因为您需要所有部分来描述它们。

为了解决这个问题，一些数据库针对特定用例（如货币）提供了自定义数据类型，或者允许您创建用户定义类型。但这些类型不灵活；很容易达到它们的限制，这使得它们不适用于广泛使用。

[Oracle Database 23ai](https://blogs.oracle.com/database/post/oracle-23ai-now-generally-available) 中的数据用例域为您提供了两全其美的优势。这些值是基本类型，因此它们支持所有标准操作，无需特殊处理。

同时，域提供了与自定义类型相关的优势：

- 查找数据用例的所有列。
- 为用例一次性定义约束、默认值和其他属性。
- 为显示和排序值编写标准表达式。

要查看这些操作，请下载 [Oracle Database 23ai Free](https://www.oracle.com/database/free/?source=:ex:pw:::::&SC=:ex:pw:::::&pcode=) 或立即在 Oracle Cloud Infrastructure 上创建 [Always Free Oracle Autonomous Database](https://www.oracle.com/cloud/free/?source=:ex:pw:::::TheNewStack_D&SC=:ex:pw:::::TheNewStack_D&pcode=) 。
