from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=255, db_index=True)

    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Product(models.Model):

    title = models.CharField(max_length=255, null=False)
    brand = models.CharField(max_length=255, default='no-branded')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    image = models.ImageField(upload_to='images/')

    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'products'
