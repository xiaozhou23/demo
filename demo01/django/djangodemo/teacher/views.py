from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

def do_normalmap(request):
    #print("do normal")
    return HttpResponse("This is normalmap!")

def with_param(request, year, month):
    return HttpResponse("Year: {0} Month: {1}".format(year, month))

def do_teacher(request):
    return HttpResponse("This is a subroute!")

def do_param2(request, pn):
    return HttpResponse("Page number is {0}".format(pn))

def extraParam(request, name):
    return HttpResponse("Extra param is {0}".format(name))

def revParse(request):
    return HttpResponse("Your request url is {0}".format(reverse("askname")))