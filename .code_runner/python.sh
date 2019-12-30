#!/bin/sh
SCRIPT_DIR=$(cd $(dirname $0); pwd)
python3 $1 < ${SCRIPT_DIR}/input.txt