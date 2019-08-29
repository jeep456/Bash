#!/bin/bash

# Заводим переменную date и записываем в неё текущую дату и день недели
date=$(date +"%X %d.%m.%Y (%A)");

# Заводим переменную и записываем в неё текущую минуту часа
minutes=$(date +%M);
hour=$(date +%H);

#chmod -R 777 /home/jeen/Bash/mysql/*.txt;

if [ $((minutes%4)) -eq 0 -a $minutes -lt 5 ];
#if [ 1 -eq 1 ];
#if [ $((minutes%5)) -eq 0 ];
then

    if [ -f ~/Bash/BackUp/allBases.tbz ];
    then
        rm ~/Bash/BackUp/allBases.tbz;
    fi

    #####mkdir $HOME/.Back $HOME/.Back/mysql

#    array=$(mysql -uroot -p123 -e "SHOW DATABASES;" | sed 's/mysql//g; s/films//g; s/lars//g; s/information_schema//g; s/sys//g; s/Database//g; s/performance_schema//g' | sed '/^\s*$/d' | sort);
    array=$(mysql -uroot -p123 -e "SHOW DATABASES;" | sed 's/mysql//g; s/information_schema//g; s/sys//g; s/Database//g; s/performance_schema//g' | sed '/^\s*$/d' | sort);

    for i in $array;
        do mysqldump -uroot -p123 $i > $HOME/Bash/BackUp/mysql/$i.sql;
    done;

    cd ~/Bash/BackUp/

    tar -cjf allBases.tbz mysql/*.sql

    cp allBases.tbz /media/jeen/Transcend/BackUp_jeen/

    sleep 2

    ########    Копируем скрипты наутилуса              ##############
    cp -r /home/jeen/.local/share/nautilus/scripts/* /home/jeen/Bash/BackUp/another/nautilusScripts/

    cp /media/jeen/Transcend/web/OpenServer/settings.jar ~/Bash/BackUp/another/phpstorm/

    cp $HOME/.bashrc ~/Bash/BackUp/another/bashrc/

    strings ~/'.config/chromium/Default/Current Session' | 'grep' -E '^https?://' | sort -u > another/chrome_sessions/chrome_session.txt



    tar -cjf another.tbz another/

    cp another.tbz /media/jeen/Transcend/BackUp_jeen/


#    chmod -R 777 /home/jeen/Bash/mysql/*.sql;

#    sleep 3

#################    crontab -l > $HOME/.Back/crontabUser.txt

#################    rar a $HOME/.Back/nautilusScripts.rar $HOME/.local/share/nautilus/scripts/*;

#################    cp $HOME/.bashrc $HOME/.Back/bashrc.txt

#    rar a $HOME/.Back/Bash.rar $HOME/Bash/*;

#    rar a $HOME/.Back/sites/sites.rar $HOME/sites/*;

    sleep 3

#    rar a $HOME/Bash/BackUp.rar $HOME/.Back/*;

#    rm -rf $HOME/.Back/

#    rm $HOME/Bash/crontab_and_other/crontabUser.txt

#    rm -rf $HOME/.Back

    if [ $((hour%4)) -eq 0 ];
    then

#        /usr/bin/mysqldump --all-databases --result-file=/home/jeen/Bash/mysql/allDB.sql -uroot -p123

#        rar a /home/jeen/Bash/mysql/arhivesDB.rar /home/jeen/Bash/mysql/*.sql /home/jeen/Bash/mysql/*.sh /home/jeen/Bash/crontab_and_other/* ;

#	chmod -R 777 /home/jeen/Bash/mysql/arhivesDB.rar;

        echo "Дамп всех баз данных из сервера MYSQL $date" | mutt -s "Дамп баз данных $date" konstnitin.yolkin@yandex.ru -a $HOME/Bash/BackUp/allBases.tbz -a $HOME/Bash/BackUp/another.tbz;

        sleep 3

#        rm $HOME/Bash/crontab_and_other/crontabUser.txt $HOME/Bash/crontab_and_other/nautilusScriptsAndMysqlDB.rar

    fi
elif [ $((minutes%6)) -eq 0 -a $minutes -lt 59 ];
#elif [ 2 -eq 3 ];
then

 sleep 2
    ###########rm $HOME/Bash/BackUp.rar
#   rm /home/jeen/Bash/mysql/arhivesDB.rar;
#   rm /home/jeen/Bash/mysql/*.txt;
#   rm /home/jeen/Bash/mysql/*.sql;

fi
