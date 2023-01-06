from django.db import models

# Create your models here.

class ToDo (models.Model):
    """Model for task """
    todo_text = models.CharField(verbose_name="Title", max_length=20)
    deadline = models.DateField(null= True, blank=True)
    completed = models.BooleanField()
