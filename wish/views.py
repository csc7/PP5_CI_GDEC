###############################################################################

"""
Django views for the wish list app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages

# INTERNAL:
from products.models import Product
from checkout.models import OrderLineItem
from profiles.models import UserProfile
from wish.models import WishList
from bag.templatetags.bag_tools import calc_subtotal

###############################################################################


# Wish list view
def view_wish_list(request):
    """View for the wish list"""

    profile = get_object_or_404(UserProfile, user=request.user)
    wish_list_items = WishList.objects.filter(user_profile=profile)

    user_wish_orders = profile.orders.all()

    #products_in_wish_orders = OrderLineItem.objects.filter(order=user_wish_orders)
    products_in_wish_orders = OrderLineItem.objects.filter(order=user_wish_orders)
    products_in_wish_orders = OrderLineItem.objects.all()
    products_to_show_in_wish_list = wish_list_items.values_list('product_id', flat=True)
    
    context = {
        'products_in_wish_orders': wish_list_items,
    }

    #if request.user.is_authenticated:
        #order = get_object_or_404(Order, order_number=order_number)
        # Add user profile to order
        #order.save()

    return render(request, 'wish/wish_list.html', context)


# View for adding products to the wish list
def add_to_wish_list(request, item_id):
    """ Add items to the wish list """

    #wish_list = request.session.get('wish_list', {})

    # Read product being added
    product = get_object_or_404(Product, pk=item_id)    

    # Initialize resolution and check if product has already one
    resolution = None
    if 'product_resolution' in request.POST:
        resolution = request.POST['product_resolution']
        print(resolution)

    # Read user profile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Read quantity, URL to redirect and compute line_item_total
    quantity = int(request.POST.get('quantity'))   
    redirect_url = request.POST.get('redirect_url')
    line_item_total = calc_subtotal(product.price, quantity)
    items_in_wish_list = WishList.objects.all()
    
    # Create or update new wish item
    if product.id in items_in_wish_list.values_list('product', flat=True): 
        existent_wish_item = WishList.objects.filter(product=product.id)
        existent_wish_item_resolution = existent_wish_item.values_list(
                'product_resolution', flat=True
        )
        existent_wish_item_quantity = existent_wish_item.values_list(
                'quantity', flat=True
        )
        print(resolution)
        print(existent_wish_item_resolution[0])
        print(quantity)
        print(existent_wish_item_quantity[0])
        if (existent_wish_item_resolution[0] == resolution and 
                existent_wish_item_quantity[0] == quantity):
            # Record exists
            print("Product, resolution and quantity already in wish list")
        else:
            # Update record
            new_wish_item = WishList.objects.get(user_profile=profile,
                                        product=product)
            new_wish_item.product_resolution = resolution
            new_wish_item.quantity = quantity
            new_wish_item.lineitem_total = line_item_total
            print("Record updated")
            new_wish_item.save()
    else:
        new_wish_item = WishList.objects.create(user_profile=profile,
                                        product=product,
                                        product_resolution=resolution,
                                        quantity=quantity,
                                        lineitem_total=line_item_total,)
        print("Record created")
        new_wish_item.save()
    
    #request.session['wish_list'] = wish_list

    return redirect(redirect_url)


# View for updating the wish list
def adjust_wish_list(request, item_id):
    """Adjust the quantity of items in the wish list"""

    # Read wish list content
    item_to_delete = get_object_or_404(WishList, pk=item_id)
    print(item_to_delete)

    return redirect(reverse('view_wish_list'))



def remove_from_wish_list(request, item_id):
    """Remove items from the wish_list"""

    try:
        item_to_delete = get_object_or_404(WishList, pk=item_id)
        print(item_to_delete)
        

        return HttpResponse(status=200)

    # Show an error if item cannot be removed.
    # Alert user with Django message.
    except Exception as e:
        messages.error(request, f'Error removing item_ {e}')
        return HttpResponse(status=500)