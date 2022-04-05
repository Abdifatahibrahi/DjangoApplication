from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, "home.html")


def add(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])

    result = num1 + num2
    return render(request, "result.html", {'result': result} )