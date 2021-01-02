# Original script written by Mike Ivanov - https://github.com/mikonoid/python-cisco-backup
# Fork by Stefano Giraldo - https://github.com/ste-giraldo

# router_config_v0.3.py
Script for configuring routers and switches. Hosts list and commands are taken from external files. It also use static (in script) or prompted authentication.
Tested on python 2.7 with paramiko lib.
Works on Cisco and Huawei boxes.

To avoid error "CryptographyDeprecationWarning" during SSH against Huawei devices use python-paramiko >= 2.5
For Debian users: python-paramiko_2.6.0-1~bpo10+1_all.deb works fine.
