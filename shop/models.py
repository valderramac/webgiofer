from django.db import models
from django.urls import reverse
from django_google_maps import fields as map_fields

import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'






class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_list_by_category',
                           args=[self.slug])



#
# foto
# nombre
# address
# telefono
# link
#


class JustImages(models.Model):
    theoneimage = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, default='img')
    name = models.CharField(blank=True, max_length=200,
                            db_index=True, default='imgname')
    slug = models.SlugField(blank=True, max_length=200,
                            unique=True, default='imgslug')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:infoImages_detail',
                           args=[self.id, self.slug])



class Hotel(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    address = models.TextField(blank=True)
    description = models.TextField(blank=True)

    phone = models.CharField(max_length=200, blank=True)

    link = models.URLField(max_length=200, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Info(models.Model):
    justimage = models.ForeignKey(JustImages,
                                 # related_name='infos',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    imagesecond = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    imagethird = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    imagefourth = models.ImageField(upload_to='products/%Y/%m/%d',
                            blank=True)
    description = models.TextField(blank=True)
    descriptionsecond = models.TextField(blank=True)
    descriptionthird = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:info_detail',
                           args=[self.id, self.slug])


class Mapa(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)
    available = models.BooleanField(default=True)



class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    stock = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('shop:product_detail',
                           args=[self.id, self.slug])


class PlayList(models.Model):
        nombre = models.CharField(blank=True, max_length=100)
        cancion = models.CharField(blank=False, max_length=100)
        porque = models.CharField(blank=True, max_length=100)
        available = models.BooleanField(default=True)
        created = models.DateTimeField(null=True, auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
