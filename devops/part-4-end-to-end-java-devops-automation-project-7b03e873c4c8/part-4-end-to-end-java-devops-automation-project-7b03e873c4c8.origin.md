# Part-4 End-to-End Java DevOps Automation Project
**Prerequisite**: [Part-3 End-to-End Java DevOps Automation Project](/@navin5556/part-3-end-to-end-java-devops-automation-project-63a9cf83935f)
# Setting Up Monitoring with Prometheus, Grafana, and Blackbox Exporter
In this tutorial, we will set up a monitoring system using Prometheus, Grafana, and Blackbox Exporter to monitor your applications and services effectively. We’ll also include how to monitor a Jenkins instance and system metrics with Node Exporter.

## Part 1: Setting Up Prometheus
**1. Install Prometheus**
First, update your package lists and download Prometheus:

`sudo apt update -y`
wget https://github.com/prometheus/prometheus/releases/download/v2.53.1/prometheus-2.53.1.linux-amd64.tar.gz
tar -xvf prometheus-2.53.1.linux-amd64.tar.gz
rm -rf prometheus-2.53.1.linux-amd64.tar.gz
cd prometheus-2.53.1.linux-amd64/
./prometheus &
Prometheus will run on port `9090`
. You can access the Prometheus web interface at `http://<your-public-ip>:9090/`
.

## Part 2: Setting Up Grafana
**1. Install Grafana**
Next, install Grafana:

`sudo apt-get install -y adduser libfontconfig1 musl`
wget https://dl.grafana.com/enterprise/release/grafana-enterprise_11.1.0_amd64.deb
sudo dpkg -i grafana-enterprise_11.1.0_amd64.deb
sudo /bin/systemctl start grafana-server
Grafana will run on port `3000`
. Access it at `http://<your-public-ip>:3000/login`
and log in with the default credentials (username: `admin`
, password: `admin`
). Change the default password after logging in.

## Part 3: Setting Up Blackbox Exporter
**1. Install Blackbox Exporter**
Download and install Blackbox Exporter to monitor your websites:

`wget https://github.com/prometheus/blackbox_exporter/releases/download/v0.25.0/blackbox_exporter-0.25.0.linux-amd64.tar.gz`
tar -xvf blackbox_exporter-0.25.0.linux-amd64.tar.gz
rm -rf blackbox_exporter-0.25.0.linux-amd64.tar.gz
cd blackbox_exporter-0.25.0.linux-amd64/
./blackbox_exporter &
Blackbox Exporter runs on port `9115`
. Access it at `http://<your-public-ip>:9115/`
.

**2. Configure Prometheus for Blackbox Exporter**
Edit your `prometheus.yml`
file to include the Blackbox Exporter configuration:

`scrape_configs:`
- job_name: 'blackbox'
metrics_path: /probe
params:
module: [http_2xx]
static_configs:
- targets:
- http://prometheus.io
- http://3.111.50.86:32106/ #slave node ip and port of kubernetes service for this application boardgame
relabel_configs:
- source_labels: [__address__]
target_label: __param_target
- source_labels: [__param_target]
target_label: instance
- target_label: __address__
replacement: 13.200.8.32:9115 # The blackbox exporter's real hostname:port
Restart Prometheus:

`pkill prometheus`
./prometheus &
We can verify this from inside **Prometheus **-> **Status **-> **Targets**

**3. Add Prometheus as a Data Source in Grafana**
- Log in to Grafana.
- Navigate to Connection > Data Sources > Add Data Source.
- Select Prometheus and enter
`http://<prometheus-ip>:9090/`
as the URL. - Click Save & Test.
**4. Import Blackbox Grafana Dashboard**
- Search for “blackbox grafana dashboard”.
- Copy the dashboard ID and import it in Grafana.
- Now you can see the graph on Grafana.
## Part 4: Monitoring Jenkins and System Metrics
Install **Prometheus Metrics plugin **in Jenkins.

**1. Install Node Exporter (For System level metrics)**
Download and install Node Exporter on your Jenkins server:

`wget https://github.com/prometheus/node_exporter/releases/download/v1.8.2/node_exporter-1.8.2.linux-amd64.tar.gz`
tar -xvf node_exporter-1.8.2.linux-amd64.tar.gz
rm -rf node_exporter-1.8.2.linux-amd64.tar.gz
cd node_exporter-1.8.2.linux-amd64/
./node_exporter &
Node Exporter runs on port `9100`
. Access it at `http://<your-public-ip>:9100/`
.

**2. Configure Prometheus for Node Exporter and Jenkins**
Edit your `prometheus.yml`
file to include the configurations for Node Exporter and Jenkins:

`scrape_configs:`
- job_name: 'node_exporter'
static_configs:
- targets: ['<jenkins-ip>:9100']
- job_name: 'jenkins'
metrics_path: '/prometheus'
static_configs:
- targets: ['<jenkins-ip>:8080']
Restart Prometheus:

`pkill prometheus`
./prometheus &
**3. Add Node Exporter Data Source and Import Dashboard in Grafana**
- Add Node Exporter as a data source in Grafana.
- Search for “node exporter grafana dashboard”.
- Copy the dashboard ID and import it in Grafana.
Final result:

# Conclusion
With this setup, you now have a robust monitoring system using Prometheus, Grafana, and Blackbox Exporter. You can monitor your applications, websites, and system metrics effectively. Happy monitoring!

**Links to Downloads:**