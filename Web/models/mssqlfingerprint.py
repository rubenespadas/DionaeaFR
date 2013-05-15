from django.db import models

from Web.models.connection import Connection


class MssqlFingerprint(models.Model):

    mssql_fingerprint = models.IntegerField(
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

    mssql_fingerprint_hostname = models.TextField(
        blank=True
    )

    mssql_fingerprint_appname = models.TextField(
        blank=True
    )

    mssql_fingerprint_cltintname = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'mssql_fingerprints'
        ordering = ['-mssql_fingerprint']
        verbose_name_plural = "MssqlFingerprints"

    def __str__(self):
        return str(self.mssql_fingerprint)

# vim: set expandtab:ts=4
