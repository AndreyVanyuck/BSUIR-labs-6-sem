# !/bin/bash

num=37

random_number() {
    num=$((num * 87 % 123));
}

while true
    do
    random_number
    x=$num
    random_number
    y=$num
    clear
    tput cup $x $y
    echo $(date  +%H:%M)
    sleep 1
done

