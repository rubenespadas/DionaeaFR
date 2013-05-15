from django.shortcuts import render_to_response
from django.db.models import Count
from django.conf import settings

from Web.models.connection import Connection
from Web.models.download import Download
from Web.models.virustotalscan import Virustotalscan


def home(request):
    num_connections = Connection.objects.all().count()
    num_ips = Connection.objects.values(
        'remote_host'
    ).annotate(
        num=Count(
            'remote_host'
        )
    ).count()
    num_urls = Download.objects.values(
        'download_url'
    ).annotate(
        num=Count(
            'download_url'
        )
    ).count()
    num_downloads = Download.objects.all().count()
    num_analized = Virustotalscan.objects.filter(
        virustotalscan_scanner=settings.ANTIVIRUS_VIRUSTOTAL
    ).count()
    known = Virustotalscan.objects.filter(
        virustotalscan_scanner=settings.ANTIVIRUS_VIRUSTOTAL
    ).exclude(
        virustotalscan_result__isnull=True
    )
    num_known = known.count()
    return render_to_response(
        'home.html',
        {
            'num_connections': num_connections,
            'num_ips': num_ips,
            'num_urls': num_urls,
            'num_downloads': num_downloads,
            'num_analized': num_analized,
            'num_known': num_known,
            'av_motor': settings.ANTIVIRUS_VIRUSTOTAL
        }
    )

# vim: set expandtab:ts=4
