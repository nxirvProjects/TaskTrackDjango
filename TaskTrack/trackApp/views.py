from django.shortcuts import render, HttpResponse

# Create your views here.
def kanban(response):
    return render(response, "kanban.html")