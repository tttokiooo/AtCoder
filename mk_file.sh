#!/bin/bash

base_url='https://atcoder.jp/contests'
if [ ${@} ];then
    target=${@}
else
    target=$(find . -name 'ABC[0-9]*' | sort -r | head -n 1)
    target=ABC$((${target#*ABC}+1))
    echo ${target}
fi

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
        cat template.py >> ${contest_key}/${que}.py
    done
done