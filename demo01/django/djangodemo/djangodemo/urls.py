from django.conf.urls import include, url
from django.contrib import admin
from teacher import views as tv
from teacher import teacher_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangodemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^normalmap/', tv.do_normalmap),
    url(r'^param/(?P<year>[0-9]{4})/(?P<month>[0-1][0-9])/', tv.with_param),

    url(r'^teacher/', include(teacher_urls)),
    url(r'^book/(?:page-(?P<pn>\d+)/)$', tv.do_param2),
    url(r'^extra/', tv.extraParam, {'name':"Lily"}),

    url(r'^yourname/', tv.revParse, name="askname")
]
