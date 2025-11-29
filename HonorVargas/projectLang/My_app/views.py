from django.shortcuts import render

def index(request):
    projects = [
        {"title": "Project 1", "desc": "Description 1", "image": "img/project1.jpg"},
        {"title": "Project 2", "desc": "Description 2", "image": "img/project2.jpg"},
        # Add more projects here as needed
    ]
    return render(request, "My_app/index.html", {"projects": projects})
