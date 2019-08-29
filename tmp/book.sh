#!/usr/bin/env bash

cd $HOME/Bash/tmp/;
book=`cat book.txt`;

words=`echo $book | wc -m`

if [ $words -gt 1 ];
then
    author=`echo $book | sed "s, - .*,,"`
    genre=`echo $book | sed -e "s,^.*\s,,g"`;
    genre=`echo ${genre:1:-1}`;
    book=`echo $book | sed -e "s,$author - ,," | sed "s, (\(.*\)),,"`;

    echo "{\"author\":\"$author\",\"book\":\"$book\",\"genre\":\"$genre\"}" > book.json;

    ping -c1 jeep-rap.ru > /dev/null 2>&1;
    rez=`echo $?`

    if [ $rez -eq 0 ];
    then
        echo "Делаем отправку";
        scp jeen@192.168.0.103:sites/lars/public/books/ book.json
        copys=`echo $?`

        if [ $copys -eq 0 ];
        then
#            rm book.json;
            cat book.json;
            echo "" > book.txt;
        fi

    else
        echo "Не делаем чего то";
    fi

fi
