from django.db import models

from Web.models.connection import Connection
from Web.models.virustotal import Virustotal


class Download(models.Model):
    download = models.IntegerField(
        primary_key=True,
        blank=True,
        verbose_name='ID'
    )

    connection = models.ForeignKey(
        Connection,
        to_field='connection',
        db_column='connection',
        related_name='connection__connection',
        verbose_name='Connection'
    )

    download_url = models.TextField(
        blank=True,
        verbose_name='Url'
    )

    download_md5_hash = models.TextField(
        blank=True,
        verbose_name='md5'
    )

    class Meta:
        db_table = u'downloads'
        ordering = ['-download']
        verbose_name_plural = "Downloads"

    def __str__(self):
        return str(self.download)

    @property
    def getReport(self):
        vtr = Virustotal.objects.filter(
            virustotal_md5_hash=self.download_md5_hash
        ).order_by(
            '-virustotal'
        )[:1]
        return vtr

# vim: set expandtab:ts=4
