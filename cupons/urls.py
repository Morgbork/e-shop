from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.CuponApply, name='apply')
]
