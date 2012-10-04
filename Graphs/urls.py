from django.conf.urls import patterns, url

urlpatterns = patterns('Graphs.views',
    url(r'^protocols/$', 'protocols'),
    url(r'^protocolsdata/$', 'protocolsData'),
    url(r'^urls/$', 'urls'),
    url(r'^urlsdata/$', 'urlsData'),
    url(r'^malware/$', 'malware'),
    url(r'^malwaredata/$', 'malwareData'),
    url(r'^ips/$', 'ips'),
    url(r'^ipsdata/$', 'ipsData'),
)