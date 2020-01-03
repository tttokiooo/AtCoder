#!/bin/bash

base_url='https://atcoder.jp/contests'
target=('ABCxxx')

for contest_key in ${target[@]}
do
    if [ -d ${contest_key} ];then
        echo "${contest_key} is already exists"
        continue
    fi

    mkdir ${contest_key}
    lower_conest=$(echo ${contest_key} | tr '[A-Z]' '[a-z]')
    for que in {a..d}
    do
        echo "# ${base_url}/${lower_conest}/tasks/${lower_conest}_${que}" > ${contest_key}/${que}.py
    done
done