#from django.shortcuts import render

# Create your views here.

# 20200418
from django.http import HttpResponse

def index(request):
   return HttpResponse("Hello, World. You're at the polls index.")


def detail(request, question_id):
   return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_Id):
   response = "You're looking at the results of question %s."
   return HttpResponse(response % question_id)

def vote(request, questionid):
   return HttpResponse("You're voting on question %s." % question_id)
