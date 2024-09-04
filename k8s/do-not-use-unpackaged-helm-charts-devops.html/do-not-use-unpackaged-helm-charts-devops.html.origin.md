**TL;DR**

Don't install/template from unpackaged Helm charts directly because
Helm CLI has many bugs related to packaging and dependencies, especially
bug no. [helm/helm
#11484](https://github.com/helm/helm/issues/11484) and you will get unexpected behavior.

Also, if your users use your Helm chart packaged, then you should test the Helm chart packaged and vice versa.

## ToC
## Intro
The rule of thumb is
`your test environment should be as close as possible to the production environment`
to ensure the software works correctly.

This rule is critical when you run your software as a SaaS and even more when you deliver a product artifact to your customers.

You probably know that rule, but sometimes you think,
`That's a small drift. What could it do?` In reality, it
could do a lot 😁

## Problem
In my case, I'm using [Trunk-Based Development](https://trunkbaseddevelopment.com/),
and with each Pull Request, the changes are built and deployed to a test
environment.

I maintain one of upstream Helm charts, and my mistake was deploying the unpackaged Helm chart (directly from the chart directory and skipping the packing step) in the CI pipeline. Which is basically against the rule mentioned above.

Later, I found some unexpected behavior reported by the customer, and after the investigation, I found that the Helm CLI had many bugs in the packaging step.

Well, Helm CLI has a lot of bugs in handling dependencies during the
packaging step. For example [#11484](https://github.com/helm/helm/issues/11484), [#12954](https://github.com/helm/helm/issues/12954), [#13214](https://github.com/helm/helm/issues/13214), and
more.

I hit two at the same time, where Helm `merges` the same
charts from the same repo even if they are under different aliases!

## Example
Let's see that in action ... here is an example (executed with Helm
CLI version [v3.15.1 ](https://github.com/helm/helm/releases/tag/v3.15.1)
which releseed in May 2024):

# my-chart/Chart.yaml name: my-chart version: 1.0.0 appVersion: 1.0.0 dependencies: - name: postgresql alias: psql-14 repository: https://charts.bitnami.com/bitnami version: 14.x.x - name: postgresql alias: psql-13 repository: https://charts.bitnami.com/bitnami version: 13.x.x
If you installed/templated that chart from the unpackaged directory, everything will work as expected:

$ helm dependency update $ helm dependency build $ helm template . | grep -o "Source: my-chart/charts/psql-../" | sort | uniq Source: my-chart/charts/psql-13/ Source: my-chart/charts/psql-14/
However, if you try to package it, you will see a single
**Frankenstein** package called `postgres` which
has some files from the Bitnami chart `postgresql/13.x.x` and
`postgresql/14.x.x` 🤯

In many cases (depending on the charts, it could not even render and show an error).

$ helm dependency update $ helm dependency build $ helm package . $ helm template my-chart-1.0.0.tgz | grep -o "Source: my-chart/charts/psql-../" | sort | uniq Error: template: my-chart/charts/postgresql/templates/networkpolicy-egress.yaml:6:18: executing "my-chart/charts/postgresql/templates/networkpolicy-egress.yaml" at <.Values.networkPolicy.enabled>: nil pointer evaluating interface {}.enabled Use --debug flag to render out invalid YAML
## Workaround
Till that issue is fixed in Helm CLI (issue no. [#11484](https://github.com/helm/helm/issues/11484)), the only
workaround available is to use a different name or different repo for
each dependency.

dependencies: - name: postgresql alias: psql-14 repository: https://charts.bitnami.com/bitnami version: 14.x.x # Here I made a local copy of the PostgreSQL v13 Helm chart. - name: postgresql alias: psql-13 repository: "file://../postgresql-13" version: 13.x.x
## Conclusion
This post doesn't tell you not to use unpackaged Helm charts but emphasizes the importance of testing what your users will use. If your users use your Helm chart packaged, then you should test the Helm chart packaged and vice versa.

It's annoying, but at least it's better than the bug in [#12488](https://github.com/helm/helm/issues/12488), which has
been open for more than 2 years (the issue was reported in 2022, and
Helm maintainers made a partial fix, and the other half is in [#12488](https://github.com/helm/helm/issues/12488)).

Anyway ... Happy Helming! (but I still like [Kustomize](https://tech.aabouzaid.com/search/label/Kustomize)
more TBH 😂)