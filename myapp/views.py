from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello world")
def myfunctionabout(request):
    return HttpResponse("I am Jabin Tasmin Anny")

def add(request,a,b):
    return HttpResponse(a+b)

def intro(request,name,age):
    mydictionary = {
        "name":name,
        "age":age
    }
    return JsonResponse(mydictionary)

