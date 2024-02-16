## Project03: Distributed File System - NFS on Ubuntu EC2

This project explores setting up a Network File System (NFS) for directory and file sharing across client and server EC2 instances running on Ubuntu.

[NFS Configuration Documentation](https://ubuntu.com/server/docs/service-nfs)

**Server**
```bash
sudo apt install nfs-kernel-server
sudo systemctl start nfs-kernel-server.service
mkdir storage
sudo systemctl restart nfs-kernel-server.service
cd storage/
ls -l
pwd
sudo nano /etc/exports
ls
touch File01
ls
sudo nano /etc/exports
sudo exportfs -a
ls -l
ls
echo "I made it" > File02
```

**Client**
```bash
sudo apt install nfs-common
mkdir data
cd data/
pwd
cd
sudo systemctl start nfs-kernel-server.service
sudo mount 172.31.36.82:/home/ubuntu/storage /home/ubuntu/data
cd data/
ls -l
ls
cat File02
```
