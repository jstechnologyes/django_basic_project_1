from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render (request,'home.html',{'name':'hadi'})


def add(request):

    va1=int(request.POST['num1'])
    va2=int(request.POST['num2'])
    res=va1+va2

    return render(request, 'result.html',{'result':res})
