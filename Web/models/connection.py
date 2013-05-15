import datetime
import os
try:
    import pygeoip
except ImportError:
    print "Install pygeoip"
    print "\tpip install pygeoip"
    pass


from django.db import models


gi = pygeoip.GeoIP(
    os.path.join(
        'DionaeaFR/static',
        'GeoIP.dat'
    ),
    pygeoip.MEMORY_CACHE
)


class Connection(models.Model):

    connection = models.IntegerField(
        primary_key=True,
        blank=True,
        verbose_name='ID'
    )

    connection_type = models.TextField(
        blank=True,
        verbose_name='State'
    )

    connection_transport = models.TextField(
        blank=True,
        verbose_name='Protocol'
    )

    connection_protocol = models.TextField(
        blank=True,
        verbose_name='Service'
    )

    connection_timestamp = models.IntegerField(
        blank=True,
        verbose_name='Date'
    )

    connection_root = models.IntegerField(
        blank=True,
        verbose_name='Root'
    )

    connection_parent = models.IntegerField(
        blank=True,
        verbose_name='Parent'
    )

    local_host = models.TextField(
        blank=True,
        verbose_name='Sensor'
    )

    local_port = models.IntegerField(
        blank=True,
        verbose_name='Dst Port'
    )

    remote_host = models.TextField(
        blank=True,
        verbose_name='Attacker'
    )

    remote_hostname = models.TextField(
        blank=True,
        verbose_name='Hostname'
    )

    remote_port = models.IntegerField(
        blank=True,
        verbose_name='Src Port'
    )

    class Meta:
        db_table = u'connections'
        ordering = ['-connection']
        verbose_name_plural = "Connections"

    def __str__(self):
        return str(self.connection)

    @property
    def getDate(self):
        return datetime.datetime.fromtimestamp(
            float(
                self.connection_timestamp
            )
        ).strftime("%d-%m-%Y %H:%M:%S")

    @property
    def getTrace(self):
        conns = Connection.objects.filter(
            connection_root=self.connection_root
        ).order_by(
            'connection'
        )
        return conns

    @property
    def getCC(self):
        cc = None
        if self.remote_host:
            cc = gi.country_code_by_addr(
                self.remote_host
            )
        else:
            cc = "zz"
        if cc:
            return cc.lower()
        else:
            return "zz"

    @property
    def getCountryName(self):
        name = "Unkown"
        if self.remote_host:
            name = gi.country_name_by_addr(
                self.remote_host
            )
        return name

    @property
    def getRemoteHost(self):
        if self.remote_host == "":
            return '127.0.0.1'
        else:
            return self.remote_host

# vim: set expandtab:ts=4
