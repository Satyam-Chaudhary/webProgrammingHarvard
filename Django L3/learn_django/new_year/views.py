from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
import datetime


def index(request):
    now = datetime.datetime.now()
    return render(request , 'new_year/index.html' , {
            'newyear' : now.day == 1 and now.month == 1
        })

def new(request):
    return render(request , 'new_year/index2.html')