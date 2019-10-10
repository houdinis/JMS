#!/bin/bash

trap '' SIGINT
base_dir=$(dirname $0)
export LANG='en_US.UTF-8'
/root/anaconda3/envs/jms/bin/python $base_dir/connect.py

exit
