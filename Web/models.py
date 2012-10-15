from django.db import models
import datetime
import pygeoip
import os


gi = pygeoip.GeoIP(os.path.join('static', 'GeoIP.dat'), pygeoip.MEMORY_CACHE)

class Connection(models.Model):
    connection = models.IntegerField(primary_key=True, blank=True, verbose_name='ID')
    connection_type = models.TextField(blank=True, verbose_name='Type')
    connection_transport = models.TextField(blank=True, verbose_name='Transport')
    connection_protocol = models.TextField(blank=True, verbose_name='Protocol')
    connection_timestamp = models.IntegerField(blank=True, verbose_name='Date')
    connection_root = models.IntegerField(blank=True, verbose_name='Root')
    connection_parent = models.IntegerField(blank=True, verbose_name='Parent')
    local_host = models.TextField(blank=True, verbose_name='Sensor')
    local_port = models.IntegerField(blank=True, verbose_name='DST Port')
    remote_host = models.TextField(blank=True, verbose_name='Attacker')
    remote_hostname = models.TextField(blank=True, verbose_name='Hostname')
    remote_port = models.IntegerField(blank=True, verbose_name='SRC Port')
    class Meta:
        db_table = u'connections'
        ordering = ['-connection']
        verbose_name_plural = "Connections"
    def __str__(self):
        return str(self.connection)
    def getDate(self):
        return datetime.datetime.fromtimestamp(float(self.connection_timestamp)).strftime("%d-%m-%Y %H:%M:%S")
    def getTrace(self):
        conns = Connection.objects.filter(connection_root=self.connection_root).order_by('connection')
        return conns
    def getCC(self):
        cc = None
        if self.remote_host:
            cc = gi.country_code_by_addr(self.remote_host)
        else:
            cc = "zz"
        if cc:
            return cc.lower()
        else:
            return "zz"
    def getRemoteHost(self):
        if self.remote_host == "":
            return '127.0.0.1'
        else:
            return self.remote_host

class Dcerpcbind(models.Model):
    dcerpcbind = models.IntegerField(primary_key=True, blank=True)
    connection = models.IntegerField(blank=True)
    dcerpcbind_uuid = models.TextField(blank=True)
    dcerpcbind_transfersyntax = models.TextField(blank=True)
    class Meta:
        db_table = u'dcerpcbinds'
        ordering = ['-dcerpcbind']
        verbose_name_plural = "Dcerpcbinds"
    def __str__(self):
        return str(self.dcerpcbind)

class Dcerpcrequest(models.Model):
    dcerpcrequest = models.IntegerField(primary_key=True, blank=True)
    connection = models.IntegerField(blank=True)
    dcerpcrequest_uuid = models.TextField(blank=True)
    dcerpcrequest_opnum = models.IntegerField(blank=True)
    class Meta:
        db_table = u'dcerpcrequests'
        ordering = ['-dcerpcrequest']
        verbose_name_plural = "Dcerpcrequests"
    def __str__(self):
        return str(self.dcerpcrequest)
    def getOpsName(self):
        ops = Dcerpcserviceop.objects.filter(dcerpcserviceop_opnum=self.dcerpcrequest_opnum)
        data = '<ul class="unstyled">'
        for op in  ops:
            data = data + '<li>' + op.getName() + '</li>'
        data += '</ul>'
        return data
    def getOpsVuln(self):
        ops = Dcerpcserviceop.objects.filter(dcerpcserviceop_opnum=self.dcerpcrequest_opnum)
        data = '<ul class="unstyled">'
        for op in  ops:
            data = data + '<li><a href="https://technet.microsoft.com/en-us/security/bulletin/' + op.getVuln() + '">' + op.getVuln() + '</a></li>'
        data += '</ul>'
        return data
    def getService(self):
        ops = Dcerpcserviceop.objects.filter(dcerpcserviceop_opnum=self.dcerpcrequest_opnum)
        data = '<ul class="unstyled">'
        for op in  ops:
            data = data + '<li>' + op.getService() + '</li>'
        data += '</ul>'
        return data

