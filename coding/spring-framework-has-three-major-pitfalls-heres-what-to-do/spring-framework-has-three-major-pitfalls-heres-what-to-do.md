
<!--
title: 如何应对Spring框架有三个主要陷阱
cover: https://cdn.thenewstack.io/media/2024/05/4b6a48c7-spring.jpg
-->

Spring 有一些有助于开发过程的出色功能，但了解该框架的局限性和缺点至关重要。

> 译自 [Spring Framework Has Three Major Pitfalls — Here’s What To Do](https://thenewstack.io/spring-framework-has-three-major-pitfalls-heres-what-to-do/)，作者 Jonathan Vila。

Spring 是一个流行的框架——[50%](https://anywhere.epam.com/en/blog/spring-vs-java-ee) 的开发人员现在使用它，它非常适合创建独立的生产级应用程序。借助其帮助开发过程的新类、接口和 API，开发人员必须学习以决定是否要在其编码中使用它。这是因为 Spring Boot 的新功能使用不当会导致错误、错误配置和安全问题，从而影响代码质量。

使用 [Spring 框架](https://thenewstack.io/how-spring-and-java-shaped-internal-developer-platforms/) 时，有三点重要事项需要注意。

## 事务操作

数据库操作必须全部提交才能供其他连接使用。这意味着，对数据库执行的每项操作，该过程都必须打开一个事务，更改数据并提交事务，或者在任何操作失败时回滚事务。

Spring 可以通过 [@Transactional](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html) 为方法添加注释以创建代理，生成在代码库中无缝运行以管理事务的代码。但是，您可能有多个方法调用链，其中一个操作对数据库进行多次更改，并且为了清晰起见，这些更改必须拆分为多个方法。这就是事务传播发生的地方。

通常，我们有一个带有 @Transactional 注释的入口点方法，该方法启动事务。调用链中的其余方法不会指定注释，这允许第一个方法执行整个提交。这是必需的默认传播方法。如果没有正在运行的事务，它将创建一个事务。

但现实往往比我们想象的要复杂。例如，假设您有属于不同操作的方法，有时您的方法是唯一合适的操作。在这些调用链中，我们必须保持兼容的[事务传播](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/tx-propagation.html)，但 Spring 不会考虑自调用的事务规范。

那么，这意味着什么？当您在同一类中从一个方法调用另一个方法时，Spring 将使用“this”方法来引用接收方法。[然后 Spring 生成](https://thenewstack.io/ai-code-generation-6-faqs-for-developers/)代码作为代理来处理无法执行的事务。

为避免这种情况，当在事务中可以执行其他方法的方法中，我们应该指定 @Transaction 注释。

## 持久实体

Spring 的一个优点是它易于与持久层交互。为了使用类型化对象和属性，Java 提供了一个 @Entity 注释来表示关系表，Spring 提供了一个 @Document 注释来表示 MongoDB 和 ElasticSearch 文档。在这些情况下，Spring 可以使用元素中的信息并在对象域和数据库域之间建立桥梁。

这里至关重要的是要理解，这些对象表示与数据库中存储元素直接转换的数据对象，这意味着该对象携带的所有字段都将保存在数据库中。Spring 能够共享方法来生成 REST API 服务，这些服务在用户向该服务器发出 HTTP 请求时执行。这些方法还允许使用实体或文档作为 Spring 将从请求有效负载映射的参数。

为了防止攻击者冒充用户的安全问题，建议使用[数据传输对象 (](https://www.baeldung.com/java-dto-pattern) [DTO)](https://www.baeldung.com/java-dto-pattern)将来自用户的信息转换为实体或文档。这将仅考虑必要的信息并对转换进行清理。

## Bean 定义

Spring 的主要功能是其依赖注入，它使用户能够定义将注入到其他对象及其生命周期中的 bean。借助此功能，类只需要知道它们的依赖关系是什么。它不需要了解如何以及何时必须实例化和删除它们。


Spring 框架提供了一种 bean 发现机制，它通过扫描源代码包来查找 bean 定义。Spring 上下文随后根据配置实例化这些 bean。然而，这种强大的功能也带来了责任。重要的是要意识到，此扫描机制可能会影响应用程序的整体性能，并可能导致在编码时难以发现的运行时错误。为了避免这种情况，至关重要的是在应用程序中始终指定一个包作为 Spring bean 扫描的起点。

Spring 及其依赖注入框架在 bean 的使用者端提供了强大的注入机制。这使得 bean 实例非常易于使用，具有特定的生命周期，而无需担心这些 bean 何时何地被创建或销毁。为了避免在需要之前注入 bean（这可能会损害应用程序性能），建议不要使用 `@Autowired` 注解。相反，应尽可能晚地请求注入，即在通过参数注入需要时。这将指示 Spring 在创建依赖 bean 之前创建 bean。

## 最后的想法

Spring 提供了一些有助于开发过程的出色功能，但它也附带了复杂的配置。了解 Spring 的局限性和缺点对于充分利用它至关重要，但这可能很困难。代码中可能导致性能和稳定性中断的位置并不总是很明显。

这就是像 [Sonar](https://www.sonarsource.com/solutions/clean-code/?utm_medium=referral&utm_source=newstack&utm_campaign=ss-cleancode&utm_content=media-Spring%20Boot-240507-&utm_term=&s_category=Organic&s_source=External%Referral&s_origin=newstack) 这样的静态分析解决方案可以提供帮助的地方。它包含涵盖和发现主要问题的规则，在编码过程中提供警告，并在 CI/CD 管道中执行持续监控。通过制定适当的规则来确保质量，更容易确信编写的代码将产生增加实际价值的软件，而不是成为一种负担。