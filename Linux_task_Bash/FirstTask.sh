#!/bin/bash

#Checking the input arguments. If none - exit with info message.
if [[ $# -eq 0 ]]
then
	echo "Please execute the script with input file. Type \"./FirstTask.sh help\" to see the instructions. "
	exit
elif [[ $1 = "help" ]]
then
	echo "Please enter the command ./FirstTask.sh _file_name_ to execute the script."
	exit	
fi


myfile=$1
IFS=$'\n'
row_count=1


#Checking the existing directory for host files. If exists - remove and create from scratch.
if [ -d host_vars ]
then
	rm -r host_vars
fi
mkdir host_vars


#Creating/re-writing the Hosts file with initial row [all]
echo "[all]" >  hosts


for row in $(cat $myfile)
do
	if [ $row_count -gt 1 ]
	then
          host_name=$(echo "$row" | sed 's/|//g' | awk '{print$1}')
	  host_ip=$(echo "$row" | sed 's/|//g' | awk '{print$2}')
	 
	  echo "ansible_host: $host_ip" > host_vars/$host_name
	  echo "$host_name" >> hosts
	  
 	fi
        
	row_count=$[$row_count+1]
done

