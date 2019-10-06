from django.contrib import admin
from .models import Category, Product, Hotel, Info, Mapa, PlayList, JustImages
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(JustImages)
class JustImagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_display = ['name', 'slug', 'stock', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'stock']
    prepopulated_fields = {'slug': ('name',)}


# The list of allowed values is: `hybrid`, `roadmap`, `satellite`, `terrain`
@admin.register(Mapa)
class MapaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    formfield_overrides = {
    map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }

@admin.register(Info)
class InfoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'created', 'updated', 'available']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'created', 'updated', 'phone', 'link', 'available']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['phone', 'available']


@admin.register(PlayList)
class PlayList(admin.ModelAdmin):

        list_display = ['nombre', 'cancion', 'porque', 'available', 'created', 'updated']




# class Hotel(models.Model):
#     name = models.CharField(max_length=200, db_index=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     image = models.ImageField(upload_to='products/%Y/%m/%d',
#                               blank=True)
#     address = models.TextField(blank=True)
#
#     phone = models.DecimalField(max_digits=10)
#
#     link = models.URLField(max_length=200)
#     available = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
