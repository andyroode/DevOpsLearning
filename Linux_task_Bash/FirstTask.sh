#!/bin/bash

myfile=$1
IFS=$'\n'
row_count=1

trash_path=/dev/null
mkdir host_vars 2>> $trash_path
touch hosts

for row in $(cat $myfile)
do
	if [ $row_count -gt 1 ]
	then
          host_name=$(echo "$row" | sed 's/|//g' | awk '{print$1}')
	  host_ip=$(echo "$row" | sed 's/|//g' | awk '{print$2}')
	 
	  echo "$host_ip" > host_vars/$host_name
	  if grep $host_ip hosts >> $trash_path
          then
	  	echo "Do nothing" >> $trash_path
          else	  
	  	echo "$host_ip" >> hosts
	  fi
 
	fi
        row_count=$[$row_count+1]
done

