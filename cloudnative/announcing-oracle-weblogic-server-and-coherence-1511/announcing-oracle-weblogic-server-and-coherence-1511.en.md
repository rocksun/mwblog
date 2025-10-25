Oracle is pleased to announce the release of Oracle WebLogic Server and Coherence Version 15.1.1! This new version brings updated support for Jakarta EE 9.1, continued compatibility with Java SE 17 and 21, and comprehensive support for running Spring Framework 6.x and Hibernate 6.6.x, along with applications leveraging Jakarta dependencies.

WebLogic Server and Coherence 15.1.1 are supported both on-premises and in the cloud, including Oracle Cloud certification and tools for running WebLogic Server and Coherence in containers and Kubernetes environments. Our solutions integrate with a wide array of platforms, Oracle products, and services to deliver exceptional performance and availability for your applications. The latest software is available for download from the [Oracle Technology Network](https://www.oracle.com/middleware/technologies/fusionmiddleware-downloads.html) and the [Oracle Software Delivery Cloud](https://edelivery.oracle.com/osdc/faces/SoftwareDelivery). You can also review the updated [product documentation](https://docs.oracle.com/en/middleware/standalone/weblogic-server/15.1.1/index.html) for further details.

**Support for Spring Framework 6.x and Hibernate 6.6.x**

With enhanced support for Jakarta EE 9.1, WebLogic Server and Coherence 15.1.1 empower applications to take advantage of the latest third-party libraries, improving upgradeability and helping to future-proof your enterprise solutions. Applications built with Spring Framework 6.x and Hibernate 6.6.x, which utilize “Jakarta” package namespaces, can now be seamlessly deployed to WebLogic Server and Coherence 15.1.1.

**Upgrade Guidance**

We are committed to maintaining compatibility and streamlining the upgrade process across WebLogic Server versions. A notable requirement in WebLogic Server 15.1.1 is the migration of applications to the “Jakarta” namespace. Tools leveraging community-based OpenRewrite technology simplify and automate this transition, especially for applications upgrading from WebLogic Server 12.2.1.4, 14.1.1, and 14.1.2. Comprehensive OpenRewrite recipes reduce human error and reduce costs, particularly when managing large application portfolios.

The general upgrade process involves:

– Transforming applications

– Upgrading the domain

– Deploying the transformed applications

Detailed [upgrade guidance](//docs.oracle.com/en/middleware/standalone/weblogic-server/15.1.1/wlupg/index.html) and hands-on tutorials are available for reference, please see [Rewrite WebLogic](https://github.com/oracle/rewrite-recipes/blob/main/rewrite-weblogic/README.md).

## **Certificate Management**

WebLogic Server 15.1.1 introduces an automated certificate management feature designed to streamline secure domain configurations, including those using “Secured Production Mode” SSL settings. This new capability automates the generation, renewal, and distribution of certificates within WebLogic domains and servers. It supports certificates issued by the embedded WebLogic CA, external Certificate Authorities, and the OCI Certificates service.

We are making Certificate Management available as a Technical Preview, giving users early access to this functionality. Full support for this feature will be provided in upcoming updates to WebLogic Server 15.1.1, stay tuned to our blog for future announcements.

## **Integration with Oracle Database**

Oracle WebLogic Server continues to offer best-in-class integration with the Oracle Database. Version 15.1.1 bundles the Oracle JDBC 23ai driver, providing certified support for Oracle Database 19c and 23ai and unlocking new database functionality. Notably, with 23ai support, WebLogic Server can now support JSON Databases, allowing users to store and query relational and JSON data through SODA drivers.

Other JDBC 23ai driver enhancements include:

– Improved diagnostics and logging

– Native UCP data source support for Oracle Database Sharding

– Native Boolean datatype support

– Enhanced Transparent Application Continuity

WebLogic Server 15.1.1 also introduces tuning attributes for data sources, optimizing connection pools during periods of inactivity or low utilization.

## **Observability and OpenTelemetry Support**

With WebLogic Server’s support for the Oracle JDBC 23ai driver, users can leverage OpenTelemetry for comprehensive observability from WebLogic Server to Oracle Database 23ai. OpenTelemetry provides vendor-neutral telemetry, enhancing performance monitoring, expediting troubleshooting, and supporting proactive, data-driven operations across enterprise Java applications. In the article [Observability and Monitoring of WebLogic Server with OpenTelemetry](https://blogs.oracle.com/weblogicserver/post/wls-observability) you will find a proof-of concept – how to leverage features of OpenTelemetry in WebLogic environments.

**Cloud Native and Kubernetes Support**

The WebLogic Kubernetes Toolkit has been enhanced to fully support WebLogic Server 15.1.1 domains, enabling immediate deployment to Kubernetes. The WebLogic Kubernetes Operator efficiently manages the entire lifecycle of WebLogic Server 15.1.1 domains, ensuring streamlined operations across both legacy and new deployments. WebLogic Deploy Tooling (WDT) is also updated to support introspection, configuration, and domain creation on VMs, Kubernetes Persistent Volumes, and cloud environments.

WebLogic domains running in Kubernetes can benefit from cluster elasticity through seamless integration with Horizontal Pod Autoscalers (HPA) and metrics provided by Prometheus or KEDA. The operator can automatically scale clusters in or out based on traffic thresholds, supporting dynamic, highly available environments. You might be interested in reading  the blog [Clusterception: Autoscaling WebLogic Clusters on Kubernetes using Prometheus and Keda.](https://medium.com/oracledevs/clusterception-autoscaling-weblogic-clusters-on-kubernetes-using-prometheus-and-keda-cd4550c458c9)

Oracle continues to publish WebLogic Server and Coherence images to the Oracle Container Registry (OCR) on a quarterly basis, pre-patched with the latest Critical Patch Updates (CPUs).  Images from OCR allow to automate updates and secure your WebLogic and Coherence 15.1.1 domains running in Kubernetes.

## **Oracle Coherence 15.1.1**

Coherence 15.1.1 runs on Java 17 and Java 21, remains compatible with Jakarta EE 9.1 specifications, and introduces several enhancements, including:

– Vector DB

Coherence 15.1.1 adds support for the optimized storage of dense vector embeddings within the Coherence cluster, and the ability to perform similarity searches across those embeddings in parallel, using Coherence aggregators. It also allows users to create HNSW and Binary Quantization-based vector indices, which can significantly improve search performance.

– Lucene Full-Text Indexing

Coherence 15.1.1 also adds support for partitioned Lucene full-text indices, and parallel search across those indices, with sophisticated re-ranking of the results that ensures that the best possible matches are returned to the client.

– Coherence RAG

Coherence RAG builds on the core Vector DB and Lucene indexing functionality, and adds higher level APIs that allow you to easily integrate similarity or hybrid search results with remote LLMs in order to implement end-to-end RAG solution using Generative AI. It also provides support for massively parallel ingestion and vectorization of document content from multiple document sources, including custom ones, and seamless integration with local and remote embedding, re-ranking and chat models.

Coherence RAG allows you to utilize hundreds, or even thousands of CPU core to perform vector embeddings creation at the speed comparable, or even faster, than when running on a GPU, and will take the advantage of the GPUs as well, if they are available.     

– OpenTelemetry Support for Remote Clients

Coherence 15.1.1 adds OpenTelemetry support to remote Extend and gRPC Java clients as well, allowing users to trace the requests within Coherence application truly end-to-end: from a remote client, all the way to the external data store that is used to ultimately store the data, if one is present, or Coherence storage layer, including built-in disk persistence, if not.

 **Support Lifecycle**

WebLogic Server and Coherence 15.1.1 are designated as a Long-Term Support (LTS) release, which means five years of Premier Support plus three years of Extended Support. This provides eight years of bug and security fixes, ensuring superior application performance, reliability, and security, with clear modernization paths for future cloud adoption.

We invite you to try Oracle WebLogic Server and Coherence 15.1.1 today. Stay tuned to our blog for additional announcements and resources to support your journey to modern, cloud-ready applications.