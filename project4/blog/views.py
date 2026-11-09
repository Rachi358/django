from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def post_details(request, post_id):
    return HttpResponse(f'show blog_post {post_id}')

def user_profile(request,username):
    return HttpResponse(f'profile of user {username}')

def article_by_year(request, year):
    return HttpResponse(f"Articles from the year {year}")

def article_details(request, **kwargs):
    return HttpResponse(f" Articles from {kwargs}")