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
# Import Lower function;
# https://stackoverflow.com/questions/31734993/lowercase-django-query,
# accessed on March 15th, 2022, at 11:55
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# INTERNAL:
from .models import Product, Category, ProductComment
from .forms import ProductForm, ProductCommentForm

###############################################################################


def all_products(request):
    """View for all products

    Parameters In: HTTP request object

    Parameters Out: request object, template (products/products.html),
    context variables:
        'products',
        'filter_char',
        'search_term',
        'current_categories',
        'current_sorting',
        'title_in_body',
        'category_in_title_url',
        'page_obj'
    """

    # Read product model and initialise search options
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

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # Read the first category and assign the corresponding product group
    # title (based on top navigation menu). If no categories, then the
    # query is for all products
    if (categories is None):
        title = "All Products"
        title_url = "?sort=name&direction=asc"

    else:
        if (str(categories.first()) == 'dem' or
                str(categories.first()) == 'gravimetry' or
                str(categories.first()) == 'magnetometry' or
                str(categories.first()) == 'resistivity'):
            title = "Digital Data"
            title_url = "?category=dem,gravimetry,magnetometry,resistivity"
        elif (str(categories.first()) == 'eia' or
                str(categories.first()) == 'weather' or
                str(categories.first()) == 'geological_maps'):
            title = "Reports"
            title_url = "?category=eia,geological_maps,weather"
        elif (str(categories.first()) == 'courses' or
                str(categories.first()) == 'books'):
            title = "Training"
            title_url = "?category=courses,books"
        elif (str(categories.first()) == 'simulators' or
                str(categories.first()) == 'data_processing' or
                str(categories.first()) == 'data_qc'):
            title = "Software"
            title_url = "?category=simulators,data_processing,data_qc"
        elif (str(categories.first()) == 'data_offers' or
                str(categories.first()) == 'software_offers' or
                str(categories.first()) == 'training_offers' or
                str(categories.first()) == 'report_offers'):
            title = "Offers"
            title_url = "?category=data_offers,report_offers,"\
                "training_offers,software_offers"
        else:
            title = "All Products"
            title_url = "?sort=name&direction=asc"

    # Pagination
    page_obj, products = pagination(request, products)

    # Context to return
    context = {
        'products': products,
        'filter_char': "?",
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'title_in_body': title,
        'category_in_title_url': title_url,
        'page_obj': page_obj,
    }

    return render(request, 'products/products.html', context)


def pagination(request, items):
    """View for all products

    Parameters In: HTTP request object, selected products
    for Django pagination

    Parameters Out: page object with selected products paginated
    """

    # Pagination by Django Documentaiton:
    # https://docs.djangoproject.com/en/4.0/topics/pagination/,
    # accessed on April 15th, 2022, at 2:00
    page_number = request.GET.get('page')
    paginator = Paginator(items, 12)  # Show 12 contacts per page.

    page_obj = paginator.get_page(page_number)

    # By Vitor Freitas, "paginator.page(page)", missing line for proper
    # pagination, and option to address no integers,
    # https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html
    # accessed on April 15th, 2022, at 2:00
    try:
        items = paginator.page(page_number)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return (page_obj, items)


def product_detail(request, product_id):
    """View for details of a product"""

    product = get_object_or_404(Product, pk=product_id)

    comments = ProductComment.objects.filter(product=product,
                                             active=True)

    product.rating = compute_product_rating_value(product_id)
    product.save()

    user_has_commented = False

    if (request.user.is_authenticated):
        if(ProductComment.objects.filter(product=product, user=request.user,
                                         active=True) or request.user is None):
            user_has_commented = True

    comment_form = ProductCommentForm(request.POST)

    context = {
        'product': product,
        'comments': comments,
        'comment_form': comment_form,
        'user_has_commented': user_has_commented,
    }

    return render(request, 'products/product_detail.html', context)


# Use Django login decorator to access this view
@login_required()
def add_product(request):
    """ Add products to the store

    Parameters In: HTTP request object

    Parameters Out: request object, template (products/add_product.html),
    context variables:
        'form'
    """

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
            messages.error(
                request,
                'Failed to edit product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'

    context = {
        'form': form,
        'product': product,
        'do_not_show_bag_in_toast': True,
    }

    return render(request, template, context)


# Use Django login decorator to access this view
@login_required()
def delete_product(request, product_id):
    """ Delete products of the store

    Parameters In: HTTP request object, product ID

    Parameters Out: request object, redirect(reverse) URL to products
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')

    return redirect(reverse('products'))

# To add a comment feature:
# copied and modified (except computation of product rating)
# from https://djangocentral.com/creating-comments-system-with-django/,
# Abhijeet Pal, Author and Editor in Chief @djangocentral,
# on April 12th, 2022.


def product_review(request, product_id):
    """
    Function to show product reviews

    Parameters In: HTTP request object, product ID

    Parameters Out: request object, redirect(reverse) URL to product details
    of product being commented
    """

    new_comment = None

    # Comment posted
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        comments = ProductComment.objects.filter(product=product,
                                                 active=True)

        # Read comment form
        comment_form = ProductCommentForm(request.POST)

        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product

            # Save user that is commenting
            new_comment.user = request.user

            # Save the comment to the database
            new_comment.save()

            context = {
                'product': product,
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
    """ Delete comment from product detilas

    Parameters In: HTTP request object, product ID, comment ID

    Parameters Out: request object, redirect(reverse) URL to product details
    of product being commented
    """

    product = get_object_or_404(Product, pk=product_id)
    comments = ProductComment.objects.filter(product=product,
                                             active=True)

    # Check if user is superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('product_detail', args=[product_id]))

    comment_to_delete = get_object_or_404(ProductComment, pk=comment_id)
    comment_to_delete.delete()

    product.rating = compute_product_rating_value(product_id)
    product.save()

    messages.success(request, 'Comment deleted!')

    return redirect(reverse('product_detail', args=[product_id]))


# Compute Product Rating Value
def compute_product_rating_value(product_id):
    """
    This function computes the product rating value
    for each product

    Parameters In: product ID

    Parameters Out: product updated rate
    """

    # Read product and all comments
    product = get_object_or_404(Product, pk=product_id)
    comments = ProductComment.objects.filter(
        product=product,
        active=True
    )

    # Compute udated rate
    rate = 0
    i = 0
    for comment in comments:
        rate = rate + (comment.product_rating_value)
        i = i+1
    if i == 0:
        rate = product.rating  # If no comments, read default
    else:
        rate = rate/i

    return (rate)
