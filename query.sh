#!/bin/bash
sitelist='/usr/local/bin/sitelist.txt'
keyword=$1
egrep -i -e $1 $sitelist | sort
hit=$(egrep -i -e $keyword $sitelist | sort)
IFS=$'\n' lines=($hit)
for line in ${lines[@]}
do
    trt_id=$(echo $line | awk ' BEGIN{FS=","} { print $3 }')
    case $2 in
    open )
        # Open URL in default browser
        open "https://wesbite.com/locations/${trt_id}/it"
        ;;
    * )
    ;;
  esac
done
