#!/usr/bin/env bash


mans(){
    man $1 > "/home/jeen/Bash/tmp/10M/$1.txt";
    cat "/home/jeen/Bash/tmp/10M/$1.txt" | xclip -sel clip;
    gedit "/home/jeen/Bash/tmp/10M/$1.txt";
}

mans $1
