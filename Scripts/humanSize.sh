#!/usr/bin/env bash

size (){
    echo $(($1+1));
}

if [ ! -z $1 ];
then
    size $1;
else

    echo "Ожидается параметр";

fi
