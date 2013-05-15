from django.db import models

from Web.models.connection import Connection
from Web.models.dcerpcserviceop import Dcerpcserviceop

LINK_MS_PATTERN = '<a href="https://technet.microsoft.com/en-us/security/bulletin/{0}">{1}</a>'
LIST_PATTERN = '<li>{0}</li>'


class Dcerpcrequest(models.Model):

    dcerpcrequest = models.IntegerField(
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

    dcerpcrequest_uuid = models.TextField(
        blank=True
    )

    dcerpcrequest_opnum = models.IntegerField(
        blank=True
    )

    class Meta:
        db_table = u'dcerpcrequests'
        ordering = ['-dcerpcrequest']
        verbose_name_plural = "Dcerpcrequests"

    def __str__(self):
        return str(self.dcerpcrequest)

    @property
    def getOpsName(self):
        ops = Dcerpcserviceop.objects.filter(
            dcerpcserviceop_opnum=self.dcerpcrequest_opnum
        )
        data = '<ul class="unstyled">'
        for op in ops:
            data = data + LIST_PATTERN.fomart(
                op.getName()
            )
        data += '</ul>'
        return data

    @property
    def getOpsVuln(self):
        ops = Dcerpcserviceop.objects.filter(
            dcerpcserviceop_opnum=self.dcerpcrequest_opnum
        )
        data = '<ul class="unstyled">'
        for op in ops:
            data = data + LIST_PATTERN.fomart(
                LINK_MS_PATTERN.format(
                    op.getVuln(),
                    op.getVuln()
                )
            )
        data += '</ul>'
        return data

    @property
    def getService(self):
        ops = Dcerpcserviceop.objects.filter(
            dcerpcserviceop_opnum=self.dcerpcrequest_opnum
        )
        data = '<ul class="unstyled">'
        for op in ops:
            data = data + LIST_PATTERN.fomart(
                op.getService()
            )
        data += '</ul>'
        return data

# vim: set expandtab:ts=4
