#! /bin/bash

finds=`find ~/Downloads/ -iname 'container*'`

if [ ${#finds} -ne 0 ];
then
 rm ~/Downloads/container*
fi
