from django.db import models

from Web.models.connection import Connection


class P0f(models.Model):
    p0f = models.IntegerField(
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

    p0f_genre = models.TextField(
        blank=True
    )

    p0f_link = models.TextField(
        blank=True
    )

    p0f_detail = models.TextField(
        blank=True
    )

    p0f_uptime = models.IntegerField(
        blank=True
    )

    p0f_tos = models.TextField(
        blank=True
    )

    p0f_dist = models.IntegerField(
        blank=True
    )

    p0f_nat = models.IntegerField(
        blank=True
    )

    p0f_fw = models.IntegerField(
        blank=True
    )

    class Meta:
        db_table = u'p0fs'
        ordering = ['-p0f']
        verbose_name_plural = "P0Fs"

    def __str__(self):
        return str(self.p0f)

# vim: set expandtab:ts=4
