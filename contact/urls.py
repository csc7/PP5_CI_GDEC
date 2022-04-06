###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.urls import include, path

# INTERNAL:
from contact import views

###############################################################################


# Code copied from Code Institute "I Think Therefore I Blog" project
# on December 20th, 2022 at 18:09, later modified.


urlpatterns = [
    path("", views.get_contact_page, name="contact"),
    path("thanks/", views.get_thanks_page, name="thanks"),
]