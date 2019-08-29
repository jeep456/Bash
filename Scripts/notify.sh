#!/usr/bin/env bash

e='Wellcome'

export DISPLAY=:0 && /usr/bin/notify-send $e;

date=`date +%H:%M:%S`

#echo $date;
