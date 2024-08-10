from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.core.paginator import Paginator

from apps.products.models import Product
from apps.likes.models import Like
from apps.cart.models import CartItem

def wishlist(request, id=None):
    total_quantity = 0
    carts = CartItem.objects.filter(cart__user__username=request.user)
    for cart in carts:
           total_quantity += cart.quantity
    quantity = 0

    color = ''

    if id:
        product = Product.objects.get(id=id)
        likes = Like.objects.filter(user=request.user, product=product)
        if not likes.exists():
            Like.objects.create(user=request.user, product=product)
            color = 'default'
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            like = likes.first()
            like.delete()
            color = 'primary'
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    else:
        likes = Like.objects.filter(user=request.user).order_by("-id")
        for like in likes:
            quantity += 1
        
        
        paginator = Paginator(likes, 8)
        page = request.GET.get('page')
        like = paginator.get_page(page)

    return render(request, 'base/wishlist.html', locals())