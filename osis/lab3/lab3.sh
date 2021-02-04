# !/bin/bash

declare -a lines

while IFS= read -r line
do
    lines+=("$line")
done < $1

count_lines=$((${#lines[*]}-1))

table_name=${lines[0]}
fields_name=${lines[1]}

counter=2
while [ $counter -le $count_lines ]
do
echo "insert into $table_name ($fields_name) values (${lines[$counter]});"
((counter++))
done
