import os
import datetime

import django_tables2 as tables


try:
    import pygeoip
except:
    print "Install pygeoip"
    print "\tpip install pygeoip"
    pass

from django.conf import settings
from django.utils.safestring import mark_safe
from netaddr import IPAddress

try:
    import SubnetTree

    reserved_ipv4 = SubnetTree.SubnetTree()
    for subnet in settings.RESERVED_IP:
        reserved_ipv4[subnet] = subnet
except ImportError:
    reserved_ipv4 = dict()
    print "Install SubnetTree"
    print "\tgit clone git://git.bro-ids.org/pysubnettree.git"
    print "\tpython setup.py install"
    pass

gi = pygeoip.GeoIP(
    os.path.join(
        'DionaeaFR/static',
        'GeoIP.dat'
    ),
    pygeoip.MEMORY_CACHE
)


class UnixToDate(tables.Column):
    def render(self, value):
        return datetime.datetime.fromtimestamp(
            float(value)
        ).strftime("%d-%m-%Y %H:%M:%S")


class FormatIP(tables.Column):
    def render(self, value):
        cc = u'ZZ'
        name = u'Unknown'
        ip = IPAddress(str(value))
        if ip.version == 4:
            try:
                reserved_ipv4[str(ip)]
            except KeyError:
                cc = gi.country_code_by_addr(
                    str(ip)
                )
                name = gi.country_name_by_addr(
                    str(ip)
                )
        if not cc or not name:
            cc = u'ZZ'
            name = u'Unknown'
        return mark_safe(
            '<img class="flag" src="/static/img/flags/' +
            cc.lower() +
            '.gif" rel="tooltip" title="' +
            name +
            '" alt="' +
            name +
            '" data-placement="top"/> ' +
            str(ip)
        )


# vim: set expandtab:ts=4
