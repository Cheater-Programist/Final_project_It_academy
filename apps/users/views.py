from django.shortcuts import render, redirect

from apps.users.models import User
from apps.cart.models import CartItem

# Create your views here.
def user_form(request):
    total_quantity = 0
    carts = CartItem.objects.filter(cart__user__username=request.user, status=True)
    for cart in carts:
           total_quantity += cart.quantity

    user = User.objects.get(email=request.user.email)
    if request.method == 'POST':
        if 'info' in request.POST:
            f_name = request.POST.get('f_name')
            l_name = request.POST.get('l_name')
            country = request.POST.get('country')
            city = request.POST.get('city')
            street = request.POST.get('street')
            phone = request.POST.get('phone')
            # email = request.POST.get('email')

            user.first_name = f_name
            user.last_name = l_name
            user.country = country
            user.city = city
            user.street = street
            user.phone = phone

            user.save()

            return redirect("/order_review")

    return render(request, 'cart/checkout1.html', locals())