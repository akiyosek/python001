#from django.shortcuts import render

# Create your views here.

# 20200418
from django.http import HttpResponse

def index(request):
   return HttpResponse("Hello, World. You're at the polls index.")