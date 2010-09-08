#!/bin/bash

DEV=$1
OPTION=$2 # (add | remove)
LABEL=$3
PID=/var/run/tracd.pid
#MOUNT_POINT=`mount | grep /dev/${DEV} | cut -d ' ' -f 3`
#MOUNT_POINT=`cat /proc/mounts | grep /dev/${DEV} | cut -d ' ' -f 2`
USERNAME=humitos
LABEL=humitos
#MOUNT_POINT=/media/${USERNAME}
#MOUNT_POINT=/auto/humitos
MOUNT_POINT=/home/humitos/trachumitos

get_mount_point(){
    #LABEL=`vol_id /dev/${DEV} | grep "ID_FS_LABEL=" | sed -e "s/ID_FS_LABEL=//g"`

    if [ -z  "$MOUNTPOINT" ]; then
        MOUNT_POINT=/media/${LABEL}
        mkdir -p ${MOUNT_POINT}
        /bin/umount /dev/${DEV}
        /bin/mount /dev/${DEV} ${MOUNT_POINT}
    fi
}

add(){
    #get_mount_point
    backup_trac
    up_trac
}

remove(){
    kill_trac
}

up_trac(){
    tracd --single \
        -p 9000 \
        --basic-auth=trac,${MOUNT_POINT}/htpasswd,trac\
        --pidfile=${PID} \
        ${MOUNT_POINT}
}

kill_trac(){
    /bin/kill `cat ${PID}`
}

backup_trac(){
    DESTINO=/home/${USERNAME}/backup-trac/`date +%0d-%0m-%0y_%0k-%0M-%0S`
    /usr/bin/trac-admin ${MOUNT_POINT} hotcopy $DESTINO
}

# Run 'add' or 'remove' option
#${OPTION}
add

