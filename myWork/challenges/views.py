from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def january(request):
    return HttpResponse(" this works ")

def february(request):
    return HttpResponse("this is feb ")

def march(request):
    return HttpResponse("this is march ")

