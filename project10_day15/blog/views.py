from django.shortcuts import render
from datetime import datetime

def blog_list(request):

    blogs = [
        {
            "title":"Django Basics",
            "is_feature":True,
            "Author":"Rachit"
        },

        {
            "title":"Django Advance",
            "is_feature":False,
            "Author":""
        },

        {
            "title":"Django Reast API",
            "is_feature":False,
            "Author":"Lahase"
        }
        
    ]

    context = {
        "blogs":blogs,
        "today":datetime.now(),
        "html_code": "Welcome to my page",
    }
    return render(request, 'blog/blog_list.html', context)
