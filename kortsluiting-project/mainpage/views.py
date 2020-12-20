from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'mainpage/home.html')

def tickets(request):
    return render(request, 'mainpage/tickets.html')

def about(request):
    return render(request, 'mainpage/about.html')

def ticket_error(request):
    return render(request, 'mainpage/ticket_error')
