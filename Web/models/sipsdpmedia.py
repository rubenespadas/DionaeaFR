from django.db import models

UL_PATTERN = '<ul class="unstyled"><li><b>{0}:</b> {1}:{2}</li></ul>'


class SipSdpMedia(models.Model):
    sip_sdp_media = models.IntegerField(
        primary_key=True,
        blank=True
    )

    sip_command = models.IntegerField(
        blank=True
    )

    sip_sdp_media_media = models.TextField(
        blank=True
    )

    sip_sdp_media_port = models.TextField(
        blank=True
    )

    sip_sdp_media_number_of_ports = models.TextField(
        blank=True
    )

    sip_sdp_media_proto = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'sip_sdp_medias'
        ordering = ['-sip_sdp_media']
        verbose_name_plural = "SipSdpMedias"

    def __str__(self):
        return str(self.sip_sdp_media)

    @property
    def getData(self):
        return UL_PATTERN.format(
            str(self.sip_sdp_media_media),
            str(self.sip_sdp_media_proto),
            str(self.sip_sdp_media_port)
        )


# vim: set expandtab:ts=4
