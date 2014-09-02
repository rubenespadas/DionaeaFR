from django.db import models

from Web.models.connection import Connection


class Resolve(models.Model):
    resolve = models.IntegerField(
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

    resolve_hostname = models.TextField(
        blank=True
    )

    resolve_type = models.TextField(
        blank=True
    )

    resolve_result = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'resolves'
        ordering = ['-resolve']
        verbose_name_plural = "Resolves"

    def __str__(self):
        return str(self.resolve)

# vim: set expandtab:ts=4
