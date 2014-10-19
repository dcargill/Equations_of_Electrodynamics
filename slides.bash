#!/bin/bash
#####################

#####################

#DESKTOP="/home/dcargill/Desktop"


if [ -z "$1" ]
then
  echo "No input file"
  echo "Help: $0 -h"
  exit
else
    case $1 in
#         $IPADDRESS)
#            echo "That's your ip stupid! You can't mount that."
#            exit;;
        -h) echo "ipython nbconvert INPUTFILE.ipynb --to slides --post serve"
#            echo "ex: 192.168.2.2"
            exit;;
         *)
            INPUTFILE=$1
    esac
    
fi
ipython nbconvert $INPUTFILE.ipynb --to slides

#MOUNT_POINT="/mnt/"$INPUT
#MOUNT_DESTINATION=$INPUT":/home"

#sudo mount $MOUNT_DESTINATION $MOUNT_POINT
#ln -s $MOUNT_POINT $DESKTOP  


