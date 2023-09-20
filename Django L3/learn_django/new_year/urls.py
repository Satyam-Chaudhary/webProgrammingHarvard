from django.urls import path

from . import views

urlpatterns = [
    path("" , views.index, name = 'new_year'),
    path("new" , views.new, name = 'new')


]