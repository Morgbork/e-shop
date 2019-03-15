from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm
from analytics.signals import Signal

def ProductList(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(stock = True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'Goods/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })

def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, stock = True)
    cart_product_form = CartAddProductForm()
    # object_viewed_signal.send(product.__class__, instance=product, request=request)
    return render(request, 'Goods/product/detail.html', {'product': product, 'cart_product_form': cart_product_form })

