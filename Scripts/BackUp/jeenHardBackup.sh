#!/usr/bin/env bash

# 7 18 * * * cd /media/jeen/Transcend/BackUp_jeen/ && tar -cjf jeenHardBackUp.tbz /home/jeen/*

cd /media/jeen/Transcend/BackUp_jeen/;

if [ -f jeenHardBackUp.tbz ];
then
    rm jeenHardBackUp.tbz;
fi

tar -cjf jeenHardBackUp.tbz /home/jeen/*

good=`echo $?`;

if [ $good -eq 0 ];
then
    notify-send -i emblem-default "Пользовательские данные успешно сохранены";
else
    notify-send -i software-update-urgent "Домашний каталог НЕ сохранён.";
fi

