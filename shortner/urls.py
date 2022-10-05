from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<str:our_short_url>/', views.redirect, name='redirect'),

]
