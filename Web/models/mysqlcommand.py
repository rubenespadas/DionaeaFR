from django.db import models

from Web.models.connection import Connection
from Web.models.mysqlcommandop import MysqlCommandOp
from Web.models.mysqlcommandarg import MysqlCommandArg


class MysqlCommand(models.Model):
    mysql_command = models.IntegerField(
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

    mysql_command_cmd = models.TextField()

    class Meta:
        db_table = u'mysql_commands'
        ordering = ['-mysql_command']
        verbose_name_plural = "MysqlCommands"

    def __str__(self):
        return str(self.mysql_command)

    @property
    def getOps(self):
        ops = MysqlCommandOp.objects.get(
            mysql_command_cmd=self.mysql_command_cmd
        )
        return ops

    @property
    def getArgs(self):
        args = MysqlCommandArg.objects.get(
            mysql_command=int(self.mysql_command)
        )
        return args

# vim: set expandtab:ts=4
