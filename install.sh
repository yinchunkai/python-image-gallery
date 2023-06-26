#!/usr/bin/bash

# Install packages
yum -y update
yum install -y nano tree python3
sudo dnf install python3-pip
yum install -y git
sudo yum install -y postgresql
dnf install java-11-openjdk
sudo yum install -y gcc
sudo yum install -y python3-devel
sudo yum install -y postgresql-devel
pip3 install --user psycopg2

# config/install custom software
cd /home/ec2-user
git clone https://github.com/cdavidshaffer/python-image-gallery.git
chown -R ec2-user:ec2-user python-image-gallery

# start/enable services
systemctl stop postfix
systemctl disable postfix
~                              