class Dcerpcserviceop(models.Model):
    dcerpcserviceop = models.IntegerField(primary_key=True, blank=True)
    dcerpcservice = models.IntegerField(blank=True)
    dcerpcserviceop_opnum = models.IntegerField(blank=True)
    dcerpcserviceop_name = models.TextField(blank=True)
    dcerpcserviceop_vuln = models.TextField(blank=True)
    class Meta:
        db_table = u'dcerpcserviceops'
        ordering = ['-dcerpcserviceop']
        verbose_name_plural = "Dcerpcserviceops"
    def __str__(self):
        return str(self.dcerpcserviceop)
    def getName(self):
        return str(self.dcerpcserviceop_name)
    def getVuln(self):
        if self.dcerpcserviceop_vuln:
            vuln = self.dcerpcserviceop_vuln.split('-')
            if vuln[1][:1] != '0':
                return str(vuln[0] + '-0' + vuln[1])
            else:
                return self.dcerpcserviceop_vuln
        else:
            return self.dcerpcserviceop_vuln
    def getService(self):
        srv = Dcerpcservice.objects.get(dcerpcservice=self.dcerpcservice)
        return srv.getName()

class Dcerpcservice(models.Model):
    dcerpcservice = models.IntegerField(primary_key=True, blank=True)
    dcerpcservice_uuid = models.TextField(unique=True, blank=True)
    dcerpcservice_name = models.TextField(blank=True)
    class Meta:
        db_table = u'dcerpcservices'
        ordering = ['-dcerpcservice']
        verbose_name_plural = "Dcerpcservices"
    def __str__(self):
        return str(self.dcerpcservice)
    def getName(self):
        return str(self.dcerpcservice_name)

class Download(models.Model):
    download = models.IntegerField(primary_key=True, blank=True, verbose_name='ID')
    connection = models.IntegerField(blank=True, verbose_name='Connection')
    download_url = models.TextField(blank=True, verbose_name='URL')
    download_md5_hash = models.TextField(blank=True, verbose_name='MD5')
    class Meta:
        db_table = u'downloads'
        ordering = ['-download']
        verbose_name_plural = "Downloads"
    def __str__(self):
        return str(self.download)
    def getReport(self):
        vtr = Virustotal.objects.filter(virustotal_md5_hash=self.download_md5_hash).order_by('-virustotal')[:1]
        return vtr

class EmuProfile(models.Model):
    emu_profile = models.IntegerField(primary_key=True, blank=True)
    connection = models.IntegerField(blank=True)
    emu_profile_json = models.TextField(blank=True)
    class Meta:
        db_table = u'emu_profiles'
        ordering = ['-emu_profile']
        verbose_name_plural = "EmuProfiles"
    def __str__(self):
        return str(self.emu_profile)

class EmuService(models.Model):
    emu_serivce = models.IntegerField(primary_key=True, blank=True)
    connection = models.IntegerField(blank=True)
    emu_service_url = models.TextField(blank=True)
    class Meta:
        db_table = u'emu_services'
        ordering = ['-emu_serivce']
        verbose_name_plural = "EmuServices"
    def __str__(self):
        return str(self.emu_serivce)

class EmuServiceOld(models.Model):
    emu_serivce = models.IntegerField(primary_key=True, blank=True)
    connection = models.IntegerField(blank=True)
    emu_service_url = models.TextField(blank=True)
    class Meta:
        db_table = u'emu_services_old'
        ordering = ['-emu_serivce']
        verbose_name_plural = "EmuServicesOld"
    def __str__(self):
        return self.emu_serivce

class Login(models.Model):
    login = models.IntegerField(primary_key=True, blank=True)
    connection = models.IntegerField(blank=True)
    login_username = models.TextField(blank=True)
    login_password = models.TextField(blank=True)
    class Meta:
        db_table = u'logins'
        ordering = ['-login']
        verbose_name_plural = "Logins"
    def __str__(self):
        return str(self.login)

