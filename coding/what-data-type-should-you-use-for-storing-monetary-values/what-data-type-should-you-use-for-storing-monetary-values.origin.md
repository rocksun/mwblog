# What Data Type Should You Use for Storing Monetary Values?
![Featued image for: What Data Type Should You Use for Storing Monetary Values?](https://cdn.thenewstack.io/media/2024/06/18e770b7-monetary-value-data-type-1-1024x576.jpg)
Some databases have a
money type, but these have limitations. For example, the number of decimal digits is fixed and the currency for the values may depend on database settings. They’re also specific to the
[database](https://thenewstack.io/data/) system, which makes porting difficult. You could create a user-defined money type in your database, but this has similar challenges.
To avoid these issues, you can store monetary values using a numeric type. This only partly solves the problem. If you’re dealing with many currencies, you need to store:
- The monetary amount.
- The ISO code of the currency for this value.
- The exchange rate from this currency to a common currency.
For example:
|
1
2
3
4
5
6
|
create table product_prices (
product_id integer,
unit_price number,
currency_code char(3 char),
exchange_rate number
);
This helps, but it has challenges. For example, how do you:
- Ensure all currency codes are three uppercase letters?
- Find all the tables and columns storing monetary values?
- Use the same formulas for currency conversion across apps?
[Oracle Database 23ai](https://www.oracle.com/database/?source=:ex:pw:::::&SC=:ex:pw:::::&pcode=) helps you address these with data use case domains. These enhance [SQL](https://thenewstack.io/how-to-write-sql-queries) standard domain objects. With domains, you can extend base types (e.g.,
number,
date,
char) with properties like defaults, constraints and
[annotations](https://thenewstack.io/how-to-document-database-objects-with-annotations/) for a data use case.
When you apply a domain to table columns, the database copies the domain properties to the table columns. This helps developers and apps handle values for the same use case in the same way across all tables and applications.
In the
[SQL standard](https://roadmap.sh/sql), a domain has one value. Oracle Database 23ai enables you to group values together with multicolumn domains. You can use these to create a currency domain with all the parts of monetary values.
## Create a Currency Domain
This creates a currency domain containing its monetary amount, currency code and exchange rate to a common currency:
|
1
2
3
4
5
6
7
8
|
create usecase domain currency as (
amount as number(10,2),
iso_currency_code as char(3 char) strict
constraint curr_code_three_letters
check ( regexp_like ( iso_currency_code, '^[A-Z]{3}$') ),
exchange_rate as number
default 1
);
The regular expression for
iso_currency_code ensures it can only store three uppercase letters. The default on
exchange_rate assumes a 1:1 conversion, i.e., the values are already in the common currency.
You can then associate the domain with table columns when making or changing them:
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
-- Apply currency domain to an existing table
alter table product_prices
modify ( unit_price, currency_code, exchange_rate )
add domain currency;
-- Use currency domain when creating a table
create table order_items (
order_id integer,
product_id integer,
total_paid number, -- monetary value
currency_code char (3 char), -- monetary value
usd_exchange_rate number, -- monetary value
domain currency ( total_paid, currency_code, usd_exchange_rate )
);
Note the domain and table columns can have different names. To link a domain with a table, all the domain columns must match the corresponding table columns, e.g., both are a
number,
varchar2,
timestamp, etc. By default, domain and table columns can have a different length, precision or scale. This allows you to override these for a particular column.
For example, in the currency domain, the exchange rate is an unconstrained
number. You can use different APIs to get the exchange rates for product prices and payment amounts. These APIs may supply a different number of decimal digits for the rate.
You might want the exchange-rate columns to match the precision these APIs provide. The currency domain gives you the flexibility to do this.
Other times a value can have a fixed definition, such as the ISO currency codes. These are defined as three-letter strings, so all columns for these values should hold three characters. Two is too few; four is too many.
This is where the
strict clause on
iso_currency_code comes in. This means there must be an exact type match between the domain and table columns, e.g., in this example, they must be
char(3 char). You can also associate it with
char(N byte), where N is the maximum number of bytes per character in your database’s character set.) Try to link the
iso_currency_code domain with columns of
char(2 char) or
char(4 char), and you’ll get an error.
Associating currency with a table also applies its constraints and defaults to the table. This ensures you can only store uppercase letters in currency code columns and the exchange rate defaults to 1 if you omit it:
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
insert into product_prices
values ( 1, 0.99, 'N/A', 1 );
ORA-11534: check constraint (CHRIS.SYS_C008450) involving column CURRENCY_CODE due to domain constraint CHRIS.CURR_CODE_THREE_LETTERS of domain CHRIS.CURRENCY violated
insert into product_prices (
product_id, unit_price, currency_code
) values ( 1, 0.99, 'USD' );
select * from product_prices;
PRODUCT_ID UNIT_PRICE CUR EXCHANGE_RATE
---------- ---------- --- -------------
1 .99 USD 1
Using a multicolumn domain ensures all monetary values have an amount, currency code and exchange rate. You need to define the currency code constraint just once, reducing the chance of mistakes. It also helps you find where all the monetary values are in your database.
## Find Currency Columns with Use Case Domains
Table columns for monetary values may have many different names; for example:
- The amount could be
transaction_value,
unit_priceor
gross_amount.
- The currency code could be
currency_code,
iso_currencyor
iso_currency_code.
It’s tricky to know whether columns with similar names store values for the same data use case. This can lead to unwanted differences in the logic to handle them.
Associating the currency domain with table columns makes it clear they all belong to the same use case. To find them, you can query the
domain_name columns in the data dictionary like so:
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
select table_name, column_name
from user_tab_cols
where domain_name = 'CURRENCY';
TABLE_NAME COLUMN_NAME
-------------------- --------------------
ORDER_ITEMS TOTAL_PAID
ORDER_ITEMS CURRENCY_CODE
ORDER_ITEMS USD_EXCHANGE_RATE
PRODUCT_PRICES UNIT_PRICE
PRODUCT_PRICES CURRENCY_CODE
PRODUCT_PRICES EXCHANGE_RATE
This makes impact analysis easier and helps you check that you’re handling all currency values in the same way, regardless of what the columns are named.
There are still challenges when using these values across different apps though. For example, how do you ensure they all use the same formula for currency conversion when sorting or displaying the values?
## Sort and Show Values in a Common Currency
If you store values for many currencies in the same table, sorting by the price or amount alone gives misleading results. Currencies like Japanese yen (JPY) and Indian rupees (INR) are many multiples of US dollars or euros. So the rows for JPY and INR will appear toward the bottom in sorted results, even if they are a smaller amount when converted to the same currency.
To overcome this, first convert the values to a common currency. Then sort by the standardized value.
This is likely to be a common operation. Repeating the conversion can lead to small differences such as how many decimal places you round the values to.
Data use-case domains enable you to centralize this logic in the domain itself with order and display expressions.
For example, you may define the conversion formula as:
|
1
|
amount * exchange_rate
You can add this as an order expression to the currency domain like this:
|
1
2
|
alter domain currency
add order amount * exchange_rate;
To activate it, pass the domain columns to
domain_order:
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
|
insert into order_items
values (1, 1, 9.99, 'USD', 1 ),
(2, 2, 8.99, 'GBP', 1.27 ),
(3, 3, 8.99, 'EUR', 1.09 ),
(4, 4, 1399, 'JPY', 0.00697 ),
(5, 5, 110.20, 'NOK', 0.09062 );
select order_id, product_id,
total_paid, currency_code, usd_exchange_rate
from order_items
order by domain_order ( total_paid, currency_code, usd_exchange_rate );
ORDER_ID PRODUCT_ID TOTAL_PAID CUR USD_EXCHANGE_RATE
---------- ---------- ---------- --- -----------------
4 4 1399.00 JPY .00697
3 3 8.99 EUR 1.09
5 5 110.20 NOK .09062
1 1 9.99 USD 1
2 2 8.99 GBP 1.27
At this point, the output is more confusing — the order for the
total_paid values appears random! To avoid this, add the converted amount to the output.
You could do this using the order expression to display the values in a common currency. But it’s likely you want extra formatting, such as:
- Rounding the values to two decimal places.
- Adding decimal and thousands separators.
- Displaying the currency code of the original value.
To do this, add a display expression to the domain:
|
1
2
3
|
alter domain currency
add display '(' || iso_currency_code || ')' ||
to_char ( round ( amount * exchange_rate, 2 ), '999G999G990D00' );
Then activate it by calling the
domain_display function:
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
select order_id, product_id,
domain_display ( total_paid, currency_code, usd_exchange_rate ) usd_value
from order_items
order by domain_order ( total_paid, currency_code, usd_exchange_rate );
ORDER_ID PRODUCT_ID USD_VALUE
---------- ---------- --------------------
4 4 (JPY) 9.75
3 3 (EUR) 9.80
5 5 (NOK) 9.99
1 1 (USD) 9.99
2 2 (GBP) 11.42
Defining order and display expressions on a domain means you code this logic once. All applications reading domain data can use them by calling the
domain_order and
domain_display functions. This means you can write less code and standardize the logic for common data rules across all your apps.
## Describe Data Intent with Use-Case Domains
All database systems have types for numbers, dates and strings. These are flexible and support a wide range of use cases. But storing values in these base types means you lose the use case context for values stored in these columns. This makes working with composite values like monetary amounts challenging where you need all the parts to describe them.
To help with this, some databases have custom data types for specific use cases such as
money or enable you to create user-defined types. But these are inflexible; it’s easy to hit their limitations, making them impractical for widespread use.
Data use-case domains in
[Oracle Database 23ai](https://blogs.oracle.com/database/post/oracle-23ai-now-generally-available) give you the best of both worlds. The values are base types, so they support all standard operations and need no special handling.
At the same time, domains give advantages associated with custom types:
- Find all the columns for a data use case.
- Define constraints, defaults and other properties for a use case once.
- Write standard expressions for showing and sorting values.
To see these in action, download
[Oracle Database 23ai Free](https://www.oracle.com/database/free/?source=:ex:pw:::::&SC=:ex:pw:::::&pcode=) or create an [Always Free Oracle Autonomous Database](https://www.oracle.com/cloud/free/?source=:ex:pw:::::TheNewStack_D&SC=:ex:pw:::::TheNewStack_D&pcode=) on Oracle Cloud Infrastructure today. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)