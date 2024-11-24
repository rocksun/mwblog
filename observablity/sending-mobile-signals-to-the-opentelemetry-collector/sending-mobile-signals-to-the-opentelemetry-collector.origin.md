# Sending Mobile Signals to the OpenTelemetry Collector
![Featued image for: Sending Mobile Signals to the OpenTelemetry Collector](https://cdn.thenewstack.io/media/2024/11/47c27d1e-metrics-1024x576.jpg)
Delivering meaningful experiences is the main goal of any mobile application. Shoppers want to make purchases; influencers want to upload their latest viral post; and dog walkers want to know when and where to take their next pup. The user, not computational output, ultimately determines how well the app is working.

Creating a better user experience requires mobile [observability](https://thenewstack.io/observability/). To tie together what a user is doing and how the entire software stack is performing, [developers should unite their mobile telemetry](https://thenewstack.io/developing-a-mobile-crash-model-for-opentelemetry/) with other indicators of overall system health.

Luckily, this is precisely why [OpenTelemetry](https://opentelemetry.io/) exists. Using signals like traces, logs and metrics, [OpenTelemetry (or “OTel”)](https://thenewstack.io/why-the-latest-advances-in-opentelemetry-are-significant/) seeks to create a shared language that connects application data, or “telemetry,” collected from different software systems. The same OpenTelemetry components that unite information about microsystems in a backend architecture can also link mobile telemetry to web services and databases in that architecture.

In this tutorial, we’ll show how to link signals from a mobile app to an example tracing backend using the [OpenTelemetry Collector](https://thenewstack.io/how-the-opentelemetry-collector-scales-observability/).

## The OpenTelemetry Collector
When exporting telemetry from your mobile app, you’ll need a way to receive, or ingest, and process an application’s signals before you begin to analyze that data. Traditionally, this has been done by deploying vendor agents as “middlemen” that connect and process app signals using proprietary formats.

Instead, OpenTelemetry uses the concept of a Collector for this purpose.

According to [its documentation](https://opentelemetry.io/docs/collector/), the OTel Collector “offers a vendor-agnostic implementation of how to receive, process and export telemetry data.” The OTel Collector is a powerful entry point for traces from the mobile app, as it will serve as an initial ingestion, filtering and forwarding point in our mobile telemetry pipeline.

## Capturing Mobile Telemetry
To get traces out of an iOS app, we’ll use instrumentation from the [Embrace Apple SDK](https://github.com/embrace-io/embrace-apple-sdk/), an open source, Swift-native software development kit [built on OTel](https://embrace.io/blog/embraces-ios-sdk-is-built-on-otel-but-what-does-this-mean/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-collector). A variety of automatic instrumentation for mobile concepts like views and push notifications are captured by the Embrace SDK, which are then emitted as OpenTelemetry [traces](https://thenewstack.io/spans-what-are-they-and-why-should-mobile-engineers-care/) and logs.

We’ll use the Embrace Apple SDK to attach a compatible [OTel Exporter](https://opentelemetry.io/docs/languages/js/exporters/) to an app, and then send mobile traces to the OTel Collector. The mobile application will be the [Embrace Outdoors application](https://github.com/embrace-io/embrace-outdoors-demo), which is available open source as well. Embrace Outdoors adds vital mobile instrumentation to an iOS app with the Embrace Apple SDK, such as automatic networking capture and manual tracing of key user flows. For example, here is an example trace for part of the login flow:

Exporters are configured in the Embrace Apple SDK when the [SDK is started](https://embrace.io/docs/ios/open-source/), usually as close to app launch as possible. Here, we can attach any of the compatible [Swift-language OTel Exporters](https://github.com/open-telemetry/opentelemetry-swift/tree/main/Sources/Exporters) that are maintained by engineers in the OTel ecosystem. However, the OpenTelemetry Protocol (OTLP) also creates a set of rules to transmit over HTTP or gRPC so that any Exporter following the protocol can send telemetry.

### Configuring the OTel Exporter
Let’s design our own Exporter using gRPC to send to a local OTel Collector. This Exporter will need to conform to the OpenTelemetry protocol (OTLP) and import the Swift NIO and gRPC libraries. Then we’ll connect it to the localhost port specified for gRPC, 4317.

Then we’ll add this Exporter to the SDK when we configure it:

Now that the Exporter is hooked up to our app, any traces we create in the app will be exported in near-real time. That means network calls will automatically send a payload upon completion, and complex interactions that we’ve traced from start to finish will show in a waterfall view like in the login example above.

Because the Embrace SDK is built on OpenTelemetry, we can send telemetry wherever we want. (Well, wherever we want that also happens to support OTel.)

In the next section, we’ll configure the OTel Collector to view our traces in a tool for distributed traces called [Zipkin](https://zipkin.io/). Zipkin is an open source visualization tool that, while separate from OTel, is configurable from within the Collector.

## Configuring the OTel Collector
To configure the OTel Collector, we will use Docker and some YAML files that outline the Collector and its capabilities. One YAML file, the `collector-config.yaml`
file, will contain the specific capabilities we want in the Collector, while another, the `docker-compose.yaml`
, will deploy the Collector and Zipkin. To avoid any trouble later, open Docker now.

The OTel Collector has a variety of capabilities that allow companies to use it at scale for data ingestion, processing and forwarding. These include important security properties, sampling settings and other features that are beyond the scope of this tutorial. For our sake, we’ll want to use Receivers and Exporters.

[OTel Receivers](https://github.com/open-telemetry/opentelemetry-collector/blob/main/receiver/README.md) are “how data gets into the OpenTelemetry Collector.” Simple enough. We’ll configure a Receiver that looks for mobile data over the gRPC port outlined above. OTel’s default network port for gRPC is 4317, so this preference is built into the Collector. In the `collector-config`
, add the following:
After receiving the telemetry from our iOS app’s Exporter, we’ll want the Collector itself to send the telemetry to Zipkin. The Zipkin distribution has a port of its own, 9411, so be sure to define this in the `collector-config`
as well:

We’ve defined the Receiver and the Exporter, but now we’ll need to define how the OTel Collector uses these items to run as a service. At the end of `collector-config`
define the service for traces in this OTel Collector (entire file included for clarity):

This is the entire configuration for our Collector. We will add more to it to see how mobile traces can better serve our purposes, but that will be in the next section. Before that, we’ll need to see how to deploy the Collector.

### Deploying the Collector
In the `docker-compose`
, let’s define the components necessary for deployment of our architecture: the Collector and Zipkin. This file simply lays out which Docker images the components should use and what the relationship is between them. For example, in our configuration below, the Collector will use the latest image available and will depend on Zipkin as a place to send it.

Your `docker-compose`
file should look something like this:

You can now deploy your OTel Collector, with Zipkin connected, using the command `docker compose up`
. Your terminal should show output both from the Collector and Zipkin:

## Refining the Mobile Signals You Want to Use
With the Collector running and the iOS app in use, you’ll start to see traces run through the Collector to Zipkin. By attaching the gRPC Exporter to the iOS app, and configuring the OTel Collector to export to Zipkin, we can recreate the login trace that we previously saw in the Embrace dashboard and display it in Zipkin:

As a reminder, you may wish to exclude certain information from Zipkin or wherever you are sending your mobile traces.

For example, to measure SDK initialization time, and hopefully set an example for other mobile libraries, the Embrace Apple SDK provides an `emb-setup`
trace. This trace could be combined with other app signals and library initializations to create an “app startup” measurement that is unique to the specific app being launched, rather than one-size-fits-all. However, the other libraries in the Embrace Outdoors app are either not built on OTel or don’t allow us to measure their processes, so the `emb-setup`
trace isn’t actionable right now.

We don’t need the `emb-setup`
trace, but digging into the mobile code to remove it would require deep investigation and wrapping of native libraries. Instead, let’s use the OTel Collector to exclude that trace. This is much simpler to do, as the Collector provides a set of [processors](https://github.com/open-telemetry/opentelemetry-collector/blob/main/processor/README.md) to adjust our data after it is received but before it is exported.

We can add a [filter processor](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/filterprocessor/README.md) that will stop any `emb-setup`
in its tracks by adding the Processor to our `collector-config`
:

Make sure to add this as part of the Collector’s trace service as well:

After this change, Embrace SDK setup traces will be excluded from export, and thus from visualization in Zipkin. You can add as many processors as you need to exclude, transform and sample telemetry.

## Conclusion
The Embrace Apple SDK is a superset of the [otel-swift](https://github.com/open-telemetry/opentelemetry-swift) instrumentation and is designed specifically for mobile. Its capabilities let you send mobile telemetry to the same places you send backend observability data.

Why should a development team combine these? Well, can you know that your system is healthy if you aren’t accounting for the user experience? For example, your networking shouldn’t just reflect the services that transmit data. They need to treat [app instances and users like clients of that same networking system](https://thenewstack.io/why-your-mobile-app-needs-client-side-network-monitoring/). Only then can you turn that information into [meaningful indicators](https://embrace.io/blog/mobile-slo-guide/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-collector) of overall ecosystem health and performance.

If you have questions or would like to learn more about setting up OpenTelemetry in your mobile apps, you can join the [Embrace Slack Community](https://community.embrace.io/). In addition, visit the [Embrace website](https://embrace.io/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=otel-collector) to learn more about how you can deliver the best user experiences.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)