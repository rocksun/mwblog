# 在2026年启动任何新智能体项目之前，我会安装的5项智能体技能

[![Ali Ibrahim](https://miro.medium.com/v2/resize:fill:64:64/1*zUrydUUwoXHPljyRx2anbA.png)](/?source=post_page---byline--bf1de4fe9175---------------------------------------)

按回车键或点击查看完整尺寸图像

![]()

本文最初发表于 [Agentailor 博客](https://blog.agentailor.com/posts/top-agent-skills-for-agent-builders-2026?utm_source=medium&utm_medium=article_intro&utm_campaign=top_agent_skills_26)。

## 引言

你的编程智能体可以编写代码、重构函数和调试错误。但它能设计生产级的提示词吗？能构建遵循最佳实践的MCP服务器吗？能评估你的智能体输出是否真的优秀吗？

[**智能体技能**](https://agentskills.io/) 为你的编程助手提供按需的专业知识。它们是包含 `SKILL.md` 文件的文件夹，其中包含你的智能体仅在相关时才加载的指令、工作流程和参考资料。没有上下文膨胀，无需手动设置。要深入了解技能如何工作以及如何构建自己的技能，请参阅 [**如何从头开始构建和部署智能体技能**](https://blog.agentailor.com/blog/how-to-build-and-deploy-agent-skill-from-scratch)。

以下是涵盖智能体开发生命周期（从设计提示词到评估输出）的5项技能。列出的每项技能都适用于 Claude Code、Cursor、VS Code Copilot、Codex 和 Gemini CLI。

要安装任何技能，请运行：

```
npx skills add <owner/repo> --skill <skill-name>
```

## 1. 提示词工程师

一项专业的提示词工程技能，教授你的智能体设计有效LLM提示词的高级技术。它涵盖系统提示词架构、少样本示例设计…