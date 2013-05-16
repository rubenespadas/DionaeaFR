from django.db import models

from Web.models.connection import Connection
from Web.models.sipaddr import SipAddr
from Web.models.sipsdpconnectiondata import SipSdpConnectionData
from Web.models.sipsdpmedia import SipSdpMedia


class SipCommand(models.Model):

    sip_command = models.IntegerField(
        primary_key=True,
        blank=True
    )

    connection = models.ForeignKey(
        Connection,
        to_field='connection',
        db_column='connection',
        related_name='connection__connection',
        verbose_name='Connection'
    )

    sip_command_method = models.TextField(
        blank=True
    )

    sip_command_call_id = models.TextField(
        blank=True
    )

    sip_command_user_agent = models.TextField(
        blank=True
    )

    sip_command_allow = models.IntegerField(
        blank=True
    )

    class Meta:
        db_table = u'sip_commands'
        ordering = ['-sip_command']
        verbose_name_plural = "SipCommands"

    def __str__(self):
        return str(self.sip_command)

    @property
    def getAddr(self):
        addrs = SipAddr.objects.filter(
            sip_command=self.sip_command
        )
        data = '<ul class="unstyled">'
        for addr in addrs:
            data = data + addr.getData()
        data += '</ul>'
        return data

    @property
    def getData(self):
        cdat = SipSdpConnectionData.objects.get(
            sip_command=self.sip_command
        )
        return cdat

    @property
    def getMedia(self):
        media = SipSdpMedia.objects.get(
            sip_command=self.sip_command
        )
        return media

# vim: set expandtab:ts=4
