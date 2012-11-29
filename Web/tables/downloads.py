import django_tables2 as tables
from django.utils.safestring import mark_safe
from web.models import Download
from django_tables2_simplefilter import F

class LinkID(tables.Column):
	def render(self, value):
		return mark_safe('<a href="/connections/' + str(value) + '">' + str(value) + '</a>')

class DownloadsTable(tables.Table):
	connection = LinkID()
	class Meta:
		model = Download
		exclude = ("download", )
		attrs = {"class": "bootstrap"}
		empty_text = 'No data.'
		template = 'tables/bootstrap.html'
