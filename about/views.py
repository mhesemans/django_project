from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Index function
def about (request):
    return HttpResponse("Let me tell you about us.")