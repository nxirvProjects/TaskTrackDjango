from django.db import models


class Label(models.Model):
    label_name = models.CharField(max_length=255)
    label_colour = models.CharField(max_length=100, choices=[
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
    user = models.CharField(max_length=255, default='blank')


# Task db model
class Task(models.Model):
    task_name = models.CharField(max_length=255)
    task_description = models.CharField(max_length=500)
    task_status = models.BooleanField()
    task_label = models.ForeignKey(Label, on_delete=models.CASCADE)
    user = models.CharField(max_length=255, default='blank')
    deadline = models.DateTimeField(null=True, blank=True)

