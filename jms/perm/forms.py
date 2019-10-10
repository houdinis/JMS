from django.forms import ModelForm
from .models import Perm


class PermListForm(ModelForm):

    class Meta:
        model = Perm
        fields = '__all__'

        labels = {
            'name': '授权名',
            'user': '用户',
            'assets': '资产',
            'remark': '备注',
        }
