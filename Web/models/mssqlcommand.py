from django.db import models

from Web.models.connection import Connection


class MssqlCommand(models.Model):
    mssql_command = models.IntegerField(
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

    mssql_command_status = models.TextField(
        blank=True
    )

    mssql_command_cmd = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'mssql_commands'
        ordering = ['-mssql_command']
        verbose_name_plural = "MssqlCommands"

    def __str__(self):
        return str(self.mssql_command)

# vim: set expandtab:ts=4
