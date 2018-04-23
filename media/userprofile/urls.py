from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from userprofile import views

app_name = 'userprofile'


urlpatterns = [
    url(r'^logout$', views.logout_view, name='logout_view'),
    url(r'^login/$', auth_views.login, {'template_name':'userprofile/login.html'}),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
]
