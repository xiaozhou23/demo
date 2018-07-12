from django.conf.urls import include, url
from django.contrib import admin

from demoapp import views as v

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_views.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^demoapp/', v.do_demoapp),
    url(r'^exp/', v.exception)
]
