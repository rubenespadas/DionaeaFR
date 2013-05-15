from django.db import models

from Web.models.connection import Connection


class Dcerpcbind(models.Model):

    dcerpcbind = models.IntegerField(
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

    dcerpcbind_uuid = models.TextField(
        blank=True
    )

    dcerpcbind_transfersyntax = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'dcerpcbinds'
        ordering = ['-dcerpcbind']
        verbose_name_plural = "Dcerpcbinds"

    def __str__(self):
        return str(self.dcerpcbind)

# vim: set expandtab:ts=4
