#! /usr/bin/bash

tput setaf 6
yum install -y httpd

tput setaf 2
echo "do you have any webpage code or want to create some??[y/n]"

read request
if [[ request=='y' ]]
then
	cd /var/www/html
	touch webpage.html
else 
	echo "starting the webserver services"
fi

tput setaf 6
systemctl start httpd

tput setaf 2
echo "the webserver services started but is not enabled"

tput setaf 7
