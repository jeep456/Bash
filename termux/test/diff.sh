

file1="$EXTERNAL_STORAGE/ADM/backup.txt";
file2="$HOME/termux/nuznoe.txt";

df1=`cat $file1 | wc -l`;
df2=`cat $file2 | wc -l`;

if [ $df1 -gt $df2 ];
then
 echo "файл больше";
elif [ $df1 -lt $df2 ];
then
 echo "файл меньше";
elif [ $df1 -eq $df2 ];
then
 echo "файлы равны";
fi

