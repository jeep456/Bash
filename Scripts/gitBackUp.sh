#!/usr/bin/env bash

dateNow=`date +%Y-%m-%d`;
time=`date +%H:%M:%S`;
hour=`date +%H`;

countDate=`cat $HOME/Bash/Scripts/count.txt`

echo $countDate;
echo $hour;

needProject(){

    cd  $1;
    git add . ;
    git commit -m "Бэкап от $dateNow ($time)";
    git push origin $2;

}
/home/jeen/Bash/Scripts/gitBackUp.sh

if [ $dateNow \> $countDate ];
then

    echo "Делаем бэкап";
    echo $dateNow > $HOME/Bash/Scripts/count.txt;
    needProject "$HOME/Bash" 'master';
    needProject "$HOME/sites/films" 'master';
    needProject "$HOME/sites/jeep.github.io" 'gh-pages';
#    needProject "$HOME/sites/lars" 'master';

fi



