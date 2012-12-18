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
	known = Virustotalscan.objects.filter(virustotalscan_scanner='Sophos').exclude(virustotalscan_result__isnull=True)
	num_known = known.count()
	unknown = Virustotalscan.objects.filter(virustotalscan_scanner='Sophos').exclude(virustotalscan_result__isnull=False)
	num_unkown = unknown.count()
	return render_to_response('index/index.html',
		{
			'num_connections': num_connections,
			'num_ips': num_ips,
			'num_urls': num_urls,
			'num_downloads': num_downloads,
			'num_known': num_known,
			'num_unkown': num_unkown
		}
	)

