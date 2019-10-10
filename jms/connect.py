#!/root/anaconda3/envs/jms/bin/python
# coding: utf-8
import pwd
import sys
import getpass
import os
import django
import textwrap
import re
import paramiko
import socket
import datetime
import termios
import tty
import select

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, 'logs')

# 设置django环境变量
os.environ['DJANGO_SETTINGS_MODULE'] = 'jms.settings'
django.setup()

from assets.models import Assets
from perm.perm_api import get_user_asset




# 获取当前登陆用户名
user_login = getpass.getuser()

def color_print(msg, color='red', exit=False):
    """
    Print colorful string.
    颜色打印字符或者退出
    """
    color_msg = {'blue': '\033[1;36m{0}\033[0m',
                 'green': '\033[1;32m{0}\033[0m',
                 'yellow': '\033[1;33m{0}\033[0m',
                 'red': '\033[1;31m{0}\033[0m',
                 'title': '\033[30;42m{0}\033[0m',
                 'info': '\033[32m{0}\033[0m'}
    msg = color_msg.get(color, 'red').format(msg)
    print(msg)
    if exit:
        time.sleep(2)
        sys.exit()
    return msg

class TTY:
    def __init__(self, host='127.0.0.1', port=22, username='root', password=''):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.ssh = None
        self.chan = None
        self.__get_chan()

    def __get_chan(self):
        """
        使用paramiko模块与后端ssh建立channel
        paramiko的channel其实是与后面ssh server建立了一个tcp长连接,输入都会发送到后面的主机上
        :return: None
        """
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(self.host,
                        port=self.port,
                        username=self.username,
                        password=self.password)
        except (paramiko.ssh_exception.AuthenticationException, paramiko.ssh_exception.SSHException):
            color_print('连接服务器失败', exit=True)
        self.ssh = ssh
        self.chan = ssh.invoke_shell(term='xterm') # TODO

    def __get_log_f(self):
        now = datetime.datetime.now()
        date_today = now.strftime('%Y%m%d')
        time_now = now.strftime('%H%M%S')
        log_today_dir = os.path.join(LOG_DIR, date_today)
        log_filename = os.path.join(log_today_dir, '{host}-{port}-{username}-{date}{time}.log'.format(
            host=self.host, port=self.port, username=self.username, date=date_today, time=time_now,
        ))
        if not os.path.isdir(log_today_dir):
            os.mkdir(log_today_dir, mode=0o777)
        log_f = open(log_filename, 'a')
        return log_f

    def posix_shell(self):
        log_f = self.__get_log_f()
        old_tty = termios.tcgetattr(sys.stdin)    # TODO
        try:
            # 设置tty为raw模式, 不再使用已经设置好的tty, tty需要由我们来重新控制
            tty.setraw(sys.stdin.fileno())
            tty.setcbreak(sys.stdin.fileno())
            self.chan.settimeout(0.0) # TODO

            while True:
                try:
                    r, w, e = select.select([self.chan, sys.stdin], [], [])
                except:
                    pass

                if self.chan in r:
                    try:
                        recv_data = self.chan.recv(1024).decode('utf8')
                        if len(recv_data) == 0:
                            break
                        sys.stdout.write(recv_data)
                        sys.stdout.flush()
                        # 记录输入输出到日志
                        log_f.write(recv_data)
                    except socket.timeout:
                        print('Timeout')
                if sys.stdin in r:
                    x = os.read(sys.stdin.fileno(), 1024)
                    if len(x) == 0:
                        break
                    self.chan.send(x)

        finally:
            # 最终将原来的tty返回给用户
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_tty)
            log_f.close()


class MenuOption:
     
    def __init__(self, user_login):
        self.user = user_login
    
    def info_assets_user(self):
        print('%-16s\t%-16s' % ('Hostname', 'IP')) 
        for asset in get_user_asset(self.user):
            print('%-16s\t%-16s' % (asset.hostname, asset.ip))
     

    @staticmethod 
    def is_ipv4(addr):
        pattern = '(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}'
        return True if re.fullmatch(pattern, addr) else False

    def menu(self):
        option_print = """\n\033[1;32m###    欢迎使用JMS跳板机系统   ### \033[0m
        1) 输入 \033[32mIP\033[0m 登录设备
        2) 按 \033[32mp\033[0m 查看有权限的设备
        3) 按 \033[32mq\033[0m 退出
        """
        if self.user:
            print(textwrap.dedent(option_print)) 
        else:
            color_msg('用户不存在,正在退出', exit=True)
   
    @staticmethod 
    def option():
        opt = input('请输入选项: ').strip() 
        return opt
 
    @staticmethod   
    def connect(ip):
        try:
            asset = Assets.objects.get(ip=ip) 
        except Assets.DoesNotExist:
            print('ip不正确')
            return 
        print('{0} {1} {2} {3}'.format(asset.ip, asset.port, asset.account, asset.password))
        tty_ = TTY(host=asset.ip, port=asset.port, username=asset.account, password=asset.password)
        tty_.posix_shell()
        
 
    def dispatcher(self):
        while True:
            input_ = self.option()
            if input_ == 'p':
                self.info_assets_user()
                continue
            elif input_ == 'q':
                print('正在退出JMS')
                sys.exit(1)
            elif self.is_ipv4(input_):   
                self.connect(input_)
            else:
                print('输入不正确') 

   
if __name__=='__main__':
    mo = MenuOption(user_login)    
    mo.menu()
    mo.dispatcher()
