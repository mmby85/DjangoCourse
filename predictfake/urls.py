from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index2"),
    path("formulaire/", views.index),
    path("traitement/", views.index),
    path("affichage/", views.index),
    path("home/", views.home, name="home"),
    path("show_news/", views.show_news, name="show_news"),
    path("fill_news/", views.fill_news, name="fill_news"),

]