class MssqlCommand(models.Model):
    mssql_command = models.IntegerField(primary_key=True, blank=True)
    connection = models.IntegerField(blank=True)
    mssql_command_status = models.TextField(blank=True)
    mssql_command_cmd = models.TextField(blank=True)
    class Meta:
        db_table = u'mssql_commands'
        ordering = ['-mssql_command']
        verbose_name_plural = "MssqlCommands"
    def __str__(self):
        return str(self.mssql_command)

class MssqlFingerprint(models.Model):
    mssql_fingerprint = models.IntegerField(primary_key=True, blank=True)
    connection = models.IntegerField(blank=True)
    mssql_fingerprint_hostname = models.TextField(blank=True)
    mssql_fingerprint_appname = models.TextField(blank=True)
    mssql_fingerprint_cltintname = models.TextField(blank=True)
    class Meta:
        db_table = u'mssql_fingerprints'
        ordering = ['-mssql_fingerprint']
        verbose_name_plural = "MssqlFingerprints"
    def __str__(self):
        return str(self.mssql_fingerprint)

class MysqlCommandArg(models.Model):
    mysql_command_arg = models.IntegerField(primary_key=True, blank=True)
    mysql_command = models.IntegerField(blank=True)
    mysql_command_arg_index = models.TextField()
    mysql_command_arg_data = models.TextField()
    class Meta:
        db_table = u'mysql_command_args'
        ordering = ['-mysql_command_arg']
        verbose_name_plural = "MysqlCommandArgs"
    def __str__(self):
        return str(self.mysql_command_arg)
    def getData(self):
        return str(self.mysql_command_arg_data)

class MysqlCommandOp(models.Model):
    mysql_command_op = models.IntegerField(primary_key=True, blank=True)
    mysql_command_cmd = models.IntegerField(unique=True)
    mysql_command_op_name = models.TextField()
    class Meta:
        db_table = u'mysql_command_ops'
        ordering = ['-mysql_command_op']
        verbose_name_plural = "MysqlCommandOps"
    def __str__(self):
        return str(self.mysql_command_op)
    def getName(self):
        return str(self.mysql_command_op_name)

class MysqlCommand(models.Model):
    mysql_command = models.IntegerField(primary_key=True, blank=True)
    connection = models.IntegerField(blank=True)
    mysql_command_cmd = models.TextField()
    class Meta:
        db_table = u'mysql_commands'
        ordering = ['-mysql_command']
        verbose_name_plural = "MysqlCommands"
    def __str__(self):
        return str(self.mysql_command)
    def getOps(self):
        ops = MysqlCommandOp.objects.get(mysql_command_cmd=self.mysql_command_cmd)
        return ops.getName()
    def getArgs(self):
        args = MysqlCommandArg.objects.get(mysql_command=self.mysql_command)
        return args.getData()

class Offer(models.Model):
    offer = models.IntegerField(primary_key=True, blank=True)
    connection = models.IntegerField(blank=True)
    offer_url = models.TextField(blank=True)
    class Meta:
        db_table = u'offers'
        ordering = ['-offer']
        verbose_name_plural = "Offers"
    def __str__(self):
        return str(self.offer)

class P0f(models.Model):
    p0f = models.IntegerField(primary_key=True, blank=True)
    connection = models.IntegerField(blank=True)
    p0f_genre = models.TextField(blank=True)
    p0f_link = models.TextField(blank=True)
    p0f_detail = models.TextField(blank=True)
    p0f_uptime = models.IntegerField(blank=True)
    p0f_tos = models.TextField(blank=True)
    p0f_dist = models.IntegerField(blank=True)
    p0f_nat = models.IntegerField(blank=True)
    p0f_fw = models.IntegerField(blank=True)
    class Meta:
        db_table = u'p0fs'
        ordering = ['-p0f']
        verbose_name_plural = "P0Fs"
    def __str__(self):
        return str(self.p0f)

