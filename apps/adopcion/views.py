from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Epalmi pana ")

def epa(request):
    return HttpResponse("Epale xd")
