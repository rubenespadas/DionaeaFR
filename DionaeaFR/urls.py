from django.conf.urls import patterns, url
from Web.views.other import home
from Web.views.connection import connectionIndex, connectionDetail
from Web.views.download import downloadIndex
from Web.views.graph import services, servicesData
from Web.views.graph import ports, portsData
from Web.views.graph import urls, urlsData
from Web.views.graph import malware, malwareData
from Web.views.graph import ips, ipsData, ipsCountries
from Web.views.graph import connections, connectionsData, connCountries
from Web.views.graph import timeline
from Web.views.map import attackersMap, countriesMap


urlpatterns = patterns(
    'Web.views',
    url(
        r'^$',
        home
    ),
    url(
        r'^connections/$',
        connectionIndex,
        name='connection-index'
    ),
    url(
        r'^connections/(?P<connection_id>\d+)/',
        connectionDetail,
        name='connection-detail'
    ),
    url(
        r'^downloads/',
        downloadIndex,
        name='download-index'
    ),
    url(
        r'^graphs/services/$',
        services,
        name='services'
    ),
    url(
        r'^graphs/servicesdata/$',
        servicesData,
        name='services-data'
    ),
    url(
        r'^graphs/ports/$',
        ports,
        name='ports'
    ),
    url(
        r'^graphs/portsdata/$',
        portsData,
        name='ports-data'
    ),
    url(
        r'^graphs/urls/$',
        urls,
        name='urls'
    ),
    url(
        r'^graphs/urlsdata/$',
        urlsData,
        name='urls-data'
    ),
    url(
        r'^graphs/malware/$',
        malware,
        name='malware'
    ),
    url(
        r'^graphs/malwaredata/$',
        malwareData,
        name='malware-data'
    ),
    url(
        r'^graphs/ips/$',
        ips,
        name='ips'
    ),
    url(
        r'^graphs/ipsdata/$',
        ipsData,
        name='ips-data'
    ),
    url(
        r'^graphs/connections/$',
        connections,
        name='connections'
    ),
    url(
        r'^graphs/connectionsdata/$',
        connectionsData,
        name='connections-data'
    ),
    url(
        r'^graphs/timeline/$',
        timeline,
        name='timeline'
    ),
    url(
        r'^graphs/conncountries/$',
        connCountries,
        name='conn-countries'
    ),
    url(
        r'^graphs/ipscountries/$',
        ipsCountries,
        name='ips-countries'
    ),
    url(
        r'^maps/attackers/$',
        attackersMap,
        name='attackers-map'
    ),
    url(
        r'^maps/countries/$',
        countriesMap,
        name='countries-map'
    ),
)

# vim: set expandtab:ts=4
