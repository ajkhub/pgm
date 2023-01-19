from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import place
from .models import team


# Create your views here.

def index(request):
    obj = place.objects.all()
    t1 = team.objects.all()
    return render(request, "index.html", {'result': obj, 'res': t1})


# def about(request):
#     return render(request,'about.html')


