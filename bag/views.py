from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """View for the purchasing bag"""

    return render(request, 'bag/bag.html')
