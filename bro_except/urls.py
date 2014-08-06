from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^download/(?P<api_key>[a-f0-9-]+)/', 'exception.views.download_all', name='download_all'),

    url(r'^admin/', include(admin.site.urls)),
)
