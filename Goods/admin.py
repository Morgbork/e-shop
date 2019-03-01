from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'specification']
    prepopulated_fields = {'slug' : ('name', )}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['manufacturer', 'name',  'description', 'price', 'stock', 'updated', 'specification']
    list_editable = ['price', 'stock']
    list_filter = ['manufacturer', 'price', 'stock', 'updated']
    prepopulated_fields = {'slug' : ('manufacturer', 'name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin) 