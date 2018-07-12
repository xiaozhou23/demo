from django.conf.urls import include, url
from django.contrib import admin
from . import views as tv

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangodemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'.*/', tv.do_teacher),
]