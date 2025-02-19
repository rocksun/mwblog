Featured

# Can Configuration Languages (config DSLs) solve configuration complexity?
A proliferation of domain-specific languages (DSLs) designed to generate configuration, or *configuration languages*, has emerged over the past several years: [HCL](https://github.com/hashicorp/hcl), [Dhall](https://dhall-lang.org/), [Jsonnet](https://jsonnet.org/), [Starlark](https://github.com/bazelbuild/starlark), [CUE](https://cuelang.org/), [Nickel](https://nickel-lang.org/), [KCL](https://www.kcl-lang.io/), [Pkl](https://pkl-lang.org/), and [others](https://github.com/rix0rrr/gcl). I’m sure there are at least [15](https://xkcd.com/927/). I differentiate these from data serialization languages like JSON, XML, TOML, INI, etc. by the inclusion of expressions, conditionals, variables, and other syntactic constructs that facilitate generating multiple concrete configurations as outputs based on inputs. I’m going to count YAML as being in the data serialization category. [YAMLScript](https://yamlscript.org/) is new enough that I haven’t seen any uses of it yet, and won’t cover it. For a more detailed breakdown of different kinds of languages, see [this article by the KCL project](https://blog.stackademic.com/10-ways-for-kubernetes-declarative-configuration-management-3538673fd0b5), which also [compares KCL with many of these languages](https://www.kcl-lang.io/docs/user_docs/getting-started/intro).

Why would someone choose to use a configuration language to write configuration generators / templates rather than a general-purpose language or template language (e.g., Go templates, Jinja, Mustache)?

For a tool builder, one benefit compared to a general-purpose language is that these languages are (mostly) interpreted and embeddable in the tool, though that’s also true of template languages. Configuration languages can also be more amenable to static analysis than either general-purpose languages or template languages, and it is straightforward to [ensure that they don’t produce side effects](https://sre.google/workbook/configuration-specifics/).

In addition to [just shaping the language to your liking](https://ruudvanasseldonk.com/2024/a-reasonable-configuration-language), a benefit of creating a new configuration language is that it provides more control over the package and registry systems, and over the standard libraries. Indeed, some of these languages were originally [created for specific tools](https://www.reddit.com/r/ProgrammingLanguages/comments/gzqsxj/the_future_of_general_purpose_configuration/), such as HCL for Terraform, Starlark for [Bazel](https://bazel.build/extending/config), Nickel for the [Nix package manager](https://www.tweag.io/blog/2023-01-24-nix-with-with-nickel/), and KCL for [KusionStack](https://www.kusionstack.io/docs/).

For a user, the syntax may be a little more concise than with general-purpose languages. Additionally, I have read that some non-programmers found HCL similar enough to scripting languages (like shell, awk, and/or perl?) to be approachable compared to general-purpose languages like Python and Typescript. For programmers, [using a familiar general-purpose language](/generating-configuration-using-general-purpose-programming-languages-19230a2c2573) is a marketable aspect of tools like Pulumi, but perhaps a configuration language provides a neutral middle ground in environments where multiple general-purpose languages are in use for applications. Compared with template languages, configuration languages have more expressive power and frequently more type safety and schema validation.

Each language designer of course has some specific goals when designing a language. For example, [CUE](https://cuelang.org/docs/introduction/) was based on lessons learned from Google’s internal configuration languages (as was [Jsonnet](https://jsonnet.org/)), and one goal of CUE was to [make it easier to determine where final values were set by disallowing overrides](https://cuelang.org/docs/concept/the-logic-of-cue/#relation-to-inheritance). One goal of [Dhall was to make imports safe](https://dhall-lang.org/). Starlark is an [embeddable Python dialect](https://github.com/bazelbuild/starlark/?tab=readme-ov-file#design-principles) that is familiar to people familiar with Python. Jsonnet is a [superset of JSON](https://jsonnet.org/articles/design.html). [Types are optional in Nickel](https://nickel-lang.org/user-manual/introduction). [Pkl](https://www.youtube.com/watch?v=N7zmsHUiTkM)… And so on. They are interesting from a programming language design point of view, if nothing else.

Ok, what do these languages look like? Since I’m not proficient with most of these languages, I used Claude to generate an example of a Kubernetes Deployment in each language with the resource name, label values, and container image parameterized. Which I have to say I was pretty impressed by. Claude included instructions for how to run each tool, mentioned some benefits of each language, and offered suggestions for further improvements using specific language capabilities. I compared the results with other examples I could find, but didn’t run them through the tools. This is just meant to illustrate the flavor of the languages.

Here’s the YAML for the Deployment, including some properties values that are strings, integers, and booleans, and both maps and arrays/lists:

`apiVersion: apps/v1`
kind: Deployment
metadata:
labels:
app: mydep
name: mydep
namespace: example
spec:
replicas: 3
selector:
matchLabels:
app: mydep
template:
metadata:
labels:
app: mydep
spec:
dnsPolicy: ClusterFirst
containers:
- image: nginx:latest
name: nginx
ports:
- containerPort: 8080
HCL using the [Kubernetes provider](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/deployment#example-usage):

`# Variables`
variable "deployment_name" {
description = "Name of the Kubernetes deployment"
type = string
}
variable "container_image" {
description = "Container image to deploy"
type = string
}
# Deployment resource
resource "kubernetes_deployment" "deployment" {
metadata {
name = var.deployment_name
namespace = "example"
labels = {
app = var.deployment_name
}
}
spec {
replicas = 3
selector {
match_labels = {
app = var.deployment_name
}
}
template {
metadata {
labels = {
app = var.deployment_name
}
}
spec {
dns_policy = "ClusterFirst"
container {
name = "nginx"
image = var.container_image
port {
container_port = 8080
}
}
}
}
}
}
Dhall ([official example](https://github.com/dhall-lang/dhall-kubernetes/blob/master/examples/deployment.dhall)):

`-- Type definitions for our configuration`
let Kubernetes =
https://raw.githubusercontent.com/dhall-lang/dhall-kubernetes/master/package.dhall
let deploymentName : Text = "mydep"
let containerImage : Text = "nginx:latest"
let deploymentLabels =
toMap { app = deploymentName }
let containerPort =
Kubernetes.ContainerPort::{
, containerPort = 8080
}
let container =
Kubernetes.Container::{
, name = "nginx"
, image = Some containerImage
, ports = Some [ containerPort ]
}
let podTemplateSpec =
Kubernetes.PodTemplateSpec::{
, metadata = Some Kubernetes.ObjectMeta::{ labels = Some deploymentLabels }
, spec = Some Kubernetes.PodSpec::{
, containers = [ container ]
, dnsPolicy = Some "ClusterFirst"
}
}
let deploymentSpec =
Kubernetes.DeploymentSpec::{
, replicas = Some 3
, selector = Kubernetes.LabelSelector::{ matchLabels = Some deploymentLabels }
, template = podTemplateSpec
}
in Kubernetes.Deployment::{
, metadata = Kubernetes.ObjectMeta::{
, name = Some deploymentName
, namespace = Some "example"
, labels = Some deploymentLabels
}
, spec = Some deploymentSpec
}
Jsonnet ([more Kubernetes examples](https://jsonnet.org/articles/kubernetes.html)):

`// Input parameters`
local params = {
deploymentName: 'mydep',
containerImage: 'nginx:latest',
};
// Helper to generate consistent labels
local labels = {
app: params.deploymentName,
};
// Main deployment definition
{
apiVersion: 'apps/v1',
kind: 'Deployment',
metadata: {
name: params.deploymentName,
namespace: 'example',
labels: labels,
},
spec: {
replicas: 3,
selector: {
matchLabels: labels,
},
template: {
metadata: {
labels: labels,
},
spec: {
dnsPolicy: 'ClusterFirst',
containers: [
{
name: 'nginx',
image: params.containerImage,
ports: [
{
containerPort: 8080,
},
],
},
],
},
},
},
}
CUE ([Kubernetes tutorial](https://github.com/cue-labs/cue-by-example/tree/main/003_kubernetes_tutorial#controlling-kubernetes-with-cue)) — I removed the schema since that probably would be imported:

`// Input parameters`
params: {
deploymentName: string
containerImage: string
}
// Default values
params: {
deploymentName: "mydep"
containerImage: "nginx:latest"
}
// Deployment configuration
deployment: #Deployment & {
metadata: {
name: params.deploymentName
namespace: "example"
labels: {
app: params.deploymentName
}
}
spec: {
replicas: 3
selector: {
matchLabels: {
app: params.deploymentName
}
}
template: {
metadata: {
labels: {
app: params.deploymentName
}
}
spec: {
containers: [{
name: "nginx"
image: params.containerImage
ports: [{
containerPort: 8080
}]
}]
}
}
}
}
// Output the deployment
deployment
Pkl ([examples](https://github.com/apple/pkl-k8s-examples/tree/main/pkl)):

`module deployment`
import "package://pkg.pkl-lang.org/k8s/apps/v1/1.27" as apps
import "package://pkg.pkl-lang.org/k8s/core/v1/1.27" as core
// Input parameters
deployCfg {
name: String = "mydep"
image: String = "nginx:latest"
}
// Create deployment using official K8s types
output = new apps.Deployment {
metadata {
name = deployCfg.name
namespace = "example"
labels = new {
app = deployCfg.name
}
}
spec {
replicas = 3
selector {
matchLabels = new {
app = deployCfg.name
}
}
template {
metadata {
labels = new {
app = deployCfg.name
}
}
spec {
dnsPolicy = "ClusterFirst"
containers = List(
new core.Container {
name = "nginx"
image = deployCfg.image
ports = List(
new core.ContainerPort {
containerPort = 8080
}
)
}
)
}
}
}
}
Nickel ([example](https://github.com/tweag/nickel-kubernetes/blob/master/examples/redis-replication-controller.ncl)):

`# Type contracts`
let DeploymentConfig = {
name | Str,
image | Str,
}
# Function to generate labels
let makeLabels = fun name => {
app = name
}
# Main deployment generator function
let makeDeployment = fun config | DeploymentConfig => {
apiVersion = "apps/v1",
kind = "Deployment",
metadata = {
name = config.name,
namespace = "example",
labels = makeLabels config.name,
},
spec = {
replicas = 3,
selector = {
matchLabels = makeLabels config.name,
},
template = {
metadata = {
labels = makeLabels config.name,
},
spec = {
dnsPolicy = "ClusterFirst",
containers = [
{
name = "nginx",
image = config.image,
ports = [
{
containerPort = 8080,
},
],
},
],
},
},
},
}
# Default configuration
let defaultConfig = {
name = "mydep",
image = "nginx:latest",
}
# Generate the deployment with default config
makeDeployment defaultConfig
KCL ([examples](https://github.com/kcl-lang/examples)):

`import k8s.api.apps.v1 as appsv1`
import k8s.api.core.v1 as corev1
# Configuration parameters
schema DeploymentConfig:
name: str = "mydep"
image: str = "nginx:latest"
# Configuration values
config = DeploymentConfig {}
# Generate deployment using standard library types
deployment = appsv1.Deployment {
metadata = corev1.ObjectMeta {
name = config.name
namespace = "example"
labels.app = config.name
}
spec = appsv1.DeploymentSpec {
replicas = 3
selector = corev1.LabelSelector {
matchLabels.app = config.name
}
template = corev1.PodTemplateSpec {
metadata = corev1.ObjectMeta {
labels.app = config.name
}
spec = corev1.PodSpec {
dnsPolicy = "ClusterFirst"
containers = [
corev1.Container {
name = "nginx"
image = config.image
ports = [
corev1.ContainerPort {
containerPort = 8080
}
]
}
]
}
}
}
}
Starlark ([example](https://github.com/cruise-automation/isopod/blob/master/examples/ingress.ipd)):

`# Helper function to create consistent labels`
def make_labels(name):
return {"app": name}
# Main deployment generator function
def make_deployment(name = "mydep", image = "nginx:latest"):
"""Creates a Kubernetes deployment configuration.
Args:
name: The name of the deployment
image: The container image to deploy
Returns:
Dictionary containing the deployment configuration
"""
return {
"apiVersion": "apps/v1",
"kind": "Deployment",
"metadata": {
"name": name,
"namespace": "example",
"labels": make_labels(name),
},
"spec": {
"replicas": 3,
"selector": {
"matchLabels": make_labels(name),
},
"template": {
"metadata": {
"labels": make_labels(name),
},
"spec": {
"dnsPolicy": "ClusterFirst",
"containers": [
{
"name": "nginx",
"image": image,
"ports": [
{
"containerPort": 8080,
},
],
},
],
},
},
},
}
# Default deployment configuration
deployment = make_deployment()
def main(ctx):
"""Main entry point for Starlark configuration.
Args:
ctx: The rule context
Returns:
The deployment configuration
"""
return deployment
Just as with different general-purpose programming languages, obviously [the syntax](https://github.com/lightbend/config/blob/master/HOCON.md#syntax) of each configuration language is somewhat different: curly braces or not, trailing commas or not, double quotes vs single quotes vs no quotes, strictly nested vs not, colon vs equal sign, type names or not, schema definitions inside the language or not, explicit generation statements or not, additional keywords or punctuation, etc. Some have a little more boilerplate and some a little less. Type safety works a bit differently in each. Different languages will feel more familiar to different people, depending on what other languages they know. For instance, Dhall may be [more familiar to people who know Haskell](https://pv.wtf/posts/taming-the-beast#dhall).

With this example there’s not a dramatic benefit of any of these languages. I could have used `envsubst`
. I did not use a more complicated example, such as building a reusable function or module around the Deployment, partly just to keep the examples simple and partly because I’ve seen [such abstractions erode](/the-tension-between-flexibility-and-simplicity-in-infrastructure-as-code-6cec841e3d16) many times, and have seen attempts to [make configuration more reusable backfire](https://medium.com/itnext/how-software-engineering-instincts-clash-with-infrastructure-as-code-6b18a9cd9cef). A Kubernetes Deployment with lots of parameters isn’t going to be any simpler in any of these languages.

In any case, no configuration language is going to be more powerful than a tool using general-purpose languages like cdk8s or Pulumi. Configuration languages are sort of a compromise on the spectrum between data formats like JSON and YAML and general-purpose languages. For some, a Goldilocks option, and for others neither here nor there. Or just a clickstop on the [Configuration Complexity Clock](https://mikehadlow.blogspot.com/2012/05/configuration-complexity-clock.html).

The intent is that constraints imposed by the languages should make it easier to catch and prevent mistakes, and perhaps make configurations easier to read and/or write. However, while I have read many [lengthy debates](https://news.ycombinator.com/item?id=22787332) online regarding which languages are “better” or “worse” than others, they have all been subjective, and without consensus. I haven’t seen any studies of the quantitative benefits of expressing configuration generators in different languages. If you’re aware of any, please send me a pointer!

Additionally, while the ecosystems around the languages are sometimes superior to template languages ([Pkl emphasizes their integrations](https://github.com/apple/pkl/discussions/7) more than specific language features), they can’t really compare to general-purpose languages. Configuration languages have less available documentation, examples, educational content, tool integrations, service integrations, etc.

One reason is that configuration languages are all much less widely used than popular programming languages such as Python or Javascript. The most popular language of these by far is HCL, due of course to the popularity of Terraform. I don’t see HCL used outside of the Terraform ecosystem, though, and some people even [wrap uses of it with YAML](https://github.com/AppsFlyer/terra-crust). Like [Helm’s template syntax](/kubernetes-configuration-in-2024-434abc7a5a1b), not everyone loves it, but it mostly gets the job done.

Ok, so what is my point?

If you’ve read this far, you have probably guessed that I don’t think configuration languages are the best solution to configuration complexity. Each language has its pros and cons, but none moves the needle much. They are micro-optimizations rather than macro-optimizations. As [I’ve mentioned before](/fundamental-challenges-with-infrastructure-as-code-imply-the-language-doesnt-matter-41030475c296), no new configuration language will address the [fundamental issues with IaC](/the-12-anti-factors-of-infrastructure-as-code-acb52fba3ae0). To make significant improvements, we need to try some macro-level changes to the overall approach.

Do you have a favorite configuration language that I didn’t cover? What are its strengths? Have you found any significant, measurable benefits of using a configuration language over other representations and approaches? Have you found any of the static analysis tools for the language especially helpful? Did others in your organization have any difficulty learning the language? Do you wonder why we’re still writing configuration files by hand in 2025?

Feel free to reply here, or send me a message on [LinkedIn](https://www.linkedin.com/in/bgrant0607/), [X/Twitter](https://x.com/bgrant0607), or [Bluesky](https://bsky.app/profile/bgrant0607.bsky.social), where I plan to crosspost this.

If you found this interesting, you may be interested in other posts in my [Infrastructure as Code and Declarative Configuration series](https://medium.com/@bgrant0607/list/infrastructure-as-code-and-declarative-configuration-8c441ae74836).