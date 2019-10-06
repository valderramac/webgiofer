from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('boda/informacion/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('', views.info_list, name='info_list'),
    path('comollegar/mapa/', views.mapa_detail, name='mapa_detail'),
    path('estadias/hoteles/', views.hotel_detail, name='hotel_detail'),
    path('<int:id>/<slug:slug>/informacion/', views.info_detail, name='info_detail'),
    # path('<int:id>/<slug:slug>/informacion/', views.add, name='info_detail'),
]

# path('', views.product_list, name='product_list'),

    # path('boda/informacion/', views.info_detail, name='info_detail'),
# <int:id>/<slug:slug>/
