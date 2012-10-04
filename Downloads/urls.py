from django.conf.urls import patterns, url

urlpatterns = patterns('Downloads.views',
    url(r'^$', 'index'),
    url(r'^(?P<download_id>\d+)/$', 'detail'),
)