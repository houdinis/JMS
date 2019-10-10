from django.conf.urls import url
from . import views


app_name = 'user'
urlpatterns = [
    url(r'^$', views.user_list, name='list'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^create/$', views.user_create, name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.user_delete, name='delete'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.user_update, name='update'),
]
