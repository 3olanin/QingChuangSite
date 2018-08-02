from django.shortcuts import render
import time
# Create your views here.
# coding:utf-8
from django.http import HttpResponse
import json
 
def index(request):
    return HttpResponse(u"欢迎光临 自强学堂!")

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

def downloadData(request):
	context = {}
	starttime = request.GET['thestarttime']
	endtime = request.GET['theendtime']
	timeArrayStart = time.strptime(starttime, "%Y-%m-%d %H:%M:%S")
	timeArrayEnd = time.strptime(endtime, "%Y-%m-%d %H:%M:%S")
	timeStampStart = int(time.mktime(timeArrayStart))
	timeStampEnd = int(time.mktime(timeArrayEnd))
	context['start'] = timeStampStart
	context['end'] = timeStampEnd
	if timeStampStart > timeStampEnd :
		return render(request, 'downloadFail.html')
	else :
		response = HttpResponse(content_type='text/plain')
		response['Content-Disposition'] = 'attachment; filename=target.txt'
		response.write("aa\n")
		for i in range(1,50000000):
			response.write("bb")
		return response
		#return render(request, 'downloadSucceed.html', context)
