#!/usr/bin/env bash

timestamp=`date +"%Y-%m-%d %H:%M:%S"`;

folder="$HOME/Bash/";

if [ ! -f "$folder/NeedLists/aliases.txt" ];
then
    cd  $HOME/Bash/NeedLists/;
    cat $HOME/.bashrc | grep '^alias' | cut -f2- -d \ | sort | sed 's,^,alias ,' > aliases.txt;
fi

file1=`cat $HOME/.bashrc | grep '^alias' | cut -f2 -d \ | sort | sed 's,^,alias ,' | wc -l`
file2=`cat $folder/NeedLists/aliases.txt | wc -l`

if [ $file1 -ne $file2 ];
then
    rm $folder/NeedLists/aliases.txt;
    cd  $HOME/Bash/NeedLists/;
    cat $HOME/.bashrc | grep '^alias' | cut -f2 -d \ | sort | sed 's,^,alias ,' > aliases.txt;
fi

gitBacks(){
   cd $HOME/Bash/;
   git add .;
   git commit -m "BackUp $timestamp";
   git push origin master;
}

status=`git st`;
str="На ветке master нечего коммитить, нет изменений в рабочем каталоге";
status=${#status};
str=${#str};

if [ $status -ne $str ];
then
    echo "Делаем коммит";
    gitBacks
else
    echo "Ничего не делаем";
fi

echo $status;
#echo ${#check}
echo $timestamp;
