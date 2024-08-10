from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from apps.categories.models import Category
from apps.tags.models import Tag
from apps.products.models import Product, PriceFilter
from apps.cart.models import *

# Create your views here.
def category_page(request):
    search_query = request.GET.get('search', '')
    tag = Tag.objects.order_by('title')
    category = Category.objects.order_by('title')
    total_quantity = 0
    carts = CartItem.objects.filter(cart__user__username=request.user, status=True)
    for cart in carts:
           total_quantity += cart.quantity

    if request.method == 'POST':
        min_price = request.POST.get("min_price")
        max_price = request.POST.get("max_price")
        redirect("/category") 
        result = PriceFilter.objects.create(min_price=min_price, max_price=max_price)
        try:
            products = Product.objects.filter(Q(price__gt=min_price) & Q(price__lte=max_price)).exclude(user=request.user)
        except:
            products = Product.objects.filter(Q(price__gt=min_price) & Q(price__lte=max_price))
    
    else:
        if search_query:
            try:
                products = Product.objects.filter(Q(title__icontains=search_query) | Q(category__title__icontains=search_query) | Q(tag__title__icontains=search_query)).exclude(user=request.user)
            except:
                products = Product.objects.filter(Q(title__icontains=search_query) | Q(category__title__icontains=search_query) | Q(tag__title__icontains=search_query))
        else:
            try:
                products = Product.objects.all().order_by("-id").exclude(user=request.user)
            except TypeError:
                products = Product.objects.all().order_by("-id")

    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    product = paginator.get_page(page)

    return render(request, 'base/category.html', locals())


def category_detail(request, tag_id=None, category_id=None):
    search_query = request.GET.get('search', '')
    tag = Tag.objects.order_by('title')
    category = Category.objects.order_by('title')
    total_quantity = 0
    carts = CartItem.objects.filter(cart__user__username=request.user, status=True)
    for cart in carts:
           total_quantity += cart.quantity

    if category_id:
        try:
            products = Product.objects.filter(category=category_id).exclude(user=request.user)
        except:
            products = Product.objects.filter(category=category_id)
    elif tag_id:
        try:
            products = Product.objects.filter(tag=tag_id).exclude(user=request.user)
        except:
            products = Product.objects.filter(tag=tag_id)
    else:
        if search_query:
            try:
                products = Product.objects.filter(Q(title__icontains=search_query) | Q(category__title__icontains=search_query) | Q(tag__title__icontains=search_query)).exclude(user=request.user)
            except:
                products = Product.objects.filter(Q(title__icontains=search_query) | Q(category__title__icontains=search_query) | Q(tag__title__icontains=search_query))
        else:
            try:
                products = Product.objects.all().order_by("-id").exclude(user=request.user)
            except TypeError:
                products = Product.objects.all().order_by("-id")

    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    product = paginator.get_page(page)

    return render(request, 'base/category_detail.html', locals())

def create_category(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        categories = Category.objects.all()
        lst = []
        for category in categories:
            if category.title == title:
                lst.append(title)
        if lst == []:
            result = Category.objects.create(title=title)

        return redirect("/category")

    return render(request, 'base/create_category.html', locals())