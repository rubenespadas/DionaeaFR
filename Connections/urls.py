from django.conf.urls import patterns, url

urlpatterns = patterns('Connections.views',
    url(r'^(?P<connection_id>\d+)/$', 'detail'),
)