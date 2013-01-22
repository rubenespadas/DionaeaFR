from django.shortcuts import render_to_response
from django.template import RequestContext
from django_tables2 import RequestConfig
from django.http import Http404
from Web.tables import ConnectionsTable
from Web.models import Connection
from Web.models import Dcerpcbind
from Web.models import Dcerpcrequest
from Web.models import Download
from Web.models import EmuProfile
from Web.models import EmuService
from Web.models import Login
from Web.models import MssqlCommand
from Web.models import MssqlFingerprint
from Web.models import MysqlCommand
from Web.models import Offer
from Web.models import P0f
from Web.models import Resolve
from Web.models import SipCommand


def cindex(request):
    queryset = Connection.objects.all()
    table = ConnectionsTable(queryset)
    RequestConfig(request, paginate={"per_page": 20}).configure(table)
    return render_to_response('connections/index.html', {"table": table}, context_instance=RequestContext(request))

def cdetail(request, connection_id):
    try:
        q = Connection.objects.annotate(length=Count('connection_id'))
        length = q[0].length
        conn = Connection.objects.get(pk=connection_id)
        dcerpcbind = Dcerpcbind.objects.filter(connection=connection_id)
       	dcerpcrequest = Dcerpcrequest.objects.filter(connection=connection_id)
       	download = Download.objects.filter(connection=connection_id)
       	emuProfile = EmuProfile.objects.filter(connection=connection_id)
       	emuService = EmuService.objects.filter(connection=connection_id)
       	login = Login.objects.filter(connection=connection_id)
       	mssqlCommand = MssqlCommand.objects.filter(connection=connection_id)
       	mssqlFingerprint = MssqlFingerprint.objects.filter(connection=connection_id)
       	mysqlCommand = MysqlCommand.objects.filter(connection=connection_id)
       	offer = Offer.objects.filter(connection=connection_id)
       	p0f = P0f.objects.filter(connection=connection_id)
       	resolve = Resolve.objects.filter(connection=connection_id)
       	sipcommand = SipCommand.objects.filter(connection=connection_id)
        previous = 0
        next = 0
        if int(connection_id) > 0:
            previous = int(connection_id) - 1
        if int(connection_id) < length:
            next = int(connection_id) + 1
    except Connection.DoesNotExist:
        raise Http404
    return render_to_response('connections/detail.html',
		{
            'connection' : conn,
            'dcerpcbind' : dcerpcbind,
            'dcerpcrequest' : dcerpcrequest,
            'download' : download,
            'emuProfile' : emuProfile,
            'emuService' : emuService,
            'login' : login,
            'mssqlCommand' : mssqlCommand,
            'mssqlFingerprint' : mssqlFingerprint,
            'mysqlCommand' : mysqlCommand,
            'offer' : offer,
            'p0f' : p0f,
            'resolve' : resolve,
            'sipcommand' : sipcommand,
            'previous' : int(previous),
            'next' : int(next)
		}
	)
