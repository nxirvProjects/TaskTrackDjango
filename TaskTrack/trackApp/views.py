from django.shortcuts import render, HttpResponse


def home(response):
    return render(response, "home.html")


def kanban(response):
    return render(response, "kanban.html")


def add_task(response):
    return 0


def delete_task(response):
    return 0

def edit_task(response):
    return 0

