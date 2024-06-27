from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

'''def january(request):
    return HttpResponse(" this works ")

def february(request):
    return HttpResponse("this is feb ")

def march(request):
    return HttpResponse("this is march ")'''

def monthly_challenges(request, month):
    challenge_text = None

    if month == "january":
        challenge_text = " this is january"

    elif month == "february":
        challenge_text = " this is february"

    elif month == "march":
        challenge_text = " this is march"

    elif month == "april":
        challenge_text = " this is april"

    else:
        return HttpResponseNotFound("This month not supported")

    return HttpResponse(challenge_text)


