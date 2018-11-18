from django.shortcuts import render
from django.http import HttpResponse

def greeting_view(request):
    return HttpResponse('<h1>Hello Friend Good Morning have a nice day</h1>')

'''Create your views here.
 def index(request):
     return HttpResponse("<h1>Welcome To django application</h1")
'''
'''
def index(request):
     date=datetime.datetime.now()
     s='<h1>The Current Date and Time at Server is:' +str(date)+ '</h1>'
     return HttpResponse(s)

def good_morning_view(request):
    return HttpResponse('<h1>Hello friend Good morning</h1>')


def good_evening_view(request):
    return HttpResponse('<h1>Hello friend Good evening</h1>')

def good_afternoon_view(request):
    return HttpResponse('<h1>Hello friend Good afternoon</h1>')     
    '''
