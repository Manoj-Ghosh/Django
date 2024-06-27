from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

'''def january(request):
    return HttpResponse(" this works ")

def february(request):
    return HttpResponse("this is feb ")

def march(request):
    return HttpResponse("this is march ")'''

monthly_challenges_dict = {
    "january": "this is january",
    "february": " this is february",
    "march": " this is march",
    "april" : "this is april",
    "may": " this is may",
    "june": "this is june"
}




def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_dict.keys())

    if month > len(months):
        return HttpResponseNotFound(" Invalid month ...")
    
    redirected_month = months[month - 1]

    challenge_text = monthly_challenges_dict[redirected_month]
    return HttpResponseRedirect("/challenges/" + redirected_month)

def monthly_challenges(request, month):

    try:
        challenge_text = monthly_challenges_dict[month]
        return HttpResponse(challenge_text)

    except:
        return HttpResponseNotFound("this month not supported...")



    '''if month == "january":
        challenge_text = " this is january"

    elif month == "february":
        challenge_text = " this is february"

    elif month == "march":
        challenge_text = " this is march"

    elif month == "april":
        challenge_text = " this is april"

    else:
        return HttpResponseNotFound("This month not supported")

    return HttpResponse(challenge_text)'''


