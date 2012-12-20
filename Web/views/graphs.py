from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import Count
from Web.models import Connection
from Web.models import Offer
from collections import defaultdict
from collections import Counter
from netaddr import IPAddress
import SubnetTree
import pygeoip
import datetime
import time
import json
import re
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

gi = pygeoip.GeoIP(os.path.join('DionaeaFR/static', 'GeoIP.dat'), pygeoip.MEMORY_CACHE)

reserved_ipv4 = SubnetTree.SubnetTree()
for subnet in settings.RESERVED_IP:
	reserved_ipv4[subnet] = subnet

def protocols(request):
	return render_to_response('graphs/protocols.html')

def protocolsData(request):
	date_now = datetime.date.today() - datetime.timedelta(days=7)
	conn = Connection.objects.filter(connection_timestamp__gt=time.mktime(date_now.timetuple())).values('connection_protocol').exclude(connection_type="listen").annotate(Count("connection_protocol")).order_by('-connection_protocol__count')
	data = []
	for c in conn:
		b = {}
		b['name'] = c['connection_protocol']
		b['value'] = c['connection_protocol__count']
		data.append(b)
	return HttpResponse(json.dumps(data), mimetype="application/json")

def ports(request):
	return render_to_response('graphs/ports.html')

def portsData(request):
	date_now = datetime.date.today() - datetime.timedelta(days=7)
	conn = Connection.objects.filter(connection_timestamp__gt=time.mktime(date_now.timetuple())).values('local_port').exclude(connection_type="listen").annotate(Count("local_port")).order_by('-local_port__count')[:10]
	data = []
	for c in conn:
		b = {}
		b['name'] = c['local_port']
		b['value'] = c['local_port__count']
		data.append(b)
	return HttpResponse(json.dumps(data), mimetype="application/json")

def urls(request):
	return render_to_response('graphs/urls.html')

def urlsData(request):
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
	from django.db import connection
	cursor = connection.cursor()
	sql = U"""SELECT virustotalscans.virustotalscan_result, count(*) as num
		FROM downloads, virustotals, virustotalscans
		WHERE downloads.download_md5_hash = virustotals.virustotal_md5_hash
		AND virustotals.virustotal = virustotalscans.virustotal
		AND virustotalscans.virustotalscan_scanner = '""" + settings.ANTIVIRUS_VIRUSTOTAL + """'
		AND virustotalscans.virustotalscan_result IS NOT NULL
		GROUP BY virustotalscans.virustotalscan_result
		ORDER BY num DESC
		"""
	cursor.execute(sql)
	data = []
	for c in cursor.fetchall():
		b = {}
		b['name'] = c[0]
		b['value'] = c[1]
		data.append(b)
	return HttpResponse(json.dumps(data), mimetype="application/json")

def ips(request):
	return render_to_response('graphs/ips.html')

def ipsData(request):
	date_now = datetime.date.today() - datetime.timedelta(days=7)
	conn = Connection.objects.filter(connection_timestamp__gt=time.mktime(date_now.timetuple())).values('remote_host').exclude(remote_host="").annotate(Count("remote_host")).order_by('-remote_host__count')[:10]
	data = []
	for c in conn:
		try:
			reserved_ipv4[str(c['remote_host'])]
		except KeyError:
			b = {}
			b['name'] = c['remote_host']
			b['value'] = c['remote_host__count']
			data.append(b)
	return HttpResponse(json.dumps(data), mimetype="application/json")

def connections(request):
	return render_to_response('graphs/connections.html')

def connectionsData(request):
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
		b['day'] = str(c[2]) + '-' + str(c[1]) + '-' + str(c[0])
		b['value'] = c[3]
		data.append(b)
	data.reverse()
	return HttpResponse(json.dumps(data), mimetype="application/json")

