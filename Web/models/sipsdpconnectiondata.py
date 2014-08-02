from django.db import models

LI_PATTERN = '<li><b>{0}:</b> {1}</li>'


class SipSdpConnectionData(models.Model):
    sip_sdp_connectiondata = models.IntegerField(
        primary_key=True,
        blank=True
    )

    sip_command = models.IntegerField(
        blank=True
    )

    sip_sdp_connectiondata_nettype = models.TextField(
        blank=True
    )

    sip_sdp_connectiondata_addrtype = models.TextField(
        blank=True
    )

    sip_sdp_connectiondata_connection_address = models.TextField(
        blank=True
    )

    sip_sdp_connectiondata_ttl = models.TextField(
        blank=True
    )

    sip_sdp_connectiondata_number_of_addresses = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'sip_sdp_connectiondatas'
        ordering = ['-sip_sdp_connectiondata']
        verbose_name_plural = "SipSdpConnectiondatas"

    def __str__(self):
        return str(self.sip_sdp_connectiondata)

    @property
    def getData(self):
        data = '<ul class="unstyled">'
        data += LI_PATTERN.format(
            'NetType',
            str(self.sip_sdp_connectiondata_nettype)
        )
        data += LI_PATTERN.format(
            'AddrType',
            str(self.sip_sdp_connectiondata_addrtype)
        )
        data += LI_PATTERN.format(
            'Addresses',
            str(self.sip_sdp_connectiondata_connection_address)
        )
        data += LI_PATTERN.format(
            'TTL',
            str(self.sip_sdp_connectiondata_ttl)
        )
        data += LI_PATTERN.format(
            'Num Addrs',
            str(self.sip_sdp_connectiondata_number_of_addresses)
        )
        data += '</ul>'
        return data

# vim: set expandtab:ts=4
