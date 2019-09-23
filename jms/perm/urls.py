from django.conf.urls import url
from . import views

app_name = 'perm'
urlpatterns = [
    url(r'^$', views.PermList.as_view(), name='list'),
    url(r'^add/$', views.PermCreate.as_view(), name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.PermDelete.as_view(), name='delete'),
    url(r'^details/(?P<pk>[0-9]+)/$', views.PermDetails.as_view(), name='details'),
]