def timeline(request):
	from django.db import connection
	cursor = connection.cursor()
	sql = u"""SELECT strftime('%%Y', connection_timestamp,'unixepoch') as 'year', strftime('%%m', connection_timestamp,'unixepoch') as 'month', count(strftime('%%m', connection_timestamp,'unixepoch')) as 'num'
			FROM connections
			GROUP BY strftime('%%Y', connection_timestamp,'unixepoch'), strftime('%%m', connection_timestamp,'unixepoch')
			ORDER BY strftime('%%Y', connection_timestamp,'unixepoch') DESC, strftime('%%m', connection_timestamp,'unixepoch') DESC
			LIMIT 12"""
	cursor.execute(sql)
	data = []
	for c in cursor.fetchall():
		b = {}
		b['year'] = c[0]
		b['month'] = str(c[1]) +'-'+ str(c[0])
		b['value'] = c[2]
		data.append(b)
	data.reverse()
	return HttpResponse(json.dumps(data), mimetype="application/json")

def connCountries(request):
	conn = Connection.objects.values('remote_host').exclude(connection_type="listen").annotate(Count("remote_host")).order_by('-remote_host__count')
	data = []
	b = defaultdict(str)
	b['UNKNOWN'] = 0
	b['RESERVED'] = 0
	for c in conn:
		ip = IPAddress(c['remote_host'])
		if ip.version == 4:
			try:
				reserved_ipv4[str(c['remote_host'])]
				if b['RESERVED']:
					b['RESERVED'] = int(b['RESERVED']) + int(c['remote_host__count'])
				else:
					b['RESERVED'] = int(c['remote_host__count'])
			except KeyError:
				cc = gi.country_name_by_addr(c['remote_host'])
				if cc != '':
					if b[cc]:
						b[cc] = int(b[cc]) + int(c['remote_host__count'])
					else:
						b[cc] = int(c['remote_host__count'])
				else:
					if b['UNKNOWN']:
						b['UNKNOWN'] = int(b['UNKNOWN']) + int(c['remote_host__count'])
					else:
						b['UNKNOWN'] = int(c['remote_host__count'])
	try:
		reserved = int(b['RESERVED'])
		del b['RESERVED']
	except KeyError:
		reserved = 0
	try:
		unknown = int(b['UNKNOWN'])
		del b['UNKNOWN']
	except KeyError:
		unknown = 0
	values = Counter(b).most_common(8)
	top = []
	for country in values:
		top.append(country[0])
	for country, count in b.iteritems():
		if country not in top:
			unknown += count
	for c in values:
		data.append({'cc':c[0], 'value':c[1]})
	data.append({'cc':'Reserved', 'value':reserved})
	data.append({'cc':'Unknown', 'value':unknown})
	return HttpResponse(json.dumps(data), mimetype="application/json")

def ipsCountries(request):
	conn = Connection.objects.values('remote_host').exclude(remote_host="").annotate(Count("remote_host")).order_by('-remote_host__count')
	data = []
	b = defaultdict(str)
	b['UNKNOWN'] = 0
	b['RESERVED'] = 0
	for c in conn:
		ip = IPAddress(c['remote_host'])
		if ip.version == 4:
			try:
				reserved_ipv4[str(c['remote_host'])]
				if b['RESERVED']:
					b['RESERVED'] = int(b['RESERVED']) + 1
				else:
					b['RESERVED'] = 1
			except KeyError:
				cc = gi.country_name_by_addr(c['remote_host'])
				if cc != '':
					if b[cc]:
						b[cc] = int(b[cc]) + 1
					else:
						b[cc] = 1
				else:
					if b['UNKNOWN']:
						b['UNKNOWN'] = int(b['UNKNOWN']) + 1
					else:
						b['UNKNOWN'] = 1
	try:
		reserved = int(b['RESERVED'])
		del b['RESERVED']
	except KeyError:
		reserved = 0
	try:
		unknown = int(b['UNKNOWN'])
		del b['UNKNOWN']
	except KeyError:
		unknown = 0
	values = Counter(b).most_common(8)
	top = []
	for country in values:
		top.append(country[0])
	for country, count in b.iteritems():
		if country not in top:
			unknown += count
	for c in values:
		data.append({'cc':c[0], 'value':c[1]})
	data.append({'cc':'Reserved', 'value':reserved})
	data.append({'cc':'Unknown', 'value':unknown})
	return HttpResponse(json.dumps(data), mimetype="application/json")
