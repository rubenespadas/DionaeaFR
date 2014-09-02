from django.db import models


class Virustotalscan(models.Model):
    virustotalscan = models.IntegerField(
        primary_key=True,
        blank=True
    )

    virustotal = models.IntegerField()

    virustotalscan_scanner = models.TextField()

    virustotalscan_result = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'virustotalscans'
        ordering = ['-virustotalscan']
        verbose_name_plural = "Virustotalscans"

    def __str__(self):
        return str(self.virustotalscan)

    @property
    def getVirusName(self):
        return str(self.virustotalscan_result)

# vim: set expandtab:ts=4
