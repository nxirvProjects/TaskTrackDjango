from django.shortcuts import render, HttpResponse
from .models import Task, Label
from .forms import AddTaskForm, AddLabelForm
from django.forms.models import model_to_dict


def home(response):
    return render(response, "home.html")


def view_labels(response):
    labels = {}
    return render(response, "view_labels.html", {"labels": labels})


def add_labels(response):
    return 0


def kanban(response):
    all_tasks = Task.objects.all().values()
    print(all_tasks)
    tasks = []
    for i in all_tasks:
        tasks.append(i)

    print(tasks)

    return render(response, "kanban.html", {"tasks": tasks})


# Add a task to the database
def add_task(response):
    if response.method == 'POST':
        form = AddTaskForm(response.POST)  # Bind POST data to the form
        if form.is_valid():
            task_name = form.cleaned_data['task_name']
            task_description = form.cleaned_data['task_description']
            task_label = form.cleaned_data['task_label']

            new_task = Task(task_name=task_name,
                            task_description=task_description,
                            task_label=task_label,
                            task_status=False)

            new_task.save()

            return render(response, 'add_task.html', {'Message': 'Task Added Successfully!'})
    else:
        form = AddTaskForm()  # Create an instance of your form

    return render(response, 'add_task.html', {'Message': ''})


def delete_task(response):
    return 0


def edit_task(response):
    return 0

