If you’ve ever built more than a quick prototype with AI tools like Lovable or Replit, you’ve likely felt the friction that comes with extending the first version. A small code refactoring can trigger new bugs, a new feature can break old logic and progress starts to feel like rework instead of iteration.

This pattern isn’t random. Most AI coding tools are designed to generate code quickly, rather than preserving structure over time. While they can create working APIs and functions, they don’t establish an overarching architecture to connect and organize them. The result is a single, functional codebase with limited isolation, unclear ownership and no reliable path for reuse. What begins as rapid development soon becomes rework.

The evolution from AI code generation to composable architecture changes how AI fits into real-world software development. Instead of producing entire files in one shot, developers can use AI to create independent modules that plug into a broader architecture. This approach aligns better with how teams maintain, test and ship production code.

In this article, I’ll walk through what that looks like.

I’ll start by asking an AI [assistant to generate code](https://thenewstack.io/how-generative-ai-coding-assistants-increase-developer-velocity/) for a small working React app and inspect its structure. Next, I’ll identify where the architecture creates friction when making changes or adding new features. Finally, I’ll rebuild the same app using a composable workflow that enforces boundaries, version tracking and modular reuse, turning the same generated code into software that can grow sustainably.

## **Let’s Generate the App**

To put composability to the test, I asked Cursor to generate a complete React task manager application using a single prompt.

The request mirrors how most developers interact with AI tools: describe the requirements once and let the model provide relevant suggestions for a full implementation.

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

Below is the generated task manager and its file structure. The full code is also available in [this GitHub Repository](https://github.com/ThatCoolGuyyy/ai-generated-task-manager).

[![](https://cdn.thenewstack.io/media/2025/12/32026aa7-image2-1024x554.png)](https://cdn.thenewstack.io/media/2025/12/32026aa7-image2-1024x554.png)

AI-generated task manager

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

At first glance, the project structure looks familiar and usable. The app compiles and runs successfully, providing authentication, a dashboard, and persistent task management through local storage, exactly as requested in the prompt.

However, the real question isn’t whether the application runs, but how the files are structured. The present architecture lacks clear boundaries. Logic, state, and presentation are intertwined. Nothing in this structure enforces modularity, reuse or version control.

This is where the absence of composable architecture becomes visible.

The best AI code generators can produce working applications, but they rarely define systems. Without isolation between state and UI, clear ownership of logic or explicit contracts between components, each feature becomes interdependent.

In the next section, I’ll examine the structure of this application more closely, highlighting where architectural shortcuts create friction.

## **Issues With the Cursor-Generated App**

The generated task manager’s structure shows clear limitations when evaluated for long-term maintainability. The weaknesses are not in the syntax or React patterns, but in the system’s composition.

The following examples illustrate how these structural gaps appear in the code.

1. **No prop boundaries between components**

**Where it happens:** *App.js* (lines 9–22)

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

`ProtectedRoute` accepts any `children` element without constraints. No defined interface explains what kind of component can be passed, what props it should receive or what data context it depends on.

In a larger application, this leads to fragile integration points. Without explicit boundaries, a small change in the route logic can silently affect every component nested inside it.

Every component should define its interface and dependencies. In a composable system, this is achieved through typed props, contracts or schema definitions that describe what each unit consumes and exposes.

2. **Zero test coverage**

**Where it happens:** *App.test.js* (lines 4–8)

```
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
```

The only test checks that the React starter template renders, leaving all actual application logic unverified. Authentication, state persistence and task updates operate without any automated guardrails.

Without unit or integration tests, the system has no measurable feedback loop. Each change risks introducing regressions that remain invisible until runtime.

Each module should have defined and testable behavior. Isolated tests serve as the compositional boundaries of a system, ensuring that changes in one area do not silently alter another.

3. **Broken separation of concerns**

**Where it happens:** *Dashboard.js* (lines 32–52)

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

The `handleAddTask` function combines event handling, validation, API simulation and state updates in one place, making it difficult to test or replace any single part.

As the app grows, adding new features would require rewriting this logic rather than extending it through isolated modules.

Logic, state and presentation should evolve independently of each other, enabling systems to adapt without requiring the rewriting of entire components.

4. **Tightly coupled state**

**Where it happens:** *AuthContext.js* (lines 19–21)

```
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
```

The authentication state lives directly inside the provider component. All updates, persistence logic and API handling are bound to a single context.

This coupling prevents reusability. The authentication logic cannot be shared across projects or replaced with a different implementation because the state is not portable or parameterized.

Application state should have clear ownership and live outside the components that consume it. This separation keeps the state reusable and portable across contexts.

5. **No path for reusability**

**Where it happens:** *AuthContext.js* (lines 6–9, 32–52)

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

Mock users are hardcoded directly into the authentication context, with no abstraction or configuration layer. This tightly couples authentication logic to the app, making it impossible to integrate a new provider without rewriting the entire context.

Authentication should instead be defined through an interface, allowing providers to be swapped seamlessly without requiring modifications to internal logic.

## **Rebuilding With a Composable Architecture**

The issues in the code generated by AI tools are not unique to Cursor. They appear in almost every AI-generated project that prioritizes code completion over architectural intent. To correct them, [developers need to change their practices to generate code](https://thenewstack.io/ai-generated-code-needs-refactoring-say-76-of-developers/) based on modular composition.

Composable architecture starts with an architectural plan that guides the code generation process. Before writing any logic, the system defines its structure, including what units exist, how they communicate and where state and behavior reside. Once these boundaries are set, AI can safely generate code for each component within that structure. The output becomes a network of versioned modules, rather than a single, untracked codebase.

This approach is what [Hope AI](https://bit.cloud/products/hope-ai?c=new) and [Bit Cloud](https://bit.cloud/?c=new) implement together. Hope AI generates code through an architecture-first workflow, and Bit Cloud provides the system that stores, versions and reuses every generated component. Together, they show how AI-assisted code generation can evolve into a repeatable software development process.

The rebuild follows three structured steps:

### **Step 1: Defining Architecture Before Code**

The development process begins with an architectural proposal. The developer describes the high-level design, for instance, separating logic into services, hooks and UI layers, and the AI returns a diagram of that structure before writing a single line of code.

For our task manager, Hope AI proposed the following layout:

[![](https://cdn.thenewstack.io/media/2025/12/2fe61ec2-image1.png)](https://cdn.thenewstack.io/media/2025/12/2fe61ec2-image1.png)

Hope AI Architecture

This architectural layout already resolves several earlier issues:

* **Pages** handle navigation-level logic (login, dashboard).
* **UI components** focus on rendering and interaction (task-item, add-task).
* **Hooks** encapsulate state and data (use-tasks, use-auth).
* The **root app** connects these pieces without embedding logic directly.

By reviewing this structure before generation, developers can adjust boundaries, for example, requesting a `services/TaskService` to isolate async logic.

This architectural checkpoint converts AI from a code producer into a design collaborator.

**Step 2: Component Generation**

After the architecture is approved, Hope AI generates each component as a standalone, testable unit. Instead of assembling a large bundle of files, it produces small, modular components with clear responsibilities, each packaged with local tests, documentation and usage previews.

For example, the `useAuth` hook is generated as a reusable function rather than a block of inline logic:

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

A matching test file `use-tasks.spec.tsx` is also created to validate the hook’s behavior:

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

Each component appears in the review panel once generated, where developers can refine logic through prompts or direct edits. This keeps human oversight at the center of the code generation process, ensuring that AI-generated code remains guided by developer intent.

The result is a library of modular, tested components that support real-world development.

### **Step 3: Versioning, Reuse and Team Collaboration**

When a component reaches stability, developers can snap it into a versioned release directly from the review panel. Each snap captures the exact state of the component, its code, dependencies and metadata, creating an immutable record in Bit Cloud’s version history. This makes it simple to reuse, roll back or branch from any earlier version without introducing regressions.

Once versioned, updates follow a structured review process. Proposed changes open as [Change Requests](https://bit.dev/reference/change-requests/submit-change-request), where teammates can review diffs, leave feedback and approve revisions before they merge. This flow preserves quality while allowing continuous iteration across teams.

Stable components can then be installed as dependencies from Bit Cloud’s registry or Git. For example, to reuse the authentication hook:

`npm i @<org>/tasks.hooks.use-auth@<version>`

The image below shows the rebuilt task manager, now structured around independent, reusable components.

[![](https://cdn.thenewstack.io/media/2025/12/21faf24e-image3-1024x554.png)](https://cdn.thenewstack.io/media/2025/12/21faf24e-image3-1024x554.png)

Rebuilt Task Manager Application

By leading with architecture and composability, AI-generated applications evolve into modular systems that scale naturally with team and business growth.

## **Practical Checklist**

Before deploying any AI-generated application, use this checklist to evaluate its production readiness:

|  |  |  |  |
| --- | --- | --- | --- |
| Category | Criterion | Description | ✓ |
| Architecture | Single responsibility | Each component handles one primary concern | [  ] |
|  | Clear boundaries | Well-defined interfaces and dependencies | [  ] |
|  | Separation of concerns | Business logic separated from UI | [  ] |
| Code quality | No duplication | Shared logic extracted into reusable services/hooks | [  ] |
|  | Type safety | Prop validation or TypeScript interfaces | [  ] |
|  | Accessibility | UI follows WCAG and semantic HTML practices | [  ] |
| Testing | Unit test coverage | Core logic thoroughly tested | [  ] |
|  | Component testing | UI behavior and edge cases covered | [  ] |
|  | Integration testing | End-to-end workflows verified | [  ] |
| Infrastructure | Security | Proper validation implemented to prevent security vulnerabilities, with user authentication and authorization in place | [  ] |
|  | Monitoring | Error tracking and performance metrics integrated | [  ] |
|  | Deployment pipeline | Automated CI/CD with test gates | [  ] |
| Scalability | Modular design | Features can be added without rewriting existing code | [  ] |
|  | Service abstractions | External dependencies can be swapped without rewrites | [  ] |
|  | Database and caching | Models and strategies support growth | [  ] |

Applications that pass these criteria will [scale sustainably with your team](https://thenewstack.io/sustainable-scale-how-to-grow-engineering-teams-strategically/) and business requirements.

## **Wrapping Up**

The mistake that weakens every AI-generated app isn’t the code itself but the lack of structure, modularity and clear boundaries. Developers often rely on code completion and code suggestions to speed up software development, but without a plan for composable architecture, the resulting applications become fragile, hard to maintain and difficult to extend.

To build AI-assisted applications that scale, teams should start with architecture, defining modular components, clear interfaces and separation of concerns before generating code. Integrating code review, testing and version control ensures that each module maintains high code quality and can be reused across projects.

By adopting this approach, AI transitions from a simple code generator to a partner in structured, [sustainable software development](https://thenewstack.io/can-open-source-sustain-itself-without-losing-its-soul/), enabling teams to create prototypes that evolve into lasting, maintainable applications. You can sign up for [Bit Cloud](https://bit.cloud/signup?c=new) and explore their generous free tier to see how modular AI code generation can enhance your code generation process.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/12/fd90908c-1739284331173-600x600.jpeg)

Oluwadamilola is a software engineer and technical passionate about sharing knowledge his with the community

Read more from Oluwadamilola Oshungboye](https://thenewstack.io/author/oluwadamilola-oshungboye/)