#!/bin/bash

if [ ${#1} -gt 0 -a ${#2} -gt 0 ];
then

    columns=$(mysql -uroot -p123 -e "SELECT column_name FROM information_schema.columns WHERE table_schema = '$1' AND table_name = '$2';");
    echo $columns | sed 's/ /\n/g' > /home/jeen/Bash/Scripts/columns.txt;
    sed -i '1d' /home/jeen/Bash/Scripts/columns.txt;

    checkXclip=`which xclip`;
    checkXclip=`echo -n "$checkXclip" | wc -c`

    if [ $checkXclip -gt 0 ];
    then
        cat /home/jeen/Bash/Scripts/columns.txt | xclip -sel clip;
        echo "Названия колонок \`$1\`.\`$2\` скопированы в буффер обмена";
        rm /home/jeen/Bash/Scripts/columns.txt;
    fi

elif [ ${#1} -gt 0 -a ${#2} -eq 0 ];
then

    echo "Не хватает названия таблицы"

elif [ ${#1} -eq 0 -a ${#2} -gt 0 ];
then

    echo "Не хватает названия БД"

else

    echo "Введите имя БД и имя Таблицы для выборки колонок";

fi
