
mins=`date +%M`

#if [ $((mins%15)) -eq 0 ];
if [ 1 -eq 1 ];
then
 
 fileFirst="$EXTERNAL_STORAGE/ADM/backup.txt";

 if [ -f $fileFirst ];
 then
 
  fileSecond="nuznoe.txt"

  if [ ! -f $fileSecond ];
  then
    cp $fileFirst "$HOME/termux/$fileSecond";
  fi

  cntLnFile1=`cat $EXTERNAL_STORAGE/ADM/backup.txt | wc -l`;
  cntLnFile2=`cat $HOME/termux/nuznoe.txt | wc -l`;

  check=`curl -Is http://jeep-rap.ru | head -1`;

  if [ $cntLnFile1 -ne $cntLnFile2 ];
  then
    echo "больше однако" >> $HOME/termux/bolshe.txt;
  fi

  if [ $cntLnFile1 -ne $cntLnFile2 -a ${#check} -gt 0 ];
  then
      echo "Копируем файл" >> $HOME/termux/bolshe2.txt;
      cp $fileFirst "$HOME/termux/$fileSecond";
      scp "$HOME/termux/$fileSecond" jeen@192.168.0.103:~/Bash/termux/backUp.txt

  fi

 else

  echo "Файл для бэкапа отсутствует";

 fi

fi
