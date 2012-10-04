from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
	url(r'^$', 'Connections.views.index'),
    url(r'^connections/', include('Connections.urls')),
    url(r'^downloads/', include('Downloads.urls')),
    url(r'^graphs/', include('Graphs.urls')),
    url(r'^maps/', include('Maps.urls')),
)

urlpatterns += staticfiles_urlpatterns()