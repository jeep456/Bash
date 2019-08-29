#!/usr/bin/env bash

cntSearch=`find $HOME/Downloads/ -type f -iname '*.torrent' | wc -l`;

if [ $cntSearch -gt 0 ];
then

    /usr/bin/transmission-gtk;

fi
