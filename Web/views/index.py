from django.shortcuts import render_to_response
from django.db.models import Count
from Web.models import Connection
from Web.models import Download
from Web.models import Virustotalscan

def index(request):
	num_connections = Connection.objects.all().count()
	num_ips = Connection.objects.values('remote_host').annotate(num=Count('remote_host')).count()
	num_urls = Download.objects.values('download_url').annotate(num=Count('download_url')).count()
	num_downloads = Download.objects.all().count()
	num_unique = Virustotalscan.objects.filter(virustotalscan_scanner='Sophos').count()
	known = Virustotalscan.objects.filter(virustotalscan_scanner='Sophos').exclude(virustotalscan_result__isnull=True)
	num_known = known.count()
	return render_to_response('index/index.html',
		{
			'num_connections': num_connections,
			'num_ips': num_ips,
			'num_urls': num_urls,
			'num_downloads': num_downloads,
			'num_unique': num_unique,
			'num_known': num_known
		}
	)

