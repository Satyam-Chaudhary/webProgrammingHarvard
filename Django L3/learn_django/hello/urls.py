from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name= "index"),
#    path("<str:name>", views.name , name = "name"),
#    path("<str:name>", views.greet , name = "greet"),
    path('satyam', views.satyam, name= 'satyam'),
    path('david', views.david, name= 'david')
]