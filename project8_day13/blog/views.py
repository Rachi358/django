from django.shortcuts import render
from datetime import datetime
# Create your views here.

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def home(request):
    context = {
        "name" : 'Rachit Lahase',
        "age" : 22,
        "skill": ['python', 'django', 'react'],
        "user": User("Lahase", 23),
        "blog":{
            "title": "Django Template intro",
            "content" : "<b> This is he bold </b>",
            "created_at" : datetime(2025,8,18,10,30), #Year/Month/Day/Hour/Min
            "author":{
                "name": "Rachit Lahase"
            },
        },
        "empty_value": None

    }

    return render(request, "home.html", context)