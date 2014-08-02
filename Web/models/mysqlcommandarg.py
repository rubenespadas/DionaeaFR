from django.db import models


class MysqlCommandArg(models.Model):
    mysql_command_arg = models.IntegerField(
        primary_key=True,
        blank=True
    )

    mysql_command = models.IntegerField()

    mysql_command_arg_index = models.TextField()

    mysql_command_arg_data = models.TextField()

    class Meta:
        db_table = u'mysql_command_args'
        ordering = ['-mysql_command_arg']
        verbose_name_plural = "MysqlCommandArgs"

    def __str__(self):
        return str(self.mysql_command_arg)

    @property
    def getData(self):
        return str(self.mysql_command_arg_data)

# vim: set expandtab:ts=4
