from django.conf import settings
import django_tables2 as tables
from django.utils.safestring import mark_safe
from Web.models import Connection
from django_tables2_simplefilter import F
from netaddr import IPAddress
import SubnetTree
import pygeoip
import os
import datetime

gi = pygeoip.GeoIP(os.path.join('DionaeaFR/static', 'GeoIP.dat'), pygeoip.MEMORY_CACHE)

reserved_ipv4 = SubnetTree.SubnetTree()
for subnet in settings.RESERVED_IP:
	reserved_ipv4[subnet] = subnet

class getDate(tables.Column):
	def render(self, value):
		return datetime.datetime.fromtimestamp(float(value)).strftime("%d-%m-%Y %H:%M:%S")

class remoteHost(tables.Column):
	def render(self, value):
		cc = "zz"
		name = "Unknown"
		ip = IPAddress(str(value))
		if ip.version == 4:
			try:
				reserved_ipv4[str(ip)]
			except KeyError:
				cc = gi.country_code_by_addr(str(ip))
				name = gi.country_name_by_addr(str(ip))
		return mark_safe('<img class="flag" src="/static/images/flags/' + cc.lower() + '.gif" rel="tooltip" title="'+name+'" alt="'+name+'" data-placement="top"/> '+ str(ip))

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
