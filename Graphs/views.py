from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import Count
from Connections.models import Connection
from Connections.models import Virustotal
from Connections.models import Offer
import datetime
import time
import json

def protocols(request):
	return render_to_response('graphs/protocols.html')

def protocolsData(request):
	date_now = datetime.date.today() - datetime.timedelta(days=7)
	conn = Connection.objects.filter(connection_timestamp__gt=time.mktime(date_now.timetuple())).values('connection_protocol').annotate(Count("connection_protocol")).order_by('-connection_protocol__count')
	data = []
	for c in conn:
		b = {}
		b['name'] = c['connection_protocol']
		b['value'] = c['connection_protocol__count']
		data.append(b)
	return HttpResponse(json.dumps(data), mimetype="application/json")

def urls(request):
	return render_to_response('graphs/urls.html')

def urlsData(request):
	date_now = datetime.date.today() - datetime.timedelta(days=7)
	conn = Offer.objects.all().values('offer_url').annotate(Count("offer_url")).order_by('-offer_url__count')[:10]
	data = []
	for c in conn:
		b = {}
		b['name'] = c['offer_url']
		b['value'] = c['offer_url__count']
		data.append(b)
	return HttpResponse(json.dumps(data), mimetype="application/json")

def malware(request):
	return render_to_response('graphs/malware.html')

def malwareData(request):
	conn = Virustotal.objects.filter().values('virustotal_md5_hash').annotate(Count("virustotal_md5_hash")).order_by('-virustotal_md5_hash__count')[:10]
	data = []
	for c in conn:
		b = {}
		name = Virustotal.objects.filter(virustotal_md5_hash=c['virustotal_md5_hash'])[:1]
		b['name'] = c['virustotal_md5_hash'] + ' - ' + name[0].getResult() 
		b['value'] = c['virustotal_md5_hash__count']
		data.append(b)
	return HttpResponse(json.dumps(data), mimetype="application/json")

def ips(request):
	return render_to_response('graphs/ips.html')

def ipsData(request):
	date_now = datetime.date.today() - datetime.timedelta(days=7)
	conn = Connection.objects.filter(connection_timestamp__gt=time.mktime(date_now.timetuple())).values('remote_host').annotate(Count("remote_host")).order_by('-remote_host__count')[:10]
	data = []
	for c in conn:
		b = {}
		if c['remote_host'] == "":
			b['name'] = '127.0.0.1'
		else:
			b['name'] = c['remote_host']
		b['value'] = c['remote_host__count']
		data.append(b)
	return HttpResponse(json.dumps(data), mimetype="application/json")
