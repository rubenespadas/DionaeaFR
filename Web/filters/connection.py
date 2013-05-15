try:
	import django_filters as filters
except ImportError:
	print "Install django-filter"
	print "\tpip install django-filter"
	pass

from Web.models.connection import Connection


class ConnectionFilter(filters.FilterSet):

    connection_type = filters.CharFilter(
        lookup_type='contains'
    )

    connection_transport = filters.CharFilter(
        lookup_type='contains'
    )

    connection_protocol = filters.CharFilter(
        lookup_type='contains'
    )

    local_port = filters.NumberFilter()

    remote_port = filters.NumberFilter()

    class Meta:
        model = Connection
        fields = [
            'connection_type',
            'connection_transport',
            'connection_protocol',
            'local_port',
            'remote_port',
        ]

# vim: set expandtab:ts=4
