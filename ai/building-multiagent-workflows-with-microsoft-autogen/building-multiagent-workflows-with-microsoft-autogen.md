<!--
title: 微软AutoGen：构建多智能体工作流的艺术
cover: https://cdn.thenewstack.io/media/2025/10/a54300f1-agents.jpg
summary: 多智能体AI系统让AI专家团队协作，相互辩论、纠错，解决复杂问题。微软AutoGen使多智能体协作易于实现，提升输出质量，减少幻觉，是“管理AI团队”的趋势。
-->

多智能体AI系统让AI专家团队协作，相互辩论、纠错，解决复杂问题。微软AutoGen使多智能体协作易于实现，提升输出质量，减少幻觉，是“管理AI团队”的趋势。

> 译自：[Building Multiagent Workflows With Microsoft AutoGen](https://thenewstack.io/building-multiagent-workflows-with-microsoft-autogen/)
> 
> 作者：Oladimeji Sowole

大多数AI实施方案都感觉像是只有一个非常聪明的实习生：有帮助，但视角单一，容易给出自信满满却错误的答案。但如果相反，你能组建一个由AI专家组成的小团队，他们在向你提出最终建议之前能相互辩论呢？

这正是当前行业正在发生的变化。组织正在超越基本的聊天机器人，转向选择能够解决真实复杂问题的[AI系统](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/)。微软的[AutoGen](https://microsoft.github.io/autogen/)引起了我的注意，因为它使这种多智能体协作变得出奇地容易实现。

我使用AutoGen进行了几个月的实验，其差异令人震惊。你不再是希望一个模型能给出正确答案，而是观察智能体相互质疑推理、发现错误并在此基础上提出新想法——这有点像无意中听到一场富有成效的头脑风暴会议。

当你处理混乱的现实世界问题时，这种方法变得至关重要：处理复杂的文档、综合来自多个来源的研究或生成需要实际运行的代码。单一智能体往往会错过细微之处，或者做出在孤立情况下看似合理但在审查下就会崩溃的假设。

以下是如何构建一个简单但有效率的多智能体系统。你将设置具有不同角色的智能体——一个专注于生成想法，另一个专注于批判它们——并观察它们如何协同工作，以产生比任何一个单独智能体所能达到的更好的结果。

到最后，你不仅会理解如何在技术上实现这一点，还会理解为什么它代表了我们看待AI在商业环境中角色的根本性转变。

## **为什么多智能体协作很重要**

传统的[大型语言模型（LLM）系统使用一个模型](https://thenewstack.io/getting-started-with-function-calling-in-llms/)来回答查询。但是如果该模型：

* 需要以前答案的上下文？
* 遗漏了重要事实？
* 能从结构化审查中受益？

多智能体系统通过分配角色来解决这些问题：

* 一个智能体负责规划。
* 另一个智能体生成输出。
* 第三个智能体进行批判。
* 用户代理收集并路由输入。

### **实际示例**

* 研究助手：分析师智能体搜索文档，摘要智能体进行浓缩，QA智能体验证事实。
* 编程智能体：用户定义规范，构建者智能体生成代码，评论智能体测试或审查代码。

## **AutoGen 分步教程**

### **1. 安装依赖项**

`pip install pyautogen openai`

**注意**：建议在安装Python包时使用虚拟环境，例如 [venv](https://docs.python.org/3/library/venv.html) 或 [conda](https://anaconda.org/anaconda/conda)。这有助于有效地管理依赖项并防止与其他项目发生冲突。

你需要一个 [OpenAI API 密钥](https://platform.openai.com/account/api-keys) 并访问 GPT-4 或 GPT-3.5 Turbo。安全地存储你的密钥：

`export OPENAI_API_KEY="your-openai-key"`

### **2. 创建智能体配置**

AutoGen 智能体使用类似 JSON 的字典进行配置。你定义：

* 角色（例如助手、用户、评论者）
* [LLM](https://thenewstack.io/build-scalable-llm-apps-with-kubernetes-a-step-by-step-guide/) 设置
* 行为标志（如自动回复、启用反馈）

```
llm_config = {
    "model": "gpt-4",
    "api_key": os.environ["OPENAI_API_KEY"],
    "temperature": 0.5
}
```

### **3. 创建用户代理智能体**

用户代理充当人类[用户和LLM智能体](https://thenewstack.io/how-ai-agents-will-change-the-web-for-users-and-developers/)之间的桥梁。它路由消息并可选地注入提示。

```
user_proxy = UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    code_execution_config={"work_dir": "./autogen_output"},
    llm_config=llm_config
)
```

如果你希望用户参与每个步骤，请设置 `human_input_mode="ALWAYS"`。否则，智能体将自动运行。

### **4. 创建任务助手智能体**

此智能体处理实际任务（答案生成、编码、摘要）。

```
assistant = AssistantAgent(
    name="assistant",
    llm_config=llm_config
)
```

### **5. 创建评论智能体（可选但功能强大）**

为了提高质量，引入第二个智能体来评估和改进助手智能体的输出。

```
critic = AssistantAgent(
    name="critic",
    system_message="You are a critic agent. Improve and verify the responses from other agents.",
    llm_config=llm_config
)
```

### **6. 设置协作工作流**

AutoGen 允许你定义群聊（智能体之间的多轮对话）或静态消息传递。以下是一个简单的用户-助手对话：

```
user_proxy.initiate_chat(assistant, message="Explain the concept of transfer learning in machine learning.")
```

为了评论智能体的参与，链式连接多个智能体：

```
def critic_loop(user_proxy, assistant, critic):
    user_proxy.initiate_chat(
        recipient=assistant,
        message="Write a Python function to calculate the Fibonacci sequence.",
        summary_method="last_msg"
    )
    assistant.initiate_chat(critic, message="Please review my previous response.")

critic_loop(user_proxy, assistant, critic)
```

这模拟了现实世界的协作：一个智能体完成任务，另一个智能体审查并可选地将输出路由回用户。

## **可选：多智能体群聊**

AutoGen 支持 GroupChatManager，它在回合制设置中协调多个智能体：

```
from autogen import GroupChat, GroupChatManager

groupchat = GroupChat(
    agents=[user_proxy, assistant, critic],
    messages=[],
    max_round=5
)

manager = GroupChatManager(groupchat=groupchat)
user_proxy.initiate_chat(manager, message="Design a plan to teach AI in high schools.")
```

这种结构允许每个智能体在多轮对话中增加价值，直到达成共识。

## **实际运行效果**

* 提示：“为一款环保牙膏设计营销活动。”
* 助手智能体响应：提出一个包含社交媒体和网红推广的三阶段计划。
* 评论智能体：指出未考虑预算限制。
* 最终答案：通过实际成本和A/B测试进行完善。

你刚刚构建了一个自我改进的自主思维伙伴关系。

## **高级扩展**

* 使用工具的智能体：配置[智能体来运行Python代码](https://thenewstack.io/building-autonomous-systems-in-python-with-agentic-workflows/)、查询API或搜索网络。
* 自我反思：让助手在发送响应之前进行自我审查。
* 自定义角色：定义“规划者”、“战略家”、“编码员”或“测试员”等智能体。

调用工具的助手示例：

```
AssistantAgent(..., code_execution_config={"use_docker": True})
```

## **商业和技术要点**

| **益处** | **对高管而言** | **对开发者而言** |
| --- | --- | --- |
| 模块化智能体 | 委托职责以提高可解释性和信任。 | 独立测试和调试角色。 |
| 对话驱动架构 | 模仿人类的工作流以进行审查和反馈。 | 易于复制敏捷式流程。 |
| 生产就绪 | 与OpenAI API和可插拔后端配合使用。 | 非常适合实验和后续部署。 |

## **最后思考**

使用单一AI模型通常感觉就像拥有一个聪明但孤立的顾问，你只能获得一个视角，要么接受，要么放弃。但如果能组建一个由AI专家组成的完整团队，他们能实际相互交流、辩论想法并纠正彼此的错误呢？

这就是微软AutoGen等多智能体系统的承诺。你不再是交叉手指，希望一个模型能给出正确答案，而是协调不同AI智能体之间的对话，每个智能体都发挥自己的优势。

我见过这种方法解决了让单一模型束手无策的问题。当智能体能够相互质疑推理、疑问假设并协同构建想法时，结果会明显更好。更少的幻觉，更细致的思考，以及感觉像是来自实际团队讨论的输出。

实际好处不容忽视：

* 当多个视角并行工作时，决策速度更快。
* 智能体在错误到达你之前就能发现它们。
* 你可以为不同领域（包括法律、金融和营销）创建专业智能体，并让他们结合专业知识。

那些及早弄清楚这一点的组织将拥有巨大的优势。我们正在从“使用AI”转向“管理AI团队”。那些成功实现这一转变的公司将成为引领者。