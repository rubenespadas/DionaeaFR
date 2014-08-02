from django.db import models

from Web.models.connection import Connection


class EmuProfile(models.Model):
    emu_profile = models.IntegerField(
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

    emu_profile_json = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'emu_profiles'
        ordering = ['-emu_profile']
        verbose_name_plural = "EmuProfiles"

    def __str__(self):
        return str(self.emu_profile)

# vim: set expandtab:ts=4
