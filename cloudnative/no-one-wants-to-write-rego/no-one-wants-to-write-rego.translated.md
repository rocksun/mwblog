[策略即代码](https://www.permit.io/blog/what-is-policy-as-code)彻底改变了组织管理访问控制、合规性和治理的方式。通过将策略编码，团队可以确保一致的执行，自动化流程，并敏捷地适应不断变化的需求。然而，尽管其优势不容否认，“策略即代码”的实施往往感觉像是一场 uphill battle。

尤其是在面对 Rego 策略语言的复杂性时更是如此，Rego 语言虽然功能极其强大，但也突显了使“策略即代码”更容易被更广泛的受众所接受的挑战。

每个人都喜欢“策略即代码”，但没有人想编写 Rego。

为什么会这样？为了解答这个问题，让我们首先探讨为什么“策略即代码”及其姊妹方案“策略即图”已成为不可或缺的，然后再讨论其采用的障碍。

**策略即代码：现代治理的基础**

从根本上说，“策略即代码”使团队能够将管理谁可以访问什么、在什么条件下以及为什么的规则编码。在软件开发中，所有参与者——开发人员、安全团队、合规官员和产品经理——都需要将人员和系统连接到已构建的内容。“策略即代码”提供了一个框架，可以通过一些关键优势来可靠且透明地实现这一目标：

* **一致性**:  作为代码编写的策略在所有环境中都得到统一应用，从而减少错误和差异。
* **透明性和可审计性**: 存储在代码存储库中的策略可以轻松地进行审查、测试和审计，从而使合规性得到证明。
* **自动化**: 将策略集成到 CI/CD 管道中可确保自动测试和执行策略，防止策略漂移。
* **版本控制**: 策略随着其所管理的系统一起发展，每个更改都通过 Git 等工具进行跟踪和可逆转。

尽管有这些优势，但实施之路远非易事，尤其是在制定复杂策略时。

**Rego 作为案例研究：策略编写的挑战**

Rego，[开放策略代理 (OPA)](https://www.permit.io/blog/introduction-to-opa) 的策略语言，是组织在采用“策略即代码”时面临的障碍的一个典型例子。

OPA 非常高效且构建用于性能 - 它将需要评估规则的策略和数据保存在缓存中，并支持将多个实例作为 sidecar 部署到每个微服务，从而避免网络延迟。

它还支持[基于角色的访问控制 (RBAC)](https://www.permit.io/blog/what-is-rbac)、[基于属性的访问控制 (ABAC)](https://www.permit.io/blog/what-is-abac) 和[基于关系的访问控制](https://www.permit.io/blog/what-is-rebac)（ReBAC，经过一定的调整），从而实现高度细粒度的权限管理。

凭借其在业界的广泛采用，它得到了一个蓬勃发展的社区的支持，使其成为构建[细粒度](https://www.permit.io/blog/what-is-fine-grained-authorization-fga)授权策略的可靠选择。

它的语言 Rego 与主流语言（如 Python、Java 或 Go）有很大不同。它源于 Prolog 和 Datalog，这使得它的学习曲线非常陡峭，尤其对于不熟悉逻辑编程范式的开发人员而言。

在简单的情况下，Rego 感觉非常声明式 - 这是一个简单的 Rego 策略示例，用于说明访问控制：

```rego
package example.allow
default allow = false
allow {
input.user == "alice"
input.action == "read"
input.resource == "file1"
}
```

在此策略中：

- `default allow = false` 行确保除非明确允许，否则拒绝访问。
- `allow` 块指定授予访问权限的条件（例如，如果用户是“alice”并且想要“读取”“file1”）。

虽然此示例看起来很简单，但实际策略通常涉及递归、嵌套逻辑以及与外部系统的集成，这些都会迅速增加复杂性。例如，考虑以下涉及 ReBAC 和 ABAC 的稍微高级一些的示例：

```rego
package access
default allow = false
# Define the relationships
relations = {
"user1": {"resources": {"resource1": ["owner"]}},
"user2": {"resources": {"resource1": ["viewer"], "resource2": ["manager"]}}
}
# Fetch the current time from an external service
current_time = time_response {
some resp
http.send({
"method": "GET",
"url": "<http://worldtimeapi.org/api/timezone/Etc/UTC>"
}, resp)
resp.status_code == 200
parsed_body := json.unmarshal(resp.body)
time_response := parsed_body.datetime # Example ISO 8601 time string: "2023-10-25T14:23:42+00:00"
} else = "1970-01-01T00:00:00+00:00" # Default fallback value if HTTP request fails
# Parse the hour from the fetched current time
current_hour = hour {
split(current_time, "T", parts)
split(parts[1], ":", time_parts)
hour := to_number(time_parts[0])
}
# ReBAC logic to check relationships using `walk`
allow_rebac(user, resource) {
walk(relations, [user, "resources", resource, role])
}
```

role == "owner"
}

# 基于属性的访问控制逻辑，用于检查基于时间的约束
allow_time_based_access {
  current_hour >= 9
  current_hour < 17
}

# 组合策略
allow {
  input.user
  input.resource
  allow_rebac(input.user, input.resource)
  allow_time_based_access
}

```

此示例演示了 Rego 如何集成多种访问控制模型，但也强调了其复杂性。我们能否轻松地说这段代码是声明式的？即使稍微推动一些逻辑也会使平衡转向命令式。随着策略的增长，这种挑战和向命令式的趋势只会恶化。

[Styra 的 Regal 项目](https://docs.styra.com/regal) 通过其广泛的 lint 规则、文档和编辑器集成，可以显著降低使用 Rego 编写策略的工作量。
但问题并不仅仅局限于 Rego 本身——它也存在于其他模型中，例如策略即图。

**策略即图：不同的模型**
作为替代方案，一些组织已经采用策略即图框架，例如[Google 的 Zanzibar](https://www.permit.io/blog/what-is-google-zanzibar)，以简化访问控制。这些系统将策略建模为实体（例如，用户、角色和资源）之间的关系，这些关系存储为图节点和边。

例如：

```
document:123 {
  writer: alice
  reader: group:editors
}
group:editors {
  member: bob
}
```

基于图的方法擅长表示层次关系和组成员关系。但是，它们通常难以处理高级条件逻辑，例如基于属性的或基于时间的访问控制，这在该模式中变得很麻烦。虽然策略即图改进了策略可读性的某些方面，但它缺乏更细致场景所需的灵活性。

**策略即代码采用的障碍**
Rego 和策略即图系统都突出了策略即代码采用中的常见挑战：

**复杂性**:许多策略即代码语言都是为精确性和灵活性而设计的，但难以编写和维护。**可访问性有限**:非技术利益相关者，例如合规官员或产品经理，通常缺乏直接参与策略定义的工具或技能。**陡峭的学习曲线**:逻辑编程范式（例如，Rego）和模式配置（例如，Zanzibar）需要专门的知识，即使是经验丰富的开发人员也会感到疏远。**可扩展性**:随着策略规模和复杂性的增长，调试、测试和扩展它们变得越来越具有挑战性。

那么我们如何帮助用户弥合这一差距并提高这些系统的采用率呢？

**使用更高级别的接口弥合差距**
为了充分发挥策略即代码的潜力，组织需要降低这些障碍的工具和实践：

**高级抽象**:通过角色、关系和属性定义策略可以抽象掉底层代码的复杂性。**低代码接口**:像[可视化策略编辑器](https://www.permit.io/)或[Terraform 提供程序](https://docs.permit.io/integrations/infra-as-code/terraform-provider)这样的工具使非技术用户可以访问策略管理。
*Permit.io* 的无代码策略编辑器 UI 会为您生成 Rego 代码。

```
resource"permitio_resource" "document" {
  key = "document"
  name = "Document"
  description = "A confidential document"
  actions = {
    "read" : {
      "name" : "Read",
      "description" : "Read a document",
    },
    "write" : {
      "name" : "Write",
      "description" : "Write a document",
    }
  }
}
```

```
resource"permitio_role" "reader" {
  key = "reader"
  name = "Reader"
  description = "A role that allows reading documents"
  permissions = [
    "document:read"
  ]
  extends = []
  depends_on = [
    permitio_resource.document
  ]
}
```

*使用 **Permit.io** 的 Terraform 提供程序创建资源和角色*

**模板和可重用性**:预构建的策略模板和模块化设计减少了从头编写策略的工作量。

为此，[Permit.io](http://Permit.io) 提供了一个平台，该平台为用户生成策略即代码（使用 Rego 或其他语言），同时允许他们与角色和用户集等高级对象进行交互。这种抽象使安全、合规和运营团队能够参与其中，而无需深入的编程专业知识。

**结论**
策略即代码是现代治理的强大工具，但其复杂性往往会阻止其发挥全部潜力。无论是通过 Rego 等逻辑编程语言还是 Zanzibar 等基于图的模型，该行业都面临着一个共同的挑战：如何使策略既精确又易于访问。

通过采用最佳实践——例如高级抽象、低代码接口和可重用模板——组织可以实现策略即代码的民主化，使所有利益相关者都能有效地做出贡献。诸如[Permit.io](https://www.permit.io/)之类的工具就是这些原则的典范，但整个行业必须继续创新，使策略与它们所管理的系统一样具有包容性。

最终，每个人都喜欢策略即代码，因为它改变了治理方式。成功的关键在于确保每个人——而不仅仅是开发人员——都能参与其中并从中受益。

需要帮助创建Rego策略吗？使用[Permit.io](http://Permit.io)生成它们是免费的——所以一定要查看一下，如果您对Rego、授权或其实现有任何其他疑问，欢迎在我们的[Slack社区](https://io.permit.io/se-slack)中提出。

## 作者
### Or Weis
Permit.io联合创始人/首席执行官

## 相关标签
喜欢这篇文章？

[在Github上关注我们](https://github.com/permitio)![](https://raw.githubusercontent.com/permitio/website/main/public/_next/static/media/github.35b09e10.svg)
不同意？

[告诉我们原因](https://io.permit.io/blog-slack)![](https://raw.githubusercontent.com/permitio/website/main/public/_next/static/media/slack.cbb6ed5c.svg)
想要更多？

[加入我们的Substack](https://io.permit.io/blogstack)![](https://raw.githubusercontent.com/permitio/website/main/public/_next/static/media/pen.e40711f5.svg)