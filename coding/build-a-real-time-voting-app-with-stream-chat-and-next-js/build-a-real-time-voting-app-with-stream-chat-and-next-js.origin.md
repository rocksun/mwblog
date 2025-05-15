# Build a Real-Time Voting App With Stream Chat and Next.js
![Featued image for: Build a Real-Time Voting App With Stream Chat and Next.js](https://cdn.thenewstack.io/media/2025/05/f9283f84-voting12-1024x534.png)
For situations where you’d like to gather opinions from a variety of sources, you can set up a real-time voting system that will allow users to vote on different options in real time, updating the results instantly. Here’s a tutorial on how to build that using the [Stream Chat API](https://getstream.io/chat/) and [Next.js](https://nextjs.org/).

Stream is a powerful tool for adding real-time chat functionality to applications. It provides features like channels, messages and users, making it easy to build interactive chat applications.

Next.js is a popular [React framework](https://getstream.io/chat/sdk/react/) that simplifies building [server-rendered applications](https://thenewstack.io/the-pros-and-cons-of-using-react-today/). It provides features like automatic code splitting, server-side rendering and hot module replacement, making it an excellent choice for building modern web applications.

**Set Up Chat Messaging**
Before you can [create a new project on Stream](https://getstream.io/blog/stream-getting-started-guide/), you need a Stream account, and you’ll need to generate an API key to use the Stream Chat API. You can [create a new Stream account](https://getstream.io/try-for-free/) for free.

Once you’re signed up, create a new project and generate an auth token to authenticate your application with the Stream Chat API. Follow the steps in [this tutorial](https://getstream.io/blog/livestream-chat-nextjs/#setting-up-a-new-stream-application) to generate the auth token and set up the Stream Chat API. This will:

- Create a new organization on the Stream dashboard.
- Create a new app inside the organization by clicking the “Create App” button.
- Configure the app by setting roles and permissions, and get the “key” and (optionally) the “secret” from the “App Access Keys” section.
In a production application, you should generate the auth token using the “key” and the “secret.” However, in this tutorial, you’ll use the “key” alone for simplicity.

To disable authentication, enable the setting “Disable Auth Checks” in the Stream Chat dashboard.

**Application Overview**
Before building the application, review the key components and features you’ll implement.

The application will have the following screens:

**Login**: Users must provide a username to join the voting.**Voting system**: This is the part of the application where voting happens.
Functionally, the application has the following features:

- When a user logs in, they can see and vote on all existing questions.
- Users can add new questions with multiple options.
- The results are updated in real time as users vote.
Please note that we will not implement authentication, nor focus on the user interface (UI) design in this tutorial. However, the final code is available for reference. Instead, we’ll focus on the core functionality of the voting system and its integration with Stream Chat.

**Set Up Your Project**
Create a new Next.js project with the necessary configurations using the `create-next-app`
command:

12 |
npx create-next-app my-voting-appcd my-voting-app |
**Install Dependencies**
Next, install the necessary dependencies to work with Stream Chat API:

1 |
npm install stream-chat-react |
In addition to the [Stream Chat SDK](https://github.com/GetStream/stream-chat-js/), you must install other dependencies, including `zustand`
, a lightweight state management library that’s used to manage the application state:
1 |
npm install zustand |
**Initialize the Stream Client**
Create a Stream client instance to interact with the Stream Chat API. For this, create a new file named `src/lib/stream.ts`
and add the following code:

123 |
import { StreamChat } from 'stream-chat';const chatClient = StreamChat.getInstance('your_api_key'); |
You’ll use this client instance to create channels, send messages and handle real-time updates in your application.
**Manage Users**
When users log in, they’ll connect to Stream Chat and be added to the voting session channel. This will allow the user to send and receive real-time voting session messages.

The steps are:

- Connect the user to Stream Chat.
- Add the user to the voting session channel.
- Load existing questions and votes from the channel.
- Return the session channel object to interact with the voting session on the frontend.
**1. Connect the User to Stream Chat**
To add a user to the voting session channel, you need to connect them to Stream Chat. Use the `connectUser`
method provided by the Stream Chat SDK:

1234567891011121314 |
export const initializeStream = async (username: string) => { try { // Connect user to Stream await chatClient.connectUser( { id: username, name: username, }, chatClient.devToken(username) ); } catch (error) { console.error('Error connecting to Stream Chat:', error); }}; |
Pass the user ID and name as parameters to identify the user in the chat. Then generate a development token using the `devToken`
method to [authenticate the user](https://thenewstack.io/master-difficult-user-authentication-requirements-with-oauth/).
**2. Add the User to the Voting Session**
Once the user is connected to Stream Chat, add them to the voting session channel. This allows the user to send and receive messages in the voting session:

12345678 |
// Create or connect to the session channel if not already connectedif (!sessionChannel) { sessionChannel = chatClient.channel('messaging', 'voting-session', { name: 'Voting Session', members: [username], });}This |
This code first checks if the session channel exists. If not, it creates a new channel using the `chatClient.channel`
method with the type `messaging`
and the ID `voting-session`
. it specifies the channel name as `Voting Session`
and adds the user to the channel as a member. Stream Chat then connects the user to the existing channel and returns the channel object if the channel already exists.
**3. Load Existing Questions and Votes**
After connecting the user to Stream Chat and adding them to the voting session channel, load the existing questions and votes from the channel:

1234567891011121314151617181920212223242526272829303132 |
// Get all messages from the channel const response = await sessionChannel.query({ messages: { limit: 100 }, // limit is not required but added for demonstration state: true});const messages = response.messages || [];// Process messages to get questions and votesconst questions: VotingQuestion[] = [];const seenQuestions = new Set();// Process from oldest to newest to maintain order and get latest statemessages.reverse().forEach((msg: MessageResponse) => { if (msg.type === 'regular') { const customData = msg.data as any; if (customData?.type === 'new_question' && !seenQuestions.has(customData.id)) { questions.push({ id: customData.id, question: customData.question, options: customData.options, votes: customData.votes || {} }); seenQuestions.add(customData.id); } }});// Update store with existing questionsif (questions.length > 0) { useVoteStore.setState({ questions });} |
This queries the channel for the latest messages and state. It then processes the messages to extract the questions and votes from the channel data. It stores the questions in an array and the votes in a map for easy access.
Add the above functions to your `initializeStream`
function to handle user management in the voting system. This function should return the session channel object that the application uses to send and receive messages in the voting session.

The application’s state is updated for every message received to reflect the new questions and votes. This ensures that the UI is always current with the latest data from the voting session.

Here’s the updated `initializeStream`
function with user management logic:

1234567891011121314151617181920 |
// Create a singleton instance for the session channellet sessionChannel: any = null;const initializeStream = async (username: string) => { try { // Connect user to Stream ... (as shown above) // Create or connect to the session channel if not already connected // Get all messages from the channel // Process messages to get questions and votes // Update store with existing questions return sessionChannel; } catch (error) { console.error('Error initializing Stream:', error); return null; }}; |
This setup connects users to Stream Chat, adds them to the voting session channel and loads existing questions and votes from the channel.
In the next section, you’ll implement the logic to allow users to vote on questions and add new questions to the voting session.

**Voting System**
Next, let’s focus on implementing the core functionality of the voting system. Users should be able to vote on existing questions and add new questions with multiple options. For this, you’ll define the following features:

- Add users to the session when they log in. Listen for new questions and votes from the session.
- Allow users to vote on questions and add new questions. This should propagate to the session in real time.
**Vote Store**
Before implementing the voting system, set up a store using Zustand to [manage the application state](https://thenewstack.io/how-to-better-manage-stateful-applications-in-kubernetes/). Configure Zustand to create a store for [managing the users](https://thenewstack.io/managing-user-access-in-multiregion-deployments/), questions and votes in the voting system:

123456789101112131415161718192021 |
// Define our store typesinterface User { username: string;}export interface VotingQuestion { id: string; question: string; options: string[]; votes: Record<string, string>; // userId -> optionId}interface VoteStore { user: User | null; questions: VotingQuestion[]; setUser: (user: User | null) => void; addQuestion: (question: Omit<VotingQuestion, "id" | "votes">) => void; vote: (questionId: string, option: string) => void; addQuestionFromStream: (question: VotingQuestion) => void; addVoteFromStream: (questionId: string, userId: string, option: string) => void;} |
This defines the store types for the user, voting questions and the store itself. The store contains the user object, an array of voting questions and methods to update the store state. I won’t go into the details of each method here, but you’ll implement them as you build the voting system.
Create the store using Zustand and export it for use in our application:

1234 |
// Create the storeexport const useVoteStore = create<VoteStore>((set) => ({ // contains implementation of the store methods})); |
**Listen for Messages in a Session**
You’ll use the session channel object returned by the `initializeStream`
function to display existing questions and options.

When users log in, they’ll be connected to Stream Chat and the existing questions and votes from the channel will load. Then the application will display the questions and options on the frontend:

1234567891011121314151617181920212223242526272829 |
// Handle form submission const handleSubmit = async (e: React.FormEvent) => { e.preventDefault(); if (username.trim()) { try { const channel = await initializeStream(username.trim()); // Listen for new messages channel.on('message.new', (event: any) => { if (event.user?.id !== username.trim()) { const customData = event.message.data; if (customData?.type === 'new_question') { useVoteStore.getState().addQuestionFromStream(customData); } if (customData?.type === 'new_vote') { const { questionId, userId, option } = customData; useVoteStore.getState().addVoteFromStream(questionId, userId, option); } } }); setUser({ username: username.trim() }); router.replace("/vote"); } catch (error) { console.error('Failed to initialize Stream:', error); // Handle error appropriately } } }; |
This gets the username from the form input and calls the `initializeStream`
function to connect the user to Stream Chat. It then listens for new messages in the voting session channel and updates the application state based on the received messages. Finally, it sets the user state and navigates to the voting page.
New data received is either a new question or a vote. They are displayed on the UI by updating the local state objects accordingly.

**Add New Questions and Votes**
Next, you’ll implement the logic to handle user interactions in the voting system. Whether users are voting on existing questions or adding new questions with multiple options, the voting and question creation must be propagated to the voting session in real time.

I’ll model both interactions as messages sent to the session channel. I’ll start by adding a new question:

1234567891011121314151617181920212223 |
addQuestion: (questionData) => { const newQuestion = { ...questionData, id: generateId(), votes: {} }; // Update local state first set((state) => ({ questions: [...state.questions, newQuestion] })); // Then broadcast to other users if (sessionChannel) { void sessionChannel.sendMessage({ text: JSON.stringify(newQuestion), data: { type: 'new_question', ...newQuestion } }); }} |
When the user adds a question, the app generates a unique ID and updates the local state with the new question. It then sends a message with the new question data to the session channel. Note that the message type is set to `new_question`
to differentiate it from voting messages.
You can implement the logic to handle user votes similarly:

123456789101112131415161718192021222324252627282930 |
vote: (questionId, option) => { const username = useVoteStore.getState().user?.username; if (!username) return; // Send vote to stream sessionChannel?.sendMessage({ text: 'New vote cast', type: 'regular', data: { type: 'new_vote', questionId, userId: username, option } }); set((state) => ({ questions: state.questions.map(q => q.id === questionId ? { ...q, votes: { ...q.votes, [username]: option } } : q ) }));} |
Vote are sent to the session channel, then the local state is updated with the new vote. The message type is set to `new_vote`
and includes the question ID, user ID and the selected option.
The [final code for this project](https://github.com/tyaga001/voting-system) is available on GitHub for reference.

If you enjoyed this, you might also like my [detailed guide on building a custom video conferencing app with Stream](https://www.freecodecamp.org/news/how-i-built-a-custom-video-conferencing-app-with-stream-and-nextjs/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)