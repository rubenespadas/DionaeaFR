try:
    import django_filters as filters
except ImportError:
    print "Install django-filter"
    print "\tpip install django-filter"
    pass

from Web.models.download import Download


class DownloadFilter(filters.FilterSet):
    download_url = filters.CharFilter(
        lookup_type='icontains'
    )

    download_md5_hash = filters.CharFilter(
        lookup_type='contains'
    )

    class Meta:
        model = Download
        fields = [
            'download_url',
            'download_md5_hash',
        ]

# vim: set expandtab:ts=4
