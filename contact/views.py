###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render

# INTERNAL:
from .models import DataFromContactForm
from .forms import ContactForm

###############################################################################


# Reference: Django Project.
# https://docs.djangoproject.com/en/4.0/topics/forms/


def get_contact_page(request):
    """
    View for the Contact page
    Process of contact form
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            record = DataFromContactForm(date = datetime.datetime.now().date(),
                                         time = datetime.datetime.now().time(),
                                         full_name = form.cleaned_data['full_name'],
                                         email = form.cleaned_data['email'],
                                         text_content = form.cleaned_data[
                                             'text_content']
                                        )
            record.save()
            # redirect to a new URL:

            return HttpResponseRedirect('thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


def get_thanks_page(request):
    """
    View for "thank-you" page after sending a contact form
    """
    context = {
                'form_data': DataFromContactForm.objects.all().order_by('-id')[0]
              }   
    return render(request, 'thanks.html', context)