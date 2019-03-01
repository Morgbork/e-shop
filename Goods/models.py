from django.db import models
from django.urls import reverse 




class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, )
    slug = models.SlugField(max_length=250, unique = True, db_index = True, default = name)
    specification = models.TextField(blank = True)

    class Meta:
        ordering= ['name']

    def get_absolute_url(self):
        from . import views
        return reverse('Goods:ProductListByCategory', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name = 'Products', on_delete = models.CASCADE)
    manufacturer = models.CharField(max_length = 100)
    name = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200, db_index = True, default = name)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places = 2)
    stock = models.BooleanField(default = False)
    updated = models.DateTimeField(auto_now = True)
    specification = models.TextField(blank=True)
    image =  models.ImageField(upload_to='products/%Y/%m/%d/')

    class Meta:
        unique_together = ("manufacturer", "name")

    def get_absolute_url(self):
        from . import views
        return reverse('Goods:ProductDetail', args=[self.id, self.slug])

    def __str__(self):
        return self.name



