from django.db import models

# Create your models here.

class  ToDoList(models.Model):
    '''Model for ToDoList'''

    name = models.CharField(verbose_name='Name', max_length= 255)
    
    def __str__(self) -> str:
        return self.name

class ToDo (models.Model):
    """Model for task """
    todo_text = models.CharField(verbose_name="Title", max_length=20)
    todo_list= models.ForeignKey(ToDoList, null = True, blank=True, on_delete=models.CASCADE)
    deadline = models.DateField(null= True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.todo_text

