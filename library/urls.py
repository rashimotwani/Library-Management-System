from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Library"),
    path("issuedBooks/", views.issue, name="issuedBooks"),
]