class Resolve(models.Model):
    resolve = models.IntegerField(primary_key=True, blank=True)
    connection = models.IntegerField(blank=True)
    resolve_hostname = models.TextField(blank=True)
    resolve_type = models.TextField(blank=True)
    resolve_result = models.TextField(blank=True)
    class Meta:
        db_table = u'resolves'
        ordering = ['-resolve']
        verbose_name_plural = "Resolves"
    def __str__(self):
        return str(self.resolve)

class SipAddr(models.Model):
    sip_addr = models.IntegerField(primary_key=True, blank=True)
    sip_command = models.IntegerField(blank=True)
    sip_addr_type = models.TextField(blank=True)
    sip_addr_display_name = models.TextField(blank=True)
    sip_addr_uri_scheme = models.TextField(blank=True)
    sip_addr_uri_user = models.TextField(blank=True)
    sip_addr_uri_password = models.TextField(blank=True)
    sip_addr_uri_host = models.TextField(blank=True)
    sip_addr_uri_port = models.TextField(blank=True)
    class Meta:
        db_table = u'sip_addrs'
        ordering = ['-sip_addr']
        verbose_name_plural = "SipAddrs"
    def __str__(self):
        return str(self.sip_addr)
    def getData(self):
        return '<li><b>' + str(self.sip_addr_type) + ':</b> ' + str(self.sip_addr_display_name) + ' ' + str(self.sip_addr_uri_scheme) +':' + str(self.sip_addr_uri_user) + '@' + str(self.sip_addr_uri_host) + ':' + str(self.sip_addr_uri_port) + '</li>'

class SipCommand(models.Model):
    sip_command = models.IntegerField(primary_key=True, blank=True)
    connection = models.IntegerField(blank=True)
    sip_command_method = models.TextField(blank=True)
    sip_command_call_id = models.TextField(blank=True)
    sip_command_user_agent = models.TextField(blank=True)
    sip_command_allow = models.IntegerField(blank=True)
    class Meta:
        db_table = u'sip_commands'
        ordering = ['-sip_command']
        verbose_name_plural = "SipCommands"
    def __str__(self):
        return str(self.sip_command)
    def getAddr(self):
        addrs = SipAddr.objects.filter(sip_command=self.sip_command)
        data = '<ul class="unstyled">'
        for addr in  addrs:
            data = data + addr.getData()
        data += '</ul>'
        return data
    def getData(self):
        cdat = SipSdpConnectiondata.objects.get(sip_command=self.sip_command)
        return cdat.getData()
    def getMedia(self):
        media = SipSdpMedia.objects.get(sip_command=self.sip_command)
        return media.getData()

class SipSdpConnectiondata(models.Model):
    sip_sdp_connectiondata = models.IntegerField(primary_key=True, blank=True)
    sip_command = models.IntegerField(blank=True)
    sip_sdp_connectiondata_nettype = models.TextField(blank=True)
    sip_sdp_connectiondata_addrtype = models.TextField(blank=True)
    sip_sdp_connectiondata_connection_address = models.TextField(blank=True)
    sip_sdp_connectiondata_ttl = models.TextField(blank=True)
    sip_sdp_connectiondata_number_of_addresses = models.TextField(blank=True)
    class Meta:
        db_table = u'sip_sdp_connectiondatas'
        ordering = ['-sip_sdp_connectiondata']
        verbose_name_plural = "SipSdpConnectiondatas"
    def __str__(self):
        return str(self.sip_sdp_connectiondata)
    def getData(self):
        data = '<ul class="unstyled">'
        data += '<li><b>NetType:</b> ' + str(self.sip_sdp_connectiondata_nettype) + '</li>'
        data += '<li><b>AddrType:</b> ' + str(self.sip_sdp_connectiondata_addrtype) + '</li>'
        data += '<li><b>Addresses:</b> ' + str(self.sip_sdp_connectiondata_connection_address) + '</li>'
        data += '<li><b>TTL:</b> ' + str(self.sip_sdp_connectiondata_ttl) + '</li>'
        data += '<li><b>Num Addrs:</b> ' + str(self.sip_sdp_connectiondata_number_of_addresses) + '</li>'
        data += '</ul>'
        return data

