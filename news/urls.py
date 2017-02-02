from django.conf.urls import url
from django.conf import settings
from .views import create_article, show_list, show_article, reload_page
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$', auth_views.login,
    	{'template_name': 'login.html'}, name='login'),
    # url(r'^login$', login, name='login'),
    url(r'^create/$', create_article, name='create'),
    url(r'^create/(?P<id>\w+)/$', create_article, name='create'),
    url(r'^view/(?P<id>\w+)/$', show_article, name='view'),
    url(r'^reload/$', reload_page, name='reload'),
    url(r'^$', show_list, name='show_list'),
]
