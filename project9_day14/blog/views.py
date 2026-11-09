from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    post = {
        "title":"My second template blog",
        'discription':"Django is the  high level web framework that helps in rapid development",
        "author":None,
        "create_at":datetime(2026,1,11,4,37),
        "comments_count":5,
        "tags":["Django", "python", "Web Development"],
        "price":100,
        "normal_num":7,
    }
    return render(request, "blog/blog_details.html", {"post":post})
