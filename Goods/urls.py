from django.urls import path
from . import views 

urlpatterns = [
    path('<str:category_slug>/', views.ProductList, name='ProductListByCategory'),
    path('<int:id>/<str:slug>/', views.ProductDetail, name='ProductDetail'),
    path('', views.ProductList, name='ProductList'),
]