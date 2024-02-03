<!--
title: 用于基础设施即代码的生成式AI工具
cover: https://cdn.thenewstack.io/media/2024/01/b479226b-generative-ai-for-infrastructure-as-code-1024x576.jpg
-->

掌握生成式人工智能，优化代码生成、解释与调试，助力工作流程飞速前行。

> 译自 [Generative AI Tools for Infrastructure as Code](https://thenewstack.io/generative-ai-tools-for-infrastructure-as-code/)，作者 Parasar Kodati 在技术领域拥有长达两十年的经验，包括技术支持、工程、产品管理以及最为显著的技术推广等多个角色。

[基础设施即代码](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/)（IaC）帮助DevOps、IT运维和其他工程师在不断扩大、复杂化和多样化的动态IT环境中管理数据、应用程序和基础设施。通过GitOps驱动的工作流，工程师可以在不同环境中引入急需的标准化、安全性和操作一致性。

虽然有许多令人信服的理由支持采用IaC，但有一项创新使其更具优势：生成式人工智能（AI）。仅仅一年前，人们对于AI生成的代码的准确性存在很多怀疑。但是这项技术正在迅速发展，变得越来越成为IaC的关键推动因素，从最佳实践转变为不可或缺的战略。

OpenAI一直在领导产业，推出了ChatGPT等生成式AI工具，而Meta的LLAMA等其他强大的大语言模型（LLMs）也具备广泛的生成式AI能力。我的同事们在戴尔公司发表了一篇关于[构建通用型LLM环境](https://infohub.delltechnologies.com/t/design-guide-implementing-a-digital-assistant-with-red-hat-openshift-ai-on-dell-apex-cloud-platform-1/)的白皮书。

有许多生成式AI工具可用，可以帮助您加速工作流程、学习甚至职业发展。我将在这里描述其中一些功能。

## 代码生成

如果让我在每月理发和生成式代码助手订阅之间选择，我会选择后者。像GitHub Copilot这样的工具现在变得不可或缺——即使您只是在进行Shell脚本编写，更不用说编写复杂的Ansible Playbooks了。这些工具减少了创建自动化任务所需的代码基础块的时间，而且每一行生成的代码都包含了您高中英语老师会认可的有意义的注释。我的《[Ansible for OpenManage Enterprise](https://www.youtube.com/watch?v=fZQgtexO1t4&list=PL2nlzNk2-VMHsKVguetbetbmxd4eMfc_X&index=29)》视频展示了这些工具如何帮助您生成代码的许多示例。

## 代码解释

生成式AI模型可以解析和解释广泛的编程语言编写的代码，这得益于它们在数百万行代码的广泛训练。当您需要解释代码时，例如重构代码或尝试改进现有的自动化脚本时，使用代码提示LLM可能比使用纯英语更容易。以下是一个快速示例，我使用最新的ChatGPT 4模型生成了一个优秀的旧Shell脚本的Ansible等效版本。

我用于创建文件夹压缩备份的Shell脚本输入：

```bash
#!/bin/bash


# Set the directory to back up and the backup location
DIRECTORY_TO_BACKUP="/home/user/data"
BACKUP_LOCATION="/backup"
TIMESTAMP=$(date +"%F")
BACKUP_FILE="backup-$TIMESTAMP.tar.gz"


# Create the backup
tar -czf $BACKUP_LOCATION/$BACKUP_FILE $DIRECTORY_TO_BACKUP


# Check if the backup was successful
if [ $? -eq 0 ]; then
  echo "Backup completed successfully."
else
  echo "Backup failed." >&2
fi
```

初始的Ansible输出：

```yaml
---
- name: Create Backup of Directory
  hosts: all
  tasks:
    - name: Create backup file
      ansible.builtin.archive:
        path: /home/user/data
        dest: /backup/backup-{{ ansible_date_time.iso8601_basic_short }}.tar.gz
        format: gz
```

当我提示模型生成一个带有变量的更结构化代码块时，它返回：

```yaml
---
- name: Create Backup of Directory with Variables
  hosts: all
  vars:
    backup_source: /home/user/data # Define the source directory to back up
    backup_destination: /backup # Define the backup destination directory
    backup_filename: "backup-{{ ansible_date_time.iso8601_basic_short }}.tar.gz" # Backup filename with a timestamp
  tasks:
    - name: Create backup directory if it does not exist
      ansible.builtin.file:
        path: "{{ backup_destination }}"
        state: directory
        mode: '0755'


    - name: Create backup file
      ansible.builtin.archive:
        path: "{{ backup_source }}"
        dest: "{{ backup_destination }}/{{ backup_filename }}"
        format: gz
```

最新的ChatGPT界面支持附加文件，因此您无需复制粘贴需要重构的代码。只需组织好文件，然后将它们附加到您的提示中。

## 错误分析与调试

如果你认为将错误消息复制粘贴到Stack Overflow是调试代码的最佳方式，那就再想想吧。基于LLM的代码解释工具可以分析错误消息和日志，并在许多情况下识别经常发生的问题的根本原因。这适用于任何代码，包括Ansible Playbooks和Terraform模块，LLM可以迅速推荐修复措施，链接到相关文档，甚至可能自动化解决过程。

## 提示工程

编写提示已经成为确定LLM响应准确性的关键技能。您的提示越具体和详细，响应就越有用。以下是一些IaC的示例：

> “我正在进行一个Terraform项目，在其中我需要为AWS EC2实例进行配置，具体要求是：它应该是‘t2.micro’类型，在‘us-east-1’区域，并包含‘Name’标签为‘MyInstance’和‘Environment’标签为‘Development’。你能提供定义这个资源的Terraform代码片段吗？”

或者：

> “我需要创建一个Ansible playbook，执行一个常见的操作：在一组Ubuntu服务器上更新所有软件包。Playbook应该是幂等的，只能针对‘webservers’组的服务器。如果更新需要重新启动，它还必须仅重新启动‘nginx’服务。你能为这个playbook生成YAML代码吗？”

如果你正在致力于通过自动化改变世界，可以尝试类似这样的内容：

> “对于在DevOps环境中使用Python编写的自动化脚本，我需要一个强大的错误处理策略，它能将错误记录到文件并在发生关键故障时发送电子邮件通知。该脚本旨在自动化部署流程。你能提供一个演示这种错误处理的Python代码示例吗？”

有了这些强大的功能，请让一个代码助手来帮助你，即使你不得不跳过一些咖啡或理发。

## 创建你自己的GPT（全球项目工具）

如果你在浏览器中一直打开着一个ChatGPT标签，并且已经成为一个提示编写专家，那么你可以利用生成式AI做更多事情，而不仅仅是生成代码。

多亏了最近宣布的GPT模型和OpenAI的[Assistants API](https://platform.openai.com/docs/assistants/overview)，你可以创建一个定制的模型，它在响应速度和准确性方面更快更精确。你可以用任何东西训练GPT模型，比如政策文件、编码准则或IT基础设施大小计算器，并让聊天机器人使用这些后端模型来回答客户或内部利益相关者的查询（请注意，根据客户数量和使用情况，这些能力是有成本的）。

**定制GPT的关键元素：**

**代码解释器**：这与ChatGPT或GitHub Copilot中的编码能力没有太大区别。在创建定制GPT时，包括一个选项，用户可以选择是否要使用代码解释器。这是因为Assistants API采用的是按使用量计费模型；不需要此功能的用户可以取消选择。

**知识检索**：由人工智能提供支持的知识检索系统可以即时检索与手头任务相关的技术文档和最佳实践，无论是制作Ansible Playbook还是在Terraform中定义资源。这种对信息的即时访问加速了开发过程，并有助于在各个平台上保持行业标准。

**自定义功能**：如果您已经构建了用于计算或做决策的脚本和例程，您可以将它们整合到您的自定义GPT中。我最近看到一个例子，其中投资回报率（ROI）计算器被整合到一个聊天机器人中，以帮助网站访问者评估转换为太阳能的好处。您可以为目标终端用户创建一个大小估算工具或性能基准测试工具。

## 关于专有和敏感数据的注意事项

虽然大型语言模型是程序员长期以来最好的东西，但在使用非公开数据训练AI模型时要极度谨慎。根据用例，在使用敏感或专有数据的提示或用于训练的知识文档中设置严格的防护措施。如果您的组织没有这样的防护措施，您可以成为创建它们的倡导者，并参与帮助组织实现更高的AI采用成熟度。

## 了解更多

Dell一直是企业领先的人工智能[基础设施提供商](https://www.dell.com/en-us/dt/solutions/artificial-intelligence/index.htm#scroll=off&accordion0)。以下是一些其他资源，了解有关为大型语言模型培训设置基础设施的更多信息：

- [戴尔科技的人工智能，包括首席技术官John Roese引人深思的演讲](https://www.dell.com/en-us/blog/ai-at-dell-technologies/)
- [戴尔与Meta合作推动生成式人工智能创新](https://www.dell.com/en-us/blog/dell-and-meta-collaborate-to-drive-generative-ai-innovation/)
- [Llama 2：单一图形处理单元上的推理](https://infohub.delltechnologies.com/t/llama-2-inferencing-on-a-single-gpu/)
- [企业中的生成式人工智能 — 推理](https://infohub.delltechnologies.com/t/design-guide-generative-ai-in-the-enterprise-inferencing/)
