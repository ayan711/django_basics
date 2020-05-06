from django.shortcuts import render
from django.http import HttpResponse

information = [
    {
        'Dev_Info':'About Developer',
        'created_by': 'Ayan',
        'hosted_on': 'Ubuntu'
    }
     ,
    {
        'Dev_Info':'About Developer',
        'created_by': 'Unknown',
        'hosted_on': 'Ubuntu'
    }
]
def home(request):
    return HttpResponse('### This is Home Page of App1 ###')
def user(request):
    return HttpResponse('***This is the User Page of App1***')
def login(request):
    return render(request, 'App1/page.html')
def about(request):
   context = {
       'info':information
   }
   return render(request,'App1/about.html',context)