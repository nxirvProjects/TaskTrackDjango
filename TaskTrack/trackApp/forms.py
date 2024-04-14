from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AddTaskForm(forms.Form):
    task_name = forms.CharField(label='task name', max_length=255, required=True)
    task_description = forms.CharField(label='task description', max_length=500, required=False)
    task_label = forms.CharField(label='task label', max_length=100, required=True)
    task_deadline = forms.DateTimeField(label='task deadline', required=True)


class SaveTaskForm(forms.Form):
    task_name = forms.CharField(label='task name', max_length=255, required=True)
    task_description = forms.CharField(label='task description', max_length=500, required=False)
    task_label = forms.CharField(label='task label', max_length=100, required=False)
    task_status = forms.BooleanField(label="task status")


class AddLabelForm(forms.Form):
    label_name = forms.CharField(label='label name', max_length=255, required=True)
    label_colour = forms.ChoiceField(label="label colour", choices=[
        ("#FFD1DC", "Pastel Pink"),
        ("#FFB6C1", "Light Pink"),
        ("#FFA07A", "Light Salmon"),
        ("#FFE4B5", "Moccasin"),
        ("#FFDAB9", "Peachpuff"),
        ("#FA8072", "Salmon"),
        ("#FFD700", "Gold"),
        ("#FFFACD", "Lemon Chiffon"),
        ("#F0FFF0", "Honeydew"),
        ("#FFA07A", "Peach")])


class EditTaskForm(forms.Form):
    task_name = forms.CharField(label='task name', max_length=255, required=True)
    task_description = forms.CharField(label='task description', max_length=500, required=False)
    task_label = forms.CharField(label='task label', max_length=100, required=False)
    task_deadline = forms.DateTimeField(label='task deadline', required=True)

class EditLabelForm(forms.Form):
    label_name = forms.CharField(label='label name', max_length=255, required=True)
    label_colour = forms.ChoiceField(label="label colour", choices=[
        ("#FFD1DC", "Pastel Pink"),
        ("#FFB6C1", "Light Pink"),
        ("#FFA07A", "Light Salmon"),
        ("#FFE4B5", "Moccasin"),
        ("#FFDAB9", "Peachpuff"),
        ("#FA8072", "Salmon"),
        ("#FFD700", "Gold"),
        ("#FFFACD", "Lemon Chiffon"),
        ("#F0FFF0", "Honeydew"),
        ("#FFA07A", "Peach")])

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
