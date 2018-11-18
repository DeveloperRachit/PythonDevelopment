from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_View(request):
    return HttpResponse("<h1>this is first view</h1>")
def second_View(request):
    return HttpResponse("<h1>this is second view</h1>")
def third_View(request):
    return HttpResponse("<h1>this is third view</h1>")    
def fourth_View(request):
    return HttpResponse("<h1>this is fourth view</h1>")
def fifth_View(request):
    return HttpResponse("<h1>this is fifth view</h1>")    