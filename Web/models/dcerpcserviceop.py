from django.db import models

from Web.models.dcerpcservice import Dcerpcservice


class Dcerpcserviceop(models.Model):
    dcerpcserviceop = models.IntegerField(
        primary_key=True,
        blank=True
    )

    dcerpcservice = models.IntegerField(
        blank=True
    )

    dcerpcserviceop_opnum = models.IntegerField(
        blank=True
    )

    dcerpcserviceop_name = models.TextField(
        blank=True
    )

    dcerpcserviceop_vuln = models.TextField(
        blank=True
    )

    class Meta:
        db_table = u'dcerpcserviceops'
        ordering = ['-dcerpcserviceop']
        verbose_name_plural = "Dcerpcserviceops"

    def __str__(self):
        return str(self.dcerpcserviceop)

    @property
    def getName(self):
        return str(self.dcerpcserviceop_name)

    @property
    def getVuln(self):
        if self.dcerpcserviceop_vuln:
            vuln = self.dcerpcserviceop_vuln.split('-')
            if vuln[1][:1] != '0':
                return str(vuln[0] + '-0' + vuln[1])
            else:
                return str(self.dcerpcserviceop_vuln)
        else:
            return str(self.dcerpcserviceop_vuln)

    @property
    def getService(self):
        srv = Dcerpcservice.objects.get(
            dcerpcservice=self.dcerpcservice
        )
        return srv

# vim: set expandtab:ts=4
