# UI Libraries Are Dying: What’s Next?
![Featued image for: UI Libraries Are Dying: What’s Next?](https://cdn.thenewstack.io/media/2024/03/83c1de4e-image1a-1024x663.png)
UI libraries are a collection of UI components, styles, and utilities packaged and published to be reused in applications. They help maintain consistency in and across apps, speed up development and make code more maintainable.
UI libraries come with their own set of challenges, which greatly limit their effectiveness. These challenges stem from more fundamental problems related to code sharing and reuse. Let’s explore some of these challenges and examine how a new entity, the
[Bit](https://bit.dev/?utm_content=inline+mention) component, addresses them.
**What Is a Bit Component?**
A
[Bit component](https://bit.dev/reference/components/the-bit-component) can be thought of as a next-generation package. Its build setup, [tooling](https://bit.dev/docs/getting-started/composing/dev-environments) and even [version control](https://bit.dev/reference/components/version-changes) are all encapsulated within the component itself. Bit components are hosted on [bit.cloud](https://bit.cloud), grouped by scopes with different access controls. That means a Bit component is not tied to any git repository. You can [import](https://bit.dev/reference/workspace/importing-components) (clone) it into your [development environment](https://thenewstack.io/how-to-choose-a-cloud-development-environment/), modify it and push it back to bit.cloud.
When components are released they go through a
[build process](https://bit.dev/reference/ci/ripple-ci) that generates artifacts. One important artifact is the component’s package. A component can be installed as a regular Node package or, as mentioned earlier, imported (cloned) into your project where it can be updated.
For example, to modify a component, we’ll first search for it on bit.cloud:
We’ll run the following to import it into our project:
bit import bitdesign.sparks/actions/button
The imported component is now available as source files to modify and a package to consume. Bit automatically updates the package on every change.
Once our changes are made, we can create a new version of the component and push it back to bit.cloud:
|
1
2
|
bit tag --message "use lighter color tokens"
bit export
Our button component is now available with a new version on bit.cloud. We can keep maintaining it, or we can remove it from our project while keeping only the package for consumption.
**Making Your UI Components Reusable and Portable Is Hard** **Making Your UI Components Reusable and Portable Is Hard**
Sharing individual UI components as packages takes too much effort. Decoupling the component from the project, making sure it is generic or “reusable enough,” configuring its package.json, documenting, versioning and publishing can be a hassle.
This is more evident when it comes to complex components like forms and full-page layouts. These components often remain “hidden” in repositories and unshared, forcing others to build them from scratch, which is time-consuming, leaves room for errors and makes the code base more difficult to maintain.
As you’ll see in the next section, limited collaboration is also a factor in this problem. Package consumers are not able to modify and extend components to address new needs as they arise, and by following this iterative process, you can make concrete components more generic and reusable.
Closely related to this issue is the common practice of creating “mega-libraries” that contain a large number of components. This is another symptom of the same problem: Sharing individual components as packages is not easy.
![The traditional workflow for library publishing](https://cdn.thenewstack.io/media/2024/03/674bee5c-image4a.png)
The traditional workflow for library publishing
**Bit Makes Sharing Individual Components Simple and Easy**
Teams are more inclined to
[share components](https://thenewstack.io/how-to-bridge-the-developer-designer-gap/) when the process is easy, and equally, they are more prone to reuse components when they are easy to find. Bit makes sharing components easy. Bit components require no configuration. Their dependencies are automatically detected and intelligently resolved to the proper versions and types.
Bit also auto-generates the component documentation and makes it simple to render component previews.
As mentioned earlier, package publishing is an integral part of a component’s build pipeline. When a component is versioned and released, its package gets automatically published to bit.cloud’s registry (and possibly to
[a registry of your choice](https://bit.dev/reference/packages/publishing-components-to-commonjs-registries)), where it can be discovered and installed by others.
Individually packaged components allow the consumers to pick and choose the components they need and avoid meaningless
[updates to their project’s dependencies](https://thenewstack.io/ai-assisted-dependency-updates-without-breaking-things/).
**UI Libraries Limit Collaboration **
Component libraries are built to enforce consistency in UI/UX and development standards. This is a good thing; however, it can also become a challenge if the library is not flexible enough to address the project’s needs. When that happens, the team is forced to work around the library, fork it and maintain their own version, or suggest a pull request (PR) to the library maintainers and wait for it to be merged and released.
This can often lead to poor library adoption, which beats the purpose of having a library in the first place.
**Bit Components Promote Cross-Team Collaboration**
Since Bit components are autonomous, they canbe developed and maintained anywhere. That means that teams consuming a component can also contribute to it without having to come up with various workarounds or switching from one repository to another.
Components can be modified and improved instantly from any consuming project, while the maintainers can review and merge the changes at their own pace.
Changes are immediately available in that project, and they can be reviewed, tested and merged at the maintainers’ own pace.
**A Future Beyond Libraries: Fully Component-Based Projects**
With
[Bit](https://bit.dev), the traditional concept of separate UI libraries, or libraries in general, may soon become obsolete. The natural composition from “library” to more complex components can be achieved using the same structure and tooling without the need to distinguish between “library code” and “application code.”
This shift toward a more integrated and flexible approach to code reuse and package management heralds a new era in software development. The boundaries between libraries and applications blur, leading to more efficient, maintainable and collaborative development practices.
As we move forward, the focus will likely shift from using and contributing to standalone UI libraries to creating and sharing Bit components in a more dynamic, interconnected ecosystem.
This evolution promises to make software development more modular, scalable and inclusive, paving the way for a future where developers can easily build upon each other’s work, leading to faster innovation and more robust applications.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)