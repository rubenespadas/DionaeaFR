from django.conf.urls import patterns, url

urlpatterns = patterns('Maps.views',
    url(r'^attackers/$', 'attackers'),
    url(r'^countries/$', 'countries'),
)
