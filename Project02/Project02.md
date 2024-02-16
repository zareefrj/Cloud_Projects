## Project02: Resource Management - HTCondor Cluster on EC2
This project involved setting up an HTCondor cluster across multiple EC2 instances and submitting scheduled jobs to the cluster.
The HTCondor Architecture Diagram is attached in this project folder.

**Steps:**

1. **Install Condor Manager:**
    * Execute the following command on the manager node, replacing `<ip_address>` with the actual IP:
        ```bash
        curl -fsSL https://get.htcondor.org | sudo /bin/bash -s -- --no-dry-run --password "nopassword" --execute "<ip_address>"
        ```
    * Replace `"nopassword"` with a secure password if desired.
    * Restart Condor: `sudo systemctl restart condor`
    * Verify status: `sudo systemctl status condor`

2. **Repeat for Submit and Execute Hosts:**
    * Follow steps 1.a-c on additional nodes designated as submit and execute hosts.

3. **Verify Installation:**
    * Run `condor_status` on any machine. Two workers should be listed.

4. **Submit First Job:**
    * Refer to the HTCondor quick start guide for user job submission: [https://htcondor.readthedocs.io/en/latest/users-manual/quick-start-guide.html](https://htcondor.readthedocs.io/en/latest/users-manual/quick-start-guide.html)
