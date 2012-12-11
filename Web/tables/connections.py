import django_tables2 as tables
from django.utils.safestring import mark_safe
from Web.models import Connection
from django_tables2_simplefilter import F
import pygeoip
import os
import datetime

gi = pygeoip.GeoIP(os.path.join('static', 'GeoIP.dat'), pygeoip.MEMORY_CACHE)

class getDate(tables.Column):
	def render(self, value):
		return datetime.datetime.fromtimestamp(float(value)).strftime("%d-%m-%Y %H:%M:%S")

class remoteHost(tables.Column):
	def render(self, value):
		cc = None
		if value:
			cc = gi.country_code_by_addr(value)
		else:
			cc = "zz"
		if cc:
			return mark_safe('<img class="flag" src="/static/images/flags/' + cc.lower() + '.gif" rel="tooltip" title="'+cc+'" alt="'+cc+'" data-placement="top"/> '+ value)
		else:
			return mark_safe('<img class="flag" src="/static/images/flags/zz.gif" rel="tooltip" title="Unknown" alt="Unknown" data-placement="top"/> '+ value)
class LinkID(tables.Column):
	def render(self, value):
		return mark_safe('<a href="/connections/' + str(value) + '">' + str(value) + '</a>')

class ConnectionsTable(tables.Table):
	connection = LinkID()
	connection_timestamp = getDate()
	connection_root = LinkID()
	connection_parent = LinkID()
	remote_host = remoteHost()
	class Meta:
		model = Connection
		attrs = {"class": "bootstrap"}
		empty_text = 'No data.'
		template = 'tables/bootstrap.html'
	filters = (
		F('connection_type','Type',values_list=(
				('accept','accept'),
				('connect','connect'),
				('listen','listen'),
				('reject','reject')
			)
		),
		F('connection_transport','Transport',values_list=(
				('TCP','tcp'),
				('UDP','udp'),
				('TLS','tls')
			)
		),
		F('connection_protocol','Protocol',values_list=(
				('xmppclient','xmppclient'),
				('smbd','smbd'),
				('remoteshell','remoteshell'),
				('pcap','pcap'),
				('mysqld','mysqld'),
				('mssqld','mssqld'),
				('mirrord','mirrord'),
				('mirrorc','mirrorc'),
				('httpd','httpd'),
				('ftpdatalisten','ftpdatalisten'),
				('ftpdata','ftpdata'),
				('ftpd','ftpd'),
				('ftpctrl','ftpctrl'),
				('epmapper','epmapper'),
				('emulation','emulation'),
				('TftpClient','TftpClient'),
				('SipSession','SipSession'),
				('SipCall','SipCall'),
				('RtpUdpStream','RtpUdpStream')
			)
		)
	)
