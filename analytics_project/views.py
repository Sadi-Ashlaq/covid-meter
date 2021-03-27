from django.shortcuts import render, redirect
from .models import Country
from .resources import CountryResource
from django.db.models import Sum, Avg, Max
from django.http import JsonResponse
from django.db.models import Sum , Count, Avg
from tablib import Dataset
from django.contrib import messages
import sweetify
from django.contrib.auth import authenticate, login, logout
import time
import math








# Create your views here.

def index(request):

    if request.user.is_authenticated:
        context = {
        "countries" : Country.objects.all(),
        "topten" : Country.objects.order_by('-Total_Cases')[:10],
        "totalCasesSum" : Country.objects.aggregate(Sum('Total_Cases')),
        "totalDeathsSum" : Country.objects.aggregate(Sum('Total_Deaths')),
        "totalCasesCount" : Country.objects.aggregate(Count('Total_Deaths')),
        }
        return render(request, 'analytics_project/partials/base.html' , context)
    else:
        return redirect ('/')


def landing(request):
   
    
       return render(request, 'analytics_project/landing.html')


def simple_upload(request):
    
    context = {
        "countries" : Country.objects.all(),
        "topten" : Country.objects.order_by('-Total_Cases')[:10],
        "totalCasesSum" : Country.objects.aggregate(Sum('Total_Cases')),
        "totalCasesCount" : Country.objects.aggregate(Count('Total_Cases')),
        "totalDeathsSum" : Country.objects.aggregate(Sum('Total_Deaths')),
    }

    start_time = time.time()

    
    if request.method == 'POST':
        country_resource = CountryResource()
        dataset = Dataset()
        new_countries = request.FILES['myfile']


        if not new_countries.name.endswith("xlsx"):

            messages.error(request, "Wrong Format for " +  new_countries.name)
            return redirect ('/dashboard')
            # sweetify.info(self.request, 'Message sent', button='Ok', timer=3000)

            
            


        imported_data = dataset.load(new_countries.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	# print(data[1])
        	value = Country(
        		data[0],
        		data[1],
        		 data[2],
        		 data[3],
        		 data[4],
        		 data[5],
        		)
        	value.save()  

    duration = ((time.time() - start_time))
    string_duration = str(duration)

    
    messages.success(request,   new_countries.name +" Successfully Added, it was executed in " +  string_duration + " seconds")
    return redirect ('/dashboard')




def delete(request, id):
    countries =  Country.objects.get(id=id)
    countries.delete()
    return redirect ('/dashboard')


def update(request, id):
    countries =  Country.objects.get(id=id)
    countries.Country = request.POST['country']  # change field
    countries.Total_Cases = request.POST['total_cases']  # change field
    countries.New_Cases = request.POST['new_cases']  # change field
    countries.Total_Deaths = request.POST['total_death']  # change field
    countries.New_Deaths = request.POST['new_death']  # change field
    countries.save()
    return redirect ('/dashboard')



def login_form(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        return render(request, 'analytics_project/partials/login2.html' )




def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect ('/dashboard')



    else:
        messages.error(request, "Invalid Credentials")
        return redirect ('/login')
        # Return an 'invalid login' error message.
        ...


def logout_view(request):
    logout(request)
    return redirect ('/login')

    # Redirect to a success page.




# def covid_chart(request):
#     labels = []
#     data = []

#     queryset = Country.objects.values('Total_Cases').annotate(Total_Cases=Sum('Total_Cases')).order_by('-Total_Cases')
#     for entry in queryset:
#         labels.append(entry['Country'])
#         data.append(entry['Total_Cases'])
    
#     return JsonResponse(data={
#         'labels': labels,
#         'data': data,
#     })

