from django.urls import path
from . import views

urlpatterns = [
    path('', views.index) # the path for our view index
]