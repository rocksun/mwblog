如果你曾使用 Lovable 或 Replit 等 AI 工具构建过不仅仅是快速原型的东西，你很可能感受过扩展第一版本所带来的阻力。一次小小的代码重构可能会引发新错误，一个新功能可能会破坏旧逻辑，进展开始感觉像是返工而不是迭代。

这种模式并非偶然。大多数 AI 编码工具旨在快速生成代码，而不是随时间推移保持结构。虽然它们可以创建可用的 API 和函数，但它们没有建立一个总体架构来连接和组织它们。结果是一个单一的、功能性的代码库，其隔离性有限、所有权不明确，并且没有可靠的重用路径。始于快速开发的很快就变成了返工。

从 AI 代码生成到可组合架构的演变，改变了 AI 如何适应现实世界的软件开发。开发人员不再一次性生成整个文件，而是可以使用 AI 创建可插入更广泛架构的独立模块。这种方法更符合团队维护、测试和发布生产代码的方式。

在本文中，我将详细介绍这是怎样的。

我将首先请一个 AI [助手生成代码](https://thenewstack.io/how-generative-ai-coding-assistants-increase-developer-velocity/)，用于一个小型可运行的 React 应用，并检查其结构。接下来，我将找出在进行更改或添加新功能时，架构在哪里产生了摩擦。最后，我将使用可组合工作流重建同一个应用，该工作流强制执行边界、版本跟踪和模块化重用，将相同的生成代码转化为可以可持续增长的软件。

## **让我们生成应用**

为了测试可组合性，我请 Cursor 使用单个提示生成了一个完整的 React 任务管理器应用程序。

这个请求反映了大多数开发人员与 AI 工具交互的方式：描述一次需求，然后让模型提供完整的实现建议。

```
Create a complete React task manager application.


Requirements:
Login/logout flow with mock authentication (username/password check against hardcoded data).
After logging in, display a Dashboard page with a task list.
Allow adding and deleting tasks.
Store the authentication state in local storage so that the session persists after refresh.
Use React functional components with hooks.
Include basic error handling and loading states.
```

下面是生成的任务管理器及其文件结构。完整代码也可在[此 GitHub 仓库](https://github.com/ThatCoolGuyyy/ai-generated-task-manager)中获取。

[![](https://cdn.thenewstack.io/media/2025/12/32026aa7-image2-1024x554.png)](https://cdn.thenewstack.io/media/2025/12/32026aa7-image2-1024x554.png)

AI 生成的任务管理器

```
src/
├── App.css                   
├── App.js                    
├── App.test.js                
├── index.css                  
├── index.js                  
├── logo.svg                   
├── reportWebVitals.js         
├── setupTests.js              
├── components/               
│   ├── Dashboard.css          
│   ├── Dashboard.js          
│   ├── Login.css              
│   └── Login.js              
└── contexts/                 
    └── AuthContext.js  
```

乍一看，项目结构看起来很熟悉且可用。该应用成功编译并运行，提供了身份验证、仪表板以及通过本地存储实现持久的任务管理，完全符合提示中的要求。

然而，真正的问题不是应用程序是否运行，而是文件是如何构建的。目前的架构缺乏清晰的边界。逻辑、状态和呈现相互交织。这种结构中没有任何东西强制执行模块化、重用或版本控制。

这就是可组合架构缺失的地方变得显而易见。

最好的 AI 代码生成器可以生成可运行的应用程序，但它们很少定义系统。如果没有状态和 UI 之间的隔离、清晰的逻辑所有权或组件之间的明确契约，每个功能都会变得相互依赖。

在下一节中，我将更仔细地检查这个应用程序的结构，突出显示架构捷径在哪里造成了摩擦。

## **Cursor 生成应用的问题**

当评估生成的任务管理器的长期可维护性时，其结构显示出明显的局限性。这些弱点不在于语法或 React 模式，而在于系统的组成。

以下示例说明了这些结构性缺陷如何在代码中体现。

1.  **组件之间没有属性边界**

**发生位置：** *App.js*（第 9-22 行）

```
const ProtectedRoute = ({ children }) => {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div className="loading-container">
        <div className="spinner"></div>
        <p>Loading...</p>
      </div>
    );
  }

  return user ? children : <Navigate to="/login" replace />;
};
```

`ProtectedRoute` 接受任何 `children` 元素，没有任何限制。没有定义的接口解释可以传递哪种组件、它应该接收哪些属性或它依赖于什么数据上下文。

在一个更大的应用程序中，这会导致脆弱的集成点。没有明确的边界，路由逻辑中的一个小改动可能会悄无声息地影响其中嵌套的每个组件。

每个组件都应该定义其接口和依赖项。在可组合系统中，这通过类型化的属性、契约或模式定义来实现，这些定义描述了每个单元消耗和暴露的内容。

2.  **零测试覆盖率**

**发生位置：** *App.test.js*（第 4-8 行）

```
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
```

唯一的测试检查了 React 启动模板是否渲染，所有实际的应用程序逻辑都未经验证。身份验证、状态持久性和任务更新在没有任何自动化防护措施的情况下运行。

没有单元测试或集成测试，系统就没有可测量的反馈循环。每次更改都可能引入回归，这些回归在运行时之前一直不可见。

每个模块都应该具有已定义且可测试的行为。独立的测试作为系统的组合边界，确保一个区域的更改不会悄无声息地改变另一个区域。

3.  **关注点分离不佳**

**发生位置：** *Dashboard.js*（第 32-52 行）

```
const handleAddTask = async (e) => {
  e.preventDefault();

  if (!newTask.trim()) {
    setError('Task description cannot be empty');
    return;
  }

  setLoading(true);
  setError('');

  await new Promise(resolve => setTimeout(resolve, 500));

  const task = {
    id: Date.now().toString(),
    text: newTask.trim(),
    completed: false,
    createdAt: new Date().toISOString()
  };

  setTasks(prev => [task, ...prev]);
  setNewTask('');
  setLoading(false);
};
```

`handleAddTask` 函数将事件处理、验证、API 模拟和状态更新组合在一起，使得测试或替换任何一个部分都变得困难。

随着应用程序的增长，添加新功能将需要重写此逻辑，而不是通过独立的模块进行扩展。

逻辑、状态和呈现应该相互独立地演变，使系统能够在不要求重写整个组件的情况下进行适应。

4.  **紧密耦合的状态**

**发生位置：** *AuthContext.js*（第 19-21 行）

```
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
```

身份验证状态直接存在于 provider 组件内部。所有更新、持久化逻辑和 API 处理都绑定到一个单一的上下文。

这种耦合阻止了可重用性。身份验证逻辑无法在项目之间共享或替换为不同的实现，因为状态不可移植或参数化。

应用程序状态应该有明确的所有权，并存在于使用它的组件之外。这种分离使状态在不同上下文中可重用和可移植。

5.  **没有重用路径**

**发生位置：** *AuthContext.js*（第 6-9 行，第 32-52 行）

```
const MOCK_USERS = [
  { username: 'admin', password: 'password123', name: 'Admin User' },
  { username: 'user', password: 'user123', name: 'Regular User' }
];

const login = async (username, password) => {
  setLoading(true);
  await new Promise(resolve => setTimeout(resolve, 1000));
  const foundUser = MOCK_USERS.find(
    u => u.username === username && u.password === password
  );
  if (foundUser) {
    const userData = { username: foundUser.username, name: foundUser.name };
    setUser(userData);
    localStorage.setItem('user', JSON.stringify(userData));
    setLoading(false);
    return { success: true };
  } else {
    setLoading(false);
    return { success: false, error: 'Invalid username or password' };
  }
};
```

模拟用户直接硬编码到身份验证上下文中，没有抽象或配置层。这使得身份验证逻辑与应用程序紧密耦合，导致在不重写整个上下文的情况下无法集成新的提供者。

身份验证应该通过接口来定义，允许提供者无缝切换，而无需修改内部逻辑。

## **使用可组合架构进行重建**

AI 工具生成的代码中的问题并非 Cursor 独有。它们几乎出现在所有优先考虑代码完成而非架构意图的 AI 生成项目中。为了纠正这些问题，[开发人员需要改变他们的实践，以基于模块化组合生成代码](https://thenewstack.io/ai-generated-code-needs-refactoring-say-76-of-developers/)。

可组合架构始于指导代码生成过程的架构计划。在编写任何逻辑之前，系统会定义其结构，包括存在哪些单元、它们如何通信以及状态和行为位于何处。一旦设定了这些边界，AI 就可以安全地为该结构中的每个组件生成代码。输出变成了一个版本化的模块网络，而不是一个单一的、未跟踪的代码库。

这种方法是 [Hope AI](https://bit.cloud/products/hope-ai?c=new) 和 [Bit Cloud](https://bit.cloud/?c=new) 共同实现的。Hope AI 通过架构优先的工作流生成代码，而 Bit Cloud 则提供存储、版本化和重用每个生成组件的系统。它们共同展示了 AI 辅助代码生成如何演变为可重复的软件开发过程。

重建遵循三个结构化步骤：

### **步骤 1：代码之前定义架构**

开发过程从架构提案开始。开发人员描述高级设计，例如，将逻辑分离到服务、钩子和 UI 层中，AI 在编写一行代码之前会返回该结构的图表。

对于我们的任务管理器，Hope AI 提出了以下布局：

[![](https://cdn.thenewstack.io/media/2025/12/2fe61ec2-image1.png)](https://cdn.thenewstack.io/media/2025/12/2fe61ec2-image1.png)

Hope AI 架构

这个架构布局已经解决了几个早期问题：

*   **页面**处理导航级逻辑（登录、仪表板）。
*   **UI 组件**专注于渲染和交互（任务项、添加任务）。
*   **钩子**封装状态和数据（use-tasks、use-auth）。
*   **根应用**连接这些部分，而无需直接嵌入逻辑。

通过在生成之前审查此结构，开发人员可以调整边界，例如，请求一个 `services/TaskService` 来隔离异步逻辑。

这个架构检查点将 AI 从代码生产者转变为设计协作者。

### **步骤 2：组件生成**

架构批准后，Hope AI 将每个组件生成为独立的、可测试的单元。它不是组装一大堆文件，而是生成具有清晰职责的小型模块化组件，每个组件都包含本地测试、文档和使用预览。

例如，`useAuth` 钩子被生成为一个可重用函数，而不是一段内联逻辑：

```
export function useAuth(): UseAuthValue {
  const [currentUser, setCurrentUser] = useState<User | null>(null);
  const [isAuthLoading, setIsAuthLoading] = useState(true);

  useEffect(() => {    
  }, []);

  const login = useCallback(async (username: string, password: string): Promise<void> => {
  }, []);

  const logout = useCallback(() => {
  }, []);
```

还创建了一个匹配的测试文件 `use-tasks.spec.tsx` 来验证钩子的行为：

```
describe('useAuth', () => {
  beforeEach(() => {
    localStorage.clear();
  });

  it('should initialize with user data from localStorage if it exists', () => {
    const mockUser = { id: '123', username: 'testuser' };
    localStorage.setItem('app-auth-session', JSON.stringify(mockUser));

    const { result } = renderHook(() => useAuth());

    expect(result.current.user).toEqual(mockUser);
    expect(result.current.isAuthenticated).toBe(true);
  });

  it('should log in a user and store the user in localStorage', async () => {
    const { result } = renderHook(() => useAuth());

    await act(async () => {
      await result.current.login('testuser', 'password');
    });

    expect(result.current.user).toEqual({ id: 'clxtest123', username: 'testuser' });
    expect(localStorage.getItem('app-auth-session')).toEqual(JSON.stringify({ id: 'clxtest123', username: 'testuser' }));
  });
```

每个组件生成后都会出现在评审面板中，开发人员可以通过提示或直接编辑来完善逻辑。这使得人工监督处于代码生成过程的中心，确保 AI 生成的代码始终由开发人员的意图指导。

结果是一个模块化、经过测试的组件库，支持实际开发。

### **步骤 3：版本控制、重用和团队协作**

当组件达到稳定状态时，开发人员可以直接从评审面板将其快照为版本化发布。每个快照都捕获组件的精确状态、其代码、依赖项和元数据，在 Bit Cloud 的版本历史中创建了一个不可变记录。这使得重用、回滚或从任何早期版本分支变得简单，而不会引入回归。

一旦版本化，更新将遵循结构化的评审过程。提议的更改作为[更改请求](https://bit.dev/reference/change-requests/submit-change-request)打开，团队成员可以在合并前评审差异、留下反馈并批准修订。这个流程在保持质量的同时，允许团队之间持续迭代。

稳定的组件可以从 Bit Cloud 的注册表或 Git 安装为依赖项。例如，要重用身份验证钩子：

`npm i @<org>/tasks.hooks.use-auth@<version>`

下图显示了重建后的任务管理器，现在围绕独立的、可重用组件进行构建。

[![](https://cdn.thenewstack.io/media/2025/12/21faf24e-image3-1024x554.png)](https://cdn.thenewstack.io/media/2025/12/21faf24e-image3-1024x554.png)

重建后的任务管理器应用程序

通过以架构和可组合性为先导，AI 生成的应用程序演变为模块化系统，这些系统能够随着团队和业务的增长而自然扩展。

## **实用清单**

在部署任何 AI 生成的应用程序之前，请使用此清单评估其生产就绪情况：

| 类别 | 标准 | 描述 | ✓ |
| --- | --- | --- | --- |
| 架构 | 单一职责 | 每个组件处理一个主要关注点 | [ ] |
| | 清晰的边界 | 定义明确的接口和依赖项 | [ ] |
| | 关注点分离 | 业务逻辑与 UI 分离 | [ ] |
| 代码质量 | 无重复 | 共享逻辑提取到可重用服务/钩子中 | [ ] |
| | 类型安全 | 属性验证或 TypeScript 接口 | [ ] |
| | 可访问性 | UI 遵循 WCAG 和语义 HTML 实践 | [ ] |
| 测试 | 单元测试覆盖率 | 核心逻辑经过彻底测试 | [ ] |
| | 组件测试 | 涵盖 UI 行为和边缘情况 | [ ] |
| | 集成测试 | 端到端工作流经过验证 | [ ] |
| 基础设施 | 安全性 | 实施适当的验证以防止安全漏洞，并到位用户身份验证和授权 | [ ] |
| | 监控 | 集成错误跟踪和性能指标 | [ ] |
| | 部署流水线 | 带有测试门禁的自动化 CI/CD | [ ] |
| 可扩展性 | 模块化设计 | 无需重写现有代码即可添加功能 | [ ] |
| | 服务抽象 | 无需重写即可交换外部依赖项 | [ ] |
| | 数据库和缓存 | 模型和策略支持增长 | [ ] |

符合这些标准的应用程序将能够[随着您的团队](https://thenewstack.io/sustainable-scale-how-to-grow-engineering-teams-strategically/)和业务需求实现可持续的扩展。

## **总结**

削弱每个 AI 生成应用程序的错误不是代码本身，而是缺乏结构、模块化和清晰的边界。开发人员经常依赖代码自动完成和代码建议来加速软件开发，但如果没有可组合架构的计划，生成的应用程序就会变得脆弱、难以维护且难以扩展。

为了构建可扩展的 AI 辅助应用程序，团队应该从架构开始，在生成代码之前定义模块化组件、清晰的接口和关注点分离。集成代码审查、测试和版本控制可确保每个模块保持高代码质量，并可在项目之间重用。

通过采用这种方法，AI 从一个简单的代码生成器转变为结构化、[可持续软件开发](https://thenewstack.io/can-open-source-sustain-itself-without-losing-its-soul/)的合作伙伴，使团队能够创建演变为持久、可维护应用程序的原型。您可以注册 [Bit Cloud](https://bit.cloud/signup?c=new) 并探索其慷慨的免费套餐，了解模块化 AI 代码生成如何增强您的代码生成过程。