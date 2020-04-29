#!/bin/sh
SCRIPT_DIR=$(cd $(dirname $0); pwd)
gtimeout 5 python3 $1 < ${SCRIPT_DIR}/../input.txt
STATUS=$?
if [ "${STATUS}" -eq 124 ];then
    echo "\ntimeout!!"
fi
