#! /usr/bin/bash

cd ~

cd /etc/yum.repos.d

cat > testrepo.repo << EOF
[dvd1]
baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream
gpgcheck=0

[dvd2]
baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS
gpgcheck=0

EOF


