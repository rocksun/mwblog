# A Developer’s Guide to Server-Side JavaScript
![Featued image for: A Developer’s Guide to Server-Side JavaScript](https://cdn.thenewstack.io/media/2025/04/44147507-modules-1024x613.jpg)
Developers resort to databases for storing, retrieving and manipulating data whenever applications need to handle state. This approach isn’t debated anymore; using databases for your persistence layer is a proven, mature approach. However, the follow-up decision has been fiercely discussed for decades: Where should you place your application’s business logic?

**Client-Side vs. Server-Side Business Logic**
On the one hand, developers like to be in control, performing all operations concerning the application’s data in the frontend. Writing stored code in the database requires knowledge of SQL and the procedural language your database supports. Whether that’s PL/SQL, T-SQL or PL/pgSQL, a [React developer](https://roadmap.sh/react) might not be familiar with it. [Writing business logic in the same language](https://thenewstack.io/3-foundational-principles-for-writing-efficient-sql/) as the [frontend](https://thenewstack.io/introduction-to-frontend-development/) (or [microservice](https://thenewstack.io/microservices/)) comes naturally.

The proponents of stored code executed within the database rightly point out that duplicating database functionality inside the application — ensuring atomicity, consistency, isolation and durability — is redundant. Consider the duplication of effort across many applications and you will become painfully aware of the extra effort spent. Furthermore, issues might arise regarding data quality, governance, auditing and so on. And you haven’t even talked about the performance benefits of well-written stored code yet.

This discussion appears to have reached a stalemate if you follow social media and websites like Reddit and Stack Overflow.

Wouldn’t having the best of both worlds be nice — a familiar programming language to write your business logic, plus all the benefits of running the code where the data resides? JavaScript, for example, is one of the most popular languages. Oracle Database 23ai is among the databases supporting server-side [JavaScript](https://thenewstack.io/javascript/) based on the hugely popular GraalVM. MySQL is a good example of such a database management system.

Let’s take a look at how developers can write server-side JavaScript in Oracle Database 23ai.

**What Is Multilingual Engine and How Do You Use It?**
[Multilingual Engine](https://docs.oracle.com/en/database/oracle/oracle-database/23/mlejs/introduction-to-mle.html?source=:ex:pw:::::TNS_MLE_A&SC=:ex:pw:::::TNS_MLE_A&pcode=), or MLE for short, allows developers to store and execute JavaScript code inside the Oracle database. It implements the ECMAScript 2023 standard and has many [built-in functions](https://oracle-samples.github.io/mle-modules/).
You can use existing JavaScript modules from a content delivery network or write your code just as you would in PL/SQL. Using existing modules can significantly speed up development, provided the module’s license is compatible with your project and no other compliance issues prevent its use.

**Use Case No. 1: ****Embed Third-Party Modules in Your App**
A common database task is to validate input to help ensure data quality. The popular [validator library](https://github.com/validatorjs/validator.js) provides a plethora of string validation methods. Let’s assume that your task at hand is to validate email addresses. Using JavaScript, that’s simple.

Start by downloading the `validatorjs`
module from your favorite CDN. The following example has been run on MacOS; you might have to adapt the `curl`
arguments for Windows.

1 |
curl -Lo validator-13.12.0.js 'https://cdn.jsdelivr.net/npm/validator@13.12.0/+esm' |
[Oracle’s SQL Developer Command Line](https://www.oracle.com/database/sqldeveloper/technologies/sqlcl/?source=:ex:pw:::::TNS_MLE_B&SC=:ex:pw:::::TNS_MLE_B&pcode=) (SQLcl) offers the most convenient way to deploy the JavaScript module to the database. The following SQLcl command creates a new module named `validator_module`
in the database based on the downloaded file’s contents. It’s good practice to also provide the module version.
1 |
mle create-module -filename validator-13.12.0.js -module-name validator_module -version 13.12.0 |
The module is created as a new schema object; its properties are available in the data dictionary. Before you can use it in SQL and PL/SQL, you must create a so-called [call specification](https://docs.oracle.com/en/database/oracle/oracle-database/23/mlejs/call-specifications-functions.html?source=:ex:pw:::::TNS_MLE_C&SC=:ex:pw:::::TNS_MLE_C&pcode=#GUID-D0C14B08-5B84-4127-8DE7-F56043F79630). According to [its documentation](https://github.com/validatorjs/validator.js/blob/master/README.md), `validatorjs`
offers a function named `isEmail`
that does precisely what is needed: validate whether a string is an email address. Let’s expose the function to SQL:
123456789101112131415161718192021222324252627 |
create function is_email(p_string varchar2)return boolean as mle module validator_module signature 'default.isEmail';/That’s all there is to it. Let’s validate some strings:SQL> with sample_data (email_address) as ( 2 values 3 ('not a valid email address'), 4 ('user@domain.com'), 5 ('user@'), 6 ('user~~name@domain.com') 7 ) 8 select 9 email_address, 10 is_email(email_address) valid_email_address 11 from 12 sample_data 13 /EMAIL_ADDRESS VALID_EMAIL_ADDRESS _____________________________ ______________________ not a valid email address false user@domain.com true user@ false user~~name@domain.com true |
Any database client capable of executing SQL calls can call the function.
**Use Case No. 2: Writing Custom MLE Modules**
Writing custom JavaScript modules is another popular use case. Before diving into the mechanics, it’s essential to understand how module resolution works in Oracle Database. Unlike Node, where you have multiple ways of defining [import specifiers](https://nodejs.org/docs/latest-v22.x/api/esm.html#import-specifiers), the database stores JavaScript modules as schema objects. Therefore, Oracle’s naming resolution algorithm must map an import specifier to an existing JavaScript module. This is done using an MLE environment, another new schema object introduced in release 23ai.

Continuing the previous example, you can use `validatorjs`
in your code after creating the MLE environment like so:

1 |
create mle env newstack_env imports ('validator' module validator_module); |
With the environment created, it’s time to turn attention to the JavaScript module. Let’s assume your task is to validate a JSON document your application received via a POST request. The JSON must contain a field named “requestor.” You must then provide a valid email address for the value. Here is an example of how you might perform this validation:
12345678910111213141516171819202122232425262728293031323334 |
import validator from "validator";/** * Validates a POST request object against certain criteria. * * @param {object} data - The POST request body to be validated. * @throws {Error} If no data is provided or validation fails. * @returns {boolean} true if the request is valid */export function validatePOSTRequest(data) { // make sure data has been received, fail if that is not the case if (data === undefined) { throw new Error("please provide the POST request body for validation"); } /** * Check if the 'requestor' field exists in the request body and * whether its value is a valid email address. */ if ("requestor" in data) { if (typeof data.requestor !== "string") { throw new Error("the requestor field must provide a value of type 'string'"); } if (!validator.isEmail(data.requestor)) { throw new Error("the requestor field does not contain a valid email address"); } } else { throw new Error("the required requestor field is missing from the POST request"); } // many more validations return true;} |
Next, load the module into the database using SQLcl:
1 |
mle create-module -filename newstack.js -module-name validate_post_request_module |
Before you can use the JavaScript code in your application, you need to provide a call specification:
123456 |
create or replace function validate_post_request( p_data json) return boolean as mle module validate_post_request_module env newstack_env signature 'validatePOSTRequest'; |
That’s it! You can now use this function in your application. Again, any client capable of executing SQL and PL/SQL can use this function seamlessly.
**Summary**
Developers no longer need to feel intimidated when coding server-side business logic. The availability of JavaScript adds another language to developers’ toolbox. There is, of course, a lot more to say about MLE. To learn more, visit the [Oracle JavaScript Developer’s Guide](https://docs.oracle.com/en/database/oracle/oracle-database/23/mlejs/oracle-database-javascript-developers-guide.pdf?source=:ex:pw:::::TNS_MLE_D&SC=:ex:pw:::::TNS_MLE_D&pcode=) and [Oracle developer blog](https://blogs.oracle.com/developers?source=:ex:pw:::::TNS_MLE_E&SC=:ex:pw:::::TNS_MLE_E&pcode=).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)