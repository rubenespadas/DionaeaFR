from django.db import models


class Dcerpcservice(models.Model):
    dcerpcservice = models.IntegerField(
        primary_key=True,
        blank=True
    )

    dcerpcservice_uuid = models.TextField(
        unique=True,
        blank=True
    )

    dcerpcservice_name = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'dcerpcservices'
        ordering = ['-dcerpcservice']
        verbose_name_plural = "Dcerpcservices"

    def __str__(self):
        return str(self.dcerpcservice)

    @property
    def getName(self):
        return str(self.dcerpcservice_name)

# vim: set expandtab:ts=4
