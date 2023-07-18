from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("analyze", views.analyze, name="analyze"),
    path("about", views.about, name="about"),
    path("admin/", admin.site.urls),
]
from django.urls import path,re_path


from mysite import views