from django.shortcuts import render, redirect
from .models import Missing_Person


# Create your views here.

def addPageView(request):
    if request.method == 'POST' :
        date_missing = request.POST['date_missing']
        lastName = request.POST['lastName']
        firstName = request.POST['firstName']
        age_at_missing = request.POST['age_at_missing']
        city = request.POST['city']
        state = request.POST['state']
        gender = request.POST['gender']
        race = request.POST['race']

        new_person = Missing_Person()
        new_person.date_missing = date_missing
        new_person.lastName = lastName
        new_person.firstName = firstName
        new_person.age_at_missing = age_at_missing
        new_person.city = city
        new_person.state = state
        new_person.gender = gender
        new_person.race = race

        new_person.save()

        return redirect('table') 
    else:
        return render(request, 'missingpersonsapp/add.html')

def homePageView(request):
    return render(request, 'missingpersonsapp/home.html')

def resourcesPageView(request):
    return render(request, 'missingpersonsapp/resources.html')

def searchPageView(request):
    try: 
       firstName = request.GET['firstName']
       people = Missing_Person.objects.filter(firstName=firstName)
    except:
        people = Missing_Person.objects.all()

    context = {
        'people' : people
    }
    return render(request, 'missingpersonsapp/search.html', context)

def tablePageView(request):
    db_missingpersons = Missing_Person.objects.all()
    context = {
        "missingpersons" : db_missingpersons
        }
    return render(request, 'missingpersonsapp/table.html', context)