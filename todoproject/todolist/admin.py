from django.contrib import admin
from todolist.models import ToDo, ToDoList

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('todo_text', 'deadline', 'completed')

admin.site.register(ToDo, TaskAdmin)
admin.site.register(ToDoList)

