from django.db import models

from Web.models.connection import Connection


class Login(models.Model):
    login = models.IntegerField(
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

    login_username = models.TextField(
        blank=True
    )

    login_password = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'logins'
        ordering = ['-login']
        verbose_name_plural = "Logins"

    def __str__(self):
        return str(self.login)

# vim: set expandtab:ts=4
