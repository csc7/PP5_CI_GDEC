###############################################################################

# IMPORTED RESOURCES #

# EXTERNAL:
from django.db import models

###############################################################################


class DataFromContactForm(models.Model):
    """
    A contact form class for the data of the contact form
    Primary key (id field) automatically added my Django
    """
    date = models.DateField(max_length=200)
    time = models.TimeField(default="00:00:00", max_length=200)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    description = models.TextField(max_length=2000)

    def __str__(self):
        return f"Contact form from {self.full_name}"