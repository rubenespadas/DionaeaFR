from django.db import models

from Web.models.connection import Connection
from Web.models.dcerpcserviceop import Dcerpcserviceop


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
    def getOps(self):
        ops = Dcerpcserviceop.objects.filter(
            dcerpcserviceop_opnum=self.dcerpcrequest_opnum
        )
        return ops

# vim: set expandtab:ts=4
