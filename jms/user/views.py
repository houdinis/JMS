<<<<<<< HEAD
#!/root/anaconda3/envs/jms/bin/python
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from .models import User
from .forms import UserAddForm, UserUpdateForm
from .utils import UserManager, Bash
from django.conf import settings
=======
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import User
from .forms import UserAddForm, UserUpdateForm
from django.contrib.auth.hashers import make_password
from django.conf import settings
from .utils import UserManager, Bash
>>>>>>> 6fbd2458bc48b291b170883f84e1268ac32948df
import os

init_path = os.path.join(settings.BASE_DIR, 'init.sh')

<<<<<<< HEAD

@login_required
@user_passes_test(lambda user: user.is_superuser)
=======
@login_required
>>>>>>> 6fbd2458bc48b291b170883f84e1268ac32948df
def user_list(request):
    user = User.objects.all()
    form = UserAddForm()
    return render(request, 'user/list.html', {'users': user, 'form': form})


# 用户增加
@login_required
<<<<<<< HEAD
@user_passes_test(lambda user: user.is_superuser)
=======
>>>>>>> 6fbd2458bc48b291b170883f84e1268ac32948df
def user_create(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            username = form.cleaned_data['username'].strip()
            password = form.cleaned_data['password'].strip()
            f = form.save(commit=False)
            user = UserManager(Bash) 
            ret, msg = user.user_create(username=username, password=password, shell=init_path)
            if not ret:
=======
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            f = form.save(commit=False)
            user = UserManager(Bash) 
            ret, msg = user.user_create(username=username, password=password, shell=init_path)
            if ret:
>>>>>>> 6fbd2458bc48b291b170883f84e1268ac32948df
               f.save()
               return HttpResponseRedirect(reverse('user:list'))
            else:
               user.user_delete(username)
               return HttpResponse(msg)
        else:
            error_msg = form.errors
            return HttpResponse('验证失败: {}'.format(error_msg))
        return HttpResponse('The data entered is not valid!')
    return HttpResponse('Method mismatch!')


@login_required
<<<<<<< HEAD
@user_passes_test(lambda user: user.is_superuser)
=======
>>>>>>> 6fbd2458bc48b291b170883f84e1268ac32948df
def user_delete(request, pk):
    user = get_object_or_404(User, id=pk)
    um = UserManager(Bash)
    msg = um.user_delete(user.username)
    print(msg)
    user.delete()
    return HttpResponseRedirect(reverse('user:list'))


# 用户信息更新
@login_required
<<<<<<< HEAD
@user_passes_test(lambda user: user.is_superuser)
=======
>>>>>>> 6fbd2458bc48b291b170883f84e1268ac32948df
def user_update(request, pk):
    user = get_object_or_404(User, id=pk)

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            password = form.cleaned_data['password'].strip() 
            f = form.save(commit=False)
            if password:
                um = UserManager(Bash)
<<<<<<< HEAD
                ret, msg = um.user_create(username=user.username, password=password, shell=init_path)
=======
                ret, msg = um.user_create(username=user.username, password=password,shell=init_path)
>>>>>>> 6fbd2458bc48b291b170883f84e1268ac32948df
                user.set_password(password)
                if ret:
                    return HttpResponse(msg)
            f.save()
            return HttpResponseRedirect(reverse('user:list'))
    form = UserUpdateForm(instance=user)
    return render(request, 'user/update.html', {'form': form})


# 登陆
def user_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
<<<<<<< HEAD
=======
        print(username, password)
>>>>>>> 6fbd2458bc48b291b170883f84e1268ac32948df
        user_obj = authenticate(username=username, password=password)
        if user_obj is not None:
            if user_obj.is_active:
                login(request, user_obj)
                return HttpResponseRedirect(reverse('user:list'))
            else:
                error = '用户已被禁用!'
        else:
            error = '用户或密码不正确,请重新输入!'
    return render(request, 'user/login.html', {'error': error})


# 退出
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:login'))

