from django.shortcuts import render, redirect
from django.utils import timezone
def index(request):
    today = str(timezone.now()).split('-')
    context = {
        'year' : today[0],
        'month' : today[1],
    }
    return render(request, 'utilityfee/index.html', context)