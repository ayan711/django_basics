from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('### This is Home Page of App1 ###')
def user(request):
    return HttpResponse('***This is the User Page of App1***')
def login(request):
    return render(request, 'App1/page.html')