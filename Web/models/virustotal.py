import datetime

from django.conf import settings
from django.db import models

from Web.models.virustotalscan import Virustotalscan


class Virustotal(models.Model):
    virustotal = models.IntegerField(
        primary_key=True,
        blank=True
    )

    virustotal_md5_hash = models.TextField()

    virustotal_timestamp = models.IntegerField()

    virustotal_permalink = models.TextField()

    class Meta:
        db_table = u'virustotals'
        ordering = ['-virustotal']
        verbose_name_plural = "Virustotals"

    def __str__(self):
        return str(self.virustotal)

    @property
    def getUrl(self):
        return str(self.virustotal_permalink)

    @property
    def getDate(self):
        return datetime.datetime.fromtimestamp(
            float(
                self.virustotal_timestamp
            )
        ).strftime("%d-%m-%Y %H:%M:%S")

    @property
    def getResult(self):
        result = Virustotalscan.objects.get(
            virustotal=self.virustotal,
            virustotalscan_scanner=settings.ANTIVIRUS_VIRUSTOTAL
        )
        return result


# vim: set expandtab:ts=4
