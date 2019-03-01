from django.urls import path
from . import views 

urlpatterns = [
    path('create/', views.OrderCreate, name='OrderCreate'),
    path('admin/order/<str:order_id>/', views.AdminOrderDetail, name='AdminOrderDetail'),
]