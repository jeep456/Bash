#!/usr/bin/env bash

cntFolder=`ls "/home/jeen/Bash/tmp/3H/" | wc -l`;

min10=`ls "/home/jeen/Bash/tmp/10M/" | wc -l`;

day=`date +%d`;
hour=`date +%H`;
min=`date +%M`;

if [ $(($hour%3)) -eq 0 ];
then

#    if [ $cntFolder -gt 0 -a $min -lt 10 ];
    if [ $(($min%10)) -eq 0 -a $min -lt 6 ];
    then
        rm -fr "/home/jeen/Bash/tmp/3H/"*;
    fi

else
    echo "Nothing to doing";
fi


if [ $(($min%10)) -eq 0  ];
then

    if [ $min -gt 0 ];
    then
        rm -rf "/home/jeen/Bash/tmp/10M/"*;
    fi

fi

