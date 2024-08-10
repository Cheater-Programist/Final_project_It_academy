from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from apps.products.models import Product
from apps.cart.models import Cart, CartItem, OrderPage, Order

def cart(request, id=None):
    Cart.objects.get_or_create(user=request.user)
    
    if id:
        product = Product.objects.get(id=id)
        carts = CartItem.objects.filter(cart__user=request.user, product__id=product.id, status=True)
        user_cart = Cart.objects.get(user=request.user)
        
        if not carts.exists():
            CartItem.objects.create(cart=user_cart, product=product, quantity=1)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            cart = carts.first()
            cart.quantity += 1
            cart.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        total_price = 0
        total_quantity = 0
        carts = CartItem.objects.filter(cart__user__username=request.user, status=True).order_by("-id")
        for cart in carts:
           total_price += cart.sum()
           total_quantity += cart.quantity

    return render(request, 'cart/basket.html', locals())

def cart_update(request, id):
    # user_cart = Cart.objects.get(user=request.user)
    cart = get_object_or_404(CartItem, id=id)
    if request.method == 'POST':
        if 'update' in request.POST:
            quantity = request.POST.get('quantity')

        if quantity:
                cart.quantity = int(quantity)

    cart.save()        

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cart_delete(request, id):
    if request.method == 'POST':
        if 'delete' in request.POST:
            cart = CartItem.objects.get(id=id)
            cart.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def order_review(request):
    OrderPage.objects.get_or_create(user=request.user)
    total_price = 0
    total_quantity = 0

    user_order = OrderPage.objects.get(user=request.user)
    carts = CartItem.objects.filter(cart__user__username=request.user, status=True).order_by("-id")
    orders = Order.objects.create(order=user_order)
    for cart in carts:
        orders.product.add(cart)
        cart.status = False
        cart.save()
    orders.save()

    for order in orders.product.all():
        total_price += order.quantity * order.product.price
        total_quantity += order.quantity


    return render(request, 'cart/checkout2.html', locals())

def orders(request):
    orders = Order.objects.filter(order__user__username=request.user).order_by("-id")
    
    total_quantity = 0
    carts = CartItem.objects.filter(cart__user__username=request.user, status=True)
    for cart in carts:
           total_quantity += cart.quantity

    return render(request, "cart/my_orders.html", locals())

def order_detail(request, id):
    orders = Order.objects.get(id=id)
    
    total_price = 0
    for order in orders.product.all():
        total_price += order.quantity * order.product.price
        
    total_quantity = 0
    carts = CartItem.objects.filter(cart__user__username=request.user, status=True)
    for cart in carts:
           total_quantity += cart.quantity

    return render(request, 'cart/order_detail.html', locals())