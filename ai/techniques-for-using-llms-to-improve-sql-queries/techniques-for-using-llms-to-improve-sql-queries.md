<!--
# 利用LLM改进SQL查询的技术
https://cdn.thenewstack.io/media/2023/11/105b5ea9-jandira-sonnendeck-acw1zwd-qc0-unsplash-1024x685.jpg
-->

首先我们修复了一个SQL查询中的bug。然后我们重新思考了查询的设计。这里是使用LLM调整SQL查询的进一步方法。

译自 [Techniques for Using LLMs to Improve SQL Queries](https://thenewstack.io/techniques-for-using-llms-to-improve-sql-queries/) 。

这个有问题的查询本意是检测Azure虚拟机中的网络安全组是否允许对敏感端口进行入站访问。一个用户报告说，对于两个不同的测试用例，查询报告**正常**，但本应该报告**警报**。在第一个用例中，安全组直接附加到了VM的网络接口上;在第二个用例中，它附加到了VM的子网上。

要调试这个查询SQL语句，它需要通过包括 [azure_compute_virtual_machine](https://hub.steampipe.io/plugins/turbot/azure/tables/azure_compute_virtual_machine) 和 [azure_network_security_group](https://hub.steampipe.io/plugins/turbot/azure/tables/azure_network_security_group) 在内的Steampipe表来查询一个Azure订阅，就需要准备一对配置了这两种不同方式安全组的VM。在LLM时代之前，搭建这些资源意味着要搜索Terraform示例，然后消除找到的示例和所需设置之间的差异。

现在你可以让LLM编写初始的Terraform代码，然后在反复交流中逐步完善它。我的所有LLM助手都证明自己有这个能力: 这是一个我们不应视为理所当然的奇迹，但我们可能很快就会如此认为。LLM编写的Terraform代码快速完成了所需资源的配置，然后我们继续调试查询。

## 调试有问题的 JOIN

这里是失败查询的主要部分。

```sql
select
  'Unrestricted Ingress' as label,
  case
    when sg.sg_name is null then 'Restricted' 
    else 'Unrestricted'
  end as value,
  case
    when sg.sg_name is null then 'ok'
    else 'alert' 
  end as type
from
  azure_compute_virtual_machine as vm
  left join network_sg as sg on sg.network_interfaces @> vm.network_interfaces
```

这个连接失败是因为两个network_interfaces列包含了形状不同的JSONB对象;Postgres的JSONB包含操作符@>无法匹配它们。由于JSONB对象是数组，而我们需要匹配的是一个两个数组中共有的键值对，那么展开数组并在其元素中查找匹配那个键值对是合理的。

## 简明与冗长的SQL语法

ChatGPT、Copilot Chat和新来者[Unblocked](https://getunblocked.com/)给出的初始解决方案使用了各种形式的利用Postgres的jsonb_array_elements函数进行交叉连接来实现这个策略。这里是一些变种:

```sql
-- ChatGPT
from
  azure_compute_virtual_machine as vm
  left join network_sg as sg on exists (
     select 1
       from
         jsonb_array_elements(sg.network_interfaces) as sg_if_elements(sg_obj),
         jsonb_array_elements(vm.network_interfaces) as vm_if_elements(vm_obj)
       where sg_if_elements.sg_obj->'id' = vm_if_elements.vm_obj->'id'
   )
```

```sql
-- Copilot Chat   
from
  (select jsonb_array_elements(network_interfaces) -> 'id' as network_interface_id from azure_compute_virtual_machine) as vm
  left join network_sg as sg on sg.network_interface_id = vm.network_interface_id
```

```sql
-- Unblocked
from
  azure_compute_virtual_machine as vm,
  jsonb_array_elements(vm.network_interfaces) as vm_ni
  left join lateral (
    select sg_name from network_sg, jsonb_array_elements(network_interfaces) as sg_ni
    where sg_ni -&gt;&gt; 'id' = vm_ni -&gt;&gt; 'id'
  ) as sg on true
```

虽然所有这些解决方案都实现了需要的连接，但它们都难以阅读和理解 - 即使对我这种使用Postgres JSONB数据类型和jsonb_array_elements等集合返回函数有一定经验的人来说也是如此。当你把这些与(可能是横向的)交叉连接组合使用时，你最终会得到一些简明但不透明且难以调试的SQL表达式。

我长期主张将查询重构为CTE(公共表表达式)管道，每个CTE执行复杂转换中的一步。这样你就可以单独推理、测试和调试每一步。但我也认识到简明语法的作用，它可以折叠步骤。通过深厚的专业知识和长期的练习，你可以建立起心智模型，以便形象地思考这些复杂的转换。到那时，详细的逐步查询可能过于冗长;使用简洁的语法更有效率。

那么，应该为初学者还是专家编写代码呢？理想情况下，你不应该在两者之间做选择。在这个练习中，我提示我的LLM助手将上述等简明表达式重写为更易理解的简单CTE管道。它们都能做到这一点。我可以想象在简明和冗长语法之间进行自动双向翻译，作为另一种动态文档形式。

## 有罪推定，除非证明无辜

对修改后的查询进行的测试暴露出一个新问题。有许多方法可以描述网络安全组中指定的入站端口: 特定端口或端口范围、诸如Internet和any之类的词以及*和/0等通配符。不考虑任何这些都会导致错误的报告OK。如何使查询对这种遗漏具有弹性？以下是我向ChatGPT提出这个挑战的方式。

```
PROMPT:
Although our query now works as designed, there is a problem with the design. The query’s job is to ring an alarm bell if an azure vm is open to attack in two different ways. The first case is an Azure VM with a security group – that has sensitive open inbound ports – attached directly to its network interface. The second case is similar, but now the security group is attached to the VM’s subnet. If you have two VMs matching these conditions, two alarms should ring. The problem we solved was that the alarms weren’t ringing because there was a faulty SQL join between two of Steampipe’s Azure tables. The shape of the data structure in the JSONB network_interfaces column of one table didn’t match the shape of the data the corresponding column of the other, and the JSONB comparison operator couldn’t handle that difference. To fix the query, we switched to a strategy that unnests the JSONB structures and matches on a particular key/value pair. Are you with me so far?

RESPONSE
Yes, I understand the scenario you’re describing. [replay of prompt]

PROMPT:
OK good. Now here is the design problem I mentioned. This query isn’t failsafe. The VMs are deemed innocent until proven guilty. When the conditions of guilt aren’t met because of a query error or omission, the query reports OK instead of Alarm. How can we make it so the VMs are deemed guilty until proven innocent? In case of a query error or omission, they’ll report Alarm instead of OK. Better to have a false alarm in a case where the VMs are actually innocent than to have no alarm when they are guilty. Do you understand the problem?

RESPONSE:
Yes, I understand the problem. [replay of prompt]
```

然后我们讨论了如何反转查询的逻辑以使其失败安全。经过几次迭代，ChatGPT给出以下策略:

```
RESPONSE:
To modify the query according to the discussed plan, we will first create a list of all VMs and assign an initial status of ‘alarm’ to each. Then we’ll check against the conditions that would indicate a VM is not vulnerable (i.e., ‘innocent’). If a VM does not meet these conditions, it will remain ‘guilty’ (status remains ‘alarm’).
```

经过几次迭代，我们得到一个工作的查询，它可以正确识别易受攻击的安全组，并且对错误或遗漏具有弹性。 VM先前是无辜直到被证明有罪，现在是相反的: 它们被视为有罪，直到被证明无辜。而且目前，我保留了调试时使用的详细、分步的格式。

## 简明与冗长语法再探讨

作为最后一个测试，我要求ChatGPT使冗长的查询更加紧凑。它提出了一种使用CROSS JOIN LATERAL以及EXISTS子查询中的隐式 jsonb_array_elements 交叉连接的简明替代方案。这种方法在第一次试验中就没有成功，并且难以通过迭代改进。

在冗长和简明SQL语法之间进行自动转换是一个有吸引力的想法。但是，虽然LLM在将5000字的文章缩减到500字方面做得相当不错，但对于SQL查询来说，目前要求它们做同样的工作可能过高。我们使查询更紧凑的努力就到此结束了。

```
RESPONSE:
Since the goal is to produce a more succinct query without losing the logical flow of the original, we must preserve the order of operations and the conditions applied in each CTE. However, the challenge is that compacting the query might obscure the complex relationships between network interfaces, security groups, and virtual machines. Considering the complexity, the verbose query might be the best approach for maintainability and debugging purposes. Compact queries can be harder to debug and understand, especially when dealing with nested JSONB structures and multiple JOIN conditions.
```

来自一个随机生成器的非常好的建议!

我很成功地要求LLM将简明的查询展开为更易理解的简单CTE管道，我强烈建议你也这样使用它们。但是，如果你想走另一条路，目前看来你只能靠自己了。
