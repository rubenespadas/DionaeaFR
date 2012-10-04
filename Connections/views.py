from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.http import Http404
from Connections.models import *

length = len(Connection.objects.all())

def index(request):
	latest_connection_list = Connection.objects.all().order_by('-connection_timestamp')
	paginator = Paginator(latest_connection_list, 15)
	page = request.GET.get('page')
	try:
		latest_connection_list = paginator.page(page)
	except PageNotAnInteger:
		latest_connection_list = paginator.page(1)
	except EmptyPage:
		latest_connection_list = paginator.page(paginator.num_pages)
	return render_to_response('connections/index.html', {"latest_connection_list": latest_connection_list})

def detail(request, connection_id):
    try:
        conn = Connection.objects.get(pk=connection_id)
        dcerpcbind = Dcerpcbind.objects.filter(connection=connection_id)
       	dcerpcrequest = Dcerpcrequest.objects.filter(connection=connection_id)
       	download = Download.objects.filter(connection=connection_id)
       	emuProfile = EmuProfile.objects.filter(connection=connection_id)
       	emuService = EmuService.objects.filter(connection=connection_id)
       	emuServiceOld = EmuServiceOld.objects.filter(connection=connection_id)
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
        if int(connection_id) < int(length):
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
            'emuServiceOld' : emuServiceOld,
            'login' : login,
            'mssqlCommand' : mssqlCommand,
            'mssqlFingerprint' : mssqlFingerprint,
            'mysqlCommand' : mysqlCommand,
            'offer' : offer,
            'p0f' : p0f,
            'resolve' : resolve,
            'sipcommand' : sipcommand,
            'previous' : str(previous),
            'next' : str(next)
		}
	)
