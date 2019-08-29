dateC=`date +%Y-%m-%d`;
dateF=`cat $HOME/termux/date.txt`;

hour=`date +%H`;

#echo $dateC;
#echo $dateF;
#echo $hour;

gitFunc(){
 cd $HOME/termux;
 git add .;
 git commit -m "Автобэкап $dateC";
 git push origin master;
}

tossh(){
 scp $HOME/termux/nuznoe.txt jeen@192.168.0.103:Bash/termux/
}

if [[ $dateC > $dateF && $hour > 21 ]];
then
 #echo "good";
 echo $dateC > $HOME/termux/date.txt;
 gitFunc;
 tossh;
else
 echo "bad"
 tp=`date +"%Y-%m-%d %H:%M:%S"`;
 echo "Комитить пока рано $tp" >> $HOME/termux/gitlog;
fi

gitlogS=`cat $HOME/termux/gitlog | wc -l`;
gitlogS=$((gitlogS*1));

echo $gitlogS;

if [ $gitlogS -gt 170  ];
then
  rm $HOME/termux/gitlog;
fi
