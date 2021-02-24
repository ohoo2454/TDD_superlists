from django.conf.urls import url
from django.contrib import auth

from accounts import views

urlpatterns = [
    url(r'^login$', views.persona_login, name='persona_login'),
    url(r'^logout$', auth.logout, {'next_page': '/'}, name='logout'),
]
