from django.shortcuts import render
from  django.http.response import HttpResponse, Http404
# Create your views here.

def do_demoapp(request):
    return HttpResponse("It's a dempapp view")

def exception(request):
    raise Http404
    return  HttpResponse("OK")
