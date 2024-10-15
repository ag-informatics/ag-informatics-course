from django.shortcuts import render
from django.http import HttpResponse

#Show all the fields in my farm
def index(request):
    return HttpResponse("Hello, world! You're at the farmnotes index, or 'home' page.")