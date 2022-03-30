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


# Create your views here.

def view_bag(request):
    """View for the purchasing bag"""

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add items to the purchasing bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    resolution = None
    if 'product_resolution' in request.POST:
        resolution = request.POST['product_resolution']

    bag = request.session.get('bag', {})

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
            

    else:

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')


        else:
            bag[item_id] = quantity
            messages.success(request, f'{product.name} added to the bag')
            

    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of items in the purchasing bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    resolution = None
    if 'product_resolution' in request.POST:
        resolution = request.POST['product_resolution']
        
    bag = request.session.get('bag', {})

    if resolution:
        if quantity > 0:
            bag[item_id]['items_by_resolution'][resolution] = quantity
            messages.success(request, f'Updated {resolution.upper()} resolution quantity for {product.name}')
        else:
            del bag[item_id]['items_by_resolution'][resolution]
            if not bag[item_id]['items_by_resolution']:
                bag.pop(item_id)
            messages.success(request, f'Removed {resolution.upper()} resolution for {product.name} from the bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            
            messages.success(request, f'Updated {product.name} quantity to {product.name}')
            
        else:
            bag.pop(item_id)
            messages.success(request, f'{product.name} removed from the bag')
            #print("RESOLUTON =")

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove items from the purchasing bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        resolution = None
        if 'product_resolution' in request.POST:
            resolution = request.POST['product_resolution']
        bag = request.session.get('bag', {})

        if resolution:
            
            del bag[item_id]['items_by_resolution'][resolution]
            if not bag[item_id]['items_by_resolution']:
                bag.pop(item_id)
            messages.success(request, f'Removed {resolution.upper()} resolution for {product.name} from the bag')
        else:
            bag.pop(item_id)
            print("REMOVING")
            messages.success(request, f'{product.name} removed from the bag')

        request.session['bag'] = bag

        return HttpResponse(status=200)


    except Exception as e:
        messages.error(request, f'Error removing item_ {e}')
        return HttpResponse(status=500)