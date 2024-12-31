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

def myfirstpage(request):
    return render(request,'index.html')

def mysecondpage(request):
    return render(request,'second.html')

def mythirdpage(request):
    var = 'hello, world!'
    greeting = 'Hello How are you...?'
    fruits = ['apple', 'banana', 'mango']
    num1, num2 = 16, 15
    ans = num1 > num2
    print(ans)
    
    mydictionary = {
               "var":var,
               "msg": greeting,
               "myfruits" : fruits,
               "num1":num1,
               "num2":num2,
               "ans":ans
    }
    return render(request, 'third.html', context=mydictionary)

def myimagepage(request):
    return render(request,'imagepage.html')

def myimagepage2(request):
    return render(request, 'imagepage2.html')

def myimagepage3(request,imagename):
    myimagename = str(imagename);
    myimagename = myimagename.lower();
    print(myimagename)
    if myimagename == 'django':
        var = True
    elif myimagename == 'python':
        var = False
    mydictionary = {
        "var":var
    }
    return render(request, 'imagepage3.html', context=mydictionary)

def myform(request):
    return render(request, 'myform.html')

def submitmyform(request):
    mytext = request.POST.get('mytext', None)  # Get 'mytext', default to None if missing
    mytextarea = request.POST.get('mytextarea', None)  # Get 'mytextarea', default to None if missing

    if mytext is None or mytextarea is None:
        return JsonResponse({"status": "error", "message": "Missing form data."}, status=400)

    mydictionary = {
        "var1": mytext,
        "var2": mytextarea,
        "method": request.method
    }
    return JsonResponse(mydictionary)