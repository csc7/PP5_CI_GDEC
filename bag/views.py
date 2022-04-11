###############################################################################

"""
Django views for the bag app
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


# Bag view
def view_bag(request):
    """View for the purchasing bag"""

    return render(request, 'bag/bag.html')


# View for adding products to the bag
def add_to_bag(request, item_id):
    """ Add items to the purchasing bag """

    # Read bag content
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    resolution = None
    # Consider, initially, that user wants a delivery
    digital = 0

    # Check if product has resolution and read it
    if 'product_resolution' in request.POST:
        resolution = request.POST['product_resolution']

    # Get current session bag
    bag = request.session.get('bag', {})

    # Check if product has resolution and consider it as a product (to be
    # added) if requested by user.
    # Alert user with Django message.
    if resolution:
        if item_id in list(bag.keys()):
            if resolution in bag[item_id]['items_by_resolution'].keys():
                bag[item_id]['items_by_resolution'][resolution] += quantity
                messages.success(request, f'Updated {resolution.upper()} resolution quantity for {product.name}')
            else:
                bag[item_id]['items_by_resolution'][resolution] = quantity
                messages.success(request, f'{resolution.upper()} resolution for {product.name} added to the bag')
        else:
            bag[item_id] = {'items_by_resolution': {resolution: quantity}}
            messages.success(request, f'{resolution.upper()} resolution for {product.name} added to the bag')
            
    # If product does not have resolution, just add it according to
    # user's request.
    # Alert user with Django message.
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'{product.name} added to the bag')
            
    # Add bag to current session
    request.session['bag'] = bag

    return redirect(redirect_url)


# View for updating the bag
def adjust_bag(request, item_id):
    """Adjust the quantity of items in the purchasing bag"""

    # Read bag content
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

    # Get current session bag
    bag = request.session.get('bag', {})

    # Check if product has resolution and consider it as a product (to be
    # updated) if requested by user.
    # Alert user with Django message.
    if resolution:
        if quantity > 0:
            bag[item_id]['items_by_resolution'][resolution] = quantity
            messages.success(request, f'Updated {resolution.upper()} resolution quantity for {product.name}')
            print(bag[item_id])
        else:
            del bag[item_id]['items_by_resolution'][resolution]
            if not bag[item_id]['items_by_resolution']:
                bag.pop(item_id)
            messages.success(request, f'Removed {resolution.upper()} resolution for {product.name} from the bag')

    # If product does not have resolution, just update it according to
    # user's request.
    # Alert user with Django message.
    else:
        if quantity > 0:               
            
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {product.name}')
            print(bag[item_id])

        else:
            bag.pop(item_id)
            messages.success(request, f'{product.name} removed from the bag')
            
    # Update bag to current session
    request.session['bag'] = bag

    return redirect(reverse('view_bag'))



def remove_from_bag(request, item_id):
    """Remove items from the purchasing bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        resolution = None
        # Check if product to update has resolution
        if 'product_resolution' in request.POST:
            resolution = request.POST['product_resolution']
        # Get current session bag
        bag = request.session.get('bag', {})

        # Check if product has resolution and consider it as a product (to be
        # deleted) if requested by user.
        # Alert user with Django message.
        if resolution:
            
            del bag[item_id]['items_by_resolution'][resolution]
            if not bag[item_id]['items_by_resolution']:
                bag.pop(item_id)
            messages.success(request, f'Removed {resolution.upper()} resolution for {product.name} from the bag')
        
        # If product does not have resolution, just delete it according to
        # user's request.
        # Alert user with Django message.
        else:
            bag.pop(item_id)
            messages.success(request, f'{product.name} removed from the bag')

        # Update bag to current session
        request.session['bag'] = bag

        return HttpResponse(status=200)

    # Show an error if item cannot be removed.
    # Alert user with Django message.
    except Exception as e:
        messages.error(request, f'Error removing item_ {e}')
        return HttpResponse(status=500)