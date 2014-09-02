from django.shortcuts import render_to_response
from django.template import RequestContext

from django_tables2 import RequestConfig
from Web.models.download import Download
from Web.tables.download import DownloadTable
from Web.filters.download import DownloadFilter
from Web.forms.download import DownloadFilterForm


length = len(Download.objects.all())


def downloadIndex(request):
    downloads = Download.objects.all()
    filterQueryset = DownloadFilter(
        request.GET,
        queryset=downloads
    )
    table = DownloadTable(
        filterQueryset
    )
    filters = DownloadFilterForm()
    RequestConfig(
        request,
        paginate={
            "per_page": 12
        }
    ).configure(
        table
    )
    return render_to_response(
        'base.html',
        {
            'table': table,
            'filters': filters,
            'title': u'Downloads'
        },
        context_instance=RequestContext(
            request
        )
    )

# vim: set expandtab:ts=4
