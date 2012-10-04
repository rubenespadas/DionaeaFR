from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.http import Http404
from Connections.models import Download

length = len(Download.objects.all())

def index(request):
	latest_download_list = Download.objects.all().order_by('-download')
	paginator = Paginator(latest_download_list, 15)
	page = request.GET.get('page')
	try:
		latest_download_list = paginator.page(page)
	except PageNotAnInteger:
		latest_download_list = paginator.page(1)
	except EmptyPage:
		latest_download_list = paginator.page(paginator.num_pages)
	return render_to_response('downloads/index.html', {"latest_download_list": latest_download_list})

def detail(request, download_id):
    try:
       	download = Download.objects.filter(download=download_id)
        previous = 0
        next = 0
        if int(download_id) > 0:
          previous = int(download_id) - 1
        if int(download_id) < int(length):
          next = int(download_id) + 1
    except Download.DoesNotExist:
        raise Http404
    return render_to_response('downloads/detail.html',
    		{
    			'download' : download,
          		'previous' : str(previous),
          		'next' : str(next)
    		}
    	)
