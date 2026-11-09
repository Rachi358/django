from django.shortcuts import render
from django.http import HttpResponse, request

# Create your views here.
def home(request):
    return HttpResponse('Wellcome to blog home page')

def about(request):
    a = 10 + 20
    return HttpResponse(f"addition is {a}")