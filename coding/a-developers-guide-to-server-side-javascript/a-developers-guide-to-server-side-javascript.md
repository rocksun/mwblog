<!--
title: 服务端JavaScript开发者指南
cover: https://cdn.thenewstack.io/media/2025/04/44147507-modules.jpg
summary: 告别后端恐惧！Oracle Database 23ai 引入 MLE，让 JS 开发者也能轻松驾驭服务器端。通过 GraalVM 支持，直接在数据库中运行 JavaScript 代码，像 `validator.js` 模块无缝集成。自定义模块结合 `create mle env`，实现高效数据验证，解锁云原生时代Server-Side JavaScript 新姿势！
-->

告别后端恐惧！Oracle Database 23ai 引入 MLE，让 JS 开发者也能轻松驾驭服务器端。通过 GraalVM 支持，直接在数据库中运行 JavaScript 代码，像 `validator.js` 模块无缝集成。自定义模块结合 `create mle env`，实现高效数据验证，解锁云原生时代Server-Side JavaScript 新姿势！

> 译自：[A Developer’s Guide to Server-Side JavaScript](https://thenewstack.io/a-developers-guide-to-server-side-javascript/)
> 
> 作者：Martin Bach

每当应用程序需要处理状态时，开发人员都会求助于数据库来存储、检索和操作数据。这种方法已不再被争论；使用数据库作为持久层是一种经过验证的成熟方法。然而，后续的决定已经争论了几十年：应该将应用程序的业务逻辑放在哪里？

## 客户端与服务器端业务逻辑

一方面，开发人员喜欢掌控一切，在前端执行所有与应用程序数据相关的操作。在数据库中编写存储代码需要了解 SQL 和数据库支持的过程语言。无论是 PL/SQL、T-SQL 还是 PL/pgSQL，[React developer](https://roadmap.sh/react) 可能并不熟悉它。与 [前端](https://thenewstack.io/introduction-to-frontend-development/)（或 [microservice](https://thenewstack.io/microservices/)）使用 [相同的语言编写业务逻辑](https://thenewstack.io/3-foundational-principles-for-writing-efficient-sql/) 很自然。

在数据库中执行的存储代码的支持者正确地指出，在应用程序内部复制数据库功能（确保原子性、一致性、隔离性和持久性）是多余的。考虑到在许多应用程序中重复工作，您会痛苦地意识到花费了额外的精力。此外，可能会出现关于数据质量、治理、审计等方面的问题。而且您甚至还没有谈到编写良好的存储代码的性能优势。

如果您关注社交媒体和 Reddit 和 Stack Overflow 等网站，这场讨论似乎已经陷入僵局。

如果能够两全其美岂不是很好——一种熟悉的编程语言来编写业务逻辑，再加上在数据所在位置运行代码的所有好处？例如，JavaScript 是最流行的语言之一。Oracle Database 23ai 是支持基于广受欢迎的 GraalVM 的服务器端 [JavaScript](https://thenewstack.io/javascript/) 的数据库之一。MySQL 是这种数据库管理系统的一个很好的例子。

让我们来看看开发人员如何在 Oracle Database 23ai 中编写服务器端 JavaScript。

## 什么是多语言引擎，如何使用它？

[Multilingual Engine](https://docs.oracle.com/en/database/oracle/oracle-database/23/mlejs/introduction-to-mle.html?source=:ex:pw:::::TNS_MLE_A&SC=:ex:pw:::::TNS_MLE_A&pcode=)（简称 MLE）允许开发人员在 Oracle 数据库中存储和执行 JavaScript 代码。它实现了 ECMAScript 2023 标准，并具有许多 [内置函数](https://oracle-samples.github.io/mle-modules/)。
您可以使用来自内容分发网络的现有 JavaScript 模块，或者像在 PL/SQL 中一样编写代码。如果模块的许可证与您的项目兼容，并且没有其他合规性问题阻止其使用，那么使用现有模块可以显着加快开发速度。

## 用例 1：将第三方模块嵌入到您的应用程序中

常见的数据库任务是验证输入，以帮助确保数据质量。流行的 [validator library](https://github.com/validatorjs/validator.js) 提供了大量的字符串验证方法。假设您手头的任务是验证电子邮件地址。使用 JavaScript，这很简单。

首先从您喜欢的 CDN 下载 `validatorjs` 模块。以下示例已在 MacOS 上运行；您可能需要为 Windows 调整 `curl` 参数。

```
curl -Lo validator-13.12.0.js 'https://cdn.jsdelivr.net/npm/validator@13.12.0/+esm'
```

[Oracle’s SQL Developer Command Line](https://www.oracle.com/database/sqldeveloper/technologies/sqlcl/?source=:ex:pw:::::TNS_MLE_B&SC=:ex:pw:::::TNS_MLE_B&pcode=) (SQLcl) 提供了将 JavaScript 模块部署到数据库的最便捷方式。以下 SQLcl 命令基于下载文件的内容在数据库中创建一个名为 `validator_module` 的新模块。最好也提供模块版本。

```
mle create-module -filename validator-13.12.0.js -module-name validator_module -version 13.12.0
```

该模块创建为新的模式对象；其属性在数据字典中可用。在 SQL 和 PL/SQL 中使用它之前，必须创建一个所谓的 [call specification](https://docs.oracle.com/en/database/oracle/oracle-database/23/mlejs/call-specifications-functions.html?source=:ex:pw:::::TNS_MLE_C&SC=:ex:pw:::::TNS_MLE_C&pcode=#GUID-D0C14B08-5B84-4127-8DE7-F56043F79630)。根据 [its documentation](https://github.com/validatorjs/validator.js/blob/master/README.md)，`validatorjs` 提供了一个名为 `isEmail` 的函数
可以精确地完成所需的操作：验证字符串是否为电子邮件地址。让我们将该函数公开给 SQL：

```sql
create function is_email(p_string varchar2)return boolean as mle module validator_module signature 'default.isEmail';
```

这就是全部。让我们验证一些字符串：

```sql
with sample_data (email_address) as (
  values
  ('not a valid email address'),
  ('user@domain.com'),
  ('user@'),
  ('user~~name@domain.com')
  )
  select
  email_address,
  is_email(email_address) valid_email_address
  from
  sample_data
  /

EMAIL_ADDRESS                VALID_EMAIL_ADDRESS
_____________________________ ______________________
not a valid email address     false
user@domain.com               true
user@                         false
user~~name@domain.com        true
```

任何能够执行 SQL 调用的数据库客户端都可以调用该函数。

## 用例 2：编写自定义 MLE 模块

编写自定义 JavaScript 模块是另一个常见的用例。在深入研究其机制之前，必须了解模块解析在 Oracle 数据库中的工作方式。与 Node 不同，Node 有多种定义 [导入说明符](https://nodejs.org/docs/latest-v22.x/api/esm.html#import-specifiers) 的方法，数据库将 JavaScript 模块存储为模式对象。因此，Oracle 的命名解析算法必须将导入说明符映射到现有的 JavaScript 模块。这是通过 MLE 环境完成的，MLE 环境是 23ai 版本中引入的另一个新的模式对象。

继续前面的示例，您可以在创建 MLE 环境后在代码中使用 `validatorjs`，如下所示：

```sql
create mle env newstack_env imports ('validator' module validator_module);
```

创建环境后，就该关注 JavaScript 模块了。假设您的任务是验证应用程序通过 POST 请求接收的 JSON 文档。JSON 必须包含一个名为“requestor”的字段。然后，您必须为该值提供有效的电子邮件地址。以下是如何执行此验证的示例：

```javascript
import validator from "validator";

/**
 * Validates a POST request object against certain criteria.
 *
 * @param {object} data - The POST request body to be validated.
 * @throws {Error} If no data is provided or validation fails.
 * @returns {boolean} true if the request is valid
 */
export function validatePOSTRequest(data) {
  // make sure data has been received, fail if that is not the case
  if (data === undefined) {
    throw new Error("please provide the POST request body for validation");
  }

  /**
   * Check if the 'requestor' field exists in the request body and
   * whether its value is a valid email address.
   */
  if ("requestor" in data) {
    if (typeof data.requestor !== "string") {
      throw new Error("the requestor field must provide a value of type 'string'");
    }

    if (!validator.isEmail(data.requestor)) {
      throw new Error("the requestor field does not contain a valid email address");
    }
  } else {
    throw new Error("the required requestor field is missing from the POST request");
  }

  // many more validations
  return true;
}
```

接下来，使用 SQLcl 将模块加载到数据库中：

```sql
mle create-module -filename newstack.js -module-name validate_post_request_module
```

在应用程序中使用 JavaScript 代码之前，您需要提供一个调用规范：

```sql
create or replace function validate_post_request(
  p_data json
) return boolean as
  mle module validate_post_request_module
  env newstack_env
  signature 'validatePOSTRequest';
```

就是这样！您现在可以在应用程序中使用此函数。同样，任何能够执行 SQL 和 PL/SQL 的客户端都可以无缝地使用此函数。

## 总结

开发人员在编写服务器端业务逻辑时不再需要感到害怕。JavaScript 的可用性为开发人员的工具箱中添加了另一种语言。当然，关于 MLE 还有很多要说的。要了解更多信息，请访问 [Oracle JavaScript 开发人员指南](https://docs.oracle.com/en/database/oracle/oracle-database/23/mlejs/oracle-database-javascript-developers-guide.pdf?source=:ex:pw:::::TNS_MLE_D&SC=:ex:pw:::::TNS_MLE_D&pcode=) 和 [Oracle 开发人员博客](https://blogs.oracle.com/developers?source=:ex:pw:::::TNS_MLE_E&SC=:ex:pw:::::TNS_MLE_E&pcode=)。