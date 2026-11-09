from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Blog Home")


def about(request):
    return HttpResponse("Blog About")



# def post_details(request,post_id):
#     return HttpResponse(f"<h1> Show post{post_id} </h1>")


# def user_profile(request,username):
#     return HttpResponse(f"<h1> Profile of user: {username} </h1>")