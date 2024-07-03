from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from django.urls import reverse

#from django.template.loader import render_to_string


# Create your views here.

'''def january(request):
    return HttpResponse(" this works ")

def february(request):
    return HttpResponse("this is feb ")

def march(request):
    return HttpResponse("this is march ")'''

def index(request):

    list_item = ""

    months = list(monthly_challenges_dict.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args= [month])
        list_item += f"<li><a href = \"{month_path}\"> {capitalized_month}</a></li>"

    response_data = f"<ul>{list_item} </ul>"
    
    #return HttpResponse(response_data)
    return render(request, "challenges/index.html", {
        "months": months
    })

monthly_challenges_dict = {
    "january": "this is january",
    "february": " this is february",
    "march": " this is march",
    "april" : "this is april",
    "may": " this is may",
    "june": "this is june",
    "december": None
}




def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_dict.keys())

    if month > len(months):
        return HttpResponseNotFound(" Invalid month ...")
    
    redirected_month = months[month - 1]
    redirect_path = reverse("month-challenge", args= [redirected_month]) # /challenges/january

    challenge_text = monthly_challenges_dict[redirected_month]
    #return HttpResponseRedirect("/challenges/" + redirected_month)

    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request, month):

    try:
        challenge_text = monthly_challenges_dict[month]
        #response_data = f"<h1> {challenge_text} </h1>"
        return render(request, "challenges/challenge.html", {
            "text" : challenge_text,
            "month_name": month.capitalize()
        })
    
        #response_data = render_to_string("challenges/challenge.html")
        #return HttpResponse(response_data)

    except:
        return HttpResponseNotFound("<h1>this month not supported...</h1>")



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


