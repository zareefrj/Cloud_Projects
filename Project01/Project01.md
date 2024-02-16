## Project 01: Dive into the Cloud

This project involved launching an EC2 instance running Ubuntu and configuring an Apache2 web server.

**Steps:**

1. **Launching an AWS instance:**
    * Choose an appropriate Ubuntu image and instance type for your needs.
    * Configure security groups and network settings.
    * Launch the instance.

2. **Connecting to the instance:**
    * Use PuTTY, terminal, or AWS console to connect to the instance.
    * Ensure you have the correct credentials and security group rules in place.

3. **Updating APT repository:**
    ```bash
    sudo apt-get update
    ```

4. **Installing Apache2 web server:**
    ```bash
    sudo apt install apache2
    ```

5. **Checking Apache2 status:**
    ```bash
    sudo systemctl status apache2.service
    ```

6. **Modifying the web page:**
    * Identify the desired location for the "My name is ..." text within the HTML code.
    * Edit the `/var/www/html/index.html` file using a text editor like nano.
    * Make your changes and save the file (Ctrl + O in nano).
    * Exit the editor (Ctrl + X in nano).

7. **Restarting Apache2:**
    ```bash
    sudo systemctl restart apache2
    ```
You can refer to the png image attached in this folder as visual aid for the end results.
