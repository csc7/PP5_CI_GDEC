###############################################################################

"""
Django views for the products app
"""

###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
# Import Lower function; https://stackoverflow.com/questions/31734993/lowercase-django-query, accessed on March 15th, 2022, at 11:55
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

# INTERNAL:
from .models import Product, Category, ProductComment
from .forms import ProductForm, ProductCommentForm

###############################################################################


def all_products(request):
    """View for all products"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    # Check if there is a request to select products
    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
    

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,

    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """View for details of a product"""

    product = get_object_or_404(Product, pk=product_id)

    comments = ProductComment.objects.filter(product=product,
                                             active=True)

    comment_form = ProductCommentForm(request.POST)

    context = {
        'product': product,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'products/product_detail.html', context)


# Use Django login decorator to access this view
@login_required()
def add_product(request):
    """ Add products to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # If method is post, instantiate a product form, accepting images with
    # request.FILES
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product successfully added!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure \
                the form is valid.')
    # Otherwise, instantiate a blank form
    else:
        form = ProductForm()

    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# Use Django login decorator to access this view
@login_required()
def edit_product(request, product_id):
    """ Edit products of the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Prefill the form
    product = get_object_or_404(Product, pk=product_id)
    # Instantiate the form if method is POST
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to edit product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'

    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


# Use Django login decorator to access this view
@login_required()
def delete_product(request, product_id):
    """ Delete products of the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')

    

    return redirect(reverse('products'))


# modified from https://djangocentral.com/creating-comments-system-with-django/
def product_review(request, product_id):
    """
    Function
    """
    #template_name = 'products/product_detail.html'
    #product = get_object_or_404(Product, pk=product_id)
    #comments = ProductComment.objects.filter(product=product,
    #                                         active=True)
    new_comment = None

    # Comment posted
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        comments = ProductComment.objects.filter(product=product,
                                                 active=True)
        comment_form = ProductCommentForm(request.POST)

        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            # Save the comment to the database
            new_comment.save()

            context = {'product': product,
                       'comments': comments,
                       'new_comment': new_comment,
                       'comment_form': comment_form,
            }
            messages.success(request, 'Comment sent!')
            return render(request, 'products/product_detail.html', context)

        else:
            messages.error(request, 'Sorry, comment could not be sent')

    else:
            messages.error(request, 'Sorry, comment could not be sent')

    return redirect(reverse('product_detail', args=[product_id]))


# Use Django login decorator to access this view
@login_required()
def delete_product_review(request, product_id, comment_id):
    """ Delete comment from product detilas """
    product = get_object_or_404(Product, pk=product_id)
    comments = ProductComment.objects.filter(product=product,
                                                 active=True)

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('product_detail', args=[product_id]))

    comment_to_delete = get_object_or_404(ProductComment, pk=comment_id)
    comment_to_delete.delete()
    #messages.success(request, 'Comment deleted!')
   
    return redirect(reverse('product_detail', args=[product_id]))