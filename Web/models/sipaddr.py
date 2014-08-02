from django.db import models

LI_PATTERN = '<li><b>{0}:</b> {1} {2}:{3}@{4}:{5}</li>'


class SipAddr(models.Model):
    sip_addr = models.IntegerField(
        primary_key=True,
        blank=True
    )

    sip_command = models.IntegerField(
        blank=True
    )

    sip_addr_type = models.TextField(
        blank=True
    )

    sip_addr_display_name = models.TextField(
        blank=True
    )

    sip_addr_uri_scheme = models.TextField(
        blank=True
    )

    sip_addr_uri_user = models.TextField(
        blank=True
    )

    sip_addr_uri_password = models.TextField(
        blank=True
    )

    sip_addr_uri_host = models.TextField(
        blank=True
    )

    sip_addr_uri_port = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'sip_addrs'
        ordering = ['-sip_addr']
        verbose_name_plural = "SipAddrs"

    def __str__(self):
        return str(self.sip_addr)

    @property
    def getData(self):
        return LI_PATTERN.format(
            str(self.sip_addr_type),
            str(self.sip_addr_display_name),
            str(self.sip_addr_uri_scheme),
            str(self.sip_addr_uri_user),
            str(self.sip_addr_uri_host),
            str(self.sip_addr_uri_port)
        )

# vim: set expandtab:ts=4
