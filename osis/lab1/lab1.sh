#!/bin/bash

echo "Statistics of the current session:" 
echo "username:"  $USER 
echo "time:" `date +%X` 
echo "date:" `date +%D` 
echo "current directory:" `pwd` 

num_processes=`ps -A | wc -l`
num_processes=$((num_processes - 1))
echo "number of processes in the system:" $num_processes 

uptime_result=`uptime`
IFS=" " read -a a <<< $uptime_result
time=${a[2]}
echo "work time:" ${time/,/ } 
