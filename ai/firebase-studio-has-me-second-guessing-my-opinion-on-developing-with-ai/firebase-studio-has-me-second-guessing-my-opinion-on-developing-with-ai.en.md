AI has its place.

It’s important, however, to keep AI siloed within its place, otherwise it will get out of control and be used as a shortcut for everything (especially in the creative arts).

That being said, why would I want to talk about an agentic AI service that can build apps for those with zero programming experience?

It’s a challenging argument, that’s for sure. Why? Because AI has already begun putting a lot of people out of work. As more and more developers find themselves replaced by a machine, where are businesses going to turn for new applications?

It’s a recursive nightmare.

If you find yourself on the business end of things, where you need to have an app built to help your company thrive, and you’re having trouble locating someone to build it, there’s always [Firebase Studio](https://thenewstack.io/your-ai-coding-buddy-is-always-available-at-2-am/).

## What Is Firebase Studio?

Firebase Studio is a cloud-based, [agentic development environment](https://thenewstack.io/agentic-ides-next-frontier-in-intelligent-coding/) that was created by [Google](https://cloud.google.com/?utm_content=inline+mention) to help streamline building and deploying AI-powered applications. The service offers a one-stop shop for prototyping, building, and publishing apps. This [no-code](https://thenewstack.io/no-code-is-dead/) solution integrates with [Google’s Gemini](https://thenewstack.io/qa-how-google-itself-uses-its-gemini-large-language-model/) to help with code generation, [app prototyping](https://thenewstack.io/microsoft-builds-autogen-studio-for-ai-agent-prototyping/) and more.

Firebase is a full-stack development platform that supports both frontend and backend development and even integrates with services such as Authentication, Firestore and Hosting.

With Firebase, you build apps via an AI prompt. Imagine building a robust application using nothing more than natural language. If that’s not enough, you can also use traditional code-based development with popular frameworks, such as [Next.js](https://thenewstack.io/next-js-deployment-spec-simplifies-frontend-hosting/).

You can either start with the 60 prebuilt templates or use the App Prototyping agent.

I tested the App Prototyping agent and came away *very* impressed. What I did was ask Firebase Studio to build a [Kanban](https://www.atlassian.com/agile/kanban) app that integrates with Google Calendar. After I typed out my prompt, Firebase Studio suggested a more detailed prompt, which was:

> “A collaborative kanban board application for project and task management. Key features include creating and organizing tasks on customizable boards, adding cards with attachments and fully customizable data fields, integrating with Google Calendar for task deadlines, and dragging cards between columns to update status. Use a calm teal and professional gray color scheme.”

Next came the app blueprint (the list of features that would be included), which was:

* **Board creation:** Create and customize multiple Kanban boards to manage different projects or workflows.
* **Card management:** Add cards to boards to represent tasks; customize each card with assignees, descriptions, deadlines, attachments and fully customizable data fields.
* **Google Calendar integration:** Connect Google Calendar to sync task deadlines, providing reminders and a unified schedule view.
* **Drag-and-drop interface:** Drag and drop cards between columns to update their status (e.g., To Do, In Progress, Done).
* **Change notification:** Generate a notification for collaborators when any of the cards is changed, to ensure synchronous collaborative flow.
* **AI resource suggestion:** Based on analyzing card context and content, an AI tool suggests related and relevant resources to facilitate more streamlined card development.

Things are looking pretty good so far. Firebase Studio then suggested the following stack for the application:

* **AI:** Gemini, Genkit
* **UI:** [TypeScript](https://thenewstack.io/what-is-typescript/), NextJS, Tailwind CSS

Time to prototype, which is done with a single click.

After the prototyping, I realized I needed a Gemini API key (Figure 1).

[![](https://cdn.thenewstack.io/media/2025/07/059d9b8e-screenshot-2025-07-29-at-2.13.07%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/07/059d9b8e-screenshot-2025-07-29-at-2.13.07%E2%80%AFpm.png)

Figure 1. Without a Gemini API key, the Kanban board wouldn’t function as needed.

Fortunately, there’s an Auto-generate button for that very purpose. After clicking Auto-generate, Firebase Studio did its thing, and I had my key. With that taken care of, I could test the app to see how well it worked, and, surprisingly, it was seriously impressive.

## What About Tweaking the App?

Anyone who has ever created anything knows the first try is rarely the last. Although my Kanban app worked quite well, there might be changes necessary. After the app is built, you’ll find an Edit the Code button at the bottom right corner of the window. Click that and you’ll be presented with a list of every file created for the app in a sidebar. Expand one of the entries, click on a file, and it’ll open in a code editor (Figure 2).

[![](https://cdn.thenewstack.io/media/2025/07/6ea2dc60-screenshot-2025-07-29-at-2.19.25%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/07/6ea2dc60-screenshot-2025-07-29-at-2.19.25%E2%80%AFpm.png)

Figure 2. The Firebase Studio code editor.

As you can see, the developer skill set is still needed because, as with everything AI, mistakes will be made, and there will *always* be room for improvement.

Edit the code as needed, and then when you’re finished, click the Rebuild Environment button to apply your changes. When the environment is rebuilt, test it again to see if it now meets your needs (or the needs of your client).

## Post-Build Options

Once you’re satisfied with your app, you have a few options.

### Zip and Download

You can create a zip archive and download your project by following these steps:

1. Within your project, navigate to the Code view.
2. Right-click on an empty space in the file explorer pane and select the “Zip & Download” option.
3. When prompted, save the download file to your local machine.

### Git Integration

You can integrate your project with various [Git](https://thenewstack.io/linus-torvalds-reflects-on-20-years-of-git/) providers (such as GitHub and [GitLab](https://about.gitlab.com/?utm_content=inline+mention)), so you can push your code to the repository of your choice. Once you’ve pushed the code, you can then clone it to your local machine, using the standard Git commands and tools.

### Firebase App Distribution (for Test Builds)

Testers can download specific builds of the app via the Firebase App Distribution. Of course, this is for testing purposes and will download the fully compiled app (such as an APK for Android and IPA for iOS). If you click the link icon near the top right, you’ll get a QR code that can be scanned on a phone (Figure 3). Once scanned, it will open your app on the phone, so it can be tested (on either Android or iOS).

[![](https://cdn.thenewstack.io/media/2025/07/e796d2a3-screenshot-2025-07-29-at-2.36.54%E2%80%AFpm.png)](https://cdn.thenewstack.io/media/2025/07/e796d2a3-screenshot-2025-07-29-at-2.36.54%E2%80%AFpm.png)

Figure 3. This is my test Kanban app you can try on your phone.

There is much more to Firebase Studio, but this will give you a good idea of how it works. I would suggest you read [this piece of Google documentation](https://cloud.google.com/blog/products/application-development/firebase-studio-lets-you-build-full-stack-ai-apps-with-gemini) to learn more after you’ve given it a first look.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)