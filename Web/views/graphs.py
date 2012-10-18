from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import Count
from Web.models import Connection
from Web.models import Virustotal
from Web.models import Offer
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

def attacks(request):
	return render_to_response('graphs/attacks.html')

def attacksData(request):
	from django.db import connection
	cursor = connection.cursor()
	sql = u"""SELECT strftime('%%Y', connection_timestamp,'unixepoch') as 'year', strftime('%%m', connection_timestamp,'unixepoch') as 'month', strftime('%%d', connection_timestamp,'unixepoch') as 'day', count(strftime('%%m', connection_timestamp,'unixepoch')) as 'num'
			FROM connections
			GROUP BY strftime('%%Y', connection_timestamp,'unixepoch'), strftime('%%m', connection_timestamp,'unixepoch'), strftime('%%d', connection_timestamp,'unixepoch')
			ORDER BY strftime('%%Y', connection_timestamp,'unixepoch') DESC, strftime('%%m', connection_timestamp,'unixepoch') DESC, strftime('%%d', connection_timestamp,'unixepoch') DESC
			LIMIT 7"""
	cursor.execute(sql)
	data = []
	for c in cursor.fetchall():
		b = {}
		b['year'] = c[0]
		b['month'] = c[1]
		b['day'] = c[2]
		b['value'] = c[3]
		data.append(b)
	data.reverse()
	return HttpResponse(json.dumps(data), mimetype="application/json")
