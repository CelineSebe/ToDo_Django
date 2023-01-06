from django.urls import path
from todolist import views

urlpatterns = [
    path('about/', views.AboutView.as_view()),
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name="archive")
]