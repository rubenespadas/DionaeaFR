from django.db import models

from Web.models.connection import Connection


class EmuService(models.Model):
    emu_serivce = models.IntegerField(
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

    emu_service_url = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'emu_services'
        ordering = ['-emu_serivce']
        verbose_name_plural = "EmuServices"

    def __str__(self):
        return str(self.emu_serivce)

# vim: set expandtab:ts=4
