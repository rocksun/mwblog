# How to Remotely Record Java Logs from Containers
![Featued image for: How to Remotely Record Java Logs from Containers](https://cdn.thenewstack.io/media/2024/06/20a8222a-remotely-record-java-logs-from-containers.jpg)
[Java Flight Recorder](https://thenewstack.io/your-guide-to-navigating-openjdk-in-2023/) (JFR) is the go-to technology for recording and viewing [Java Virtual Machine (JVM)](https://thenewstack.io/how-to-avoid-overprovisioning-java-resources/) and system metrics. JFR logs reveal much about the running application, the JVM’s health and the system’s stability. You can access JFR logs by going into the command line or terminal and entering a few commands.
But what if you don’t have direct access to the command line or terminal on the system where the JVM is running, like when the JVM is running in a [container](https://thenewstack.io/containers/)?

Fortunately, you can obtain JFR logs without much configuration using JVM’s Java Management Extension (JMX) connector and a utility for profiling and analysis of JVM-based applications. You’ll want to have working knowledge of JVMs, JFR and JFR logs to follow along with this tutorial.

## Set Up JMX on Your JVM
Before you can access your JVM outside of the command line or terminal, you must set up your JVM to be discoverable and accessible over remote connections. You can accomplish this simply by enabling the JVM’s JMX connector. Configure your Java application with the following VM parameters:

Enables JMX/JMXRMI (Java Management Extensions Remote Management Interface) connectivity.`-Dcom.sun.management.jmxremote`
:Sets the address for the JMX connection. Use an external IP address or host name of the computer or container where the Java program is running.`-Dcom.sun.management.jmxremote.host=<IP/Hostname>`
:Sets the TCP port for the JMX connection.`-Dcom.sun.management.jmxremote.port=<port>`
:Sets the address for the JMXRMI connection. Use the same IP/hostname you used for the JMX connection.`-Djava.rmi.server.hostname=<IP/hostname>`
:Sets the TCP port for the JMXRMI connection. Use the same TCP port you used for the JMX connection.`-Dcom.sun.management.jmxremote.rmi.port=<port>`
:If you are connecting to the JVM from a different machine, you have to unbind ports from localhost.`-Dcom.sun.management.jmxremote.local.only=false`
:
Additionally, you may want to enable JMX authentication/SSL using:

`-Dcom.sun.management.jmxremote.authenticate=true`
`-Dcom.sun.management.jmxremote.ssl=true`
For example:

`-Dcom.sun.management.jmxremote \`
`-Dcom.sun.management.jmxremote.host=192.168.0.166 \`
`-Dcom.sun.management.jmxremote.port=7091 \`
`-Djava.rmi.server.hostname=192.168.0.166 \`
`-Dcom.sun.management.jmxremote.rmi.port=7091 \`
`-Dcom.sun.management.jmxremote.local.only=false \`
`-Dcom.sun.management.jmxremote.authenticate=false \`
`-Dcom.sun.management.jmxremote.ssl=false \`
## Connect to a Remote JVM with Azul Mission Control
To start, you will need a utility for profiling and analysis of JVM-based applications. For demonstration purposes, I will use Azul Mission Control, which is free to download. If you don’t have Azul Mission Control, head over to the [Azul Mission Control download page](https://www.azul.com/products/components/azul-mission-control/#downloads).

Other similar utilities include [Oracle](https://developer.oracle.com/?utm_content=inline+mention) JDK Mission Control, VisualVM, JProfiler, YourKit Java Profiler, AppDynamics for Java, Dynatrace, New Relic APM, Glowroot and Java Flight Recorder (JFR).

In Azul Mission Control, go to the **JVM Browser** and click the **Add JVM Connection** button to create a new custom JVM connection.

Specify the host name/IP address of the remote system and the JMX port number.

If JMX authentication is enabled, enter User and Password.

Click **Test Connection** to make sure your remote JVM is reachable, and click **Finish**.

Your remote JVM now appears in the JVM Browser.

Depending on your network and container setup, port forwarding may need to be set up. Contact your network’s administrator if you need help with [port forwarding](https://thenewstack.io/linux-create-encrypted-tunnels-with-ssh-port-forwarding/).

## Record a JFR From Your Remote JVM
Now that you’re connected to your JVM remotely, it’s time to make a JFR recording.

In Azul Mission Control, go to the JDK Browser, right-click your remote JVM connection and select **Start Flight Recording**.

Select your preferred options and time intervals (either fixed-time recording or continuous recording) based on the JFR log’s size and/or age, and click **Finish**.

Your remote JFR recording has begun. You’re almost there!

Check the progress of the recording by expanding the remote JVM connection in the JVM Browser.

Once your recording has finished, your JFR log opens automatically in Azul Mission Control. You can now check the **Outline** tab to take a deeper look into your JVM’s [performance](https://thenewstack.io/does-garbage-collection-logging-affect-app-performance/) portfolio.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)