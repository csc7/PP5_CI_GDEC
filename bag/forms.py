from django import forms

class DownloadAndCancelDeliveryCost(forms.Form):
    repeat=forms.BooleanField(required=False)