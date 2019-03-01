"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('', include(('Goods.urls', 'Goods'), namespace='Goods')),
<<<<<<< HEAD
    path('cupons/', include(('cupons.urls', 'cupons'), namespace='cupon')),
=======
>>>>>>> 05f74e2887f8030af7242c6bf46b1af72701bd6e
    path('payment/', include(('payment.urls', 'payment'), namespace='payment')),
    path('order/', include(('orders.urls', 'orders'), namespace='orders')),
    path('paypal/', include('paypal.standard.ipn.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)