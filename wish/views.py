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
    print("Profile: ")
    print (profile)
    user_wish_orders = profile.orders.all()
    #user_orders_ids = user_orders.id
    
    print(user_wish_orders)
    #products_in_history_orders = {}
    for user_wish_order in user_wish_orders:      
        print(user_wish_order)

    products_in_wish_orders = OrderLineItem.objects.filter(order=user_wish_orders)
    products_in_wish_orders = OrderLineItem.objects.all()
    products_to_show_in_wish_list = products_in_wish_orders.values_list('product_id', flat=True)
    
    context = {
        'products_in_wish_orders': products_to_show_in_wish_list,
    }

    #if request.user.is_authenticated:
        #order = get_object_or_404(Order, order_number=order_number)
        # Add user profile to order
        #order.save()

    return render(request, 'wish/wish_list.html', context)


# View for adding products to the wish list
def add_to_wish_list(request, item_id):
    """ Add items to the wish list """
    
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
    
    return redirect(redirect_url)


# View for updating the wish list
def adjust_wish_list(request, item_id):
    """Adjust the quantity of items in the wish list"""

    # Read wish list content
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    resolution = None
    # Consider, initially, that user wants a delivery
    #digital = 0

    # Check if product to update has resolution and read it
    if 'product_resolution' in request.POST:
        resolution = request.POST['product_resolution']
        
    #if 'digital' in request.POST:
    #    print("OK")

    # Get current session wish list
    wish_list = request.session.get('wish_list', {})

    # Check if product has resolution and consider it as a product (to be
    # updated) if requested by user.
    # Alert user with Django message.
    if resolution:
        if quantity > 0:
            wish_list[item_id]['items_by_resolution'][resolution] = quantity
            messages.success(request, f'Updated {resolution.upper()} resolution quantity for {product.name}')

        else:
            del wish_list[item_id]['items_by_resolution'][resolution]
            if not wish_list[item_id]['items_by_resolution']:
                wish_list.pop(item_id)
            messages.success(request, f'Removed {resolution.upper()} resolution for {product.name} from the wish list')

    # If product does not have resolution, just update it according to
    # user's request.
    # Alert user with Django message.
    else:
        if quantity > 0:               
            
            wish_list[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {product.name}')

        else:
            wish_list.pop(item_id)
            messages.success(request, f'{product.name} removed from the wish list')
            
    # Update wish list to current session
    request.session['wish_list'] = wish_list

    return redirect(reverse('view_wish_list'))



def remove_from_wish_list(request, item_id):
    """Remove items from the wish_list"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        resolution = None
        # Check if product to update has resolution
        if 'product_resolution' in request.POST:
            resolution = request.POST['product_resolution']
        # Get current session wish list
        wish_list = request.session.get('wish_list', {})

        # Check if product has resolution and consider it as a product (to be
        # deleted) if requested by user.
        # Alert user with Django message.
        if resolution:
            
            del wish_list[item_id]['items_by_resolution'][resolution]
            if not wish_list[item_id]['items_by_resolution']:
                wish_list.pop(item_id)
            messages.success(request, f'Removed {resolution.upper()} resolution for {product.name} from the wish list')
        
        # If product does not have resolution, just delete it according to
        # user's request.
        # Alert user with Django message.
        else:
            wish_list.pop(item_id)
            messages.success(request, f'{product.name} removed from the wish list')

        # Update wish list to current session
        request.session['wish_list'] = wish_list

        return HttpResponse(status=200)

    # Show an error if item cannot be removed.
    # Alert user with Django message.
    except Exception as e:
        messages.error(request, f'Error removing item_ {e}')
        return HttpResponse(status=500)