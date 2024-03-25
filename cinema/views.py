from django.shortcuts import render
from cinema.cinema import getCinemaInfo

# Create your views here.

def index(request):
    cinema = getCinemaInfo('My cinema')

    return render(request, 'cinema/index.html', cinema)
