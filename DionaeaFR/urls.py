from django.conf.urls import patterns, url
from django_tables2_simplefilter import FilteredSingleTableView
from Web.views import *

urlpatterns = patterns('Web.views',
	url(r'^$', FilteredSingleTableView.as_view(template_name='connections/index.html',
                                        table_class=ConnectionsTable,
                                        model=Connection,
                                        table_pagination={"per_page": 15}),
                                        name='Connections'),
    url(r'^connections/(?P<connection_id>\d+)/', 'cdetail'),
    url(r'^downloads/', FilteredSingleTableView.as_view(template_name='downloads/index.html',
                                        table_class=DownloadsTable,
                                        model=Download,
                                        table_pagination={"per_page": 15}),
                                        name='Downloads'),
    url(r'^graphs/protocols/$', 'protocols'),
    url(r'^graphs/protocolsdata/$', 'protocolsData'),
    url(r'^graphs/urls/$', 'urls'),
    url(r'^graphs/urlsdata/$', 'urlsData'),
    url(r'^graphs/malware/$', 'malware'),
    url(r'^graphs/malwaredata/$', 'malwareData'),
    url(r'^graphs/ips/$', 'ips'),
    url(r'^graphs/ipsdata/$', 'ipsData'),
	url(r'^graphs/attacks/$', 'attacks'),
    url(r'^graphs/attacksdata/$', 'attacksData'),
    url(r'^maps/attackers/$', 'attackers'),
    url(r'^maps/countries/$', 'countries'),
)