from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404

from django_tables2 import RequestConfig
from Web.models.connection import Connection
from Web.models.dcerpcbind import Dcerpcbind
from Web.models.dcerpcrequest import Dcerpcrequest
from Web.models.download import Download
from Web.models.emuprofile import EmuProfile
from Web.models.emuservice import EmuService
from Web.models.login import Login
from Web.models.mssqlcommand import MssqlCommand
from Web.models.mssqlfingerprint import MssqlFingerprint
from Web.models.mysqlcommand import MysqlCommand
from Web.models.offer import Offer
from Web.models.p0f import P0f
from Web.models.resolve import Resolve
from Web.models.sipcommand import SipCommand
from Web.tables.connection import ConnectionTable
from Web.forms.connection import ConnectionFilterForm
from Web.filters.connection import ConnectionFilter


def connectionIndex(request):
    connections = Connection.objects.all()
    filterQueryset = ConnectionFilter(
        request.GET,
        queryset=connections
    )
    table = ConnectionTable(
        filterQueryset
    )
    filters = ConnectionFilterForm()
    RequestConfig(
        request,
        paginate={
            "per_page": 15
        }
    ).configure(
        table
    )
    return render_to_response(
        'base.html',
        {
            'filters': filters,
            'table': table,
            'title': u'Connections'
        },
        context_instance=RequestContext(
            request
        )
    )


def connectionDetail(request, connection_id):
    try:
        length = Connection.objects.count()
        conn = Connection.objects.get(
            pk=connection_id
        )
        dcerpcbind = Dcerpcbind.objects.filter(
            connection=connection_id
        )
        dcerpcrequest = Dcerpcrequest.objects.filter(
            connection=connection_id
        )
        download = Download.objects.filter(
            connection=connection_id
        )
        emuProfile = EmuProfile.objects.filter(
            connection=connection_id
        )
        emuService = EmuService.objects.filter(
            connection=connection_id
        )
        login = Login.objects.filter(
            connection=connection_id
        )
        mssqlCommand = MssqlCommand.objects.filter(
            connection=connection_id
        )
        mssqlFingerprint = MssqlFingerprint.objects.filter(
            connection=connection_id
        )
        mysqlCommand = MysqlCommand.objects.filter(
            connection=connection_id
        )
        offer = Offer.objects.filter(
            connection=connection_id
        )
        p0f = P0f.objects.filter(
            connection=connection_id
        )
        resolve = Resolve.objects.filter(
            connection=connection_id
        )
        sipcommand = SipCommand.objects.filter(
            connection=connection_id
        )
        previous = 0
        next = 0
        if int(connection_id) > 0:
            previous = int(connection_id) - 1
        if int(connection_id) < length:
            next = int(connection_id) + 1
    except Connection.DoesNotExist:
        raise Http404
    return render_to_response(
        'connections/detail.html',
        {
            'connection': conn,
            'dcerpcbind': dcerpcbind,
            'dcerpcrequest': dcerpcrequest,
            'download': download,
            'emuProfile': emuProfile,
            'emuService': emuService,
            'login': login,
            'mssqlCommand': mssqlCommand,
            'mssqlFingerprint': mssqlFingerprint,
            'mysqlCommand': mysqlCommand,
            'offer': offer,
            'p0f': p0f,
            'resolve': resolve,
            'sipcommand': sipcommand,
            'previous': int(previous),
            'next': int(next),
            'title': str(conn)
        }
    )

# vim: set expandtab:ts=4
