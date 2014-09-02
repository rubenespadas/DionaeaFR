from django.db import models

from Web.models.sipcommand import SipCommand


class SipVia(models.Model):
    sip_via = models.IntegerField(
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

    sip_via_protocol = models.TextField(
        blank=True
    )

    sip_via_address = models.TextField(
        blank=True
    )

    sip_via_port = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'sip_vias'
        ordering = ['-sip_via']
        verbose_name_plural = "SipVias"

    def __str__(self):
        return str(self.sip_via)

# vim: set expandtab:ts=4
