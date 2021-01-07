from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
from mainapp.models import Product, ProductCategory
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def main(request):
    title = 'Главная'
    products_list = Product.objects.all()[:4]
    basket = get_basket(request.user)
    content = {
        'title': title,
        'products': products_list,
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None, page=1):
    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)
    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            category = {
                'pk': 0,
                'name': 'все'
            }
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by(
                'price')

        paginator = Paginator(products, 3)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'Контакты'
    basket = get_basket(request.user)
    content = {
        'title': title,
    }
    return render(request, 'mainapp/contact.html', content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]

    return same_products


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)

# def products(request, pk=None):
#     title = 'Продукты'
#     links_menu = ProductCategory.objects.all()
#
#     basket = []
#     if request.user.is_authenticated:
#         basket = Basket.objects.filter(user=request.user)
#
#     if pk is not None:
#         if pk == 0:
#             products = Product.objects.all().order_by('price')
#             category = {'name': 'все'}
#         else:
#             category = get_object_or_404(ProductCategory, pk=pk)
#             products = Product.objects.filter(category__pk=pk).order_by('price')
#
#         content = {
#             'title': title,
#             'links_menu': links_menu,
#             'category': category,
#             'products': products,
#             'basket': basket,
#         }
#
#         return render(request, 'products_list.html', content)
#
#     products_list = Product.objects.all()[::3]
#     content = {
#         'title': title,
#         'products': products_list,
#         'links_menu': ProductCategory.objects.all()
#     }
#     if pk:
#         product_category = ProductCategory.objects.get(pk=pk)
#         # content['category'] = product_category, products_list
#         content['products'] = Product.objects.filter(category__pk=pk)
#     return render(request, 'products.html', content)


# def products(request, pk=None):
#     print(pk)
#
#     title = 'продукты'
#     links_menu = ProductCategory.objects.all()
#     products_list = Product.objects.all()[::3]
#
#     content = {'title': title, 'links_menu': links_menu, 'products_list': products_list}
#     return render(request, 'products.html', content)


# def products(request, pk=None):
#     print(pk)
#     title = 'Продукты'
#     products_list = Product.objects.all()[:12]
#     content = {
#         'title': title,
#         'products': products_list
#     }
#     if pk:
#         product_category = ProductCategory.get_object_or_404(pk=pk)
#         content['product'] = product_category, products_list
#     return render(request, 'products.html', content)


# def products_all(request):
#     title = 'Все товары'
#     links_menu = [
#         {'href': 'products', 'name': 'All series'},
#         {'href': 'products/', 'name': '12v series'},
#         {'href': 'products_18v', 'name': '18v series'},
#         {'href': 'products_2436v', 'name': '24-36v series'},
#     ]
#     products_list = Product.objects.all()[:4]
#     content = {
#         'title': title, 'products': products_list
#
#     }
#     return render(request, 'products.html', content)
#
#
# def products_12v(request):
#     links_menu = [
#         {'href': 'products_all', 'name': 'All series'},
#         {'href': 'products_12v', 'name': '12v series'},
#         {'href': 'products_18v', 'name': '18v series'},
#         {'href': 'products_2436v', 'name': '24-36v series'},
#     ]
#     content = {
#         'links_menu': links_menu
#     }
#     return render(request, 'products.html', content)
#
#
# def products_18v(request):
#     links_menu = [
#         {'href': 'products_all', 'name': 'All series'},
#         {'href': 'products_12v', 'name': '12v series'},
#         {'href': 'products_18v', 'name': '18v series'},
#         {'href': 'products_2436v', 'name': '24-36v series'},
#     ]
#     content = {
#         'links_menu': links_menu
#     }
#     return render(request, 'products.html', content)
#
#
# def products_2436v(request):
#     links_menu = [
#         {'href': 'products_all', 'name': 'All series'},
#         {'href': 'products_12v', 'name': '12v series'},
#         {'href': 'products_18v', 'name': '18v series'},
#         {'href': 'products_2436v', 'name': '24-36v series'},
#     ]
#     content = {
#         'links_menu': links_menu
#     }
#     return render(request, 'products.html', content)
