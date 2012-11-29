from django.shortcuts import render_to_response
from django.template import RequestContext
from django_tables2 import RequestConfig
from web.tables import DownloadsTable
from web.models import Download


length = len(Download.objects.all())

def dindex(request):
    queryset = Download.objects.all()
    table = DownloadsTable(queryset)
    RequestConfig(request, paginate={"per_page": 20}).configure(table)
    return render_to_response('downloads/index.html', {"table": table}, context_instance=RequestContext(request))