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
import re
import json

# INTERNAL:
from products.models import Product

###############################################################################


# Bag view
def view_bag(request):
    """View for the purchasing bag
    This function computes the grand total amount based on the products
    in the bag and the user's delivery preferences

    Parameters In: HTTP request object

    Parameters Out: HTTP request object to bag/bag.html template
    """

    return render(request, 'bag/bag.html')


# View for adding products to the bag
def add_to_bag(request, item_id):
    """ Add items to the purchasing bag

    Parameters In: HTTP request object, product ID

    Parameters Out: redirect URL
    """

    # Convert to string if product ID is not an integer
    if isinstance(item_id, int):
        item_id = str(item_id)

    # Read bag content
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # Assing none to resolution in case the product does not contain it
    resolution = None

    # Consider, initially, that user wants a delivery
    digital = 0

    # Check if product has resolution and read it
    if 'product_resolution' in request.POST:
        resolution = request.POST['product_resolution'].lower()

    # Get current session bag
    bag = request.session.get('bag', {})

    # Check if product has resolution and consider it as a product (to be
    # added) if requested by user.
    # Alert user with Django message.
    if resolution:
        if item_id in list(bag.keys()):
            if resolution in bag[item_id]['items_by_resolution'].keys():
                bag[item_id]['items_by_resolution'][resolution] += quantity
                messages.success(
                    request,
                    f'Updated {resolution.upper()} resolution quantity for'
                    f' {product.name}',
                    extra_tags='show_bag_in_toast'
                )
            else:
                bag[item_id]['items_by_resolution'][resolution] = quantity
                messages.success(
                    request,
                    f'{resolution.upper()} resolution for {product.name} '
                    'added to the bag',
                    extra_tags='show_bag_in_toast'
                )
        else:
            bag[item_id] = {'items_by_resolution': {resolution: quantity}}
            messages.success(
                request,
                f'{resolution.upper()} resolution for {product.name} '
                'added to the bag',
                extra_tags='show_bag_in_toast'
            )

    # If product does not have resolution, just add it according to
    # user's request.
    # Alert user with Django message.
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}'
            )
        else:
            bag[item_id] = quantity
            messages.success(request, f'{product.name} added to the bag')

    # Add bag to current session
    request.session['bag'] = bag

    return redirect(redirect_url)


# View for updating the bag
def adjust_bag(request, item_id):
    """Adjust the quantity of items in the purchasing bag

    Parameters In: HTTP request object, product ID

    Parameters Out: HttpResponse onbject (200)
    """

    # Assing none to resolution in case the product does not contain it
    resolution = None

    # If not HTML request, it is AJAX request
    requested_html = re.search(r'^text/html',
                               request.META.get('HTTP_ACCEPT')
                               )

    if not requested_html:
        # Just check that AJAX post does not add "\n" at the end (last
        # character) is an "n", remember AJAX post inclue quotes ("") so
        # first and last characters need to be removed ([1:1] below)
        if (json.dumps(request.POST.get('resolution'))[-2].lower() == 'n'):
            resolution = json.dumps(request.POST.get(
                'resolution'))[1:-3].lower()
        else:
            resolution = json.dumps(request.POST.get(
                'resolution'))[1:-1].lower()
        ajax_id = json.dumps(request.POST.get('itemId'))[1:-1]
        quantity = int(json.dumps(request.POST.get('quantity'))[1:-1])
        product = get_object_or_404(Product, pk=ajax_id)

    # Read bag content if not from AJAX
    else:
        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST.get('quantity'))

    # Get current session bag
    bag = request.session.get('bag', {})

    # Check if product to update has resolution and read it
    # if not from AJAX
    if 'product_resolution' in request.POST:
        resolution = request.POST['product_resolution'].lower()

    # Check if product has resolution and consider it as a product (to be
    # updated) if requested by user.
    # Alert user with Django message.

    if (resolution.lower() == 'high' or resolution.lower() == 'medium' or
            resolution.lower() == 'low'):
        if quantity > 0:
            bag[item_id]['items_by_resolution'][resolution] = quantity
            messages.success(
                request,
                f'Updated {resolution.upper()} resolution quantity for '
                f'{product.name}',
                extra_tags='show_bag_in_toast'
            )
        else:
            del bag[item_id]['items_by_resolution'][resolution]
            if not bag[item_id]['items_by_resolution']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed {resolution.upper()} resolution for '
                f'{product.name} from the bag',
                extra_tags='show_bag_in_toast'
            )

    # If product does not have resolution, just update it according to
    # user's request.
    # Alert user with Django message.
    else:
        if quantity > 0:

            bag[item_id] = quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {product.name}',
                extra_tags='show_bag_in_toast'
            )

        else:
            bag.pop(item_id)
            messages.success(
                request,
                f'{product.name} removed from the bag',
                extra_tags='show_bag_in_toast'
            )

    # Update bag to current session
    request.session['bag'] = bag

    return HttpResponse(status=200)


def remove_from_bag(request, item_id):
    """Remove items from the purchasing bag

    Parameters In: HTTP request object, product ID

    Parameters Out: HttpResponse (200 or 500)

    """
    # Read resolution and product ID to delete
    resolution = json.dumps(request.POST.get('resolution'))[1:-1].lower()
    ajax_id = json.dumps(request.POST.get('itemId'))[1:-1]
    item_id = ajax_id

    # Remove product or inform user
    try:
        product = get_object_or_404(Product, pk=item_id)

        # Get current session bag
        bag = request.session.get('bag', {})

        # Check if product has resolution.
        # Alert user with Django message.
        if (resolution == 'low' or resolution == 'medium' or
                resolution == 'high'):

            del bag[item_id]['items_by_resolution'][resolution]
            if not bag[item_id]['items_by_resolution']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed {resolution.upper()} resolution'
                f' for {product.name} from the bag',
                extra_tags='show_bag_in_toast'
            )

        # If product does not have resolution, just delete it according to
        # user's request.
        # Alert user with Django message.
        else:
            bag.pop(item_id)
            messages.success(
                request,
                f'{product.name} removed from the bag',
                extra_tags='show_bag_in_toast'
            )

        # Update bag to current session
        request.session['bag'] = bag

        return HttpResponse(status=200)

    # Show an error if item cannot be removed.
    # Alert user with Django message.
    except Exception as e:
        messages.error(request, f'Error removing item_ {e}')
        return HttpResponse(status=500)
