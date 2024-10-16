# Boost Your Shipping Velocity With Argo and Buildpacks
![Featued image for: Boost Your Shipping Velocity With Argo and Buildpacks](https://cdn.thenewstack.io/media/2024/10/99798b46-chuttersnap-at5-ssyp6e4-unsplash-1024x683.jpg)
[CHUTTERSNAP](https://unsplash.com/@chuttersnap?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/assorted-shipping-trailers-in-port-aT5-sSYP6e4?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
[A recent Microsoft](https://queue.acm.org/detail.cfm?id=3595878) study looked into what drives developers’ productivity and found that the feedback loop had a strong impact. The findings recommend that feedback loops — the speed and quality of responses to actions performed — should be shortened to the maximum possible extent. One example they mention in their finding is the time it takes to push code to production.
CNCF graduated project Argo is one of the leading choices for [continuous integration and delivery](https://thenewstack.io/how-continuous-integration-and-continuous-delivery-ci-cd-enhances-devops/) tools and generally makes developers’ lives easier. But before code can be pushed into Argo, [developers typically need](https://thenewstack.io/5-things-developers-need-to-know-about-kubernetes-management/) to write a Dockerfile to containerize it.

In this article, I will explore how to use CNCF incubating project [Buildpacks](https://buildpacks.io/), an application definition, and image build to skip the Dockerfile step and increase developer productivity.

## How can Buidlpacks increase feedback loop speed?
Let’s first set the context for Buildpacks. Cloud native buildpacks transform your application source code into images running on any cloud. By looking at your code, Buildpacks auto-detect what is needed to build an OCI image with the best performance and security practices.

When using Buildpacks, writing a Dockerfile before pushing code so it can be pulled into Argo is no longer necessary. Developers can go from writing code to pushing it into the company CI/CD pipeline.

## Integrates Buildpacks within Argo
Buildpacks are specifications that define how source code is transformed into containerized applications. But to create an OCI image based on these specifications, you will use the [pack command](https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/) and specify a Buildpack (more on that later).

This step is used as part of an Argo workflow:

123456789 |
- name: build-image inputs: parameters: - name: passed-tag container: image: buildpacksio/pack command: ["pack", "build"] args: - "172.31.17.128:5000/my-python-app:{{inputs.parameters.passed-tag}} --path /mnt/vol/app --builder paketobuildpacks/builder-jammy-base --publish" |
Let’s go over each argument
`name: build-image`
is the name of the Argo workflow step. My workflow has multiple steps (clone and build). For more info, refer to the[entire configuration file](https://github.com/sylvainkalache/deploy-buildpack-containerized-python-app-to-argo/blob/main/pack-build-argo-workflow.yaml)on my Github repository.`inputs: parameters: - name: passed-tag`
this specifies which version of the code to use to build my image. This is optional, and I will explain it further in the next paragraph.`image: buildpacksio/pack`
we are using the buildpacks/pack image to run this Argo step.`command: ["pack", "build"]`
we tell the workflow to run the pack build command.
Now let’s look at the `pack build`
command arguments:

`172.31.17.128:5000/my-python-app:{{inputs.parameters.passed-tag}}`
the IP is where my container registry is hosted. Here, I am using a self-hosted registry, but you can use anything from ECR to Dockerhub. The second part,`my-python-app,`
, is the name of my container image. In the next paragraph, I cover`{{inputs.parameters.passed-tag}}`
.`--path /mnt/vol/app`
is where my application code is.`--builder paketobuildpacks/builder-jammy-base`
a builder is an image containing an ordered combination of buildpacks and a build-time base image, a lifecycle binary, and a reference to a runtime base image. I am using one from[Paketo Buildpacks](https://paketo.io/), but here are other providers, such as[Google](https://cloud.google.com/docs/buildpacks/builders)and[Heroku](https://devcenter.heroku.com/articles/buildpacks).`--publish`
publishes the application image directly to the container registry specified in image name (see first argument), instead of the daemon.
That’s all you need to get Argo to containerize any application written in pretty much any language. There is no need for developers to write a Dockerfile, meaning that as soon as their application is written, they can push it to Argo and see it being deployed.

## Image immutability and release strategy
One important thing to know is that Buildpacks marks images with a fixed date (January 1, 1980) for immutability and reproducibility. The reason for using a fixed timestamp is to ensure consistent image creation, which helps eliminate the differences caused by build times. This is a great security feature but can cause challenges for CI/CD deployment workflows. If your workflow is based on the latest tag, you will encounter issues because all images will have the same timestamp.

That’s why I am using a semver versioning strategy. In my Argo workflow, I leverage Argo parameter inputs to get the tag with which I want to build my image. I receive the tag with `inputs: parameters: - name: passed-tag`
and pass it to my pack command with `{{inputs.parameters.passed-tag}}`
.

## Conclusion
Using Buildpacks as part of your Argo workflow will improve the developer experience and shipping velocity and ensure your container images are secure and optimized. Indeed, the open-source implementation of the Buildpacks spec Paketo Buildpacks [ensures](https://paketo.io/docs/concepts/stacks/) that their images are always up-to-date with the latest CVE patches and tuned for every stack. Last but not least, if you want to dig deeper, I recorded [a video](https://youtu.be/TojM-kmYeXA) showcasing this entire tutorial and going more in-depth on some of the concepts.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)