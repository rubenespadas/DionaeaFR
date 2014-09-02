import django_tables2 as tables

from django_tables2.utils import A

from Web.models.connection import Connection

from Web.columns.base import UnixToDate
from Web.columns.base import FormatIP


class ConnectionTable(tables.Table):
    connection = tables.LinkColumn(
        'connection-detail',
        args=[A('pk')],
        verbose_name=u'ID'
    )

    connection_timestamp = UnixToDate(
        verbose_name=u'Date'
    )

    connection_root = tables.LinkColumn(
        'connection-detail',
        args=[A('pk')],
        verbose_name=u'Root'
    )

    connection_parent = tables.LinkColumn(
        'connection-detail',
        args=[A('pk')],
        verbose_name=u'parent'
    )

    local_host = FormatIP(
        verbose_name=u'Sensor'
    )

    remote_host = FormatIP(
        verbose_name=u'Attacker'
    )

    class Meta:
        model = Connection
        empty_text = 'No data.'
        template = 'table.html'
        sequence = (
            'connection',
            'connection_type',
            'connection_transport',
            'connection_protocol',
            'connection_timestamp',
            'connection_root',
            'connection_parent',
            'local_host',
            'local_port',
            'remote_host',
            'remote_hostname',
            'remote_port',
        )
        attrs = {
            'class': 'table table-hover table-condensed'
        }

# vim: set expandtab:ts=4
