from django.conf.urls import url
from . import views

app_name = 'assets'
urlpatterns = [
    url(r'^$', views.AssetList.as_view(), name='list'),
    url(r'^create/$', views.AssetCreate.as_view(), name='create'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.AssetDelete.as_view(), name='delete'),
    url(r'^update/(?P<pk>[0-9]+)/$', views.AssetUpdate.as_view(), name='update'),
]