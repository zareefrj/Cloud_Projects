## Project05: Building a Distributed File System - Apache Hadoop on EC2

This project focused on configuring an Apache Hadoop Distributed File System (HDFS) across an EC2 cluster.

**Objective:**

* Implement a scalable and reliable HDFS for distributed data storage and processing.
* Leverage the power of EC2 instances to build a robust Hadoop environment.

**Implementation:**

* This project followed the comprehensive hands-on tutorial: [https://sparkbyexamples.com/hadoop/apache-hadoop-installation/](https://sparkbyexamples.com/hadoop/apache-hadoop-installation/)

**Key Steps:**

* **Node Setup:**
    * Launched multiple EC2 instances following the tutorial guidelines.
    * Configured networking and security groups for cluster communication.

* **Hadoop Installation:**
    * Downloaded and installed Hadoop on each node according to the tutorial steps.
    * Configured HDFS master and data node roles on respective instances.

* **Cluster Configuration:**
    * Edited configuration files (`hdfs-site.xml`, `core-site.xml`) for cluster communication and data storage.
    * Ensured proper permissions and ownership for HDFS directories.

* **Verification:**
    * Started the HDFS master and data nodes on all instances.
    * Verified cluster health and data access using Hadoop commands.
