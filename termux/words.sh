#!/usr/bin/env bash

part(){
 cd /home/jeen/Bash/termux/;
 param=$(($1-1));
 start=$(($param*20));
 end=$(($start+20));
 if [ $param -eq 0 -o $param -lt 0 ];
 then
     start=1;
     end=20;
 fi

 cat 1000words2.txt | sed -n "$start,${end}p";
}

if [ ! -z $1 ];
then
    part $1
else
    echo "Введите параметр";
fi
