from django.conf.urls import include, url
from django.conf import settings
#from django.contrib import admin

#admin.autodiscover()


urlpatterns = [
    url(r'', include('news.urls')),
    #url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout'),
    #url(r'^admin/', include(admin.site.urls)),
]