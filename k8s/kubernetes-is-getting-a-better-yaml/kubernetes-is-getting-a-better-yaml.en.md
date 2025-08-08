The data serialization language used to deploy and run Kubernetes has gotten an overhaul.

The [upcoming 1.34 release](https://kubernetes.io/blog/2025/07/28/kubernetes-v1-34-sneak-peek/) of Kubernetes may come with KYAML, a strict subset of YAML formatted specially for [Kubernetes users](https://thenewstack.io/kubernetes/).

“YAML is the programming language of Kubernetes,” noted [Nigel Douglas](https://allthingsopen.org/authors/nigel-douglas), head of developer relations at [Cloudsmith](https://cloudsmith.com/company/about), a cloud native package management service, in an interview with TNS.

Yet, many users feel frustrated by a number of [design quirks](https://thenewstack.io/yall-against-my-lingo-why-everyone-hates-on-yaml/) in YAML that cause extra work and additional debugging (even as the creator himself is working to make [YAML a full-fledged programming language](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/)).

The solution to YAML’s woes? Add in a pinch of [JSON](https://thenewstack.io/an-introduction-to-json/).

## Paging Dr. Null

YAML is [used throughout](https://thenewstack.io/from-yaml-to-platforms-the-kubernetes-deployment-journey/) the Kubernetes ecosystem: to create a network policy, for writing a deployment manifest or for Helm deployment files.

One problem: YAML doesn’t digest [white spaces](https://thenewstack.io/spaces-vs-tabs-a-20-year-debate-and-now-this-what-the-hell-is-wrong-with-go/) well. Particularly, when users come with nested instructions, they must pay close attention to the number of indentations used. Formatting  is a tedious exercise for [the cloud native warrior,](https://thenewstack.io/cloud-native/) yet having the wrong number of idents in the code can trip up Helm, for instance.

Likewise, optional quotes in YAML have led to ambiguity, which is always dangerous for a computer. The challenge with quotes is aptly illustrated through “[The Norway Problem](https://hitchdev.com/strictyaml/why/implicit-typing-removed/),” in which the failure to encapsulate a two-letter country abbreviation with a set of quotes may trip up a parser on the lookout for reserved keywords, such as “NO” for Norway.

Or, in another case, `Last_Name=Null` for someone actually named Richard Null.

As many have noted, JSON could also be used in place of YAML, though it comes with its own limitations in a Kubernetes environment: no comment support and a strict adherence to trailing commas and quoted keys.

## Yet Another Markup Language

“The most frustrating part of YAML is that it doesn’t have to be this bad. YAML is a very broad specification. Inside that specification is a reasonable grammar screaming to be let out,” Kubernetes proposal [KEP 5295](https://github.com/kubernetes/enhancements/issues/5295) asserts.

KYAML is that specification, at least for Kubernetes users. KYAML is “built in a way that it’s, like, totally compatible with the existing design around Kubernetes objects,” Douglas said.

KYAML is a strict subset of YAML. All KAYML files are also valid YAML, and they can be used to write manifests and [Helm charts](https://thenewstack.io/what-the-helm-the-tool-we-all-love-and-sometimes-hate/), with no additional flags for K8s.

If included in Kubernetes 1.34 (still being finalized), KYAML will work with `kubectl` Kubernetes command line, which will output in KYAML with a special flag (i.e., `kubectl get -o kyaml`).

Here are the additional rules for KYAML.

* Double-quotes are value strings.
* Keys are unquoted unless potentially ambiguous.
* Mappings (associative arrays) use braces `{}`.
* Lists use brackets `[]`.

These rules mimic JSON, though unlike JSON, KYAML supports comments and trailing commas and doesn’t need quoted keys.

Also, KYAML is [not sensitive](https://github.com/kubernetes/enhancements/blob/master/keps/sig-cli/5295-kyaml/README.md) to white space.

Here is a sample provided by the proposal:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | $ kubectl get -o kyaml svc hostnames |
|  | --- |
|  | { |
|  | apiVersion: "v1", |
|  | kind: "Service", |
|  | metadata: { |
|  | creationTimestamp: "2025-05-09T21:14:40Z", |
|  | labels: { |
|  | app: "hostnames", |
|  | }, |
|  | name: "hostnames", |
|  | namespace: "default", |
|  | resourceVersion: "37697", |
|  | uid: "7aad616c-1686-4231-b32e-5ec68a738bba", |
|  | }, |
|  | spec: { |
|  | clusterIP: "10.0.162.160", |
|  | clusterIPs: [ |
|  | "10.0.162.160", |
|  | ], |
|  | internalTrafficPolicy: "Cluster", |
|  | ipFamilies: [ |
|  | "IPv4", |
|  | ], |
|  | ipFamilyPolicy: "SingleStack", |
|  | ports: [{ |
|  | port: 80, |
|  | protocol: "TCP", |
|  | targetPort: 9376, |
|  | }], |
|  | selector: { |
|  | app: "hostnames", |
|  | }, |
|  | sessionAffinity: "None", |
|  | type: "ClusterIP", |
|  | }, |
|  | status: { |
|  | loadBalancer: {}, |
|  | }, |
|  | } |

## But I Still Hate It

As with any modified data format, the changes will be [hotly contested](https://thenewstack.io/typescript-vs-javascript/). The developers anticipate this.

“Syntax has always been a magnet for arguments in our industry. We expect this to be no exception. Reasonable people will disagree with our choices, which is fine, but we should hold a strong opinion on this,” the developers warned in the [ReadMe file](https://github.com/kubernetes/enhancements/blob/master/keps/sig-cli/5295-kyaml/README.md), originally authored by [Tim Hockin](https://thenewstack.io/tim-hockin-kubernetes-needs-a-complexity-budget/).

And the reactions are coming in already.

“It’s better than JSON, and I see why this is better than YAML, but I still hate it,” one [user on Reddit wrote](https://www.reddit.com/r/kubernetes/comments/1md8wle/kyaml_looks_like_json_but_named_after_yaml/).

A quick search has shown that at least one programming-language-specific implementation of KYAML has been made for [the Go programming language](https://pkg.go.dev/sigs.k8s.io/kustomize/kyaml).

Other approaches have been taken, including the stripped-down [StrictYAML](https://hitchdev.com/strictyaml/features-removed/), though KYAML has a fast track in the new Kubernetes version. Let’s see where else it can be used.

*Kubernetes 1.34 is expected to be released in late August.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 25 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)