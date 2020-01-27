#!/bin/sh
SCRIPT_DIR=$(cd $(dirname $0); pwd)
gtimeout 10 python3 $1 < ${SCRIPT_DIR}/input.txt