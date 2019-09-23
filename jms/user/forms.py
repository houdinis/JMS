from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from .models import User


class UserAddForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'password', 'email']
        labels = {
            'name': '姓名',
            'username': '用户名',
            'password': '密码',
            'email': '邮件',
        }
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Name'}),
            'username': TextInput(attrs={'placeholder': 'Username'}),
            'password': PasswordInput(attrs={'placeholder': 'Password'}),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
        }


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'password', 'email', 'is_active', 'is_superuser']
        labels = {
            'name': '姓名',
            'password': '密码',
            'email': '邮件',
            'is_active': '激活',
            'is_superuser': '管理员'
        }
        widgets = {
            'name': TextInput(),
            'password': PasswordInput(render_value=User.password),
            'email': EmailInput(attrs={'placeholder': 'Email'}),
        }
