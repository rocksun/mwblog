# AI Agent 的崛起：Arazzo 如何定义 API 工作流的未来

![Featued image for: AI Agent 的崛起：Arazzo 如何定义 API 工作流的未来](https://cdn.thenewstack.io/media/2025/02/b383a55d-james-harrison-vpoexr5wmr4-unsplash-1-1024x576.jpg)

[James Harrison](https://unsplash.com/@jstrippa?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) 来自 [Unsplash](https://unsplash.com/photos/black-laptop-computer-turned-on-on-table-vpOeXr5wmR4?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).

曾经，移动革命的口号是：“为此有一个应用程序”。如今，新的现实是，AI驱动的 Agent 正在极大地改变我们与软件交互的方式，创造了一个新的口号：“为此有一个 Agent！”从自动化任务到执行复杂的工作流，并代表我们自主行动，AI Agent 正在成为数字交互中关键的中介。虽然这看起来像是魔法，但 API——而不是新的巫术——仍然提供了使这些 Agent 工作流成为可能并服务于这类新用户的连接结构。

这种转变导致了 API 使用的巨大加速，随着对机器可读数据交换的需求激增，2024 年 AI 驱动的 API 使用量飙升。新一波的 AI 用户推动了 AI 相关 API 生产的急剧[增长 800%](https://nordicapis.com/shift-to-ai-exploded-api-usage-in-2024/)，进一步强化了设计结构化、互操作性和 AI 就绪型 API 的重要性。因此，从整体上考虑 API——并[确保它们是为 AI 时代而构建的](https://thenewstack.io/why-api-first-matters-in-an-ai-driven-world/)——在所有行业领域都比以往任何时候都更加重要。

API 活动的激增也推动了基于标准的倡议（如[OpenAPI Initiative](https://www.openapis.org/) (OAI)）的 renewed momentum。2024 年，该倡议通过发布 Arazzo [1.0.0](https://www.openapis.org/arazzo) 和 [Overlay](https://www.openapis.org/blog/2024/10/22/announcing-overlay-specification) 1.0.0 等规范，以及 OpenAPI 规范的两个重要补丁版本：[3.1.1 和 3.0.4](https://www.openapis.org/blog/2024/10/25/announcing-openapi-specification-patch-releases)，为活动设定了新的标准。这一势头一直持续到 2025 年，最近发布的 [Arazzo 1.0.1](https://spec.openapis.org/arazzo/v1.0.1.html) 补丁版本标志着这一势头。

## 为什么标准和规范很重要？

在当今快速发展的 API 环境中，AI Agent 正在成为一流的 API 使用者，标准和规范在确保互操作性、改进工具体验以及促进对 API 设计、实现和使用方式的共同理解方面发挥着关键作用。OpenAPI、AsyncAPI 和 Arazzo 等规范构成了创建一致、可预测的 API 体验的基础——尤其是在我们进入 AI 时代时，这一点至关重要。

API 使用的这种转变具有实际意义。但这为什么重要呢？

从[API 中提取价值通常需要不止一次](https://thenewstack.io/confluent-combines-cloud-native-and-on-premises-data-streaming-through-single-api/) API 调用。相反，[工作流通常需要一系列以编程方式协调的 API](https://thenewstack.io/asyncapi-looks-to-unify-api-workflow-under-linux-foundation/) 调用来完成特定任务（或作业）。当将责任委托给代表我们自主执行任务的 AI Agent 时，同样的前提也成立。

但是，API 文档的质量和准确性差异很大，这给所有使用者带来了挑战。即使是 OpenAPI 描述之类的结构化格式也[不能原生定义复杂的工作流](https://thenewstack.io/boost-azures-faas-capabilities-with-durable-functions/)，尤其是在跨越多个 API 时。支持文档也经常省略关于将多个 API 调用编排到一个连贯的工作流中的指导，尤其是在可以验证的方式中。人工使用者通过反复试验、带外文档或与 API 提供商直接沟通来弥补这些差距。但是，AI Agent 缺乏这种灵活性，我们当然不希望它们在没有确定性指导的情况下进行反复试验的执行，以确保可靠地运行。

为了有效且一致地利用 API，AI Agent 和系统需要结构化、确定性和可靠的工作流——只有强大的规范才能保证这一点。通过标准化一系列复杂或敏感的 API 调用如何协同执行，我们可以：

- 防止 AI 幻觉或来自 AI 驱动的使用者的错误输出。
- 确保跨 API 生态系统的互操作性、质量和效率。
- 在 API 生产者和使用者（人和机器）之间建立信任。
通过这样做，我们同时提升了人类开发者体验 (DX) 和代理体验 (AX)。

正如**David Roldán Martínez**（一位**人工智能研究员和行业顾问**）所说：

“在自主系统日益依赖于与各种 API 交互的代理人工智能时代，Arazzo 这样的规范成为确定性和可靠性 API 工作流的关键推动因素。通过提供一个标准化的框架来编排复杂的 API 交互，Arazzo 使[开发人员能够构建强大且可扩展的](https://thenewstack.io/how-to-build-scalable-real-time-applications-with-javascript/)解决方案。这增强了人工智能驱动系统的可预测性和效率，并促进了更大的信任和控制，确保下一波 API 使用保持灵活和可治理。”

## 什么是 Arazzo 规范？
Arazzo 规范（目前版本为 [1.0.1](https://www.openapis.org/blog/2025/01/24/announcing-arazzo-specification-version-1-0-1)）支持创建确定性 API 工作流——一系列结构化的 API 调用，当组合在一起时，可以实现特定的业务目标或消费者工作。

Arazzo 支持 JSON 和 YAML 格式，使工作流既可读懂也可由机器读取。这使得 API 功能更容易理解和使用，从而加快了传统人类开发者和 AI 代理消费者的采用速度。通过提供一种表达工作流的结构化方式，Arazzo 弥合了 API 生产者和消费者之间的差距，使 API 的高效集成更容易。

除了可读性之外，Arazzo 的确定性还有助于[API 提供商应对关键行业](https://thenewstack.io/a-look-at-telecom-apis/)挑战，同时为下一代基于代理的 API 使用创造新的可能性。它还支持第三方验证，允许监管机构[提高各个司法管辖区的严谨性和合规性](https://thenewstack.io/a-call-to-use-generative-ai-to-create-more-trustworthy-data/)。

## Arazzo 和 AI 代理 API 使用
Arazzo 的确定性方法使代理 API 使用更高效。它允许 API 提供商在各种大型语言模型 (LLM) 和代理技术栈之间交付互操作的工作流。提供商可以定义和使用面向用例的消费语义[跨多个 API 操作](https://thenewstack.io/linux-run-a-single-command-across-multiple-servers-with-ssh/)，无论是在单个 API 描述中还是在多个独立的 API 描述中。

此外，Arazzo 的可扩展性允许包含基于使用情况或基于 SLA 的元数据，这些元数据可以在处理或可观测性层强制执行，以确保可预测的规模、成本管理和预期的 AI 代理对 API 的使用，这对于 IT 领导者在应对[总拥有成本](https://thenewstack.io/how-real-time-database-design-boosts-total-cost-of-ownership/)(TCO)新的 AI 融合拓扑结构时将变得越来越重要。

## API 是代理的“最佳”接口
用于计算机使用 (ACU) 和计算机使用代理 (UCA) 的人工智能代理的兴起——包括最近 OpenAI 的 Operator 等创新——展示了人工智能如何通过与现有用户界面 (UI) 交互来增强人类工作流程。这种方法在遗留环境中非常重要，在这些环境中，人工智能可以[快速释放价值，而无需开发新的 API](https://thenewstack.io/apis-are-driving-new-business-models-and-unlocking-revenue-streams/)。

然而，虽然利用基于 UI 的自动化可以带来短期收益，但 API 本质上是人工智能代理的更优接口。与专为人类认知而设计的 UI 不同，API 是为机器使用而构建的，从长远来看，它们更具可扩展性、可靠性和成本效益。

便利技术往往会适得其反，虽然可能会有短期收益，但管理人员可能会误解这些收益，认为它们是实现人工智能目标更便宜、更快、更一致的方法。正如[机器人流程自动化](https://thenewstack.io/robocorp-makes-remote-process-automation-programmable/)(RPA)通常被误解为“快速自动化解决方案”（后来导致昂贵的维护成本一样），如果公司未能投资于 API 优先战略，短期基于 UI 的 AI 集成可能会成为一种拐杖。

通过投资强大的 API 资源，组织可以为不可避免的转变做好准备，在这种转变中，API 而不是 UI 将成为人工智能代理的主要接口。这就是 Arazzo 的作用所在——通过提供确定性 API 工作流层，Arazzo 确保代理以结构化、可靠的方式与 API 交互，而不是依赖于脆弱的基于 UI 的自动化并交付前面提到的代理体验 (AX) 需求。

## 超越 AI：Arazzo 的更广泛用例
虽然 Arazzo 是基于 AI 的 API 使用的关键推动因素，但它也为当今 API 生产者和消费者在整个 API 生命周期中提供了更广泛的价值：
提供确定性API使用方案：标准化工作流程，确保API交互的可重复性和结构化。
充当动态工作流程文档：保持API工作流程的最新性，无需依赖过时或外部文档。
自动化面向消费者的文档：通过动态生成开发者门户文档，减少对外部文档的依赖。
启用端到端测试自动化：定义可用于自动化测试的API工作流程。
简化监管合规性验证：
[自动化检查以根据合规性要求验证API交互](https://thenewstack.io/want-to-mitigate-risk-invest-in-automation/)。- 增强下一代API SDK生成：为
[改进的开发者体验](https://thenewstack.io/improve-developer-experience-to-prevent-burnout/)启用工作流感知的SDK。
Arazzo规范不要求特定的开发流程，例如*设计优先*或*代码优先*。它通过使用OpenAPI规范（计划[扩展到基于事件的](https://github.com/OAI/Arazzo-Specification/issues/270)协议和AsyncAPI规范）来描述HTTP API，从而促进这两种技术，建立精确的工作流程交互。


## Arazzo — 一个具体的例子
让我们想象一下，我们想描述如何实现在线产品的“先买后付(BNPL)”结账工作流程。代理将负责确定产品和客户是否有资格享受这种类型的金融服务。执行BNPL流程的步骤如下：

- 检查所选产品是否符合BNPL资格
- 获取条款和条件并确定客户资格
- 创建客户记录（如有需要）
- 启动BNPL贷款交易
- 验证客户身份并获得贷款授权
- 计算并检索用于客户端渲染的付款方案
- 更新订单状态

有两个API提供完成此过程所需的端点/方法。它们是：

![图1 – 先买后付 – 资格API](https://cdn.thenewstack.io/media/2025/02/db49f6c6-picture1.png)

![图2 – 先买后付 – 贷款API](https://cdn.thenewstack.io/media/2025/02/8208d243-picture1.png)

利用Arazzo，我们可以明确地描述工作流程，指导代理首先并每次都正确地执行工作流程。如果您想在查看下面的Arazzo文档之前更好地了解规范结构，请查看这篇关于规范的[深入探讨](https://swagger.io/blog/the-arazzo-specification-a-deep-dive/)。

```yaml
arazzo: 1.0.1

info:
  title: BNPL贷款申请流程
  version: 1.0.0
  description: >
    此流程概述了在结账时申请BNPL贷款的步骤，
    包括检查产品资格、检索条款和条件、创建客户记录、
    启动贷款交易、客户身份验证以及检索最终付款计划。
    交易完成后，它将通过更新订单状态来结束。

sourceDescriptions:
  - name: BnplEligibilityApi
    url: https://raw.githubusercontent.com/frankkilcommins/apidays-describing-api-workflows-with-arazzo/ef35e237576d7af2bc3be66d94ffca94eee5036d/specs/bnpl-eligibility.openapi.yaml
    type: openapi

  - name: BnplLoanApi
    url: https://raw.githubusercontent.com/frankkilcommins/apidays-describing-api-workflows-with-arazzo/ef35e237576d7af2bc3be66d94ffca94eee5036d/specs/bnpl-loan.openapi.yaml
    type: openapi

workflows:
  - workflowId: ApplyForLoanAtCheckout
    summary: 使用BNPL平台在结账时申请BNPL贷款
    description: >
      此流程描述了使用BNPL平台在结账时获得贷款的步骤，其中涉及多个API调用，
      以检查产品资格、确定客户资格、启动贷款交易、验证客户身份、
      检索付款计划和更新订单状态。

    inputs:
      type: object
      required:
        - customer
        - products
        - totalAmount
        - token
      properties:
        customer:
          description: 客户详细信息或现有客户记录的链接。
          oneOf:
            - type: object
              required:
                - firstName
                - lastName
                - dateOfBirth
                - postalCode
              properties:
                firstName:
                  type: string
                lastName:
                  type: string
                dateOfBirth:
                  type: string
                  format: date-time
                postalCode:
                  type: string
            - type: object
              required:
                - uri
              properties:
                uri:
                  description: 现有客户的URI。
                  type: string
                  format: uri

        products:
          type: array
          minItems: 1
          items:
            type: object
            required:
              - productCode
              - purchaseAmount
            properties:
              productCode:
                type: string
              purchaseAmount:
                type: object
                required:
                  - currency
                  - amount
                properties:
                  currency:
                    type: string
                    pattern: "^[A-Z]{3}$"
                  amount:
                    type: number

        totalAmount:
          type: object
          required:
            - currency
            - amount
          properties:
            currency:
              type: string
              pattern: "^[A-Z]{3}$"
            amount:
              type: number

        token:
          description: 贷款交易的授权令牌。
          type: string

    steps:
      - stepId: checkProductEligibility
        description: 调用BNPL API以检查所选产品是否有资格获得BNPL贷款。
        operationId: $sourceDescriptions.BnplEligibilityApi.findEligibleProducts
        requestBody:
          contentType: application/json
          payload: |
            {
              "customer": "{$inputs.customer.uri}",
              "products": $inputs.products
            }
        successCriteria:
          - condition: $statusCode == 200
        outputs:
          eligibilityCheckRequired: $response.body.eligibilityCheckRequired
          eligibleProducts: $response.body.productCodes
          totalLoanAmount: $response.body.totalAmount
        onSuccess:
          - name: productsEligible
            type: goto
            stepId: getCustomerTermsAndConditions
            criteria:
              - condition: $response.body.productCodes != null
          - name: productsNotEligible
            type: end
            criteria:
              - condition: $response.body.productCodes == null

      - stepId: getCustomerTermsAndConditions
        description: 检索BNPL贷款的条款和条件。
        operationId: $sourceDescriptions.BnplEligibilityApi.getTermsAndConditions
        successCriteria:
          - condition: $statusCode == 200
        outputs:
          termsAndConditions: $response.body
        onSuccess:
          - name: eligibilityCheckRequired
            type: goto
            stepId: createCustomer
            criteria:
              - condition: $steps.checkProductEligibility.outputs.eligibilityCheckRequired == true
          - name: eligibilityCheckNotRequired
            type: goto
            stepId: initiateBnplTransaction
            criteria:
              - condition: $steps.checkProductEligibility.outputs.eligibilityCheckRequired == false

      - stepId: createCustomer
        description: >
          如果客户尚未注册，请通过验证其BNPL贷款资格来创建一个新的客户记录。
        operationId: $sourceDescriptions.BnplEligibilityApi.createCustomer
        requestBody:
          contentType: application/json
          payload: |
            {
              "firstName": "{$inputs.customer.firstName}",
              "lastName": "{$inputs.customer.lastName}",
              "dateOfBirth": "{$inputs.customer.dateOfBirth}",
              "postalCode": "{$inputs.customer.postalCode}",
              "termsAndConditionsAccepted": true
            }
        successCriteria:
          - condition: $statusCode == 200 || $statusCode == 201
        outputs:
          customer: $response.body.links.self
        onSuccess:
          - name: customerCreated
            type: goto
            stepId: initiateBnplTransaction
            criteria:
              - condition: $statusCode == 201
          - name: customerNotEligible
            type: end
            criteria:
              - condition: $statusCode == 200

      - stepId: initiateBnplTransaction
        description: 启动BNPL贷款交易。
        operationId: $sourceDescriptions.BnplLoanApi.createBnplTransaction
        requestBody:
          contentType: application/json
          payload: |
            {
              "enrolledCustomer": "https://api.example.com/customers/12345",
              "products": $inputs.products,
              "totalAmount": $inputs.totalAmount
            }
        successCriteria:
          - condition: $statusCode == 202
        outputs:
          redirectAuthToken: $response.body.redirectAuthToken
          loanTransactionId: $response.body.loanTransactionId
        onSuccess:
          - name: authorizationRequired
            type: goto
            stepId: authenticateCustomerAndAuthorizeLoan
            criteria:
              - condition: $response.body.redirectAuthToken != null
          - name: authorizationNotRequired
            type: goto
            stepId: retrievePaymentPlan
            criteria:
              - condition: $response.body.redirectAuthToken == null

      - stepId: authenticateCustomerAndAuthorizeLoan
        description: 验证客户身份并获得贷款授权。
        operationId: $sourceDescriptions.BnplEligibilityApi.getAuthorization
        parameters:
          - name: authorizationToken
            in: query
            value: $inputs.token
        successCriteria:
          - condition: $statusCode == 200
        outputs:
          redirectUrl: $response.headers.Location

      - stepId: retrievePaymentPlan
        description: 贷款授权后检索最终付款计划。
        operationId: $sourceDescriptions.BnplLoanApi.retrieveBnplLoanTransaction
        parameters:
          - name: loanTransactionId
            in: path
            value: $steps.initiateBnplTransaction.outputs.loanTransactionId
        successCriteria:
          - condition: $statusCode == 200
        outputs:
          finalizedPaymentPlan: $response.body

      - stepId: updateOrderStatus
        description: 贷款交易完成后，将订单状态更新为"已完成"。
        operationId: $sourceDescriptions.BnplLoanApi.updateBnplLoanTransactionStatus
        parameters:
          - name: loanTransactionId
            in: path
            value: $steps.initiateBnplTransaction.outputs.loanTransactionId
        requestBody:
          contentType: application/json
          payload: |
            {
              "status": "Completed"
            }
        successCriteria:
          - condition: $statusCode == 204
        outputs:
          finalizedPaymentPlan: $steps.retrievePaymentPlan.outputs.finalizedPaymentPlan
```

哇——这么多YAML。是的，机器喜欢它，但这种格式的美妙之处在于我们也可以利用工具将Arazzo渲染成以人为本的形式。Arazzo文档可以解析为类似这样的序列图：

## 启用自主式API使用

向AI驱动的API使用转变正在加速，确定性API工作流对于确保AI代理能够可靠地与API交互至关重要。Arazzo弥合了传统API使用者和AI代理之间的差距，提供了一个结构化、可验证的框架，消除了歧义并增强了互操作性，从而减少了厂商锁定。

无论您是自动化工作流、启用AI使用还是增强API治理，Arazzo都是释放下一代API驱动创新关键。

立即浏览[Arazzo规范](https://spec.openapis.org/arazzo/latest.html)了解更多信息。

[YouTube](https://youtube.com/thenewstack?sub_confirmation=1) 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。