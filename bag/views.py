from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_bag(request):
    """View for the purchasing bag"""

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add items to the purchasing bag """

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
            else:
                bag[item_id]['items_by_resolution'][resolution] = quantity
        else:
            bag[item_id] = {'items_by_resolution': {resolution: quantity}}


    else:

        if item_id in list(bag.keys()):
            bag[item_id] += quantity

        else:
            bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """Adjust the quantity of items in the purchasing bag"""

    quantity = int(request.POST.get('quantity'))
    resolution = None
    if 'product_resolution' in request.POST:
        resolution = request.POST['product_resolution']
    bag = request.session.get('bag', {})

    if resolution:
        if quantity > 0:
            bag[item_id]['items_by_resolution'][resolution] = quantity
        else:
            del bag[item_id]['items_by_resolution'][resolution]
            if not bag[item_id]['items_by_resolution']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove items from the purchasing bag"""

    try:
        resolution = None
        if 'product_resolution' in request.POST:
            resolution = request.POST['product_resolution']
        bag = request.session.get('bag', {})

        if resolution:
            del bag[item_id]['items_by_resolution'][resolution]
            if not bag[item_id]['items_by_resolution']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)