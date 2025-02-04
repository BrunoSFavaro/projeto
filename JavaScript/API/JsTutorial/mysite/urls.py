
from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("sections/<int:num>", views.section, name="section"),
    path("posts", views.posts, name="posts")
]
