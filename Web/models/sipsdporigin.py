from django.db import models

from Web.models.sipcommand import SipCommand


class SipSdpOrigin(models.Model):
    sip_sdp_origin = models.IntegerField(
        primary_key=True,
        blank=True
    )

    sip_command = models.ForeignKey(
        SipCommand,
        to_field='sip_command',
        db_column='sip_command',
        related_name='sip_commands__sip_command',
        verbose_name='Command'
    )

    sip_sdp_origin_username = models.TextField(
        blank=True
    )

    sip_sdp_origin_sess_id = models.TextField(
        blank=True
    )

    sip_sdp_origin_sess_version = models.TextField(
        blank=True
    )

    sip_sdp_origin_nettype = models.TextField(
        blank=True
    )

    sip_sdp_origin_addrtype = models.TextField(
        blank=True
    )

    sip_sdp_origin_unicast_address = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'sip_sdp_origins'
        ordering = ['-sip_sdp_origin']
        verbose_name_plural = "SipSdpOrigins"

    def __str__(self):
        return str(self.sip_sdp_origin)

# vim: set expandtab:ts=4
