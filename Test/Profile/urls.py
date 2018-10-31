from django.conf.urls import url
from django.urls import path

from . import views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^user$', views.index, name='index'),
    url(r'^user/(?P<profile_id>[0-9]+)/$', views.profile, name='profile'),
    path('edit', views.edit_profile, name='edit'),
]