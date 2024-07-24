# How To Run Databases in Kubernetes
![Featued image for: How To Run Databases in Kubernetes](https://cdn.thenewstack.io/media/2024/07/86fab00b-cloud-7832677_1280-1024x512.jpg)
The debate about where databases should run in [Kubernetes](https://thenewstack.io/kubernetes/) has been a hot topic in the tech community. The prevailing argument is about “[building stateless applications](https://thenewstack.io/how-to-better-manage-stateful-applications-in-kubernetes/),” suggesting that databases are best suited as managed services with cloud providers. However, there are practical design patterns for successfully running databases in Kubernetes.

On most cloud providers, volumes are constrained to a single [Availability Zone](https://thenewstack.io/use-multi-availability-zone-kubernetes-for-disaster-recovery/) (AZ), which means the databases are also constrained to that AZ by design. Most production clusters are likely regional or multi-AZ, especially for stateless applications. Using node selectors to ensure the database pods are located in the AZs where their volumes can be mounted is important.

Example:

12 |
nodeSelector: topology.kubernetes.io/zone: europe-west6-b |
This configuration specifies that the database pod should run in the ‘*europe-west6-b*’ AZ.
**Plan Resource Usage**
Since our databases are constrained to one AZ, we must carefully plan our node-to-AZ design to avoid scheduling errors and unavailability issues. One effective strategy is to run separate node groups or node pools specifically for database workloads. This ensures that sufficient resources are always available in the required AZ.

Example:

- Create a dedicated node pool for database workloads.
- Use taints and tolerations to ensure only database pods are scheduled on these nodes.
123456789101112131415 |
# Taint nodes to be dedicated to databasesspec: taints: - key: "dedicated" value: "database" effect: "NoSchedule"# Toleration in the DB pod specspec: tolerations: - key: "dedicated" operator: "Equal" value: "database" effect: "NoSchedule" |
**High Availability**
Managed database services often provide built-in high availability and failover capabilities. To achieve similar resilience in Kubernetes, meticulous planning for recovery and availability strategies is essential. Here are two approaches:

**Using Kubernetes Operators:**
Kubernetes operators like the Zalando Postgres Operator offer advanced features like read replicas and automatic failovers, similar to managed database services. These operators can significantly simplify the setup and management of high availability for your databases.

The Zalando Postgres Operator allows you to specify the number of read replicas and automatically manages failovers. This operator provides a UI where you can configure these settings, making it an intuitive and powerful tool for managing database high availability in Kubernetes. Here is a [list](https://operatorhub.io/?category=Database) of some other Operators, some of which are managed by their respective communities

**Self-Service Approach:**
For those who prefer a more hands-on approach, particularly for NoSQL databases, here’s a step-by-step method:

**Mount Data Volumes on Both Pods:**Ensure that the data volume is accessible by both the primary and secondary pods.**Pod Affinity:**Use pod affinity rules to ensure that the primary and secondary pods are placed together, respecting volume constraints.**Init Container:**At startup, use an init container in the secondary pod to copy all data from the primary pod.**Volume Mount Constraint:**Set the volume mount on the secondary pod to read-only to prevent data corruption.**Use cronjob for restarts**: Create a simple CronJob that deletes the old pod every six hours, allowing the init container to run and copy new data.
**Example Configurations**
The example below shows how to set up a Neo4j read replica using pod affinity, an init container for data copying, and mount volumes with read-only constraints to ensure data integrity.

123456789101112131415161718192021222324252627282930313233343536 |
affinity: podAffinity: requiredDuringSchedulingIgnoredDuringExecution: - labelSelector: matchExpressions: - key: app operator: In values: - primary-db topologyKey: "kubernetes.io/hostname"initContainers: - name: copy-data image: busybox command: ["sh", "-c", "cp -r /data/* /backup/"] volumeMounts: - name: data-volume mountPath: /data - name: backup-volume mountPath: /backupvolumes: - name: data-volume persistentVolumeClaim: claimName: primary-db-pvc - name: backup-volume persistentVolumeClaim: claimName: secondary-db-pvccontainers: - name: secondary-db image: neo4j:latest volumeMounts: - name: backup-volume mountPath: /data readOnly: true |
**Backups and Restore**
Many service providers offer ways to schedule recurring snapshots on disk-based volumes. This is often the preferred method because it is easier to set up, and the recovery process is faster. We can back up the volumes hosting the DB data regularly in this scenario.

Another approach involves combining the database’s proprietary tools, such as pg_dump for PostgreSQL.

Here is an example Configuration for PostgreSQL using Kubernetes Cron Jobs to backup to s3

123456789101112131415161718192021 |
apiVersion: batch/v1beta1kind: CronJobmetadata: name: postgres-backupspec: schedule: "0 0 * * *" jobTemplate: spec: template: spec: containers: - name: backup image: postgres command: ["sh", "-c", "pg_dumpall -c -U $PGUSER | gzip > /backup/db_backup.gz && aws s3 cp /backup/db_backup.gz s3://your-bucket/db-backup-$(date +\%F).gz"] volumeMounts: - name: backup-volume mountPath: /backup restartPolicy: OnFailure volumes: - name: backup-volume emptyDir: {} |
**Summary**
Even though the initial setup or learning curve might be steep, running your database in Kubernetes provides plenty of advantages. One not-so-talked-about benefit is cost. Running a db.m4.2xlarge (4vCPUs, 32GB RAM) instance in RDS costs approximately $1200/month, while running a similarly sized EC2 instance costs around $150/month. A node in Kubernetes will likely also run more than one pod, further optimizing resource use.

Vendor agnosticism is another key motivation for many people running databases in Kubernetes. Moving your workloads across any platform with minimal tweaks is incredibly appealing.

In conclusion, consider the pros and cons before deciding where to run your production database. Many people successfully run their databases in Kubernetes, and the number of such deployments is growing daily.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)