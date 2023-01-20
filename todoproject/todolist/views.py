from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView

from todolist.models import ToDo

# Create your views here.
def index(request):
    return HttpResponse("<h1>Bienvenue sur notre application</h1>")

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Bienvenue sur notre IndexView</h1>")

class AboutView(TemplateView):
    template_name = "about.html"

class ArchiveView(View):
    def get(self, request, year, month):
        if year > 2023:
            return HttpResponse("sélectionnez une ancienne année")
        return HttpResponse(f"{month}, {year}")

class ToDosView(View):
    def get(self, request):
        todos = ToDo.objects.all()
        todos.values("todo_text")
        return HttpResponse(todos)