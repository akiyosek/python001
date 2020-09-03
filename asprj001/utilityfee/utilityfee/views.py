from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Utilityfee

def index(request):
    today = str(timezone.now()).split('-')
    utilityfee = Utilityfee.objects.all()
    context = {
        'year' : today[0],
        'month' : today[1],
    }
    return render(request, 'utilityfee/index.html', context)