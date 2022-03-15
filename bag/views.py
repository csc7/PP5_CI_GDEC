from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """View for the purchasing bag"""

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add items to the shopping bag """

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