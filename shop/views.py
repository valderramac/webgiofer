from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Hotel, Info, Mapa, PlayList
from cart.forms import CartAddProductForm
from .forms import PlayListForm
from django.views.decorators.http import require_POST
from django.shortcuts import redirect


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    products = products.filter(category=category)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render (request,
                    'shop/product/list.html',
                    {'category': category,
                    'categories': categories,
                    'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id = id,
                                slug = slug,
                                available = True)
    cart_product_form = CartAddProductForm()
    return render(request,
                    'shop/product/detail.html',
                    {'product': product,
                    'cart_product_form': cart_product_form})



def info_list(request, category_slug=None):
    infos = Info.objects.filter(available=True)
    return render(request,
                  'shop/product/informacion.html',
                  {'infos': infos})
    # aqui el formulario de las canciones



# @require_POST
def info_detail(request, id, slug):
    info = get_object_or_404(Info,
                             id = id,
                             slug = slug,
                             available = True)

    form = PlayListForm()

    if request.method == "POST":
        form = PlayListForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return redirect('/7/playlist/informacion/')

    return render(request,
                 'shop/product/infoDetail.html',
                 {'info': info,
                  'form': form})



# aqui el mapa
def mapa_detail(request):
    mapas = Mapa.objects.filter(available=True)
    return render(request,
                 'shop/product/mapa.html',
                 {'mapas': mapas})

# def hoteles_detail(request):
#     return render(request, 'shop/product/hoteles.html')



def hotel_detail(request, category_slug=None):
    hotels = Hotel.objects.filter(available=True)
    return render (request,
                    'shop/product/hoteles.html',
                    {
                    'hotels': hotels})

#
# def add(request):
#     form = PlayListForm()
#
#     if request.method == "POST":
#         if form.is_valid():
#             instancia = form.save(commit=False)
#             instancia.save()
#             return redirect('/')
#
#     return render(request, "shop/product/infoDetail.html", {'form': form})
