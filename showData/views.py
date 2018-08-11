from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from showData.models import LinePns
from showData.models import LineTxt
import time
# Create your views here.
# coding:utf-8
from django.http import HttpResponse
import json
 
def index(request):
    return HttpResponse(u"welcome!")

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(c)

def add2(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(c)

def home(request):
	#List = ['自强学堂','渲染Json到模板']
	context = {}
	context['hello'] = 'HelloWorld'
	#return render(request, 'home.html',{'List' : json.dumps(List)})
	return render(request, 'home.html',context)

def indexShow(request):
	#List = ['自强学堂','渲染Json到模板']
	context = {}
	context['hello'] = 'HelloWorld'
	#return render(request, 'home.html',{'List' : json.dumps(List)})
	return render(request, 'index.html',context)

def showdataIndex(request):
	return render(request, 'showdataIndex.html')

def showdataRule1(request):
	linepns_list = LinePns.objects.all().order_by('-c_date_stamp')
	page = request.GET.get('page',1)
	paginator = Paginator(linepns_list, 25) # Show 25 contacts per page
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	for contact in contacts:
		time_local = time.localtime(contact.c_date_stamp)
		contact.c_date_stamp= time.strftime("%Y-%m-%d %H:%M:%S",time_local)
	return render(request, 'showdataRule1.html',  {'contacts': contacts})

def downloadDataRule1(request):
	context = {}
	starttime = request.GET['thestarttime']
	endtime = request.GET['theendtime']
	timeArrayStart = time.strptime(starttime, "%Y-%m-%d %H:%M:%S")
	timeArrayEnd = time.strptime(endtime, "%Y-%m-%d %H:%M:%S")
	timeStampStart = time.mktime(timeArrayStart)
	timeStampEnd = time.mktime(timeArrayEnd)
	context['start'] = timeStampStart
	context['end'] = timeStampEnd
	if timeStampStart > timeStampEnd :
		return render(request, 'downloadFail.html')
	else :
		linepns = LinePns.objects.filter(c_date_stamp__range = (timeStampStart,timeStampEnd)).order_by('-c_date_stamp')
		response = HttpResponse(content_type='text/plain')
		response['Content-Disposition'] = 'attachment; filename=target.txt'
		#response.write("aa\n")
		for line in linepns:
			response.write(line.c_mac+",")
			response.write(line.c_imei+",")
			response.write(line.c_imsi+",")
			response.write(line.c_date+",")
			response.write(line.c_rsrp+",")
			response.write(line.c_lon+",")
			response.write(line.c_lat+",")
			response.write(line.c_isp+"\r\n")
		return response
		#return render(request, 'downloadSucceed.html', context)

def showdataRule2(request):
	linetxt_list = LineTxt.objects.all().order_by('-c_time_stamp')
	page = request.GET.get('page',1)
	paginator = Paginator(linetxt_list, 25) # Show 25 contacts per page
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	for contact in contacts:
		#time_local = time.localtime(contact.c_time_stamp)
		#contact.c_time_stamp= time.strftime("%Y-%m-%d %H:%M:%S",time_local)
		contact.c_fcn = int(contact.c_fcn)
	return render(request, 'showdataRule2.html',  {'contacts': contacts})

def downloadDataRule2(request):
	context = {}
	starttime = request.GET['thestarttime']
	endtime = request.GET['theendtime']
	timeArrayStart = time.strptime(starttime, "%Y-%m-%d %H:%M:%S")
	timeArrayEnd = time.strptime(endtime, "%Y-%m-%d %H:%M:%S")
	timeStampStart = time.mktime(timeArrayStart)
	timeStampEnd = time.mktime(timeArrayEnd)
	context['start'] = timeStampStart
	context['end'] = timeStampEnd
	if timeStampStart > timeStampEnd :
		return render(request, 'downloadFail.html')
	else :
		linetxt = LineTxt.objects.filter(c_time_stamp__range = (timeStampStart,timeStampEnd)).order_by('-c_time_stamp')
		response = HttpResponse(content_type='text/plain')
		response['Content-Disposition'] = 'attachment; filename=target.txt'
		#response.write("aa\n")
		for line in linetxt:
			response.write(line.c_imsi+"\t")
			response.write(line.c_tmsi+"\t")
			response.write(line.c_fcn+"\t")
			response.write(line.c_time+"\t")
			response.write(line.c_lon+"\t")
			response.write(line.c_lat+"\r\n")
		return response

def ResultIMSI(request):
	imsi = request.GET.get('imsi_num',0)
	linetxt_list = LineTxt.objects.filter(c_imsi = imsi).order_by('-c_time_stamp')
	page = request.GET.get('page',1)
	paginator = Paginator(linetxt_list, 25) # Show 25 contacts per page
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	for contact in contacts:
		#time_local = time.localtime(contact.c_time_stamp)
		#contact.c_time_stamp= time.strftime("%Y-%m-%d %H:%M:%S",time_local)
		contact.c_fcn = int(contact.c_fcn)
	return render(request, 'showdataRule2.html',  {'contacts': contacts})
	return response