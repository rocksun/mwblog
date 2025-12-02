<!--
title: MCP驱动代码执行：构建超高效智能体
cover: https://res.cloudinary.com/dkrpg71cx/image/upload/v1764659153/oh6dzemhdxkt3pskix9e.png
summary: MCP连接AI代理，但传统方法导致token消耗高。代码执行使MCP代理更高效，减少token用量，提升上下文管理、隐私及工具重用能力。
-->

MCP连接AI代理，但传统方法导致token消耗高。代码执行使MCP代理更高效，减少token用量，提升上下文管理、隐私及工具重用能力。

> 译自：[Code execution with MCP: Building more efficient agents](https://www.anthropic.com/engineering/code-execution-with-mcp)
> 
> 作者：[no-author]

[模型上下文协议 (MCP)](https://modelcontextprotocol.io/) 是连接 AI 代理到外部系统的开放标准。传统上，将代理连接到工具和数据需要为每个配对进行定制集成，这会造成碎片化和重复工作，使得真正互联系统的扩展变得困难。MCP 提供了一个通用协议——开发人员只需在他们的代理中实现一次 MCP，即可解锁整个集成生态系统。

自 2024 年 11 月 MCP 发布以来，其普及速度非常快：社区已经构建了数千个 [MCP 服务器](https://github.com/modelcontextprotocol/servers)，所有主流编程语言都提供了 [SDK](https://modelcontextprotocol.io/docs/sdk)，并且行业已将 MCP 采纳为连接代理到工具和数据的实际标准。

如今，开发人员通常构建的代理可以访问数十个 MCP 服务器上的数百或数千个工具。然而，随着连接工具数量的增长，预先加载所有工具定义并将中间结果通过上下文窗口传递会降低代理速度并增加成本。

在这篇博客中，我们将探讨代码执行如何使代理更有效地与 MCP 服务器交互，在处理更多工具的同时使用更少的 token。

## **工具过度消耗 token 降低了代理效率**

随着 MCP 使用规模的扩大，有两种常见模式可能会增加代理成本和延迟：

1.  工具定义使上下文窗口过载；
2.  中间工具结果消耗额外的 token。

### **1. 工具定义使上下文窗口过载**

大多数 MCP 客户端会预先将所有工具定义直接加载到上下文，使用直接工具调用语法将其暴露给模型。这些工具定义可能看起来像：

```
gdrive.getDocument
     Description: Retrieves a document from Google Drive
     Parameters:
                documentId (required, string): The ID of the document to retrieve
                fields (optional, string): Specific fields to return
     Returns: Document object with title, body content, metadata, permissions, etc.
```

```
salesforce.updateRecord
    Description: Updates a record in Salesforce
    Parameters:
               objectType (required, string): Type of Salesforce object (Lead, Contact,      Account, etc.)
               recordId (required, string): The ID of the record to update
               data (required, object): Fields to update with their new values
     Returns: Updated record object with confirmation
```

工具描述占据了更多的上下文窗口空间，增加了响应时间和成本。在代理连接到数千个工具的情况下，它们在读取请求之前需要处理数十万个 token。

### **2. 中间工具结果消耗额外的 token**

大多数 MCP 客户端允许模型直接调用 MCP 工具。例如，你可能会问你的代理：“从 Google 云端硬盘下载我的会议记录并将其附加到 Salesforce 销售线索。”

模型将进行如下调用：

```
TOOL CALL: gdrive.getDocument(documentId: "abc123")
        → returns "Discussed Q4 goals...\n[full transcript text]"
           (loaded into model context)

TOOL CALL: salesforce.updateRecord(
			objectType: "SalesMeeting",
			recordId: "00Q5f000001abcXYZ",
  			data: { "Notes": "Discussed Q4 goals...\n[full transcript text written out]" }
		)
		(model needs to write entire transcript into context again)
```

每个中间结果都必须通过模型。在此示例中，完整的通话记录流经两次。对于一个 2 小时的销售会议，这可能意味着额外处理 50,000 个 token。即使是更大的文档也可能超出上下文窗口限制，从而中断工作流程。

对于大型文档或复杂数据结构，模型在工具调用之间复制数据时更容易出错。

![展示 MCP 客户端如何与 MCP 服务器和 LLM 协作的图像。](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F9ecf165020005c09a22a9472cee6309555485619-1920x1080.png&w=1920&q=75)

MCP 客户端将工具定义加载到模型的上下文窗口中，并编排一个消息循环，其中每个工具调用和结果在操作之间都会通过模型。

## **使用 MCP 进行代码执行可提高上下文效率**

随着代码执行环境在代理中变得越来越普遍，一种解决方案是将 MCP 服务器呈现为代码 API，而不是直接工具调用。然后，代理可以编写代码与 MCP 服务器交互。这种方法解决了这两个挑战：代理只加载其所需的工具，并在执行环境中处理数据，然后将结果传回模型。

有多种方法可以做到这一点。一种方法是从连接的 MCP 服务器生成所有可用工具的文件树。这是一个使用 TypeScript 的实现：

```
servers
├── google-drive
│   ├── getDocument.ts
│   ├── ... (other tools)
│   └── index.ts
├── salesforce
│   ├── updateRecord.ts
│   ├── ... (other tools)
│   └── index.ts
└── ... (other servers)
```

然后每个工具对应一个文件，例如：

```
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput {
  documentId: string;
}

interface GetDocumentResponse {
  content: string;
}

/* Read a document from Google Drive */
export async function getDocument(input: GetDocumentInput): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>('google_drive__get_document', input);
}

```

我们上面 Google 云端硬盘到 Salesforce 的示例变为以下代码：

```
// Read transcript from Google Docs and add to Salesforce prospect
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

const transcript = (await gdrive.getDocument({ documentId: 'abc123' })).content;
await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});

```

代理通过探索文件系统来发现工具：列出 `./servers/` 目录以查找可用的服务器（如 `google-drive` 和 `salesforce`），然后读取其所需的特定工具文件（如 `getDocument.ts` 和 `updateRecord.ts`）以了解每个工具的接口。这使得代理只加载当前任务所需的定义。这将 token 使用量从 150,000 个减少到 2,000 个——节省了 98.7% 的时间和成本**。**

Cloudflare [发布了类似的发现](https://blog.cloudflare.com/code-mode/)，将使用 MCP 进行的代码执行称为“代码模式”。核心洞察是相同的：LLM 擅长编写代码，开发人员应该利用这一优势来构建更有效率地与 MCP 服务器交互的代理。

## **使用 MCP 进行代码执行的好处**

使用 MCP 进行代码执行使代理能够更有效地利用上下文，通过按需加载工具、在数据到达模型之前进行过滤以及一步执行复杂逻辑来实现。这种方法还具有安全性和状态管理方面的好处。

### 渐进式披露

模型非常擅长导航文件系统。将工具作为文件系统上的代码呈现，允许模型按需读取工具定义，而不是预先读取所有定义。

或者，可以在服务器上添加一个 `search_tools` 工具来查找相关定义。例如，在使用上面假设的 Salesforce 服务器时，代理会搜索“salesforce”并只加载当前任务所需的工具。在 `search_tools` 工具中包含一个详细级别参数，允许代理选择所需的详细程度（例如仅名称、名称和描述，或包含模式的完整定义），这也有助于代理节省上下文并高效地查找工具。

### 上下文高效的工具结果

处理大型数据集时，代理可以在返回结果之前在代码中过滤和转换结果。考虑获取一个 10,000 行的电子表格：

```
// Without code execution - all rows flow through context
TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
        → returns 10,000 rows in context to filter manually

// With code execution - filter in the execution environment
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(row => 
  row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // Only log first 5 for review
```

代理看到的是五行而不是 10,000 行。类似的模式适用于聚合、跨多个数据源的连接或提取特定字段——所有这些都不会使上下文窗口膨胀。

#### **更强大、上下文高效的控制流**

循环、条件和错误处理可以使用熟悉的编码模式完成，而不是串联单个工具调用。例如，如果你需要在 Slack 中接收部署通知，代理可以编写：

```
let found = false;
while (!found) {
  const messages = await slack.getChannelHistory({ channel: 'C123456' });
  found = messages.some(m => m.text.includes('deployment complete'));
  if (!found) await new Promise(r => setTimeout(r, 5000));
}
console.log('Deployment notification received');
```

这种方法比通过代理循环在 MCP 工具调用和休眠命令之间交替更有效率。

此外，能够编写一个可执行的条件树也节省了“首个 token 时间”延迟：代理可以由代码执行环境来评估 if 语句，而无需等待模型。

### 隐私保护操作

当代理使用 MCP 进行代码执行时，中间结果默认保留在执行环境中。这样，代理只看到你明确记录或返回的内容，这意味着你不想与模型共享的数据可以在你的工作流程中流动，而无需进入模型的上下文。

对于更敏感的工作负载，代理驱动程序可以自动对敏感数据进行 token 化处理。例如，假设你需要将客户联系方式从电子表格导入 Salesforce。代理编写：

```
const sheet = await gdrive.getSheet({ sheetId: 'abc123' });
for (const row of sheet.rows) {
  await salesforce.updateRecord({
    objectType: 'Lead',
    recordId: row.salesforceId,
    data: { 
      Email: row.email,
      Phone: row.phone,
      Name: row.name
    }
  });
}
console.log(`Updated ${sheet.rows.length} leads`);
```

MCP 客户端在数据到达模型之前拦截并对 PII 进行 token 化处理：

```
// What the agent would see, if it logged the sheet.rows:
[
  { salesforceId: '00Q...', email: '[EMAIL_1]', phone: '[PHONE_1]', name: '[NAME_1]' },
  { salesforceId: '00Q...', email: '[EMAIL_2]', phone: '[PHONE_2]', name: '[NAME_2]' },
  ...
]
```

然后，当数据在另一个 MCP 工具调用中共享时，通过 MCP 客户端中的查找进行反 token 化。真实的电子邮件地址、电话号码和姓名从 Google 表格流向 Salesforce，但从不通过模型。这可以防止代理意外记录或处理敏感数据。你还可以使用它来定义确定性安全规则，选择数据可以流向何处以及从何处流出。

### 状态持久化和技能

具有文件系统访问权限的代码执行允许代理在操作之间维护状态。代理可以将中间结果写入文件，从而使它们能够恢复工作并跟踪进度：

```
const leads = await salesforce.query({ 
  query: 'SELECT Id, Email FROM Lead LIMIT 1000' 
});
const csvData = leads.map(l => `${l.Id},${l.Email}`).join('\n');
await fs.writeFile('./workspace/leads.csv', csvData);

// Later execution picks up where it left off
const saved = await fs.readFile('./workspace/leads.csv', 'utf-8');
```

代理还可以将自己的代码持久化为可重用函数。一旦代理为某个任务开发出可用的代码，它就可以保存该实现以供将来使用：

```
// In ./skills/save-sheet-as-csv.ts
import * as gdrive from './servers/google-drive';
export async function saveSheetAsCsv(sheetId: string) {
  const data = await gdrive.getSheet({ sheetId });
  const csv = data.map(row => row.join(',')).join('\n');
  await fs.writeFile(`./workspace/sheet-${sheetId}.csv`, csv);
  return `./workspace/sheet-${sheetId}.csv`;
}

// Later, in any agent execution:
import { saveSheetAsCsv } from './skills/save-sheet-as-csv';
const csvPath = await saveSheetAsCsv('abc123');
```

这与 [技能](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) 的概念紧密相关，技能是可重用指令、脚本和资源的文件夹，用于提高模型在专业任务上的性能。将 SKILL.md 文件添加到这些已保存的函数中，可以创建模型可以引用和使用的结构化技能。随着时间的推移，这使得你的代理能够构建一个更高层次能力的工具箱，发展其有效工作所需的支架。

请注意，代码执行引入了其自身的复杂性。运行代理生成的代码需要一个安全的执行环境，具有适当的[沙盒隔离](https://www.anthropic.com/engineering/claude-code-sandboxing)、资源限制和监控。这些基础设施要求增加了直接工具调用所避免的运营开销和安全考虑。代码执行的好处——降低 token 成本、更低的延迟和改进的工具组合——应该与这些实施成本进行权衡。

## **总结**

MCP 为代理连接到许多工具和系统提供了基础协议。然而，一旦连接了过多的服务器，工具定义和结果会消耗过多的 token，降低代理效率。

尽管这里提到的许多问题（上下文管理、工具组合、状态持久化）感觉新颖，但它们在软件工程中都有已知的解决方案。代码执行将这些已建立的模式应用于代理，让他们可以使用熟悉的编程构造更有效地与 MCP 服务器交互。如果你采用这种方法，我们鼓励你与 [MCP 社区](https://modelcontextprotocol.io/community/communication) 分享你的发现。

### 致谢

*本文由 Adam Jones 和 Conor Kelly 撰写。感谢 Jeremy Fox、Jerome Swannack、Stuart Ritchie、Molly Vorwerck、Matt Samuels 和 Maggie Vo 对本文草稿的反馈。*