class SipSdpMedia(models.Model):
    sip_sdp_media = models.IntegerField(primary_key=True, blank=True)
    sip_command = models.IntegerField(blank=True)
    sip_sdp_media_media = models.TextField(blank=True)
    sip_sdp_media_port = models.TextField(blank=True)
    sip_sdp_media_number_of_ports = models.TextField(blank=True)
    sip_sdp_media_proto = models.TextField(blank=True)
    class Meta:
        db_table = u'sip_sdp_medias'
        ordering = ['-sip_sdp_media']
        verbose_name_plural = "SipSdpMedias"
    def __str__(self):
        return str(self.sip_sdp_media)
    def getData(self):
        return '<ul class="unstyled"><li><b>' + str(self.sip_sdp_media_media) + ':</b> ' + str(self.sip_sdp_media_proto) +':' + str(self.sip_sdp_media_port) + '</li></ul>'

class SipSdpOrigin(models.Model):
    sip_sdp_origin = models.IntegerField(primary_key=True, blank=True)
    sip_command = models.IntegerField(blank=True)
    sip_sdp_origin_username = models.TextField(blank=True)
    sip_sdp_origin_sess_id = models.TextField(blank=True)
    sip_sdp_origin_sess_version = models.TextField(blank=True)
    sip_sdp_origin_nettype = models.TextField(blank=True)
    sip_sdp_origin_addrtype = models.TextField(blank=True)
    sip_sdp_origin_unicast_address = models.TextField(blank=True)
    class Meta:
        db_table = u'sip_sdp_origins'
        ordering = ['-sip_sdp_origin']
        verbose_name_plural = "SipSdpOrigins"
    def __str__(self):
        return str(self.sip_sdp_origin)

class SipVia(models.Model):
    sip_via = models.IntegerField(primary_key=True, blank=True)
    sip_command = models.IntegerField(blank=True)
    sip_via_protocol = models.TextField(blank=True)
    sip_via_address = models.TextField(blank=True)
    sip_via_port = models.TextField(blank=True)
    class Meta:
        db_table = u'sip_vias'
        ordering = ['-sip_via']
        verbose_name_plural = "SipVias"
    def __str__(self):
        return str(self.sip_via)

class Virustotal(models.Model):
    virustotal = models.IntegerField(primary_key=True, blank=True)
    virustotal_md5_hash = models.TextField()
    virustotal_timestamp = models.IntegerField()
    virustotal_permalink = models.TextField()
    class Meta:
        db_table = u'virustotals'
        ordering = ['-virustotal']
        verbose_name_plural = "Virustotals"
    def __str__(self):
        return str(self.virustotal)
    def getUrl(self):
        return str(self.virustotal_permalink)
    def getDate(self):
        return datetime.datetime.fromtimestamp(float(self.virustotal_timestamp)).strftime("%d-%m-%Y %H:%M:%S")
    def getResult(self):
        result = Virustotalscan.objects.get(virustotal=self.virustotal,virustotalscan_scanner="Microsoft")
        if result.getVirusName() == "None":
            result = Virustotalscan.objects.get(virustotal=self.virustotal,virustotalscan_scanner="Sophos")
        return result.getVirusName()

class Virustotalscan(models.Model):
    virustotalscan = models.IntegerField(primary_key=True, blank=True)
    virustotal = models.IntegerField()
    virustotalscan_scanner = models.TextField()
    virustotalscan_result = models.TextField(blank=True)
    class Meta:
        db_table = u'virustotalscans'
        ordering = ['-virustotalscan']
        verbose_name_plural = "Virustotalscans"
    def __str__(self):
        return str(self.virustotalscan)
    def getVirusName(self):
        return str(self.virustotalscan_result)
