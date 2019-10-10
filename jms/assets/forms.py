from django.forms import ModelForm, PasswordInput, TextInput
from .models import Assets


class AssetCreateForm(ModelForm):
    class Meta:
        model = Assets
        fields = ['hostname', 'ip', 'port', 'account', 'password', 'os', 'activate']

        labels = {
            'hostname': '主机名',
            'ip': 'IP',
            'port': '端口',
            'account': '用户名',
            'password': '密码',
            'os': '操作系统',
            'activate': '激活'
        }
        widgets = {
            'hostname': TextInput(attrs={'placeholder': 'hostname'}),
            'ip': TextInput(attrs={'placeholder': 'ip'}),
            'account': TextInput(attrs={'placeholder': 'account'}),
            'password': PasswordInput(attrs={'placeholder': 'Password'}),
        }


class AssetUpdateForm(ModelForm):
    class Meta:
        model = Assets
        fields = ['hostname', 'ip', 'port', 'account', 'password', 'os', 'activate']

        labels = {
            'hostname': '主机名',
            'ip': 'IP',
            'port': '端口',
            'account': '用户名',
            'password': '密码',
            'os': '操作系统',
            'activate': '激活'
        }
        widgets = {
            'hostname': TextInput(attrs={'placeholder': 'hostname'}),
            'ip': TextInput(attrs={'placeholder': 'ip'}),
            'account': TextInput(attrs={'placeholder': 'account'}),
            'password': PasswordInput(render_value=Assets.password),
        }



