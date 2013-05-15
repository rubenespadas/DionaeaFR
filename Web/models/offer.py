from django.db import models

from Web.models.connection import Connection


class Offer(models.Model):

    offer = models.IntegerField(primary_key=True, blank=True)

    connection = models.ForeignKey(
        Connection,
        to_field='connection',
        db_column='connection',
        related_name='connection__connection',
        verbose_name='Connection'
    )

    offer_url = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'offers'
        ordering = ['-offer']
        verbose_name_plural = "Offers"

    def __str__(self):
        return str(self.offer)

# vim: set expandtab:ts=4
