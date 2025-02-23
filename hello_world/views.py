from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Index function
def index (request):
    return HttpResponse("Hello, World!")
