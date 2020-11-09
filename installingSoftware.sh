#! /usr/bin/bash

tput setaf 2
echo "enter the name of the package u want to install"
echo "" 
echo ""
echo ""
 
read package

yum install ${package}
tput setaf 7
