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

###############################################################################


# Wish list view
def view_wish_list(request):
    """View for the wish list"""

    return render(request, 'wish/wish_list.html')


# View for adding products to the wish list
def add_to_wish_list(request, item_id):
    """ Add items to the wish list """

    # Read wish list content
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    resolution = None
    # Consider, initially, that user wants a delivery
    digital = 0

    # Check if product has resolution and read it
    if 'product_resolution' in request.POST:
        resolution = request.POST['product_resolution']

    # Get current session of the wish list
    wish_list = request.session.get('wish_list', {})

    # Check if product has resolution and consider it as a product (to be
    # added) if requested by user.
    # Alert user with Django message.
    if resolution:
        if item_id in list(wish_list.keys()):
            if resolution in wish_list[item_id]['items_by_resolution'].keys():
                wish_list[item_id]['items_by_resolution'][resolution] += quantity
                messages.success(request, f'Updated {resolution.upper()} resolution quantity for {product.name}')
            else:
                wish_list[item_id]['items_by_resolution'][resolution] = quantity
                messages.success(request, f'{resolution.upper()} resolution for {product.name} added to the wish list')
        else:
            wish_list[item_id] = {'items_by_resolution': {resolution: quantity}}
            messages.success(request, f'{resolution.upper()} resolution for {product.name} added to the wish list')
            
    # If product does not have resolution, just add it according to
    # user's request.
    # Alert user with Django message.
    else:
        if item_id in list(wish_list.keys()):
            wish_list[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {wish_list[item_id]}')
        else:
            wish_list[item_id] = quantity
            messages.success(request, f'{product.name} added to the wish list')
            
    # Add wish list to current session
    request.session['wish_list'] = wish_list

    return redirect(redirect_url)


# View for updating the wish list
def adjust_wish_list(request, item_id):
    """Adjust the quantity of items in the wish list"""

    # Read wish list content
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    resolution = None
    # Consider, initially, that user wants a delivery
    digital = 0

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