from django.shortcuts import render_to_response
from django.db.models import Count
from Web.models import Connection
import re
import pygeoip
import time
import datetime
import codecs
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

gi = pygeoip.GeoIP(os.path.join('static', 'GeoIP.dat'), pygeoip.MEMORY_CACHE)
gic = pygeoip.GeoIP(os.path.join('static', 'GeoLiteCity.dat'), pygeoip.STANDARD)

def countries(request):
	date_now = datetime.date.today() - datetime.timedelta(days=7)
	conn = Connection.objects.filter(connection_timestamp__gt=time.mktime(date_now.timetuple())).values('remote_host')
	data = {}
	for c in conn:
		if(re.match("(^[2][0-5][0-5]|^[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})$",c['remote_host']) != None):
			cc = gi.country_code_by_addr(c['remote_host'])
			if cc != "":
				try:
					data[cc] += 1
				except:
					data[cc] = 1
	var = "var gdpData = {"
	for country in data:
		var = var + '"' + country +'":' + str(data[country]) + ','
	var = var.rstrip(',') + "};"
	return render_to_response('maps/countries.html',
		{
			'cc' : var
		}
	)

def attackers(request):
	date_now = datetime.date.today() - datetime.timedelta(days=7)
	conn = Connection.objects.filter(connection_timestamp__gt=time.mktime(date_now.timetuple())).values('remote_host')
	var = "var gdpData = ["
	counts = {}
	for c in conn:
		if(re.match("(^[2][0-5][0-5]|^[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})$",c['remote_host']) != None):
			try:
				counts[c['remote_host']] += 1
			except:
				counts[c['remote_host']] = 1
	for c in counts:
		if(re.match("(^[2][0-5][0-5]|^[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})$",c) != None):
			cc = gic.record_by_addr(c)
			if cc != None:
				try:
					var = var + "{latLng:[" + str(cc['latitude']) + "," + str(cc['longitude']) + "], count:'" + str(counts[c]).decode('iso-8859-1', 'ignore').encode('utf-8','ignore') + "',host:'" + str(c)+"'},"
				except:
					var = var + "{latLng:[" + str(cc['latitude']) + "," + str(cc['longitude']) + "], count:'" + str(counts[c]) + "',host:'" + str(c)+"'},"
	var = var.rstrip(',') + "];"
	return render_to_response('maps/attackers.html',
		{
			'attackers' : var
		}
	)