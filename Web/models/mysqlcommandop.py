from django.db import models


class MysqlCommandOp(models.Model):
    mysql_command_op = models.IntegerField(
        primary_key=True,
        blank=True
    )

    mysql_command_cmd = models.IntegerField(
        unique=True
    )

    mysql_command_op_name = models.TextField(
    )

    class Meta:
        db_table = u'mysql_command_ops'
        ordering = ['-mysql_command_op']
        verbose_name_plural = "MysqlCommandOps"

    def __str__(self):
        return str(self.mysql_command_op)

    @property
    def getName(self):
        return str(self.mysql_command_op_name)

# vim: set expandtab:ts=4
