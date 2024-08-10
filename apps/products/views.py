from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from apps.products.models import Product
from apps.categories.models import Category
from apps.tags.models import Tag
from apps.comments.models import Comment
from apps.likes.models import Like
from apps.cart.models import Cart, CartItem
from apps.users.models import User

# Create your views here.
def home(request):
    search_query = request.GET.get('search', '')
    total_quantity = 0
    carts = CartItem.objects.filter(cart__user__username=request.user, status=True)
    for cart in carts:
           total_quantity += cart.quantity

    if search_query:
        try:
            products = Product.objects.filter(Q(title__icontains=search_query) | Q(category__title__icontains=search_query) | Q(tag__title__icontains=search_query)).exclude(user=request.user)
        except:
            products = Product.objects.filter(Q(title__icontains=search_query) | Q(category__title__icontains=search_query) | Q(tag__title__icontains=search_query))
    else:
        try:
            products = Product.objects.all().order_by("-id").exclude(user=request.user)
        except:
            products = Product.objects.all().order_by("-id") 
        
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    product = paginator.get_page(page)
    return render(request, 'base/index.html', locals())

@login_required
def my_products(request):
    product_quantity = 0
    search_query = request.GET.get('search', '')

    total_quantity = 0
    carts = CartItem.objects.filter(cart__user__username=request.user, status=True)
    for cart in carts:
           total_quantity += cart.quantity

    if search_query:
        products = Product.objects.filter(Q(title__icontains=search_query) | Q(category__title__icontains=search_query) | Q(tag__title__icontains=search_query)).get(user=request.user)
    else:
        products = Product.objects.filter(user=request.user).order_by("-id")
        for product in products:
            product_quantity += 1
        
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    product = paginator.get_page(page)
    return render(request, 'base/my_products.html', locals())

def detail(request, id=None, comment_id=None):    
    product_by_id = get_object_or_404(Product, id=id)
    comments = Comment.objects.filter(product=product_by_id).order_by("-id")

    total_quantity = 0
    carts = CartItem.objects.filter(cart__user__username=request.user, status=True)
    for cart in carts:
           total_quantity += cart.quantity

    if request.method == 'POST':
        if 'comment' in request.POST:
            user = request.user
            product = product_by_id
            text = request.POST.get('text')
            result = Comment.objects.create(user=user, product=product, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if 'cart' in request.POST:
            carts = CartItem.objects.filter(cart__user=request.user, product__id=product_by_id.id, status=True)
            user_cart = Cart.objects.get_or_create(user_id=request.user.id)
            quant = request.POST.get('quantity')
            
            if not carts.exists():
                CartItem.objects.create(cart=user_cart, product=product_by_id, quantity=int(quant))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                cart = carts.first()
                cart.quantity += int(quant)
                cart.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if 'like' in request.POST:
            likes = Like.objects.filter(user=request.user, product=product_by_id)
            if not likes.exists():
                Like.objects.create(user=request.user, product=product_by_id)
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                like = likes.first()
                like.delete()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    return render(request, 'base/detail.html', locals())

def create(request):
    category = Category.objects.all().order_by('title')
    tag = Tag.objects.all().order_by('title')
    
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.getlist('category')
        tag = request.POST.getlist('tag')
        price = request.POST.get('price')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        result = Product.objects.create(user=user, title=title, description=description, price=price, image1=image1, image2=image2, image3=image3)

        for cat in category:
            result.category.add(cat)
        for ta in tag:
            result.tag.add(ta)

        return redirect("/my_products")

    return render(request, 'base/create_product.html', locals())

def update(request, pk):
    category = Category.objects.all()
    tag = Tag.objects.all()
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        selected_categories = request.POST.getlist('category')
        selected_tags = request.POST.getlist('tag')
        price = request.POST.get('price')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        # product = Product.objects.update(user=user, title=title, description=description, price=price, image1=image1, image2=image2, image3=image3)
        
        product.title = title
        product.description=description
        product.price=price
        if image1:
            product.image1=image1
        if image2:
            product.image2=image2
        if image3:
            product.image3=image3

        # Обновление категорий
        for category_id in selected_categories:
            category_obj = Category.objects.get(id=category_id)
            if category_obj in product.category.all():
                product.category.remove(category_obj)
            else:
                product.category.add(category_obj)

        # Обновление тегов
        for tag_id in selected_tags:
            tag_obj = Tag.objects.get(id=tag_id)
            if tag_obj in product.tag.all():
                product.tag.remove(tag_obj)
            else:
                product.tag.add(tag_obj)
        
        product.save()

        return redirect(f"/product/{product.pk}")

    return render(request, 'base/update_product.html', locals())

def delete(request, id):
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        product.delete()
        return redirect("/my_products")
    return render(request, 'base/delete_product.html', locals())