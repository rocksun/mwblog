重构过去仅限于IDE中硬编码的固定转换集。如果你需要的转换不包含在内，你就束手无策，只能采取困难的方式。支持模型上下文协议（MCP）工具的AI辅助IDE改变了这一局面。向它们展示各种模式的修改前后示例，它们就能在没有明确支持的情况下找出所有类型的转换。

例如，这是我用来清理不必要使用 [Fragment](https://docs.xmlui.org/components/Fragment) 组件的 [XMLUI](https://thenewstack.io/make-react-components-with-xmlui-a-visual-basic-for-the-ai-era/) 应用程序的提示：

[![](https://jonudell.info/newstack/refactor-01.png)](https://jonudell.info/newstack/refactor-01.png)

我让 Claude、Cursor 和 Codex 处理一个包含 XMLUI 应用程序的目录，其中包含了根据这些规则应或不应重构的 `Fragment` 用法。所有工具都产生了相同的正确差异。传统方法需要使用一个 XMLUI 解析器，该解析器能够区分 `when` 属性与（如 `gap`）等其他属性并采取相应行动。大型语言模型（LLM）并非如此工作；它们是通用模式识别器，我与它们合作的[七项原则](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)之一是：*利用模式识别*。

## 提取组件以减少重复

在 XMLUI 中创建[用户定义组件](https://docs.xmlui.org/components-intro)以封装重复很容易。当你只做一次时，没有必要。当你再次做，并且有变化时，你可能会开始考虑将共同的部分提取到一个组件中。但通常需要更多的重复和更多的变化，才能明确组件应该体现的共同核心是什么。在允许变化发生以发现真正共同之处与整合为更具可读性和可维护性的代码之间，一直存在着张力。LLM可以缓解这种张力。

假设你发现自己在做类似这样的事情：

```
<!-- before -->
<HStack>
  <VStack>
    <Text variant="secondary" fontSize="$fontSize-sm">Cloud Cover</Text>
    <Text fontWeight="semibold" fontSize="$fontSize-lg">
      {condition.cloudcover}%
    </Text>
  </VStack>


  <VStack>
    <Text variant="secondary" fontSize="$fontSize-sm">Humidity</Text>
    <Text fontWeight="semibold" fontSize="$fontSize-lg">
      {condition.humidity}%
    </Text>
  </VStack>


  <VStack>
    <Text variant="secondary" fontSize="$fontSize-sm">Wind Speed</Text>
    <Text fontWeight="semibold" fontSize="$fontSize-lg">
      {condition.windspeedMiles} mph
    </Text>
  </VStack>
</HStack>
```

你可能会意识到这样更好：

```
<!-- after -->
<HStack>
  <WeatherStat
 label="Cloud Cover"
 value="{condition.cloudcover}%"
  />
  <WeatherStat
 label="Humidity"
 value="{condition.humidity}%"
  />
  <WeatherStat
 label="Wind Speed"
 value="{condition.windspeedMiles} mph"
  />
</HStack>


<!-- a new component -->
<Component name="WeatherStat">
  <VStack
 gap="$space-1"
 minWidth="8rem"
  >
    <Text
 variant="secondary"
 fontSize="$fontSize-sm"
    >
      {$props.label}
    </Text>
    <Text fontWeight="semibold">
      {$props.value}
    </Text>
  </VStack>
</Component>
```

我们常常懒于应用这种转换，但懒惰有时也是一种美德。如果你没有看到足够多和足够多样化的*之前*案例，你可能还不知道*之后*应该是什么样子。AI助手可以让实验变得廉价而流畅。

## 利用AI协作规划代码变更

[AWS Kiro](https://thenewstack.io/aws-kiro-testing-an-ai-ide-with-a-spec-driven-approach/) 邀请你以规范模式（Spec mode）操作，在该模式下，你可以协作编写需求、设计文档和任务清单。根据我的经验，它的能力常常超出其掌握范围，我曾放弃过几个清单。但这个想法以一种不那么正式的方式扎根，并现在融入了 Claude Code 和 Codex 的对话式使用中。

当我让 Claude 为一个由 XMLUI 初学者开发者构建的应用程序[实现一个认证门](https://docs.xmlui.org/howto/implement-an-authentication-gate)时，它识别出了所有需要更改的用户定义组件，列举了它建议进行的更改，并指出了一个需要特殊处理的组件。

*Customers.xmlui has a pattern close to the standard but with some differences:*  
*– Uses contact\_id for routes, but id for API URLs*  
*– Only has “Mark as inactive” (no status toggle)*  
*– Delete APICall is outside the DropdownMenuI need to update the component to support different ID fields for routes vs API calls.*  
*Let me do that first.*

该应用程序还对处理批量 API 调用的 [Queue](https://docs.xmlui.org/components/Queue) 组件进行了不必要的利用。在这种情况下，不需要 `Queue`，因为后端提供了批量 API。这项更改涉及删除多余的内容并添加对批量 API 的调用。以下是计划：

*1. Remove the Queue (lines 106-143)*  
*2. Remove unnecessary variables (lines 4-7): var.action, var.processedCount, var.errorCount, var.completed*  
*3. Replace the bulk action buttons (lines 84-104) to call APICall components instead of Queue*  
*4. Add APICall components following the pattern you described:*  
*– POST /contacts/active with body: {contact\_ids: […], organization\_id: 906441453}*  
*– POST /contacts/inactive with body: {contact\_ids: […], organization\_id: 906441453}*  
*– DELETE /contacts/{ids} for bulk delete*

在这种情况下，事情完全按计划进行。虽然通常情况并非如此，但 AI 辅助编程的[对话式风格](https://thenewstack.io/lets-talk-conversational-software-development/)有助于我在工作进行中调整计划。

## 通过更简洁的代码限制软件负债

正如 [Cory Doctorow](https://doctorow.medium.com/) 最近观察到的，[代码是负债（而非资产）](https://doctorow.medium.com/https-pluralistic-net-2026-01-06-1000x-liability-graceful-failure-modes-d69f384af9e4)。他说，科技老板们不知道这一点。

“They think they’ve found a machine that produces assets at 10,000 times the rate of a human programmer. They haven’t. They’ve found a machine that produces liability at 10,000 times the rate of any human programmer.”

对于 Bruce Schneier 来说，这种负债会带来[法律和财务](https://www.schneier.com/essays/archives/2003/11/liability_changes_ev.html)风险，软件制造商需要通过保险政策来缓解，这些政策会使发布不安全或有缺陷的产品成本高昂。AI 辅助编码会增加软件负债吗？当然，如果使用不当的话。但两件事可以同时成立。审慎使用 AI 也可以帮助我们减少负债，因为它让持续重构变得更容易、更安全，从而保持代码库精简和干净。

## 借助AI辅助应用创造性洞察

在移除了 `Queue` 的多余用法后，仍然存在重复使用 [APICall](https://docs.xmlui.org/components/APICall) 来在一套用户定义组件中实现相似模式的情况。鉴于 `APICall` 无法封装在声明式用户定义组件中，如何进行整合呢？我意识到 `APICall` 的命令式“表亲” [Actions.callAPI](https://docs.xmlui.org/globals#actionscallapi) 可以在 `onClick` 处理程序中使用，从而避免了声明单独的 `APICall` 组件的需要。这并非立竿见影的胜利；它只是将声明式属性转移到了命令式参数中。但在命令式领域，为不同情况定义参数家族变得更容易。例如，在处理一批项目时，操作的名称可能是*标记为活动*或*删除*，其进行中的消息可能是*正在标记为活动*或*正在删除*，其完成消息可能是*已标记为不活动*或*已删除*。

将这种变化封装在一个函数中使代码更整洁，但也带来了一个新的重构挑战。每个组件都需要该函数的一个变体。它们如何共享一个共同的函数呢？[AppState](https://docs.xmlui.org/components/AppState) 提供了一个全局键/值存储，对应用程序中的所有用户定义组件都可见。它通常用于存储简单值，但我意识到也可以在那里存储箭头函数。LLM 不会发现这种[创造性洞察](https://thenewstack.io/human-insight-llm-grunt-work-creative-publishing-solution/)，但当你发现时，它们可以帮助你验证和应用它。在这种情况下，Claude 编写了一个快速测试来证明它会起作用，然后将一组类似的函数合并到一个公共全局函数中。

## 编码中的“少即是多”方法

[Bill Gates](https://en.wikipedia.org/wiki/Bill_Gates) 在很久以前的一次采访中对我说的最令人难忘的话是：“一切都与编写更少的代码有关。”LLM 喜欢编写代码，如果滥用，它们会生成超出我们想要或需要的代码。代码*是*一种负债。我们有责任控制 LLM 的生成本能，并将其集中于限制这种负债所需的重构。我们决定何时以及如何重构，它们执行机械转换——这是一个持续的对话。旨在生成大量代码的工具，反而可以帮助我们编写更少的代码。