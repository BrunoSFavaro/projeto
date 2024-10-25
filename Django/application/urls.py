from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bruno", views.bruno, name="bruno"),
    path("alexandre", views.alexandre, name="alexandre"),
    path("<str:name>", views.greet, name="greet")
]