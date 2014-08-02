import re
import time
import datetime
import sys
import os

try:
    import pygeoip
except ImportError:
    print "Install pygeoip"
    print "\tpip install pygeoip"
    pass

from django.conf import settings
from django.shortcuts import render_to_response

from Web.models.connection import Connection

reload(sys)
sys.setdefaultencoding('utf-8')

gi = pygeoip.GeoIP(
    os.path.join(
        'DionaeaFR/static',
        'GeoIP.dat'
    ),
    pygeoip.MEMORY_CACHE
)

gic = pygeoip.GeoIP(
    os.path.join(
        'DionaeaFR/static',
        'GeoLiteCity.dat'
    ),
    pygeoip.STANDARD
)

IP_PATTERN = "(^[2][0-5][0-5]|^[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})$"
LAT_PATTERN = "{{latLng:[{:-f},{:-f}], count:'{}', host:'{}'}},"
COUNTRY_PATTERN = '"{0}":{1},'


def countriesMap(request):
    date_now = datetime.date.today() - datetime.timedelta(days=settings.RESULTS_DAYS)
    conn = Connection.objects.filter(
        connection_timestamp__gt=time.mktime(
            date_now.timetuple()
        )
    ).values(
        'remote_host'
    )
    data = {}
    for c in conn:
        if (re.match(IP_PATTERN, c['remote_host']) is not None):
            cc = gi.country_code_by_addr(
                c['remote_host']
            )
            if cc != "":
                try:
                    data[cc] += 1
                except:
                    data[cc] = 1
    var = "var gdpData = {"
    for country in data:
        var = var + COUNTRY_PATTERN.format(
            country,
            str(data[country])
        )
    var = var.rstrip(',') + "};"
    return render_to_response(
        'maps/countries.html',
        {
            'cc': var
        }
    )


def attackersMap(request):
    date_now = datetime.date.today() - datetime.timedelta(days=settings.RESULTS_DAYS)
    conn = Connection.objects.filter(
        connection_timestamp__gt=time.mktime(
            date_now.timetuple()
        )
    ).values(
        'remote_host'
    )
    var = "var gdpData = ["
    counts = {}
    for c in conn:
        if (re.match(IP_PATTERN, c['remote_host']) is not None):
            try:
                counts[c['remote_host']] += 1
            except:
                counts[c['remote_host']] = 1
    for c in counts:
        if (re.match(IP_PATTERN, c) is not None):
            cc = gic.record_by_addr(
                c
            )
            if cc:
                var = var + LAT_PATTERN.format(
                    cc['latitude'],
                    cc['longitude'],
                    counts[c],
                    str(c)
                )
    var = var.rstrip(',') + "];"
    return render_to_response(
        'maps/attackers.html',
        {
            'attackers': var
        }
    )

# vim: set expandtab:ts=4
