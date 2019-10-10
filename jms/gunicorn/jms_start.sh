#!/bin/bash

NAME="jms" # 应用的名字，这里填上Django project下面的app名字
DJANGODIR=/home/jms/ # Django project 路径
SOCKFILE=/home/jms/gunicorn/jms.sock # 使用这个文件进行unix socket通信
# USER=hello # 运行的用户，我们这里使用的是root用户所以不需要
# GROUP=webapps # 运行的用户组
NUM_WORKERS=3 # Gunicorn 可以产生的工作进程数量
DJANGO_SETTINGS_MODULE=jms.settings # Django project使用的settings
DJANGO_WSGI_MODULE=jms.wsgi # WSGI模块，默认与settings.py文件同目录

echo "Starting $NAME as `whoami`"

# 启用虚拟环境
#cd $DJANGODIR # cd到Django project目录
#source trydjango110_env/bin/activate # 启用
#export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
#export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Start your Django gunicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /root/anaconda3/envs/jms/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--bind=unix:$SOCKFILE \
--log-level=debug \
--log-file=- &
