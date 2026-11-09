from django.shortcuts import render

def home(request):
    return render(request, "base.html")

def blog(request):
    student_list = [
        {"name":"Rachit", "course":"Python"},
        {"name":"Adity", "course":"Data Science"},
        {"name":"Nikhil", "course":"Treding"}
    ]
    return render(request, "blog.html", {'students' : student_list})
