#!/root/anaconda3/envs/jms/bin python3.5
import subprocess
import os
import pwd


class Bash(object):
    def __init__(self):
        self.ret = None

    def exec(self, command):
        self.ret = subprocess.Popen('{0}'.format(command), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.ret.wait()
        print(self.ret.stderr.read())
    
    @property
    def stdout(self):
        return self.ret.stdout.read()

    @property
    def stderr(self):
        return self.ret.stderr.read()

    @property
    def code(self):
        return self.ret.returncode


class UserManager(object):
    def __init__(self, sh):
        self.sh = sh()

    # 用户添加
    def user_create(self, username=None, password=None, shell='/bin/bash'):
        cmd = 'id {username} || useradd {username} -s {shell}'.format(username=username, shell=shell)
        self.sh.exec(cmd)
        if self.sh.code != 0:
            return [1, '用户添加失败!']

        if password:
            cmd = 'echo {password} | passwd --stdin {username}'.format(password=password, username=username)
            self.sh.exec(cmd)
            if self.sh.code != 0:
                return [1, '用户密码修改失败!']
        return [0, '用户添加成功!']

    # 用户删除
    def user_delete(self, username='', force=False):
        if self.check_user_exist(username):
            cmd = 'userdel {username}'.format(username=username)
            if force:
                cmd += '--force -r'
            self.sh.exec(cmd)
            if self.sh.code:
                return [0, '用户已删除!']
            else:
                return [1, '用户删除失败!']
        return [1, '用户不存在!']

    # 检查用户是否存在
    def check_user_exist(self, username):
        cmd = 'id {username}'.format(username=username)
        self.sh.exec(cmd)
        if self.sh.code == 0:
            return True
        else:
            return False
