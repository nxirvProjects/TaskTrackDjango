from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Task, Label
from .forms import AddTaskForm, AddLabelForm, EditTaskForm, RegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form": form})


@login_required(redirect_field_name="/accounts/login/")
def home(response):
    return render(response, "home.html")


@login_required(redirect_field_name="/accounts/login/")
def view_labels(response):
    all_labels = Label.objects.filter(user=response.user).values()

    labels = []
    for i in all_labels:
        labels.append(i)
    return render(response, "view_labels.html", {"labels": labels})


@login_required(redirect_field_name="/accounts/login/")
def add_labels(response):
    if response.method == 'POST':
        form = AddLabelForm(response.POST)  # Bind POST data to the form
        if form.is_valid():
            label_name = form.cleaned_data['label_name']
            label_colour = form.cleaned_data['label_colour']

            new_label = Label(label_name=label_name,
                              label_colour=label_colour,
                              user=response.user.username)

            new_label.save()

            return render(response, 'add_label.html', {'Message': 'Label Added Successfully!'})
    else:
        form = AddLabelForm()

    return render(response, 'add_label.html', {'Message': ''})


@login_required(redirect_field_name="/accounts/login/")
def delete_label(response, label_name):
    label = Label.objects.get(pk=label_name)

    label.delete()
    return HttpResponseRedirect(f"/view_labels/")


@login_required(redirect_field_name="/accounts/login/")
def kanban(response, label_name):

    if response.method == 'POST':
        tasks_old = response.POST.getlist('task_status')

        all_tasks = Task.objects.filter(user=response.user).values()
        l_tasks = [task for task in all_tasks]

        for task in l_tasks:
            # Check if the task id is in tasks_old
            if str(task['id']) in tasks_old:
                task_instance = Task.objects.get(id=task['id'])
                task_instance.task_status = True
                task_instance.save()
            else:
                task_instance = Task.objects.get(id=task['id'])
                task_instance.task_status = False
                task_instance.save()

        all_tasks = Task.objects.filter(user=response.user).values()
        tasks = []
        for i in all_tasks:
            if i["task_label_id"] == int(label_name):
                tasks.append(i)

        return render(response, "kanban.html", {"tasks": tasks, "label_id": label_name})

    else:
        # If the request method is not POST, fetch all tasks from the database
        all_tasks = Task.objects.filter(user=response.user).values()
        tasks = []
        for i in all_tasks:
            if i["task_label_id"] == int(label_name):
                tasks.append(i)
        return render(response, "kanban.html", {"tasks": tasks, "label_id": label_name})

@login_required(redirect_field_name="/accounts/login/")
def view_all_tasks(response):
    if response.method == 'POST':
        tasks_old = response.POST.getlist('task_status')

        all_tasks = Task.objects.filter(user=response.user).values()
        l_tasks = [task for task in all_tasks]

        for task in l_tasks:
            # Check if the task id is in tasks_old
            if str(task['id']) in tasks_old:
                task_instance = Task.objects.get(id=task['id'])
                task_instance.task_status = True
                task_instance.save()
            else:
                task_instance = Task.objects.get(id=task['id'])
                task_instance.task_status = False
                task_instance.save()

        all_tasks = Task.objects.filter(user=response.user).values()
        tasks = [task for task in all_tasks]
        return render(response, "all_tasks.html", {"tasks": tasks})

    else:
        # If the request method is not POST, fetch all tasks from the database
        all_tasks = Task.objects.filter(user=response.user).values()
        tasks = [task for task in all_tasks]
        return render(response, "all_tasks.html", {"tasks": tasks})


@login_required(redirect_field_name="/accounts/login/")
def add_task(response):

    all_labels = Label.objects.filter(user=response.user).values()
    labels = []
    for i in all_labels:
        labels.append(i)

    if response.method == 'POST':
        form = AddTaskForm(response.POST)  # Bind POST data to the form
        if form.is_valid():
            task_name = form.cleaned_data['task_name']
            task_description = form.cleaned_data['task_description']

            task_label = form.cleaned_data['task_label']
            label = Label.objects.get(pk=task_label)
            deadline=form.cleaned_data['task_deadline']

            new_task = Task(task_name=task_name,
                            task_description=task_description,
                            task_label=label,
                            task_status=False,
                            user=response.user.username,
                            deadline=deadline)

            new_task.save()

            return render(response, 'add_task.html', {'Message': 'Task Added Successfully!', 'labels': labels})
        else:
            return render(response, 'add_task.html',
                          {'Message': 'There was an error, please fill out all fields marked with an asterisk', 'labels': labels})
    else:
        form = AddTaskForm()  # Create an instance of your form

    return render(response, 'add_task.html', {'Message': '', 'labels': labels})


@login_required(redirect_field_name="/accounts/login/")
def delete_task(response, task_name):
    task = Task.objects.get(pk=task_name)

    task.delete()
    return HttpResponseRedirect(f"/")


@login_required(redirect_field_name="/accounts/login/")
def edit_task(response, task_name):
    if response.method == 'POST':
        print(task_name)
        form = EditTaskForm(response.POST)  # Bind POST data to the form
        if form.is_valid():
            task_name_new = form.cleaned_data['task_name']
            task_description = form.cleaned_data['task_description']
            task_label = form.cleaned_data['task_label']
            deadline = form.cleaned_data['task_deadline']

            Task.objects.filter(pk=task_name).update(task_name=task_name_new,
                                                     task_description=task_description,
                                                     task_label=task_label,
                                                     deadline=deadline)

            return render(response, 'edit_task.html', {'Message': 'Task Edited!'})
    else:
        form = EditTaskForm()  # Create an instance of your form
        all_labels = Label.objects.filter(user=response.user).values()
        labels = []
        for i in all_labels:
            labels.append(i)

        task = Task.objects.get(pk=task_name)
        name = task.task_name
        desc = task.task_description
        return render(response, 'edit_task.html', {'Message': '', 'form': form, 'labels': labels, 'name': name,
                                               'desc': desc})

