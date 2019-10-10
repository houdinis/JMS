
from .models import Perm
from user.models import User

def get_user_asset(user):
    user_id = User.objects.filter(username=user).first()
    perms = Perm.objects.filter(user=user_id).first()
    assets = perms.assets.all()
    return assets
