import django_tables2 as tables

from django_tables2.utils import A

from Web.models.download import Download


class DownloadTable(tables.Table):
    connection = tables.LinkColumn(
        'connection-detail',
        args=[A('connection')],
        verbose_name="ID"
    )

    class Meta:
        model = Download
        exclude = ("download", )
        empty_text = 'No data.'
        template = 'table.html'
        attrs = {
            'class': 'table table-hover'
        }

# vim: set expandtab:ts=4
